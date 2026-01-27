# Auto-generated
from typing import Any, Dict, List

MARKET_REQUESTS = {
    'AFR': {
        'tr_cd': 'AFR',
        'title': 'API사용자조건검색실시간',
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
                'desc': 't1860 TR의 t1860OutBlock. sAlertNum (실시간키)',
                'key': 'tr_key',
                'length': 11,
                'name': '사용자구분키',
                'type': 'string'
            }
        ]
    },
    'BMT': {
        'tr_cd': 'BMT',
        'title': '시간대별투자자매매추이',
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
                'desc': '001 : 코스피<br/>101 : KP200<br/>301 : 코스닥<br/>550 : ELW<br/>560 : ETF<br/>600 : 주식선물<br/>700 : 콜옵션<br/>800 : 풋옵션<br/>900 : 선물<br/>940 : 미니KP200선물<br/>941 : 미니KP200옵션-콜<br/>942 : 미니KP200옵션-풋<br/>946 : 코스피200위클리-콜<br/>947 : 코스피200위클리-풋',
                'key': 'tr_key',
                'length': 3,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'BM_': {
        'tr_cd': 'BM_',
        'title': '업종별투자자별매매현황',
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
                'desc': '001 : 코스피<br/>101 : KP200<br/>301 : 코스닥<br/>550 : ELW<br/>560 : ETF<br/>600 : 주식선물<br/>700 : 콜옵션<br/>800 : 풋옵션<br/>900 : 선물<br/>940 : 미니KP200선물<br/>941 : 미니KP200옵션-콜<br/>942 : 미니KP200옵션-풋<br/>946 : 코스피200위클리-콜<br/>947 : 코스피200위클리-풋',
                'key': 'tr_key',
                'length': 3,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'CUR': {
        'tr_cd': 'CUR',
        'title': '현물정보USD실시간',
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
    'DH1': {
        'tr_cd': 'DH1',
        'title': 'KOSPI시간외단일가호가잔량',
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
    'DHA': {
        'tr_cd': 'DHA',
        'title': 'KOSDAQ시간외단일가호가잔량',
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
    'DK3': {
        'tr_cd': 'DK3',
        'title': 'KOSDAQ시간외단일가체결',
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
    'DS3': {
        'tr_cd': 'DS3',
        'title': 'KOSPI시간외단일가체결',
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
    'DVI': {
        'tr_cd': 'DVI',
        'title': '시간외단일가VI발동해제',
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
                'desc': '단축코드 6자리 또는 전체종목 \'000000\'',
                'key': 'tr_key',
                'length': 6,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'H1_': {
        'tr_cd': 'H1_',
        'title': 'KOSPI호가잔량',
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
    'H2_': {
        'tr_cd': 'H2_',
        'title': 'KOSPI장전시간외호가잔량',
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
    'HA_': {
        'tr_cd': 'HA_',
        'title': 'KOSDAQ호가잔량',
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
    'HB_': {
        'tr_cd': 'HB_',
        'title': 'KOSDAQ장전시간외호가잔량',
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
    'IJ_': {
        'tr_cd': 'IJ_',
        'title': '지수',
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
    'JIF': {
        'tr_cd': 'JIF',
        'title': '장운영정보',
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
    'K1_': {
        'tr_cd': 'K1_',
        'title': 'KOSPI거래원',
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
    'K3_': {
        'tr_cd': 'K3_',
        'title': 'KOSDAQ체결',
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
    'KH_': {
        'tr_cd': 'KH_',
        'title': 'KOSDAQ프로그램매매종목별',
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
    'KM_': {
        'tr_cd': 'KM_',
        'title': 'KOSDAQ프로그램매매전체집계',
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
    'KS_': {
        'tr_cd': 'KS_',
        'title': 'KOSDAQ우선호가',
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
    'MK2': {
        'tr_cd': 'MK2',
        'title': 'US지수',
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
                'desc': 'DJI@DJI         : 다우산업<br/>NAS@IXIC      : 나스닥 종합<br/>SPI@SPX       : S&P 500<br/>USI@SOXX      : 필라델피아 반도체',
                'key': 'tr_key',
                'length': 16,
                'name': '심볼코드',
                'type': 'string'
            }
        ]
    },
    'NBM': {
        'tr_cd': 'NBM',
        'title': '(NXT)업종별투자자별매매현황',
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
                'desc': 'N + 업종코드',
                'key': 'tr_key',
                'length': 4,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'NBT': {
        'tr_cd': 'NBT',
        'title': '(NXT)시간대별투자자매매추이',
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
                'desc': 'N + 업종코드',
                'key': 'tr_key',
                'length': 4,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'NH1': {
        'tr_cd': 'NH1',
        'title': '(NXT)호가잔량',
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
                'desc': '단축코드 7자리 + 공백 3자리',
                'key': 'tr_key',
                'length': 10,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'NK1': {
        'tr_cd': 'NK1',
        'title': '(NXT)거래원',
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
                'desc': '단축코드 7자리 + 공백 3자리',
                'key': 'tr_key',
                'length': 10,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'NPH': {
        'tr_cd': 'NPH',
        'title': '(NXT)프로그램매매종목별',
        'fields': [
            {
                'desc': 'LS증권 거래코드',
                'key': 'tr_cd',
                'length': 3,
                'name': '거래 CD',
                'type': 'string'
            },
            {
                'desc': '단축코드 7자리 + 공백 3자리',
                'key': 'tr_key',
                'length': 10,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'NPM': {
        'tr_cd': 'NPM',
        'title': '(NXT)프로그램매매전체집계',
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
                'desc': '\'N\' + 구분값<br/>N0:코스피<br/>N1:코스닥',
                'key': 'tr_key',
                'length': 2,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'NS2': {
        'tr_cd': 'NS2',
        'title': '(NXT)우선호가',
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
                'desc': '단축코드 7자리 + 공백 3자리',
                'key': 'tr_key',
                'length': 10,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'NS3': {
        'tr_cd': 'NS3',
        'title': '(NXT)체결',
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
                'desc': '단축코드 7자리 + 공백 3자리',
                'key': 'tr_key',
                'length': 10,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'NVI': {
        'tr_cd': 'NVI',
        'title': '(NXT)VI 발동 해제',
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
                'desc': '\'N\' + 단축코드 6자리 + 공백 3자리',
                'key': 'tr_key',
                'length': 10,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'NWS': {
        'tr_cd': 'NWS',
        'title': '실시간뉴스제목패킷',
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
    'NYS': {
        'tr_cd': 'NYS',
        'title': '(NXT)예상체결',
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
                'desc': '단축코드 7자리 + 공백 3자리',
                'key': 'tr_key',
                'length': 110,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'OK_': {
        'tr_cd': 'OK_',
        'title': 'KOSDAQ거래원',
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
    'PH_': {
        'tr_cd': 'PH_',
        'title': 'KOSPI프로그램매매종목별',
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
    'PM_': {
        'tr_cd': 'PM_',
        'title': 'KOSPI프로그램매매전체집계',
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
    'S2_': {
        'tr_cd': 'S2_',
        'title': 'KOSPI우선호가',
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
    'S3_': {
        'tr_cd': 'S3_',
        'title': 'KOSPI체결',
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
    'S4_': {
        'tr_cd': 'S4_',
        'title': 'KOSPI기세',
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
    'SC1': {
        'tr_cd': 'SC1',
        'title': '주식주문체결',
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
    'SC2': {
        'tr_cd': 'SC2',
        'title': '주식주문정정',
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
    'SC4': {
        'tr_cd': 'SC4',
        'title': '주식주문거부',
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
    'SHC': {
        'tr_cd': 'SHC',
        'title': '상/하한가근접진입',
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
    'SHD': {
        'tr_cd': 'SHD',
        'title': '상/하한가근접이탈',
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
    'SHI': {
        'tr_cd': 'SHI',
        'title': '상/하한가진입',
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
    'SHO': {
        'tr_cd': 'SHO',
        'title': '상/하한가이탈',
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
    'UBM': {
        'tr_cd': 'UBM',
        'title': '(통합) 업종별투자자별매매현황',
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
                'desc': 'U + 업종코드',
                'key': 'tr_key',
                'length': 4,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'UBT': {
        'tr_cd': 'UBT',
        'title': '(통합)시간대별투자자매매추이',
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
                'desc': 'U + 업종코드',
                'key': 'tr_key',
                'length': 4,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'UH1': {
        'tr_cd': 'UH1',
        'title': '(통합)호가잔량',
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
                'desc': '단축코드 7자리 + 공백 3자리',
                'key': 'tr_key',
                'length': 10,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'UK1': {
        'tr_cd': 'UK1',
        'title': '(통합)거래원',
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
                'desc': '단축코드 7자리 + 공백 3자리',
                'key': 'tr_key',
                'length': 10,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'UPH': {
        'tr_cd': 'UPH',
        'title': '(통합)프로그램매매종목별',
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
                'desc': '단축코드 7자리 + 공백 3자리',
                'key': 'tr_key',
                'length': 10,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'UPM': {
        'tr_cd': 'UPM',
        'title': '(통합)프로그램매매전체집계',
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
                'desc': '\'U\' + 구분값<br/>U0:코스피<br/>U1:코스닥',
                'key': 'tr_key',
                'length': 2,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'US2': {
        'tr_cd': 'US2',
        'title': '(통합)우선호가',
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
                'desc': '단축코드 7자리 + 공백 3자리',
                'key': 'tr_key',
                'length': 10,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'US3': {
        'tr_cd': 'US3',
        'title': '(통합)체결',
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
                'desc': '단축코드 7자리 + 공백 3자리',
                'key': 'tr_key',
                'length': 10,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'UVI': {
        'tr_cd': 'UVI',
        'title': '(통합)VI발동해제',
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
                'desc': '\'U\' + 단축코드 6자리 + 공백 3자리',
                'key': 'tr_key',
                'length': 10,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'UYS': {
        'tr_cd': 'UYS',
        'title': '(통합)예상체결',
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
                'desc': '단축코드 7자리 + 공백 3자리',
                'key': 'tr_key',
                'length': 10,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'VI_': {
        'tr_cd': 'VI_',
        'title': 'VI발동해제',
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
                'desc': '단축코드 6자리',
                'key': 'tr_key',
                'length': 6,
                'name': '단축코드',
                'type': 'string'
            }
        ]
    },
    'YJ_': {
        'tr_cd': 'YJ_',
        'title': '예상지수',
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
    'YK3': {
        'tr_cd': 'YK3',
        'title': 'KOSDAQ예상체결',
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
    'YS3': {
        'tr_cd': 'YS3',
        'title': 'KOSPI예상체결',
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
}
