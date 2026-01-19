# Auto-generated
from typing import Any, Dict, List

AUTH_RESPONSES = {
    'revoke': {
        'tr_cd': 'revoke',
        'title': '접근토큰 폐기',
        'fields': [
            {
                'key': 'code',
                'length': 3,
                'name': '응답코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '응답메시지',
                'key': 'message',
                'length': 100,
                'name': '응답메시지',
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
                'desc': 'G/W 에서 발급하는 접근토큰',
                'key': 'access_token',
                'length': 1000,
                'name': '접근토큰',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '유효기간(초)',
                'key': 'expire_in',
                'length': 10,
                'name': '접근토큰 유효기간',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '"oob" 고정',
                'key': 'scope',
                'length': 256,
                'name': 'scope',
                'required': True,
                'type': 'string'
            },
            {
                'desc': 'Bearer',
                'key': 'token_type',
                'length': 256,
                'name': '토큰 유형',
                'required': True,
                'type': 'string'
            }
        ]
    }
}
