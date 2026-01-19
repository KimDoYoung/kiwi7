# Auto-generated
from typing import Any, Dict, List

MARKET_PRICE_TICK_REQUESTS = {
    't1301': {
        'tr_cd': 't1301',
        'title': '주식시간대별체결조회',
        'blocks': {
            't1301InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'cvolume', 'name': '특이거래량', 'type': 'float', 'length': 12, 'desc': '거래량 > 특이거래량', 'required': True}, {'key': 'starttime', 'name': '시작시간', 'type': 'string', 'length': 4, 'desc': '장시작시간 이후', 'required': True}, {'key': 'endtime', 'name': '종료시간', 'type': 'string', 'length': 4, 'desc': '장종료시간 이전', 'required': True}, {'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 10, 'desc': '연속조회시 OutBlock의 동일필드 입력', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1302': {
        'tr_cd': 't1302',
        'title': '주식분별주가조회',
        'blocks': {
            't1302InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'gubun', 'name': '작업구분', 'type': 'string', 'length': 1, 'desc': '0:30초<br/>1:1분<br/>2:3분<br/>3:5분<br/>4:10분<br/>5:30분<br/>6:60분', 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 cts_time 값으로 설정', 'required': True}, {'key': 'cnt', 'name': '건수', 'type': 'float', 'length': 3, 'desc': '1이상 900 이하', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1305': {
        'tr_cd': 't1305',
        'title': '기간별주가',
        'blocks': {
            't1305InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dwmcode', 'name': '일주월구분', 'type': 'float', 'length': 1, 'desc': '1@일, 2@주, 3@월', 'required': True}, {'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 date 값으로 설정<br/>', 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'desc': '사용안함(Space)', 'required': True}, {'key': 'cnt', 'name': '건수', 'type': 'float', 'length': 4, 'desc': '1 이상', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1308': {
        'tr_cd': 't1308',
        'title': '주식시간대별체결조회챠트',
        'blocks': {
            't1308InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'starttime', 'name': '시작시간', 'type': 'string', 'length': 4, 'desc': '장시작시간 이후(hhmm)', 'required': True}, {'key': 'endtime', 'name': '종료시간', 'type': 'string', 'length': 4, 'desc': '장종료시간 이전(hhmm)', 'required': True}, {'key': 'bun_term', 'name': '분간격', 'type': 'string', 'length': 2, 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리<br/>', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1310': {
        'tr_cd': 't1310',
        'title': '주식당일전일분틱조회',
        'blocks': {
            't1310InBlock': {
                'fields': [{'key': 'daygb', 'name': '당일전일구분', 'type': 'string', 'length': 1, 'desc': '0:당일<br/>1:전일', 'required': True}, {'key': 'timegb', 'name': '분틱구분', 'type': 'string', 'length': 1, 'desc': '0:분<br/>1:틱', 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'endtime', 'name': '종료시간', 'type': 'string', 'length': 4, 'desc': '처음 조회시 시간 입력값.<br/>t1310OutBlock1.chetime <= endtime 인 데이터 조회됨.', 'required': True}, {'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 10, 'desc': '처음 조회시 Space<br/>다음 조회시 t1310OutBlock.cts_time 값 입력', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리<br/>', 'required': True}],
                'type': 'single'
            }
        }
    }
}
