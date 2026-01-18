"""Auto-generated definition file"""
from typing import Any, Dict, List

from .requests.market import MARKET_REQUESTS
from .requests.market_etf import MARKET_ETF_REQUESTS
from .requests.market_realtime import MARKET_REALTIME_REQUESTS
from .requests.trading import TRADING_REQUESTS

KIS_REQUEST_DEF = {}
KIS_REQUEST_DEF.update(MARKET_REQUESTS)
KIS_REQUEST_DEF.update(TRADING_REQUESTS)
KIS_REQUEST_DEF.update(MARKET_ETF_REQUESTS)
KIS_REQUEST_DEF.update(MARKET_REALTIME_REQUESTS)

def get_request_definition(api_id: str) -> Dict[str, Any]:
    return KIS_REQUEST_DEF.get(api_id)

def get_required_fields(api_id: str) -> List[str]:
    api_def = KIS_REQUEST_DEF.get(api_id, {})
    body = api_def.get('body', [])
    return [field['key'] for field in body if field.get('required', False)]
    
def get_tr_id(api_id: str, is_virtual: bool = False) -> str:
    api_def = KIS_REQUEST_DEF.get(api_id, {})
    tr_id = api_def.get('tr_id', api_id)
    if is_virtual and tr_id and tr_id.startswith('T'):
        return 'V' + tr_id[1:]
    return tr_id

def is_hashkey_required(api_id: str) -> bool:
    api_def = KIS_REQUEST_DEF.get(api_id, {})
    return api_def.get('hashkey_required', False)
