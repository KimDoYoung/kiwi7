# kiwoom_api_definition.py
"""
모듈 설명: 
    - 키움에서 제공하는 excel에서 유틸리티(extract_kw_api_def.py)를 이용해서 KIWOOM_REQUEST_DEF 만듬.
    - API 정의 정보를 관리하고 조회하는 기능을 제공
    - python ./extract_kw_req_def.py c:\\tmp\\kwapi.xlsx > 1.txt
    - python ./extract_kw_resp_def.py c:\\tmp\\kwapi.xlsx > 2.txt
주요 기능:
    - get_required_fields: 필수 필드 목록을 반환
    - get_api_definition: api_id로 KIWOOM_REQUEST_DEF

작성자: 김도영
작성일: 2025-07-24
버전: 1.0
"""
from typing import Dict, Any, List

KIWOOM_REQUEST_DEF = {
'au10001': {
    'url': 'https://api.kiwoom.com/oauth2/token',
    'title': '접근토큰 발급',
    'body': [
        {'key': 'grant_type', 'name': 'grant_type', 'type': 'string', 'required': True, 'length': None, 'description': 'client_credentials 입력'},
        {'key': 'appkey', 'name': '앱키', 'type': 'string', 'required': True, 'length': None, 'description': ''},
        {'key': 'secretkey', 'name': '시크릿키', 'type': 'string', 'required': True, 'length': None, 'description': ''}
    ]
},

'au10002': {
    'url': 'https://api.kiwoom.com/oauth2/revoke',
    'title': '접근토큰폐기',
    'body': [
        {'key': 'appkey', 'name': '앱키', 'type': 'string', 'required': True, 'length': None, 'description': ''},
        {'key': 'secretkey', 'name': '시크릿키', 'type': 'string', 'required': True, 'length': None, 'description': ''},
        {'key': 'token', 'name': '접근토큰', 'type': 'string', 'required': True, 'length': None, 'description': ''}
    ]
},
'ka00198': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '실시간종목조회순위',
    'body': [
        {'key': 'qry_tp', 'name': '구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:1분, 2:10분, 3:1시간, 4:당일 누적, 5:30초'}
    ]
},

'ka01690': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '일별잔고수익률',
    'body': [
        {'key': 'qry_dt', 'name': '조회일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''}
    ]
},
'ka10001': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '주식기본정보요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'}
    ]
},

'ka10002': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '주식거래원요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'}
    ]
},

'ka10003': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '체결정보요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'}
    ]
},

'ka10004': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '주식호가요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'}
    ]
},

'ka10005': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '주식일주월시분요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'}
    ]
},

'ka10006': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '주식시분요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'}
    ]
},

'ka10007': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '시세표성정보요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'}
    ]
},

'ka10008': {
    'url': 'https://api.kiwoom.com/api/dostk/frgnistt',
    'title': '주식외국인종목별매매동향',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'}
    ]
},

'ka10009': {
    'url': 'https://api.kiwoom.com/api/dostk/frgnistt',
    'title': '주식기관요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'}
    ]
},

'ka10010': {
    'url': 'https://api.kiwoom.com/api/dostk/sect',
    'title': '업종프로그램요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'}
    ]
},

'ka10011': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '신주인수권전체시세요청',
    'body': [
        {'key': 'newstk_recvrht_tp', 'name': '신주인수권구분', 'type': 'string', 'required': True, 'length': 2, 'description': '00:전체, 05:신주인수권증권, 07:신주인수권증서'}
    ]
},

'ka10013': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '신용매매동향요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'dt', 'name': '일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'qry_tp', 'name': '조회구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:융자, 2:대주'}
    ]
},

'ka10014': {
    'url': 'https://api.kiwoom.com/api/dostk/shsa',
    'title': '공매도추이요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'tm_tp', 'name': '시간구분', 'type': 'string', 'required': False, 'length': 1, 'description': '0:시작일, 1:기간'},
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'}
    ]
},

'ka10015': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '일별거래상세요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'}
    ]
},

