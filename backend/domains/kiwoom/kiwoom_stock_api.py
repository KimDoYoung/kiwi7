# kiwoom_api.py
"""
모듈 설명: 
    - kiwoom 증권 OpenAPI를 활용한 주식 API 구현체

작성자: 김도영
작성일: 2025-07-23
버전: 1.0
"""
from datetime import datetime
import json
import aiohttp
from backend.domains.kiwoom.managers.kiwwom_token_manager import KiwoomTokenManager
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomApiHelper, KiwoomRequest
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomResponse
from backend.domains.stock_api import StockApi
from backend.core.config import config
from backend.domains.user.user_service import UserService
from backend.core.logger import get_logger

logger = get_logger(__name__)

class KiwoomStockApi(StockApi):
    """
    키움증권 OpenAPI를 활용한 주식 API 구현체
    StockApi 인터페이스를 상속받아 키움증권의 실시간 주식 거래 및 정보 조회 기능을 제공합니다.
    """
    
    def __init__(self, token_manager: KiwoomTokenManager):
        """키움 API 클래스 초기화"""
        super().__init__(config.KIWOOM_ACCT_NO, UserService())
        self.token_manager = token_manager
        # 키움 API 기본 설정
        # self.BASE_URL = 'https://openapi.kiwoom.com'  # 실제 키움 API URL로 수정
        # self.APP_KEY = config.KIWOOM_APP_KEY
        # self.APP_SECRET = config.KIWOOM_SECRET_KEY
        
        # # 토큰 관리 변수
        # self.ACCESS_TOKEN: Optional[str] = None
        # self.ACCESS_TOKEN_EXPIRED_TIME: Optional[str] = None
    

    def get_headers(self, data: KiwoomRequest, token:str) -> dict:
        """
        키움 API 요청에 필요한 HTTP 헤더를 생성합니다.
        
        Args:
            data: 키움 API 요청 데이터
            
        Returns:
            dict: HTTP 요청 헤더
        """
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'authorization': f'Bearer {token}',
            'cont-yn': data.cont_yn.value,  
            'next-key': data.next_key or '',
            'api-id': data.api_id,  
        }
        return headers

    async def send_request(self, data: KiwoomRequest) -> KiwoomResponse:
        """
        키움 API에 요청을 전송하고 응답을 처리합니다.
        
        Args:
            data: 키움 API 요청 데이터
            
        Returns:
            KiwoomResponse: 표준화된 키움 API 응답 객체
            
        Raises:
            KiwoomApiException: API 요청 실패 시
            InvalidResponseException: 응답 파싱 실패 시
        """
        request_time = datetime.now()
        
        try:
            # API 정보 생성
            request_info = KiwoomApiHelper.get_request_info(data.api_id)
            
            # 요청 유효성 검증
            if not KiwoomApiHelper.validate_api_request(data):
                validation_errors = KiwoomApiHelper.get_validation_errors(data)
                return KiwoomApiHelper.create_error_response(
                    error_code="INVALID_REQUEST",
                    error_message=f"요청 데이터 오류: {', '.join(validation_errors)}",
                    status_code=400,
                    request_time=request_time
                )
            
            # 요청 파라미터 준비
            method = request_info.get('method')
            token = await self.token_manager.get_token()
            headers = self.get_headers(data, token)
            url = request_info.get('url')
            title = request_info.get('title')

            logger.info(f"{title} 요청 전송 - URL: {url}")
            logger.debug(f"요청 데이터: {data.payload}")

            # HTTP 요청 전송
            async with aiohttp.ClientSession() as session:
                if method == 'POST':
                    async with session.post(url, headers=headers, json=data.payload) as response:
                        return await self._process_response(response, request_info, request_time)
                        
                elif method == 'GET':
                    async with session.get(url, headers=headers, params=data.payload) as response:
                        return await self._process_response(response, request_info, request_time)
                else:
                    return KiwoomApiHelper.create_error_response(
                        error_code="UNSUPPORTED_METHOD",
                        error_message=f"지원하지 않는 HTTP 메서드: {method}",
                        status_code=400,
                        api_info=request_info,
                        request_time=request_time
                    )
                    
        except aiohttp.ClientError as e:
            logger.error(f"HTTP 요청 오류: {e}")
            return KiwoomApiHelper.create_error_response(
                error_code="HTTP_ERROR",
                error_message=f"HTTP 요청 실패: {str(e)}",
                status_code=500,
                request_time=request_time
            )
        except Exception as e:
            logger.error(f"예상치 못한 오류: {e}")
            return KiwoomApiHelper.create_error_response(
                error_code="UNEXPECTED_ERROR",
                error_message=f"요청 처리 중 오류 발생: {str(e)}",
                status_code=500,
                request_time=request_time
            )
    
    async def _process_response(
        self, 
        response: aiohttp.ClientResponse, 
        api_info: dict, 
        request_time: datetime
    ) -> KiwoomResponse:
        """
        HTTP 응답을 처리하여 KiwoomResponse 객체로 변환합니다.
        
        Args:
            response: aiohttp 응답 객체
            api_info: API 메타 정보
            request_time: 요청 시작 시간
            
        Returns:
            KiwoomResponse: 처리된 응답 객체
        """
        try:
            # HTTP 상태 코드 확인
            if response.status != 200:
                error_text = await response.text()
                logger.error(f"API 응답 오류 - 상태코드: {response.status}")
                return KiwoomApiHelper.create_error_response(
                    error_code=f"HTTP_{response.status}",
                    error_message=f"API 응답 오류: {error_text}",
                    status_code=response.status,
                    api_info=api_info,
                    request_time=request_time
                )
            logger.info(f"API 요청 성공 - 상태코드: {response.status}")
            # 응답 헤더 추출
            response_headers = self._extract_kiwoom_headers(response.headers)
            logger.debug(f"응답 헤더: {response_headers}")
            # 모든 응답 헤더 출력(Debug용)
            # logger.debug("=== 응답 헤더 전체 정보 ===")
            # for key, value in response.headers.items():
            #     logger.debug(f"{key}: {value}")
            # logger.debug("========================")
            response_data = await response.json()
            logger.debug(f"응답 데이터: {response_data}")

            # 키움에서 보내준 응답 코드에 따라 성공/오류 응답 생성
            # return_code가 문자열 '0' 또는 숫자 0이 아닌 경우 오류로 처리
            return_code = response_data.get('return_code')
            if return_code is not None and str(return_code) != '0':
                logger.error(f"API 오류 응답: {response_data}")
                return KiwoomApiHelper.create_error_response(
                    error_code=str(return_code),
                    error_message=response_data.get('return_message', '알 수 없는 오류'),
                    status_code=500,
                    api_info=api_info,
                    request_time=request_time
                )

            # 성공 응답 생성
            # 한글 필드명으로 변환된 데이터 생성 (선택적 사용)
            # korea_data = KiwoomApiHelper.to_korea_data(response_data, api_info.get('api_id', ''))
            # logger.debug(f"한글 변환 데이터: {korea_data}")
            
            return KiwoomApiHelper.create_success_response(
                data=response_data,
                headers=response_headers,
                api_info=api_info,
                request_time=request_time
            )
            
        except json.JSONDecodeError as e:
            logger.error(f"JSON 파싱 오류: {e}")
            return KiwoomApiHelper.create_error_response(
                error_code="JSON_PARSE_ERROR",
                error_message=f"응답 내용이 JSON 형식이 아닙니다: {str(e)}",
                status_code=502,
                api_info=api_info,
                request_time=request_time
            )
    
    def _extract_kiwoom_headers(self, response_headers) -> dict:
        """
        키움 API 응답 헤더에서 중요한 정보를 추출합니다.
        
        Args:
            response_headers: HTTP 응답 헤더
            
        Returns:
            dict: 추출된 키움 관련 헤더 정보
        """
        # 키움 API 관련 중요 헤더들
        important_headers = [
            'next-key', 'cont-yn', 'api-id','resp-cnt'  
        ]
        
        extracted = {}
        for key in important_headers:
            if key in response_headers:
                extracted[key] = response_headers[key]
        
        return extracted
    # """
    # 키움증권 OpenAPI를 활용한 주식 API 구현체
    # StockApi 인터페이스를 상속받아 키움증권 고유 기능을 구현합니다.
    # """
    # def __init__(self):
    #     super().__init__(config.KIWOOM_ACCT_NO, UserService())
    #     self.BASE_URL ='https://api.kiwoom.com'
    #     self.APP_KEY = config.KIWOOM_APP_KEY
    #     self.APP_SECRET = config.KIWOOM_SECRET_KEY
    #     self.ACCESS_TOKEN: Optional[str] = None
    #     self.ACCESS_TOKEN_EXPIRED_TIME: Optional[str] = None
    
    # async def refresh_token(self) -> bool:
    #     """
    #     users DB에서 ACCESS_TOKEN과 ACCESS_TOKEN_TIME을 가져온다.
    #     없거나 시간이 12시간이 지났다면 ACCESS_TOKEN을 새로 발급받는다.
    #     table users에 보관한다. 20250724135248
    #     Returns:
    #         bool: 초기화 성공 여부
    #     """
    #     try:
    #         # 현재 갖고 있지 않으면 DB에서 가져온다
    #         if not self.ACCESS_TOKEN or not self.ACCESS_TOKEN_EXPIRED_TIME:
    #             token_info = await self.user_service.get("ACCESS_TOKEN")
    #             time_info = await self.user_service.get("ACCESS_TOKEN_EXPIRED_TIME")
    #             self.ACCESS_TOKEN = token_info.value if token_info else None
    #             self.ACCESS_TOKEN_EXPIRED_TIME = time_info.value if time_info else None            
    #         # DB에서도 없다면 발급받는다
    #         if not self.ACCESS_TOKEN or not self.ACCESS_TOKEN_EXPIRED_TIME:
    #             await self.issue_access_token()

    #         # 시각이 만료1시간 전이라면 다시 발급받는다.
    #         expire_time = datetime.strptime(self.ACCESS_TOKEN_EXPIRED_TIME, '%Y%m%d%H%M%S')
    #         if expire_time <= (datetime.now() + timedelta(hours=1)):
    #             await self.issue_access_token()
            
    #         return True
    #     except Exception as e:
    #         raise KiwoomAuthException(f"Failed to refresh token: {str(e)}")
        

    # async def issue_access_token(self):
    #     """
    #     키움증권 OpenAPI를 통해 ACCESS_TOKEN을 발급받는다. DB에 저장
    #     """
    #     url = self.BASE_URL + '/oauth2/token'

    #     headers = {
    #         'Content-Type': 'application/json;charset=UTF-8',
    #     }
    #     params = {
    #         'grant_type': 'client_credentials',
    #         'appkey': self.APP_KEY,
    #         'secretkey': self.APP_SECRET,
    #     }
    #     async with aiohttp.ClientSession() as session:
    #         async with session.post(url, headers=headers, json=params) as response:
    #             if response.status != 200:
    #                 raise KiwoomAuthException(f"Failed to issue access token: {response.status}")
    #             resp_json = await response.json()
    #             self.ACCESS_TOKEN = resp_json.get("token")
    #             self.ACCESS_TOKEN_EXPIRED_TIME = resp_json.get("expires_dt")
    #             # DB에 저장하는 로직 추가 필요
    #             await self.user_service.set("ACCESS_TOKEN", self.ACCESS_TOKEN)
    #             await self.user_service.set("ACCESS_TOKEN_EXPIRED_TIME", self.ACCESS_TOKEN_EXPIRED_TIME)

    # def get_headers(self, data: KiwoomRequest) -> dict:
    #     headers = {
    #         'Content-Type': 'application/json;charset=UTF-8',
    #         'authorization': f'Bearer {self.ACCESS_TOKEN}',
    #         'cont-yn': data.cont_yn,
    #         'next-key': data.next_key or '',
    #         'api-id': data.api_id,
    #     }
    #     return headers

    # async def send_request(self, data: KiwoomRequest):
    #     try:
    #         api_definition = KIWOOM_REQUEST_DEF.get(data.api_id)
    #         if not api_definition:
    #             raise KiwoomApiException(status_code=404, detail=f"API ID {data.api_id} not found")
            
    #         method = 'POST'
    #         headers = self.get_headers(data)
    #         url = api_definition.get('url')
    #         title = api_definition.get('title')
            
    #         logger.info(f"Sending request to {title} ({url}) with data: {data.payload}")

    #         async with aiohttp.ClientSession() as session:
    #             if method == 'POST':
    #                 async with session.post(url, headers=headers, json=data.payload) as response:
    #                     response.raise_for_status()
    #                     return await response.json()
    #             elif method == 'GET':
    #                 async with session.get(url, headers=headers, params=data.payload) as response:
    #                     response.raise_for_status()
    #                     return await response.json()
    #     except aiohttp.ClientError as e:
    #         logger.error(f"HTTP 오류 ({title}): {e}")
    #         raise KiwoomApiException(status_code=500, detail=f"HTTP 오류 ({title}): {e}")
    #     except json.JSONDecodeError as e:
    #         logger.error(f"Response is not in JSON format.{title}")
    #         raise InvalidResponseException(f"응답 내용이 JSON형식이 아닙니다 ({title})")