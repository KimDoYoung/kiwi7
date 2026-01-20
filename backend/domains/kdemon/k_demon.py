import asyncio
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Optional

from backend.core.logger import get_logger
from backend.domains.stkcompanys.kiwoom.kiwoom_rest_api import KiwoomRestApi
from backend.domains.stkcompanys.kiwoom.managers.kiwoom_token_manager import KiwoomTokenManager

logger = get_logger(__name__)

def now_ymdhms() -> str:
    return datetime.now().strftime("%Y%m%d%H%M%S")

@dataclass
class Rule:
    id: int
    name: str
    symbol: str
    condition_op: str
    threshold: float
    action: str
    qty: int
    status: str
    cooldown_sec: int
    valid_from: Optional[str]
    valid_to: Optional[str]
    last_price: Optional[float]
    last_triggered_at: Optional[str]

class KDemon:
    """주기적으로 가격을 조회하고 룰을 평가해 주문을 실행하는 데몬."""
    _instance: "KDemon|None" = None

    def __init__(self, db_path: str, poll_interval_sec: int = 5, dry_run: bool = True):
        self.db_path = db_path
        self.poll_interval_sec = poll_interval_sec
        self.dry_run = dry_run  # True면 실제 주문 대신 로그만
        self._task: Optional[asyncio.Task] = None
        self._stop_event = asyncio.Event()
        self._refresh_event = asyncio.Event()
        self._rules: List[Rule] = []
        self._conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self.token_manager = KiwoomTokenManager()
        self._api = KiwoomRestApi(self.token_manager)

    # ---------- singleton ----------
    @classmethod
    def get(cls, db_path: str, poll_interval_sec: int = 5, dry_run: bool = True) -> "KDemon":
        if cls._instance is None:
            cls._instance = KDemon(db_path, poll_interval_sec, dry_run)
        return cls._instance

    # ---------- DB helpers ----------
    def _fetch_rules(self) -> List[Rule]:
        cur = self._conn.cursor()
        cur.execute("""
            SELECT * FROM kdemon_rules WHERE status='active'
        """)
        rules = []
        for r in cur.fetchall():
            rules.append(Rule(
                id=r["id"], name=r["name"], symbol=r["symbol"],
                condition_op=r["condition_op"], threshold=float(r["threshold"]),
                action=r["action"], qty=int(r["qty"]), status=r["status"],
                cooldown_sec=int(r["cooldown_sec"]),
                valid_from=r["valid_from"], valid_to=r["valid_to"],
                last_price=r["last_price"] if r["last_price"] is not None else None,
                last_triggered_at=r["last_triggered_at"]
            ))
        return rules

    def _update_rule_after_tick(self, rule: Rule, price: float, triggered: bool):
        cur = self._conn.cursor()
        if triggered:
            cur.execute("""
                UPDATE kdemon_rules
                   SET last_price=?, last_triggered_at=?
                 WHERE id=?
            """, (price, now_ymdhms(), rule.id))
        else:
            cur.execute("""
                UPDATE kdemon_rules
                   SET last_price=?
                 WHERE id=?
            """, (price, rule.id))
        self._conn.commit()

    def _set_state(self, status: str):
        cur = self._conn.cursor()
        cur.execute("""
            UPDATE kdemon_state
               SET status=?, updated_at=?
             WHERE id=1
        """, (status, now_ymdhms()))
        self._conn.commit()

    # ---------- Kiwoom helpers ----------
    async def _ensure_token(self):
        await self._api.refresh_token()

    async def _get_current_price(self, symbol: str) -> Optional[float]:
        """종목 현재가 조회. 실제 API id는 프로젝트에 맞춰 교체."""
        # 예시: 시세조회 API 아이디/페이로드는 환경에 맞게 조정
        req = {
            "api_id": "ka11001",         # <-- 실제 현재가/호가 API로 교체
            "cont_yn": "N",
            "next_key": "",
            "payload": {"stk_cd": symbol}
        }
        try:
            resp = await self._api.send_request(req)  # KiwoomStockApi는 dataclass 사용 중이면 맞춰 wrapping
            # 응답 구조에 맞게 파싱 (예: resp["output"]["현재가"])
            price = float(resp["output"]["현재가"])
            return price
        except Exception as e:
            logger.error(f"[kdemon] 현재가 조회 실패 {symbol}: {e}")
            return None

    async def _place_order(self, rule: Rule, price: float):
        """주문 실행. 실제 API/필드명은 환경에 맞게 교체."""
        if self.dry_run:
            logger.info(f"[kdemon] (DRY-RUN) {rule.action.upper()} {rule.qty} @ {price} / {rule.symbol} (rule:{rule.id})")
            return

        api_id = "ka20001"  # 예: 현금 매수/매도 API ID로 교체
        side = "01" if rule.action == "buy" else "02"  # 예) 01=매수, 02=매도(실제 문서 확인)
        req = {
            "api_id": api_id,
            "cont_yn": "N",
            "next_key": "",
            "payload": {
                "stk_cd": rule.symbol,
                "ord_qty": rule.qty,
                "ord_prc": price,      # 지정가/시장가 정책에 맞게 필드 조정
                "ord_dvsn": side,
            }
        }
        try:
            resp = await self._api.send_request(req)
            logger.info(f"[kdemon] 주문 성공 rule={rule.id}, resp={resp}")
        except Exception as e:
            logger.error(f"[kdemon] 주문 실패 rule={rule.id}: {e}")

    # ---------- rule evaluation ----------
    def _in_valid_window(self, rule: Rule) -> bool:
        now = now_ymdhms()
        if rule.valid_from and now < rule.valid_from:
            return False
        if rule.valid_to and now > rule.valid_to:
            return False
        return True

    def _cooldown_ok(self, rule: Rule) -> bool:
        if not rule.last_triggered_at:
            return True
        last = datetime.strptime(rule.last_triggered_at, "%Y%m%d%H%M%S")
        return datetime.now() >= (last + timedelta(seconds=rule.cooldown_sec))

    def _should_trigger(self, rule: Rule, price: float) -> bool:
        op = rule.condition_op
        th = rule.threshold
        lp = rule.last_price

        if op == "gte":
            return price >= th
        if op == "lte":
            return price <= th
        if op == "cross_up":
            return lp is not None and lp < th and price >= th
        if op == "cross_down":
            return lp is not None and lp > th and price <= th
        logger.warning(f"[kdemon] unknown condition_op: {op}")
        return False

    # ---------- control ----------
    async def start(self):
        if self._task and not self._task.done():
            logger.info("[kdemon] already running")
            return
        self._stop_event.clear()
        await self._ensure_token()
        self._rules = self._fetch_rules()
        self._set_state("running")
        self._task = asyncio.create_task(self._run())
        logger.info("[kdemon] started")

    async def stop(self):
        if not self._task:
            logger.info("[kdemon] not running")
            self._set_state("stopped")
            return
        self._stop_event.set()
        await self._task
        self._task = None
        self._set_state("stopped")
        logger.info("[kdemon] stopped")

    async def refresh(self):
        self._refresh_event.set()
        logger.info("[kdemon] refresh requested")

    async def _run(self):
        try:
            while not self._stop_event.is_set():
                # refresh?
                if self._refresh_event.is_set():
                    self._rules = self._fetch_rules()
                    self._refresh_event.clear()
                    logger.info(f"[kdemon] rules reloaded: {len(self._rules)}")

                # evaluate rules
                for rule in list(self._rules):
                    if self._stop_event.is_set():
                        break
                    if rule.status != "active":
                        continue
                    if not self._in_valid_window(rule):
                        continue
                    if not self._cooldown_ok(rule):
                        continue

                    price = await self._get_current_price(rule.symbol)
                    if price is None:
                        continue

                    triggered = self._should_trigger(rule, price)
                    if triggered:
                        await self._place_order(rule, price)
                        self._update_rule_after_tick(rule, price, True)
                        # 바로 상태 반영
                        rule.last_price = price
                        rule.last_triggered_at = now_ymdhms()
                    else:
                        self._update_rule_after_tick(rule, price, False)
                        rule.last_price = price

                await asyncio.sleep(self.poll_interval_sec)
        except asyncio.CancelledError:
            logger.info("[kdemon] task cancelled")
        except Exception as e:
            logger.exception(f"[kdemon] fatal error: {e}")
        finally:
            self._set_state("stopped")
