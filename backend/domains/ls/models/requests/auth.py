# Auto-generated
from typing import Any, Dict, List

AUTH_REQUESTS = {
    'revoke': {
        'tr_cd': 'revoke',
        'title': '접근토큰 폐기',
        'fields': [
            {
                'desc': '포탈에서 발급된 고객의 앱Key ',
                'key': 'appkey',
                'length': '100',
                'name': '고객 앱Key',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '포탈에서 발급된 고객의 앱 비밀Key',
                'key': 'appsecretkey',
                'length': '36',
                'name': '고객 앱 비밀Key',
                'required': True,
                'type': 'string'
            },
            {
                'desc': 'access_token, refresh_token 토큰 타입',
                'key': 'token_type_hint',
                'length': '36',
                'name': '토큰 유형 hint',
                'required': True,
                'type': 'string'
            },
            {
                'desc': 'G/W 에서 발급하는 접근토큰',
                'key': 'token',
                'length': '256',
                'name': '접근토큰',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'token': {
        'tr_cd': 'token',
        'title': '접근토큰 발급',
        'fields': [
            {
                'desc': '"client_credentials" 고정',
                'key': 'grant_type',
                'length': '100',
                'name': '권한부여  Type',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '포탈에서 발급된 고객의 앱Key ',
                'key': 'appkey',
                'length': '36',
                'name': '고객 앱Key',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '포탈에서 발급된 고객의 앱 비밀Key',
                'key': 'appsecretkey',
                'length': '36',
                'name': '고객 앱 비밀Key',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '"oob" 고정',
                'key': 'scope',
                'length': '256',
                'name': 'scope',
                'required': True,
                'type': 'string'
            }
        ]
    }
}
