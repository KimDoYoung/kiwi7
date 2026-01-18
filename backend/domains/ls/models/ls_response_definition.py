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


def get_response_fields(api_id: str) -> list:
    """API ID로 응답 필드 정의(목록) 조회"""
    resp_def = LS_RESPONSE_DEF.get(api_id)
    if resp_def and isinstance(resp_def, dict):
        return resp_def.get('fields', [])
    return []


def get_field_name(api_id: str, key: str) -> str:
    """필드 키의 한글 이름 반환"""
    fields = get_response_fields(api_id)
    
    for field in fields:
        if isinstance(field, dict) and field.get('key') == key:
            return field.get('name', key)
    return key
