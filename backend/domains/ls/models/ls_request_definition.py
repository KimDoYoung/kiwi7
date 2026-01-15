"""
LS증권 API 요청 정의
API 문서: https://openapi.ls-sec.co.kr/apiservice
"""
from typing import Dict, Any, List

LS_REQUEST_DEF = {
    # === 주식 현재가 조회 ===
    't1102': {
        'url': '/stock/market-data',
        'title': '주식현재가(시세)조회',
        'method': 'POST',
        'tr_cd': 't1102',
        'body': [
            {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6},
        ]
    },

    # === 주식 호가 조회 ===
    't1101': {
        'url': '/stock/market-data',
        'title': '주식현재가호가조회',
        'method': 'POST',
        'tr_cd': 't1101',
        'body': [
            {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'required': True},
        ]
    },

    # === 주식 체결 조회 ===
    't1301': {
        'url': '/stock/market-data',
        'title': '주식현재가체결조회',
        'method': 'POST',
        'tr_cd': 't1301',
        'body': [
            {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'required': True},
            {'key': 'cvolume', 'name': '체결수량', 'type': 'string', 'required': False},
            {'key': 'starttime', 'name': '시작시간', 'type': 'string', 'required': False},
            {'key': 'endtime', 'name': '종료시간', 'type': 'string', 'required': False},
            {'key': 'cts_time', 'name': '연속조회시간', 'type': 'string', 'required': False},
        ]
    },

    # === 주식 일자별 시세 ===
    't1305': {
        'url': '/stock/market-data',
        'title': '주식일자별시세조회',
        'method': 'POST',
        'tr_cd': 't1305',
        'body': [
            {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'required': True},
            {'key': 'dwmcode', 'name': '일주월구분', 'type': 'string', 'required': True, 'description': '1:일, 2:주, 3:월'},
            {'key': 'date', 'name': '날짜', 'type': 'string', 'required': False},
            {'key': 'idx', 'name': '인덱스', 'type': 'string', 'required': False},
            {'key': 'cnt', 'name': '건수', 'type': 'string', 'required': True},
        ]
    },

    # === 주식 매수 주문 ===
    'CSPAT00601': {
        'url': '/stock/order',
        'title': '주식현금매수주문',
        'method': 'POST',
        'tr_cd': 'CSPAT00601',
        'body': [
            {'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'required': True, 'description': 'A+6자리'},
            {'key': 'OrdQty', 'name': '주문수량', 'type': 'number', 'required': True},
            {'key': 'OrdPrc', 'name': '주문가격', 'type': 'number', 'required': True},
            {'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'required': True, 'description': '2:매수'},
            {'key': 'OrdprcPtnCode', 'name': '호가유형코드', 'type': 'string', 'required': True, 'description': '00:지정가, 03:시장가'},
            {'key': 'MgntrnCode', 'name': '신용거래코드', 'type': 'string', 'required': True, 'description': '000:보통'},
            {'key': 'LoanDt', 'name': '대출일', 'type': 'string', 'required': False},
            {'key': 'OrdCndiTpCode', 'name': '주문조건구분', 'type': 'string', 'required': True, 'description': '0:없음'},
        ]
    },

    # === 주식 매도 주문 ===
    'CSPAT00701': {
        'url': '/stock/order',
        'title': '주식현금매도주문',
        'method': 'POST',
        'tr_cd': 'CSPAT00701',
        'body': [
            {'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'required': True},
            {'key': 'OrdQty', 'name': '주문수량', 'type': 'number', 'required': True},
            {'key': 'OrdPrc', 'name': '주문가격', 'type': 'number', 'required': True},
            {'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'required': True, 'description': '1:매도'},
            {'key': 'OrdprcPtnCode', 'name': '호가유형코드', 'type': 'string', 'required': True},
            {'key': 'MgntrnCode', 'name': '신용거래코드', 'type': 'string', 'required': True},
            {'key': 'LoanDt', 'name': '대출일', 'type': 'string', 'required': False},
            {'key': 'OrdCndiTpCode', 'name': '주문조건구분', 'type': 'string', 'required': True},
        ]
    },

    # === 주문 정정 ===
    'CSPAT00701': {
        'url': '/stock/order',
        'title': '주식주문정정',
        'method': 'POST',
        'tr_cd': 'CSPAT00701',
        'body': [
            {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'number', 'required': True},
            {'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'required': True},
            {'key': 'OrdQty', 'name': '주문수량', 'type': 'number', 'required': True},
            {'key': 'OrdprcPtnCode', 'name': '호가유형코드', 'type': 'string', 'required': True},
            {'key': 'OrdCndiTpCode', 'name': '주문조건구분', 'type': 'string', 'required': True},
            {'key': 'OrdPrc', 'name': '주문가격', 'type': 'number', 'required': True},
        ]
    },

    # === 주문 취소 ===
    'CSPAT00801': {
        'url': '/stock/order',
        'title': '주식주문취소',
        'method': 'POST',
        'tr_cd': 'CSPAT00801',
        'body': [
            {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'number', 'required': True},
            {'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'required': True},
            {'key': 'OrdQty', 'name': '주문수량', 'type': 'number', 'required': True},
        ]
    },

    # === 계좌 잔고 조회 ===
    't0424': {
        'url': '/stock/accno',
        'title': '주식잔고조회',
        'method': 'POST',
        'tr_cd': 't0424',
        'body': [
            {'key': 'pession', 'name': '단가구분', 'type': 'string', 'required': True, 'description': '0:평균단가, 1:BEP단가'},
            {'key': 'cts_expcode', 'name': '연속조회종목코드', 'type': 'string', 'required': False},
        ]
    },

    # === 주문 체결 조회 ===
    't0425': {
        'url': '/stock/accno',
        'title': '주식주문체결조회',
        'method': 'POST',
        'tr_cd': 't0425',
        'body': [
            {'key': 'expcode', 'name': '종목코드', 'type': 'string', 'required': False},
            {'key': 'chegession', 'name': '체결구분', 'type': 'string', 'required': True, 'description': '0:전체, 1:체결, 2:미체결'},
            {'key': 'medession', 'name': '매매구분', 'type': 'string', 'required': True, 'description': '0:전체, 1:매도, 2:매수'},
            {'key': 'sortgubun', 'name': '정렬기준', 'type': 'string', 'required': True, 'description': '1:주문번호역순, 2:주문번호순'},
            {'key': 'cts_ordno', 'name': '연속조회주문번호', 'type': 'string', 'required': False},
        ]
    },

    # === 예수금 조회 ===
    'CSPAQ12200': {
        'url': '/stock/accno',
        'title': '현물계좌예수금조회',
        'method': 'POST',
        'tr_cd': 'CSPAQ12200',
        'body': [
            {'key': 'BalCreTp', 'name': '잔고생성구분', 'type': 'string', 'required': True, 'description': '0:전체'},
        ]
    },

    # === 업종 지수 ===
    't1511': {
        'url': '/stock/market-data',
        'title': '업종현재가조회',
        'method': 'POST',
        'tr_cd': 't1511',
        'body': [
            {'key': 'upcode', 'name': '업종코드', 'type': 'string', 'required': True, 'description': '001:코스피, 301:코스닥'},
        ]
    },
}


def get_request_definition(api_id: str) -> Dict[str, Any]:
    """API ID로 정의 조회"""
    if api_id not in LS_REQUEST_DEF:
        return None
    return LS_REQUEST_DEF[api_id]


def get_required_fields(api_id: str) -> List[str]:
    """필수 필드 목록 반환"""
    api_def = LS_REQUEST_DEF.get(api_id, {})
    body = api_def.get('body', [])
    return [field['key'] for field in body if field.get('required', False)]


def get_tr_cd(api_id: str) -> str:
    """TR 코드 반환"""
    api_def = LS_REQUEST_DEF.get(api_id, {})
    return api_def.get('tr_cd', api_id)
