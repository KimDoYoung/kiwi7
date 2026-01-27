# Auto-generated
from typing import Any, Dict, List

MARKET_OVERSEAS_FUTURES_REQUESTS = {
    'CIDBQ01400': {
        'tr_cd': 'CIDBQ01400',
        'title': '해외선물 체결내역개별 조회(주문가능수량)',
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
        'blocks': {
            'CIDEQ00800InBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'TrdDt', 'name': '거래일자', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3101': {
        'tr_cd': 'o3101',
        'title': '해외선물마스터조회',
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
        'blocks': {
            't3521InBlock': {
                'fields': [{'key': 'kind', 'name': '종목종류', 'type': 'string', 'length': 1, 'desc': 'S : 해외지수<br/>R : 해외환율<br/>F : 해외선물', 'required': True}, {'key': 'symbol', 'name': 'SYMBOL', 'type': 'string', 'length': 16, 'desc': '해외지수/환율/선물 SYMBOL<br/>----- 주요해외지수 SYMBOL -----<br/>DJI@DJI       : 다우산업<br/>NAS@IXIC      : 나스닥 종합<br/>SPI@SPX       : S&P 500<br/>USI@SOXX      : 필라델피아 반도체<br/>NII@NI225     : 니케이 225<br/>TWS@TI01      : 대만 가권<br/>SHS@000002    : 상해 A<br/>SHS@000003    : 상해 B<br/>SGI@STI       : 싱가폴 STI<br/>HSI@HSI       : 항셍<br/>PAS@CAC40     : 프랑스 CAC 40<br/>LNS@FTSE100   : 영국 FTSE 100<br/>XTR@DAX30     : 독일 DAX 30<br/>----- 주요해외환율 SYMBOL -----<br/>USDKRWSMBS    : 원/달러<br/>USDJPYCOMP    : 일본 엔/달러<br/>EURUSDCOMP    : 달러/유로<br/>JPYKRWCOMP    : 한국 원/일본 엔<br/>USDCNYCOMP    : 중국 위안/달러<br/>----- 주요해외선물 SYMBOL -----<br/>SPT@DU        : 두바이유 현물<br/>NYM@CL        : WTI 11-10<br/>COM@GC        : 금 11-09<br/>LME@ZDA       : 아연 3M<br/>LME@CDA       : 전기동 3M', 'required': True}],
                'type': 'single'
            }
        }
    }
}
