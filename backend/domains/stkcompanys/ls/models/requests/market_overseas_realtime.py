# Auto-generated
from typing import Any, Dict, List

MARKET_OVERSEAS_REALTIME_REQUESTS = {
    'AS0': {
        'tr_cd': 'AS0',
        'title': '해외주식주문접수(미국)',
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
    'COSMT00300': {
        'tr_cd': 'COSMT00300',
        'title': '해외증권 매도상환주문(미국)',
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
        'url': '/overseas-stock/accno',
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
    }
}
