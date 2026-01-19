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
    'CIDBQ01400': {
        'tr_cd': 'CIDBQ01400',
        'title': '해외선물 체결내역개별 조회(주문가능수량)',
        'blocks': {
            'CIDBQ01400InBlock1': {
                'fields': [{'key': 'QryTpCode', 'name': '조회구분코드', 'type': 'string', 'length': 1, 'desc': '1:신규 2:청산 3:총가능', 'required': True}, {'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'desc': '1:매도 2:매수', 'required': True}, {'key': 'OvrsDrvtOrdPrc', 'name': '해외파생주문가격', 'type': 'float', 'length': 30.11, 'desc': '지정가 (시장가인경우 0)', 'required': True}, {'key': 'AbrdFutsOrdPtnCode', 'name': '해외선물주문유형코드', 'type': 'string', 'length': 1, 'desc': '1: 시장가 2: 지정가', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDBQ01500': {
        'tr_cd': 'CIDBQ01500',
        'title': '해외선물 미결제잔고내역 조회',
        'blocks': {
            'CIDBQ01500InBlock1': {
                'fields': [{'key': 'AcntTpCode', 'name': '계좌구분코드', 'type': 'string', 'length': 1, 'desc': '1:위탁', 'required': True}, {'key': 'QryDt', 'name': '조회일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'BalTpCode', 'name': '잔고구분코드', 'type': 'string', 'length': 1, 'desc': '1:합산<br/>2:건별', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDBQ01800': {
        'tr_cd': 'CIDBQ01800',
        'title': '해외선물 주문내역 조회',
        'blocks': {
            'CIDBQ01800InBlock1': {
                'fields': [{'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'OrdDt', 'name': '주문일자', 'type': 'string', 'length': 8, 'desc': 'YYYYMMDD 형식', 'required': True}, {'key': 'ThdayTpCode', 'name': '당일구분코드', 'type': 'string', 'length': 1, 'desc': 'SPACE', 'required': True}, {'key': 'OrdStatCode', 'name': '주문상태코드', 'type': 'string', 'length': 1, 'desc': '0:전체<br/>1:체결<br/>2:미체결', 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'desc': '0:전체<br/>1:매도<br/>2:매수', 'required': True}, {'key': 'QryTpCode', 'name': '조회구분코드', 'type': 'string', 'length': 1, 'desc': '1:역순<br/>2:정순', 'required': True}, {'key': 'OrdPtnCode', 'name': '주문유형코드', 'type': 'string', 'length': 2, 'desc': '00:전체<br/>01:일반<br/>02:Average<br/>03:Spread', 'required': True}, {'key': 'OvrsDrvtFnoTpCode', 'name': '해외파생선물옵션구분코드', 'type': 'string', 'length': 1, 'desc': 'A:전체<br/>F:선물<br/>O:옵션', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDBQ02400': {
        'tr_cd': 'CIDBQ02400',
        'title': '해외선물 주문체결내역 상세 조회',
        'blocks': {
            'CIDBQ02400InBlock1': {
                'fields': [{'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'QrySrtDt', 'name': '조회시작일자', 'type': 'string', 'length': 8, 'desc': 'YYYYMMDD 형식<br/>과거조회시는 사용<br/>당일조회시는 공백', 'required': True}, {'key': 'QryEndDt', 'name': '조회종료일자', 'type': 'string', 'length': 8, 'desc': 'YYYYMMDD 형식<br/>과거조회시는 사용<br/>당일조회시는 공백', 'required': True}, {'key': 'ThdayTpCode', 'name': '당일구분코드', 'type': 'string', 'length': 1, 'desc': '0:과거조회<br/>1:당일조회', 'required': True}, {'key': 'OrdStatCode', 'name': '주문상태코드', 'type': 'string', 'length': 1, 'desc': '0:전체<br/>1:체결<br/>2:미체결', 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'desc': '0:전체<br/>1:매도<br/>2:매수', 'required': True}, {'key': 'QryTpCode', 'name': '조회구분코드', 'type': 'string', 'length': 1, 'desc': '1:역순<br/>2:정순', 'required': True}, {'key': 'OrdPtnCode', 'name': '주문유형코드', 'type': 'string', 'length': 2, 'desc': '00:전체<br/>01:일반<br/>02:Average<br/>03:Spread', 'required': True}, {'key': 'OvrsDrvtFnoTpCode', 'name': '해외파생선물옵션구분코드', 'type': 'string', 'length': 1, 'desc': 'A:전체<br/>F:선물<br/>O:옵션', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDBQ03000': {
        'tr_cd': 'CIDBQ03000',
        'title': '해외선물 예수금/잔고현황',
        'blocks': {
            'CIDBQ03000InBlock1': {
                'fields': [{'key': 'AcntTpCode', 'name': '계좌구분코드', 'type': 'string', 'length': 1, 'desc': '1 : 위탁계좌 2 : 중개계좌', 'required': True}, {'key': 'TrdDt', 'name': '거래일자', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDBQ05300': {
        'tr_cd': 'CIDBQ05300',
        'title': '해외선물 예탁자산 조회',
        'blocks': {
            'CIDBQ05300InBlock1': {
                'fields': [{'key': 'OvrsAcntTpCode', 'name': '해외계좌구분코드', 'type': 'string', 'length': 1, 'desc': '1:위탁', 'required': True}, {'key': 'CrcyCode', 'name': '통화코드', 'type': 'string', 'length': 3, 'desc': 'ALL:전체 CAD:캐나다 달러 CHF:스위스 프랑 EUR:유럽연합 유로 GBP:영국 파운드 HKD:홍콩 달러 JPY:일본 엔 SGD:싱가포르 달러 USD:미국 달러', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDBT00100': {
        'tr_cd': 'CIDBT00100',
        'title': '해외선물 신규주문',
        'blocks': {
            'CIDBT00100InBlock1': {
                'fields': [{'key': 'OrdDt', 'name': '주문일자', 'type': 'string', 'length': 8, 'desc': 'YYYYMMDD 형식', 'required': True}, {'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'FutsOrdTpCode', 'name': '선물주문구분코드', 'type': 'string', 'length': 1, 'desc': '1:신규', 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'desc': '1:매도<br/>2:매수', 'required': True}, {'key': 'AbrdFutsOrdPtnCode', 'name': '해외선물주문유형코드', 'type': 'string', 'length': 1, 'desc': '1:시장가<br/>2:지정가', 'required': True}, {'key': 'CrcyCode', 'name': '통화코드', 'type': 'string', 'length': 3, 'desc': 'SPACE', 'required': True}, {'key': 'OvrsDrvtOrdPrc', 'name': '해외파생주문가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'CndiOrdPrc', 'name': '조건주문가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PrdtCode', 'name': '상품코드', 'type': 'string', 'length': 6, 'desc': 'SPACE', 'required': True}, {'key': 'DueYymm', 'name': '만기년월', 'type': 'string', 'length': 6, 'desc': 'SPACE', 'required': True}, {'key': 'ExchCode', 'name': '거래소코드', 'type': 'string', 'length': 10, 'desc': 'SPACE', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDBT00900': {
        'tr_cd': 'CIDBT00900',
        'title': '해외선물 정정주문',
        'blocks': {
            'CIDBT00900InBlock1': {
                'fields': [{'key': 'OrdDt', 'name': '주문일자', 'type': 'string', 'length': 8, 'desc': 'YYYYMMDD 형식', 'required': True}, {'key': 'OvrsFutsOrgOrdNo', 'name': '해외선물원주문번호', 'type': 'string', 'length': 10, 'required': True}, {'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'FutsOrdTpCode', 'name': '선물주문구분코드', 'type': 'string', 'length': 1, 'desc': '2:정정', 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'desc': '1:매도<br/>2:매수', 'required': True}, {'key': 'FutsOrdPtnCode', 'name': '선물주문유형코드', 'type': 'string', 'length': 1, 'desc': '2:지정가', 'required': True}, {'key': 'CrcyCodeVal', 'name': '통화코드값', 'type': 'string', 'length': 3, 'desc': 'SPACE', 'required': True}, {'key': 'OvrsDrvtOrdPrc', 'name': '해외파생주문가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'CndiOrdPrc', 'name': '조건주문가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OvrsDrvtPrdtCode', 'name': '해외파생상품코드', 'type': 'string', 'length': 10, 'desc': 'SPACE', 'required': True}, {'key': 'DueYymm', 'name': '만기년월', 'type': 'string', 'length': 6, 'desc': 'SPACE', 'required': True}, {'key': 'ExchCode', 'name': '거래소코드', 'type': 'string', 'length': 10, 'desc': 'SPACE', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDBT01000': {
        'tr_cd': 'CIDBT01000',
        'title': '해외선물 취소주문',
        'blocks': {
            'CIDBT01000InBlock1': {
                'fields': [{'key': 'OrdDt', 'name': '주문일자', 'type': 'string', 'length': 8, 'desc': 'YYYYMMDD 형식', 'required': True}, {'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'OvrsFutsOrgOrdNo', 'name': '해외선물원주문번호', 'type': 'string', 'length': 10, 'required': True}, {'key': 'FutsOrdTpCode', 'name': '선물주문구분코드', 'type': 'string', 'length': 1, 'desc': '3:취소', 'required': True}, {'key': 'PrdtTpCode', 'name': '상품구분코드', 'type': 'string', 'length': 2, 'desc': 'SPACE', 'required': True}, {'key': 'ExchCode', 'name': '거래소코드', 'type': 'string', 'length': 10, 'desc': 'SPACE', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDEQ00800': {
        'tr_cd': 'CIDEQ00800',
        'title': '일자별 미결제 잔고내역',
        'blocks': {
            'CIDEQ00800InBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'TrdDt', 'name': '거래일자', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
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
    'COSMT00300': {
        'tr_cd': 'COSMT00300',
        'title': '해외증권 매도상환주문(미국)',
        'fields': [
            {
                'key': 'COSMT00300InBlock1',
                'length': None,
                'name': 'COSMT00300InBlock1',
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
                'key': 'OrdPtnCode',
                'length': 2,
                'name': '주문유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'OrgOrdNo',
                'length': 10,
                'name': '원주문번호',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'AcntNo',
                'length': 20,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'InptPwd',
                'length': 8,
                'name': '입력비밀번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'OrdMktCode',
                'length': 2,
                'name': '주문시장코드',
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
                'key': 'BrkTpCode',
                'length': 2,
                'name': '중개인구분코드',
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
            }
        ]
    },
    'COSOQ00201': {
        'tr_cd': 'COSOQ00201',
        'title': '해외주식 종합잔고평가 API',
        'fields': [
            {
                'key': 'COSOQ00201InBlock1',
                'length': None,
                'name': 'COSOQ00201InBlock1',
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
                'key': 'BaseDt',
                'length': 8,
                'name': '기준일자',
                'required': True,
                'type': 'string'
            },
            {
                'desc': 'ALL@전체<br/>USD@미국',
                'key': 'CrcyCode',
                'length': 3,
                'name': '통화코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '00 전체<br/>10 일반<br/>20 소수점',
                'key': 'AstkBalTpCode',
                'length': 2,
                'name': '해외증권잔고구분코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'COSOQ02701': {
        'tr_cd': 'COSOQ02701',
        'title': '해외주식 예수금 조회 API',
        'blocks': {
            'COSOQ02701InBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'CrcyCode', 'name': '통화코드', 'type': 'string', 'length': 3, 'required': True}],
                'type': 'single'
            }
        }
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
    },
    'o3101': {
        'tr_cd': 'o3101',
        'title': '해외선물마스터조회',
        'blocks': {
            'o3101InBlock': {
                'fields': [{'key': 'gubun', 'name': '입력구분(예비)', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3103': {
        'tr_cd': 'o3103',
        'title': '해외선물차트 분봉 조회',
        'blocks': {
            'o3103InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'desc': 'ex) ADU13', 'required': True}, {'key': 'ncnt', 'name': 'N분주기', 'type': 'float', 'length': 4, 'desc': 'ex) 0(30초), 1(1분), 30(30분), …', 'required': True}, {'key': 'readcnt', 'name': '조회건수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3104': {
        'tr_cd': 'o3104',
        'title': '해외선물 일별체결 조회',
        'blocks': {
            'o3104InBlock': {
                'fields': [{'key': 'gubun', 'name': '조회구분', 'type': 'string', 'length': 1, 'desc': '0:일별 1:주별 2:월별', 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'date', 'name': '조회일자', 'type': 'string', 'length': 8, 'desc': 'YYYYMMDD', 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3105': {
        'tr_cd': 'o3105',
        'title': '해외선물 현재가(종목정보) 조회',
        'blocks': {
            'o3105InBlock': {
                'fields': [{'key': 'symbol', 'name': '종목심볼', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3106': {
        'tr_cd': 'o3106',
        'title': '해외선물 현재가호가 조회',
        'blocks': {
            'o3106InBlock': {
                'fields': [{'key': 'symbol', 'name': '종목심볼', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3107': {
        'tr_cd': 'o3107',
        'title': '해외선물 관심종목 조회',
        'blocks': {
            'o3107InBlock (Occurs)': {
                'fields': [{'key': 'symbol', 'name': '종목심볼', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    'o3108': {
        'tr_cd': 'o3108',
        'title': '해외선물차트(일주월) 조회',
        'blocks': {
            'o3108InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 16, 'desc': 'ex) ADU13', 'required': True}, {'key': 'gubun', 'name': '주기구분', 'type': 'string', 'length': 1, 'desc': 'ex) 0(일), 1(주), 2(월)', 'required': True}, {'key': 'qrycnt', 'name': '요청건수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'sdate', 'name': '시작일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'edate', 'name': '종료일자', 'type': 'string', 'length': 8, 'desc': 'ex) 조회당일', 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3116': {
        'tr_cd': 'o3116',
        'title': '해외선물 시간대별(Tick)체결 조회',
        'blocks': {
            'o3116InBlock': {
                'fields': [{'key': 'gubun', 'name': '조회구분', 'type': 'string', 'length': 1, 'desc': '0:당일 만 사용가능', 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'readcnt', 'name': '조회갯수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'cts_seq', 'name': '순번CTS', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3117': {
        'tr_cd': 'o3117',
        'title': '해외선물 차트 NTick 체결 조회',
        'blocks': {
            'o3117InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'ncnt', 'name': '단위', 'type': 'float', 'length': 4, 'required': True}, {'key': 'qrycnt', 'name': '건수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'cts_seq', 'name': '순번CTS', 'type': 'string', 'length': 10, 'required': True}, {'key': 'cts_daygb', 'name': '당일구분CTS', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3121': {
        'tr_cd': 'o3121',
        'title': '해외선물옵션 마스터 조회',
        'blocks': {
            'o3121InBlock': {
                'fields': [{'key': 'MktGb', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': 'ex) F(선물), O(옵션)', 'required': True}, {'key': 'BscGdsCd', 'name': '옵션기초상품코드', 'type': 'string', 'length': 10, 'desc': "ex) ['시장구분' 옵션의 경우]      공란(옵션상품 목록),      O_ES(ES상품옵션종목 목록)", 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3123': {
        'tr_cd': 'o3123',
        'title': '해외선물옵션 차트 분봉 조회',
        'blocks': {
            'o3123InBlock': {
                'fields': [{'key': 'mktgb', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': 'ex) F(선물), O(옵션)', 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 16, 'desc': 'ex) ADU13,2ESF16_1915', 'required': True}, {'key': 'ncnt', 'name': 'N분주기', 'type': 'float', 'length': 4, 'desc': 'ex) 0(30초), 1(1분), 30(30분), …', 'required': True}, {'key': 'readcnt', 'name': '조회건수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3125': {
        'tr_cd': 'o3125',
        'title': '해외선물옵션 현재가(종목정보) 조회',
        'blocks': {
            'o3125InBlock': {
                'fields': [{'key': 'mktgb', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': 'ex) F(선물), O(옵션)', 'required': True}, {'key': 'symbol', 'name': '종목심볼', 'type': 'string', 'length': 16, 'desc': 'ex) 2ESF16_1915', 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3126': {
        'tr_cd': 'o3126',
        'title': '해외선물옵션 현재가호가 조회',
        'blocks': {
            'o3126InBlock': {
                'fields': [{'key': 'mktgb', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': 'ex) F(선물), O(옵션)', 'required': True}, {'key': 'symbol', 'name': '종목심볼', 'type': 'string', 'length': 16, 'desc': 'ex) 2ESF16_1915', 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3127': {
        'tr_cd': 'o3127',
        'title': '해외선물옵션 관심종목 조회',
        'blocks': {
            'o3127InBlock': {
                'fields': [{'key': 'nrec', 'name': '건수', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            'o3127InBlock1 (Occurs)': {
                'fields': [{'key': 'mktgb', 'name': '기본입력', 'type': 'string', 'length': 1, 'desc': 'ex) F(선물), O(옵션)', 'required': True}, {'key': 'symbol', 'name': '종목심볼', 'type': 'string', 'length': 16, 'desc': 'ex) 2ESF16_1915', 'required': True}],
                'type': 'array'
            }
        }
    },
    'o3128': {
        'tr_cd': 'o3128',
        'title': '해외선물옵션 차트 일주월 조회',
        'blocks': {
            'o3128InBlock': {
                'fields': [{'key': 'mktgb', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': 'ex) F(선물), O(옵션)', 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 16, 'desc': 'ex) ADU13,2ESF16_1915', 'required': True}, {'key': 'gubun', 'name': '주기구분', 'type': 'string', 'length': 1, 'desc': 'ex) 0(일), 1(주), 2(월)', 'required': True}, {'key': 'qrycnt', 'name': '요청건수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'sdate', 'name': '시작일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'edate', 'name': '종료일자', 'type': 'string', 'length': 8, 'desc': 'ex) 조회당일', 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3136': {
        'tr_cd': 'o3136',
        'title': '해외선물옵션 시간대별 Tick 체결 조회',
        'blocks': {
            'o3136InBlock': {
                'fields': [{'key': 'gubun', 'name': '조회구분', 'type': 'string', 'length': 1, 'desc': 'ex) 0(당일), 1(전일)', 'required': True}, {'key': 'mktgb', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': 'ex) F(선물), O(옵션)', 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 16, 'desc': 'ex) 2ESF16_1915', 'required': True}, {'key': 'readcnt', 'name': '조회갯수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'cts_seq', 'name': '순번CTS', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3137': {
        'tr_cd': 'o3137',
        'title': '해외선물옵션 차트 NTick 체결 조회',
        'blocks': {
            'o3137InBlock': {
                'fields': [{'key': 'mktgb', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': 'ex) F(선물), O(옵션)', 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 16, 'desc': 'ex) 2ESF16_1915', 'required': True}, {'key': 'ncnt', 'name': '단위', 'type': 'float', 'length': 4, 'required': True}, {'key': 'qrycnt', 'name': '건수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'cts_seq', 'name': '순번CTS', 'type': 'string', 'length': 10, 'required': True}, {'key': 'cts_daygb', 'name': '당일구분CTS', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3139': {
        'tr_cd': 'o3139',
        'title': '해외선물옵션차트용NTick(고정형)-API용',
        'blocks': {
            'o3139InBlock': {
                'fields': [{'key': 'mktgb', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': 'ex) F(선물), O(옵션)', 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 16, 'desc': 'ex) 2ESF16_1915', 'required': True}, {'key': 'ncnt', 'name': '단위', 'type': 'float', 'length': 4, 'required': True}, {'key': 'qrycnt', 'name': '건수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'cts_seq', 'name': '순번CTS', 'type': 'string', 'length': 10, 'required': True}, {'key': 'cts_daygb', 'name': '당일구분CTS', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            }
        }
    },
    't3518': {
        'tr_cd': 't3518',
        'title': '해외실시간지수',
        'blocks': {
            't3518InBlock': {
                'fields': [{'key': 'kind', 'name': '종목종류', 'type': 'string', 'length': 1, 'desc': 'S:해외지수 F:해외선물 R:환율/금리', 'required': True}, {'key': 'symbol', 'name': 'SYMBOL', 'type': 'string', 'length': 16, 'required': True}, {'key': 'cnt', 'name': '입력건수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'jgbn', 'name': '조회구분', 'type': 'string', 'length': 1, 'desc': '0:일 1:주 2:월 3:분 4:틱', 'required': True}, {'key': 'nmin', 'name': 'N분', 'type': 'float', 'length': 3, 'desc': 'jgbn이 3인 경우에 n분', 'required': True}, {'key': 'cts_date', 'name': 'CTS_DATE', 'type': 'string', 'length': 8, 'desc': '다음 조회시 OutBlock의 cts_date 입력 처음 조회시 스페이스', 'required': True}, {'key': 'cts_time', 'name': 'CTS_TIME', 'type': 'string', 'length': 6, 'desc': '다음 조회시 OutBlock의 cts_time 입력 처음 조회시 스페이스', 'required': True}],
                'type': 'single'
            }
        }
    },
    't3521': {
        'tr_cd': 't3521',
        'title': '해외지수조회(API용)',
        'blocks': {
            't3521InBlock': {
                'fields': [{'key': 'kind', 'name': '종목종류', 'type': 'string', 'length': 1, 'desc': 'S : 해외지수<br/>R : 해외환율<br/>F : 해외선물', 'required': True}, {'key': 'symbol', 'name': 'SYMBOL', 'type': 'string', 'length': 16, 'desc': '해외지수/환율/선물 SYMBOL<br/>----- 주요해외지수 SYMBOL -----<br/>DJI@DJI       : 다우산업<br/>NAS@IXIC      : 나스닥 종합<br/>SPI@SPX       : S&P 500<br/>USI@SOXX      : 필라델피아 반도체<br/>NII@NI225     : 니케이 225<br/>TWS@TI01      : 대만 가권<br/>SHS@000002    : 상해 A<br/>SHS@000003    : 상해 B<br/>SGI@STI       : 싱가폴 STI<br/>HSI@HSI       : 항셍<br/>PAS@CAC40     : 프랑스 CAC 40<br/>LNS@FTSE100   : 영국 FTSE 100<br/>XTR@DAX30     : 독일 DAX 30<br/>----- 주요해외환율 SYMBOL -----<br/>USDKRWSMBS    : 원/달러<br/>USDJPYCOMP    : 일본 엔/달러<br/>EURUSDCOMP    : 달러/유로<br/>JPYKRWCOMP    : 한국 원/일본 엔<br/>USDCNYCOMP    : 중국 위안/달러<br/>----- 주요해외선물 SYMBOL -----<br/>SPT@DU        : 두바이유 현물<br/>NYM@CL        : WTI 11-10<br/>COM@GC        : 금 11-09<br/>LME@ZDA       : 아연 3M<br/>LME@CDA       : 전기동 3M', 'required': True}],
                'type': 'single'
            }
        }
    }
}
