# Auto-generated
from typing import Any, Dict, List

MARKET_OTHER_REQUESTS = {
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
    'CDPCQ04700': {
        'tr_cd': 'CDPCQ04700',
        'title': '계좌 거래내역',
        'blocks': {
            'CDPCQ04700InBlock1': {
                'fields': [{'key': 'QryTp', 'name': '조회구분', 'type': 'string', 'length': 1, 'desc': '0@전체, 1@입출금, 2@입출고, 3@매매, 4@환전, 9@기타', 'required': True}, {'key': 'QrySrtDt', 'name': '조회시작일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryEndDt', 'name': '조회종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'SrtNo', 'name': '시작번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'PdptnCode', 'name': '상품유형코드', 'type': 'string', 'length': 2, 'desc': '01', 'required': True}, {'key': 'IsuLgclssCode', 'name': '종목대분류코드', 'type': 'string', 'length': 2, 'desc': '00@전체, 01@주식, 02@채권, 04@펀드, 03@선물, 05@해외주식, 06@해외파생', 'required': True}, {'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CLNAQ00100': {
        'tr_cd': 'CLNAQ00100',
        'title': '예탁담보융자가능종목현황조회',
        'blocks': {
            'CLNAQ00100InBlock1': {
                'fields': [{'key': 'QryTp', 'name': '조회구분', 'type': 'string', 'length': 1, 'desc': '0@전체, 1@가능, 2@불가능', 'required': True}, {'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'SecTpCode', 'name': '유가증권구분', 'type': 'string', 'length': 1, 'desc': '0@전체, 3@거래소, 4@코스닥, 1@주식(거래소+코스닥)', 'required': True}, {'key': 'LoanIntrstGrdCode', 'name': '대출이자등급코드', 'type': 'string', 'length': 2, 'desc': '00', 'required': True}, {'key': 'LoanTp', 'name': '대출구분', 'type': 'string', 'length': 1, 'desc': '1@예탁증권담보융자, 3@융자, 4@유통대주, 5@자기대주', 'required': True}],
                'type': 'single'
            }
        }
    },
    'CSPBQ00200': {
        'tr_cd': 'CSPBQ00200',
        'title': '현물계좌증거금률별주문가능수량조회',
        'blocks': {
            'CSPBQ00200InBlock1': {
                'fields': [{'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'length': 1, 'desc': '1@매도, 2@매수', 'required': True}, {'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'OrdPrc', 'name': '주문가격', 'type': 'float', 'length': 15.2, 'required': True}],
                'type': 'single'
            }
        }
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
    't1809': {
        'tr_cd': 't1809',
        'title': '신호조회',
        'blocks': {
            't1809InBlock': {
                'fields': [{'key': 'gubun', 'name': '신호구분', 'type': 'string', 'length': 1, 'desc': "'0'", 'required': True}, {'key': 'jmGb', 'name': '종목구분', 'type': 'string', 'length': 1, 'desc': "'0'", 'required': True}, {'key': 'jmcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'cts', 'name': 'NEXTKEY', 'type': 'string', 'length': 30, 'desc': '처음 조회시는 Space 연속 조회시에 이전 조회한 OutBlock의 cts 값으로 설정', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1825': {
        'tr_cd': 't1825',
        'title': '종목Q클릭검색(씽큐스마트)',
        'blocks': {
            't1825InBlock': {
                'fields': [{'key': 'search_cd', 'name': '검색코드', 'type': 'string', 'length': 4, 'desc': 't1826OutBlock의 search_cd 참조', 'required': True}, {'key': 'gubun', 'name': '구분(0:전체1:코스피2:코스닥)', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1826': {
        'tr_cd': 't1826',
        'title': '종목Q클릭검색리스트조회(씽큐스마트)',
        'blocks': {
            't1826InBlock': {
                'fields': [{'key': 'search_gb', 'name': '검색구분(0:핵심검색1:지표검색2:시세동향3:투자자동향)', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1852': {
        'tr_cd': 't1852',
        'title': '파일저장종목 실시간검색',
        'blocks': {
            't1852InBlock': {
                'fields': [{'key': 'flag', 'name': '등록구분', 'type': 'string', 'length': 1, 'desc': 'E : 등록<br/>D : 해지', 'required': True}, {'key': 'sservergb', 'name': '서버구분', 'type': 'string', 'length': 1, 'desc': 'I : 운영<br/>S : 모의투자', 'required': True}, {'key': 'sFileData', 'name': 'sFileData', 'type': 'string', 'length': 26779, 'desc': '대상파일 binaryType 오픈 > base64 incoding > utf8 incoding', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1856': {
        'tr_cd': 't1856',
        'title': '파일저장종목검색',
        'blocks': {
            't1856InBlock': {
                'fields': [{'key': 'sFileData', 'name': 'sFileData', 'type': 'string', 'length': 26779, 'desc': '대상파일 binaryType 오픈 > base64 incoding > utf8 incoding', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1859 ': {
        'tr_cd': 't1859 ',
        'title': '서버저장조건 조건검색',
        'blocks': {
            't1859InBlock': {
                'fields': [{'key': 'query_index', 'name': '서버저장인덱스', 'type': 'string', 'length': 12, 'desc': 't1866  TR에서 조회한 t1866OutBlock1.query_index ', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1860': {
        'tr_cd': 't1860',
        'title': '서버저장조건 실시간검색',
        'blocks': {
            't1860InBlock': {
                'fields': [{'key': 'sSysUserFlag', 'name': '사용자구분', 'type': 'string', 'length': 1, 'desc': "'U' 고정 ", 'required': True}, {'key': 'sFlag', 'name': 'Flag', 'type': 'string', 'length': 1, 'desc': "'E:'등록, 'D':중지", 'required': True}, {'key': 'sAlertNum', 'name': '실시간 검색키', 'type': 'string', 'length': 11, 'desc': "Flag 값 <br/>'D':중지  일떄만 입력  -  등록 요청 시 수신받은  t1860OutBlock.sAlertNum 값", 'required': True}, {'key': 'query_index', 'name': '서버저장인덱스', 'type': 'string', 'length': 12, 'desc': 't1866 TR에서 조회한 t1866OutBlock1.query_index', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1866': {
        'tr_cd': 't1866',
        'title': '서버저장조건 리스트조회',
        'blocks': {
            't1866InBlock': {
                'fields': [{'key': 'user_id', 'name': '로그인ID', 'type': 'string', 'length': 8, 'required': True}, {'key': 'gb', 'name': '조회구분', 'type': 'string', 'length': 1, 'desc': '0 : 그룹+조건리스트 조회<br/>1 : 그룹리스트조회<br/>2 : 그룹명에 속한 조건리스트조회', 'required': True}, {'key': 'group_name', 'name': '연속키', 'type': 'string', 'length': 40, 'desc': '조회구분 2일 경우만 입력', 'required': True}, {'key': 'cont', 'name': '연속여부', 'type': 'string', 'length': 1, 'desc': '연속여부 0, 1(다음데이타 있음)', 'required': True}, {'key': 'cont_key', 'name': '연속키', 'type': 'string', 'length': 40, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1921': {
        'tr_cd': 't1921',
        'title': '신용거래동향',
        'blocks': {
            't1921InBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'gubun', 'name': '융자대주구분', 'type': 'string', 'length': 1, 'desc': '1:융자 2:대주', 'required': True}, {'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'desc': '다음 조회시 사용 OutBlock의 date 필드를 입력함.', 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'desc': '사용안함', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1926': {
        'tr_cd': 't1926',
        'title': '종목별신용정보',
        'blocks': {
            't1926InBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1927': {
        'tr_cd': 't1927',
        'title': '공매도일별추이',
        'blocks': {
            't1927InBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'desc': '다음 조회시 사용. OutBlock의 date 필드 값을 입력함.', 'required': True}, {'key': 'sdate', 'name': '시작일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'edate', 'name': '종료일자', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1941': {
        'tr_cd': 't1941',
        'title': '종목별대차거래일간추이',
        'blocks': {
            't1941InBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'sdate', 'name': '시작일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'edate', 'name': '종료일자', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1959': {
        'tr_cd': 't1959',
        'title': 'LP대상종목정보조회',
        'blocks': {
            't1959InBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1988': {
        'tr_cd': 't1988',
        'title': '기초자산리스트조회',
        'blocks': {
            't1988InBlock': {
                'fields': [{'key': 'mkt_gb', 'name': '시장구분(0:전체1:코스피2:코스닥)', 'type': 'string', 'length': 1, 'desc': '0:전체 1:코스피 2:코스닥', 'required': True}, {'key': 'chk_price', 'name': '가격설정(0:전체1:조건설정)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'from_price', 'name': '가격1', 'type': 'string', 'length': 12, 'required': True}, {'key': 'to_price', 'name': '가격2', 'type': 'string', 'length': 12, 'required': True}, {'key': 'chk_vol', 'name': '거래량설정(0:전체1:조건설정)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'from_vol', 'name': '거래량1', 'type': 'string', 'length': 12, 'required': True}, {'key': 'to_vol', 'name': '거래량2', 'type': 'string', 'length': 12, 'required': True}, {'key': 'chk_rate', 'name': '등락율설정(0:전체1:조건설정)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'from_rate', 'name': '등락율1', 'type': 'float', 'length': 5.2, 'required': True}, {'key': 'to_rate', 'name': '등락율2', 'type': 'float', 'length': 5.2, 'required': True}, {'key': 'chk_amt', 'name': '거래대금설정(0:전체1:조건설정)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'from_amt', 'name': '거래대금1', 'type': 'string', 'length': 12, 'required': True}, {'key': 'to_amt', 'name': '거래대금2', 'type': 'string', 'length': 12, 'required': True}, {'key': 'chk_up', 'name': '양봉설정(0:전체1:조건설정)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'chk_down', 'name': '음봉설정(0:전체1:조건설정)', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    't2203': {
        'tr_cd': 't2203',
        'title': '기간별주가',
        'blocks': {
            't2203InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'futcheck', 'name': '선물최근월물', 'type': 'string', 'length': 1, 'desc': '0:default 1:최근월물만연결', 'required': True}, {'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'desc': '처음 조회시는 Space 연속 조회시에 이전 조회한 OutBlock의 date 값으로 설정', 'required': True}, {'key': 'cts_code', 'name': 'CTS종목코드', 'type': 'string', 'length': 8, 'desc': '처음 조회시는 Space 연속 조회시에 이전 조회한 OutBlock의 cts_code 값으로 설정', 'required': True}, {'key': 'lastdate', 'name': '전종목만기일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cnt', 'name': '조회요청건수', 'type': 'long', 'length': 3, 'required': True}],
                'type': 'single'
            }
        }
    },
    't2421': {
        'tr_cd': 't2421',
        'title': '미결제약정추이',
        'blocks': {
            't2421InBlock': {
                'fields': [{'key': 'focode', 'name': '종목코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'bdgubun', 'name': '분일구분', 'type': 'string', 'length': 1, 'desc': '0:30초 1:분 2:일', 'required': True}, {'key': 'nmin', 'name': 'N분', 'type': 'long', 'length': 3, 'desc': 't2421InBlock.bdgubun 이 1인 경우 N분', 'required': True}, {'key': 'tcgubun', 'name': '당일연결구분', 'type': 'string', 'length': 1, 'desc': '0:전체 1:당일', 'required': True}, {'key': 'cnt', 'name': '조회건수', 'type': 'long', 'length': 4, 'required': True}],
                'type': 'single'
            }
        }
    },
    't3102': {
        'tr_cd': 't3102',
        'title': '뉴스본문',
        'blocks': {
            't3102InBlock': {
                'fields': [{'key': 'sNewsno', 'name': '뉴스번호', 'type': 'string', 'length': 24, 'required': True}],
                'type': 'single'
            }
        }
    },
    't3202': {
        'tr_cd': 't3202',
        'title': '종목별증시일정',
        'blocks': {
            't3202InBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'date', 'name': '조회일자', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't3320': {
        'tr_cd': 't3320',
        'title': 'FNG_요약',
        'blocks': {
            't3320InBlock': {
                'fields': [{'key': 'gicode', 'name': '종목코드', 'type': 'string', 'length': 7, 'required': True}],
                'type': 'single'
            }
        }
    },
    't3341': {
        'tr_cd': 't3341',
        'title': '재무순위종합',
        'blocks': {
            't3341InBlock': {
                'fields': [{'key': 'gubun', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': '0:전체 1:코스피 2:코스닥', 'required': True}, {'key': 'gubun1', 'name': '순위구분(1:매출액증가율2:영업이익증가율\n3:세전계속이익증가율4:부채비율5:유보율\n6:EPS7:BPS8:ROE9:PERa:PBRb:PEG)', 'type': 'string', 'length': 1, 'desc': '1@매출액증가율 2@영업이익증가율 3@세전계속이익증가율 4@부채비율 5@유보율 6@EPS 7@BPS 8@ROE 9@PER             : 오름차순 a@PBR             : 오름차순 b@PEG             : 오름차순', 'required': True}, {'key': 'gubun2', 'name': '대비구분', 'type': 'string', 'length': 1, 'desc': '1 고정', 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'desc': 'idx 첫조회시 space 연속조회시 Outblock의 idx 값 세팅', 'required': True}],
                'type': 'single'
            }
        }
    },
    't3401': {
        'tr_cd': 't3401',
        'title': '투자의견',
        'blocks': {
            't3401InBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 9, 'required': True}, {'key': 'gubun1', 'name': '구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'tradno', 'name': '회원사코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'cts_date', 'name': 'IDXDATE', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't4203': {
        'tr_cd': 't4203',
        'title': '업종차트(종합)',
        'blocks': {
            't4203InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'gubun', 'name': '주기구분(0:틱1:분2:일3:주4:월)', 'type': 'string', 'length': 1, 'desc': '0:틱<br/>1:분<br/>2:일<br/>3:주<br/>4:월', 'required': True}, {'key': 'ncnt', 'name': '틱개수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'qrycnt', 'name': '건수', 'type': 'float', 'length': 4, 'desc': '1 이상 500 이하값만 유효', 'required': True}, {'key': 'tdgb', 'name': '당일구분(0:전체1:당일만)', 'type': 'string', 'length': 1, 'desc': '0:전체<br/>1:당일만', 'required': True}, {'key': 'sdate', 'name': '시작일자', 'type': 'string', 'length': 8, 'desc': '조회구간종료일<br/>Space:기본값', 'required': True}, {'key': 'edate', 'name': '종료일자', 'type': 'string', 'length': 8, 'desc': '처음조회기준일(LE)<br/>처음조회일 경우 이 값 기준으로 조회', 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 cts_date 값으로 설정', 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 10, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 cts_time 값으로 설정', 'required': True}, {'key': 'cts_daygb', 'name': '연속당일구분(0:연속전체1:연속당일만2:연속전일만)', 'type': 'string', 'length': 1, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 cts_daygb 값으로 설정', 'required': True}],
                'type': 'single'
            }
        }
    }
}
