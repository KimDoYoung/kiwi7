# Auto-generated
from typing import Any, Dict, List

TRADING_REQUESTS = {
    'CTRGA011R': {
        'method': 'GET',
        'title': '기간별계좌권리현황조회',
        'tr_id': 'CTRGA011R',
        'url': '/uapi/domestic-stock/v1/trading/period-rights',
        'query': [
            {
                'description': '03 입력',
                'key': 'INQR_DVSN',
                'length': 2,
                'name': '조회구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '공란',
                'key': 'CUST_RNCNO25',
                'length': 25,
                'name': '고객실명확인번호25',
                'required': True,
                'type': 'string'
            },
            {
                'description': '공란',
                'key': 'HMID',
                'length': 8,
                'name': '홈넷ID',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 8자리 입력 (ex.12345678)',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '상품계좌번호 2자리 입력(ex. 01 or 22)',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '조회시작일자(YYYYMMDD)',
                'key': 'INQR_STRT_DT',
                'length': 8,
                'name': '조회시작일자',
                'required': True,
                'type': 'string'
            },
            {
                'description': '조회종료일자(YYYYMMDD)',
                'key': 'INQR_END_DT',
                'length': 8,
                'name': '조회종료일자',
                'required': True,
                'type': 'string'
            },
            {
                'description': '공란',
                'key': 'RGHT_TYPE_CD',
                'length': 2,
                'name': '권리유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '공란',
                'key': 'PDNO',
                'length': 12,
                'name': '상품번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '공란',
                'key': 'PRDT_TYPE_CD',
                'length': 3,
                'name': '상품유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '다음조회시 입력',
                'key': 'CTX_AREA_NK100',
                'length': 100,
                'name': '연속조회키100',
                'required': True,
                'type': 'string'
            },
            {
                'description': '다음조회시 입력',
                'key': 'CTX_AREA_FK100',
                'length': 100,
                'name': '연속조회검색조건100',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'CTRP6548R': {
        'method': 'GET',
        'title': '투자계좌자산현황조회',
        'tr_id': 'CTRP6548R',
        'url': '/uapi/domestic-stock/v1/trading/inquire-account-balance',
        'query': [
            {
                'description': '계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '공백입력',
                'key': 'INQR_DVSN_1',
                'length': 1,
                'name': '조회구분1',
                'required': True,
                'type': 'string'
            },
            {
                'description': '공백입력',
                'key': 'BSPR_BF_DT_APLY_YN',
                'length': 1,
                'name': '기준가이전일자적용여부',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'CTSC0004R': {
        'method': 'GET',
        'title': '주식예약주문조회',
        'tr_id': 'CTSC0004R',
        'url': '/uapi/domestic-stock/v1/trading/order-resv-ccnl',
        'query': [
            {
                'key': 'RSVN_ORD_ORD_DT',
                'length': 8,
                'name': '예약주문시작일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'RSVN_ORD_END_DT',
                'length': 8,
                'name': '예약주문종료일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'RSVN_ORD_SEQ',
                'length': 10,
                'name': '예약주문순번',
                'required': True,
                'type': 'string'
            },
            {
                'description': '"00" 입력',
                'key': 'TMNL_MDIA_KIND_CD',
                'length': 2,
                'name': '단말매체종류코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '0: 전체 1: 처리내역 2: 미처리내역',
                'key': 'PRCS_DVSN_CD',
                'length': 2,
                'name': '처리구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '"Y" 유효한 주문만 조회',
                'key': 'CNCL_YN',
                'length': 1,
                'name': '취소여부',
                'required': True,
                'type': 'string'
            },
            {
                'description': '종목코드(6자리) (공백 입력 시 전체 조회)',
                'key': 'PDNO',
                'length': 12,
                'name': '상품번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'SLL_BUY_DVSN_CD',
                'length': 2,
                'name': '매도매수구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '다음 페이지 조회시 사용',
                'key': 'CTX_AREA_FK200',
                'length': 200,
                'name': '연속조회검색조건200',
                'required': True,
                'type': 'string'
            },
            {
                'description': '다음 페이지 조회시 사용',
                'key': 'CTX_AREA_NK200',
                'length': 200,
                'name': '연속조회키200',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'CTSC0008U': {
        'method': 'POST',
        'title': '주식예약주문',
        'tr_id': 'CTSC0008U',
        'url': '/uapi/domestic-stock/v1/trading/order-resv',
        'body': [
            {
                'description': '계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'PDNO',
                'length': 12,
                'name': '종목코드(6자리)',
                'required': True,
                'type': 'string'
            },
            {
                'description': '주문주식수',
                'key': 'ORD_QTY',
                'length': 10,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'description': '1주당 가격  * 장전 시간외, 시장가의 경우 1주당 가격을 공란으로 비우지 않음 "0"으로 입력 권고',
                'key': 'ORD_UNPR',
                'length': 19,
                'name': '주문단가',
                'required': True,
                'type': 'string'
            },
            {
                'description': '01 : 매도 02 : 매수',
                'key': 'SLL_BUY_DVSN_CD',
                'length': 2,
                'name': '매도매수구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00 : 지정가 01 : 시장가 02 : 조건부지정가 05 : 장전 시간외',
                'key': 'ORD_DVSN_CD',
                'length': 2,
                'name': '주문구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[매도매수구분코드 01:매도/02:매수시 사용] 10 : 현금   [매도매수구분코드 01:매도시 사용] 12 : 주식담보대출  14 : 대여상환 21 : 자기융자신규 22 : 유통대주신규 23 : 유통융자신규 24 : 자기대주신규 25 : 자기융자상환 26 : 유통대주상환 27 : 유통융자상환 28 : 자기대주상환',
                'key': 'ORD_OBJT_CBLC_DVSN_CD',
                'length': 2,
                'name': '주문대상잔고구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'LOAN_DT',
                'length': 8,
                'name': '대출일자',
                'required': False,
                'type': 'string'
            },
            {
                'description': '(YYYYMMDD) 현재 일자보다 이후로 설정해야 함 * RSVN_ORD_END_DT(예약주문종료일자)를 안 넣으면 다음날 주문처리되고 예약주문은 종료됨 * RSVN_ORD_END_DT(예약주문종료일자)는 익영업일부터 달력일 기준으로 공휴일 포함하여 최대 30일이 되는 일자까지 입력 가능',
                'key': 'RSVN_ORD_END_DT',
                'length': 8,
                'name': '예약주문종료일자',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'LDNG_DT',
                'length': 8,
                'name': '대여일자',
                'required': False,
                'type': 'string'
            }
        ]
    },
    'CTSC0009U': {
        'method': 'POST',
        'title': '주식예약주문정정취소',
        'tr_id': 'CTSC0009U',
        'url': '/uapi/domestic-stock/v1/trading/order-resv-rvsecncl',
        'body': [
            {
                'description': '[정정/취소] 계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정/취소] 계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정]',
                'key': 'PDNO',
                'length': 12,
                'name': '종목코드(6자리)',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정] 주문주식수',
                'key': 'ORD_QTY',
                'length': 10,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정] 1주당 가격  * 장전 시간외, 시장가의 경우 1주당 가격을 공란으로 비우지 않음 "0"으로 입력 권고',
                'key': 'ORD_UNPR',
                'length': 19,
                'name': '주문단가',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정] 01 : 매도 02 : 매수',
                'key': 'SLL_BUY_DVSN_CD',
                'length': 2,
                'name': '매도매수구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정] 00 : 지정가 01 : 시장가 02 : 조건부지정가 05 : 장전 시간외',
                'key': 'ORD_DVSN_CD',
                'length': 2,
                'name': '주문구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정] 10 : 현금 12 : 주식담보대출 14 : 대여상환 21 : 자기융자신규 22 : 유통대주신규 23 : 유통융자신규 24 : 자기대주신규 25 : 자기융자상환 26 : 유통대주상환 27 : 유통융자상환 28 : 자기대주상환',
                'key': 'ORD_OBJT_CBLC_DVSN_CD',
                'length': 2,
                'name': '주문대상잔고구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정]',
                'key': 'LOAN_DT',
                'length': 8,
                'name': '대출일자',
                'required': False,
                'type': 'string'
            },
            {
                'description': '[정정]',
                'key': 'RSVN_ORD_END_DT',
                'length': 8,
                'name': '예약주문종료일자',
                'required': False,
                'type': 'string'
            },
            {
                'description': '[정정]',
                'key': 'CTAL_TLNO',
                'length': 20,
                'name': '연락전화번호',
                'required': False,
                'type': 'string'
            },
            {
                'description': '[정정/취소]',
                'key': 'RSVN_ORD_SEQ',
                'length': 10,
                'name': '예약주문순번',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정/취소]',
                'key': 'RSVN_ORD_ORGNO',
                'length': 5,
                'name': '예약주문조직번호',
                'required': False,
                'type': 'string'
            },
            {
                'description': '[정정/취소]',
                'key': 'RSVN_ORD_ORD_DT',
                'length': 8,
                'name': '예약주문주문일자',
                'required': False,
                'type': 'string'
            }
        ]
    },
    'CTSC0013U': {
        'method': 'POST',
        'title': '주식예약주문정정취소',
        'tr_id': 'CTSC0013U',
        'url': '/uapi/domestic-stock/v1/trading/order-resv-rvsecncl',
        'body': [
            {
                'description': '[정정/취소] 계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정/취소] 계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정]',
                'key': 'PDNO',
                'length': 12,
                'name': '종목코드(6자리)',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정] 주문주식수',
                'key': 'ORD_QTY',
                'length': 10,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정] 1주당 가격  * 장전 시간외, 시장가의 경우 1주당 가격을 공란으로 비우지 않음 "0"으로 입력 권고',
                'key': 'ORD_UNPR',
                'length': 19,
                'name': '주문단가',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정] 01 : 매도 02 : 매수',
                'key': 'SLL_BUY_DVSN_CD',
                'length': 2,
                'name': '매도매수구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정] 00 : 지정가 01 : 시장가 02 : 조건부지정가 05 : 장전 시간외',
                'key': 'ORD_DVSN_CD',
                'length': 2,
                'name': '주문구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정] 10 : 현금 12 : 주식담보대출 14 : 대여상환 21 : 자기융자신규 22 : 유통대주신규 23 : 유통융자신규 24 : 자기대주신규 25 : 자기융자상환 26 : 유통대주상환 27 : 유통융자상환 28 : 자기대주상환',
                'key': 'ORD_OBJT_CBLC_DVSN_CD',
                'length': 2,
                'name': '주문대상잔고구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정]',
                'key': 'LOAN_DT',
                'length': 8,
                'name': '대출일자',
                'required': False,
                'type': 'string'
            },
            {
                'description': '[정정]',
                'key': 'RSVN_ORD_END_DT',
                'length': 8,
                'name': '예약주문종료일자',
                'required': False,
                'type': 'string'
            },
            {
                'description': '[정정]',
                'key': 'CTAL_TLNO',
                'length': 20,
                'name': '연락전화번호',
                'required': False,
                'type': 'string'
            },
            {
                'description': '[정정/취소]',
                'key': 'RSVN_ORD_SEQ',
                'length': 10,
                'name': '예약주문순번',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[정정/취소]',
                'key': 'RSVN_ORD_ORGNO',
                'length': 5,
                'name': '예약주문조직번호',
                'required': False,
                'type': 'string'
            },
            {
                'description': '[정정/취소]',
                'key': 'RSVN_ORD_ORD_DT',
                'length': 8,
                'name': '예약주문주문일자',
                'required': False,
                'type': 'string'
            }
        ]
    },
    'CTSC9215R': {
        'method': 'GET',
        'title': '주식일별주문체결조회',
        'tr_id': 'CTSC9215R',
        'url': '/uapi/domestic-stock/v1/trading/inquire-daily-ccld',
        'query': [
            {
                'description': '계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'YYYYMMDD',
                'key': 'INQR_STRT_DT',
                'length': 8,
                'name': '조회시작일자',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'YYYYMMDD',
                'key': 'INQR_END_DT',
                'length': 8,
                'name': '조회종료일자',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00 : 전체 / 01 : 매도 / 02 : 매수',
                'key': 'SLL_BUY_DVSN_CD',
                'length': 2,
                'name': '매도매수구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '종목번호(6자리)',
                'key': 'PDNO',
                'length': 12,
                'name': '상품번호',
                'required': False,
                'type': 'string'
            },
            {
                'description': '주문시 한국투자증권 시스템에서 지정된 영업점코드',
                'key': 'ORD_GNO_BRNO',
                'length': 5,
                'name': '주문채번지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '주문시 한국투자증권 시스템에서 채번된 주문번호',
                'key': 'ODNO',
                'length': 10,
                'name': '주문번호',
                'required': False,
                'type': 'string'
            },
            {
                'description': '\'00 전체 01 체결 02 미체결\'',
                'key': 'CCLD_DVSN',
                'length': 2,
                'name': '체결구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'00 역순 01 정순\'',
                'key': 'INQR_DVSN',
                'length': 2,
                'name': '조회구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'없음: 전체 1: ELW 2: 프리보드\'',
                'key': 'INQR_DVSN_1',
                'length': 1,
                'name': '조회구분1',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'00 전체 01 현금 02 신용 03 담보 04 대주 05 대여 06 자기융자신규/상환 07 유통융자신규/상환\'',
                'key': 'INQR_DVSN_3',
                'length': 2,
                'name': '조회구분3',
                'required': True,
                'type': 'string'
            },
            {
                'description': '한국거래소 : KRX 대체거래소 (NXT) : NXT SOR (Smart Order Routing) : SOR ALL : 전체 ※ 모의투자는 KRX만 제공',
                'key': 'EXCG_ID_DVSN_CD',
                'length': 3,
                'name': '거래소ID구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'공란 : 최초 조회시는  이전 조회 Output CTX_AREA_FK100 값 : 다음페이지 조회시(2번째부터)\'',
                'key': 'CTX_AREA_FK100',
                'length': 100,
                'name': '연속조회검색조건100',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'공란 : 최초 조회시  이전 조회 Output CTX_AREA_NK100 값 : 다음페이지 조회시(2번째부터)\'',
                'key': 'CTX_AREA_NK100',
                'length': 100,
                'name': '연속조회키100',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'FHKST17010000': {
        'method': 'GET',
        'title': '국내주식 신용잔고 상위',
        'tr_id': 'FHKST17010000',
        'url': '/uapi/domestic-stock/v1/ranking/credit-balance',
        'query': [
            {
                'description': 'Unique key(11701)',
                'key': 'FID_COND_SCR_DIV_CODE',
                'length': 5,
                'name': '조건 화면 분류 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200,',
                'key': 'FID_INPUT_ISCD',
                'length': 12,
                'name': '입력 종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '2~999',
                'key': 'FID_OPTION',
                'length': 5,
                'name': '증가율기간',
                'required': True,
                'type': 'string'
            },
            {
                'description': '시장구분코드 (주식 J)',
                'key': 'FID_COND_MRKT_DIV_CODE',
                'length': 2,
                'name': '조건 시장 분류 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'(융자)0:잔고비율 상위, 1: 잔고수량 상위, 2: 잔고금액 상위, 3: 잔고비율 증가상위, 4: 잔고비율 감소상위  (대주)5:잔고비율 상위, 6: 잔고수량 상위, 7: 잔고금액 상위, 8: 잔고비율 증가상위, 9: 잔고비율 감소상위 \'',
                'key': 'FID_RANK_SORT_CLS_CODE',
                'length': 2,
                'name': '순위 정렬 구분 코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'FHKST66430100': {
        'method': 'GET',
        'title': '국내주식 대차대조표',
        'tr_id': 'FHKST66430100',
        'url': '/uapi/domestic-stock/v1/finance/balance-sheet',
        'query': [
            {
                'description': '0: 년, 1: 분기',
                'key': 'FID_DIV_CLS_CODE',
                'length': 2,
                'name': '분류 구분 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'J',
                'key': 'fid_cond_mrkt_div_code',
                'length': 2,
                'name': '조건 시장 분류 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '000660 : 종목코드',
                'key': 'fid_input_iscd',
                'length': 12,
                'name': '입력 종목코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'FHPST01720000': {
        'method': 'GET',
        'title': '국내주식 호가잔량 순위',
        'tr_id': 'FHPST01720000',
        'url': '/uapi/domestic-stock/v1/ranking/quote-balance',
        'query': [
            {
                'description': '입력값 없을때 전체 (거래량 ~)',
                'key': 'fid_vol_cnt',
                'length': 12,
                'name': '거래량 수',
                'required': True,
                'type': 'string'
            },
            {
                'description': '시장구분코드 (J:KRX, NX:NXT)',
                'key': 'fid_cond_mrkt_div_code',
                'length': 2,
                'name': '조건 시장 분류 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'Unique key( 20172 )',
                'key': 'fid_cond_scr_div_code',
                'length': 5,
                'name': '조건 화면 분류 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '0000(전체) 코스피(0001), 코스닥(1001), 코스피200(2001)',
                'key': 'fid_input_iscd',
                'length': 12,
                'name': '입력 종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '0: 순매수잔량순, 1:순매도잔량순, 2:매수비율순, 3:매도비율순',
                'key': 'fid_rank_sort_cls_code',
                'length': 2,
                'name': '순위 정렬 구분 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '0:전체',
                'key': 'fid_div_cls_code',
                'length': 2,
                'name': '분류 구분 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '0:전체',
                'key': 'fid_trgt_cls_code',
                'length': 32,
                'name': '대상 구분 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '0:전체',
                'key': 'fid_trgt_exls_cls_code',
                'length': 32,
                'name': '대상 제외 구분 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '입력값 없을때 전체 (가격 ~)',
                'key': 'fid_input_price_1',
                'length': 12,
                'name': '입력 가격1',
                'required': True,
                'type': 'string'
            },
            {
                'description': '입력값 없을때 전체 (~ 가격)',
                'key': 'fid_input_price_2',
                'length': 12,
                'name': '입력 가격2',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'FHPST01760000': {
        'method': 'GET',
        'title': '국내주식 시간외잔량 순위',
        'tr_id': 'FHPST01760000',
        'url': '/uapi/domestic-stock/v1/ranking/after-hour-balance',
        'query': [
            {
                'description': '입력값 없을때 전체 (가격 ~)',
                'key': 'fid_input_price_1',
                'length': 12,
                'name': '입력 가격1',
                'required': True,
                'type': 'string'
            },
            {
                'description': '시장구분코드 (주식 J)',
                'key': 'fid_cond_mrkt_div_code',
                'length': 2,
                'name': '조건 시장 분류 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'Unique key( 20176 )',
                'key': 'fid_cond_scr_div_code',
                'length': 5,
                'name': '조건 화면 분류 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '1: 장전 시간외, 2: 장후 시간외, 3:매도잔량, 4:매수잔량',
                'key': 'fid_rank_sort_cls_code',
                'length': 2,
                'name': '순위 정렬 구분 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '0 : 전체',
                'key': 'fid_div_cls_code',
                'length': 2,
                'name': '분류 구분 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200',
                'key': 'fid_input_iscd',
                'length': 12,
                'name': '입력 종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '0 : 전체',
                'key': 'fid_trgt_exls_cls_code',
                'length': 32,
                'name': '대상 제외 구분 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '0 : 전체',
                'key': 'fid_trgt_cls_code',
                'length': 32,
                'name': '대상 구분 코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '입력값 없을때 전체 (거래량 ~)',
                'key': 'fid_vol_cnt',
                'length': 12,
                'name': '거래량 수',
                'required': True,
                'type': 'string'
            },
            {
                'description': '입력값 없을때 전체 (~ 가격)',
                'key': 'fid_input_price_2',
                'length': 12,
                'name': '입력 가격2',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC0011U': {
        'method': 'POST',
        'title': '주식주문(현금)',
        'tr_id': 'TTTC0011U',
        'url': '/uapi/domestic-stock/v1/trading/order-cash',
        'body': [
            {
                'description': '종합계좌번호',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '상품유형코드',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '종목코드(6자리) , ETN의 경우 7자리 입력',
                'key': 'PDNO',
                'length': 12,
                'name': '상품번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '01@일반매도 02@임의매매 05@대차매도 → 미입력시 01 일반매도로 진행',
                'key': 'SLL_TYPE',
                'length': 2,
                'name': '매도유형 (매도주문 시)',
                'required': False,
                'type': 'string'
            },
            {
                'description': '[KRX] 00 : 지정가 01 : 시장가 02 : 조건부지정가 03 : 최유리지정가 04 : 최우선지정가 05 : 장전 시간외 06 : 장후 시간외 07 : 시간외 단일가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소) 21 : 중간가 22 : 스톱지정가 23 : 중간가IOC 24 : 중간가FOK  [NXT] 00 : 지정가 03 : 최유리지정가 04 : 최우선지정가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소) 21 : 중간가 22 : 스톱지정가 23 : 중간가IOC 24 : 중간가FOK  [SOR] 00 : 지정가 01 : 시장가 03 : 최유리지정가 04 : 최우선지정가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소)',
                'key': 'ORD_DVSN',
                'length': 2,
                'name': '주문구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '주문수량',
                'key': 'ORD_QTY',
                'length': 10,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'description': '주문단가 시장가 등 주문시, "0"으로 입력',
                'key': 'ORD_UNPR',
                'length': 19,
                'name': '주문단가',
                'required': True,
                'type': 'string'
            },
            {
                'description': '스탑지정가호가 주문 (ORD_DVSN이 22) 사용 시에만 필수',
                'key': 'CNDT_PRIC',
                'length': 19,
                'name': '조건가격',
                'required': False,
                'type': 'string'
            },
            {
                'description': '한국거래소 : KRX 대체거래소 (넥스트레이드) : NXT SOR (Smart Order Routing) : SOR → 미입력시 KRX로 진행되며, 모의투자는 KRX만 가능',
                'key': 'EXCG_ID_DVSN_CD',
                'length': 3,
                'name': '거래소ID구분코드',
                'required': False,
                'type': 'string'
            }
        ]
    },
    'TTTC0012U': {
        'method': 'POST',
        'title': '주식주문(현금)',
        'tr_id': 'TTTC0012U',
        'url': '/uapi/domestic-stock/v1/trading/order-cash',
        'body': [
            {
                'description': '종합계좌번호',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '상품유형코드',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '종목코드(6자리) , ETN의 경우 7자리 입력',
                'key': 'PDNO',
                'length': 12,
                'name': '상품번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '01@일반매도 02@임의매매 05@대차매도 → 미입력시 01 일반매도로 진행',
                'key': 'SLL_TYPE',
                'length': 2,
                'name': '매도유형 (매도주문 시)',
                'required': False,
                'type': 'string'
            },
            {
                'description': '[KRX] 00 : 지정가 01 : 시장가 02 : 조건부지정가 03 : 최유리지정가 04 : 최우선지정가 05 : 장전 시간외 06 : 장후 시간외 07 : 시간외 단일가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소) 21 : 중간가 22 : 스톱지정가 23 : 중간가IOC 24 : 중간가FOK  [NXT] 00 : 지정가 03 : 최유리지정가 04 : 최우선지정가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소) 21 : 중간가 22 : 스톱지정가 23 : 중간가IOC 24 : 중간가FOK  [SOR] 00 : 지정가 01 : 시장가 03 : 최유리지정가 04 : 최우선지정가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소)',
                'key': 'ORD_DVSN',
                'length': 2,
                'name': '주문구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '주문수량',
                'key': 'ORD_QTY',
                'length': 10,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'description': '주문단가 시장가 등 주문시, "0"으로 입력',
                'key': 'ORD_UNPR',
                'length': 19,
                'name': '주문단가',
                'required': True,
                'type': 'string'
            },
            {
                'description': '스탑지정가호가 주문 (ORD_DVSN이 22) 사용 시에만 필수',
                'key': 'CNDT_PRIC',
                'length': 19,
                'name': '조건가격',
                'required': False,
                'type': 'string'
            },
            {
                'description': '한국거래소 : KRX 대체거래소 (넥스트레이드) : NXT SOR (Smart Order Routing) : SOR → 미입력시 KRX로 진행되며, 모의투자는 KRX만 가능',
                'key': 'EXCG_ID_DVSN_CD',
                'length': 3,
                'name': '거래소ID구분코드',
                'required': False,
                'type': 'string'
            }
        ]
    },
    'TTTC0013U': {
        'method': 'POST',
        'title': '주식주문(정정취소)',
        'tr_id': 'TTTC0013U',
        'url': '/uapi/domestic-stock/v1/trading/order-rvsecncl',
        'body': [
            {
                'description': '종합계좌번호',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '상품유형코드',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'KRX_FWDG_ORD_ORGNO',
                'length': 5,
                'name': '한국거래소전송주문조직번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '원주문번호',
                'key': 'ORGN_ODNO',
                'length': 10,
                'name': '원주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[KRX] 00 : 지정가 01 : 시장가 02 : 조건부지정가 03 : 최유리지정가 04 : 최우선지정가 05 : 장전 시간외 06 : 장후 시간외 07 : 시간외 단일가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소) 21 : 중간가 22 : 스톱지정가 23 : 중간가IOC 24 : 중간가FOK  [NXT] 00 : 지정가 03 : 최유리지정가 04 : 최우선지정가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소) 21 : 중간가 22 : 스톱지정가 23 : 중간가IOC 24 : 중간가FOK  [SOR] 00 : 지정가 01 : 시장가 03 : 최유리지정가 04 : 최우선지정가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소)',
                'key': 'ORD_DVSN',
                'length': 2,
                'name': '주문구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '01@정정 02@취소',
                'key': 'RVSE_CNCL_DVSN_CD',
                'length': 2,
                'name': '정정취소구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '주문수량',
                'key': 'ORD_QTY',
                'length': 10,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'description': '주문단가',
                'key': 'ORD_UNPR',
                'length': 19,
                'name': '주문단가',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'Y@전량 N@일부\'',
                'key': 'QTY_ALL_ORD_YN',
                'length': 1,
                'name': '잔량전부주문여부',
                'required': True,
                'type': 'string'
            },
            {
                'description': '스탑지정가호가에서 사용',
                'key': 'CNDT_PRIC',
                'length': 19,
                'name': '조건가격',
                'required': False,
                'type': 'string'
            },
            {
                'description': '한국거래소 : KRX 대체거래소 (넥스트레이드) : NXT SOR (Smart Order Routing) : SOR → 미입력시 KRX로 진행되며, 모의투자는 KRX만 가능',
                'key': 'EXCG_ID_DVSN_CD',
                'length': 3,
                'name': '거래소ID구분코드',
                'required': False,
                'type': 'string'
            }
        ]
    },
    'TTTC0051U': {
        'method': 'POST',
        'title': '주식주문(신용)',
        'tr_id': 'TTTC0051U',
        'url': '/uapi/domestic-stock/v1/trading/order-credit',
        'body': [
            {
                'description': '계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '종목코드(6자리)',
                'key': 'PDNO',
                'length': 5,
                'name': '상품번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '공란 입력',
                'key': 'SLL_TYPE',
                'length': 10,
                'name': '매도유형',
                'required': False,
                'type': 'string'
            },
            {
                'description': '[매도] 22 : 유통대주신규, 24 : 자기대주신규, 25 : 자기융자상환, 27 : 유통융자상환 [매수] 21 : 자기융자신규, 23 : 유통융자신규 , 26 : 유통대주상환, 28 : 자기대주상환',
                'key': 'CRDT_TYPE',
                'length': 2,
                'name': '신용유형',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[신용매수]  신규 대출로, 오늘날짜(yyyyMMdd)) 입력   [신용매도]  매도할 종목의 대출일자(yyyyMMdd)) 입력',
                'key': 'LOAN_DT',
                'length': 2,
                'name': '대출일자',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[KRX] 00 : 지정가 01 : 시장가 02 : 조건부지정가 03 : 최유리지정가 04 : 최우선지정가 05 : 장전 시간외 06 : 장후 시간외 07 : 시간외 단일가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소) 21 : 중간가 22 : 스톱지정가 23 : 중간가IOC 24 : 중간가FOK  [NXT] 00 : 지정가 03 : 최유리지정가 04 : 최우선지정가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소) 21 : 중간가 22 : 스톱지정가 23 : 중간가IOC 24 : 중간가FOK  [SOR] 00 : 지정가 01 : 시장가 03 : 최유리지정가 04 : 최우선지정가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소)',
                'key': 'ORD_DVSN',
                'length': 8,
                'name': '주문구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ORD_QTY',
                'length': 2,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'description': '1주당 가격  * 장전 시간외, 장후 시간외, 시장가의 경우 1주당 가격을 공란으로 비우지 않음 "0"으로 입력 권고',
                'key': 'ORD_UNPR',
                'length': 5,
                'name': '주문단가',
                'required': True,
                'type': 'string'
            },
            {
                'description': '정규 증권시장이 열리지 않는 시간 (15:10분 ~ 익일 7:30분) 에 주문을 미리 설정 하여 다음 영업일 또는 설정한 기간 동안 아침 동시 호가에 주문하는 것  Y : 예약주문  N : 신용주문',
                'key': 'RSVN_ORD_YN',
                'length': 2,
                'name': '예약주문여부',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'EMGC_ORD_YN',
                'length': 2,
                'name': '비상주문여부',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'PGTR_DVSN',
                'length': 10,
                'name': '프로그램매매구분',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'MGCO_APTM_ODNO',
                'length': 19,
                'name': '운용사지정주문번호',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'LQTY_TR_NGTN_DTL_NO',
                'length': 1,
                'name': '대량거래협상상세번호',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'LQTY_TR_AGMT_NO',
                'length': 20,
                'name': '대량거래협정번호',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'LQTY_TR_NGTN_ID',
                'length': 19,
                'name': '대량거래협상자Id',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'LP_ORD_YN',
                'length': 3,
                'name': 'LP주문여부',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'MDIA_ODNO',
                'length': 10,
                'name': '매체주문번호',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'ORD_SVR_DVSN_CD',
                'length': 19,
                'name': '주문서버구분코드',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'PGM_NMPR_STMT_DVSN_CD',
                'length': 1,
                'name': '프로그램호가신고구분코드',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'CVRG_SLCT_RSON_CD',
                'length': 20,
                'name': '반대매매선정사유코드',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'CVRG_SEQ',
                'length': 19,
                'name': '반대매매순번',
                'required': False,
                'type': 'string'
            },
            {
                'description': '한국거래소 : KRX 대체거래소 (넥스트레이드) : NXT SOR (Smart Order Routing) : SOR → 미입력시 KRX로 진행되며, 모의투자는 KRX만 가능',
                'key': 'EXCG_ID_DVSN_CD',
                'length': 3,
                'name': '거래소ID구분코드',
                'required': False,
                'type': 'string'
            },
            {
                'description': '스탑지정가호가에서 사용',
                'key': 'CNDT_PRIC',
                'length': 19,
                'name': '조건가격',
                'required': False,
                'type': 'string'
            }
        ]
    },
    'TTTC0052U': {
        'method': 'POST',
        'title': '주식주문(신용)',
        'tr_id': 'TTTC0052U',
        'url': '/uapi/domestic-stock/v1/trading/order-credit',
        'body': [
            {
                'description': '계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '종목코드(6자리)',
                'key': 'PDNO',
                'length': 5,
                'name': '상품번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '공란 입력',
                'key': 'SLL_TYPE',
                'length': 10,
                'name': '매도유형',
                'required': False,
                'type': 'string'
            },
            {
                'description': '[매도] 22 : 유통대주신규, 24 : 자기대주신규, 25 : 자기융자상환, 27 : 유통융자상환 [매수] 21 : 자기융자신규, 23 : 유통융자신규 , 26 : 유통대주상환, 28 : 자기대주상환',
                'key': 'CRDT_TYPE',
                'length': 2,
                'name': '신용유형',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[신용매수]  신규 대출로, 오늘날짜(yyyyMMdd)) 입력   [신용매도]  매도할 종목의 대출일자(yyyyMMdd)) 입력',
                'key': 'LOAN_DT',
                'length': 2,
                'name': '대출일자',
                'required': True,
                'type': 'string'
            },
            {
                'description': '[KRX] 00 : 지정가 01 : 시장가 02 : 조건부지정가 03 : 최유리지정가 04 : 최우선지정가 05 : 장전 시간외 06 : 장후 시간외 07 : 시간외 단일가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소) 21 : 중간가 22 : 스톱지정가 23 : 중간가IOC 24 : 중간가FOK  [NXT] 00 : 지정가 03 : 최유리지정가 04 : 최우선지정가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소) 21 : 중간가 22 : 스톱지정가 23 : 중간가IOC 24 : 중간가FOK  [SOR] 00 : 지정가 01 : 시장가 03 : 최유리지정가 04 : 최우선지정가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소)',
                'key': 'ORD_DVSN',
                'length': 8,
                'name': '주문구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ORD_QTY',
                'length': 2,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'description': '1주당 가격  * 장전 시간외, 장후 시간외, 시장가의 경우 1주당 가격을 공란으로 비우지 않음 "0"으로 입력 권고',
                'key': 'ORD_UNPR',
                'length': 5,
                'name': '주문단가',
                'required': True,
                'type': 'string'
            },
            {
                'description': '정규 증권시장이 열리지 않는 시간 (15:10분 ~ 익일 7:30분) 에 주문을 미리 설정 하여 다음 영업일 또는 설정한 기간 동안 아침 동시 호가에 주문하는 것  Y : 예약주문  N : 신용주문',
                'key': 'RSVN_ORD_YN',
                'length': 2,
                'name': '예약주문여부',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'EMGC_ORD_YN',
                'length': 2,
                'name': '비상주문여부',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'PGTR_DVSN',
                'length': 10,
                'name': '프로그램매매구분',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'MGCO_APTM_ODNO',
                'length': 19,
                'name': '운용사지정주문번호',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'LQTY_TR_NGTN_DTL_NO',
                'length': 1,
                'name': '대량거래협상상세번호',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'LQTY_TR_AGMT_NO',
                'length': 20,
                'name': '대량거래협정번호',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'LQTY_TR_NGTN_ID',
                'length': 19,
                'name': '대량거래협상자Id',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'LP_ORD_YN',
                'length': 3,
                'name': 'LP주문여부',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'MDIA_ODNO',
                'length': 10,
                'name': '매체주문번호',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'ORD_SVR_DVSN_CD',
                'length': 19,
                'name': '주문서버구분코드',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'PGM_NMPR_STMT_DVSN_CD',
                'length': 1,
                'name': '프로그램호가신고구분코드',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'CVRG_SLCT_RSON_CD',
                'length': 20,
                'name': '반대매매선정사유코드',
                'required': False,
                'type': 'string'
            },
            {
                'key': 'CVRG_SEQ',
                'length': 19,
                'name': '반대매매순번',
                'required': False,
                'type': 'string'
            },
            {
                'description': '한국거래소 : KRX 대체거래소 (넥스트레이드) : NXT SOR (Smart Order Routing) : SOR → 미입력시 KRX로 진행되며, 모의투자는 KRX만 가능',
                'key': 'EXCG_ID_DVSN_CD',
                'length': 3,
                'name': '거래소ID구분코드',
                'required': False,
                'type': 'string'
            },
            {
                'description': '스탑지정가호가에서 사용',
                'key': 'CNDT_PRIC',
                'length': 19,
                'name': '조건가격',
                'required': False,
                'type': 'string'
            }
        ]
    },
    'TTTC0081R': {
        'method': 'GET',
        'title': '주식일별주문체결조회',
        'tr_id': 'TTTC0081R',
        'url': '/uapi/domestic-stock/v1/trading/inquire-daily-ccld',
        'query': [
            {
                'description': '계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'YYYYMMDD',
                'key': 'INQR_STRT_DT',
                'length': 8,
                'name': '조회시작일자',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'YYYYMMDD',
                'key': 'INQR_END_DT',
                'length': 8,
                'name': '조회종료일자',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00 : 전체 / 01 : 매도 / 02 : 매수',
                'key': 'SLL_BUY_DVSN_CD',
                'length': 2,
                'name': '매도매수구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '종목번호(6자리)',
                'key': 'PDNO',
                'length': 12,
                'name': '상품번호',
                'required': False,
                'type': 'string'
            },
            {
                'description': '주문시 한국투자증권 시스템에서 지정된 영업점코드',
                'key': 'ORD_GNO_BRNO',
                'length': 5,
                'name': '주문채번지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '주문시 한국투자증권 시스템에서 채번된 주문번호',
                'key': 'ODNO',
                'length': 10,
                'name': '주문번호',
                'required': False,
                'type': 'string'
            },
            {
                'description': '\'00 전체 01 체결 02 미체결\'',
                'key': 'CCLD_DVSN',
                'length': 2,
                'name': '체결구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'00 역순 01 정순\'',
                'key': 'INQR_DVSN',
                'length': 2,
                'name': '조회구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'없음: 전체 1: ELW 2: 프리보드\'',
                'key': 'INQR_DVSN_1',
                'length': 1,
                'name': '조회구분1',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'00 전체 01 현금 02 신용 03 담보 04 대주 05 대여 06 자기융자신규/상환 07 유통융자신규/상환\'',
                'key': 'INQR_DVSN_3',
                'length': 2,
                'name': '조회구분3',
                'required': True,
                'type': 'string'
            },
            {
                'description': '한국거래소 : KRX 대체거래소 (NXT) : NXT SOR (Smart Order Routing) : SOR ALL : 전체 ※ 모의투자는 KRX만 제공',
                'key': 'EXCG_ID_DVSN_CD',
                'length': 3,
                'name': '거래소ID구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'공란 : 최초 조회시는  이전 조회 Output CTX_AREA_FK100 값 : 다음페이지 조회시(2번째부터)\'',
                'key': 'CTX_AREA_FK100',
                'length': 100,
                'name': '연속조회검색조건100',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'공란 : 최초 조회시  이전 조회 Output CTX_AREA_NK100 값 : 다음페이지 조회시(2번째부터)\'',
                'key': 'CTX_AREA_NK100',
                'length': 100,
                'name': '연속조회키100',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC0084R': {
        'method': 'GET',
        'title': '주식정정취소가능주문조회',
        'tr_id': 'TTTC0084R',
        'url': '/uapi/domestic-stock/v1/trading/inquire-psbl-rvsecncl',
        'query': [
            {
                'description': '계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'공란 : 최초 조회시는  이전 조회 Output CTX_AREA_FK100 값 : 다음페이지 조회시(2번째부터)\'',
                'key': 'CTX_AREA_FK100',
                'length': 100,
                'name': '연속조회검색조건100',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'공란 : 최초 조회시  이전 조회 Output CTX_AREA_NK100 값 : 다음페이지 조회시(2번째부터)\'',
                'key': 'CTX_AREA_NK100',
                'length': 100,
                'name': '연속조회키100',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'0 주문 1 종목\'',
                'key': 'INQR_DVSN_1',
                'length': 1,
                'name': '조회구분1',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'0 전체 1 매도 2 매수\'',
                'key': 'INQR_DVSN_2',
                'length': 1,
                'name': '조회구분2',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC0503R': {
        'method': 'GET',
        'title': '퇴직연금 매수가능조회',
        'tr_id': 'TTTC0503R',
        'url': '/uapi/domestic-stock/v1/trading/pension/inquire-psbl-order',
        'query': [
            {
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '29',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'PDNO',
                'length': 12,
                'name': '상품번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00',
                'key': 'ACCA_DVSN_CD',
                'length': 2,
                'name': '적립금구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CMA_EVLU_AMT_ICLD_YN',
                'length': 1,
                'name': 'CMA평가금액포함여부',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00 : 지정가 / 01 : 시장가',
                'key': 'ORD_DVSN',
                'length': 2,
                'name': '주문구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ORD_UNPR',
                'length': 19,
                'name': '주문단가',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC0506R': {
        'method': 'GET',
        'title': '퇴직연금 예수금조회',
        'tr_id': 'TTTC0506R',
        'url': '/uapi/domestic-stock/v1/trading/pension/inquire-deposit',
        'query': [
            {
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '29',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00',
                'key': 'ACCA_DVSN_CD',
                'length': 2,
                'name': '적립금구분코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC0869R': {
        'method': 'GET',
        'title': '주식통합증거금 현황',
        'tr_id': 'TTTC0869R',
        'url': '/uapi/domestic-stock/v1/trading/intgr-margin',
        'query': [
            {
                'description': '계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'N 입력',
                'key': 'CMA_EVLU_AMT_ICLD_YN',
                'length': 1,
                'name': 'CMA평가금액포함여부',
                'required': True,
                'type': 'string'
            },
            {
                'description': '01(외화기준),02(원화기준)',
                'key': 'WCRC_FRCR_DVSN_CD',
                'length': 2,
                'name': '원화외화구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '01(외화기준),02(원화기준)',
                'key': 'FWEX_CTRT_FRCR_DVSN_CD',
                'length': 2,
                'name': '선도환계약외화구분코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC2201R': {
        'method': 'GET',
        'title': '퇴직연금 미체결내역',
        'tr_id': 'TTTC2201R',
        'url': '/uapi/domestic-stock/v1/trading/pension/inquire-daily-ccld',
        'query': [
            {
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '29',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '%%',
                'key': 'USER_DVSN_CD',
                'length': 2,
                'name': '사용자구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00 : 전체 / 01 : 매도 / 02 : 매수',
                'key': 'SLL_BUY_DVSN_CD',
                'length': 2,
                'name': '매도매수구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '%% : 전체 / 01 : 체결 / 02 : 미체결',
                'key': 'CCLD_NCCS_DVSN',
                'length': 2,
                'name': '체결미체결구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00 : 전체',
                'key': 'INQR_DVSN_3',
                'length': 2,
                'name': '조회구분3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CTX_AREA_FK100',
                'length': 100,
                'name': '연속조회검색조건100',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CTX_AREA_NK100',
                'length': 100,
                'name': '연속조회키100',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC2202R': {
        'method': 'GET',
        'title': '퇴직연금 체결기준잔고',
        'tr_id': 'TTTC2202R',
        'url': '/uapi/domestic-stock/v1/trading/pension/inquire-present-balance',
        'query': [
            {
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '29',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00',
                'key': 'USER_DVSN_CD',
                'length': 2,
                'name': '사용자구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CTX_AREA_FK100',
                'length': 100,
                'name': '연속조회검색조건100',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CTX_AREA_NK100',
                'length': 100,
                'name': '연속조회키100',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC2208R': {
        'method': 'GET',
        'title': '퇴직연금 잔고조회',
        'tr_id': 'TTTC2208R',
        'url': '/uapi/domestic-stock/v1/trading/pension/inquire-balance',
        'query': [
            {
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '29',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00',
                'key': 'ACCA_DVSN_CD',
                'length': 2,
                'name': '적립금구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00 : 전체',
                'key': 'INQR_DVSN',
                'length': 2,
                'name': '조회구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CTX_AREA_FK100',
                'length': 100,
                'name': '연속조회검색조건100',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CTX_AREA_NK100',
                'length': 100,
                'name': '연속조회키100',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC2210R': {
        'method': 'GET',
        'title': '퇴직연금 미체결내역',
        'tr_id': 'TTTC2210R',
        'url': '/uapi/domestic-stock/v1/trading/pension/inquire-daily-ccld',
        'query': [
            {
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '29',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '%%',
                'key': 'USER_DVSN_CD',
                'length': 2,
                'name': '사용자구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00 : 전체 / 01 : 매도 / 02 : 매수',
                'key': 'SLL_BUY_DVSN_CD',
                'length': 2,
                'name': '매도매수구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '%% : 전체 / 01 : 체결 / 02 : 미체결',
                'key': 'CCLD_NCCS_DVSN',
                'length': 2,
                'name': '체결미체결구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00 : 전체',
                'key': 'INQR_DVSN_3',
                'length': 2,
                'name': '조회구분3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CTX_AREA_FK100',
                'length': 100,
                'name': '연속조회검색조건100',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CTX_AREA_NK100',
                'length': 100,
                'name': '연속조회키100',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC8408R': {
        'method': 'GET',
        'title': '매도가능수량조회',
        'tr_id': 'TTTC8408R',
        'url': '/uapi/domestic-stock/v1/trading/inquire-psbl-sell',
        'query': [
            {
                'description': '종합계좌번호',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌상품코드',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '보유종목 코드 ex)000660',
                'key': 'PDNO',
                'length': 12,
                'name': '종목번호',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC8434R': {
        'method': 'GET',
        'title': '주식잔고조회',
        'tr_id': 'TTTC8434R',
        'url': '/uapi/domestic-stock/v1/trading/inquire-balance',
        'query': [
            {
                'description': '계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'N : 기본값, Y : 시간외단일가, X : NXT 정규장 (프리마켓, 메인, 애프터마켓) ※ NXT 선택 시 : NXT 거래종목만 시세 등 정보가 NXT 기준으로 변동됩니다. KRX 종목들은 그대로 유지',
                'key': 'AFHR_FLPR_YN',
                'length': 1,
                'name': '시간외단일가, 거래소여부',
                'required': True,
                'type': 'string'
            },
            {
                'description': '공란(Default)',
                'key': 'OFL_YN',
                'length': 1,
                'name': '오프라인여부',
                'required': False,
                'type': 'string'
            },
            {
                'description': '01 : 대출일별 02 : 종목별',
                'key': 'INQR_DVSN',
                'length': 2,
                'name': '조회구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '01 : 기본값',
                'key': 'UNPR_DVSN',
                'length': 2,
                'name': '단가구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'N : 포함하지 않음 Y :  포함',
                'key': 'FUND_STTL_ICLD_YN',
                'length': 1,
                'name': '펀드결제분포함여부',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'N : 기본값',
                'key': 'FNCG_AMT_AUTO_RDPT_YN',
                'length': 1,
                'name': '융자금액자동상환여부',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00 :  전일매매포함 01 : 전일매매미포함',
                'key': 'PRCS_DVSN',
                'length': 2,
                'name': '처리구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '공란 : 최초 조회시 이전 조회 Output CTX_AREA_FK100 값 : 다음페이지 조회시(2번째부터)',
                'key': 'CTX_AREA_FK100',
                'length': 100,
                'name': '연속조회검색조건100',
                'required': False,
                'type': 'string'
            },
            {
                'description': '공란 : 최초 조회시 이전 조회 Output CTX_AREA_NK100 값 : 다음페이지 조회시(2번째부터)',
                'key': 'CTX_AREA_NK100',
                'length': 100,
                'name': '연속조회키100',
                'required': False,
                'type': 'string'
            }
        ]
    },
    'TTTC8494R': {
        'method': 'GET',
        'title': '주식잔고조회_실현손익',
        'tr_id': 'TTTC8494R',
        'url': '/uapi/domestic-stock/v1/trading/inquire-balance-rlz-pl',
        'query': [
            {
                'description': '계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '\'N : 기본값  Y : 시간외단일가\'',
                'key': 'AFHR_FLPR_YN',
                'length': 1,
                'name': '시간외단일가여부',
                'required': True,
                'type': 'string'
            },
            {
                'description': '공란',
                'key': 'OFL_YN',
                'length': 1,
                'name': '오프라인여부',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00 : 전체',
                'key': 'INQR_DVSN',
                'length': 2,
                'name': '조회구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '01 : 기본값',
                'key': 'UNPR_DVSN',
                'length': 2,
                'name': '단가구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'N : 포함하지 않음  Y : 포함',
                'key': 'FUND_STTL_ICLD_YN',
                'length': 1,
                'name': '펀드결제포함여부',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'N : 기본값',
                'key': 'FNCG_AMT_AUTO_RDPT_YN',
                'length': 1,
                'name': '융자금액자동상환여부',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00 : 전일매매포함  01 : 전일매매미포함',
                'key': 'PRCS_DVSN',
                'length': 2,
                'name': 'PRCS_DVSN',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'COST_ICLD_YN',
                'length': 1,
                'name': '비용포함여부',
                'required': True,
                'type': 'string'
            },
            {
                'description': '공란 : 최초 조회시  이전 조회 Output CTX_AREA_FK100 값 : 다음페이지 조회시(2번째부터)',
                'key': 'CTX_AREA_FK100',
                'length': 100,
                'name': '연속조회검색조건100',
                'required': True,
                'type': 'string'
            },
            {
                'description': '공란 : 최초 조회시  이전 조회 Output CTX_AREA_NK100 값 : 다음페이지 조회시(2번째부터)',
                'key': 'CTX_AREA_NK100',
                'length': 100,
                'name': '연속조회키100',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC8708R': {
        'method': 'GET',
        'title': '기간별손익일별합산조회',
        'tr_id': 'TTTC8708R',
        'url': '/uapi/domestic-stock/v1/trading/inquire-period-profit',
        'query': [
            {
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'INQR_STRT_DT',
                'length': 8,
                'name': '조회시작일자',
                'required': True,
                'type': 'string'
            },
            {
                'description': '""공란입력 시, 전체',
                'key': 'PDNO',
                'length': 12,
                'name': '상품번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CTX_AREA_NK100',
                'length': 100,
                'name': '연속조회키100',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'INQR_END_DT',
                'length': 8,
                'name': '조회종료일자',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00: 최근 순, 01: 과거 순, 02: 최근 순',
                'key': 'SORT_DVSN',
                'length': 2,
                'name': '정렬구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00 입력',
                'key': 'INQR_DVSN',
                'length': 2,
                'name': '조회구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00: 전체',
                'key': 'CBLC_DVSN',
                'length': 2,
                'name': '잔고구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CTX_AREA_FK100',
                'length': 100,
                'name': '연속조회검색조건100',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC8715R': {
        'method': 'GET',
        'title': '기간별매매손익현황조회',
        'tr_id': 'TTTC8715R',
        'url': '/uapi/domestic-stock/v1/trading/inquire-period-trade-profit',
        'query': [
            {
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00: 최근 순, 01: 과거 순, 02: 최근 순',
                'key': 'SORT_DVSN',
                'length': 2,
                'name': '정렬구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '""공란입력 시, 전체',
                'key': 'PDNO',
                'length': 12,
                'name': '상품번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'INQR_STRT_DT',
                'length': 8,
                'name': '조회시작일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'INQR_END_DT',
                'length': 8,
                'name': '조회종료일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CTX_AREA_NK100',
                'length': 100,
                'name': '연속조회키100',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00: 전체',
                'key': 'CBLC_DVSN',
                'length': 2,
                'name': '잔고구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CTX_AREA_FK100',
                'length': 100,
                'name': '연속조회검색조건100',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC8908R': {
        'method': 'GET',
        'title': '매수가능조회',
        'tr_id': 'TTTC8908R',
        'url': '/uapi/domestic-stock/v1/trading/inquire-psbl-order',
        'query': [
            {
                'description': '계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '종목번호(6자리) * PDNO, ORD_UNPR 공란 입력 시, 매수수량 없이 매수금액만 조회됨',
                'key': 'PDNO',
                'length': 12,
                'name': '상품번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '1주당 가격 * 시장가(ORD_DVSN:01)로 조회 시, 공란으로 입력 * PDNO, ORD_UNPR 공란 입력 시, 매수수량 없이 매수금액만 조회됨',
                'key': 'ORD_UNPR',
                'length': 19,
                'name': '주문단가',
                'required': True,
                'type': 'string'
            },
            {
                'description': '* 특정 종목 전량매수 시 가능수량을 확인할 경우     00:지정가는 증거금율이 반영되지 않으므로     증거금율이 반영되는 01: 시장가로 조회 * 다만, 조건부지정가 등 특정 주문구분(ex.IOC)으로 주문 시 가능수량을 확인할 경우 주문 시와 동일한 주문구분(ex.IOC) 입력하여 가능수량 확인 * 종목별 매수가능수량 조회 없이 매수금액만 조회하고자 할 경우 임의값(00) 입력 00 : 지정가 01 : 시장가 02 : 조건부지정가 03 : 최유리지정가 04 : 최우선지정가 05 : 장전 시간외 06 : 장후 시간외 07 : 시간외 단일가 08 : 자기주식 09 : 자기주식S-Option 10 : 자기주식금전신탁 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소) 51 : 장중대량 52 : 장중바스켓 62 : 장개시전 시간외대량 63 : 장개시전 시간외바스켓 67 : 장개시전 금전신탁자사주 69 : 장개시전 자기주식 72 : 시간외대량 77 : 시간외자사주신탁 79 : 시간외대량자기주식 80 : 바스켓',
                'key': 'ORD_DVSN',
                'length': 2,
                'name': '주문구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'Y : 포함 N : 포함하지 않음',
                'key': 'CMA_EVLU_AMT_ICLD_YN',
                'length': 1,
                'name': 'CMA평가금액포함여부',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'Y : 포함 N : 포함하지 않음',
                'key': 'OVRS_ICLD_YN',
                'length': 1,
                'name': '해외포함여부',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TTTC8909R': {
        'method': 'GET',
        'title': '신용매수가능조회',
        'tr_id': 'TTTC8909R',
        'url': '/uapi/domestic-stock/v1/trading/inquire-credit-psamount',
        'query': [
            {
                'description': '계좌번호 체계(8-2)의 앞 8자리',
                'key': 'CANO',
                'length': 8,
                'name': '종합계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '계좌번호 체계(8-2)의 뒤 2자리',
                'key': 'ACNT_PRDT_CD',
                'length': 2,
                'name': '계좌상품코드',
                'required': True,
                'type': 'string'
            },
            {
                'description': '종목코드(6자리)',
                'key': 'PDNO',
                'length': 12,
                'name': '상품번호',
                'required': True,
                'type': 'string'
            },
            {
                'description': '1주당 가격  * 장전 시간외, 장후 시간외, 시장가의 경우 1주당 가격을 공란으로 비우지 않음 "0"으로 입력 권고',
                'key': 'ORD_UNPR',
                'length': 19,
                'name': '주문단가',
                'required': True,
                'type': 'string'
            },
            {
                'description': '00 : 지정가  01 : 시장가  02 : 조건부지정가  03 : 최유리지정가  04 : 최우선지정가  05 : 장전 시간외  06 : 장후 시간외  07 : 시간외 단일가  등',
                'key': 'ORD_DVSN',
                'length': 2,
                'name': '주문구분',
                'required': True,
                'type': 'string'
            },
            {
                'description': '21 : 자기융자신규  23 : 유통융자신규  26 : 유통대주상환  28 : 자기대주상환  25 : 자기융자상환  27 : 유통융자상환  22 : 유통대주신규  24 : 자기대주신규',
                'key': 'CRDT_TYPE',
                'length': 2,
                'name': '신용유형',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'Y/N',
                'key': 'CMA_EVLU_AMT_ICLD_YN',
                'length': 1,
                'name': 'CMA평가금액포함여부',
                'required': True,
                'type': 'string'
            },
            {
                'description': 'Y/N',
                'key': 'OVRS_ICLD_YN',
                'length': 1,
                'name': '해외포함여부',
                'required': True,
                'type': 'string'
            }
        ]
    }
}
