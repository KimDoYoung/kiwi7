from multiprocessing.util import get_logger
import websockets
import json
from typing import Callable

from backend.domains.kiwoom.managers.kiwwom_token_manager import KiwoomTokenManager

from backend.core.logger import get_logger
logger = get_logger(__name__)

class KiwoomWsClient:
    def __init__(self, uri: str = 'wss://api.kiwoom.com:10000/api/dostk/websocket', token_manager: KiwoomTokenManager = None):
        self.uri = uri
        self.token_manager = token_manager
        self.websocket = None
        self.connected = False
        self.keep_running = True
        self.handlers: dict[str, Callable] = {}

    async def connect(self):
        try:
            token = await self.token_manager.get_token()

            self.websocket = await websockets.connect(self.uri)
            self.connected = True
            logger.info("키움 웹소켓 서버와 연결을 시도 중입니다.")

            login_msg = {
                'trnm': 'LOGIN',
                'token': token
            }

            logger.info('실시간 웹소켓 서버로 로그인 패킷을 전송합니다.')
            await self.send_message(message=login_msg)

        except Exception as e:
            logger.error(f'Connection error: {e}')
            self.connected = False

    async def send_message(self, message):
        if not self.connected:
            await self.connect()
        if self.connected:
            if not isinstance(message, str):
                message = json.dumps(message)
            await self.websocket.send(message)
            logger.info(f'웹소켓 메세지를 키움서버로 전송했습니다: {message}')

    async def receive_messages(self):
        while self.keep_running:
            try:
                response = json.loads(await self.websocket.recv())
                trnm = response.get('trnm', 'UNKNOWN')

                if trnm == 'LOGIN':
                    if response.get('return_code') != 0:
                        logger.error('웹소켓(실시간) 로그인 실패하였습니다. : ', response.get('return_msg'))
                        await self.disconnect()
                    else:
                        logger.info('웹소켓(실시간) 로그인 성공하였습니다.')

                elif trnm == 'PING':
                    await self.send_message(response)

                elif trnm == 'UNKNOWN':
                    logger.warning('알 수 없는 메시지를 받았습니다:', response)

                else:
                    if trnm in self.handlers:
                        data_list = response.get('data', [])
                        if isinstance(data_list, list):
                            for data in data_list:
                                type_ = data['type']
                                name_ = data['name']
                                item_ = data['item']
                                await self.handlers[type_](data)
                        else:
                            logger.warning(f"response의 데이터가 리스트가 아님 {response}")
                    else:
                        logger.info(f"실시간 응답 수신: {response}")

            except websockets.ConnectionClosed:
                logger.warning('키움 웹소켓 서버로부터 연결이 종료되었습니다')
                self.connected = False
                await self.websocket.close()

    async def register(self, grp_no: str, item_list: list[str], type_list: list[str]):
        message = {
            "trnm": "REG",
            "grp_no": grp_no,
            "refresh": "1",
            "data": [{
                "item": item_list,
                "type": type_list
            }]
        }
        await self.send_message(message)

    async def unregister(self, grp_no: str):
        message = {
            "type": "REMOVE",
            "grp_no": grp_no
        }
        await self.send_message(message)

    def add_handler(self, msg_type: str, handler: Callable):
        """
        실시간 수신 메시지 핸들러 등록
        """
        self.handlers[msg_type] = handler

    async def run(self):
        await self.connect()
        await self.receive_messages()

    async def disconnect(self):
        self.keep_running = False
        if self.connected and self.websocket:
            await self.websocket.close()
            self.connected = False
            logger.info('키움 웹소켓 서버와의 연결이 종료되었습니다.')
