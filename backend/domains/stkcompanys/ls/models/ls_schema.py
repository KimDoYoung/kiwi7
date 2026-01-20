"""
LS증권 스키마 정의
API 요청/응답 모델 및 유틸리티 클래스를 정의합니다.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional

from backend.domains.base.base_schema import BaseRequest, BaseResponse, ContYn
from backend.domains.stkcompanys.ls.models.ls_request_definition import (
  LS_REQUEST_DEF,
  get_request_definition,
  get_required_fields,
)
from backend.domains.stkcompanys.ls.models.ls_response_definition import LS_RESPONSE_DEF


class LsRequest(BaseRequest):
  """LS API 요청 모델"""

  def validate_payload(self) -> List[str]:
    """payload의 유효성을 검증"""
    # 커스텀 API는 검증 스킵
    if self.api_id.startswith('kiwi7_'):
      return []

    api_def = get_request_definition(self.api_id)
    if not api_def:
      return [f'정의되지 않은 API ID: {self.api_id}']

    errors = []
    required_fields = get_required_fields(self.api_id)

    for field in required_fields:
      if field not in self.payload:
        errors.append(f'필수 필드 누락: {field}')

    return errors


class LsResponse(BaseResponse):
  """LS API 응답 모델"""

  pass


class LsApiHelper:
  """LS API 유틸리티 클래스"""

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
      'method': api_def.get('method', 'POST'),
      'tr_cd': api_def.get('tr_cd', api_id),
    }

  @staticmethod
  def validate_api_request(request: LsRequest) -> bool:
    """API 요청 유효성 검증"""
    if request.api_id.startswith('kiwi7_'):
      return True

    if request.api_id not in LS_REQUEST_DEF:
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
    request_time: datetime = None,
  ) -> LsResponse:
    """성공 응답 생성"""
    cont_yn = ContYn.N
    next_key = None

    # LS 연속조회 처리
    if data:
      # t1102OutBlock 등의 형태에서 연속조회 키 추출
      if data.get('tr_cont') == 'Y':
        cont_yn = ContYn.Y
      for key in data:
        if key.endswith('OutBlock') and isinstance(data[key], dict):
          cts = (
            data[key].get('cts_expcode') or data[key].get('cts_ordno') or data[key].get('cts_time')
          )
          if cts:
            next_key = cts
            cont_yn = ContYn.Y
            break

    return LsResponse(
      data=data,
      headers=headers,
      api_info=api_info,
      status_code=200,
      cont_yn=cont_yn,
      next_key=next_key,
      success=True,
      request_time=request_time,
      response_time=datetime.now(),
    )

  @staticmethod
  def create_error_response(
    error_code: str,
    error_message: str,
    api_info: Dict[str, str] = None,
    request_time: datetime = None,
  ) -> LsResponse:
    """에러 응답 생성"""
    return LsResponse(
      data=None,
      api_info=api_info,
      status_code=int(error_code) if error_code.isdigit() else 500,
      error_code=error_code,
      error_message=error_message,
      success=False,
      request_time=request_time,
      response_time=datetime.now(),
    )

  @staticmethod
  def to_korea_data(response_data: Dict[str, Any], api_id: str) -> Dict[str, Any]:
    """영문 필드명을 한글로 변환"""
    response_def = LS_RESPONSE_DEF.get(api_id, {})
    if not response_def:
      return response_data

    # 모든 block의 fields를 통합하여 key_to_name_map 생성
    key_to_name_map = {}

    # response_def에서 blocks 구조 파싱
    blocks = response_def.get('blocks', {})
    for block_name, block_value in blocks.items():
      if isinstance(block_value, dict) and 'fields' in block_value:
        for field in block_value['fields']:
          if 'key' in field and 'name' in field:
            key_to_name_map[field['key']] = field['name']

    if not key_to_name_map:
      return response_data

    def convert_dict(data: Dict) -> Dict:
      korea_data = {}
      for key, value in data.items():
        korean_key = key_to_name_map.get(key, key)
        if isinstance(value, dict):
          korea_data[korean_key] = convert_dict(value)
        elif isinstance(value, list):
          korea_data[korean_key] = [
            convert_dict(item) if isinstance(item, dict) else item for item in value
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
  def has_more_data(response: LsResponse) -> bool:
    """연속조회 가능 여부 확인"""
    return response.cont_yn == ContYn.Y and bool(response.next_key)
