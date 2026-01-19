# Auto-generated
from typing import Any, Dict, List

AUTH_RESPONSES = {
    'token': {'tr_cd': 'token', 'title': '접근토큰 발급', 'fields': [{'key': 'access_token', 'name': '접근토큰', 'type': 'string', 'length': 1000, 'desc': 'G/W 에서 발급하는 접근토큰', 'required': True}, {'key': 'expire_in', 'name': '접근토큰 유효기간', 'type': 'string', 'length': 10, 'desc': '유효기간(초)', 'required': True}, {'key': 'scope', 'name': 'scope', 'type': 'string', 'length': 256, 'desc': '"oob" 고정', 'required': True}, {'key': 'token_type', 'name': '토큰 유형', 'type': 'string', 'length': 256, 'desc': 'Bearer', 'required': True}]},
    'revoke': {'tr_cd': 'revoke', 'title': '접근토큰 폐기', 'fields': [{'key': 'code', 'name': '응답코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'message', 'name': '응답메시지', 'type': 'string', 'length': 100, 'desc': '응답메시지', 'required': True}]},
}
