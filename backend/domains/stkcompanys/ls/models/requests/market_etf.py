# Auto-generated
from typing import Any, Dict, List

MARKET_ETF_REQUESTS = {
    'B7_': {
        'tr_cd': 'B7_',
        'title': 'ETF호가잔량',
        'fields': [
            {
                'desc': 'LS증권 거래코드',
                'key': 'tr_cd',
                'length': 3,
                'name': '거래 CD',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '단축코드 6자리 또는 8자리 (단건, 연속), (계좌등록/해제 일 경우 필수값 아님)',
                'key': 'tr_key',
                'length': 8,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'I5_': {
        'tr_cd': 'I5_',
        'title': '코스피ETF종목실시간NAV',
        'fields': [
            {
                'desc': 'LS증권 거래코드',
                'key': 'tr_cd',
                'length': 3,
                'name': '거래 CD',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '단축코드 6자리 또는 8자리 (단건, 연속), (계좌등록/해제 일 경우 필수값 아님)',
                'key': 'tr_key',
                'length': 8,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    't1901': {
        'tr_cd': 't1901',
        'title': 'ETF현재가(시세)조회',
        'blocks': {
            't1901InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1902': {
        'tr_cd': 't1902',
        'title': 'ETF시간별추이',
        'blocks': {
            't1902InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'desc': '연속조회키 연속 조회시 이 값을 InBlock의 time 필드에 넣어준다.', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1903': {
        'tr_cd': 't1903',
        'title': 'ETF일별추이',
        'blocks': {
            't1903InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'desc': '연속조회키 연속 조회시 이 값을 InBlock의 date 필드에 넣어준다.', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1904': {
        'tr_cd': 't1904',
        'title': 'ETF구성종목조회',
        'blocks': {
            't1904InBlock': {
                'fields': [{'key': 'shcode', 'name': 'ETF단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'date', 'name': 'PDF적용일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'sgb', 'name': '정렬기준(1:평가금액2:증권수)', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1906': {
        'tr_cd': 't1906',
        'title': 'ETFLP호가',
        'blocks': {
            't1906InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            }
        }
    }
}
