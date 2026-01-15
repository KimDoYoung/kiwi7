"""
LS증권 API 응답 정의
각 API별 응답 필드 매핑을 정의합니다.
"""

LS_RESPONSE_DEF = {
    # === 주식현재가(시세)조회 ===
    't1102': [
        {'key': 'hname', 'name': '종목명'},
        {'key': 'price', 'name': '현재가'},
        {'key': 'sign', 'name': '전일대비구분'},
        {'key': 'change', 'name': '전일대비'},
        {'key': 'diff', 'name': '등락율'},
        {'key': 'volume', 'name': '누적거래량'},
        {'key': 'value', 'name': '누적거래대금'},
        {'key': 'open', 'name': '시가'},
        {'key': 'high', 'name': '고가'},
        {'key': 'low', 'name': '저가'},
        {'key': 'uplmtprice', 'name': '상한가'},
        {'key': 'dnlmtprice', 'name': '하한가'},
        {'key': 'jnilvolume', 'name': '전일거래량'},
        {'key': 'per', 'name': 'PER'},
        {'key': 'eps', 'name': 'EPS'},
        {'key': 'capital', 'name': '자본금'},
        {'key': 'cvolume', 'name': '체결수량'},
        {'key': 'offerho1', 'name': '매도호가1'},
        {'key': 'bidho1', 'name': '매수호가1'},
        {'key': 'offerrem1', 'name': '매도잔량1'},
        {'key': 'bidrem1', 'name': '매수잔량1'},
        {'key': 'listing', 'name': '상장주식수'},
        {'key': 'totpq', 'name': '총매도잔량'},
        {'key': 'totbq', 'name': '총매수잔량'},
        {'key': 'market', 'name': '시장구분'},
    ],

    # === 주식현재가호가조회 ===
    't1101': [
        {'key': 'hname', 'name': '종목명'},
        {'key': 'price', 'name': '현재가'},
        {'key': 'offerho1', 'name': '매도호가1'},
        {'key': 'offerho2', 'name': '매도호가2'},
        {'key': 'offerho3', 'name': '매도호가3'},
        {'key': 'offerho4', 'name': '매도호가4'},
        {'key': 'offerho5', 'name': '매도호가5'},
        {'key': 'offerho6', 'name': '매도호가6'},
        {'key': 'offerho7', 'name': '매도호가7'},
        {'key': 'offerho8', 'name': '매도호가8'},
        {'key': 'offerho9', 'name': '매도호가9'},
        {'key': 'offerho10', 'name': '매도호가10'},
        {'key': 'bidho1', 'name': '매수호가1'},
        {'key': 'bidho2', 'name': '매수호가2'},
        {'key': 'bidho3', 'name': '매수호가3'},
        {'key': 'bidho4', 'name': '매수호가4'},
        {'key': 'bidho5', 'name': '매수호가5'},
        {'key': 'bidho6', 'name': '매수호가6'},
        {'key': 'bidho7', 'name': '매수호가7'},
        {'key': 'bidho8', 'name': '매수호가8'},
        {'key': 'bidho9', 'name': '매수호가9'},
        {'key': 'bidho10', 'name': '매수호가10'},
        {'key': 'offerrem1', 'name': '매도잔량1'},
        {'key': 'offerrem2', 'name': '매도잔량2'},
        {'key': 'offerrem3', 'name': '매도잔량3'},
        {'key': 'offerrem4', 'name': '매도잔량4'},
        {'key': 'offerrem5', 'name': '매도잔량5'},
        {'key': 'bidrem1', 'name': '매수잔량1'},
        {'key': 'bidrem2', 'name': '매수잔량2'},
        {'key': 'bidrem3', 'name': '매수잔량3'},
        {'key': 'bidrem4', 'name': '매수잔량4'},
        {'key': 'bidrem5', 'name': '매수잔량5'},
        {'key': 'totofferrem', 'name': '총매도잔량'},
        {'key': 'totbidrem', 'name': '총매수잔량'},
    ],

    # === 주식잔고조회 ===
    't0424': [
        {'key': 'expcode', 'name': '종목코드'},
        {'key': 'hname', 'name': '종목명'},
        {'key': 'janqty', 'name': '잔고수량'},
        {'key': 'mdposqt', 'name': '매도가능수량'},
        {'key': 'pamt', 'name': '평균단가'},
        {'key': 'mamt', 'name': '매입금액'},
        {'key': 'price', 'name': '현재가'},
        {'key': 'appamt', 'name': '평가금액'},
        {'key': 'dtsunik', 'name': '평가손익'},
        {'key': 'sunikrt', 'name': '수익율'},
        {'key': 'jangb', 'name': '잔고구분'},
        {'key': 'syession', 'name': '신용구분'},
    ],

    # === 주문 응답 ===
    'CSPAT00601': [
        {'key': 'OrdNo', 'name': '주문번호'},
        {'key': 'OrdTime', 'name': '주문시각'},
        {'key': 'OrdMktCode', 'name': '주문시장코드'},
        {'key': 'OrdPtnCode', 'name': '주문유형코드'},
        {'key': 'ShtnIsuNo', 'name': '단축종목번호'},
        {'key': 'MgempNo', 'name': '관리사원번호'},
        {'key': 'OrdAmt', 'name': '주문금액'},
        {'key': 'SpareOrdNo', 'name': '예비주문번호'},
        {'key': 'CvrgSeqno', 'name': '반대매매일련번호'},
        {'key': 'RsvOrdNo', 'name': '예약주문번호'},
    ],

    # === 주문체결조회 ===
    't0425': [
        {'key': 'ordno', 'name': '주문번호'},
        {'key': 'expcode', 'name': '종목코드'},
        {'key': 'hname', 'name': '종목명'},
        {'key': 'ordqty', 'name': '주문수량'},
        {'key': 'price', 'name': '주문가격'},
        {'key': 'cheqty', 'name': '체결수량'},
        {'key': 'cheprice', 'name': '체결가격'},
        {'key': 'ordrem', 'name': '미체결잔량'},
        {'key': 'ordtime', 'name': '주문시간'},
        {'key': 'ordgb', 'name': '주문구분'},
        {'key': 'medession', 'name': '매매구분'},
        {'key': 'hogagb', 'name': '호가구분'},
        {'key': 'cheytime', 'name': '체결시간'},
    ],

    # === 예수금 조회 ===
    'CSPAQ12200': [
        {'key': 'MnyOrdAbleAmt', 'name': '현금주문가능금액'},
        {'key': 'MnyoutAbleAmt', 'name': '현금출금가능금액'},
        {'key': 'SeijunAmt', 'name': '청산가능금액'},
        {'key': 'BalEvalAmt', 'name': '잔고평가금액'},
        {'key': 'DpsastAmt', 'name': '예탁자산금액'},
        {'key': 'InvstOrgAmt', 'name': '투자원금'},
        {'key': 'InvstPlAmt', 'name': '투자손익금액'},
        {'key': 'CrdtPldgOrdAmt', 'name': '신용담보주문금액'},
        {'key': 'Dps', 'name': '예수금'},
        {'key': 'SubstAmt', 'name': '대용금액'},
    ],
}


def get_response_fields(api_id: str) -> list:
    """API ID로 응답 필드 정의 조회"""
    return LS_RESPONSE_DEF.get(api_id, [])


def get_field_name(api_id: str, key: str) -> str:
    """필드 키의 한글 이름 반환"""
    fields = LS_RESPONSE_DEF.get(api_id, [])
    for field in fields:
        if field['key'] == key:
            return field['name']
    return key