'ka10016': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '신고저가요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'ntl_tp', 'name': '신고저구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:신고가,2:신저가'},
        {'key': 'high_low_close_tp', 'name': '고저종구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:고저기준, 2:종가기준'},
        {'key': 'stk_cnd', 'name': '종목조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회,1:관리종목제외, 3:우선주제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 5, 'description': '00000:전체조회, 00010:만주이상, 00050:5만주이상, 00100:10만주이상, 00150:15만주이상, 00200:20만주이상, 00300:30만주이상, 00500:50만주이상, 01000:백만주이상'},
        {'key': 'crd_cnd', 'name': '신용조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체'},
        {'key': 'updown_incls', 'name': '상하한포함', 'type': 'string', 'required': True, 'length': 1, 'description': '0:미포함, 1:포함'},
        {'key': 'dt', 'name': '기간', 'type': 'string', 'required': True, 'length': 3, 'description': '5:5일, 10:10일, 20:20일, 60:60일, 250:250일, 250일까지 입력가능'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10017': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '상하한가요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'updown_tp', 'name': '상하한구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:상한, 2:상승, 3:보합, 4: 하한, 5:하락, 6:전일상한, 7:전일하한'},
        {'key': 'sort_tp', 'name': '정렬구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:종목코드순, 2:연속횟수순(상위100개), 3:등락률순'},
        {'key': 'stk_cnd', 'name': '종목조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회,1:관리종목제외, 3:우선주제외, 4:우선주+관리종목제외, 5:증100제외, 6:증100만 보기, 7:증40만 보기, 8:증30만 보기, 9:증20만 보기, 10:우선주+관리종목+환기종목제외'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 5, 'description': '00000:전체조회, 00010:만주이상, 00050:5만주이상, 00100:10만주이상, 00150:15만주이상, 00200:20만주이상, 00300:30만주이상, 00500:50만주이상, 01000:백만주이상'},
        {'key': 'crd_cnd', 'name': '신용조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체'},
        {'key': 'trde_gold_tp', 'name': '매매금구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:1천원미만, 2:1천원~2천원, 3:2천원~3천원, 4:5천원~1만원, 5:1만원이상, 8:1천원이상'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10018': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '고저가근접요청',
    'body': [
        {'key': 'high_low_tp', 'name': '고저구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:고가, 2:저가'},
        {'key': 'alacc_rt', 'name': '근접율', 'type': 'string', 'required': True, 'length': 2, 'description': '05:0.5 10:1.0, 15:1.5, 20:2.0. 25:2.5, 30:3.0'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 5, 'description': '00000:전체조회, 00010:만주이상, 00050:5만주이상, 00100:10만주이상, 00150:15만주이상, 00200:20만주이상, 00300:30만주이상, 00500:50만주이상, 01000:백만주이상'},
        {'key': 'stk_cnd', 'name': '종목조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회,1:관리종목제외, 3:우선주제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기'},
        {'key': 'crd_cnd', 'name': '신용조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10019': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '가격급등락요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥, 201:코스피200'},
        {'key': 'flu_tp', 'name': '등락구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:급등, 2:급락'},
        {'key': 'tm_tp', 'name': '시간구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:분전, 2:일전'},
        {'key': 'tm', 'name': '시간', 'type': 'string', 'required': True, 'length': 2, 'description': '분 혹은 일입력'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 4, 'description': '00000:전체조회, 00010:만주이상, 00050:5만주이상, 00100:10만주이상, 00150:15만주이상, 00200:20만주이상, 00300:30만주이상, 00500:50만주이상, 01000:백만주이상'},
        {'key': 'stk_cnd', 'name': '종목조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회,1:관리종목제외, 3:우선주제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기'},
        {'key': 'crd_cnd', 'name': '신용조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체'},
        {'key': 'pric_cnd', 'name': '가격조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:1천원미만, 2:1천원~2천원, 3:2천원~3천원, 4:5천원~1만원, 5:1만원이상, 8:1천원이상'},
        {'key': 'updown_incls', 'name': '상하한포함', 'type': 'string', 'required': True, 'length': 1, 'description': '0:미포함, 1:포함'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10020': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '호가잔량상위요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '001:코스피, 101:코스닥'},
        {'key': 'sort_tp', 'name': '정렬구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:순매수잔량순, 2:순매도잔량순, 3:매수비율순, 4:매도비율순'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 4, 'description': '0000:장시작전(0주이상), 0010:만주이상, 0050:5만주이상, 00100:10만주이상'},
        {'key': 'stk_cnd', 'name': '종목조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:관리종목제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기'},
        {'key': 'crd_cnd', 'name': '신용조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10021': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '호가잔량급증요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '001:코스피, 101:코스닥'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:매수잔량, 2:매도잔량'},
        {'key': 'sort_tp', 'name': '정렬구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:급증량, 2:급증률'},
        {'key': 'tm_tp', 'name': '시간구분', 'type': 'string', 'required': True, 'length': 2, 'description': '분 입력'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 4, 'description': '1:천주이상, 5:5천주이상, 10:만주이상, 50:5만주이상, 100:10만주이상'},
        {'key': 'stk_cnd', 'name': '종목조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:관리종목제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10022': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '잔량율급증요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '001:코스피, 101:코스닥'},
        {'key': 'rt_tp', 'name': '비율구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:매수/매도비율, 2:매도/매수비율'},
        {'key': 'tm_tp', 'name': '시간구분', 'type': 'string', 'required': True, 'length': 2, 'description': '분 입력'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '5:5천주이상, 10:만주이상, 50:5만주이상, 100:10만주이상'},
        {'key': 'stk_cnd', 'name': '종목조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:관리종목제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10023': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '거래량급증요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'sort_tp', 'name': '정렬구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:급증량, 2:급증률, 3:급감량, 4:급감률'},
        {'key': 'tm_tp', 'name': '시간구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:분, 2:전일'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '5:5천주이상, 10:만주이상, 50:5만주이상, 100:10만주이상, 200:20만주이상, 300:30만주이상, 500:50만주이상, 1000:백만주이상'},
        {'key': 'tm', 'name': '시간', 'type': 'string', 'required': False, 'length': 2, 'description': '분 입력'},
        {'key': 'stk_cnd', 'name': '종목조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:관리종목제외, 3:우선주제외, 11:정리매매종목제외, 4:관리종목,우선주제외, 5:증100제외, 6:증100만보기, 13:증60만보기, 12:증50만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기, 17:ETN제외, 14:ETF제외, 18:ETF+ETN제외, 15:스팩제외, 20:ETF+ETN+스팩제외'},
        {'key': 'pric_tp', 'name': '가격구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 2:5만원이상, 5:1만원이상, 6:5천원이상, 8:1천원이상, 9:10만원이상'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10024': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '거래량갱신요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'cycle_tp', 'name': '주기구분', 'type': 'string', 'required': True, 'length': 1, 'description': '5:5일, 10:10일, 20:20일, 60:60일, 250:250일'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '5:5천주이상, 10:만주이상, 50:5만주이상, 100:10만주이상, 200:20만주이상, 300:30만주이상, 500:50만주이상, 1000:백만주이상'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10025': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '매물대집중요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'prps_cnctr_rt', 'name': '매물집중비율', 'type': 'string', 'required': True, 'length': 3, 'description': '0~100 입력'},
        {'key': 'cur_prc_entry', 'name': '현재가진입', 'type': 'string', 'required': True, 'length': 1, 'description': '0:현재가 매물대 진입 포함안함, 1:현재가 매물대 진입포함'},
        {'key': 'prpscnt', 'name': '매물대수', 'type': 'string', 'required': True, 'length': 2, 'description': '숫자입력'},
        {'key': 'cycle_tp', 'name': '주기구분', 'type': 'string', 'required': True, 'length': 2, 'description': '50:50일, 100:100일, 150:150일, 200:200일, 250:250일, 300:300일'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10026': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '고저PER요청',
    'body': [
        {'key': 'pertp', 'name': 'PER구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:저PBR, 2:고PBR, 3:저PER, 4:고PER, 5:저ROE, 6:고ROE'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10027': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '전일대비등락률상위요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'sort_tp', 'name': '정렬구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:상승률, 2:상승폭, 3:하락률, 4:하락폭, 5:보합'},
        {'key': 'trde_qty_cnd', 'name': '거래량조건', 'type': 'string', 'required': True, 'length': 5, 'description': '0000:전체조회, 0010:만주이상, 0050:5만주이상, 0100:10만주이상, 0150:15만주이상, 0200:20만주이상, 0300:30만주이상, 0500:50만주이상, 1000:백만주이상'},
        {'key': 'stk_cnd', 'name': '종목조건', 'type': 'string', 'required': True, 'length': 2, 'description': '0:전체조회, 1:관리종목제외, 4:우선주+관리주제외, 3:우선주제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기, 11:정리매매종목제외, 12:증50만보기, 13:증60만보기, 14:ETF제외, 15:스펙제외, 16:ETF+ETN제외'},
        {'key': 'crd_cnd', 'name': '신용조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체'},
        {'key': 'updown_incls', 'name': '상하한포함', 'type': 'string', 'required': True, 'length': 2, 'description': '0:불 포함, 1:포함'},
        {'key': 'pric_cnd', 'name': '가격조건', 'type': 'string', 'required': True, 'length': 2, 'description': '0:전체조회, 1:1천원미만, 2:1천원~2천원, 3:2천원~5천원, 4:5천원~1만원, 5:1만원이상, 8:1천원이상, 10: 1만원미만'},
        {'key': 'trde_prica_cnd', 'name': '거래대금조건', 'type': 'string', 'required': True, 'length': 4, 'description': '0:전체조회, 3:3천만원이상, 5:5천만원이상, 10:1억원이상, 30:3억원이상, 50:5억원이상, 100:10억원이상, 300:30억원이상, 500:50억원이상, 1000:100억원이상, 3000:300억원이상, 5000:500억원이상'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10028': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '시가대비등락률요청',
    'body': [
        {'key': 'sort_tp', 'name': '정렬구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:시가, 2:고가, 3:저가, 4:기준가'},
        {'key': 'trde_qty_cnd', 'name': '거래량조건', 'type': 'string', 'required': True, 'length': 4, 'description': '0000:전체조회, 0010:만주이상, 0050:5만주이상, 0100:10만주이상, 0500:50만주이상, 1000:백만주이상'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'updown_incls', 'name': '상하한포함', 'type': 'string', 'required': True, 'length': 1, 'description': '0:불 포함, 1:포함'},
        {'key': 'stk_cnd', 'name': '종목조건', 'type': 'string', 'required': True, 'length': 2, 'description': '0:전체조회, 1:관리종목제외, 4:우선주+관리주제외, 3:우선주제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기'},
        {'key': 'crd_cnd', 'name': '신용조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체'},
        {'key': 'trde_prica_cnd', 'name': '거래대금조건', 'type': 'string', 'required': True, 'length': 4, 'description': '0:전체조회, 3:3천만원이상, 5:5천만원이상, 10:1억원이상, 30:3억원이상, 50:5억원이상, 100:10억원이상, 300:30억원이상, 500:50억원이상, 1000:100억원이상, 3000:300억원이상, 5000:500억원이상'},
        {'key': 'flu_cnd', 'name': '등락조건', 'type': 'string', 'required': True, 'length': 1, 'description': '1:상위, 2:하위'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10029': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '예상체결등락률상위요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'sort_tp', 'name': '정렬구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:상승률, 2:상승폭, 3:보합, 4:하락률, 5:하락폭, 6:체결량, 7:상한, 8:하한'},
        {'key': 'trde_qty_cnd', 'name': '거래량조건', 'type': 'string', 'required': True, 'length': 5, 'description': '0:전체조회, 1;천주이상, 3:3천주, 5:5천주, 10:만주이상, 50:5만주이상, 100:10만주이상'},
        {'key': 'stk_cnd', 'name': '종목조건', 'type': 'string', 'required': True, 'length': 2, 'description': '0:전체조회, 1:관리종목제외, 3:우선주제외, 4:관리종목,우선주제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기, 11:정리매매종목제외, 12:증50만보기, 13:증60만보기, 14:ETF제외, 15:스팩제외, 16:ETF+ETN제외'},
        {'key': 'crd_cnd', 'name': '신용조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 5:신용한도초과제외, 8:신용대주, 9:신용융자전체'},
        {'key': 'pric_cnd', 'name': '가격조건', 'type': 'string', 'required': True, 'length': 2, 'description': '0:전체조회, 1:1천원미만, 2:1천원~2천원, 3:2천원~5천원, 4:5천원~1만원, 5:1만원이상, 8:1천원이상, 10:1만원미만'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10030': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '당일거래량상위요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'sort_tp', 'name': '정렬구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:거래량, 2:거래회전율, 3:거래대금'},
        {'key': 'mang_stk_incls', 'name': '관리종목포함', 'type': 'string', 'required': True, 'length': 1, 'description': '0:관리종목 포함, 1:관리종목 미포함, 3:우선주제외, 11:정리매매종목제외, 4:관리종목, 우선주제외, 5:증100제외, 6:증100마나보기, 13:증60만보기, 12:증50만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기, 14:ETF제외, 15:스팩제외, 16:ETF+ETN제외'},
        {'key': 'crd_tp', 'name': '신용구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 9:신용융자전체, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 8:신용대주'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 5:5천주이상, 10:1만주이상, 50:5만주이상, 100:10만주이상, 200:20만주이상, 300:30만주이상, 500:500만주이상, 1000:백만주이상'},
        {'key': 'pric_tp', 'name': '가격구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:1천원미만, 2:1천원이상, 3:1천원~2천원, 4:2천원~5천원, 5:5천원이상, 6:5천원~1만원, 10:1만원미만, 7:1만원이상, 8:5만원이상, 9:10만원이상'},
        {'key': 'trde_prica_tp', 'name': '거래대금구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:1천만원이상, 3:3천만원이상, 4:5천만원이상, 10:1억원이상, 30:3억원이상, 50:5억원이상, 100:10억원이상, 300:30억원이상, 500:50억원이상, 1000:100억원이상, 3000:300억원이상, 5000:500억원이상'},
        {'key': 'mrkt_open_tp', 'name': '장운영구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:장중, 2:장전시간외, 3:장후시간외'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10031': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '전일거래량상위요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'qry_tp', 'name': '조회구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:전일거래량 상위100종목, 2:전일거래대금 상위100종목'},
        {'key': 'rank_strt', 'name': '순위시작', 'type': 'string', 'required': True, 'length': 3, 'description': '0 ~ 100 값 중에  조회를 원하는 순위 시작값'},
        {'key': 'rank_end', 'name': '순위끝', 'type': 'string', 'required': True, 'length': 3, 'description': '0 ~ 100 값 중에  조회를 원하는 순위 끝값'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10032': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '거래대금상위요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'mang_stk_incls', 'name': '관리종목포함', 'type': 'string', 'required': True, 'length': 1, 'description': '0:관리종목 미포함, 1:관리종목 포함'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10033': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '신용비율상위요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 3, 'description': '0:전체조회, 10:만주이상, 50:5만주이상, 100:10만주이상, 200:20만주이상, 300:30만주이상, 500:50만주이상, 1000:백만주이상'},
        {'key': 'stk_cnd', 'name': '종목조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:관리종목제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기'},
        {'key': 'updown_incls', 'name': '상하한포함', 'type': 'string', 'required': True, 'length': 1, 'description': '0:상하한 미포함, 1:상하한포함'},
        {'key': 'crd_cnd', 'name': '신용조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10034': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '외인기간별매매상위요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:순매도, 2:순매수, 3:순매매'},
        {'key': 'dt', 'name': '기간', 'type': 'string', 'required': True, 'length': 2, 'description': '0:당일, 1:전일, 5:5일, 10;10일, 20:20일, 60:60일'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT, 3:통합'}
    ]
},

'ka10035': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '외인연속순매매상위요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:연속순매도, 2:연속순매수'},
        {'key': 'base_dt_tp', 'name': '기준일구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:당일기준, 1:전일기준'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT, 3:통합'}
    ]
},

'ka10036': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '외인한도소진율증가상위',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'dt', 'name': '기간', 'type': 'string', 'required': True, 'length': 2, 'description': '0:당일, 1:전일, 5:5일, 10;10일, 20:20일, 60:60일'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT, 3:통합'}
    ]
},

'ka10037': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '외국계창구매매상위요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'dt', 'name': '기간', 'type': 'string', 'required': True, 'length': 2, 'description': '0:당일, 1:전일, 5:5일, 10;10일, 20:20일, 60:60일'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:순매수, 2:순매도, 3:매수, 4:매도'},
        {'key': 'sort_tp', 'name': '정렬구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:금액, 2:수량'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT, 3:통합'}
    ]
},

'ka10038': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '종목별증권사순위요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD (연도4자리, 월 2자리, 일 2자리 형식)'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD (연도4자리, 월 2자리, 일 2자리 형식)'},
        {'key': 'qry_tp', 'name': '조회구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:순매도순위정렬, 2:순매수순위정렬'},
        {'key': 'dt', 'name': '기간', 'type': 'string', 'required': True, 'length': 2, 'description': '1:전일, 4:5일, 9:10일, 19:20일, 39:40일, 59:60일, 119:120일'}
    ]
},

'ka10039': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '증권사별매매상위요청',
    'body': [
        {'key': 'mmcm_cd', 'name': '회원사코드', 'type': 'string', 'required': True, 'length': 3, 'description': '회원사 코드는 ka10102 조회'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 4, 'description': '0:전체, 5:5000주, 10:1만주, 50:5만주, 100:10만주, 500:50만주, 1000: 100만주'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 2, 'description': '1:순매수, 2:순매도'},
        {'key': 'dt', 'name': '기간', 'type': 'string', 'required': True, 'length': 2, 'description': '1:전일, 5:5일, 10:10일, 60:60일'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10040': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '당일주요거래원요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka10042': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '순매수거래원순위요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD (연도4자리, 월 2자리, 일 2자리 형식)'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD (연도4자리, 월 2자리, 일 2자리 형식)'},
        {'key': 'qry_dt_tp', 'name': '조회기간구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:기간으로 조회, 1:시작일자, 종료일자로 조회'},
        {'key': 'pot_tp', 'name': '시점구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:당일, 1:전일'},
        {'key': 'dt', 'name': '기간', 'type': 'string', 'required': False, 'length': 4, 'description': '5:5일, 10:10일, 20:20일, 40:40일, 60:60일, 120:120일'},
        {'key': 'sort_base', 'name': '정렬기준', 'type': 'string', 'required': True, 'length': 1, 'description': '1:종가순, 2:날짜순'}
    ]
},

