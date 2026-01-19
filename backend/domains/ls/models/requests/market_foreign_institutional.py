# Auto-generated
from typing import Any, Dict, List

MARKET_FOREIGN_INSTITUTIONAL_REQUESTS = {
    't1601': {
        'tr_cd': 't1601',
        'title': '투자자별종합',
        'blocks': {
            't1601InBlock': {
                'fields': [{'key': 'gubun1', 'name': '주식금액수량구분1', 'type': 'string', 'length': 1, 'desc': '1:수량<br/>2:금액', 'required': True}, {'key': 'gubun2', 'name': '옵션금액수량구분2', 'type': 'string', 'length': 1, 'desc': '1:수량<br/>2:금액', 'required': True}, {'key': 'gubun3', 'name': '금액단위', 'type': 'string', 'length': 1, 'desc': '사용안함', 'required': True}, {'key': 'gubun4', 'name': '선물금액수량구분4', 'type': 'string', 'length': 1, 'desc': '1:수량<br/>2:금액', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리<br/>', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1602': {
        'tr_cd': 't1602',
        'title': '시간대별투자자매매추이',
        'blocks': {
            't1602InBlock': {
                'fields': [{'key': 'market', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': '1@코스피<br/>2@KP200<br/>3@코스닥<br/>4@선물<br/>5@콜옵션<br/>6@풋옵션<br/>7@ELW<br/>8@ETF', 'required': True}, {'key': 'upcode', 'name': '업종코드', 'type': 'string', 'length': 3, 'desc': '001:코스피<br/>101:KP200<br/>301:코스닥<br/>900:선  물<br/>700:콜옵션<br/>800:풋옵션<br/>550:ELW<br/>560:ETF', 'required': True}, {'key': 'gubun1', 'name': '수량구분', 'type': 'string', 'length': 1, 'desc': '1:수량<br/>2:금액', 'required': True}, {'key': 'gubun2', 'name': '전일분구분', 'type': 'string', 'length': 1, 'desc': '0:금일<br/>1:전일', 'required': True}, {'key': 'cts_time', 'name': 'CTSTIME', 'type': 'string', 'length': 8, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 cts_time 값으로 설정', 'required': True}, {'key': 'cts_idx', 'name': 'CTSIDX', 'type': 'float', 'length': 4, 'desc': '사용안함', 'required': True}, {'key': 'cnt', 'name': '조회건수', 'type': 'long', 'length': 4, 'required': True}, {'key': 'gubun3', 'name': '직전대비구분(C:직전대비)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리<br/>', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1603': {
        'tr_cd': 't1603',
        'title': '시간대별투자자매매추이상세',
        'blocks': {
            't1603InBlock': {
                'fields': [{'key': 'market', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': '1:코스피<br/>2:코스닥<br/>3:선물<br/>4:콜옵션<br/>5:풋옵션<br/>6:ELW<br/>7:ETF', 'required': True}, {'key': 'gubun1', 'name': '투자자구분', 'type': 'string', 'length': 1, 'desc': '1:개인<br/>2:외인<br/>3:기관계<br/>4:증권<br/>5:투신<br/>6:은행<br/>7:보험<br/>8:종금<br/>9:기금<br/>A:국가<br/>B:기타<br/>C:사모펀드', 'required': True}, {'key': 'gubun2', 'name': '전일분구분', 'type': 'string', 'length': 1, 'desc': '0:당일<br/>1:전일', 'required': True}, {'key': 'cts_time', 'name': 'CTSTIME', 'type': 'string', 'length': 8, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 cts_time 값으로 설정', 'required': True}, {'key': 'cts_idx', 'name': 'CTSIDX', 'type': 'float', 'length': 4, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 cts_idx 값으로 설정', 'required': True}, {'key': 'cnt', 'name': '조회건수', 'type': 'long', 'length': 3, 'desc': '020', 'required': True}, {'key': 'upcode', 'name': '업종코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1615': {
        'tr_cd': 't1615',
        'title': '투자자매매종합1',
        'blocks': {
            't1615InBlock': {
                'fields': [{'key': 'gubun1', 'name': '주식구분', 'type': 'string', 'length': 1, 'desc': '1:수량<br/>2:금액', 'required': True}, {'key': 'gubun2', 'name': '옵션구분', 'type': 'string', 'length': 1, 'desc': '1:수량<br/>2:금액', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1617': {
        'tr_cd': 't1617',
        'title': '투자자매매종합2',
        'blocks': {
            't1617InBlock': {
                'fields': [{'key': 'gubun1', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': '1:코스피<br/>2:코스닥<br/>3:선물<br/>4:콜옵션<br/>5:풋옵션<br/>6:주식선물<br/>7:변동성<br/>8:M선물<br/>9:M콜옵션<br/>0:M풋옵션', 'required': True}, {'key': 'gubun2', 'name': '수량금액구분(1:수량2:금액)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'gubun3', 'name': '일자구분(1:시간대별2:일별)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'cts_date', 'name': 'CTSDATE(연속키값-일자)', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': 'CTSTIME(연속키값-시간)', 'type': 'string', 'length': 8, 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1621': {
        'tr_cd': 't1621',
        'title': '업종별분별투자자매매동향(챠트용)',
        'blocks': {
            't1621InBlock': {
                'fields': [{'key': 'upcode', 'name': '업종코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'nmin', 'name': 'N분', 'type': 'long', 'length': 2, 'required': True}, {'key': 'cnt', 'name': '조회건수', 'type': 'long', 'length': 3, 'required': True}, {'key': 'bgubun', 'name': '전일분', 'type': 'string', 'length': 1, 'desc': '0:당일<br/>1:전일', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1631': {
        'tr_cd': 't1631',
        'title': '프로그램매매종합조회',
        'blocks': {
            't1631InBlock': {
                'fields': [{'key': 'gubun', 'name': '구분', 'type': 'string', 'length': 1, 'desc': '1:거래소<br/>2:코스닥', 'required': True}, {'key': 'dgubun', 'name': '일자구분', 'type': 'string', 'length': 1, 'desc': '1:당일조회<br/>2:기간조회', 'required': True}, {'key': 'sdate', 'name': '시작일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'edate', 'name': '종료일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1632': {
        'tr_cd': 't1632',
        'title': '시간대별프로그램매매추이',
        'blocks': {
            't1632InBlock': {
                'fields': [{'key': 'gubun', 'name': '구분', 'type': 'string', 'length': 1, 'desc': '0@거래소<br/>1@코스닥', 'required': True}, {'key': 'gubun1', 'name': '금액수량구분', 'type': 'string', 'length': 1, 'desc': '0:금액<br/>1:수량', 'required': True}, {'key': 'gubun2', 'name': '직전대비증감', 'type': 'string', 'length': 1, 'desc': '1:직전대비증감', 'required': True}, {'key': 'gubun3', 'name': '전일구분', 'type': 'string', 'length': 1, 'desc': '1:전일분', 'required': True}, {'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 date 값으로 설정', 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 time 값으로 설정', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1633': {
        'tr_cd': 't1633',
        'title': '기간별프로그램매매추이',
        'blocks': {
            't1633InBlock': {
                'fields': [{'key': 'gubun', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': '0@거래소<br/>1@코스닥', 'required': True}, {'key': 'gubun1', 'name': '금액수량구분', 'type': 'string', 'length': 1, 'desc': '0:금액<br/>1:수량', 'required': True}, {'key': 'gubun2', 'name': '수치누적구분', 'type': 'string', 'length': 1, 'desc': '0@수치<br/>1@누적', 'required': True}, {'key': 'gubun3', 'name': '일주월구분', 'type': 'string', 'length': 1, 'desc': '1@일<br/>2@주<br/>3@월', 'required': True}, {'key': 'fdate', 'name': 'from일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'tdate', 'name': 'to일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'gubun4', 'name': '직전대비증감구분', 'type': 'string', 'length': 1, 'desc': '0:Default<br/>1:직전대비증감', 'required': True}, {'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 date 값으로 설정', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1636': {
        'tr_cd': 't1636',
        'title': '종목별프로그램매매동향',
        'blocks': {
            't1636InBlock': {
                'fields': [{'key': 'gubun', 'name': '구분', 'type': 'string', 'length': 1, 'desc': '0:코스피<br/>1:코스닥', 'required': True}, {'key': 'gubun1', 'name': '금액수량구분', 'type': 'string', 'length': 1, 'desc': '0:수량<br/>1:금액', 'required': True}, {'key': 'gubun2', 'name': '정렬기준', 'type': 'string', 'length': 1, 'desc': '0:시가총액비중<br/>1:순매수상위<br/>2:순매도상위<br/>3:매도상위<br/>4:매수상위', 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'cts_idx', 'name': 'IDXCTS', 'type': 'float', 'length': 4, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 cts_idx 값으로 설정', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1637': {
        'tr_cd': 't1637',
        'title': '종목별프로그램매매추이',
        'blocks': {
            't1637InBlock': {
                'fields': [{'key': 'gubun1', 'name': '수량금액구분(0:수량1:금액)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'gubun2', 'name': '시간일별구분(0:시간1:일자)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'desc': '일별 연속 조회시에 이전 조회한 OutBlock1의 마지막 Row의 date 값으로 설정', 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'desc': '시간별 연속 조회시에 이전 조회한 OutBlock1의 마지막 Row의 time 값으로 설정', 'required': True}, {'key': 'cts_idx', 'name': 'IDXCTS(9999:차트)', 'type': 'float', 'length': 4, 'desc': '차트 조회시에만 9999로 입력', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1638': {
        'tr_cd': 't1638',
        'title': '종목별잔량/사전공시',
        'blocks': {
            't1638InBlock': {
                'fields': [{'key': 'gubun1', 'name': '구분', 'type': 'string', 'length': 1, 'desc': '1 : 코스피<br/>2 : 코스닥', 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'gubun2', 'name': '정렬', 'type': 'string', 'length': 1, 'desc': '1 : 시가총액비중<br/>2 : 순매수잔량상위<br/>3 : 순매수잔량하위<br/>4 : 매수잔량<br/>5 : 매수공시수량<br/>6 : 매도잔량<br/>7 : 매도공시수량', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1640': {
        'tr_cd': 't1640',
        'title': '프로그램매매종합조회(미니)',
        'blocks': {
            't1640InBlock': {
                'fields': [{'key': 'gubun', 'name': '구분', 'type': 'string', 'length': 2, 'desc': '11@거래소전체<br/>12@거래소차익<br/>13@거래소비차익<br/>21@코스닥전체<br/>22@코스닥차익<br/>23@코스닥비차익', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1662': {
        'tr_cd': 't1662',
        'title': '시간대별프로그램매매추이(차트)',
        'blocks': {
            't1662InBlock': {
                'fields': [{'key': 'gubun', 'name': '구분', 'type': 'string', 'length': 1, 'desc': '0@코스피<br/>1@코스닥', 'required': True}, {'key': 'gubun1', 'name': '금액수량구분', 'type': 'string', 'length': 1, 'desc': '0:금액<br/>1:수량', 'required': True}, {'key': 'gubun3', 'name': '전일구분', 'type': 'string', 'length': 1, 'desc': '0:당일<br/>1:전일', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1664': {
        'tr_cd': 't1664',
        'title': '투자자매매종합(챠트)',
        'blocks': {
            't1664InBlock': {
                'fields': [{'key': 'mgubun', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': '1@코스피<br/>2@코스닥<br/>3@선  물<br/>4@콜옵션<br/>5@풋옵션', 'required': True}, {'key': 'vagubun', 'name': '금액수량구분', 'type': 'string', 'length': 1, 'desc': '1:수량<br/>2:금액', 'required': True}, {'key': 'bdgubun', 'name': '시간일별구분', 'type': 'string', 'length': 1, 'desc': '1:시간별<br/>2:일별', 'required': True}, {'key': 'cnt', 'name': '조회건수', 'type': 'long', 'length': 3, 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1665': {
        'tr_cd': 't1665',
        'title': '기간별투자자매매추이(차트)',
        'blocks': {
            't1665InBlock': {
                'fields': [{'key': 'market', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': '1@코스피<br/>2@KP200<br/>3@코스닥<br/>4@선물<br/>5@풋옵션<br/>6@콜옵션', 'required': True}, {'key': 'upcode', 'name': '업종코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'gubun2', 'name': '수치구분(1:수치2:누적)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'gubun3', 'name': '단위구분(1:일2:주3:월)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'from_date', 'name': '시작날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'to_date', 'name': '종료날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1702': {
        'tr_cd': 't1702',
        'title': '외인기관종목별동향',
        'blocks': {
            't1702InBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'fromdt', 'name': '시작일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'todt', 'name': '종료일자', 'type': 'string', 'length': 8, 'desc': 't1702OutBlock1.date <= t1702InBlock.todt', 'required': True}, {'key': 'volvalgb', 'name': '금액수량구분(0:금액1:수량2:단가)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'msmdgb', 'name': '매수매도구분(0:순매수1:매수2:매도)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'gubun', 'name': '누적구분(0:일간1:누적)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1716': {
        'tr_cd': 't1716',
        'title': '외인기관종목별동향',
        'blocks': {
            't1716InBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'gubun', 'name': '구분(0:일간순매수1:기간누적순매수)', 'type': 'string', 'length': 1, 'desc': '0:일간순매수<br/>1:기간내누적순매수', 'required': True}, {'key': 'fromdt', 'name': '시작일자', 'type': 'string', 'length': 8, 'desc': 'YYYYMMDD', 'required': True}, {'key': 'todt', 'name': '종료일자', 'type': 'string', 'length': 8, 'desc': 'YYYYMMDD', 'required': True}, {'key': 'prapp', 'name': 'PR감산적용율', 'type': 'float', 'length': 3, 'desc': '프로그램매매 감산 적용율 - %단위', 'required': True}, {'key': 'prgubun', 'name': 'PR적용구분(0:적용안함1:적용)', 'type': 'string', 'length': 1, 'desc': '0:미적용<br/>1:적용', 'required': True}, {'key': 'orggubun', 'name': '기관적용', 'type': 'string', 'length': 1, 'desc': '0:미적용<br/>1:적용', 'required': True}, {'key': 'frggubun', 'name': '외인적용', 'type': 'string', 'length': 1, 'desc': '0:미적용<br/>1:적용', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1717': {
        'tr_cd': 't1717',
        'title': '외인기관종목별동향',
        'blocks': {
            't1717InBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'gubun', 'name': '구분(0:일간순매수1:기간누적순매수)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'fromdt', 'name': '시작일자(일간조회일경우는space)', 'type': 'string', 'length': 8, 'desc': 'OutBlock.date >= fromdt', 'required': True}, {'key': 'todt', 'name': '종료일자', 'type': 'string', 'length': 8, 'desc': 'OutBlock.date <= todt', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1752': {
        'tr_cd': 't1752',
        'title': '종목별상위회원사',
        'blocks': {
            't1752InBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'traddate1', 'name': '조회날짜1', 'type': 'string', 'length': 8, 'desc': '기간 조회시 시작일(YYYYMMDD)', 'required': True}, {'key': 'traddate2', 'name': '조회날짜2', 'type': 'string', 'length': 8, 'desc': '기간 조회시 종료일(YYYYMMDD)', 'required': True}, {'key': 'fwgubun1', 'name': '외국계구분', 'type': 'string', 'length': 1, 'desc': '0 : 전체<br/>1 : 외국계 회원사만 조회', 'required': True}, {'key': 'cts_idx', 'name': 'CTSIDX', 'type': 'float', 'length': 4, 'desc': 'OutBlock 동일필드 연속조회시 입력', 'required': True}, {'key': 'exchgubun', 'name': '거래소구분코드', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1764': {
        'tr_cd': 't1764',
        'title': '회원사리스트',
        'blocks': {
            't1764InBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'gubun1', 'name': '구분1', 'type': 'string', 'length': 1, 'desc': '0 or 1 : 전회원사조회 0,1 이외의 값 입력시 InBlock.shcode 종목으로 거래가 있는 회원사만 조회됨', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1771': {
        'tr_cd': 't1771',
        'title': '종목별회원사추이',
        'blocks': {
            't1771InBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'tradno', 'name': '거래원코드', 'type': 'string', 'length': 3, 'desc': '거래원코드<br/>t1764 를 조회한 후 t1764OutBlock 의 tradno 의 값을 사용', 'required': True}, {'key': 'gubun1', 'name': '구분1', 'type': 'string', 'length': 1, 'desc': '0 : 시간별<br/>1 : 일별', 'required': True}, {'key': 'traddate1', 'name': '거래원날짜1', 'type': 'string', 'length': 8, 'desc': '일별 조회시 사용<br/>OutBlock1.traddate >= InBlock.traddate1', 'required': True}, {'key': 'traddate2', 'name': '거래원날짜2', 'type': 'string', 'length': 8, 'desc': '일별 조회시 사용<br/>OutBlock1.traddate <= InBlock.traddate2', 'required': True}, {'key': 'cts_idx', 'name': 'CTSIDX', 'type': 'float', 'length': 4, 'desc': '처음 조회시 Space 입력<br/>다음 조회시 OutBlock의 cts_idx 값을 입력', 'required': True}, {'key': 'cnt', 'name': '요청건수', 'type': 'long', 'length': 3, 'required': True}, {'key': 'exchgubun', 'name': '거래소구분', 'type': 'string', 'length': 1, 'desc': 'K: KRX<br/>N: NXT<br/>U:통합<br/>그외 입력값은 KRX로 처리', 'required': True}],
                'type': 'single'
            }
        }
    }
}
