"""
KIS(한국투자증권) REST API 클라이언트
"""
from datetime import datetime
from typing import Dict, Any
import aiohttp

from backend.domains.stock_api import StockApi, BrokerType
from backend.domains.kis.managers.kis_token_manager import KisTokenManager
from backend.domains.kis.models.kis_schema import KisRequest, KisResponse, KisApiHelper
from backend.domains.kis.models.kis_request_definition import (
    get_request_definition,
    get_tr_id,
    is_hashkey_required,
)
from backend.core.config import config
from backend.core.exceptions import KisApiException
from backend.core.logger import get_logger

logger = get_logger(__name__)


class KisRestApi(StockApi):
    """한국투자증권 REST API 클라이언트"""

    def __init__(self, token_manager: KisTokenManager):
        super().__init__(
            acctno=config.KIS_ACCT_NO,
            broker_type=BrokerType.KIS
        )
        self.token_manager = token_manager
        self.acct_prdt_cd = config.KIS_ACCT_PRDT_CD

    def get_base_url(self) -> str:
        return config.KIS_BASE_URL

    @property
    def base_url(self) -> str:
        return self.get_base_url()

    def get_headers(self, request: KisRequest, token: str, tr_id: str, hashkey: str = None) -> Dict[str, str]:
        """HTTP 헤더 생성"""
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'authorization': f'Bearer {token}',
            'appkey': self.token_manager.app_key,
            'appsecret': self.token_manager.app_secret,
            'tr_id': tr_id,
        }

        # 연속조회 헤더
        if request.cont_yn.value == 'Y':
            headers['tr_cont'] = 'N'
        else:
            headers['tr_cont'] = ''

        # 해시키 (주문 API용)
        if hashkey:
            headers['hashkey'] = hashkey

        return headers

    async def get_hashkey(self, payload: Dict[str, Any]) -> str:
        """해시키 생성 (주문 시 필요)"""
        url = f"{self.base_url}/uapi/hashkey"
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'appkey': self.token_manager.app_key,
            'appsecret': self.token_manager.app_secret,
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=payload) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        raise KisApiException(f"해시키 생성 실패: {error_text}")

                    data = await response.json()
                    return data.get('HASH', '')

        except aiohttp.ClientError as e:
            raise KisApiException(f"해시키 생성 네트워크 오류: {e}")

    async def send_request(self, request: KisRequest) -> KisResponse:
        """API 요청 전송"""
        request_time = datetime.now()

        try:
            # API 정보 조회
            api_info = KisApiHelper.get_request_info(request.api_id)
            if not api_info:
                return KisApiHelper.create_error_response(
                    error_code="400",
                    error_message=f"정의되지 않은 API ID: {request.api_id}",
                    request_time=request_time
                )

            # 요청 검증
            if not KisApiHelper.validate_api_request(request):
                validation_errors = request.validate_payload()
                return KisApiHelper.create_error_response(
                    error_code="400",
                    error_message=f"요청 검증 실패: {', '.join(validation_errors)}",
                    api_info=api_info,
                    request_time=request_time
                )

            # 토큰 획득
            token = await self.token_manager.get_token()

            # TR ID (실전 환경)
            tr_id = get_tr_id(request.api_id, is_virtual=False)

            # 해시키 생성 (주문 API인 경우)
            hashkey = None
            if is_hashkey_required(request.api_id):
                hashkey = await self.get_hashkey(request.payload)

            # 헤더 생성
            headers = self.get_headers(request, token, tr_id, hashkey)

            # URL 구성
            api_def = get_request_definition(request.api_id)
            url = f"{self.base_url}{api_def['url']}"
            method = api_def.get('method', 'GET')

            logger.info(f"[KIS] {api_info['title']} 요청 - URL: {url}, TR_ID: {tr_id}")

            # HTTP 요청
            async with aiohttp.ClientSession() as session:
                if method == 'POST':
                    async with session.post(url, headers=headers, json=request.payload) as response:
                        return await self._process_response(response, api_info, request_time)
                else:  # GET
                    async with session.get(url, headers=headers, params=request.payload) as response:
                        return await self._process_response(response, api_info, request_time)

        except aiohttp.ClientError as e:
            logger.error(f"[KIS] HTTP 요청 오류: {e}")
            return KisApiHelper.create_error_response(
                error_code="500",
                error_message=f"HTTP 요청 실패: {str(e)}",
                request_time=request_time
            )
        except KisApiException as e:
            logger.error(f"[KIS] API 오류: {e}")
            return KisApiHelper.create_error_response(
                error_code=e.error_code or "500",
                error_message=str(e),
                request_time=request_time
            )
        except Exception as e:
            logger.error(f"[KIS] 예상치 못한 오류: {e}")
            return KisApiHelper.create_error_response(
                error_code="500",
                error_message=f"요청 처리 중 오류: {str(e)}",
                request_time=request_time
            )

    async def _process_response(
        self,
        response: aiohttp.ClientResponse,
        api_info: Dict[str, str],
        request_time: datetime
    ) -> KisResponse:
        """응답 처리"""
        # HTTP 상태 코드 확인
        if response.status != 200:
            error_text = await response.text()
            return KisApiHelper.create_error_response(
                error_code=str(response.status),
                error_message=f"HTTP 오류: {error_text}",
                api_info=api_info,
                request_time=request_time
            )

        # 응답 헤더 추출
        response_headers = self._extract_headers(response.headers)

        # JSON 파싱
        try:
            response_data = await response.json()
        except Exception as e:
            return KisApiHelper.create_error_response(
                error_code="502",
                error_message=f"JSON 파싱 실패: {str(e)}",
                api_info=api_info,
                request_time=request_time
            )

        # KIS API 오류 확인
        rt_cd = response_data.get('rt_cd')
        if rt_cd and rt_cd != '0':
            msg_cd = response_data.get('msg_cd', '')
            msg1 = response_data.get('msg1', '알 수 없는 오류')
            return KisApiHelper.create_error_response(
                error_code=msg_cd,
                error_message=msg1,
                api_info=api_info,
                request_time=request_time
            )

        # 성공 응답
        return KisApiHelper.create_success_response(
            data=response_data,
            headers=response_headers,
            api_info=api_info,
            request_time=request_time
        )

    def _extract_headers(self, headers) -> Dict[str, str]:
        """응답 헤더에서 필요한 정보 추출"""
        kis_headers = {}
        header_keys = [
            'tr_id', 'tr_cont', 'gt_uid',
            'ctx_area_fk100', 'ctx_area_nk100',
            'ctx_area_fk200', 'ctx_area_nk200',
        ]

        for key in header_keys:
            value = headers.get(key)
            if value:
                kis_headers[key] = value

        return kis_headers