'ka10043': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '거래원매물대분석요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'qry_dt_tp', 'name': '조회기간구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:기간으로 조회, 1:시작일자, 종료일자로 조회'},
        {'key': 'pot_tp', 'name': '시점구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:당일, 1:전일'},
        {'key': 'dt', 'name': '기간', 'type': 'string', 'required': True, 'length': 4, 'description': '5:5일, 10:10일, 20:20일, 40:40일, 60:60일, 120:120일'},
        {'key': 'sort_base', 'name': '정렬기준', 'type': 'string', 'required': True, 'length': 1, 'description': '1:종가순, 2:날짜순'},
        {'key': 'mmcm_cd', 'name': '회원사코드', 'type': 'string', 'required': True, 'length': 3, 'description': '회원사 코드는 ka10102 조회'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10044': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '일별기관매매종목요청',
    'body': [
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:순매도, 2:순매수'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '001:코스피, 101:코스닥'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10045': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '종목별기관매매추이요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'orgn_prsm_unp_tp', 'name': '기관추정단가구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:매수단가, 2:매도단가'},
        {'key': 'for_prsm_unp_tp', 'name': '외인추정단가구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:매수단가, 2:매도단가'}
    ]
},

'ka10046': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '체결강도추이시간별요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'}
    ]
},

'ka10047': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '체결강도추이일별요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'}
    ]
},

'ka10048': {
    'url': 'https://api.kiwoom.com/api/dostk/elw',
    'title': 'ELW일별민감도지표요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka10050': {
    'url': 'https://api.kiwoom.com/api/dostk/elw',
    'title': 'ELW민감도지표요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka10051': {
    'url': 'https://api.kiwoom.com/api/dostk/sect',
    'title': '업종별투자자순매수요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 1, 'description': '코스피:0, 코스닥:1'},
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '금액:0, 수량:1'},
        {'key': 'base_dt', 'name': '기준일자', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT, 3:통합'}
    ]
},

'ka10052': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '거래원순간거래량요청',
    'body': [
        {'key': 'mmcm_cd', 'name': '회원사코드', 'type': 'string', 'required': True, 'length': 3, 'description': '회원사 코드는 ka10102 조회'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': False, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:코스피, 2:코스닥, 3:종목'},
        {'key': 'qty_tp', 'name': '수량구분', 'type': 'string', 'required': True, 'length': 3, 'description': '0:전체, 1:1000주, 2:2000주, 3:, 5:, 10:10000주, 30: 30000주, 50: 50000주, 100: 100000주'},
        {'key': 'pric_tp', 'name': '가격구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:1천원 미만, 8:1천원 이상, 2:1천원 ~ 2천원, 3:2천원 ~ 5천원, 4:5천원 ~ 1만원, 5:1만원 이상'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10053': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '당일상위이탈원요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'}
    ]
},

'ka10054': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '변동성완화장치발동종목요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001: 코스피, 101:코스닥'},
        {'key': 'bf_mkrt_tp', 'name': '장전구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:정규시장,2:시간외단일가'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': False, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)  공백입력시 시장구분으로 설정한 전체종목조회'},
        {'key': 'motn_tp', 'name': '발동구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:정적VI, 2:동적VI, 3:동적VI + 정적VI'},
        {'key': 'skip_stk', 'name': '제외종목', 'type': 'string', 'required': True, 'length': 9, 'description': '전종목포함 조회시 9개 0으로 설정(000000000),전종목제외 조회시 9개 1으로 설정(111111111),9개 종목조회여부를 조회포함(0), 조회제외(1)로 설정하며 종목순서는 우선주,관리종목,투자경고/위험,투자주의,환기종목,단기과열종목,증거금100%,ETF,ETN가 됨.우선주만 조회시"011111111"", 관리종목만 조회시 ""101111111"" 설정"'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:사용안함, 1:사용'},
        {'key': 'min_trde_qty', 'name': '최소거래량', 'type': 'string', 'required': True, 'length': 12, 'description': '0 주 이상, 거래량구분이 1일때만 입력(공백허용)'},
        {'key': 'max_trde_qty', 'name': '최대거래량', 'type': 'string', 'required': True, 'length': 12, 'description': '100000000 주 이하, 거래량구분이 1일때만 입력(공백허용)'},
        {'key': 'trde_prica_tp', 'name': '거래대금구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:사용안함, 1:사용'},
        {'key': 'min_trde_prica', 'name': '최소거래대금', 'type': 'string', 'required': True, 'length': 10, 'description': '0 백만원 이상, 거래대금구분 1일때만 입력(공백허용)'},
        {'key': 'max_trde_prica', 'name': '최대거래대금', 'type': 'string', 'required': True, 'length': 10, 'description': '100000000 백만원 이하, 거래대금구분 1일때만 입력(공백허용)'},
        {'key': 'motn_drc', 'name': '발동방향', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:상승, 2:하락'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10055': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '당일전일체결량요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'tdy_pred', 'name': '당일전일', 'type': 'string', 'required': True, 'length': 1, 'description': '1:당일, 2:전일'}
    ]
},

'ka10058': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '투자자별일별매매종목요청',
    'body': [
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '순매도:1, 순매수:2'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '001:코스피, 101:코스닥'},
        {'key': 'invsr_tp', 'name': '투자자구분', 'type': 'string', 'required': True, 'length': 4, 'description': '8000:개인, 9000:외국인, 1000:금융투자, 3000:투신, 5000:기타금융, 4000:은행, 2000:보험, 6000:연기금, 7000:국가, 7100:기타법인, 9999:기관계'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10059': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '종목별투자자기관별요청',
    'body': [
        {'key': 'dt', 'name': '일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:금액, 2:수량'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:순매수, 1:매수, 2:매도'},
        {'key': 'unit_tp', 'name': '단위구분', 'type': 'string', 'required': True, 'length': 4, 'description': '1000:천주, 1:단주'}
    ]
},

'ka10060': {
    'url': 'https://api.kiwoom.com/api/dostk/chart',
    'title': '종목별투자자기관별차트요청',
    'body': [
        {'key': 'dt', 'name': '일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:금액, 2:수량'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:순매수, 1:매수, 2:매도'},
        {'key': 'unit_tp', 'name': '단위구분', 'type': 'string', 'required': True, 'length': 4, 'description': '1000:천주, 1:단주'}
    ]
},

'ka10061': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '종목별투자자기관별합계요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:금액, 2:수량'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:순매수'},
        {'key': 'unit_tp', 'name': '단위구분', 'type': 'string', 'required': True, 'length': 4, 'description': '1000:천주, 1:단주'}
    ]
},

