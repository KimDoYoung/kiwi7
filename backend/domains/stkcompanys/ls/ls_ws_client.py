"""
LS증권 WebSocket 클라이언트
실시간 시세, 호가, 체결통보를 수신합니다.
"""
import json
from typing import Callable, Dict
import websockets

from backend.domains.stkcompanys.ls.managers.ls_token_manager import LsTokenManager
from backend.core.config import config
from backend.core.exceptions import LsApiException
from backend.core.logger import get_logger

logger = get_logger(__name__)


class LsWsClient:
    """LS증권 WebSocket 클라이언트"""

    # 실시간 TR 타입
    TR_TYPES = {
        'SC0': '주식주문체결',
        'SC1': '주식주문정정',
        'SC2': '주식주문취소',
        'SC3': '주식주문거부',
        'S3_': '주식체결',
        'H1_': '주식호가잔량',
        'K3_': '주식KOSPI체결',
        'OK_': '주식KOSDAQ호가잔량',
    }

    def __init__(self, token_manager: LsTokenManager = None):
        self.token_manager = token_manager
        self.uri = config.LS_WS_URL
        # 실전 환경만 사용

        self.websocket = None
        self.connected = False
        self.keep_running = True
        self.handlers: Dict[str, Callable] = {}

    async def connect(self):
        """WebSocket 연결"""
        try:
            # 토큰 획득
            token = await self.token_manager.get_token()
            if not token:
                raise LsApiException("토큰 획득 실패")

            # WebSocket 연결
            self.websocket = await websockets.connect(self.uri, ping_interval=None)
            self.connected = True
            logger.info(f"[LS] WebSocket 연결 성공: {self.uri}")

            # 로그인 메시지 전송
            await self._send_login(token)

        except Exception as e:
            logger.error(f"[LS] WebSocket 연결 오류: {e}")
            self.connected = False
            raise LsApiException(f"WebSocket 연결 실패: {e}")

    async def _send_login(self, token: str):
        """로그인 메시지 전송"""
        login_msg = {
            'header': {
                'token': token,
                'tr_type': '1',  # 1: 등록
            },
            'body': {}
        }
        await self.send_message(login_msg)
        logger.info("[LS] WebSocket 로그인 메시지 전송")

    async def disconnect(self):
        """WebSocket 연결 해제"""
        self.keep_running = False
        if self.connected and self.websocket:
            await self.websocket.close()
            self.connected = False
            logger.info("[LS] WebSocket 연결 종료")

    async def send_message(self, message: dict):
        """메시지 전송"""
        if not self.connected:
            await self.connect()

        if self.connected:
            msg_str = json.dumps(message)
            await self.websocket.send(msg_str)
            logger.debug(f"[LS] 메시지 전송: {msg_str[:100]}...")

    async def subscribe(self, stock_code: str, tr_type: str = 'S3_'):
        """실시간 데이터 구독

        Args:
            stock_code: 종목코드 (6자리)
            tr_type: TR 타입
                - S3_: 주식체결
                - H1_: 주식호가잔량
                - SC0: 주식주문체결
        """
        message = {
            'header': {
                'tr_type': '1',   # 1: 등록
                'tr_cd': tr_type,
            },
            'body': {
                'tr_key': stock_code,
            }
        }
        await self.send_message(message)
        logger.info(f"[LS] 실시간 구독: {tr_type}({self.TR_TYPES.get(tr_type, '')}) - {stock_code}")

    async def unsubscribe(self, stock_code: str, tr_type: str = 'S3_'):
        """실시간 데이터 구독 해제"""
        message = {
            'header': {
                'tr_type': '2',   # 2: 해제
                'tr_cd': tr_type,
            },
            'body': {
                'tr_key': stock_code,
            }
        }
        await self.send_message(message)
        logger.info(f"[LS] 실시간 해제: {tr_type} - {stock_code}")

    def add_handler(self, tr_type: str, handler: Callable):
        """메시지 핸들러 등록

        Args:
            tr_type: TR 타입 (S3_, H1_, SC0 등)
            handler: 콜백 함수 (async def handler(data: dict))
        """
        self.handlers[tr_type] = handler
        logger.info(f"[LS] 핸들러 등록: {tr_type}")

    def remove_handler(self, tr_type: str):
        """메시지 핸들러 제거"""
        if tr_type in self.handlers:
            del self.handlers[tr_type]
            logger.info(f"[LS] 핸들러 제거: {tr_type}")

    async def receive_messages(self):
        """메시지 수신 루프"""
        while self.keep_running:
            try:
                raw = await self.websocket.recv()

                # JSON 파싱
                try:
                    data = json.loads(raw)
                    await self._handle_message(data)
                except json.JSONDecodeError:
                    # 바이너리 데이터 처리
                    await self._handle_binary_data(raw)

            except websockets.ConnectionClosed as e:
                logger.warning(f"[LS] WebSocket 연결 종료: {e}")
                self.connected = False
                break
            except Exception as e:
                logger.error(f"[LS] 메시지 수신 오류: {e}")

    async def _handle_message(self, data: dict):
        """JSON 메시지 처리"""
        header = data.get('header', {})
        tr_cd = header.get('tr_cd', '')

        # PING 응답
        if tr_cd == 'PINGPONG':
            await self.send_message(data)
            return

        # 등록/해제 응답
        body = data.get('body', {})
        if 'rsp_cd' in body:
            rsp_cd = body.get('rsp_cd')
            rsp_msg = body.get('rsp_msg', '')
            if rsp_cd == '0':
                logger.info(f"[LS] 구독 성공: {rsp_msg}")
            else:
                logger.warning(f"[LS] 구독 실패: {rsp_msg}")
            return

        # 실시간 데이터 처리
        if tr_cd in self.handlers:
            parsed = self._parse_realtime_data(tr_cd, body)
            await self.handlers[tr_cd]({
                'tr_cd': tr_cd,
                'raw': body,
                'parsed': parsed
            })
        else:
            logger.debug(f"[LS] 미등록 TR: {tr_cd}")

    async def _handle_binary_data(self, raw: bytes):
        """바이너리 데이터 처리"""
        logger.debug(f"[LS] 바이너리 데이터 수신: {len(raw)} bytes")

    def _parse_realtime_data(self, tr_cd: str, body: dict) -> dict:
        """실시간 데이터 파싱"""
        if tr_cd == 'S3_':  # 주식체결
            return self._parse_stock_ccnl(body)
        elif tr_cd == 'H1_':  # 주식호가
            return self._parse_stock_hoga(body)
        elif tr_cd.startswith('SC'):  # 주문체결통보
            return self._parse_order_ccnl(body)

        return body

    def _parse_stock_ccnl(self, body: dict) -> dict:
        """주식체결 데이터 파싱"""
        return {
            'stock_code': body.get('shcode', ''),
            'time': body.get('chetime', ''),
            'price': body.get('price', ''),
            'change_sign': body.get('sign', ''),
            'change': body.get('change', ''),
            'change_rate': body.get('drate', ''),
            'volume': body.get('cvolume', ''),
            'acml_volume': body.get('volume', ''),
            'acml_amount': body.get('value', ''),
            'open_price': body.get('open', ''),
            'high_price': body.get('high', ''),
            'low_price': body.get('low', ''),
        }

    def _parse_stock_hoga(self, body: dict) -> dict:
        """주식호가 데이터 파싱"""
        return {
            'stock_code': body.get('shcode', ''),
            'time': body.get('hotime', ''),
            'ask_prices': [
                body.get(f'offerho{i}', '') for i in range(1, 11)
            ],
            'bid_prices': [
                body.get(f'bidho{i}', '') for i in range(1, 11)
            ],
            'ask_volumes': [
                body.get(f'offerrem{i}', '') for i in range(1, 11)
            ],
            'bid_volumes': [
                body.get(f'bidrem{i}', '') for i in range(1, 11)
            ],
            'total_ask': body.get('totofferrem', ''),
            'total_bid': body.get('totbidrem', ''),
        }

    def _parse_order_ccnl(self, body: dict) -> dict:
        """주문체결통보 데이터 파싱"""
        return {
            'order_no': body.get('ordno', ''),
            'orgn_order_no': body.get('orgordno', ''),
            'stock_code': body.get('expcode', ''),
            'stock_name': body.get('hname', ''),
            'sell_buy': body.get('ordgb', ''),
            'order_qty': body.get('ordqty', ''),
            'order_price': body.get('ordprc', ''),
            'ccnl_qty': body.get('cheqty', ''),
            'ccnl_price': body.get('cheprc', ''),
            'ccnl_time': body.get('chetime', ''),
        }

    async def run(self):
        """WebSocket 실행"""
        await self.connect()
        await self.receive_messages()
