import asyncio
import json
from enum import Enum
from typing import Callable, Dict, List, Optional, Any
import websockets
from websockets.exceptions import ConnectionClosed, WebSocketException

from backend.domains.kiwoom.managers.kiwoom_token_manager import KiwoomTokenManager
from backend.core.logger import get_logger

logger = get_logger(__name__)


class MessageType(Enum):
    """웹소켓 메시지 타입 정의"""
    LOGIN = "LOGIN"
    PING = "PING"
    REGISTER = "REG"
    REMOVE = "REMOVE"
    UNKNOWN = "UNKNOWN"


class ConnectionState(Enum):
    """연결 상태 정의"""
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    RECONNECTING = "reconnecting"


class KiwoomWsClient:
    """키움 웹소켓 클라이언트"""
    
    def __init__(
        self, 
        uri: str = 'wss://api.kiwoom.com:10000/api/dostk/websocket',
        token_manager: Optional[KiwoomTokenManager] = None,
        reconnect_interval: int = 5,
        max_reconnect_attempts: int = 3
    ):
        self.uri = uri
        self.token_manager = token_manager
        self.reconnect_interval = reconnect_interval
        self.max_reconnect_attempts = max_reconnect_attempts
        
        # 연결 관련 상태
        self.websocket: Optional[websockets.WebSocketServerProtocol] = None
        self.connection_state = ConnectionState.DISCONNECTED
        self.keep_running = True
        self.reconnect_attempts = 0
        
        # 핸들러 관리
        self.handlers: Dict[str, Callable] = {}
        
        # 등록된 그룹 관리
        self.registered_groups: Dict[str, Dict[str, Any]] = {}

    @property
    def is_connected(self) -> bool:
        """연결 상태 확인"""
        return (
            self.connection_state == ConnectionState.CONNECTED 
            and self.websocket is not None 
            and not self.websocket.closed
        )

    async def connect(self) -> bool:
        """웹소켓 서버에 연결"""
        if not self.token_manager:
            logger.error("토큰 매니저가 설정되지 않았습니다.")
            return False

        try:
            self.connection_state = ConnectionState.CONNECTING
            logger.info("키움 웹소켓 서버 연결을 시도합니다.")
            
            # 토큰 획득
            token = await self.token_manager.get_token()
            if not token:
                logger.error("토큰을 획득할 수 없습니다.")
                return False

            # 웹소켓 연결
            self.websocket = await websockets.connect(self.uri)
            
            # 로그인 메시지 전송
            login_msg = {
                'trnm': MessageType.LOGIN.value,
                'token': token
            }
            
            await self._send_raw_message(login_msg)
            logger.info('로그인 패킷을 전송했습니다.')
            
            return True
            
        except WebSocketException as e:
            logger.error(f'웹소켓 연결 오류: {e}')
            self.connection_state = ConnectionState.DISCONNECTED
            return False
        except Exception as e:
            logger.error(f'연결 중 예상치 못한 오류: {e}')
            self.connection_state = ConnectionState.DISCONNECTED
            return False

    async def _send_raw_message(self, message: Dict[str, Any]) -> bool:
        """원시 메시지 전송 (내부용)"""
        if not self.websocket:
            return False
            
        try:
            message_str = json.dumps(message, ensure_ascii=False)
            await self.websocket.send(message_str)
            logger.debug(f'메시지 전송: {message_str}')
            return True
        except Exception as e:
            logger.error(f'메시지 전송 실패: {e}')
            return False

    async def send_message(self, message: Dict[str, Any]) -> bool:
        """메시지 전송 (재연결 포함)"""
        if not self.is_connected:
            if not await self._reconnect():
                return False
                
        return await self._send_raw_message(message)

    async def _handle_login_response(self, response: Dict[str, Any]) -> None:
        """로그인 응답 처리"""
        return_code = response.get('return_code', -1)
        return_msg = response.get('return_msg', 'Unknown error')
        
        if return_code != 0:
            logger.error(f'웹소켓 로그인 실패: {return_msg}')
            self.connection_state = ConnectionState.DISCONNECTED
            await self.disconnect()
        else:
            logger.info('웹소켓 로그인 성공')
            self.connection_state = ConnectionState.CONNECTED
            self.reconnect_attempts = 0
            
            # 기존 등록 그룹 재등록
            await self._reregister_groups()

    async def _handle_ping(self, response: Dict[str, Any]) -> None:
        """PING 메시지 처리 (PONG 응답)"""
        await self._send_raw_message(response)
        logger.debug('PING에 대한 PONG 응답 전송')

    async def _handle_data_message(self, response: Dict[str, Any]) -> None:
        """데이터 메시지 처리"""
        trnm = response.get('trnm')
        data_list = response.get('data', [])
        
        if not isinstance(data_list, list):
            logger.warning(f"데이터가 리스트 형태가 아닙니다: {response}")
            return
            
        for data in data_list:
            try:
                data_type = data.get('type')
                if data_type and data_type in self.handlers:
                    await self.handlers[data_type](data)
                else:
                    logger.debug(f"핸들러가 없는 데이터 타입: {data_type}")
            except Exception as e:
                logger.error(f"데이터 처리 중 오류: {e}, 데이터: {data}")

    async def receive_messages(self) -> None:
        """메시지 수신 루프"""
        while self.keep_running:
            try:
                if not self.websocket:
                    await asyncio.sleep(1)
                    continue
                    
                message = await self.websocket.recv()
                response = json.loads(message)
                trnm = response.get('trnm', MessageType.UNKNOWN.value)
                
                logger.debug(f'메시지 수신: {trnm}')
                
                # 메시지 타입별 처리
                if trnm == MessageType.LOGIN.value:
                    await self._handle_login_response(response)
                elif trnm == MessageType.PING.value:
                    await self._handle_ping(response)
                elif trnm == MessageType.UNKNOWN.value:
                    logger.warning(f'알 수 없는 메시지: {response}')
                else:
                    await self._handle_data_message(response)
                    
            except ConnectionClosed:
                logger.warning('웹소켓 연결이 종료되었습니다.')
                self.connection_state = ConnectionState.DISCONNECTED
                if self.keep_running:
                    await self._reconnect()
                break
            except json.JSONDecodeError as e:
                logger.error(f'JSON 파싱 오류: {e}')
            except Exception as e:
                logger.error(f'메시지 수신 중 오류: {e}')
                await asyncio.sleep(1)

    async def register(
        self, 
        grp_no: str, 
        item_list: List[str], 
        type_list: List[str]
    ) -> bool:
        """실시간 데이터 등록"""
        message = {
            "trnm": MessageType.REGISTER.value,
            "grp_no": grp_no,
            "refresh": "1",
            "data": [{
                "item": item_list,
                "type": type_list
            }]
        }
        
        # 등록 정보 저장 (재연결 시 사용)
        self.registered_groups[grp_no] = {
            "item_list": item_list,
            "type_list": type_list
        }
        
        success = await self.send_message(message)
        if success:
            logger.info(f'그룹 {grp_no} 등록 요청 전송')
        return success

    async def unregister(self, grp_no: str) -> bool:
        """실시간 데이터 등록 해제"""
        message = {
            "trnm": MessageType.REMOVE.value,
            "grp_no": grp_no
        }
        
        # 등록 정보에서 제거
        self.registered_groups.pop(grp_no, None)
        
        success = await self.send_message(message)
        if success:
            logger.info(f'그룹 {grp_no} 등록 해제 요청 전송')
        return success

    async def _reregister_groups(self) -> None:
        """재연결 시 기존 그룹 재등록"""
        if not self.registered_groups:
            return
            
        logger.info('기존 등록 그룹 재등록 시작')
        for grp_no, group_info in self.registered_groups.items():
            await self.register(
                grp_no, 
                group_info["item_list"], 
                group_info["type_list"]
            )

    def add_handler(self, msg_type: str, handler: Callable) -> None:
        """실시간 메시지 핸들러 등록"""
        if not asyncio.iscoroutinefunction(handler):
            logger.warning(f"핸들러 {msg_type}가 async 함수가 아닙니다.")
        self.handlers[msg_type] = handler
        logger.info(f'핸들러 등록: {msg_type}')

    def remove_handler(self, msg_type: str) -> None:
        """핸들러 제거"""
        if msg_type in self.handlers:
            del self.handlers[msg_type]
            logger.info(f'핸들러 제거: {msg_type}')

    async def _reconnect(self) -> bool:
        """재연결 시도"""
        if self.reconnect_attempts >= self.max_reconnect_attempts:
            logger.error('최대 재연결 시도 횟수를 초과했습니다.')
            return False
            
        self.connection_state = ConnectionState.RECONNECTING
        self.reconnect_attempts += 1
        
        logger.info(f'재연결 시도 {self.reconnect_attempts}/{self.max_reconnect_attempts}')
        
        await asyncio.sleep(self.reconnect_interval)
        return await self.connect()

    async def run(self) -> None:
        """클라이언트 실행"""
        logger.info('키움 웹소켓 클라이언트 시작')
        
        if await self.connect():
            await self.receive_messages()
        else:
            logger.error('초기 연결에 실패했습니다.')

    async def disconnect(self) -> None:
        """연결 종료"""
        logger.info('연결 종료 시작')
        self.keep_running = False
        self.connection_state = ConnectionState.DISCONNECTED
        
        if self.websocket and not self.websocket.closed:
            await self.websocket.close()
            
        self.websocket = None
        logger.info('연결이 종료되었습니다.')

    async def __aenter__(self):
        """async context manager 진입"""
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """async context manager 종료"""
        await self.disconnect()


# 사용 예시
async def example_usage():
    """사용 예시"""
    token_manager = KiwoomTokenManager()
    
    async with KiwoomWsClient(token_manager=token_manager) as client:
        # 핸들러 등록
        async def price_handler(data):
            print(f"가격 데이터: {data}")
            
        client.add_handler("price", price_handler)
        
        # 실시간 데이터 등록
        await client.register("group1", ["005930"], ["price"])
        
        # 메시지 수신
        await client.receive_messages()