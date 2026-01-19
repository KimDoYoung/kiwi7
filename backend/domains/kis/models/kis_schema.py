"""
KIS(한국투자증권) 스키마 정의
API 요청/응답 모델 및 유틸리티 클래스를 정의합니다.
"""
from datetime import datetime
from typing import Optional, Dict, Any, List

from backend.domains.base.base_schema import BaseRequest, BaseResponse, ContYn
from backend.domains.kis.models.kis_request_definition import (
    KIS_REQUEST_DEF,
    get_required_fields,
    get_request_definition,
)
from backend.domains.kis.models.kis_response_definition import KIS_RESPONSE_DEF


class KisRequest(BaseRequest):
    """KIS API 요청 모델"""

    def validate_payload(self) -> List[str]:
        """payload의 유효성을 검증"""
        # 커스텀 API는 검증 스킵
        if self.api_id.startswith('kiwi7_'):
            return []

        api_def = get_request_definition(self.api_id)
        if not api_def:
            return [f"정의되지 않은 API ID: {self.api_id}"]

        errors = []
        required_fields = get_required_fields(self.api_id)

        for field in required_fields:
            if field not in self.payload:
                errors.append(f"필수 필드 누락: {field}")

        # 연속조회 검증
        if self.cont_yn == ContYn.Y and not self.next_key:
            errors.append("연속조회 시 next_key가 필요합니다")

        return errors


class KisResponse(BaseResponse):
    """KIS API 응답 모델"""
    pass


class KisApiHelper:
    """KIS API 유틸리티 클래스"""

    @staticmethod
    def get_request_info(api_id: str) -> Optional[Dict[str, str]]:
        """API 정보 조회"""
        api_def = get_request_definition(api_id)
        if not api_def:
            return None

        return {
            'api_id': api_id,
            'url': api_def.get('url', ''),
            'title': api_def.get('title', ''),
            'method': api_def.get('method', 'GET'),
            'tr_id': api_def.get('tr_id', api_id),
            'hashkey_required': str(api_def.get('hashkey_required', False)),
        }

    @staticmethod
    def validate_api_request(request: KisRequest) -> bool:
        """API 요청 유효성 검증"""
        if request.api_id.startswith('kiwi7_'):
            return True

        if request.api_id not in KIS_REQUEST_DEF:
            return False

        validation_errors = request.validate_payload()
        if validation_errors:
            return False

        return True

    @staticmethod
    def create_success_response(
        data: Dict[str, Any],
        headers: Dict[str, str] = None,
        api_info: Dict[str, str] = None,
        request_time: datetime = None
    ) -> KisResponse:
        """성공 응답 생성"""
        cont_yn = ContYn.N
        next_key = None

        if headers:
            # KIS 연속조회 헤더 처리
            if headers.get('tr_cont') == 'M' or headers.get('tr_cont') == 'F':
                cont_yn = ContYn.Y
            next_key = headers.get('ctx_area_fk100') or headers.get('ctx_area_nk100')

        return KisResponse(
            data=data,
            headers=headers,
            api_info=api_info,
            status_code=200,
            cont_yn=cont_yn,
            next_key=next_key,
            success=True,
            request_time=request_time,
            response_time=datetime.now()
        )

    @staticmethod
    def create_error_response(
        error_code: str,
        error_message: str,
        api_info: Dict[str, str] = None,
        request_time: datetime = None
    ) -> KisResponse:
        """에러 응답 생성"""
        return KisResponse(
            data=None,
            api_info=api_info,
            status_code=int(error_code) if error_code.isdigit() else 500,
            error_code=error_code,
            error_message=error_message,
            success=False,
            request_time=request_time,
            response_time=datetime.now()
        )

    @staticmethod
    def to_korea_data(response_data: Dict[str, Any], api_id: str) -> Dict[str, Any]:
        """영문 필드명을 한글로 변환"""
        response_def = KIS_RESPONSE_DEF.get(api_id, {})
        if not response_def:
            return response_data

        # 응답 정의 구조: {'output': {'fields': [...]}}
        response_fields = []
        if isinstance(response_def, dict):
            if 'output' in response_def and isinstance(response_def['output'], dict):
                response_fields = response_def['output'].get('fields', [])
            elif 'fields' in response_def:
                response_fields = response_def.get('fields', [])

        if not response_fields:
            return response_data

        key_to_name_map = {field['key']: field['name'] for field in response_fields}

        def convert_dict(data: Dict) -> Dict:
            korea_data = {}
            for key, value in data.items():
                korean_key = key_to_name_map.get(key, key)
                if isinstance(value, dict):
                    korea_data[korean_key] = convert_dict(value)
                elif isinstance(value, list):
                    korea_data[korean_key] = [
                        convert_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ]
                else:
                    korea_data[korean_key] = value
            return korea_data

        if isinstance(response_data, dict):
            return convert_dict(response_data)
        elif isinstance(response_data, list):
            return [convert_dict(item) if isinstance(item, dict) else item for item in response_data]

        return response_data

    @staticmethod
    def has_more_data(response: KisResponse) -> bool:
        """연속조회 가능 여부 확인"""
        return response.cont_yn == ContYn.Y and bool(response.next_key)

    @staticmethod
    def create_continuation_request(
        original_request: KisRequest,
        response: KisResponse
    ) -> Optional[KisRequest]:
        """연속조회 요청 생성"""
        if not KisApiHelper.has_more_data(response):
            return None

        continuation_payload = original_request.payload.copy()

        # KIS 연속조회 키 설정
        if response.headers:
            continuation_payload['CTX_AREA_FK100'] = response.headers.get('ctx_area_fk100', '')
            continuation_payload['CTX_AREA_NK100'] = response.headers.get('ctx_area_nk100', '')

        return KisRequest(
            api_id=original_request.api_id,
            cont_yn=ContYn.Y,
            next_key=response.next_key,
            payload=continuation_payload
        )
