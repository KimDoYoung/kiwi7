"""
KIS(한국투자증권) API 요청 정의
API 문서: https://apiportal.koreainvestment.com/apiservice-apiservice
"""
from typing import Dict, Any, List

KIS_REQUEST_DEF = {
    # === 주식 현재가 조회 ===
    'FHKST01010100': {
        'url': '/uapi/domestic-stock/v1/quotations/inquire-price',
        'title': '주식현재가 시세',
        'method': 'GET',
        'tr_id': 'FHKST01010100',
        'body': [
            {'key': 'FID_COND_MRKT_DIV_CODE', 'name': '시장분류코드', 'type': 'string', 'required': True, 'description': 'J:주식'},
            {'key': 'FID_INPUT_ISCD', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6},
        ]
    },

    # === 주식 호가 조회 ===
    'FHKST01010200': {
        'url': '/uapi/domestic-stock/v1/quotations/inquire-asking-price-exp-ccn',
        'title': '주식현재가 호가/예상체결',
        'method': 'GET',
        'tr_id': 'FHKST01010200',
        'body': [
            {'key': 'FID_COND_MRKT_DIV_CODE', 'name': '시장분류코드', 'type': 'string', 'required': True},
            {'key': 'FID_INPUT_ISCD', 'name': '종목코드', 'type': 'string', 'required': True},
        ]
    },

    # === 주식 일/주/월/년 봉 ===
    'FHKST01010400': {
        'url': '/uapi/domestic-stock/v1/quotations/inquire-daily-price',
        'title': '주식현재가 일자별',
        'method': 'GET',
        'tr_id': 'FHKST01010400',
        'body': [
            {'key': 'FID_COND_MRKT_DIV_CODE', 'name': '시장분류코드', 'type': 'string', 'required': True},
            {'key': 'FID_INPUT_ISCD', 'name': '종목코드', 'type': 'string', 'required': True},
            {'key': 'FID_PERIOD_DIV_CODE', 'name': '기간분류코드', 'type': 'string', 'required': True, 'description': 'D:일, W:주, M:월, Y:년'},
            {'key': 'FID_ORG_ADJ_PRC', 'name': '수정주가원주가가격', 'type': 'string', 'required': True, 'description': '0:수정주가, 1:원주가'},
        ]
    },

    # === 주식 체결/거래원 ===
    'FHKST01010300': {
        'url': '/uapi/domestic-stock/v1/quotations/inquire-ccnl',
        'title': '주식현재가 체결',
        'method': 'GET',
        'tr_id': 'FHKST01010300',
        'body': [
            {'key': 'FID_COND_MRKT_DIV_CODE', 'name': '시장분류코드', 'type': 'string', 'required': True},
            {'key': 'FID_INPUT_ISCD', 'name': '종목코드', 'type': 'string', 'required': True},
        ]
    },

    # === 주식 매수 주문 ===
    'TTTC0802U': {
        'url': '/uapi/domestic-stock/v1/trading/order-cash',
        'title': '주식 현금 매수',
        'method': 'POST',
        'tr_id': 'TTTC0802U',  # 모의: VTTC0802U
        'hashkey_required': True,
        'body': [
            {'key': 'CANO', 'name': '계좌번호(8자리)', 'type': 'string', 'required': True},
            {'key': 'ACNT_PRDT_CD', 'name': '계좌상품코드(2자리)', 'type': 'string', 'required': True},
            {'key': 'PDNO', 'name': '종목코드', 'type': 'string', 'required': True},
            {'key': 'ORD_DVSN', 'name': '주문구분', 'type': 'string', 'required': True, 'description': '00:지정가, 01:시장가'},
            {'key': 'ORD_QTY', 'name': '주문수량', 'type': 'string', 'required': True},
            {'key': 'ORD_UNPR', 'name': '주문단가', 'type': 'string', 'required': True, 'description': '시장가는 0'},
        ]
    },

    # === 주식 매도 주문 ===
    'TTTC0801U': {
        'url': '/uapi/domestic-stock/v1/trading/order-cash',
        'title': '주식 현금 매도',
        'method': 'POST',
        'tr_id': 'TTTC0801U',  # 모의: VTTC0801U
        'hashkey_required': True,
        'body': [
            {'key': 'CANO', 'name': '계좌번호', 'type': 'string', 'required': True},
            {'key': 'ACNT_PRDT_CD', 'name': '계좌상품코드', 'type': 'string', 'required': True},
            {'key': 'PDNO', 'name': '종목코드', 'type': 'string', 'required': True},
            {'key': 'ORD_DVSN', 'name': '주문구분', 'type': 'string', 'required': True},
            {'key': 'ORD_QTY', 'name': '주문수량', 'type': 'string', 'required': True},
            {'key': 'ORD_UNPR', 'name': '주문단가', 'type': 'string', 'required': True},
        ]
    },

    # === 주문 정정 ===
    'TTTC0803U': {
        'url': '/uapi/domestic-stock/v1/trading/order-rvsecncl',
        'title': '주식 주문 정정',
        'method': 'POST',
        'tr_id': 'TTTC0803U',  # 모의: VTTC0803U
        'hashkey_required': True,
        'body': [
            {'key': 'CANO', 'name': '계좌번호', 'type': 'string', 'required': True},
            {'key': 'ACNT_PRDT_CD', 'name': '계좌상품코드', 'type': 'string', 'required': True},
            {'key': 'KRX_FWDG_ORD_ORGNO', 'name': '한국거래소전송주문조직번호', 'type': 'string', 'required': True},
            {'key': 'ORGN_ODNO', 'name': '원주문번호', 'type': 'string', 'required': True},
            {'key': 'ORD_DVSN', 'name': '주문구분', 'type': 'string', 'required': True},
            {'key': 'RVSE_CNCL_DVSN_CD', 'name': '정정취소구분코드', 'type': 'string', 'required': True, 'description': '01:정정'},
            {'key': 'ORD_QTY', 'name': '주문수량', 'type': 'string', 'required': True},
            {'key': 'ORD_UNPR', 'name': '주문단가', 'type': 'string', 'required': True},
            {'key': 'QTY_ALL_ORD_YN', 'name': '잔량전부주문여부', 'type': 'string', 'required': True, 'description': 'Y:전량, N:일부'},
        ]
    },

    # === 주문 취소 ===
    'TTTC0804U': {
        'url': '/uapi/domestic-stock/v1/trading/order-rvsecncl',
        'title': '주식 주문 취소',
        'method': 'POST',
        'tr_id': 'TTTC0804U',  # 모의: VTTC0804U
        'hashkey_required': True,
        'body': [
            {'key': 'CANO', 'name': '계좌번호', 'type': 'string', 'required': True},
            {'key': 'ACNT_PRDT_CD', 'name': '계좌상품코드', 'type': 'string', 'required': True},
            {'key': 'KRX_FWDG_ORD_ORGNO', 'name': '한국거래소전송주문조직번호', 'type': 'string', 'required': True},
            {'key': 'ORGN_ODNO', 'name': '원주문번호', 'type': 'string', 'required': True},
            {'key': 'ORD_DVSN', 'name': '주문구분', 'type': 'string', 'required': True},
            {'key': 'RVSE_CNCL_DVSN_CD', 'name': '정정취소구분코드', 'type': 'string', 'required': True, 'description': '02:취소'},
            {'key': 'ORD_QTY', 'name': '주문수량', 'type': 'string', 'required': True},
            {'key': 'ORD_UNPR', 'name': '주문단가', 'type': 'string', 'required': True},
            {'key': 'QTY_ALL_ORD_YN', 'name': '잔량전부주문여부', 'type': 'string', 'required': True},
        ]
    },

    # === 주식 잔고 조회 ===
    'TTTC8434R': {
        'url': '/uapi/domestic-stock/v1/trading/inquire-balance',
        'title': '주식 잔고 조회',
        'method': 'GET',
        'tr_id': 'TTTC8434R',  # 모의: VTTC8434R
        'body': [
            {'key': 'CANO', 'name': '계좌번호', 'type': 'string', 'required': True},
            {'key': 'ACNT_PRDT_CD', 'name': '계좌상품코드', 'type': 'string', 'required': True},
            {'key': 'AFHR_FLPR_YN', 'name': '시간외단일가여부', 'type': 'string', 'required': True, 'description': 'N'},
            {'key': 'OFL_YN', 'name': '오프라인여부', 'type': 'string', 'required': False, 'description': '공백'},
            {'key': 'INQR_DVSN', 'name': '조회구분', 'type': 'string', 'required': True, 'description': '02:종목별'},
            {'key': 'UNPR_DVSN', 'name': '단가구분', 'type': 'string', 'required': True, 'description': '01'},
            {'key': 'FUND_STTL_ICLD_YN', 'name': '펀드결제분포함여부', 'type': 'string', 'required': True, 'description': 'N'},
            {'key': 'FNCG_AMT_AUTO_RDPT_YN', 'name': '융자금액자동상환여부', 'type': 'string', 'required': True, 'description': 'N'},
            {'key': 'PRCS_DVSN', 'name': '처리구분', 'type': 'string', 'required': False, 'description': '00:전일매매포함'},
            {'key': 'CTX_AREA_FK100', 'name': '연속조회검색조건100', 'type': 'string', 'required': False},
            {'key': 'CTX_AREA_NK100', 'name': '연속조회키100', 'type': 'string', 'required': False},
        ]
    },

    # === 매수가능 조회 ===
    'TTTC8908R': {
        'url': '/uapi/domestic-stock/v1/trading/inquire-psbl-order',
        'title': '매수가능조회',
        'method': 'GET',
        'tr_id': 'TTTC8908R',  # 모의: VTTC8908R
        'body': [
            {'key': 'CANO', 'name': '계좌번호', 'type': 'string', 'required': True},
            {'key': 'ACNT_PRDT_CD', 'name': '계좌상품코드', 'type': 'string', 'required': True},
            {'key': 'PDNO', 'name': '종목코드', 'type': 'string', 'required': True},
            {'key': 'ORD_UNPR', 'name': '주문단가', 'type': 'string', 'required': True},
            {'key': 'ORD_DVSN', 'name': '주문구분', 'type': 'string', 'required': True, 'description': '00:지정가'},
            {'key': 'CMA_EVLU_AMT_ICLD_YN', 'name': 'CMA평가금액포함여부', 'type': 'string', 'required': True, 'description': 'N'},
            {'key': 'OVRS_ICLD_YN', 'name': '해외포함여부', 'type': 'string', 'required': True, 'description': 'N'},
        ]
    },

    # === 주문 체결 조회 ===
    'TTTC8001R': {
        'url': '/uapi/domestic-stock/v1/trading/inquire-daily-ccld',
        'title': '주식일별주문체결조회',
        'method': 'GET',
        'tr_id': 'TTTC8001R',  # 모의: VTTC8001R
        'body': [
            {'key': 'CANO', 'name': '계좌번호', 'type': 'string', 'required': True},
            {'key': 'ACNT_PRDT_CD', 'name': '계좌상품코드', 'type': 'string', 'required': True},
            {'key': 'INQR_STRT_DT', 'name': '조회시작일자', 'type': 'string', 'required': True, 'description': 'YYYYMMDD'},
            {'key': 'INQR_END_DT', 'name': '조회종료일자', 'type': 'string', 'required': True, 'description': 'YYYYMMDD'},
            {'key': 'SLL_BUY_DVSN_CD', 'name': '매도매수구분코드', 'type': 'string', 'required': True, 'description': '00:전체, 01:매도, 02:매수'},
            {'key': 'INQR_DVSN', 'name': '조회구분', 'type': 'string', 'required': True, 'description': '00:역순, 01:정순'},
            {'key': 'PDNO', 'name': '종목코드', 'type': 'string', 'required': False},
            {'key': 'CCLD_DVSN', 'name': '체결구분', 'type': 'string', 'required': True, 'description': '00:전체, 01:체결, 02:미체결'},
            {'key': 'ORD_GNO_BRNO', 'name': '주문채번지점번호', 'type': 'string', 'required': False},
            {'key': 'ODNO', 'name': '주문번호', 'type': 'string', 'required': False},
            {'key': 'INQR_DVSN_3', 'name': '조회구분3', 'type': 'string', 'required': True, 'description': '00:전체, 01:현금, 02:융자'},
            {'key': 'INQR_DVSN_1', 'name': '조회구분1', 'type': 'string', 'required': False},
            {'key': 'CTX_AREA_FK100', 'name': '연속조회검색조건100', 'type': 'string', 'required': False},
            {'key': 'CTX_AREA_NK100', 'name': '연속조회키100', 'type': 'string', 'required': False},
        ]
    },

    # === 예수금 조회 ===
    'CTRP6548R': {
        'url': '/uapi/domestic-stock/v1/trading/inquire-psbl-rvsecncl',
        'title': '예수금상세조회',
        'method': 'GET',
        'tr_id': 'CTRP6548R',
        'body': [
            {'key': 'CANO', 'name': '계좌번호', 'type': 'string', 'required': True},
            {'key': 'ACNT_PRDT_CD', 'name': '계좌상품코드', 'type': 'string', 'required': True},
            {'key': 'INQR_DVSN_1', 'name': '조회구분1', 'type': 'string', 'required': False},
            {'key': 'BSPR_BF_DT_APLY_YN', 'name': '기준일이전일적용여부', 'type': 'string', 'required': False},
        ]
    },

    # === 국내주식 업종/테마 ===
    'FHKUP03500100': {
        'url': '/uapi/domestic-stock/v1/quotations/inquire-index-price',
        'title': '업종현재지수',
        'method': 'GET',
        'tr_id': 'FHKUP03500100',
        'body': [
            {'key': 'FID_COND_MRKT_DIV_CODE', 'name': '시장분류코드', 'type': 'string', 'required': True, 'description': 'U:업종'},
            {'key': 'FID_INPUT_ISCD', 'name': '업종코드', 'type': 'string', 'required': True, 'description': '0001:코스피, 1001:코스닥'},
        ]
    },

    # === 종목 조건검색 ===
    'HHKST03900300': {
        'url': '/uapi/domestic-stock/v1/quotations/psearch-result',
        'title': '조건검색결과(등록된 조건)',
        'method': 'GET',
        'tr_id': 'HHKST03900300',
        'body': [
            {'key': 'user_id', 'name': '사용자ID', 'type': 'string', 'required': True},
            {'key': 'seq', 'name': '조건일련번호', 'type': 'string', 'required': True},
        ]
    },
}


def get_request_definition(api_id: str) -> Dict[str, Any]:
    """API ID로 정의 조회"""
    if api_id not in KIS_REQUEST_DEF:
        return None
    return KIS_REQUEST_DEF[api_id]


def get_required_fields(api_id: str) -> List[str]:
    """필수 필드 목록 반환"""
    api_def = KIS_REQUEST_DEF.get(api_id, {})
    body = api_def.get('body', [])
    return [field['key'] for field in body if field.get('required', False)]


def get_tr_id(api_id: str, is_virtual: bool = False) -> str:
    """TR ID 반환 (실전/모의 구분)"""
    api_def = KIS_REQUEST_DEF.get(api_id, {})
    tr_id = api_def.get('tr_id', api_id)

    # 모의투자 TR ID 변환 (T로 시작하면 V로 변경)
    if is_virtual and tr_id and tr_id.startswith('T'):
        return 'V' + tr_id[1:]
    return tr_id


def is_hashkey_required(api_id: str) -> bool:
    """해시키 필요 여부"""
    api_def = KIS_REQUEST_DEF.get(api_id, {})
    return api_def.get('hashkey_required', False)
