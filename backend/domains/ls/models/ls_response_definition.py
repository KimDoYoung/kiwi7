"""
LS증권 API 응답 정의
각 API별 응답 필드 매핑을 정의합니다.
"""

from .responses.account import ACCOUNT_RESPONSES
from .responses.auth import AUTH_RESPONSES
from .responses.market import MARKET_RESPONSES
from .responses.market_elw import MARKET_ELW_RESPONSES
from .responses.market_etf import MARKET_ETF_RESPONSES
from .responses.market_future import MARKET_FUTURE_RESPONSES
from .responses.market_overseas import MARKET_OVERSEAS_RESPONSES

LS_RESPONSE_DEF = {}
LS_RESPONSE_DEF.update(AUTH_RESPONSES)
LS_RESPONSE_DEF.update(ACCOUNT_RESPONSES)
LS_RESPONSE_DEF.update(MARKET_RESPONSES)
LS_RESPONSE_DEF.update(MARKET_OVERSEAS_RESPONSES)
LS_RESPONSE_DEF.update(MARKET_FUTURE_RESPONSES)
LS_RESPONSE_DEF.update(MARKET_ELW_RESPONSES)
LS_RESPONSE_DEF.update(MARKET_ETF_RESPONSES)


def get_response_definition(api_id: str) -> dict:
  """API 응답 정의 조회"""
  return LS_RESPONSE_DEF.get(api_id, {})


def get_response_fields(api_id: str) -> list:
  """API의 모든 block 필드를 통합하여 반환"""
  resp_def = get_response_definition(api_id)
  if not resp_def:
    return []

  fields = []
  # blocks 구조에서 모든 필드 수집
  blocks = resp_def.get('blocks', {})
  for block_name, block_value in blocks.items():
    if isinstance(block_value, dict) and 'fields' in block_value:
      fields.extend(block_value['fields'])

  return fields


def get_field_name(api_id: str, key: str) -> str:
  """필드 키의 한글 이름 반환"""
  fields = get_response_fields(api_id)

  for field in fields:
    if isinstance(field, dict) and field.get('key') == key:
      return field.get('name', key)
  return key
