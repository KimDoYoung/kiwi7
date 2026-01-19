"""Auto-generated definition file"""
from typing import Any, Dict

from .responses.kis_resp_1 import KIS_RESPONSE_DEF_1
from .responses.kis_resp_2 import KIS_RESPONSE_DEF_2
from .responses.kis_resp_3 import KIS_RESPONSE_DEF_3
from .responses.kis_resp_4 import KIS_RESPONSE_DEF_4
from .responses.kis_resp_5 import KIS_RESPONSE_DEF_5
from .responses.kis_resp_6 import KIS_RESPONSE_DEF_6
from .responses.kis_resp_7 import KIS_RESPONSE_DEF_7

KIS_RESPONSE_DEF = {}
KIS_RESPONSE_DEF.update(KIS_RESPONSE_DEF_1)
KIS_RESPONSE_DEF.update(KIS_RESPONSE_DEF_2)
KIS_RESPONSE_DEF.update(KIS_RESPONSE_DEF_3)
KIS_RESPONSE_DEF.update(KIS_RESPONSE_DEF_4)
KIS_RESPONSE_DEF.update(KIS_RESPONSE_DEF_5)
KIS_RESPONSE_DEF.update(KIS_RESPONSE_DEF_6)
KIS_RESPONSE_DEF.update(KIS_RESPONSE_DEF_7)

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