'ka10062': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '동일순매매순위요청',
    'body': [
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD (연도4자리, 월 2자리, 일 2자리 형식)'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD (연도4자리, 월 2자리, 일 2자리 형식)'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001: 코스피, 101:코스닥'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:순매수, 2:순매도'},
        {'key': 'sort_cnd', 'name': '정렬조건', 'type': 'string', 'required': True, 'length': 1, 'description': '1:수량, 2:금액'},
        {'key': 'unit_tp', 'name': '단위구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:단주, 1000:천주'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10063': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '장중투자자별매매요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:금액, 2:수량'},
        {'key': 'invsr', 'name': '투자자별', 'type': 'string', 'required': True, 'length': 1, 'description': '6:외국인, 7:기관계, 1:투신, 0:보험, 2:은행, 3:연기금, 4:국가, 5:기타법인'},
        {'key': 'frgn_all', 'name': '외국계전체', 'type': 'string', 'required': True, 'length': 1, 'description': '1:체크, 0:미체크'},
        {'key': 'smtm_netprps_tp', 'name': '동시순매수구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:체크, 0:미체크'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10064': {
    'url': 'https://api.kiwoom.com/api/dostk/chart',
    'title': '장중투자자별매매차트요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:금액, 2:수량'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:순매수, 1:매수, 2:매도'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'}
    ]
},

'ka10065': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '장중투자자별매매상위요청',
    'body': [
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:순매수, 2:순매도'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'orgn_tp', 'name': '기관구분', 'type': 'string', 'required': True, 'length': 4, 'description': '9000:외국인, 9100:외국계, 1000:금융투자, 3000:투신, 5000:기타금융, 4000:은행, 2000:보험, 6000:연기금, 7000:국가, 7100:기타법인, 9999:기관계'}
    ]
},

'ka10066': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '장마감후투자자별매매요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:금액, 2:수량'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:순매수, 1:매수, 2:매도'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka10068': {
    'url': 'https://api.kiwoom.com/api/dostk/slb',
    'title': '대차거래추이요청',
    'body': [
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'all_tp', 'name': '전체구분', 'type': 'string', 'required': True, 'length': 6, 'description': '1: 전체표시'}
    ]
},

'ka10069': {
    'url': 'https://api.kiwoom.com/api/dostk/slb',
    'title': '대차거래상위10종목요청',
    'body': [
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD (연도4자리, 월 2자리, 일 2자리 형식)'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD (연도4자리, 월 2자리, 일 2자리 형식)'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '001:코스피, 101:코스닥'}
    ]
},

'ka10072': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '일자별종목별실현손익요청_일자',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'}
    ]
},

'ka10073': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '일자별종목별실현손익요청_기간',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'}
    ]
},

'ka10074': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '일자별실현손익요청',
    'body': [
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''}
    ]
},

'ka10075': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '미체결요청',
    'body': [
        {'key': 'all_stk_tp', 'name': '전체종목구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:종목'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:매도, 2:매수'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': False, 'length': 6, 'description': ''},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0 : 통합, 1 : KRX, 2 : NXT'}
    ]
},

'ka10076': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '체결요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': False, 'length': 6, 'description': ''},
        {'key': 'qry_tp', 'name': '조회구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:종목'},
        {'key': 'sell_tp', 'name': '매도수구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:매도, 2:매수'},
        {'key': 'ord_no', 'name': '주문번호', 'type': 'string', 'required': False, 'length': 10, 'description': '검색 기준 값으로 입력한 주문번호 보다 과거에 체결된 내역이 조회됩니다.'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0 : 통합, 1 : KRX, 2 : NXT'}
    ]
},

'ka10077': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '당일실현손익상세요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka10078': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '증권사별종목매매동향요청',
    'body': [
        {'key': 'mmcm_cd', 'name': '회원사코드', 'type': 'string', 'required': True, 'length': 3, 'description': '회원사 코드는 ka10102 조회'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'}
    ]
},

'ka10079': {
    'url': 'https://api.kiwoom.com/api/dostk/chart',
    'title': '주식틱차트조회요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'tic_scope', 'name': '틱범위', 'type': 'string', 'required': True, 'length': 2, 'description': '1:1틱, 3:3틱, 5:5틱, 10:10틱, 30:30틱'},
        {'key': 'upd_stkpc_tp', 'name': '수정주가구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0 or 1'}
    ]
},

'ka10080': {
    'url': 'https://api.kiwoom.com/api/dostk/chart',
    'title': '주식분봉차트조회요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'tic_scope', 'name': '틱범위', 'type': 'string', 'required': True, 'length': 2, 'description': '1:1분, 3:3분, 5:5분, 10:10분, 15:15분, 30:30분, 45:45분, 60:60분'},
        {'key': 'upd_stkpc_tp', 'name': '수정주가구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0 or 1'}
    ]
},

'ka10081': {
    'url': 'https://api.kiwoom.com/api/dostk/chart',
    'title': '주식일봉차트조회요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'base_dt', 'name': '기준일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'upd_stkpc_tp', 'name': '수정주가구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0 or 1'}
    ]
},

'ka10082': {
    'url': 'https://api.kiwoom.com/api/dostk/chart',
    'title': '주식주봉차트조회요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'base_dt', 'name': '기준일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'upd_stkpc_tp', 'name': '수정주가구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0 or 1'}
    ]
},

'ka10083': {
    'url': 'https://api.kiwoom.com/api/dostk/chart',
    'title': '주식월봉차트조회요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'base_dt', 'name': '기준일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'upd_stkpc_tp', 'name': '수정주가구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0 or 1'}
    ]
},

'ka10084': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '당일전일체결요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'tdy_pred', 'name': '당일전일', 'type': 'string', 'required': True, 'length': 1, 'description': '당일 : 1, 전일 : 2'},
        {'key': 'tic_min', 'name': '틱분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:틱, 1:분'},
        {'key': 'tm', 'name': '시간', 'type': 'string', 'required': False, 'length': 4, 'description': '조회시간 4자리, 오전 9시일 경우 0900, 오후 2시 30분일 경우 1430'}
    ]
},

'ka10085': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '계좌수익률요청',
    'body': [
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0 : 통합, 1 : KRX, 2 : NXT'}
    ]
},

'ka10086': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '일별주가요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'qry_dt', 'name': '조회일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'indc_tp', 'name': '표시구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:수량, 1:금액(백만원)'}
    ]
},

'ka10087': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '시간외단일가요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka10088': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '미체결 분할주문 상세',
    'body': [
        {'key': 'ord_no', 'name': '주문번호', 'type': 'string', 'required': True, 'length': 20, 'description': ''}
    ]
},

'ka10094': {
    'url': 'https://api.kiwoom.com/api/dostk/chart',
    'title': '주식년봉차트조회요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'base_dt', 'name': '기준일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'upd_stkpc_tp', 'name': '수정주가구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0 or 1'}
    ]
},

'ka10095': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '관심종목정보요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL) 여러개의 종목코드 입력시 | 로 구분'}
    ]
},

'ka10098': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '시간외단일가등락율순위요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체,001:코스피,101:코스닥'},
        {'key': 'sort_base', 'name': '정렬기준', 'type': 'string', 'required': True, 'length': 1, 'description': '1:상승률, 2:상승폭, 3:하락률, 4:하락폭, 5:보합'},
        {'key': 'stk_cnd', 'name': '종목조건', 'type': 'string', 'required': True, 'length': 2, 'description': '0:전체조회,1:관리종목제외,2:정리매매종목제외,3:우선주제외,4:관리종목우선주제외,5:증100제외,6:증100만보기,7:증40만보기,8:증30만보기,9:증20만보기,12:증50만보기,13:증60만보기,14:ETF제외,15:스팩제외,16:ETF+ETN제외,17:ETN제외'},
        {'key': 'trde_qty_cnd', 'name': '거래량조건', 'type': 'string', 'required': True, 'length': 5, 'description': '0:전체조회, 10:백주이상,50:5백주이상,100;천주이상, 500:5천주이상, 1000:만주이상, 5000:5만주이상, 10000:10만주이상'},
        {'key': 'crd_cnd', 'name': '신용조건', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체조회, 9:신용융자전체, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 8:신용대주, 5:신용한도초과제외'},
        {'key': 'trde_prica', 'name': '거래대금', 'type': 'string', 'required': True, 'length': 5, 'description': '0:전체조회, 5:5백만원이상,10:1천만원이상, 30:3천만원이상, 50:5천만원이상, 100:1억원이상, 300:3억원이상, 500:5억원이상, 1000:10억원이상, 3000:30억원이상, 5000:50억원이상, 10000:100억원이상'}
    ]
},

'ka10099': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '종목정보 리스트',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 2, 'description': '0:코스피,10:코스닥,3:ELW,8:ETF,30:K-OTC,50:코넥스,5:신주인수권,4:뮤추얼펀드,6:리츠,9:하이일드'}
    ]
},

'ka10100': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '종목정보 조회',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka10101': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '업종코드 리스트',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:코스피(거래소),1:코스닥,2:KOSPI200,4:KOSPI100,7:KRX100(통합지수)'}
    ]
},

'ka10102': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '회원사 리스트',
    'body': [
    ]
},

