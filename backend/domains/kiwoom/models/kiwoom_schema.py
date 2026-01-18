from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from backend.domains.kiwoom.models.kiwoom_request_definition import (
    KIWOOM_REQUEST_DEF,
    get_request_definition,
    get_required_fields,
)
from backend.domains.kiwoom.models.kiwoom_response_definition import KIWOOM_RESPONSE_DEF


class ContYn(str, Enum):
    """연속조회 여부를 나타내는 열거형"""
    Y = 'Y'  # 연속조회 있음
    N = 'N'  # 연속조회 없음

class KiwoomRequest(BaseModel):
    """
    키움 API 요청 데이터 모델
    키움 OpenAPI 호출 시 사용되는 표준 요청 형식입니다.
    """
    api_id: str                       # API 식별자 (예: 'ka10072')
    cont_yn: ContYn = ContYn.N        # 연속조회 여부 (기본값: N)
    next_key: Optional[str] = None    # 연속조회 키 (연속조회 시 필요)
    payload: Dict[str, Any]           # POST body 또는 GET params 데이터

    def validate_payload(self) -> List[str]:
        """
        payload의 유효성을 검증합니다.
        kiwi7_로 시작하는 api_id는 자체 API이므로 검증을 스킵합니다.
        Returns:
            List[str]: 오류 메시지 목록 (빈 리스트면 유효함)
        """
        errors = []
        
        # kiwi7_로 시작하는 자체 API는 검증 스킵
        if self.api_id.startswith('kiwi7_'):
            return errors
        
        api_def = KIWOOM_REQUEST_DEF.get(self.api_id)
        if not api_def:
            errors.append(f"API 정의를 찾을 수 없습니다: {self.api_id}")
            return errors
        
        # body 필드에서 required=True인 필드들의 key 추출
        required_fields = get_required_fields(self.api_id)
        for field in required_fields:
            if field not in self.payload:
                errors.append(f"필수 필드 누락: {field}")
        # 추가적인 검증 로직 필요시 여기에 작성
        return errors

class KiwoomResponse(BaseModel):
    """
    키움 API 응답 데이터 모델
    키움 OpenAPI 응답을 표준화된 형식으로 처리합니다.
    """
    # 응답 데이터
    data: Optional[Dict[str, Any]] = None           # 실제 응답 JSON 데이터
    
    # 응답 헤더 정보
    headers: Optional[Dict[str, str]] = None        # 응답 헤더 (연속조회 키 등)
    
    # API 메타 정보
    api_info: Optional[Dict[str, str]] = None       # API 정보 (ID, 제목, URL 등)
    
    # HTTP 응답 정보
    status_code: int = 200                          # HTTP 상태 코드
    
    # 연속조회 관련 정보
    cont_yn: ContYn = ContYn.N                      # 연속조회 가능 여부
    next_key: Optional[str] = None                  # 다음 연속조회 키
    
    # 처리 시간 정보
    request_time: Optional[datetime] = None         # 요청 시간
    response_time: Optional[datetime] = None        # 응답 시간
    
    # 오류 정보
    error_code: Optional[str] = None                # 오류 코드
    error_message: Optional[str] = None             # 오류 메시지
    
    # 성공 여부
    success: bool = True                            # 요청 성공 여부

    class Config:
        """Pydantic 설정"""
        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None
        }

class KiwoomApiResult(BaseModel):
    """
    키움 API 처리 결과를 담는 통합 모델
    요청과 응답을 함께 관리할 때 사용합니다.
    """
    request: KiwoomRequest                          # 원본 요청 데이터
    response: KiwoomResponse                        # 응답 데이터
    
    # 처리 통계
    processing_time_ms: Optional[float] = None      # 처리 시간 (밀리초)
    retry_count: int = 0                           # 재시도 횟수
    
    # 로그 정보
    log_id: Optional[str] = None                   # 로그 추적 ID
    trace_id: Optional[str] = None                 # 분산 추적 ID

