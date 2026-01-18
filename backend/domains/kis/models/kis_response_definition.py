"""Auto-generated definition file"""
from typing import Any, Dict, List

from .responses.market import MARKET_RESPONSES
from .responses.trading import TRADING_RESPONSES
from .responses.misc import MISC_RESPONSES

KIS_RESPONSE_DEF = {}
KIS_RESPONSE_DEF.update(MARKET_RESPONSES)
KIS_RESPONSE_DEF.update(TRADING_RESPONSES)
KIS_RESPONSE_DEF.update(MISC_RESPONSES)

def get_response_definition(api_id: str) -> Dict[str, Any]:
    return KIS_RESPONSE_DEF.get(api_id)

def get_response_fields(api_id: str) -> list:
    resp = get_response_definition(api_id)
    if resp and 'output' in resp and 'fields' in resp['output']:
        return resp['output']['fields']
    # Fallback for flat structure?
    if resp and 'fields' in resp: 
        return resp['fields']
    return []

def get_field_name(api_id: str, key: str) -> str:
    fields = get_response_fields(api_id)
    for field in fields:
        if field.get('key') == key:
            return field.get('name', key)
    return key