'ka10131': {
    'url': 'https://api.kiwoom.com/api/dostk/frgnistt',
    'title': '기관외국인연속매매현황요청',
    'body': [
        {'key': 'dt', 'name': '기간', 'type': 'string', 'required': True, 'length': 3, 'description': '1:최근일, 3:3일, 5:5일, 10:10일, 20:20일, 120:120일, 0:시작일자/종료일자로 조회'},
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'mrkt_tp', 'name': '장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '001:코스피, 101:코스닥'},
        {'key': 'netslmt_tp', 'name': '순매도수구분', 'type': 'string', 'required': True, 'length': 1, 'description': '2:순매수(고정값)'},
        {'key': 'stk_inds_tp', 'name': '종목업종구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:종목(주식),1:업종'},
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:금액, 1:수량'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT, 3:통합'}
    ]
},

'ka10170': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '당일매매일지요청',
    'body': [
        {'key': 'base_dt', 'name': '기준일자', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD(공백입력시 금일데이터,최근 2개월까지 제공)'},
        {'key': 'ottks_tp', 'name': '단주구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:당일매수에 대한 당일매도,2:당일매도 전체'},
        {'key': 'ch_crd_tp', 'name': '현금신용구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:현금매매만, 2:신용매매만'}
    ]
},

'ka10171': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '조건검색 목록조회',
    'body': [
        {'key': 'trnm', 'name': 'TR명', 'type': 'string', 'required': True, 'length': 7, 'description': 'CNSRLST고정값'}
    ]
},

'ka10172': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '조건검색 요청 일반',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 7, 'description': 'CNSRREQ 고정값'},
        {'key': 'seq', 'name': '조건검색식 일련번호', 'type': 'string', 'required': True, 'length': 3, 'description': ''},
        {'key': 'search_type', 'name': '조회타입', 'type': 'string', 'required': True, 'length': None, 'description': '0:조건검색'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': 'K:KRX'},
        {'key': 'cont_yn', 'name': '연속조회여부', 'type': 'string', 'required': False, 'length': 1, 'description': 'Y:연속조회요청,N:연속조회미요청'},
        {'key': 'next_key', 'name': '연속조회키', 'type': 'string', 'required': False, 'length': 20, 'description': ''}
    ]
},

'ka10173': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '조건검색 요청 실시간',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 7, 'description': 'CNSRREQ 고정값'},
        {'key': 'seq', 'name': '조건검색식 일련번호', 'type': 'string', 'required': True, 'length': 3, 'description': ''},
        {'key': 'search_type', 'name': '조회타입', 'type': 'string', 'required': True, 'length': 1, 'description': '1: 조건검색+실시간조건검색'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': 'K:KRX'}
    ]
},

'ka10174': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '조건검색 실시간 해제',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 7, 'description': 'CNSRCLR 고정값'},
        {'key': 'seq', 'name': '조건검색식 일련번호', 'type': 'string', 'required': True, 'length': None, 'description': ''}
    ]
},

'ka20001': {
    'url': 'https://api.kiwoom.com/api/dostk/sect',
    'title': '업종현재가요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:코스피, 1:코스닥, 2:코스피200'},
        {'key': 'inds_cd', 'name': '업종코드', 'type': 'string', 'required': True, 'length': 3, 'description': '001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주 101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701: KRX100 나머지 ※ 업종코드 참고'}
    ]
},

'ka20002': {
    'url': 'https://api.kiwoom.com/api/dostk/sect',
    'title': '업종별주가요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:코스피, 1:코스닥, 2:코스피200'},
        {'key': 'inds_cd', 'name': '업종코드', 'type': 'string', 'required': True, 'length': 3, 'description': '001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주 101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701: KRX100 나머지 ※ 업종코드 참고'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT, 3:통합'}
    ]
},

'ka20003': {
    'url': 'https://api.kiwoom.com/api/dostk/sect',
    'title': '전업종지수요청',
    'body': [
        {'key': 'inds_cd', 'name': '업종코드', 'type': 'string', 'required': True, 'length': 3, 'description': '001:종합(KOSPI), 101:종합(KOSDAQ)'}
    ]
},

'ka20004': {
    'url': 'https://api.kiwoom.com/api/dostk/chart',
    'title': '업종틱차트조회요청',
    'body': [
        {'key': 'inds_cd', 'name': '업종코드', 'type': 'string', 'required': True, 'length': 3, 'description': '001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주 101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701: KRX100 나머지 ※ 업종코드 참고'},
        {'key': 'tic_scope', 'name': '틱범위', 'type': 'string', 'required': True, 'length': 2, 'description': '1:1틱, 3:3틱, 5:5틱, 10:10틱, 30:30틱'}
    ]
},

'ka20005': {
    'url': 'https://api.kiwoom.com/api/dostk/chart',
    'title': '업종분봉조회요청',
    'body': [
        {'key': 'inds_cd', 'name': '업종코드', 'type': 'string', 'required': True, 'length': 3, 'description': '001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주 101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701: KRX100 나머지 ※ 업종코드 참고'},
        {'key': 'tic_scope', 'name': '틱범위', 'type': 'string', 'required': True, 'length': 2, 'description': '1:1틱, 3:3틱, 5:5틱, 10:10틱, 30:30틱'}
    ]
},

'ka20006': {
    'url': 'https://api.kiwoom.com/api/dostk/chart',
    'title': '업종일봉조회요청',
    'body': [
        {'key': 'inds_cd', 'name': '업종코드', 'type': 'string', 'required': True, 'length': 3, 'description': '001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주 101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701: KRX100 나머지 ※ 업종코드 참고'},
        {'key': 'base_dt', 'name': '기준일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'}
    ]
},

'ka20007': {
    'url': 'https://api.kiwoom.com/api/dostk/chart',
    'title': '업종주봉조회요청',
    'body': [
        {'key': 'inds_cd', 'name': '업종코드', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'base_dt', 'name': '기준일자', 'type': 'string', 'required': True, 'length': 3, 'description': '001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주 101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701: KRX100 나머지 ※ 업종코드 참고'}
    ]
},

'ka20008': {
    'url': 'https://api.kiwoom.com/api/dostk/chart',
    'title': '업종월봉조회요청',
    'body': [
        {'key': 'inds_cd', 'name': '업종코드', 'type': 'string', 'required': True, 'length': 3, 'description': '001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주 101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701: KRX100 나머지 ※ 업종코드 참고'},
        {'key': 'base_dt', 'name': '기준일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'}
    ]
},

'ka20009': {
    'url': 'https://api.kiwoom.com/api/dostk/sect',
    'title': '업종현재가일별요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:코스피, 1:코스닥, 2:코스피200'},
        {'key': 'inds_cd', 'name': '업종코드', 'type': 'string', 'required': True, 'length': 3, 'description': '001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주 101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701: KRX100 나머지 ※ 업종코드 참고'}
    ]
},

'ka20019': {
    'url': 'https://api.kiwoom.com/api/dostk/chart',
    'title': '업종년봉조회요청',
    'body': [
        {'key': 'inds_cd', 'name': '업종코드', 'type': 'string', 'required': True, 'length': 3, 'description': '001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주 101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701: KRX100 나머지 ※ 업종코드 참고'},
        {'key': 'base_dt', 'name': '기준일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'}
    ]
},

