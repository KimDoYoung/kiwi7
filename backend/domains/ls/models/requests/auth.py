from typing import Any, Dict, List

AUTH_REQUESTS = {
    'token': {'tr_cd': 'token', 'title': '접근토큰 발급', 'fields': [{'key': 'grant_type', 'name': '권한부여  Type', 'type': 'string', 'length': '100', 'desc': '"client_credentials" 고정', 'required': True}, {'key': 'appkey', 'name': '고객 앱Key', 'type': 'string', 'length': '36', 'desc': '포탈에서 발급된 고객의 앱Key ', 'required': True}, {'key': 'appsecretkey', 'name': '고객 앱 비밀Key', 'type': 'string', 'length': '36', 'desc': '포탈에서 발급된 고객의 앱 비밀Key', 'required': True}, {'key': 'scope', 'name': 'scope', 'type': 'string', 'length': '256', 'desc': '"oob" 고정', 'required': True}]},
    'revoke': {'tr_cd': 'revoke', 'title': '접근토큰 폐기', 'fields': [{'key': 'appkey', 'name': '고객 앱Key', 'type': 'string', 'length': '100', 'desc': '포탈에서 발급된 고객의 앱Key ', 'required': True}, {'key': 'appsecretkey', 'name': '고객 앱 비밀Key', 'type': 'string', 'length': '36', 'desc': '포탈에서 발급된 고객의 앱 비밀Key', 'required': True}, {'key': 'token_type_hint', 'name': '토큰 유형 hint', 'type': 'string', 'length': '36', 'desc': 'access_token, refresh_token 토큰 타입', 'required': True}, {'key': 'token', 'name': '접근토큰', 'type': 'string', 'length': '256', 'desc': 'G/W 에서 발급하는 접근토큰', 'required': True}]},
}
