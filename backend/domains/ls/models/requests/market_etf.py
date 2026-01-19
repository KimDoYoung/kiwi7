# Auto-generated
from typing import Any, Dict, List

MARKET_ETF_REQUESTS = {
    't1901': {'tr_cd': 't1901', 'title': 'ETF현재가(시세)조회', 'blocks': {'t1901InBlock': {'type': 'single', 'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}]}}},
    't1902': {'tr_cd': 't1902', 'title': 'ETF시간별추이', 'blocks': {'t1902InBlock': {'type': 'single', 'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'desc': '연속조회키 연속 조회시 이 값을 InBlock의 time 필드에 넣어준다.', 'required': True}]}}},
    't1903': {'tr_cd': 't1903', 'title': 'ETF일별추이', 'blocks': {'t1903InBlock': {'type': 'single', 'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'desc': '연속조회키 연속 조회시 이 값을 InBlock의 date 필드에 넣어준다.', 'required': True}]}}},
    't1904': {'tr_cd': 't1904', 'title': 'ETF구성종목조회', 'blocks': {'t1904InBlock': {'type': 'single', 'fields': [{'key': 'shcode', 'name': 'ETF단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'date', 'name': 'PDF적용일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'sgb', 'name': '정렬기준(1:평가금액2:증권수)', 'type': 'string', 'length': 1, 'required': True}]}}},
    't1906': {'tr_cd': 't1906', 'title': 'ETFLP호가', 'blocks': {'t1906InBlock': {'type': 'single', 'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}]}}},
    'B7_': {'tr_cd': 'B7_', 'title': 'ETF호가잔량', 'fields': [{'key': 'tr_cd', 'name': '거래 CD', 'type': 'string', 'length': 3, 'desc': 'LS증권 거래코드', 'required': True}, {'key': 'tr_key', 'name': '단축코드', 'type': 'string', 'length': 8, 'desc': '단축코드 6자리 또는 8자리 (단건, 연속), (계좌등록/해제 일 경우 필수값 아님)'}]},
    'I5_': {'tr_cd': 'I5_', 'title': '코스피ETF종목실시간NAV', 'fields': [{'key': 'tr_cd', 'name': '거래 CD', 'type': 'string', 'length': 3, 'desc': 'LS증권 거래코드', 'required': True}, {'key': 'tr_key', 'name': '단축코드', 'type': 'string', 'length': 8, 'desc': '단축코드 6자리 또는 8자리 (단건, 연속), (계좌등록/해제 일 경우 필수값 아님)'}]},
}