class KiwoomApiHelper:
    """
    키움 API 응답 처리를 담당하는 유틸리티 클래스
    성공/오류 응답 생성 및 요청 검증 기능을 제공합니다.
    """
    
    @staticmethod
    def create_success_response(
        data: Dict[str, Any], 
        headers: Optional[Dict[str, str]] = None,
        api_info: Optional[Dict[str, str]] = None,
        request_time: Optional[datetime] = None
    ) -> KiwoomResponse:
        """
        성공 응답 객체를 생성합니다.
        
        Args:
            data: API 응답 데이터
            headers: HTTP 응답 헤더
            api_info: API 메타 정보 (ID, 제목, URL 등)
            request_time: 요청 시작 시간
            
        Returns:
            KiwoomResponse: 성공 응답 객체
        """
        # 연속조회 정보를 헤더에서 추출
        cont_yn = ContYn.Y if headers and headers.get('cont-yn') == 'Y' else ContYn.N
        next_key = headers.get('next-key') if headers else None
        
        return KiwoomResponse(
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
        status_code: int = 500,
        api_info: Optional[Dict[str, str]] = None,
        request_time: Optional[datetime] = None
    ) -> KiwoomResponse:
        """
        오류 응답 객체를 생성합니다.
        
        Args:
            error_code: 키움 API 오류 코드
            error_message: 오류 상세 메시지
            status_code: HTTP 상태 코드 (기본값: 500)
            api_info: API 메타 정보
            request_time: 요청 시작 시간
            
        Returns:
            KiwoomResponse: 오류 응답 객체
        """
        return KiwoomResponse(
            data=None,
            status_code=status_code,
            error_code=error_code,
            error_message=error_message,
            api_info=api_info,
            success=False,
            request_time=request_time,
            response_time=datetime.now()
        )

    @staticmethod
    def validate_api_request(request: KiwoomRequest) -> bool:
        """
        API 요청의 유효성을 검증합니다.
        kiwi7_로 시작하는 api_id는 자체 API이므로 검증을 스킵합니다.
        
        Args:
            request: 검증할 키움 API 요청 객체
            
        Returns:
            bool: 유효성 검증 결과 (True: 유효, False: 유효하지 않음)
        """
        # kiwi7_로 시작하는 자체 API는 검증 스킵
        if request.api_id.startswith('kiwi7_'):
            return True
        
        # API ID 존재 여부 확인
        if request.api_id not in KIWOOM_REQUEST_DEF:
            return False
        
        # payload 유효성 검증
        validation_errors = request.validate_payload()
        if validation_errors:
            return False
        
        # 연속조회 키 검증
        if request.cont_yn == ContYn.Y and not request.next_key:
            return False
        
        return True

    @staticmethod
    def get_validation_errors(request: KiwoomRequest) -> List[str]:
        """
        API 요청의 유효성 검증 오류 목록을 반환합니다.
        kiwi7_로 시작하는 api_id는 자체 API이므로 검증을 스킵합니다.
        
        Args:
            request: 검증할 키움 API 요청 객체
            
        Returns:
            List[str]: 유효성 검증 오류 메시지 목록 (빈 리스트면 유효함)
        """
        errors = []
        
        # kiwi7_로 시작하는 자체 API는 검증 스킵
        if request.api_id.startswith('kiwi7_'):
            return errors
        
        # API ID 존재 여부 확인
        if request.api_id not in KIWOOM_REQUEST_DEF:
            errors.append(f"정의되지 않은 API ID입니다: {request.api_id}")
            return errors  # API ID가 없으면 더 이상 검증할 수 없음
        
        # payload 데이터 검증
        payload_errors = request.validate_payload()
        errors.extend(payload_errors)
        
        # 연속조회 키 검증
        if request.cont_yn == ContYn.Y and not request.next_key:
            errors.append("연속조회 요청 시 next_key가 필요합니다.")
        
        return errors

    @staticmethod
    def extract_output_data(response: KiwoomResponse, output_key: str = 'output') -> Optional[Dict[str, Any]]:
        """
        응답에서 실제 출력 데이터를 추출합니다.
        
        Args:
            response: 키움 API 응답 객체
            output_key: 출력 데이터 키 (기본값: 'output')
            
        Returns:
            Optional[Dict[str, Any]]: 추출된 출력 데이터 (없으면 None)
        """
        if not response.success or not response.data:
            return None
        
        return response.data.get(output_key)
    
    @staticmethod
    def has_more_data(response: KiwoomResponse) -> bool:
        """
        추가 데이터가 있는지 확인합니다 (연속조회 가능 여부).
        
        Args:
            response: 키움 API 응답 객체
            
        Returns:
            bool: 추가 데이터 존재 여부
        """
        return response.cont_yn == ContYn.Y and bool(response.next_key)
    
    @staticmethod
    def create_continuation_request(
        original_request: KiwoomRequest, 
        response: KiwoomResponse
    ) -> Optional[KiwoomRequest]:
        """
        연속조회를 위한 다음 요청을 생성합니다.
        
        Args:
            original_request: 원본 요청 객체
            response: 현재 응답 객체
            
        Returns:
            Optional[KiwoomRequest]: 연속조회 요청 객체 (연속조회가 불가능하면 None)
        """
        if not KiwoomApiHelper.has_more_data(response):
            return None
        
        # 기존 payload를 복사하여 새로운 연속조회 요청 생성
        continuation_payload = original_request.payload.copy()
        
        return KiwoomRequest(
            api_id=original_request.api_id,
            cont_yn=ContYn.Y,
            next_key=response.next_key,
            payload=continuation_payload
        )

    @staticmethod
    def get_request_info(api_id: str) -> Optional[Dict[str, str]]:
        """
        API ID에 해당하는 메타 정보를 KIWOOM_REQUEST_DEF에서 취득해서 반환합니다.
        
        Args:
            api_id: 조회할 API ID
            
        Returns:
            Optional[Dict[str, str]]: API 메타 정보 (없으면 None)
        """
        try:
            api_def = get_request_definition(api_id)
            return {
                'api_id': api_id,
                'title': api_def.get('title', ''),
                'url': api_def.get('url', ''),
                'method': api_def.get('method', 'POST'),
                'description': api_def.get('description', '')
            }
        except KeyError:
            return None
    
    @staticmethod
    def to_korea_data(response_data: Dict[str, Any], api_id: str) -> Dict[str, Any]:
        """
        키움 API 응답 데이터를 한글 필드명으로 변환합니다.
        
        Args:
            response_data: 키움 API 응답 데이터
            api_id: API ID
            
        Returns:
            Dict[str, Any]: 한글 필드명으로 변환된 데이터
        """
        try:
            # 응답 정의에서 필드 매핑 정보 가져오기
            response_fields = KIWOOM_RESPONSE_DEF.get(api_id, [])
            if not response_fields:
                return response_data  # 정의가 없으면 원본 데이터 반환
            
            # 영문 key -> 한글 name 매핑 테이블 생성
            key_to_name_map = {field['key']: field['name'] for field in response_fields}
            
            korea_data = {}
            
            # response_data가 딕셔너리인 경우
            if isinstance(response_data, dict):
                for key, value in response_data.items():
                    # 한글 필드명이 있으면 변환, 없으면 원본 키 사용
                    # value가 list이면
                    if isinstance(value, list):
                        # 리스트인 경우 각 항목에 대해 한글 필드명으로 변환
                        korean_list = []
                        for item in value:
                            if isinstance(item, dict):
                                korean_item = {}
                                for item_key, item_value in item.items():
                                    korean_item[key_to_name_map.get(item_key, item_key)] = item_value
                                korean_list.append(korean_item)
                            else:
                                korean_list.append(item)
                        korean_key = key_to_name_map.get(key, key)
                        korea_data[korean_key] = korean_list

                    else:
                        korean_key = key_to_name_map.get(key, key)
                        korea_data[korean_key] = value
            
            # response_data가 리스트인 경우 (여러 레코드)
            elif isinstance(response_data, list):
                korea_data = []
                for item in response_data:
                    if isinstance(item, dict):
                        korean_item = {}
                        for key, value in item.items():
                            korean_key = key_to_name_map.get(key, key)
                            korean_item[korean_key] = value
                        korea_data.append(korean_item)
                    else:
                        korea_data.append(item)
            else:
                # 딕셔너리나 리스트가 아닌 경우 원본 반환
                return response_data
            
            return korea_data
            
        except Exception:
            # 변환 중 오류 발생 시 원본 데이터 반환
            return response_data