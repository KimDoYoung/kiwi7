# Auto-generated
from typing import Any, Dict, List

MARKET_STOCK_INFO_REQUESTS = {
    't1101': {
        'tr_cd': 't1101',
        'title': '주식현재가호가조회',
        'blocks': {
            't1101InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1102': {
        'tr_cd': 't1102',
        'title': '주식현재가(시세)조회',
        'blocks': {
            't1102InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리<br/>', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1104': {
        'tr_cd': 't1104',
        'title': '주식현재가시세메모',
        'blocks': {
            't1104InBlock': {
                'fields': [{'key': 'code', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'nrec', 'name': '건수', 'type': 'string', 'length': 2, 'desc': 't1104InBlock1 의 개수', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': ' K: KRX<br/> N: NXT<br/> U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            },
            't1104InBlock1': {
                'fields': [{'key': 'indx', 'name': '인덱스', 'type': 'string', 'length': 1, 'desc': 't1104InBlock1 의 Occurs Index(0부터 시작)', 'required': True}, {'key': 'gubn', 'name': '조건구분', 'type': 'string', 'length': 1, 'desc': '1:시세<br/>2:최고저가<br/>3:Pivot<br/>4:이동평균선', 'required': True}, {'key': 'dat1', 'name': '데이타1', 'type': 'string', 'length': 1, 'desc': '1:시가<br/>2:고가<br/>3:저가<br/>4:가중평균가', 'required': True}, {'key': 'dat2', 'name': '데이타2', 'type': 'string', 'length': 8, 'desc': '1:당일<br/>2:전일', 'required': True}],
                'type': 'array'
            }
        }
    },
    't1105': {
        'tr_cd': 't1105',
        'title': '주식피봇/디마크조회',
        'blocks': {
            't1105InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리<br/>', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1109': {
        'tr_cd': 't1109',
        'title': '시간외체결량',
        'blocks': {
            't1109InBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dan_chetime', 'name': '체결cts', 'type': 'string', 'length': 10, 'desc': '연속조회시 OutBlock의 동일필드 입력', 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'desc': '연속조회시 OutBlock의 동일필드 입력', 'required': True}],
                'type': 'single'
            }
        }
    }
}
