# Auto-generated
from typing import Any, Dict, List

MARKET_DERIVATIVES_QUERY_REQUESTS = {
    't0434': {
        'tr_cd': 't0434',
        'title': '선물/옵션체결/미체결',
        'blocks': {
            't0434InBlock': {
                'fields': [{'key': 'expcode', 'name': '종목번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'chegb', 'name': '체결구분', 'type': 'string', 'length': 1, 'desc': '0;전체<br/>1:체결<br/>2:미체결', 'required': True}, {'key': 'sortgb', 'name': '정렬순서', 'type': 'string', 'length': 1, 'desc': '1:주문번호 역순<br/>2:주문번호 순<br/>', 'required': True}, {'key': 'cts_ordno', 'name': 'CTS_주문번호', 'type': 'string', 'length': 7, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 cts_ordno 값으로 설정', 'required': True}],
                'type': 'single'
            }
        }
    },
    't0441': {
        'tr_cd': 't0441',
        'title': '선물/옵션잔고평가(이동평균)',
        'blocks': {
            't0441InBlock': {
                'fields': [{'key': 'cts_expcode', 'name': 'CTS_종목번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_medocd', 'name': 'CTS_매매구분', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    't2101': {
        'tr_cd': 't2101',
        'title': '선물/옵션현재가(시세)조회',
        'blocks': {
            't2101InBlock': {
                'fields': [{'key': 'focode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't2105': {
        'tr_cd': 't2105',
        'title': '선물/옵션현재가호가조회',
        'blocks': {
            't2105InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't2106': {
        'tr_cd': 't2106',
        'title': '선물/옵션현재가시세메모',
        'blocks': {
            't2106InBlock': {
                'fields': [{'key': 'code', 'name': '종목코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'nrec', 'name': '건수', 'type': 'string', 'length': 2, 'desc': 't2106InBlock1 의 개수', 'required': True}],
                'type': 'single'
            },
            't2106InBlock1': {
                'fields': [{'key': 'indx', 'name': '인덱스', 'type': 'string', 'length': 1, 'desc': 't2106InBlock1 의 Occurs 순서(0부터 시작)', 'required': True}, {'key': 'gubn', 'name': '조건구분', 'type': 'string', 'length': 1, 'desc': '1:시세 2:최고저가 3:Pivot 4:이동평균선', 'required': True}, {'key': 'dat1', 'name': '데이타1', 'type': 'string', 'length': 1, 'desc': '1:시가 2:고가 3:저가 4:가중평균가', 'required': True}, {'key': 'dat2', 'name': '데이타2', 'type': 'string', 'length': 8, 'desc': '1:당일 2:전일', 'required': True}],
                'type': 'array'
            }
        }
    },
    't2201': {
        'tr_cd': 't2201',
        'title': '선물옵션시간대별체결조회',
        'blocks': {
            't2201InBlock': {
                'fields': [{'key': 'focode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cvolume', 'name': '특이거래량', 'type': 'float', 'length': 12, 'desc': '체결수량 >= cvolume', 'required': True}, {'key': 'stime', 'name': '시작시간', 'type': 'string', 'length': 4, 'desc': '체결시간 >= stime(hhmm) ', 'required': True}, {'key': 'etime', 'name': '종료시간', 'type': 'string', 'length': 4, 'desc': '체결시간 <= etime(hhmm) ', 'required': True}, {'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 10, 'desc': '처음 조회시는 Space 연속 조회시에 이전 조회한 OutBlock의 cts_time 값으로 설정', 'required': True}],
                'type': 'single'
            }
        }
    },
    't2209': {
        'tr_cd': 't2209',
        'title': '선물옵션틱분별체결조회차트',
        'blocks': {
            't2209InBlock': {
                'fields': [{'key': 'focode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cgubun', 'name': '챠트구분', 'type': 'string', 'length': 1, 'desc': 'T:틱차트<br/>B:분차트', 'required': True}, {'key': 'bgubun', 'name': '분구분', 'type': 'long', 'length': 3, 'desc': "차트구분이 'B'일때만 체크<br/>0: 30초<br/>0초과 : n분", 'required': True}, {'key': 'cnt', 'name': '조회건수', 'type': 'long', 'length': 3, 'required': True}],
                'type': 'single'
            }
        }
    },
    't2210': {
        'tr_cd': 't2210',
        'title': '선물옵션시간대별체결조회(단일출력용)',
        'blocks': {
            't2210InBlock': {
                'fields': [{'key': 'focode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cvolume', 'name': '특이거래량', 'type': 'float', 'length': 12, 'desc': '체결수량 >= cvolume', 'required': True}, {'key': 'stime', 'name': '시작시간', 'type': 'string', 'length': 4, 'desc': '체결시간 >= stime(hhmm)', 'required': True}, {'key': 'etime', 'name': '종료시간', 'type': 'string', 'length': 4, 'desc': '체결시간 <= etime(hhmm)', 'required': True}],
                'type': 'single'
            }
        }
    },
    't2301': {
        'tr_cd': 't2301',
        'title': '옵션전광판',
        'blocks': {
            't2301InBlock': {
                'fields': [{'key': 'yyyymm', 'name': '월물', 'type': 'string', 'length': 6, 'desc': "ex) 미니,정규 : '200604'     위클리 : 'W1    '", 'required': True}, {'key': 'gubun', 'name': '미니구분(M:미니G:정규)', 'type': 'string', 'length': 1, 'desc': 'M: 미니 G: 정규 W: 위클리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't2405': {
        'tr_cd': 't2405',
        'title': '선물옵션호가잔량비율챠트',
        'blocks': {
            't2405InBlock': {
                'fields': [{'key': 'focode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'bgubun', 'name': '분구분', 'type': 'string', 'length': 1, 'desc': '0:30초 1:분', 'required': True}, {'key': 'nmin', 'name': 'N분', 'type': 'long', 'length': 2, 'desc': 'bgubun = 1 인 경우 N분 입력값', 'required': True}, {'key': 'etime', 'name': '종료시간', 'type': 'string', 'length': 4, 'desc': 'etime 이전 시간대를 조회함', 'required': True}, {'key': 'hgubun', 'name': '호가구분', 'type': 'string', 'length': 1, 'desc': '0@총 호가잔량 1@1차 호가잔량 2@2차 호가잔량 3@3차 호가잔량 4@4차 호가잔량 5@5차 호가잔량', 'required': True}, {'key': 'cnt', 'name': '조회건수', 'type': 'long', 'length': 3, 'required': True}, {'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 6, 'desc': '처음 조회시는 Space 연속 조회시에 이전 조회한 OutBlock의 cts_time 값으로 설정', 'required': True}],
                'type': 'single'
            }
        }
    },
    't2541': {
        'tr_cd': 't2541',
        'title': '상품선물투자자매매동향(실시간)',
        'blocks': {
            't2541InBlock': {
                'fields': [{'key': 'eitem', 'name': '상품ID', 'type': 'string', 'length': 2, 'desc': '01@KTB 02@5TB 03@LKTB 04@USD 05@JPY 06@EUR 07@GOLD 08@LH 09@MGD', 'required': True}, {'key': 'market', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': '0@선물 1@콜 2@풋', 'required': True}, {'key': 'upcode', 'name': '업종코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'gubun1', 'name': '수량구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'gubun2', 'name': '전일분구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'cts_time', 'name': 'CTSTIME', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_idx', 'name': 'CTSIDX', 'type': 'float', 'length': 4, 'required': True}, {'key': 'cnt', 'name': '조회건수', 'type': 'long', 'length': 4, 'required': True}],
                'type': 'single'
            }
        }
    },
    't2545': {
        'tr_cd': 't2545',
        'title': '상품선물투자자매매동향(챠트용)',
        'blocks': {
            't2545InBlock': {
                'fields': [{'key': 'eitem', 'name': '상품ID', 'type': 'string', 'length': 2, 'desc': '01@KTB 02@5TB 03@LKTB 04@USD 05@JPY 06@EUR 07@GOLD 08@LH 09@MGD', 'required': True}, {'key': 'sgubun', 'name': '시장구분', 'type': 'string', 'length': 1, 'desc': '0@선물 1@콜 2@풋', 'required': True}, {'key': 'upcode', 'name': '업종코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'nmin', 'name': 'N분', 'type': 'long', 'length': 2, 'required': True}, {'key': 'cnt', 'name': '조회건수', 'type': 'long', 'length': 3, 'required': True}, {'key': 'bgubun', 'name': '전일분', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8401': {
        'tr_cd': 't8401',
        'title': '주식선물마스터조회(API용)',
        'blocks': {
            't8401InBlock': {
                'fields': [{'key': 'dummy', 'name': 'Dummy', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8402': {
        'tr_cd': 't8402',
        'title': '주식선물현재가조회(API용)',
        'blocks': {
            't8402InBlock': {
                'fields': [{'key': 'focode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8403': {
        'tr_cd': 't8403',
        'title': '주식선물호가조회(API용)',
        'blocks': {
            't8403InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8404': {
        'tr_cd': 't8404',
        'title': '주식선물시간대별체결조회(API용)',
        'blocks': {
            't8404InBlock': {
                'fields': [{'key': 'focode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cvolume', 'name': '특이거래량', 'type': 'float', 'length': 12, 'desc': '거래량 > 특이거래량', 'required': True}, {'key': 'stime', 'name': '시작시간', 'type': 'string', 'length': 4, 'desc': '장시작시간 이후', 'required': True}, {'key': 'etime', 'name': '종료시간', 'type': 'string', 'length': 4, 'desc': '장종료시간 이전', 'required': True}, {'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 10, 'desc': '처음 조회시는 Space 연속 조회시에 이전 조회한 OutBlock의 cts_time 값으로 설정', 'required': True}],
                'type': 'single'
            }
        }
    },
    't8405': {
        'tr_cd': 't8405',
        'title': '주식선물기간별주가(API용)',
        'blocks': {
            't8405InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'futcheck', 'name': '선물최근월물', 'type': 'string', 'length': 1, 'desc': '0:default 1:최근월물만연결', 'required': True}, {'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'desc': '처음 조회시는 Space 연속 조회시에 이전 조회한 OutBlock의 date 값으로 설정', 'required': True}, {'key': 'cts_code', 'name': 'CTS종목코드', 'type': 'string', 'length': 8, 'desc': '처음 조회시는 Space 연속 조회시에 이전 조회한 OutBlock의 cts_code 값으로 설정', 'required': True}, {'key': 'lastdate', 'name': '전종목만기일', 'type': 'string', 'length': 8, 'desc': '처음 조회시는 Space 연속 조회시에 이전 조회한 OutBlock의 lastdate 값으로 설정', 'required': True}, {'key': 'cnt', 'name': '조회요청건수', 'type': 'long', 'length': 3, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8406': {
        'tr_cd': 't8406',
        'title': '주식선물틱분별체결조회(API용)',
        'blocks': {
            't8406InBlock': {
                'fields': [{'key': 'focode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cgubun', 'name': '챠트구분', 'type': 'string', 'length': 1, 'desc': 'T:틱차트 B:분차트', 'required': True}, {'key': 'bgubun', 'name': '분구분', 'type': 'long', 'length': 3, 'desc': "차트구분이 'B'일때만 체크 0: 30초 0초과 : n분", 'required': True}, {'key': 'cnt', 'name': '조회건수', 'type': 'long', 'length': 3, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8414': {
        'tr_cd': 't8414',
        'title': '선물옵션차트(틱/n틱)',
        'blocks': {
            't8414InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'ncnt', 'name': '단위(n틱)', 'type': 'float', 'length': 4, 'required': True}, {'key': 'qrycnt', 'name': '요청건수(최대-압축:2000비압축:500)', 'type': 'float', 'length': 4, 'desc': '요청건수  압축모듈인 경우 최대 2000건까지 조회가능. 비압축인 경우 최대 500건까지 조회가능', 'required': True}, {'key': 'nday', 'name': '조회영업일수(0:미사용1>=사용)', 'type': 'string', 'length': 1, 'desc': '0:미사용', 'required': True}, {'key': 'sdate', 'name': '시작일자', 'type': 'string', 'length': 8, 'desc': '기본값 : Space (edate(필수입력) 기준으로 qrycnt 만큼 조회)  조회구간을 설정하여 필터링 하고 싶은 경우 입력', 'required': True}, {'key': 'stime', 'name': '시작시간(현재미사용)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'edate', 'name': '종료일자', 'type': 'string', 'length': 8, 'desc': '처음조회기준일(LE) 처음조회일 경우 이 값 기준으로 조회 ("99999999" 혹은 \'당일\')', 'required': True}, {'key': 'etime', 'name': '종료시간(현재미사용)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'desc': '처음 조회시는 Space 연속 조회시에 이전 조회한 OutBlock의 cts_date 값으로 설정', 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 10, 'desc': 'N:비압축', 'required': True}, {'key': 'comp_yn', 'name': '압축여부(Y:압축N:비압축)', 'type': 'string', 'length': 1, 'desc': 'N:비압축 모듈 Y: 압 축 모듈', 'required': True}],
                'type': 'single'
            }
        }
    },
    't8415': {
        'tr_cd': 't8415',
        'title': '선물/옵션차트(N분)',
        'blocks': {
            't8415InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'ncnt', 'name': '단위(n분)', 'type': 'float', 'length': 4, 'desc': '0:30초<br/>1: 1분<br/>2: 2분<br/>.....<br/>n: n분', 'required': True}, {'key': 'qrycnt', 'name': '요청건수(최대-압축:2000비압축:500)', 'type': 'float', 'length': 4, 'desc': '요청건수<br/><br/>압축모듈인 경우 최대 2000건까지 조회가능.<br/>비압축인 경우 최대 500건까지 조회가능', 'required': True}, {'key': 'nday', 'name': '조회영업일수(0:미사용1>=사용)', 'type': 'string', 'length': 1, 'desc': '0:미사용', 'required': True}, {'key': 'sdate', 'name': '시작일자', 'type': 'string', 'length': 8, 'desc': '기본값 : Space<br/>(edate(필수입력) 기준으로 qrycnt 만큼 조회)<br/><br/>조회구간을 설정하여 필터링 하고 싶은 경우 입력', 'required': True}, {'key': 'stime', 'name': '시작시간(현재미사용)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'edate', 'name': '종료일자', 'type': 'string', 'length': 8, 'desc': '처음조회기준일(LE)<br/>처음조회일 경우 이 값 기준으로 조회<br/>("99999999" 혹은 \'당일\')', 'required': True}, {'key': 'etime', 'name': '종료시간(현재미사용)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 cts_date 값으로 설정', 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'comp_yn', 'name': '압축여부(Y:압축N:비압축)', 'type': 'string', 'length': 1, 'desc': 'N:비압축 모듈<br/>Y: 압 축 모듈', 'required': True}],
                'type': 'single'
            }
        }
    },
    't8416': {
        'tr_cd': 't8416',
        'title': '선물/옵션차트(일주월)',
        'blocks': {
            't8416InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'gubun', 'name': '주기구분(2:일3:주4:월)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'qrycnt', 'name': '요청건수(최대-압축:2000비압축:500)', 'type': 'float', 'length': 4, 'desc': '요청건수<br/><br/>압축모듈인 경우 최대 2000건까지 조회가능.<br/>비압축인 경우 최대 500건까지 조회가능', 'required': True}, {'key': 'sdate', 'name': '시작일자', 'type': 'string', 'length': 8, 'desc': '기본값 : Space<br/>(edate(필수입력) 기준으로 qrycnt 만큼 조회)<br/><br/>조회구간을 설정하여 필터링 하고 싶은 경우 입력', 'required': True}, {'key': 'edate', 'name': '종료일자', 'type': 'string', 'length': 8, 'desc': '처음조회기준일(LE)<br/>처음조회일 경우 이 값 기준으로 조회<br/>("99999999" 혹은 \'당일\')', 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'desc': '처음 조회시는 Space<br/>연속 조회시에 이전 조회한 OutBlock의 cts_date 값으로 설정', 'required': True}, {'key': 'comp_yn', 'name': '압축여부(Y:압축N:비압축)', 'type': 'string', 'length': 1, 'desc': 'N:비압축 모듈<br/>Y: 압 축 모듈', 'required': True}],
                'type': 'single'
            }
        }
    },
    't8426': {
        'tr_cd': 't8426',
        'title': '상품선물마스터조회(API용)',
        'blocks': {
            't8426InBlock': {
                'fields': [{'key': 'dummy', 'name': 'Dummy', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8432': {
        'tr_cd': 't8432',
        'title': '지수선물마스터조회API용',
        'blocks': {
            't8432InBlock': {
                'fields': [{'key': 'gubun', 'name': '구분', 'type': 'string', 'length': 1, 'desc': 'V:변동성지수선물 S:섹터지수선물 그 이외의 값은 코스피200지수선물', 'required': True}],
                'type': 'single'
            }
        }
    },
    't8433': {
        'tr_cd': 't8433',
        'title': '지수옵션마스터조회API용',
        'blocks': {
            't8433InBlock': {
                'fields': [{'key': 'dummy', 'name': 'Dummy', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8434': {
        'tr_cd': 't8434',
        'title': '선물/옵션멀티현재가조회',
        'blocks': {
            't8434InBlock': {
                'fields': [{'key': 'qrycnt', 'name': '건수', 'type': 'float', 'length': 3, 'desc': '최대50개까지', 'required': True}, {'key': 'focode', 'name': '단축코드', 'type': 'string', 'length': 400, 'desc': '구분자 없이 종목코드를 붙여서 입력', 'required': True}],
                'type': 'single'
            }
        }
    },
    't8435': {
        'tr_cd': 't8435',
        'title': '파생종목마스터조회API용',
        'blocks': {
            't8435InBlock': {
                'fields': [{'key': 'gubun', 'name': '구분(MF/MO)', 'type': 'string', 'length': 2, 'desc': 'MF : 미니선물<br/>MO : 미니옵션<br/>WK : 코스피200위클리옵션<br/>SF : 코스닥150선물<br/>QW : 코스닥150위클리옵션', 'required': True}],
                'type': 'single'
            }
        }
    },
    't8455': {
        'tr_cd': 't8455',
        'title': 'KRX야간파생 마스터조회(API용)',
        'blocks': {
            't8455InBlock': {
                'fields': [{'key': 'gubun', 'name': '구분(NF/NC/NM/NO)', 'type': 'string', 'length': 2, 'desc': '- 선물 gubun<br/>NFU : KOSPI200선물<br/>NMF : 미니선물<br/>NQF : 코스닥150선물<br/>NCF : 상품선물<br/>- 옵션 gubun<br/>NOP : KOSPI200옵션<br/>NMO : 미니옵션<br/>NQO : 코스닥150옵션<br/>NWO : 위클리옵션', 'required': True}],
                'type': 'single'
            }
        }
    },
    't8456': {
        'tr_cd': 't8456',
        'title': 'KRX야간파생 시세조회(API용)',
        'blocks': {
            't8456InBlock': {
                'fields': [{'key': 'focode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8457': {
        'tr_cd': 't8457',
        'title': 'KRX야간파생 호가조회(API용)',
        'blocks': {
            't8457InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8458': {
        'tr_cd': 't8458',
        'title': 'KRX야간파생 시간대별체결(API용)',
        'blocks': {
            't8458InBlock': {
                'fields': [{'key': 'focode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cvolume', 'name': '특이거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'stime', 'name': '시작시간', 'type': 'string', 'length': 4, 'required': True}, {'key': 'etime', 'name': '종료시간', 'type': 'string', 'length': 4, 'required': True}, {'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8459': {
        'tr_cd': 't8459',
        'title': 'KRX야간파생 기간별주가(API용)',
        'blocks': {
            't8459InBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'futcheck', 'name': '선물최근월물', 'type': 'string', 'length': 1, 'required': True}, {'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_code', 'name': 'CTS종목코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'lastdate', 'name': '전종목만기일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cnt', 'name': '조회요청건수', 'type': 'long', 'length': 3, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8460': {
        'tr_cd': 't8460',
        'title': 'KRX야간파생 옵션 전광판',
        'blocks': {
            't8460InBlock': {
                'fields': [{'key': 'yyyymm', 'name': '월물(혹은주물WN)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'gubun', 'name': '구분(G:원지수W:위클리)', 'type': 'string', 'length': 1, 'desc': 'M:미니<br/>G:원지수<br/>Q:코스닥<br/>W:위클리', 'required': True}],
                'type': 'single'
            }
        }
    },
    't8461': {
        'tr_cd': 't8461',
        'title': 'KRX야간파생 틱분별조회(API용)',
        'blocks': {
            't8461InBlock': {
                'fields': [{'key': 'focode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cgubun', 'name': '챠트구분', 'type': 'string', 'length': 1, 'desc': 'T:틱차트<br/>B:분차트', 'required': True}, {'key': 'bgubun', 'name': '분구분', 'type': 'long', 'length': 3, 'desc': "차트구분이 'B'일때만 체크<br/>0: 30초<br/>0초과 : n분", 'required': True}, {'key': 'cnt', 'name': '조회건수', 'type': 'long', 'length': 3, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8462': {
        'tr_cd': 't8462',
        'title': 'KRX야간파생 투자자기간별(API용)',
        'blocks': {
            't8462InBlock': {
                'fields': [{'key': 'tm_rng', 'name': '시간대(D/N/U)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'fot_clsf_cd', 'name': '선물옵션구분', 'type': 'string', 'length': 1, 'desc': 'F : 선물<br/>C : 콜옵션<br/>P : 풋옵션<br/>S : 스프레드', 'required': True}, {'key': 'bsc_asts_id', 'name': '기초자산코드', 'type': 'string', 'length': 3, 'desc': 'K2I : KP200선물/옵션<br/>MKI : 미니KP200선물/옵션<br/>KQI : 코스닥150선물/옵션<br/>WKM : 위클리옵션-월<br/>WKI : 위클리옵션-목<br/>BM3 : 국채3년선물<br/>BMA : 국채10년선물<br/>USD : 미국달러선물', 'required': True}, {'key': 'gubun2', 'name': '수치구분(1:수치2:누적)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'gubun3', 'name': '단위구분(1:일2:주3:월)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'from_date', 'name': '시작날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'to_date', 'name': '종료날짜', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8463': {
        'tr_cd': 't8463',
        'title': 'KRX야간파생 투자자시간대별(API용)',
        'blocks': {
            't8463InBlock': {
                'fields': [{'key': 'tm_rng', 'name': '시간대(D/N/U)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'fot_clsf_cd', 'name': '선물옵션구분', 'type': 'string', 'length': 1, 'desc': 'F : 선물<br/>C : 콜옵션<br/>P : 풋옵션<br/>S : 스프레드', 'required': True}, {'key': 'bsc_asts_id', 'name': '기초자산코드', 'type': 'string', 'length': 3, 'desc': 'K2I : KP200선물/옵션<br/>MKI : 미니KP200선물/옵션<br/>KQI : 코스닥150선물/옵션<br/>WKM : 위클리옵션-월<br/>WKI : 위클리옵션-목<br/>BM3 : 국채3년선물<br/>BMA : 국채10년선물<br/>USD : 미국달러선물', 'required': True}, {'key': 'cnt', 'name': '조회건수', 'type': 'long', 'length': 3, 'required': True}, {'key': 'bgubun', 'name': '전일분', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    't9943': {
        'tr_cd': 't9943',
        'title': '지수선물마스터조회API용',
        'blocks': {
            't9943InBlock': {
                'fields': [{'key': 'gubun', 'name': '구분', 'type': 'string', 'length': 1, 'desc': 'V:변동성지수선물 S:섹터지수선물 그 이외의 값은 코스피200지수선물', 'required': True}],
                'type': 'single'
            }
        }
    },
    't9944': {
        'tr_cd': 't9944',
        'title': '지수옵션마스터조회API용',
        'blocks': {
            't9944InBlock': {
                'fields': [{'key': 'dummy', 'name': 'Dummy', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    }
}
