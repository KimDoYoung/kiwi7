# Auto-generated
from typing import Any, Dict, List

MARKET_DERIVATIVES_ACCOUNT_REQUESTS = {
    'CCENQ10100': {
        'tr_cd': 'CCENQ10100',
        'title': 'KRX야간파생 주문가능수량 조회',
        'blocks': {
            'CCENQ10100InBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'QryTp', 'name': '조회구분', 'type': 'string', 'length': 1, 'desc': '1:일반<br/>2:금액<br/>3:비율', 'required': True}, {'key': 'OrdAmt', 'name': '주문금액', 'type': 'float', 'length': 16, 'desc': '조회구분이 2일경우만 사용, 그외 0', 'required': True}, {'key': 'RatVal', 'name': '비율값', 'type': 'float', 'length': 19.8, 'desc': '조회구분이 3일경우만 사용, 그외 0', 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'length': 1, 'desc': '1:매도<br/>2:매수', 'required': True}, {'key': 'FnoOrdPrc', 'name': '선물옵션주문가격', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'FnoOrdprcPtnCode', 'name': '선물옵션호가유형코드', 'type': 'string', 'length': 2, 'desc': '00:지정가<br/>03:시장가<br/>05:조건부지정가<br/>06:최유리지정가', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CCENQ30100': {
        'tr_cd': 'CCENQ30100',
        'title': 'KRX야간파생 주문/체결내역 조회',
        'blocks': {
            'CCENQ30100InBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'QrySrtDt', 'name': '조회시작일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryEndDt', 'name': '조회종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FnoClssCode', 'name': '선물옵션분류코드', 'type': 'string', 'length': 2, 'desc': '00:전체<br/>11:선물<br/>12:옵션', 'required': True}, {'key': 'PrdgrpCode', 'name': '상품군코드', 'type': 'string', 'length': 2, 'desc': '00:전체', 'required': True}, {'key': 'PrdtExecTpCode', 'name': '체결구분', 'type': 'string', 'length': 1, 'desc': '0:전체,1:체결,2:미체결', 'required': True}, {'key': 'StnlnSeqTp', 'name': '정렬순서구분', 'type': 'string', 'length': 1, 'desc': '1 : 원주문번호역순<br/>2 : 원주문번호순<br/>3 : 주문번호역순<br/>4 : 주문번호순', 'required': True}, {'key': 'MktTpCode', 'name': '시장구분코드', 'type': 'string', 'length': 1, 'desc': '0 : 야간장', 'required': True}, {'key': 'CommdaCode', 'name': '통신매체코드', 'type': 'string', 'length': 2, 'desc': '99', 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'FnoTrdPtnCode', 'name': '선물옵션거래유형코드', 'type': 'string', 'length': 2, 'desc': '03', 'required': True}, {'key': 'GrpId', 'name': '그룹ID', 'type': 'string', 'length': 20, 'desc': '미사용', 'required': True}, {'key': 'UserId', 'name': '사용자ID', 'type': 'string', 'length': 16, 'desc': '미사용', 'required': True}, {'key': 'SrtOrdNo2', 'name': '시작주문번호2', 'type': 'float', 'length': 10, 'desc': '0', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CCENQ90200': {
        'tr_cd': 'CCENQ90200',
        'title': 'KRX야간파생 잔고조회',
        'blocks': {
            'CCENQ90200InBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'desc': '1', 'required': True}, {'key': 'BalEvalTp', 'name': '잔고평가구분', 'type': 'string', 'length': 1, 'desc': '0:기본설정<br/> 1:이동평균법<br/> 2:선입선출법', 'required': True}, {'key': 'FutsPrcEvalTp', 'name': '선물가격평가구분', 'type': 'string', 'length': 1, 'desc': '1:당초가<br/> 2:전일종가', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CCENT00100': {
        'tr_cd': 'CCENT00100',
        'title': 'KRX야간파생 위탁 신규 주문',
        'blocks': {
            'CCENT00100InBlock1': {
                'fields': [{'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'length': 1, 'desc': '1:매도<br/>2:매수', 'required': True}, {'key': 'FnoOrdprcPtnCode', 'name': '선물옵션호가유형코드', 'type': 'string', 'length': 2, 'desc': '00@지정가<br/>03@시장가<br/>05@조건부지정가<br/>06@최유리지정가<br/>10@지정가(IOC)<br/>20@지정가(FOK)<br/>13@시장가(IOC)<br/>23@시장가(FOK)<br/>16@최유리지정가(IOC)<br/>26@최유리지정가(FOK)', 'required': True}, {'key': 'FnoOrdPrc', 'name': '선물옵션주문가격', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CCENT00200': {
        'tr_cd': 'CCENT00200',
        'title': 'KRX야간파생 위탁 정정 주문',
        'blocks': {
            'CCENT00200InBlock1': {
                'fields': [{'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'FnoOrdprcPtnCode', 'name': '선물옵션호가유형코드', 'type': 'string', 'length': 2, 'desc': '00@지정가<br/>03@시장가<br/>05@조건부지정가<br/>06@최유리지정가<br/>10@지정가(IOC)<br/>20@지정가(FOK)<br/>13@시장가(IOC)<br/>23@시장가(FOK)<br/>16@최유리지정가(IOC)<br/>26@최유리지정가(FOK)', 'required': True}, {'key': 'FnoOrdPrc', 'name': '선물옵션주문가격', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'MdfyQty', 'name': '정정수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CCENT00300': {
        'tr_cd': 'CCENT00300',
        'title': 'KRX야간파생 위탁 취소 주문',
        'blocks': {
            'CCENT00300InBlock1': {
                'fields': [{'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'CancQty', 'name': '취소수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOAQ00600': {
        'tr_cd': 'CFOAQ00600',
        'title': '선물옵션 계좌 주문체결내역 조회',
        'blocks': {
            'CFOAQ00600InBlock1': {
                'fields': [{'key': 'QrySrtDt', 'name': '조회시작일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryEndDt', 'name': '조회종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FnoClssCode', 'name': '선물옵션분류코드', 'type': 'string', 'length': 2, 'desc': '00@전체<br/>11@선물<br/>12@옵션', 'required': True}, {'key': 'PrdgrpCode', 'name': '상품군코드', 'type': 'string', 'length': 2, 'desc': '00:전체<br/>01:주가지수<br/>02:개별주식<br/>03:가공채권<br/>04:통화<br/>05:상품<br/>06:금리', 'required': True}, {'key': 'PrdtExecTpCode', 'name': '체결구분', 'type': 'string', 'length': 1, 'desc': '0:전체<br/>1:체결<br/>2:미체결', 'required': True}, {'key': 'StnlnSeqTp', 'name': '정렬순서구분', 'type': 'string', 'length': 1, 'desc': '3:역순<br/>4:정순', 'required': True}, {'key': 'CommdaCode', 'name': '통신매체코드', 'type': 'string', 'length': 2, 'desc': '99', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOAQ10100': {
        'tr_cd': 'CFOAQ10100',
        'title': '선물옵션 주문가능수량조회',
        'blocks': {
            'CFOAQ10100InBlock1': {
                'fields': [{'key': 'QryTp', 'name': '조회구분', 'type': 'string', 'length': 1, 'desc': '1@일반<br/>2@금액<br/>3@비율', 'required': True}, {'key': 'OrdAmt', 'name': '주문금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'RatVal', 'name': '비율값', 'type': 'float', 'length': 19.8, 'desc': '0', 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'length': 1, 'desc': '1@매도<br/>2@매수', 'required': True}, {'key': 'FnoOrdPrc', 'name': '선물옵션주문가격', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'FnoOrdprcPtnCode', 'name': '선물옵션호가유형코드', 'type': 'string', 'length': 2, 'desc': '00@지정가<br/>03@시장가<br/>05@조건부지정가<br/>06@최유리지정가', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOAQ50600': {
        'tr_cd': 'CFOAQ50600',
        'title': '선물옵션 계좌잔고 및 평가현황3',
        'blocks': {
            'CFOAQ50600InBlock1': {
                'fields': [{'key': 'OrdDt', 'name': '주문일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'BalEvalTp', 'name': '잔고평가구분', 'type': 'string', 'length': 1, 'desc': '0@기본설정<br/>1@이동평균법<br/>2@선입선출법', 'required': True}, {'key': 'FutsPrcEvalTp', 'name': '선물가격평가구분', 'type': 'string', 'length': 1, 'desc': '1@당초가<br/>2@전일종가<br/>', 'required': True}, {'key': 'LqdtQtyQryTp', 'name': '청산수량조회구분', 'type': 'string', 'length': 1, 'desc': '1@청산수량산출', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOAT00100': {
        'tr_cd': 'CFOAT00100',
        'title': '선물옵션 정상주문',
        'blocks': {
            'CFOAT00100InBlock1': {
                'fields': [{'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'length': 1, 'desc': '1@매도<br/>2@매수', 'required': True}, {'key': 'FnoOrdprcPtnCode', 'name': '선물옵션호가유형코드', 'type': 'string', 'length': 2, 'desc': '00@지정가<br/>03@시장가<br/>05@조건부지정가<br/>06@최유리지정가<br/>10@지정가(IOC)<br/>20@지정가(FOK)<br/>13@시장가(IOC)<br/>23@시장가(FOK)<br/>16@최유리지정가(IOC)<br/>26@최유리지정가(FOK)', 'required': True}, {'key': 'FnoOrdPrc', 'name': '선물옵션주문가격', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOAT00200': {
        'tr_cd': 'CFOAT00200',
        'title': '선물옵션 정정주문',
        'blocks': {
            'CFOAT00200InBlock1': {
                'fields': [{'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'FnoOrdprcPtnCode', 'name': '선물옵션호가유형코드', 'type': 'string', 'length': 2, 'desc': '00@지정가<br/>03@시장가<br/>05@조건부지정가<br/>06@최유리지정가<br/>10@지정가(IOC)<br/>20@지정가(FOK)<br/>13@시장가(IOC)<br/>23@시장가(FOK)<br/>16@최유리지정가(IOC)<br/>26@최유리지정가(FOK)', 'required': True}, {'key': 'FnoOrdPrc', 'name': '선물옵션주문가격', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'MdfyQty', 'name': '정정수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOAT00300': {
        'tr_cd': 'CFOAT00300',
        'title': '선물옵션 취소주문',
        'blocks': {
            'CFOAT00300InBlock1': {
                'fields': [{'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'CancQty', 'name': '취소수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOBQ10500': {
        'tr_cd': 'CFOBQ10500',
        'title': '선물옵션 계좌예탁금증거금조회',
        'blocks': {
            'CFOBQ10500InBlock1': {
                'fields': [],
                'type': 'single'
            }
        }
    },
    'CFOBQ10800': {
        'tr_cd': 'CFOBQ10800',
        'title': '선물옵션 옵션매도시 주문증거금조회(옵션매도시 1계약당 주문증거금)',
        'blocks': {
            'CFOBQ10800InBlock1': {
                'fields': [{'key': 'SpclDtPtnCode', 'name': '특별일자유형코드', 'type': 'string', 'length': 3, 'desc': '기본 공백, 단, 위클리옵션은 월요일 "MON" , 목요일 "THR"', 'required': True}, {'key': 'SettWklyCnt', 'name': '결제주간수', 'type': 'string', 'length': 2, 'desc': '기본 공백, 단, 위클리옵션은 해당 주물 "W1", "W3", "W4"', 'required': True}, {'key': 'DueYymm', 'name': '만기년월', 'type': 'string', 'length': 6, 'desc': '예)2023년 05월물 <br/>단, 위클리옵션은 공백', 'required': True}, {'key': 'IsuSmclssCode', 'name': '종목소분류코드', 'type': 'string', 'length': 3, 'desc': '501@코스피200<br/>505@미니코스피200<br/>506@코스닥150<br/>509@위클리 ( 월, 목 무관 )<br/>5AF@위클리 ( 월, 목 무관 )', 'required': True}, {'key': 'IsuMdclssCode', 'name': '종목중분류코드', 'type': 'string', 'length': 2, 'desc': '00@전체<br/>01@주가지수<br/>02@개별주식<br/>03@가공채권<br/>04@통화<br/>05@상품<br/>06@금리<br/>10@FLEX', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOEQ11100': {
        'tr_cd': 'CFOEQ11100',
        'title': '선물옵션가정산예탁금상세',
        'blocks': {
            'CFOEQ11100InBlock1': {
                'fields': [{'key': 'BnsDt', 'name': '매매일', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOEQ82600': {
        'tr_cd': 'CFOEQ82600',
        'title': '선물옵션 일별 계좌손익내역',
        'blocks': {
            'CFOEQ82600InBlock1': {
                'fields': [{'key': 'QrySrtDt', 'name': '조회시작일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryEndDt', 'name': '조회종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryTp', 'name': '조회구분', 'type': 'string', 'length': 1, 'desc': '1@일자별<br/>2@월별<br/>3@주간별', 'required': True}, {'key': 'StnlnSeqTp', 'name': '정렬순서구분', 'type': 'string', 'length': 1, 'desc': '1@순<br/>2@역순', 'required': True}, {'key': 'FnoBalEvalTpCode', 'name': '선물옵션잔고평가구분코드', 'type': 'string', 'length': 1, 'desc': '0:계좌에 따라 다르며 기본적으로는 선입선출<br/>1:이동평균<br/>2:선입선출', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOFQ02400': {
        'tr_cd': 'CFOFQ02400',
        'title': '계좌 미결제 약정현황(평균가)',
        'blocks': {
            'CFOFQ02400InBlock1': {
                'fields': [{'key': 'RegMktCode', 'name': '등록시장코드', 'type': 'string', 'length': 2, 'desc': '99@전체<br/>40@KOSPI<br/>20@KOSDAQ<br/>10@KSE<br/>50@KOFEX', 'required': True}, {'key': 'BuyDt', 'name': '매수일자', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    'FOCCQ33600': {
        'tr_cd': 'FOCCQ33600',
        'title': '주식계좌 기간별수익률 상세',
        'blocks': {
            'FOCCQ33600InBlock1': {
                'fields': [{'key': 'QrySrtDt', 'name': '조회시작일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryEndDt', 'name': '조회종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'TermTp', 'name': '기간구분', 'type': 'string', 'length': 1, 'desc': '1:일별, 2:주별, 3:월별', 'required': True}],
                'type': 'single'
            }
        }
    },
    'FOCCQ33700': {
        'tr_cd': 'FOCCQ33700',
        'title': '선물옵션 기간별 계좌 수익률 현황',
        'blocks': {
            'FOCCQ33700InBlock1': {
                'fields': [{'key': 'QrySrtDt', 'name': '조회시작일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryEndDt', 'name': '조회종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryTp', 'name': '조회구분', 'type': 'string', 'length': 1, 'desc': '1.평균예탁자산기준<br/>2.투입자산기준(기초자산+입출금액)<br/>3.투입자산기준(기초자산+입금액)', 'required': True}, {'key': 'BaseAmtTp', 'name': '기준금액구분', 'type': 'string', 'length': 1, 'desc': '1@평균예탁자산기준<br/>2@투입자산기준(기초자산+입출금액)<br/>3@투입자산기준(기초자산+입금액)', 'required': True}, {'key': 'QryTermTp', 'name': '조회기간구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'PnlCalcTpCode', 'name': '손익산출구분코드', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    'MMDAQ91200': {
        'tr_cd': 'MMDAQ91200',
        'title': '파생상품증거금율조회',
        'blocks': {
            'MMDAQ91200InBlock1': {
                'fields': [{'key': 'IsuLgclssCode', 'name': '종목대분류코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'IsuMdclssCode', 'name': '종목중분류코드', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            }
        }
    }
}
