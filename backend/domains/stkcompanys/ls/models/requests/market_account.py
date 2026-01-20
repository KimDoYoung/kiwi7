# Auto-generated
from typing import Any, Dict, List

MARKET_ACCOUNT_REQUESTS = {
    't0150': {
        'tr_cd': 't0150',
        'title': '주식당일매매일지/수수료',
        'blocks': {
            't0150InBlock': {
                'fields': [{'key': 'cts_medosu', 'name': 'CTS_매매구분', 'type': 'string', 'length': 1, 'desc': '연속조회시 OutBlock의 동일필드 입력', 'required': True}, {'key': 'cts_expcode', 'name': 'CTS_종목번호', 'type': 'string', 'length': 12, 'desc': '연속조회시 OutBlock의 동일필드 입력', 'required': True}, {'key': 'cts_price', 'name': 'CTS_단가', 'type': 'string', 'length': 9, 'desc': '연속조회시 OutBlock의 동일필드 입력', 'required': True}, {'key': 'cts_middiv', 'name': 'CTS_매체', 'type': 'string', 'length': 2, 'desc': '연속조회시 OutBlock의 동일필드 입력', 'required': True}],
                'type': 'single'
            }
        }
    },
    't0151': {
        'tr_cd': 't0151',
        'title': '주식당일매매일지/수수료(전일)',
        'blocks': {
            't0151InBlock': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_medosu', 'name': 'CTS_매매구분', 'type': 'string', 'length': 1, 'desc': '연속조회시 OutBlock의 동일필드 입력', 'required': True}, {'key': 'cts_expcode', 'name': 'CTS_종목번호', 'type': 'string', 'length': 12, 'desc': '연속조회시 OutBlock의 동일필드 입력', 'required': True}, {'key': 'cts_price', 'name': 'CTS_단가', 'type': 'string', 'length': 9, 'desc': '연속조회시 OutBlock의 동일필드 입력', 'required': True}, {'key': 'cts_middiv', 'name': 'CTS_매체', 'type': 'string', 'length': 2, 'desc': '연속조회시 OutBlock의 동일필드 입력', 'required': True}],
                'type': 'single'
            }
        }
    },
    't0167': {
        'tr_cd': 't0167',
        'title': '서버시간조회',
        'blocks': {
            't0167InBlock': {
                'fields': [{'key': 'id', 'name': 'id', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't0424': {
        'tr_cd': 't0424',
        'title': '주식잔고2',
        'blocks': {
            't0424InBlock': {
                'fields': [{'key': 'prcgb', 'name': '단가구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'chegb', 'name': '체결구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'dangb', 'name': '단일가구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'charge', 'name': '제비용포함여부', 'type': 'string', 'length': 1, 'required': True}, {'key': 'cts_expcode', 'name': 'CTS_종목번호', 'type': 'string', 'length': 22, 'desc': '연속조회시 OutBlock의 동일필드 입력', 'required': True}],
                'type': 'single'
            }
        }
    },
    't0425': {
        'tr_cd': 't0425',
        'title': '주식체결/미체결',
        'blocks': {
            't0425InBlock': {
                'fields': [{'key': 'expcode', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'chegb', 'name': '체결구분', 'type': 'string', 'length': 1, 'desc': '0;전체<br/>1:체결<br/>2:미체결', 'required': True}, {'key': 'medosu', 'name': '매매구분', 'type': 'string', 'length': 1, 'desc': '0:전체<br/>1:매도<br/>2:매수', 'required': True}, {'key': 'sortgb', 'name': '정렬순서', 'type': 'string', 'length': 1, 'desc': '1:주문번호 역순<br/>2:주문번호 순', 'required': True}, {'key': 'cts_ordno', 'name': '주문번호', 'type': 'string', 'length': 10, 'desc': '연속조회시 OutBlock의 동일필드 입력', 'required': True}],
                'type': 'single'
            }
        }
    }
}
