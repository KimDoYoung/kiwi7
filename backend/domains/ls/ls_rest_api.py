"""
LS증권 REST API 클라이언트
"""
from datetime import datetime
from typing import Dict
import aiohttp

from backend.domains.stock_api import StockApi, BrokerType
from backend.domains.ls.managers.ls_token_manager import LsTokenManager
from backend.domains.ls.models.ls_schema import LsRequest, LsResponse, LsApiHelper
from backend.domains.ls.models.ls_request_definition import (
    get_request_definition,
    get_tr_cd,
)
from backend.core.config import config
from backend.core.exceptions import LsApiException
from backend.core.logger import get_logger

logger = get_logger(__name__)


class LsRestApi(StockApi):
    """LS증권 REST API 클라이언트"""

    def __init__(self, token_manager: LsTokenManager):
        super().__init__(
            acctno=config.LS_ACCT_NO,
            broker_type=BrokerType.LS
        )
        self.token_manager = token_manager

    def get_base_url(self) -> str:
        return config.LS_BASE_URL

    @property
    def base_url(self) -> str:
        return self.get_base_url()

    def get_headers(self, request: LsRequest, token: str, tr_cd: str) -> Dict[str, str]:
        """HTTP 헤더 생성"""
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'authorization': f'Bearer {token}',
            'tr_cd': tr_cd,
            'tr_cont': 'N' if request.cont_yn.value == 'N' else 'Y',
            'tr_cont_key': request.next_key or '',
        }

        return headers

    async def send_request(self, request: LsRequest) -> LsResponse:
        """API 요청 전송"""
        request_time = datetime.now()

        try:
            # API 정보 조회
            api_info = LsApiHelper.get_request_info(request.api_id)
            if not api_info:
                return LsApiHelper.create_error_response(
                    error_code="400",
                    error_message=f"정의되지 않은 API ID: {request.api_id}",
                    request_time=request_time
                )

            # 요청 검증
            if not LsApiHelper.validate_api_request(request):
                validation_errors = request.validate_payload()
                return LsApiHelper.create_error_response(
                    error_code="400",
                    error_message=f"요청 검증 실패: {', '.join(validation_errors)}",
                    api_info=api_info,
                    request_time=request_time
                )

            # 토큰 획득
            token = await self.token_manager.get_token()

            # TR 코드
            tr_cd = get_tr_cd(request.api_id)

            # 헤더 생성
            headers = self.get_headers(request, token, tr_cd)

            # URL 구성
            api_def = get_request_definition(request.api_id)
            url = f"{self.base_url}{api_def['url']}"

            # LS는 요청 본문에 tr_cd와 데이터를 함께 전송
            body = {
                f'{tr_cd}InBlock': request.payload
            }

            logger.info(f"[LS] {api_info['title']} 요청 - URL: {url}, TR_CD: {tr_cd}")

            # HTTP 요청 (LS는 주로 POST 사용)
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=body) as response:
                    return await self._process_response(response, api_info, request_time)

        except aiohttp.ClientError as e:
            logger.error(f"[LS] HTTP 요청 오류: {e}")
            return LsApiHelper.create_error_response(
                error_code="500",
                error_message=f"HTTP 요청 실패: {str(e)}",
                request_time=request_time
            )
        except LsApiException as e:
            logger.error(f"[LS] API 오류: {e}")
            return LsApiHelper.create_error_response(
                error_code=e.error_code or "500",
                error_message=str(e),
                request_time=request_time
            )
        except Exception as e:
            logger.error(f"[LS] 예상치 못한 오류: {e}")
            return LsApiHelper.create_error_response(
                error_code="500",
                error_message=f"요청 처리 중 오류: {str(e)}",
                request_time=request_time
            )

    async def _process_response(
        self,
        response: aiohttp.ClientResponse,
        api_info: Dict[str, str],
        request_time: datetime
    ) -> LsResponse:
        """응답 처리"""
        # HTTP 상태 코드 확인
        if response.status != 200:
            error_text = await response.text()
            return LsApiHelper.create_error_response(
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
            return LsApiHelper.create_error_response(
                error_code="502",
                error_message=f"JSON 파싱 실패: {str(e)}",
                api_info=api_info,
                request_time=request_time
            )

        # LS API 오류 확인
        # rsp_cd가 '0' 또는 '00000'이면 성공, 그 외는 에러
        rsp_cd = response_data.get('rsp_cd', '')
        if rsp_cd and rsp_cd not in ('0', '00000'):
            rsp_msg = response_data.get('rsp_msg', '알 수 없는 오류')
            return LsApiHelper.create_error_response(
                error_code=rsp_cd,
                error_message=rsp_msg,
                api_info=api_info,
                request_time=request_time
            )

        # 성공 응답
        return LsApiHelper.create_success_response(
            data=response_data,
            headers=response_headers,
            api_info=api_info,
            request_time=request_time
        )

    def _extract_headers(self, headers) -> Dict[str, str]:
        """응답 헤더에서 필요한 정보 추출"""
        ls_headers = {}
        header_keys = [
            'tr_cd', 'tr_cont', 'tr_cont_key',
        ]

        for key in header_keys:
            value = headers.get(key)
            if value:
                ls_headers[key] = value

        return ls_headers
