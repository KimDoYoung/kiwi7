"""
KIS(한국투자증권) WebSocket 클라이언트
실시간 시세, 호가, 체결통보를 수신합니다.
"""
import json
import asyncio
from typing import Callable, Dict, Optional
import websockets

from backend.domains.kis.managers.kis_token_manager import KisTokenManager
from backend.core.config import config
from backend.core.exceptions import KisApiException
from backend.core.logger import get_logger

logger = get_logger(__name__)


class KisWsClient:
    """한국투자증권 WebSocket 클라이언트"""

    # 실시간 TR 타입
    TR_TYPES = {
        'H0STCNT0': '주식체결',
        'H0STASP0': '주식호가',
        'H0STCNI0': '체결통보(실전)',
        'H0STCNI9': '체결통보(모의)',
    }

    def __init__(self, token_manager: KisTokenManager = None):
        self.token_manager = token_manager
        self.uri = config.KIS_WS_URL
        self.is_virtual = config.KIS_IS_VIRTUAL

        self.websocket = None
        self.connected = False
        self.keep_running = True
        self.handlers: Dict[str, Callable] = {}

        # WebSocket 접속용 승인키
        self.approval_key: Optional[str] = None

    async def connect(self):
        """WebSocket 연결"""
        try:
            # 승인키 발급
            self.approval_key = await self.token_manager.get_approval_key()
            if not self.approval_key:
                raise KisApiException("WebSocket 승인키 발급 실패")

            # WebSocket 연결
            self.websocket = await websockets.connect(self.uri, ping_interval=None)
            self.connected = True
            logger.info(f"[KIS] WebSocket 연결 성공: {self.uri}")

        except Exception as e:
            logger.error(f"[KIS] WebSocket 연결 오류: {e}")
            self.connected = False
            raise KisApiException(f"WebSocket 연결 실패: {e}")

    async def disconnect(self):
        """WebSocket 연결 해제"""
        self.keep_running = False
        if self.connected and self.websocket:
            await self.websocket.close()
            self.connected = False
            logger.info("[KIS] WebSocket 연결 종료")

    async def send_message(self, message: dict):
        """메시지 전송"""
        if not self.connected:
            await self.connect()

        if self.connected:
            msg_str = json.dumps(message)
            await self.websocket.send(msg_str)
            logger.debug(f"[KIS] 메시지 전송: {msg_str[:100]}...")

    async def subscribe(self, stock_code: str, tr_type: str = 'H0STCNT0'):
        """실시간 데이터 구독

        Args:
            stock_code: 종목코드 (6자리)
            tr_type: TR 타입
                - H0STCNT0: 주식체결
                - H0STASP0: 주식호가
                - H0STCNI0: 체결통보(실전)
                - H0STCNI9: 체결통보(모의)
        """
        message = {
            'header': {
                'approval_key': self.approval_key,
                'custtype': 'P',  # 개인
                'tr_type': '1',   # 1: 등록
                'content-type': 'utf-8',
            },
            'body': {
                'input': {
                    'tr_id': tr_type,
                    'tr_key': stock_code,
                }
            }
        }
        await self.send_message(message)
        logger.info(f"[KIS] 실시간 구독: {tr_type}({self.TR_TYPES.get(tr_type, '')}) - {stock_code}")

    async def unsubscribe(self, stock_code: str, tr_type: str = 'H0STCNT0'):
        """실시간 데이터 구독 해제"""
        message = {
            'header': {
                'approval_key': self.approval_key,
                'custtype': 'P',
                'tr_type': '2',   # 2: 해제
                'content-type': 'utf-8',
            },
            'body': {
                'input': {
                    'tr_id': tr_type,
                    'tr_key': stock_code,
                }
            }
        }
        await self.send_message(message)
        logger.info(f"[KIS] 실시간 해제: {tr_type} - {stock_code}")

    def add_handler(self, tr_type: str, handler: Callable):
        """메시지 핸들러 등록

        Args:
            tr_type: TR 타입 (H0STCNT0, H0STASP0, H0STCNI0 등)
            handler: 콜백 함수 (async def handler(data: dict))
        """
        self.handlers[tr_type] = handler
        logger.info(f"[KIS] 핸들러 등록: {tr_type}")

    def remove_handler(self, tr_type: str):
        """메시지 핸들러 제거"""
        if tr_type in self.handlers:
            del self.handlers[tr_type]
            logger.info(f"[KIS] 핸들러 제거: {tr_type}")

    async def receive_messages(self):
        """메시지 수신 루프"""
        while self.keep_running:
            try:
                raw = await self.websocket.recv()

                # JSON 형식인지 확인
                if raw.startswith('{'):
                    await self._handle_json_message(raw)
                else:
                    # 바이너리/파이프 구분 데이터
                    await self._handle_realtime_data(raw)

            except websockets.ConnectionClosed as e:
                logger.warning(f"[KIS] WebSocket 연결 종료: {e}")
                self.connected = False
                break
            except Exception as e:
                logger.error(f"[KIS] 메시지 수신 오류: {e}")

    async def _handle_json_message(self, raw: str):
        """JSON 형식 메시지 처리"""
        try:
            data = json.loads(raw)
            header = data.get('header', {})
            tr_id = header.get('tr_id', '')

            # PINGPONG 처리
            if tr_id == 'PINGPONG':
                await self.send_message(data)
                return

            # 등록/해제 응답 처리
            body = data.get('body', {})
            if 'rt_cd' in body:
                rt_cd = body.get('rt_cd')
                msg1 = body.get('msg1', '')
                if rt_cd == '0':
                    logger.info(f"[KIS] 구독 성공: {msg1}")
                else:
                    logger.warning(f"[KIS] 구독 실패: {msg1}")

        except json.JSONDecodeError as e:
            logger.error(f"[KIS] JSON 파싱 오류: {e}")

    async def _handle_realtime_data(self, raw: str):
        """실시간 데이터 처리 (파이프 구분자 형식)"""
        # 형식: 암호화여부|TR_ID|데이터건수|데이터
        parts = raw.split('|')
        if len(parts) < 4:
            return

        encrypted = parts[0]
        tr_id = parts[1]
        data_count = int(parts[2])
        data = parts[3]

        # 핸들러 호출
        if tr_id in self.handlers:
            parsed_data = self._parse_realtime_data(tr_id, data)
            await self.handlers[tr_id]({
                'tr_id': tr_id,
                'encrypted': encrypted,
                'count': data_count,
                'raw': data,
                'parsed': parsed_data
            })
        else:
            logger.debug(f"[KIS] 미등록 TR: {tr_id}")

    def _parse_realtime_data(self, tr_id: str, data: str) -> dict:
        """실시간 데이터 파싱"""
        # 데이터는 ^ 구분자로 필드 구분
        fields = data.split('^')

        if tr_id == 'H0STCNT0':  # 주식체결
            return self._parse_stock_ccnl(fields)
        elif tr_id == 'H0STASP0':  # 주식호가
            return self._parse_stock_hoga(fields)
        elif tr_id in ['H0STCNI0', 'H0STCNI9']:  # 체결통보
            return self._parse_order_ccnl(fields)

        return {'fields': fields}

    def _parse_stock_ccnl(self, fields: list) -> dict:
        """주식체결 데이터 파싱"""
        if len(fields) < 20:
            return {'fields': fields}

        return {
            'stock_code': fields[0],       # 종목코드
            'time': fields[1],             # 체결시간
            'price': fields[2],            # 현재가
            'change_sign': fields[3],      # 전일대비부호
            'change': fields[4],           # 전일대비
            'change_rate': fields[5],      # 등락율
            'weighted_avg': fields[6],     # 가중평균가
            'open_price': fields[7],       # 시가
            'high_price': fields[8],       # 고가
            'low_price': fields[9],        # 저가
            'ask_price': fields[10],       # 매도호가1
            'bid_price': fields[11],       # 매수호가1
            'volume': fields[12],          # 체결량
            'acml_volume': fields[13],     # 누적거래량
            'acml_amount': fields[14],     # 누적거래대금
            'sell_volume': fields[15],     # 매도체결수량
            'buy_volume': fields[16],      # 매수체결수량
            'total_sell': fields[17],      # 총매도수량
            'total_buy': fields[18],       # 총매수수량
            'power': fields[19] if len(fields) > 19 else '',  # 체결강도
        }

    def _parse_stock_hoga(self, fields: list) -> dict:
        """주식호가 데이터 파싱"""
        if len(fields) < 40:
            return {'fields': fields}

        return {
            'stock_code': fields[0],
            'time': fields[1],
            'ask_prices': [fields[i] for i in range(3, 13)],      # 매도호가 1~10
            'bid_prices': [fields[i] for i in range(13, 23)],     # 매수호가 1~10
            'ask_volumes': [fields[i] for i in range(23, 33)],    # 매도호가잔량 1~10
            'bid_volumes': [fields[i] for i in range(33, 43)] if len(fields) > 42 else [],  # 매수호가잔량
        }

    def _parse_order_ccnl(self, fields: list) -> dict:
        """체결통보 데이터 파싱"""
        if len(fields) < 20:
            return {'fields': fields}

        return {
            'cust_id': fields[0],          # 고객ID
            'acct_no': fields[1],          # 계좌번호
            'order_no': fields[2],         # 주문번호
            'orgn_order_no': fields[3],    # 원주문번호
            'sell_buy': fields[4],         # 매도매수구분
            'order_type': fields[5],       # 주문구분
            'stock_code': fields[8],       # 종목코드
            'stock_name': fields[9],       # 종목명
            'order_qty': fields[10],       # 주문수량
            'order_price': fields[11],     # 주문가격
            'ccnl_qty': fields[13],        # 체결수량
            'ccnl_price': fields[14],      # 체결가격
            'ccnl_time': fields[17],       # 체결시간
        }

    async def run(self):
        """WebSocket 실행"""
        await self.connect()
        await self.receive_messages()
