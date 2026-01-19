# Auto-generated
from typing import Any, Dict, List

MARKET_OVERSEAS_STOCKS_REQUESTS = {
    'COSAQ00102': {
        'tr_cd': 'COSAQ00102',
        'title': '해외주식 계좌주문체결내역조회 API',
        'fields': [
            {
                'key': 'COSAQ00102InBlock1',
                'length': None,
                'name': 'COSAQ00102InBlock1',
                'required': True,
                'type': 'long'
            },
            {
                'desc': '00001',
                'key': 'RecCnt',
                'length': 5,
                'name': '레코드갯수',
                'required': True,
                'type': 'long'
            },
            {
                'desc': '1@계좌별',
                'key': 'QryTpCode',
                'length': 1,
                'name': '조회구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '1@역순<br/>2@정순',
                'key': 'BkseqTpCode',
                'length': 1,
                'name': '역순구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '81@뉴욕거래소<br/>82@NASDAQ',
                'key': 'OrdMktCode',
                'length': 2,
                'name': '주문시장코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '0@전체<br/>1@매도<br/>2@매수',
                'key': 'BnsTpCode',
                'length': 1,
                'name': '매매구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'IsuNo',
                'length': 12,
                'name': '종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '역순인경우 999999999<br/>정순인 경우 0',
                'key': 'SrtOrdNo',
                'length': 10,
                'name': '시작주문번호',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'OrdDt',
                'length': 8,
                'name': '주문일자',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '0@전체<br/>1@체결<br/>2@미체결',
                'key': 'ExecYn',
                'length': 1,
                'name': '체결여부',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '000@전체<br/>USD@미국',
                'key': 'CrcyCode',
                'length': 3,
                'name': '통화코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '0@미적용<br/>1@적용',
                'key': 'ThdayBnsAppYn',
                'length': 1,
                'name': '당일매매적용여부',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '0@ 전체<br/>1@ 대출잔고만',
                'key': 'LoanBalHldYn',
                'length': 1,
                'name': '대출잔고보유여부',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'COSAQ01400': {
        'tr_cd': 'COSAQ01400',
        'title': '예약주문 처리결과 조회',
        'blocks': {
            'COSAQ01400InBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'QryTpCode', 'name': '조회구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'CntryCode', 'name': '국가코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'SrtDt', 'name': '시작일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'EndDt', 'name': '종료일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'RsvOrdCndiCode', 'name': '예약주문조건코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'RsvOrdStatCode', 'name': '예약주문상태코드', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    'COSAT00301': {
        'tr_cd': 'COSAT00301',
        'title': '미국시장주문 API',
        'blocks': {
            'COSAT00301InBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'desc': '00001', 'required': True}, {'key': 'OrdPtnCode', 'name': '주문유형코드', 'type': 'string', 'length': 2, 'desc': '01 : 매도주문<br/>02 : 매수주문<br/>08 : 취소주문', 'required': True}, {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'float', 'length': 10, 'desc': '취소주문인 경우만 필수 입력', 'required': True}, {'key': 'OrdMktCode', 'name': '주문시장코드', 'type': 'string', 'length': 2, 'desc': '81 : 뉴욕거래소<br/>82 : NASDAQ', 'required': True}, {'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'length': 12, 'desc': '단축종목코드<br/>ex.TSLA', 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OvrsOrdPrc', 'name': '해외주문가', 'type': 'float', 'length': 28.7, 'required': True}, {'key': 'OrdprcPtnCode', 'name': '호가유형코드', 'type': 'string', 'length': 2, 'desc': '00@지정가<br/>M1@LOO<br/>M2@LOC<br/><br/>매도인경우 호가유형 확대<br/>03@시장가<br/>M3@MOO<br/>M4@MOC', 'required': True}, {'key': 'BrkTpCode', 'name': '중개인구분코드', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            }
        }
    },
    'COSAT00311': {
        'tr_cd': 'COSAT00311',
        'title': '미국시장정정주문 API',
        'blocks': {
            'COSAT00311InBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'desc': '00001', 'required': True}, {'key': 'OrdPtnCode', 'name': '주문유형코드', 'type': 'string', 'length': 2, 'desc': '07@정정주문', 'required': True}, {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'OrdMktCode', 'name': '주문시장코드', 'type': 'string', 'length': 2, 'desc': '81@뉴욕거래소<br/>82@NASDAQ', 'required': True}, {'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'desc': '0 입력', 'required': True}, {'key': 'OvrsOrdPrc', 'name': '해외주문가', 'type': 'float', 'length': 28.7, 'required': True}, {'key': 'OrdprcPtnCode', 'name': '호가유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'BrkTpCode', 'name': '중개인구분코드', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            }
        }
    },
    'COSAT00400': {
        'tr_cd': 'COSAT00400',
        'title': '해외주식 예약주문 등록 및 취소',
        'fields': [
            {
                'key': 'COSAT00400InBlock1',
                'length': None,
                'name': 'COSAT00400InBlock1',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'RecCnt',
                'length': 5,
                'name': '레코드갯수',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'TrxTpCode',
                'length': 1,
                'name': '처리구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CntryCode',
                'length': 3,
                'name': '국가코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'RsvOrdInptDt',
                'length': 8,
                'name': '예약주문입력일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'RsvOrdNo',
                'length': 10,
                'name': '예약주문번호',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'BnsTpCode',
                'length': 1,
                'name': '매매구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'AcntNo',
                'length': 20,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'Pwd',
                'length': 8,
                'name': '비밀번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'FcurrMktCode',
                'length': 2,
                'name': '외화시장코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'IsuNo',
                'length': 12,
                'name': '종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'OrdQty',
                'length': 16,
                'name': '주문수량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'OvrsOrdPrc',
                'length': 28.7,
                'name': '해외주문가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'OrdprcPtnCode',
                'length': 2,
                'name': '호가유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'RsvOrdSrtDt',
                'length': 8,
                'name': '예약주문시작일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'RsvOrdEndDt',
                'length': 8,
                'name': '예약주문종료일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'RsvOrdCndiCode',
                'length': 2,
                'name': '예약주문조건코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'MgntrnCode',
                'length': 3,
                'name': '신용거래코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'LoanDt',
                'length': 8,
                'name': '대출일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'LoanDtlClssCode',
                'length': 2,
                'name': '대출상세분류코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'g3101': {
        'tr_cd': 'g3101',
        'title': '해외주식 API 현재가 조회',
        'fields': [
            {
                'key': 'g3101InBlock',
                'length': None,
                'name': 'g3101InBlock',
                'required': True,
                'type': 'long'
            },
            {
                'desc': 'R',
                'key': 'delaygb',
                'length': 1,
                'name': '지연구분',
                'required': True,
                'type': 'string'
            },
            {
                'desc': 'ex)82TSLA',
                'key': 'keysymbol',
                'length': 18,
                'name': 'KEY종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '81 : 뉴욕/아멕스, 82 : 나스닥',
                'key': 'exchcd',
                'length': 2,
                'name': '거래소코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': 'ex)TSLA',
                'key': 'symbol',
                'length': 16,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'g3102': {
        'tr_cd': 'g3102',
        'title': '해외주식 API 시간대별',
        'blocks': {
            'g3102InBlock': {
                'fields': [{'key': 'delaygb', 'name': '지연구분', 'type': 'string', 'length': 1, 'desc': 'R', 'required': True}, {'key': 'keysymbol', 'name': 'KEY종목코드', 'type': 'string', 'length': 18, 'desc': 'ex) 82TSLA', 'required': True}, {'key': 'exchcd', 'name': '거래소코드', 'type': 'string', 'length': 2, 'desc': '81 : 뉴욕/아멕스, 82 : 나스닥', 'required': True}, {'key': 'readcnt', 'name': '조회갯수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'cts_seq', 'name': '연속시퀀스', 'type': 'float', 'length': 17, 'required': True}],
                'type': 'single'
            }
        }
    },
    'g3103': {
        'tr_cd': 'g3103',
        'title': '해외주식 API 일주월 조회',
        'fields': [
            {
                'key': 'g3103InBlock',
                'length': None,
                'name': 'g3103InBlock',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'delaygb',
                'length': 1,
                'name': '지연구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'keysymbol',
                'length': 18,
                'name': 'KEY종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchcd',
                'length': 2,
                'name': '거래소코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'symbol',
                'length': 16,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'gubun',
                'length': 1,
                'name': '주기구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'date',
                'length': 8,
                'name': '조회일자',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'g3104': {
        'tr_cd': 'g3104',
        'title': '해외주식 API 종목정보 조회',
        'blocks': {
            'g3104InBlock': {
                'fields': [{'key': 'delaygb', 'name': '지연구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'keysymbol', 'name': 'KEY종목코드', 'type': 'string', 'length': 18, 'required': True}, {'key': 'exchcd', 'name': '거래소코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'symbol', 'name': '종목코드', 'type': 'string', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'g3106': {
        'tr_cd': 'g3106',
        'title': '해외주식 API 현재가호가 조회',
        'blocks': {
            'g3106InBlock': {
                'fields': [{'key': 'delaygb', 'name': '지연구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'keysymbol', 'name': 'KEY종목코드', 'type': 'string', 'length': 18, 'required': True}, {'key': 'exchcd', 'name': '거래소코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'symbol', 'name': '종목코드', 'type': 'string', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'g3190': {
        'tr_cd': 'g3190',
        'title': '해외주식 API 마스터 조회',
        'blocks': {
            'g3190InBlock': {
                'fields': [{'key': 'delaygb', 'name': '지연구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'natcode', 'name': '국가구분', 'type': 'string', 'length': 2, 'required': True}, {'key': 'exgubun', 'name': '거래소구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'readcnt', 'name': '조회갯수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'cts_value', 'name': '연속구분', 'type': 'string', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'g3202': {
        'tr_cd': 'g3202',
        'title': '해외주식 API 차트NTICK 조회',
        'fields': [
            {
                'key': 'g3202InBlock',
                'length': None,
                'name': 'g3202InBlock',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'delaygb',
                'length': 1,
                'name': '지연구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'keysymbol',
                'length': 18,
                'name': 'KEY종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchcd',
                'length': 2,
                'name': '거래소코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'symbol',
                'length': 16,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ncnt',
                'length': 4,
                'name': '단위(n틱)',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'qrycnt',
                'length': 4,
                'name': '요청건수(최대-압축:2000비압축:5',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'comp_yn',
                'length': 1,
                'name': '압축여부(Y:압축N:비압축)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sdate',
                'length': 8,
                'name': '시작일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'edate',
                'length': 8,
                'name': '종료일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cts_seq',
                'length': 17,
                'name': '연속시퀀스',
                'required': True,
                'type': 'long'
            }
        ]
    },
    'g3203': {
        'tr_cd': 'g3203',
        'title': '해외주식 API 차트NMIN 조회',
        'blocks': {
            'g3203InBlock': {
                'fields': [{'key': 'delaygb', 'name': '지연구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'keysymbol', 'name': 'KEY종목코드', 'type': 'string', 'length': 18, 'required': True}, {'key': 'exchcd', 'name': '거래소코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'symbol', 'name': '종목코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'ncnt', 'name': '단위(n분)', 'type': 'float', 'length': 4, 'required': True}, {'key': 'qrycnt', 'name': '요청건수(최대-압축:2000비압축:5', 'type': 'float', 'length': 4, 'required': True}, {'key': 'comp_yn', 'name': '압축여부(Y:압축N:비압축)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'sdate', 'name': '시작일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'edate', 'name': '종료일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            }
        }
    },
    'g3204': {
        'tr_cd': 'g3204',
        'title': '해외주식 API 차트일주월년별 조회',
        'fields': [
            {
                'key': 'g3204InBlock',
                'length': None,
                'name': 'g3204InBlock',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'sujung',
                'length': 1,
                'name': '수정주가여부(Y:적용N:비적용)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'delaygb',
                'length': 1,
                'name': '지연구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'keysymbol',
                'length': 18,
                'name': 'KEY종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchcd',
                'length': 2,
                'name': '거래소코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'symbol',
                'length': 16,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'gubun',
                'length': 1,
                'name': '주기구분(5:년)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'qrycnt',
                'length': 4,
                'name': '요청건수(최대-압축:2000비압축:5',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'comp_yn',
                'length': 1,
                'name': '압축여부(Y:압축N:비압축)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sdate',
                'length': 8,
                'name': '시작일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'edate',
                'length': 8,
                'name': '종료일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cts_date',
                'length': 8,
                'name': '연속일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cts_info',
                'length': 6,
                'name': '연속정보',
                'required': True,
                'type': 'string'
            }
        ]
    }
}