'ka20068': {
    'url': 'https://api.kiwoom.com/api/dostk/slb',
    'title': '대차거래추이요청(종목별)',
    'body': [
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'all_tp', 'name': '전체구분', 'type': 'string', 'required': False, 'length': 1, 'description': '0:종목코드 입력종목만 표시'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka30001': {
    'url': 'https://api.kiwoom.com/api/dostk/elw',
    'title': 'ELW가격급등락요청',
    'body': [
        {'key': 'flu_tp', 'name': '등락구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:급등, 2:급락'},
        {'key': 'tm_tp', 'name': '시간구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:분전, 2:일전'},
        {'key': 'tm', 'name': '시간', 'type': 'string', 'required': True, 'length': 2, 'description': '분 혹은 일입력 (예 1, 3, 5)'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 4, 'description': '0:전체, 10:만주이상, 50:5만주이상, 100:10만주이상, 300:30만주이상, 500:50만주이상, 1000:백만주이상'},
        {'key': 'isscomp_cd', 'name': '발행사코드', 'type': 'string', 'required': True, 'length': 12, 'description': '전체:000000000000, 한국투자증권:3, 미래대우:5, 신영:6, NK투자증권:12, KB증권:17'},
        {'key': 'bsis_aset_cd', 'name': '기초자산코드', 'type': 'string', 'required': True, 'length': 12, 'description': '전체:000000000000, KOSPI200:201, KOSDAQ150:150, 삼성전자:005930, KT:030200..'},
        {'key': 'rght_tp', 'name': '권리구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:콜, 002:풋, 003:DC, 004:DP, 005:EX, 006:조기종료콜, 007:조기종료풋'},
        {'key': 'lpcd', 'name': 'LP코드', 'type': 'string', 'required': True, 'length': 12, 'description': '전체:000000000000, 한국투자증권:3, 미래대우:5, 신영:6, NK투자증권:12, KB증권:17'},
        {'key': 'trde_end_elwskip', 'name': '거래종료ELW제외', 'type': 'string', 'required': True, 'length': 1, 'description': '0:포함, 1:제외'}
    ]
},

'ka30002': {
    'url': 'https://api.kiwoom.com/api/dostk/elw',
    'title': '거래원별ELW순매매상위요청',
    'body': [
        {'key': 'isscomp_cd', 'name': '발행사코드', 'type': 'string', 'required': True, 'length': 3, 'description': '3자리, 영웅문4 0273화면참조 (교보:001, 신한금융투자:002, 한국투자증권:003, 대신:004, 미래대우:005, ,,,)'},
        {'key': 'trde_qty_tp', 'name': '거래량구분', 'type': 'string', 'required': True, 'length': 4, 'description': '0:전체, 5:5천주, 10:만주, 50:5만주, 100:10만주, 500:50만주, 1000:백만주'},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:순매수, 2:순매도'},
        {'key': 'dt', 'name': '기간', 'type': 'string', 'required': True, 'length': 2, 'description': '1:전일, 5:5일, 10:10일, 40:40일, 60:60일'},
        {'key': 'trde_end_elwskip', 'name': '거래종료ELW제외', 'type': 'string', 'required': True, 'length': 1, 'description': '0:포함, 1:제외'}
    ]
},

'ka30003': {
    'url': 'https://api.kiwoom.com/api/dostk/elw',
    'title': 'ELWLP보유일별추이요청',
    'body': [
        {'key': 'bsis_aset_cd', 'name': '기초자산코드', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'base_dt', 'name': '기준일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'}
    ]
},

'ka30004': {
    'url': 'https://api.kiwoom.com/api/dostk/elw',
    'title': 'ELW괴리율요청',
    'body': [
        {'key': 'isscomp_cd', 'name': '발행사코드', 'type': 'string', 'required': True, 'length': 12, 'description': '전체:000000000000, 한국투자증권:3, 미래대우:5, 신영:6, NK투자증권:12, KB증권:17'},
        {'key': 'bsis_aset_cd', 'name': '기초자산코드', 'type': 'string', 'required': True, 'length': 12, 'description': '전체:000000000000, KOSPI200:201, KOSDAQ150:150, 삼성전자:005930, KT:030200..'},
        {'key': 'rght_tp', 'name': '권리구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000: 전체, 001: 콜, 002: 풋, 003: DC, 004: DP, 005: EX, 006: 조기종료콜, 007: 조기종료풋'},
        {'key': 'lpcd', 'name': 'LP코드', 'type': 'string', 'required': True, 'length': 12, 'description': '전체:000000000000, 한국투자증권:3, 미래대우:5, 신영:6, NK투자증권:12, KB증권:17'},
        {'key': 'trde_end_elwskip', 'name': '거래종료ELW제외', 'type': 'string', 'required': True, 'length': 1, 'description': '1:거래종료ELW제외, 0:거래종료ELW포함'}
    ]
},

'ka30005': {
    'url': 'https://api.kiwoom.com/api/dostk/elw',
    'title': 'ELW조건검색요청',
    'body': [
        {'key': 'isscomp_cd', 'name': '발행사코드', 'type': 'string', 'required': True, 'length': 12, 'description': '12자리입력(전체:000000000000, 한국투자증권:000,,,3, 미래대우:000,,,5, 신영:000,,,6, NK투자증권:000,,,12, KB증권:000,,,17)'},
        {'key': 'bsis_aset_cd', 'name': '기초자산코드', 'type': 'string', 'required': True, 'length': 12, 'description': '전체일때만 12자리입력(전체:000000000000, KOSPI200:201, KOSDAQ150:150, 삼정전자:005930, KT:030200,,)'},
        {'key': 'rght_tp', 'name': '권리구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:콜, 2:풋, 3:DC, 4:DP, 5:EX, 6:조기종료콜, 7:조기종료풋'},
        {'key': 'lpcd', 'name': 'LP코드', 'type': 'string', 'required': True, 'length': 12, 'description': '전체일때만 12자리입력(전체:000000000000, 한국투자증권:003, 미래대우:005, 신영:006, NK투자증권:012, KB증권:017)'},
        {'key': 'sort_tp', 'name': '정렬구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:정렬없음, 1:상승율순, 2:상승폭순, 3:하락율순, 4:하락폭순, 5:거래량순, 6:거래대금순, 7:잔존일순'}
    ]
},

'ka30009': {
    'url': 'https://api.kiwoom.com/api/dostk/elw',
    'title': 'ELW등락율순위요청',
    'body': [
        {'key': 'sort_tp', 'name': '정렬구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:상승률, 2:상승폭, 3:하락률, 4:하락폭'},
        {'key': 'rght_tp', 'name': '권리구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:콜, 002:풋, 003:DC, 004:DP, 006:조기종료콜, 007:조기종료풋'},
        {'key': 'trde_end_skip', 'name': '거래종료제외', 'type': 'string', 'required': True, 'length': 1, 'description': '1:거래종료제외, 0:거래종료포함'}
    ]
},

'ka30010': {
    'url': 'https://api.kiwoom.com/api/dostk/elw',
    'title': 'ELW잔량순위요청',
    'body': [
        {'key': 'sort_tp', 'name': '정렬구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:순매수잔량상위, 2: 순매도 잔량상위'},
        {'key': 'rght_tp', 'name': '권리구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000: 전체, 001: 콜, 002: 풋, 003: DC, 004: DP, 006: 조기종료콜, 007: 조기종료풋'},
        {'key': 'trde_end_skip', 'name': '거래종료제외', 'type': 'string', 'required': True, 'length': 1, 'description': '1:거래종료제외, 0:거래종료포함'}
    ]
},

'ka30011': {
    'url': 'https://api.kiwoom.com/api/dostk/elw',
    'title': 'ELW근접율요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka30012': {
    'url': 'https://api.kiwoom.com/api/dostk/elw',
    'title': 'ELW종목상세정보요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka40001': {
    'url': 'https://api.kiwoom.com/api/dostk/etf',
    'title': 'ETF수익율요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
        {'key': 'etfobjt_idex_cd', 'name': 'ETF대상지수코드', 'type': 'string', 'required': True, 'length': 3, 'description': ''},
        {'key': 'dt', 'name': '기간', 'type': 'string', 'required': True, 'length': 1, 'description': '0:1주, 1:1달, 2:6개월, 3:1년'}
    ]
},

'ka40002': {
    'url': 'https://api.kiwoom.com/api/dostk/etf',
    'title': 'ETF종목정보요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka40003': {
    'url': 'https://api.kiwoom.com/api/dostk/etf',
    'title': 'ETF일별추이요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka40004': {
    'url': 'https://api.kiwoom.com/api/dostk/etf',
    'title': 'ETF전체시세요청',
    'body': [
        {'key': 'txon_type', 'name': '과세유형', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:비과세, 2:보유기간과세, 3:회사형, 4:외국, 5:비과세해외(보유기간관세)'},
        {'key': 'navpre', 'name': 'NAV대비', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:NAV > 전일종가, 2:NAV < 전일종가'},
        {'key': 'mngmcomp', 'name': '운용사', 'type': 'string', 'required': True, 'length': 4, 'description': '0000:전체, 3020:KODEX(삼성), 3027:KOSEF(키움), 3191:TIGER(미래에셋), 3228:KINDEX(한국투자), 3023:KStar(KB), 3022:아리랑(한화), 9999:기타운용사'},
        {'key': 'txon_yn', 'name': '과세여부', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:과세, 2:비과세'},
        {'key': 'trace_idex', 'name': '추적지수', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT, 3:통합'}
    ]
},

'ka40006': {
    'url': 'https://api.kiwoom.com/api/dostk/etf',
    'title': 'ETF시간대별추이요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka40007': {
    'url': 'https://api.kiwoom.com/api/dostk/etf',
    'title': 'ETF시간대별체결요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka40008': {
    'url': 'https://api.kiwoom.com/api/dostk/etf',
    'title': 'ETF일자별체결요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka40009': {
    'url': 'https://api.kiwoom.com/api/dostk/etf',
    'title': 'ETF시간대별체결요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka40010': {
    'url': 'https://api.kiwoom.com/api/dostk/etf',
    'title': 'ETF시간대별추이요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
    ]
},

'ka90001': {
    'url': 'https://api.kiwoom.com/api/dostk/thme',
    'title': '테마그룹별요청',
    'body': [
        {'key': 'qry_tp', 'name': '검색구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체검색, 1:테마검색, 2:종목검색'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': False, 'length': 6, 'description': '검색하려는 종목코드'},
        {'key': 'date_tp', 'name': '날짜구분', 'type': 'string', 'required': True, 'length': 2, 'description': 'n일전 (1일 ~ 99일 날짜입력)'},
        {'key': 'thema_nm', 'name': '테마명', 'type': 'string', 'required': False, 'length': 50, 'description': '검색하려는 테마명'},
        {'key': 'flu_pl_amt_tp', 'name': '등락수익구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:상위기간수익률, 2:하위기간수익률, 3:상위등락률, 4:하위등락률'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka90002': {
    'url': 'https://api.kiwoom.com/api/dostk/thme',
    'title': '테마구성종목요청',
    'body': [
        {'key': 'date_tp', 'name': '날짜구분', 'type': 'string', 'required': False, 'length': 1, 'description': '1일 ~ 99일 날짜입력'},
        {'key': 'thema_grp_cd', 'name': '테마그룹코드', 'type': 'string', 'required': True, 'length': 6, 'description': '테마그룹코드 번호'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka90003': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '프로그램순매수상위50요청',
    'body': [
        {'key': 'trde_upper_tp', 'name': '매매상위구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:순매도상위, 2:순매수상위'},
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': True, 'length': 2, 'description': '1:금액, 2:수량'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 10, 'description': 'P00101:코스피, P10102:코스닥'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka90004': {
    'url': 'https://api.kiwoom.com/api/dostk/stkinfo',
    'title': '종목별프로그램매매현황요청',
    'body': [
        {'key': 'dt', 'name': '일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 10, 'description': 'P00101:코스피, P10102:코스닥'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka90005': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '프로그램매매추이요청 시간대별',
    'body': [
        {'key': 'date', 'name': '날짜', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:금액(백만원), 2:수량(천주)'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 10, 'description': '코스피- 거래소구분값 1일경우:P00101, 2일경우:P001_NX01, 3일경우:P001_AL01 코스닥- 거래소구분값 1일경우:P10102, 2일경우:P101_NX02, 3일경우:P101_AL02'},
        {'key': 'min_tic_tp', 'name': '분틱구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:틱, 1:분'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka90006': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '프로그램매매차익잔고추이요청',
    'body': [
        {'key': 'date', 'name': '날짜', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka90007': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '프로그램매매누적추이요청',
    'body': [
        {'key': 'date', 'name': '날짜', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD (종료일기준 1년간 데이터만 조회가능)'},
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:금액, 2:수량'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 5, 'description': '0:코스피 , 1:코스닥'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT, 3:통합'}
    ]
},

'ka90008': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '종목시간별프로그램매매추이요청',
    'body': [
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:금액, 2:수량'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'date', 'name': '날짜', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'}
    ]
},

'ka90009': {
    'url': 'https://api.kiwoom.com/api/dostk/rkinfo',
    'title': '외국인기관매매상위요청',
    'body': [
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '000:전체, 001:코스피, 101:코스닥'},
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:금액(천만), 2:수량(천)'},
        {'key': 'qry_dt_tp', 'name': '조회일자구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:조회일자 미포함, 1:조회일자 포함'},
        {'key': 'date', 'name': '날짜', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD (연도4자리, 월 2자리, 일 2자리 형식)'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT, 3:통합'}
    ]
},

'ka90010': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '프로그램매매추이요청 일자별',
    'body': [
        {'key': 'date', 'name': '날짜', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:금액(백만원), 2:수량(천주)'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 10, 'description': '코스피- 거래소구분값 1일경우:P00101, 2일경우:P001_NX01, 3일경우:P001_AL01 코스닥- 거래소구분값 1일경우:P10102, 2일경우:P101_NX02, 3일경우:P001_AL02'},
        {'key': 'min_tic_tp', 'name': '분틱구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:틱, 1:분'},
        {'key': 'stex_tp', 'name': '거래소구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:KRX, 2:NXT 3.통합'}
    ]
},

'ka90012': {
    'url': 'https://api.kiwoom.com/api/dostk/slb',
    'title': '대차거래내역요청',
    'body': [
        {'key': 'dt', 'name': '일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 3, 'description': '001:코스피, 101:코스닥'}
    ]
},

'ka90013': {
    'url': 'https://api.kiwoom.com/api/dostk/mrkcond',
    'title': '종목일별프로그램매매추이요청',
    'body': [
        {'key': 'amt_qty_tp', 'name': '금액수량구분', 'type': 'string', 'required': False, 'length': 1, 'description': '1:금액, 2:수량'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 20, 'description': '거래소별 종목코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': 'date', 'name': '날짜', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD'}
    ]
},

'kt00001': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '예수금상세현황요청',
    'body': [
        {'key': 'qry_tp', 'name': '조회구분', 'type': 'string', 'required': True, 'length': 1, 'description': '3:추정조회, 2:일반조회'}
    ]
},

'kt00002': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '일별추정예탁자산현황요청',
    'body': [
        {'key': 'start_dt', 'name': '시작조회기간', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'end_dt', 'name': '종료조회기간', 'type': 'string', 'required': True, 'length': 8, 'description': 'YYYYMMDD'}
    ]
},

'kt00003': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '추정자산조회요청',
    'body': [
        {'key': 'qry_tp', 'name': '상장폐지조회구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:상장폐지종목제외'}
    ]
},

'kt00004': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '계좌평가현황요청',
    'body': [
        {'key': 'qry_tp', 'name': '상장폐지조회구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:상장폐지종목제외'},
        {'key': 'dmst_stex_tp', 'name': '국내거래소구분', 'type': 'string', 'required': True, 'length': 6, 'description': 'KRX:한국거래소,NXT:넥스트트레이드'}
    ]
},

'kt00005': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '체결잔고요청',
    'body': [
        {'key': 'dmst_stex_tp', 'name': '국내거래소구분', 'type': 'string', 'required': True, 'length': 6, 'description': 'KRX:한국거래소,NXT:넥스트트레이드'}
    ]
},

'kt00007': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '계좌별주문체결내역상세요청',
    'body': [
        {'key': 'ord_dt', 'name': '주문일자', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'qry_tp', 'name': '조회구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:주문순, 2:역순, 3:미체결, 4:체결내역만'},
        {'key': 'stk_bond_tp', 'name': '주식채권구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:주식, 2:채권'},
        {'key': 'sell_tp', 'name': '매도수구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:매도, 2:매수'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': False, 'length': 12, 'description': '공백허용 (공백일때 전체종목)'},
        {'key': 'fr_ord_no', 'name': '시작주문번호', 'type': 'string', 'required': False, 'length': 7, 'description': '공백허용 (공백일때 전체주문)'},
        {'key': 'dmst_stex_tp', 'name': '국내거래소구분', 'type': 'string', 'required': True, 'length': 6, 'description': '%:(전체),KRX:한국거래소,NXT:넥스트트레이드,SOR:최선주문집행'}
    ]
},

'kt00008': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '계좌별익일결제예정내역요청',
    'body': [
        {'key': 'strt_dcd_seq', 'name': '시작결제번호', 'type': 'string', 'required': False, 'length': 7, 'description': ''}
    ]
},

'kt00009': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '계좌별주문체결현황요청',
    'body': [
        {'key': 'ord_dt', 'name': '주문일자', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD'},
        {'key': 'stk_bond_tp', 'name': '주식채권구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:주식, 2:채권'},
        {'key': 'mrkt_tp', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:코스피, 2:코스닥, 3:OTCBB, 4:ECN'},
        {'key': 'sell_tp', 'name': '매도수구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:매도, 2:매수'},
        {'key': 'qry_tp', 'name': '조회구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:체결'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': False, 'length': 12, 'description': '전문 조회할 종목코드'},
        {'key': 'fr_ord_no', 'name': '시작주문번호', 'type': 'string', 'required': False, 'length': 7, 'description': ''},
        {'key': 'dmst_stex_tp', 'name': '국내거래소구분', 'type': 'string', 'required': True, 'length': 6, 'description': '%:(전체),KRX:한국거래소,NXT:넥스트트레이드,SOR:최선주문집행'}
    ]
},

'kt00010': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '주문인출가능금액요청',
    'body': [
        {'key': 'io_amt', 'name': '입출금액', 'type': 'string', 'required': False, 'length': 12, 'description': ''},
        {'key': 'stk_cd', 'name': '종목번호', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:매도, 2:매수'},
        {'key': 'trde_qty', 'name': '매매수량', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
        {'key': 'uv', 'name': '매수가격', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
        {'key': 'exp_buy_unp', 'name': '예상매수단가', 'type': 'string', 'required': False, 'length': 10, 'description': ''}
    ]
},

'kt00011': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '증거금율별주문가능수량조회요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목번호', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'uv', 'name': '매수가격', 'type': 'string', 'required': False, 'length': 10, 'description': ''}
    ]
},

'kt00012': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '신용보증금율별주문가능수량조회요청',
    'body': [
        {'key': 'stk_cd', 'name': '종목번호', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'uv', 'name': '매수가격', 'type': 'string', 'required': False, 'length': 10, 'description': ''}
    ]
},

'kt00013': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '증거금세부내역조회요청',
    'body': [
    ]
},

'kt00015': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '위탁종합거래내역요청',
    'body': [
        {'key': 'strt_dt', 'name': '시작일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        {'key': 'end_dt', 'name': '종료일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        {'key': 'tp', 'name': '구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체,1:입출금,2:입출고,3:매매,4:매수,5:매도,6:입금,7:출금,A:예탁담보대출입금,B:매도담보대출입금,C:현금상환(융자,담보상환),F:환전,M:입출금+환전,G:외화매수,H:외화매도,I:환전정산입금,J:환전정산출금'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': False, 'length': 12, 'description': ''},
        {'key': 'crnc_cd', 'name': '통화코드', 'type': 'string', 'required': False, 'length': 3, 'description': ''},
        {'key': 'gds_tp', 'name': '상품구분', 'type': 'string', 'required': True, 'length': 1, 'description': '0:전체, 1:국내주식, 2:수익증권, 3:해외주식, 4:금융상품'},
        {'key': 'frgn_stex_code', 'name': '해외거래소코드', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
        {'key': 'dmst_stex_tp', 'name': '국내거래소구분', 'type': 'string', 'required': True, 'length': 6, 'description': '%:(전체),KRX:한국거래소,NXT:넥스트트레이드'}
    ]
},

'kt00016': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '일별계좌수익률상세현황요청',
    'body': [
        {'key': 'fr_dt', 'name': '평가시작일', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        {'key': 'to_dt', 'name': '평가종료일', 'type': 'string', 'required': True, 'length': 8, 'description': ''}
    ]
},

'kt00017': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '계좌별당일현황요청',
    'body': [
    ]
},

'kt00018': {
    'url': 'https://api.kiwoom.com/api/dostk/acnt',
    'title': '계좌평가잔고내역요청',
    'body': [
        {'key': 'qry_tp', 'name': '조회구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1:합산, 2:개별'},
        {'key': 'dmst_stex_tp', 'name': '국내거래소구분', 'type': 'string', 'required': True, 'length': 6, 'description': 'KRX:한국거래소,NXT:넥스트트레이드'}
    ]
},

'kt10000': {
    'url': 'https://api.kiwoom.com/api/dostk/ordr',
    'title': '주식 매수주문',
    'body': [
        {'key': 'dmst_stex_tp', 'name': '국내거래소구분', 'type': 'string', 'required': True, 'length': 3, 'description': 'KRX,NXT,SOR'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'ord_qty', 'name': '주문수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'ord_uv', 'name': '주문단가', 'type': 'string', 'required': False, 'length': 12, 'description': ''},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 2, 'description': '0:보통 , 3:시장가 , 5:조건부지정가 , 81:장마감후시간외 , 61:장시작전시간외, 62:시간외단일가 , 6:최유리지정가 , 7:최우선지정가 , 10:보통(IOC) , 13:시장가(IOC) , 16:최유리(IOC) , 20:보통(FOK) , 23:시장가(FOK) , 26:최유리(FOK) , 28:스톱지정가,29:중간가,30:중간가(IOC),31:중간가(FOK)'},
        {'key': 'cond_uv', 'name': '조건단가', 'type': 'string', 'required': False, 'length': 12, 'description': ''}
    ]
},

'kt10001': {
    'url': 'https://api.kiwoom.com/api/dostk/ordr',
    'title': '주식 매도주문',
    'body': [
        {'key': 'dmst_stex_tp', 'name': '국내거래소구분', 'type': 'string', 'required': True, 'length': 3, 'description': 'KRX,NXT,SOR'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'ord_qty', 'name': '주문수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'ord_uv', 'name': '주문단가', 'type': 'string', 'required': False, 'length': 12, 'description': ''},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 2, 'description': '0:보통 , 3:시장가 , 5:조건부지정가 , 81:장마감후시간외 , 61:장시작전시간외, 62:시간외단일가 , 6:최유리지정가 , 7:최우선지정가 , 10:보통(IOC) , 13:시장가(IOC) , 16:최유리(IOC) , 20:보통(FOK) , 23:시장가(FOK) , 26:최유리(FOK) , 28:스톱지정가,29:중간가,30:중간가(IOC),31:중간가(FOK)'},
        {'key': 'cond_uv', 'name': '조건단가', 'type': 'string', 'required': False, 'length': 12, 'description': ''}
    ]
},

'kt10002': {
    'url': 'https://api.kiwoom.com/api/dostk/ordr',
    'title': '주식 정정주문',
    'body': [
        {'key': 'dmst_stex_tp', 'name': '국내거래소구분', 'type': 'string', 'required': True, 'length': 3, 'description': 'KRX,NXT,SOR'},
        {'key': 'orig_ord_no', 'name': '원주문번호', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'mdfy_qty', 'name': '정정수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'mdfy_uv', 'name': '정정단가', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'mdfy_cond_uv', 'name': '정정조건단가', 'type': 'string', 'required': False, 'length': 12, 'description': ''}
    ]
},

'kt10003': {
    'url': 'https://api.kiwoom.com/api/dostk/ordr',
    'title': '주식 취소주문',
    'body': [
        {'key': 'dmst_stex_tp', 'name': '국내거래소구분', 'type': 'string', 'required': True, 'length': 3, 'description': 'KRX,NXT,SOR'},
        {'key': 'orig_ord_no', 'name': '원주문번호', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'cncl_qty', 'name': '취소수량', 'type': 'string', 'required': True, 'length': 12, 'description': '0 입력시 잔량 전부 취소'}
    ]
},

'kt10006': {
    'url': 'https://api.kiwoom.com/api/dostk/crdordr',
    'title': '신용 매수주문',
    'body': [
        {'key': 'dmst_stex_tp', 'name': '국내거래소구분', 'type': 'string', 'required': True, 'length': 3, 'description': 'KRX,NXT,SOR'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'ord_qty', 'name': '주문수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'ord_uv', 'name': '주문단가', 'type': 'string', 'required': False, 'length': 12, 'description': ''},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 2, 'description': '0:보통 , 3:시장가 , 5:조건부지정가 , 81:장마감후시간외 , 61:장시작전시간외, 62:시간외단일가 , 6:최유리지정가 , 7:최우선지정가 , 10:보통(IOC) , 13:시장가(IOC) , 16:최유리(IOC) , 20:보통(FOK) , 23:시장가(FOK) , 26:최유리(FOK) , 28:스톱지정가,29:중간가,30:중간가(IOC),31:중간가(FOK)'},
        {'key': 'cond_uv', 'name': '조건단가', 'type': 'string', 'required': False, 'length': 12, 'description': ''}
    ]
},

'kt10007': {
    'url': 'https://api.kiwoom.com/api/dostk/crdordr',
    'title': '신용 매도주문',
    'body': [
        {'key': 'dmst_stex_tp', 'name': '국내거래소구분', 'type': 'string', 'required': True, 'length': 3, 'description': 'KRX,NXT,SOR'},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'ord_qty', 'name': '주문수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'ord_uv', 'name': '주문단가', 'type': 'string', 'required': False, 'length': 12, 'description': ''},
        {'key': 'trde_tp', 'name': '매매구분', 'type': 'string', 'required': True, 'length': 2, 'description': '0:보통 , 3:시장가 , 5:조건부지정가 , 81:장마감후시간외 , 61:장시작전시간외, 62:시간외단일가 , 6:최유리지정가 , 7:최우선지정가 , 10:보통(IOC) , 13:시장가(IOC) , 16:최유리(IOC) , 20:보통(FOK) , 23:시장가(FOK) , 26:최유리(FOK) , 28:스톱지정가,29:중간가,30:중간가(IOC),31:중간가(FOK)'},
        {'key': 'crd_deal_tp', 'name': '신용거래구분', 'type': 'string', 'required': True, 'length': 2, 'description': '33:융자 , 99:융자합'},
        {'key': 'crd_loan_dt', 'name': '대출일', 'type': 'string', 'required': False, 'length': 8, 'description': 'YYYYMMDD(융자일경우필수)'},
        {'key': 'cond_uv', 'name': '조건단가', 'type': 'string', 'required': False, 'length': 12, 'description': ''}
    ]
},

'kt10008': {
    'url': 'https://api.kiwoom.com/api/dostk/crdordr',
    'title': '신용 정정주문',
    'body': [
        {'key': 'dmst_stex_tp', 'name': '국내거래소구분', 'type': 'string', 'required': True, 'length': 3, 'description': 'KRX,NXT,SOR'},
        {'key': 'orig_ord_no', 'name': '원주문번호', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'mdfy_qty', 'name': '정정수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'mdfy_uv', 'name': '정정단가', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'mdfy_cond_uv', 'name': '정정조건단가', 'type': 'string', 'required': False, 'length': 12, 'description': ''}
    ]
},

'kt10009': {
    'url': 'https://api.kiwoom.com/api/dostk/crdordr',
    'title': '신용 취소주문',
    'body': [
        {'key': 'dmst_stex_tp', 'name': '국내거래소구분', 'type': 'string', 'required': True, 'length': 3, 'description': 'KRX,NXT,SOR'},
        {'key': 'orig_ord_no', 'name': '원주문번호', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
        {'key': 'stk_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
        {'key': 'cncl_qty', 'name': '취소수량', 'type': 'string', 'required': True, 'length': 12, 'description': '0 입력시 잔량 전부 취소'}
    ]
},

'00': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '주문체결',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시  0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지  해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': ''},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'04': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '잔고',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시   0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지  해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 104, 'description': ''},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0A': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '주식기세',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시  0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지  해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0B': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '주식체결',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0C': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '주식우선호가',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0D': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '주식호가잔량',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0E': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '주식시간외호가',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0F': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '주식당일거래원',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0G': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': 'ETF NAV',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0H': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '주식예상체결',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0J': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '업종지수',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0U': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '업종등락',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0g': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '주식종목정보',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0m': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': 'ELW 이론가',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0s': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '장시작시간',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0u': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': 'ELW 지표',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'0w': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': '종목프로그램매매',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
},

'1h': {
    'url': 'wss://api.kiwoom.com:10000/api/dostk/websocket',
    'title': 'VI발동/해제',
    'body': [
        {'key': 'trnm', 'name': '서비스명', 'type': 'string', 'required': True, 'length': 10, 'description': 'REG : 등록 , REMOVE : 해지'},
        {'key': 'grp_no', 'name': '그룹번호', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
        {'key': 'refresh', 'name': '기존등록유지여부', 'type': 'string', 'required': True, 'length': 1, 'description': '등록(REG)시 0:기존유지안함 1:기존유지(Default)  0일경우 기존등록한 item/type은 해지, 1일경우 기존등록한 item/type 유지 해지(REMOVE)시 값 불필요'},
        {'key': 'data', 'name': '실시간 등록 리스트', 'type': 'list', 'required': False, 'length': None, 'description': ''},
        {'key': '- item', 'name': '실시간 등록 요소', 'type': 'string', 'required': False, 'length': 100, 'description': '거래소별 종목코드, 업종코드 (KRX:039490,NXT:039490_NX,SOR:039490_AL)'},
        {'key': '- type', 'name': '실시간 항목', 'type': 'string', 'required': True, 'length': 2, 'description': 'TR 명(0A,0B....)'}
    ]
}

}

# API 유효성 검증 함수들
def get_request_definition(api_id: str) -> Dict[str, Any]:
    """
    API ID로 해당 API의 정의 정보를 반환합니다.
    
    Args:
        api_id: 조회할 API ID
        
    Returns:
        Dict[str, Any]: API 정의 정보
        
    Raises:
        KeyError: 존재하지 않는 API ID인 경우
    """
    if api_id not in KIWOOM_REQUEST_DEF:
        raise KeyError(f"API ID '{api_id}'가 정의되지 않았습니다.")
    
    return KIWOOM_REQUEST_DEF[api_id]

def get_required_fields(api_id: str) -> List[str]:
    """
    특정 API의 필수 필드 목록을 반환합니다.
    
    Args:
        api_id: 조회할 API ID
        
    Returns:
        List[str]: 필수 필드명 목록
    """
    api_def = get_request_definition(api_id)
    return [field['key'] for field in api_def.get('body', []) if field.get('required', False)]