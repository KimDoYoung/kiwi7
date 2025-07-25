# kiwoom_api.py
"""
모듈 설명: 
    - kiwoom 증권 OpenAPI를 활용한 주식 API 구현체

작성자: 김도영
작성일: 2025-07-23
버전: 1.0
"""
from datetime import datetime, timedelta
import json
from typing import Optional
import aiohttp
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomApiHelper, KiwoomRequest
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomResponse
from backend.domains.stock_api import StockApi
from backend.core.config import config
from backend.domains.user.user_service import UserService
from backend.core.exceptions import InvalidResponseException, KiwoomApiException, KiwoomAuthException
from backend.core.logger import get_logger
from backend.domains.kiwoom.models.kiwoom_request_definition import KIWOOM_REQUEST_DEF  # Add this import

logger = get_logger(__name__)

class KiwoomStockApi(StockApi):
    """
    키움증권 OpenAPI를 활용한 주식 API 구현체
    StockApi 인터페이스를 상속받아 키움증권의 실시간 주식 거래 및 정보 조회 기능을 제공합니다.
    """
    
    def __init__(self):
        """키움 API 클래스 초기화"""
        super().__init__(config.KIWOOM_ACCT_NO, UserService())
        # 키움 API 기본 설정
        self.BASE_URL = 'https://openapi.kiwoom.com'  # 실제 키움 API URL로 수정
        self.APP_KEY = config.KIWOOM_APP_KEY
        self.APP_SECRET = config.KIWOOM_SECRET_KEY
        
        # 토큰 관리 변수
        self.ACCESS_TOKEN: Optional[str] = None
        self.ACCESS_TOKEN_EXPIRED_TIME: Optional[str] = None
    
    async def refresh_token(self) -> bool:
        """
        액세스 토큰 갱신 처리
        
        사용자 DB에서 저장된 토큰을 확인하고, 없거나 만료가 임박한 경우 새로 발급받습니다.
        토큰 만료 1시간 전에 미리 갱신하여 API 호출 중단을 방지합니다.
        
        Returns:
            bool: 토큰 갱신 성공 여부
            
        Raises:
            KiwoomAuthException: 토큰 갱신 실패 시
        """
        try:
            # 메모리에 토큰이 없으면 DB에서 조회
            if not self.ACCESS_TOKEN or not self.ACCESS_TOKEN_EXPIRED_TIME:
                await self._load_token_from_db()
            
            # DB에도 토큰이 없으면 새로 발급
            if not self.ACCESS_TOKEN or not self.ACCESS_TOKEN_EXPIRED_TIME:
                logger.info("저장된 토큰이 없어 새로 발급받습니다.")
                await self.issue_access_token()
                return True

            # 토큰 만료 시간 확인 (1시간 전에 미리 갱신)
            if self._is_token_expire_soon():
                logger.info("토큰 만료가 임박하여 새로 발급받습니다.")
                await self.issue_access_token()
            
            logger.debug("토큰 상태 확인 완료")
            return True
            
        except Exception as e:
            logger.error(f"토큰 갱신 중 오류 발생: {str(e)}")
            raise KiwoomAuthException(f"토큰 갱신 실패: {str(e)}")
    
    async def _load_token_from_db(self):
        """DB에서 저장된 토큰 정보를 로드합니다."""
        token_info = await self.user_service.get("ACCESS_TOKEN")
        time_info = await self.user_service.get("ACCESS_TOKEN_EXPIRED_TIME")
        
        self.ACCESS_TOKEN = token_info.value if token_info else None
        self.ACCESS_TOKEN_EXPIRED_TIME = time_info.value if time_info else None
        
        if self.ACCESS_TOKEN:
            logger.debug("DB에서 토큰 정보를 성공적으로 로드했습니다.")
    
    def _is_token_expire_soon(self) -> bool:
        """
        토큰 만료가 임박했는지 확인합니다.
        
        Returns:
            bool: 1시간 이내 만료 예정이면 True
        """
        try:
            expire_time = datetime.strptime(self.ACCESS_TOKEN_EXPIRED_TIME, '%Y%m%d%H%M%S')
            current_time = datetime.now()
            time_diff = expire_time - current_time
            
            # 1시간(3600초) 이내에 만료되면 True
            return time_diff.total_seconds() <= 3600
            
        except ValueError as e:
            logger.error(f"토큰 만료 시간 파싱 오류: {e}")
            return True  # 파싱 오류 시 안전하게 갱신하도록 True 반환

    async def issue_access_token(self):
        """
        키움증권 OpenAPI를 통해 새로운 액세스 토큰을 발급받습니다.
        
        발급받은 토큰은 메모리와 DB에 모두 저장하여 다음 사용을 위해 보관합니다.
        
        Raises:
            KiwoomAuthException: 토큰 발급 실패 시
        """
        url = f"{self.BASE_URL}/oauth2/tokenP"  # 실제 키움 API 엔드포인트
        
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
        }
        
        params = {
            'grant_type': 'client_credentials',
            'appkey': self.APP_KEY,
            'secretkey': self.APP_SECRET,
        }
        
        try:
            logger.info("키움 API 액세스 토큰 발급 요청 중...")
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=params) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        logger.error(f"토큰 발급 실패 - 상태코드: {response.status}, 응답: {error_text}")
                        raise KiwoomAuthException(f"토큰 발급 실패: HTTP {response.status}")
                    
                    resp_json = await response.json()
                    
                    # 응답에서 토큰 정보 추출 (실제 키움 API 응답 구조에 맞게 수정 필요)
                    self.ACCESS_TOKEN = resp_json.get("access_token")  # 실제 필드명 확인 필요
                    self.ACCESS_TOKEN_EXPIRED_TIME = resp_json.get("expires_dt")  # 실제 필드명 확인 필요
                    
                    if not self.ACCESS_TOKEN:
                        raise KiwoomAuthException("응답에서 액세스 토큰을 찾을 수 없습니다.")
                    
                    # DB에 토큰 정보 저장
                    await self._save_token_to_db()
                    
                    logger.info("키움 API 액세스 토큰 발급 완료")
                    
        except aiohttp.ClientError as e:
            logger.error(f"토큰 발급 네트워크 오류: {e}")
            raise KiwoomAuthException(f"토큰 발급 네트워크 오류: {str(e)}")
        except Exception as e:
            logger.error(f"토큰 발급 중 예상치 못한 오류: {e}")
            raise KiwoomAuthException(f"토큰 발급 실패: {str(e)}")
    
    async def _save_token_to_db(self):
        """발급받은 토큰 정보를 DB에 저장합니다."""
        await self.user_service.set("ACCESS_TOKEN", self.ACCESS_TOKEN)
        await self.user_service.set("ACCESS_TOKEN_EXPIRED_TIME", self.ACCESS_TOKEN_EXPIRED_TIME)
        logger.debug("토큰 정보를 DB에 저장했습니다.")

    def get_headers(self, data: KiwoomRequest) -> dict:
        """
        키움 API 요청에 필요한 HTTP 헤더를 생성합니다.
        
        Args:
            data: 키움 API 요청 데이터
            
        Returns:
            dict: HTTP 요청 헤더
        """
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'authorization': f'Bearer {self.ACCESS_TOKEN}',
            'appkey': self.APP_KEY,  # 키움 API에서 필요한 헤더
            'appsecret': self.APP_SECRET,  # 키움 API에서 필요한 헤더
            'cont-yn': data.cont_yn.value,  # Enum 값으로 수정
            'next-key': data.next_key or '',
            'tr_id': data.api_id,  # 실제 키움 API에서는 tr_id 사용
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
            # 토큰 갱신 확인
            await self.refresh_token()
            
            # API 정의 조회
            request_definition = KIWOOM_REQUEST_DEF.get(data.api_id)
            if not request_definition:
                return KiwoomApiHelper.create_error_response(
                    error_code="REQUEST_DEFINITION_NOT_FOUND",
                    error_message=f"REQUEST DEFINITION이 정의되지 않은 API ID입니다: {data.api_id}",
                    status_code=404,
                    request_time=request_time
                )
            
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
            method = request_definition.get('method', 'POST')
            headers = self.get_headers(data)
            url = request_definition.get('url')
            title = request_definition.get('title')
            
            # API 정보 생성
            api_info = KiwoomApiHelper.get_api_info(data.api_id)
            
            logger.info(f"{title} 요청 전송 - URL: {url}")
            logger.debug(f"요청 데이터: {data.payload}")

            # HTTP 요청 전송
            async with aiohttp.ClientSession() as session:
                if method == 'POST':
                    async with session.post(url, headers=headers, json=data.payload) as response:
                        return await self._process_response(response, api_info, request_time)
                        
                elif method == 'GET':
                    async with session.get(url, headers=headers, params=data.payload) as response:
                        return await self._process_response(response, api_info, request_time)
                else:
                    return KiwoomApiHelper.create_error_response(
                        error_code="UNSUPPORTED_METHOD",
                        error_message=f"지원하지 않는 HTTP 메서드: {method}",
                        status_code=400,
                        api_info=api_info,
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
            
            # 응답 헤더 추출
            response_headers = self._extract_kiwoom_headers(response.headers)
            
            # JSON 응답 파싱
            response_data = await response.json()
            
            logger.info(f"API 요청 성공 - 상태코드: {response.status}")
            logger.debug(f"응답 헤더: {response_headers}")
            
            # 성공 응답 생성
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
            'tr_id', 'tr_cont', 'gt_uid', 'custtype',
            'next-key', 'cont-yn', 'api-id'  
        ]
        
        extracted = {}
        for key in important_headers:
            if key in response_headers:
                extracted[key] = response_headers[key]
        
        return extracted
    """
    키움증권 OpenAPI를 활용한 주식 API 구현체
    StockApi 인터페이스를 상속받아 키움증권 고유 기능을 구현합니다.
    """
    def __init__(self):
        super().__init__(config.KIWOOM_ACCT_NO, UserService())
        self.BASE_URL ='https://api.kiwoom.com'
        self.APP_KEY = config.KIWOOM_APP_KEY
        self.APP_SECRET = config.KIWOOM_SECRET_KEY
        self.ACCESS_TOKEN: Optional[str] = None
        self.ACCESS_TOKEN_EXPIRED_TIME: Optional[str] = None
    
    async def refresh_token(self) -> bool:
        """
        users DB에서 ACCESS_TOKEN과 ACCESS_TOKEN_TIME을 가져온다.
        없거나 시간이 12시간이 지났다면 ACCESS_TOKEN을 새로 발급받는다.
        table users에 보관한다. 20250724135248
        Returns:
            bool: 초기화 성공 여부
        """
        try:
            # 현재 갖고 있지 않으면 DB에서 가져온다
            if not self.ACCESS_TOKEN or not self.ACCESS_TOKEN_EXPIRED_TIME:
                token_info = await self.user_service.get("ACCESS_TOKEN")
                time_info = await self.user_service.get("ACCESS_TOKEN_EXPIRED_TIME")
                self.ACCESS_TOKEN = token_info.value if token_info else None
                self.ACCESS_TOKEN_EXPIRED_TIME = time_info.value if time_info else None            
            # DB에서도 없다면 발급받는다
            if not self.ACCESS_TOKEN or not self.ACCESS_TOKEN_EXPIRED_TIME:
                await self.issue_access_token()

            # 시각이 만료1시간 전이라면 다시 발급받는다.
            expire_time = datetime.strptime(self.ACCESS_TOKEN_EXPIRED_TIME, '%Y%m%d%H%M%S')
            if expire_time <= (datetime.now() + timedelta(hours=1)):
                await self.issue_access_token()
            
            return True
        except Exception as e:
            raise KiwoomAuthException(f"Failed to refresh token: {str(e)}")
        

    async def issue_access_token(self):
        """
        키움증권 OpenAPI를 통해 ACCESS_TOKEN을 발급받는다. DB에 저장
        """
        url = self.BASE_URL + '/oauth2/token'

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
        }
        params = {
            'grant_type': 'client_credentials',
            'appkey': self.APP_KEY,
            'secretkey': self.APP_SECRET,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=params) as response:
                if response.status != 200:
                    raise KiwoomAuthException(f"Failed to issue access token: {response.status}")
                resp_json = await response.json()
                self.ACCESS_TOKEN = resp_json.get("token")
                self.ACCESS_TOKEN_EXPIRED_TIME = resp_json.get("expires_dt")
                # DB에 저장하는 로직 추가 필요
                await self.user_service.set("ACCESS_TOKEN", self.ACCESS_TOKEN)
                await self.user_service.set("ACCESS_TOKEN_EXPIRED_TIME", self.ACCESS_TOKEN_EXPIRED_TIME)

    def get_headers(self, data: KiwoomRequest) -> dict:
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'authorization': f'Bearer {self.ACCESS_TOKEN}',
            'cont-yn': data.cont_yn,
            'next-key': data.next_key or '',
            'api-id': data.api_id,
        }
        return headers

    async def send_request(self, data: KiwoomRequest):
        try:
            api_definition = KIWOOM_REQUEST_DEF.get(data.api_id)
            if not api_definition:
                raise KiwoomApiException(status_code=404, detail=f"API ID {data.api_id} not found")
            
            method = 'POST'
            headers = self.get_headers(data)
            url = api_definition.get('url')
            title = api_definition.get('title')
            
            logger.info(f"Sending request to {title} ({url}) with data: {data.payload}")

            async with aiohttp.ClientSession() as session:
                if method == 'POST':
                    async with session.post(url, headers=headers, json=data.payload) as response:
                        response.raise_for_status()
                        return await response.json()
                elif method == 'GET':
                    async with session.get(url, headers=headers, params=data.payload) as response:
                        response.raise_for_status()
                        return await response.json()
        except aiohttp.ClientError as e:
            logger.error(f"HTTP 오류 ({title}): {e}")
            raise KiwoomApiException(status_code=500, detail=f"HTTP 오류 ({title}): {e}")
        except json.JSONDecodeError as e:
            logger.error(f"Response is not in JSON format.{title}")
            raise InvalidResponseException(f"응답 내용이 JSON형식이 아닙니다 ({title})")