# Auto-generated
from typing import Any, Dict, List

MARKET_OVERSEAS_REQUESTS = {
    'AS0': {
        'tr_cd': 'AS0',
        'title': '해외주식주문접수(미국)',
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
                'key': 'tr_key',
                'length': 8,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'AS1': {
        'tr_cd': 'AS1',
        'title': '해외주식주문체결(미국)',
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
                'key': 'tr_key',
                'length': 8,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'AS2': {
        'tr_cd': 'AS2',
        'title': '해외주식주문정정(미국)',
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
                'key': 'tr_key',
                'length': 8,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'AS3': {
        'tr_cd': 'AS3',
        'title': '해외주식주문취소(미국)',
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
                'key': 'tr_key',
                'length': 8,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'AS4': {
        'tr_cd': 'AS4',
        'title': '해외주식주문거부(미국)',
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
                'key': 'tr_key',
                'length': 8,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'GSC': {
        'tr_cd': 'GSC',
        'title': '해외주식 체결',
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
                'desc': 'Key 종목코드 + 18자리에서 남은 자릿수만큼 공백<br/>ex) \'82TSLA            \' <br/>\'82TSLA\' + 공백 12자리',
                'key': 'tr_key',
                'length': 18,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'GSH': {
        'tr_cd': 'GSH',
        'title': '해외주식 호가',
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
                'desc': 'Key 종목코드 + 남은 자릿수만큼 공백<br/>ex) \'82TSLA            \' <br/>\'82TSLA\' + 공백 12자리',
                'key': 'tr_key',
                'length': 18,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'OVC': {
        'tr_cd': 'OVC',
        'title': '해외선물 체결',
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
    'OVH': {
        'tr_cd': 'OVH',
        'title': '해외선물 호가',
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
    'TC1': {
        'tr_cd': 'TC1',
        'title': '해외선물 주문접수',
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
    'TC2': {
        'tr_cd': 'TC2',
        'title': '해외선물 주문응답',
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
    'TC3': {
        'tr_cd': 'TC3',
        'title': '해외선물 주문체결',
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
    'WOC': {
        'tr_cd': 'WOC',
        'title': '해외옵션 체결',
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
    'WOH': {
        'tr_cd': 'WOH',
        'title': '해외옵션 호가',
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
}
