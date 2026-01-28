"""
LS증권 API 요청 정의
API 문서: https://openapi.ls-sec.co.kr/apiservice
"""
from typing import Any, Dict, List

from .requests.account import ACCOUNT_REQUESTS
from .requests.auth import AUTH_REQUESTS
from .requests.market_original import MARKET_REQUESTS
from .requests.market_account import MARKET_ACCOUNT_REQUESTS
from .requests.market_chart import MARKET_CHART_REQUESTS
from .requests.market_derivatives_account import MARKET_DERIVATIVES_ACCOUNT_REQUESTS
from .requests.market_derivatives_query import MARKET_DERIVATIVES_QUERY_REQUESTS
from .requests.market_derivatives_realtime import MARKET_DERIVATIVES_REALTIME_REQUESTS
from .requests.market_elw import MARKET_ELW_REQUESTS
from .requests.market_etf import MARKET_ETF_REQUESTS
from .requests.market_foreign_institutional import MARKET_FOREIGN_INSTITUTIONAL_REQUESTS
from .requests.market_future_original import MARKET_FUTURE_REQUESTS
from .requests.market_order_execution import MARKET_ORDER_EXECUTION_REQUESTS
from .requests.market_other import MARKET_OTHER_REQUESTS
from .requests.market_overseas_futures import MARKET_OVERSEAS_FUTURES_REQUESTS
from .requests.market_overseas_original import MARKET_OVERSEAS_REQUESTS
from .requests.market_overseas_stocks import MARKET_OVERSEAS_STOCKS_REQUESTS
from .requests.market_overseas_realtime import MARKET_OVERSEAS_REALTIME_REQUESTS
from .requests.market_preferred_bond import MARKET_PREFERRED_BOND_REQUESTS
from .requests.market_price_tick import MARKET_PRICE_TICK_REQUESTS
from .requests.market_statistics_ranking import MARKET_STATISTICS_RANKING_REQUESTS
from .requests.market_stock_info import MARKET_STOCK_INFO_REQUESTS

LS_REQUEST_DEF = {}
LS_REQUEST_DEF.update(AUTH_REQUESTS)
LS_REQUEST_DEF.update(ACCOUNT_REQUESTS)
LS_REQUEST_DEF.update(MARKET_REQUESTS)
LS_REQUEST_DEF.update(MARKET_ACCOUNT_REQUESTS)
LS_REQUEST_DEF.update(MARKET_CHART_REQUESTS)
LS_REQUEST_DEF.update(MARKET_DERIVATIVES_ACCOUNT_REQUESTS)
LS_REQUEST_DEF.update(MARKET_DERIVATIVES_QUERY_REQUESTS)
LS_REQUEST_DEF.update(MARKET_DERIVATIVES_REALTIME_REQUESTS)
LS_REQUEST_DEF.update(MARKET_ELW_REQUESTS)
LS_REQUEST_DEF.update(MARKET_ETF_REQUESTS)
LS_REQUEST_DEF.update(MARKET_FOREIGN_INSTITUTIONAL_REQUESTS)
LS_REQUEST_DEF.update(MARKET_FUTURE_REQUESTS)
LS_REQUEST_DEF.update(MARKET_ORDER_EXECUTION_REQUESTS)
LS_REQUEST_DEF.update(MARKET_OTHER_REQUESTS)
LS_REQUEST_DEF.update(MARKET_OVERSEAS_FUTURES_REQUESTS)
LS_REQUEST_DEF.update(MARKET_OVERSEAS_REQUESTS)
LS_REQUEST_DEF.update(MARKET_OVERSEAS_STOCKS_REQUESTS)
LS_REQUEST_DEF.update(MARKET_OVERSEAS_REALTIME_REQUESTS)
LS_REQUEST_DEF.update(MARKET_PREFERRED_BOND_REQUESTS)
LS_REQUEST_DEF.update(MARKET_PRICE_TICK_REQUESTS)
LS_REQUEST_DEF.update(MARKET_STATISTICS_RANKING_REQUESTS)
LS_REQUEST_DEF.update(MARKET_STOCK_INFO_REQUESTS)


def get_request_definition(api_id: str) -> Dict[str, Any]:
    """API ID로 정의 조회"""
    if api_id not in LS_REQUEST_DEF:
        return None
    return LS_REQUEST_DEF[api_id]


def get_required_fields(api_id: str) -> List[str]:
    """필수 필드 목록 반환"""
    api_def = LS_REQUEST_DEF.get(api_id, {})
    body = api_def.get('body', [])
    return [field['key'] for field in body if field.get('required', False)]


def get_tr_cd(api_id: str) -> str:
    """TR 코드 반환"""
    api_def = LS_REQUEST_DEF.get(api_id, {})
    return api_def.get('tr_cd', api_id)