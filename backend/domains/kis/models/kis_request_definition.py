"""Auto-generated definition file"""
from typing import Any, Dict, List

from .requests.kis_req_1 import KIS_REQUEST_DEF_1
from .requests.kis_req_2 import KIS_REQUEST_DEF_2
from .requests.kis_req_3 import KIS_REQUEST_DEF_3
from .requests.kis_req_4 import KIS_REQUEST_DEF_4
from .requests.kis_req_5 import KIS_REQUEST_DEF_5
from .requests.kis_req_6 import KIS_REQUEST_DEF_6
from .requests.kis_req_7 import KIS_REQUEST_DEF_7

KIS_REQUEST_DEF = {}
KIS_REQUEST_DEF.update(KIS_REQUEST_DEF_1)
KIS_REQUEST_DEF.update(KIS_REQUEST_DEF_2)
KIS_REQUEST_DEF.update(KIS_REQUEST_DEF_3)
KIS_REQUEST_DEF.update(KIS_REQUEST_DEF_4)
KIS_REQUEST_DEF.update(KIS_REQUEST_DEF_5)
KIS_REQUEST_DEF.update(KIS_REQUEST_DEF_6)
KIS_REQUEST_DEF.update(KIS_REQUEST_DEF_7)

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
