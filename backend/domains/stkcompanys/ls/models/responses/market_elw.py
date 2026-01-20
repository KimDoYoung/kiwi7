# Auto-generated
from typing import Any, Dict, List

MARKET_ELW_RESPONSES = {
    'ESN': {
        'tr_cd': 'ESN',
        'title': '뉴ELW투자지표민감도',
        'fields': [
            {
                'key': 'time',
                'length': '	6',
                'name': '시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'theoryprice',
                'length': '	10.2',
                'name': '장중이론가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'delt',
                'length': '	7.6',
                'name': '델타',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'gama',
                'length': '	7.6',
                'name': '감마',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ceta',
                'length': '	12.6',
                'name': '세타',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'vega',
                'length': '	12.6',
                'name': '베가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'rhox',
                'length': '	12.6',
                'name': '로우',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'impv',
                'length': '	5.2',
                'name': '내재변동성',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'egearing',
                'length': '	8.2',
                'name': 'E.기어링',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': '	6',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'elwclose',
                'length': 8,
                'name': 'ELW현재가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sign',
                'length': 1,
                'name': 'ELW전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': 8,
                'name': 'ELW전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'date',
                'length': 8,
                'name': '일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tickvalue',
                'length': 10.2,
                'name': '틱환산',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_impv',
                'length': '	5.2',
                'name': 'LP내재변동성',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'Ys3': {
        'tr_cd': 'Ys3',
        'title': 'ELW예상체결',
        'fields': [
            {
                'key': 'hotime',
                'length': '	6',
                'name': '호가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'yeprice',
                'length': '	8',
                'name': '예상체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'yevolume',
                'length': '	12',
                'name': '예상체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jnilysign',
                'length': '	1',
                'name': '예상체결가전일종가대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jnilchange',
                'length': '	8',
                'name': '예상체결가전일종가대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jnilydrate',
                'length': '	6.2',
                'name': '예상체결가전일종가등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'yofferho0',
                'length': '	8',
                'name': '예상매도호가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ybidho0',
                'length': '	8',
                'name': '예상매수호가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'yofferrem0',
                'length': '	12',
                'name': '예상매도호가수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ybidrem0',
                'length': '	12',
                'name': '예상매수호가수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': '	6',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'h2_': {
        'tr_cd': 'h2_',
        'title': 'ELW장전시간외호가잔량',
        'fields': [
            {
                'key': 'hotime',
                'length': '	6',
                'name': '호가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tmofferrem',
                'length': '	12',
                'name': '시간외매도잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tmbidrem',
                'length': '	12',
                'name': '시간외매수잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'pretmoffercha',
                'length': '	12',
                'name': '시간외매도수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'pretmbidcha',
                'length': '	12',
                'name': '시간외매수수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': '	6',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'h3_': {
        'tr_cd': 'h3_',
        'title': 'ELW호가잔량',
        'fields': [
            {
                'key': 'hotime',
                'length': '	6',
                'name': '호가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho1',
                'length': '	7',
                'name': '매도호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho1',
                'length': '	7',
                'name': '매수호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem1',
                'length': '	9',
                'name': '매도호가잔량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem1',
                'length': '	9',
                'name': '매수호가잔량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_offerho1',
                'length': '	9',
                'name': 'LP매도호가수량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_bidho1',
                'length': '	9',
                'name': 'LP매수호가수량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho2',
                'length': '	7',
                'name': '매도호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho2',
                'length': '	7',
                'name': '매수호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem2',
                'length': '	9',
                'name': '매도호가잔량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem2',
                'length': '	9',
                'name': '매수호가잔량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_offerho2',
                'length': '	9',
                'name': 'LP매도호가수량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_bidho2',
                'length': '	9',
                'name': 'LP매수호가수량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho3',
                'length': '	7',
                'name': '매도호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho3',
                'length': '	7',
                'name': '매수호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem3',
                'length': '	9',
                'name': '매도호가잔량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem3',
                'length': '	9',
                'name': '매수호가잔량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_offerho3',
                'length': '	9',
                'name': 'LP매도호가수량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_bidho3',
                'length': '	9',
                'name': 'LP매수호가수량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho4',
                'length': '	7',
                'name': '매도호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho4',
                'length': '	7',
                'name': '매수호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem4',
                'length': '	9',
                'name': '매도호가잔량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem4',
                'length': '	9',
                'name': '매수호가잔량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_offerho4',
                'length': '	9',
                'name': 'LP매도호가수량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_bidho4',
                'length': '	9',
                'name': 'LP매수호가수량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho5',
                'length': '	7',
                'name': '매도호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho5',
                'length': '	7',
                'name': '매수호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem5',
                'length': '	9',
                'name': '매도호가잔량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem5',
                'length': '	9',
                'name': '매수호가잔량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_offerho5',
                'length': '	9',
                'name': 'LP매도호가수량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_bidho5',
                'length': '	9',
                'name': 'LP매수호가수량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho6',
                'length': '	7',
                'name': '매도호가6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho6',
                'length': '	7',
                'name': '매수호가6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem6',
                'length': '	9',
                'name': '매도호가잔량6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem6',
                'length': '	9',
                'name': '매수호가잔량6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_offerho6',
                'length': '	9',
                'name': 'LP매도호가수량6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_bidho6',
                'length': '	9',
                'name': 'LP매수호가수량6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho7',
                'length': '	7',
                'name': '매도호가7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho7',
                'length': '	7',
                'name': '매수호가7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem7',
                'length': '	9',
                'name': '매도호가잔량7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem7',
                'length': '	9',
                'name': '매수호가잔량7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_offerho7',
                'length': '	9',
                'name': 'LP매도호가수량7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_bidho7',
                'length': '	9',
                'name': 'LP매수호가수량7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho8',
                'length': '	7',
                'name': '매도호가8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho8',
                'length': '	7',
                'name': '매수호가8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem8',
                'length': '	9',
                'name': '매도호가잔량8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem8',
                'length': '	9',
                'name': '매수호가잔량8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_offerho8',
                'length': '	9',
                'name': 'LP매도호가수량8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_bidho8',
                'length': '	9',
                'name': 'LP매수호가수량8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho9',
                'length': '	7',
                'name': '매도호가9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho9',
                'length': '	7',
                'name': '매수호가9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem9',
                'length': '	9',
                'name': '매도호가잔량9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem9',
                'length': '	9',
                'name': '매수호가잔량9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_offerho9',
                'length': '	9',
                'name': 'LP매도호가수량9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_bidho9',
                'length': '	9',
                'name': 'LP매수호가수량9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho10',
                'length': '	7',
                'name': '매도호가10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho10',
                'length': '	7',
                'name': '매수호가10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem10',
                'length': '	9',
                'name': '매도호가잔량10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem10',
                'length': '	9',
                'name': '매수호가잔량10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_offerho10',
                'length': '	9',
                'name': 'LP매도호가수량10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lp_bidho10',
                'length': '	9',
                'name': 'LP매수호가수량10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totofferrem',
                'length': '	9',
                'name': '총매도호가잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidrem',
                'length': '	9',
                'name': '총매수호가잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'donsigubun',
                'length': '	1',
                'name': '동시호가구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'spread',
                'length': '	6.2',
                'name': '스프레드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': '	6',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'k1_': {
        'tr_cd': 'k1_',
        'title': 'ELW거래원',
        'fields': [
            {
                'key': 'offerno1',
                'length': '	3',
                'name': '매도증권사코드1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno1',
                'length': '	3',
                'name': '매수증권사코드1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad1',
                'length': '	6',
                'name': '매도회원사명1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad1',
                'length': '	6',
                'name': '매수회원사명1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol1',
                'length': '	10',
                'name': '매도거래량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsvol1',
                'length': '	10',
                'name': '매수거래량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdrate1',
                'length': '	6.2',
                'name': '매도거래량비중1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsrate1',
                'length': '	6.2',
                'name': '매도거래량비중1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdcha1',
                'length': '	10',
                'name': '매도거래량직전대비1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmscha1',
                'length': '	10',
                'name': '매수거래량직전대비1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno2',
                'length': '	3',
                'name': '매도증권사코드2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno2',
                'length': '	3',
                'name': '매수증권사코드2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad2',
                'length': '	6',
                'name': '매도회원사명2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad2',
                'length': '	6',
                'name': '매수회원사명2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol2',
                'length': '	10',
                'name': '매도거래량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsvol2',
                'length': '	10',
                'name': '매수거래량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdrate2',
                'length': '	6.2',
                'name': '매도거래량비중2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsrate2',
                'length': '	6.2',
                'name': '매수거래량비중2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdcha2',
                'length': '	10',
                'name': '매도거래량직전대비2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmscha2',
                'length': '	10',
                'name': '매수거래량직전대비2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno3',
                'length': '	3',
                'name': '매도증권사코드3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno3',
                'length': '	3',
                'name': '매수증권사코드3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad3',
                'length': '	6',
                'name': '매도회원사명3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad3',
                'length': '	6',
                'name': '매수회원사명3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol3',
                'length': '	10',
                'name': '매도거래량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsvol3',
                'length': '	10',
                'name': '매수거래량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdrate3',
                'length': '	6.2',
                'name': '매도거래량비중3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsrate3',
                'length': '	6.2',
                'name': '매수거래량비중3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdcha3',
                'length': '	10',
                'name': '매도거래량직전대비3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmscha3',
                'length': '	10',
                'name': '매수거래량직전대비3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno4',
                'length': '	3',
                'name': '매도증권사코드4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno4',
                'length': '	3',
                'name': '매수증권사코드4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad4',
                'length': '	6',
                'name': '매도회원사명4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad4',
                'length': '	6',
                'name': '매수회원사명4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol4',
                'length': '	10',
                'name': '매도거래량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsvol4',
                'length': '	10',
                'name': '매수거래량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdrate4',
                'length': '	6.2',
                'name': '매도거래량비중4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsrate4',
                'length': '	6.2',
                'name': '매수거래량비중4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdcha4',
                'length': '	10',
                'name': '매도거래량직전대비4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmscha4',
                'length': '	10',
                'name': '매수거래량직전대비4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno5',
                'length': '	3',
                'name': '매도증권사코드5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno5',
                'length': '	3',
                'name': '매수증권사코드5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad5',
                'length': '	6',
                'name': '매도회원사명5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad5',
                'length': '	6',
                'name': '매수회원사명5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol5',
                'length': '	10',
                'name': '매도거래량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsvol5',
                'length': '	10',
                'name': '매수거래량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdrate5',
                'length': '	6.2',
                'name': '매도거래량비중5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsrate5',
                'length': '	6.2',
                'name': '매수거래량비중5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdcha5',
                'length': '	10',
                'name': '매도거래량직전대비5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmscha5',
                'length': '	10',
                'name': '매수거래량직전대비5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmdvol',
                'length': '	10',
                'name': '외국계증권사매도합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmsvol',
                'length': '	10',
                'name': '외국계증권사매수합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmdrate',
                'length': '	6.2',
                'name': '외국계증권사매도거래량비중',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmsrate',
                'length': '	6.2',
                'name': '외국계증권사매수거래량비중',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmdcha',
                'length': '	10',
                'name': '외국계증권사매도거래량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmscha',
                'length': '	10',
                'name': '외국계증권사매수거래량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': '	6',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    's2_': {
        'tr_cd': 's2_',
        'title': 'ELW우선호가',
        'fields': [
            {
                'key': 'offerho',
                'length': '	8',
                'name': '매도호가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho',
                'length': '	8',
                'name': '매수호가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': '	6',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    's3_': {
        'tr_cd': 's3_',
        'title': 'ELW체결',
        'fields': [
            {
                'key': 'chetime',
                'length': '	6',
                'name': '체결시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sign',
                'length': '	1',
                'name': '전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': '	8',
                'name': '전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'drate',
                'length': '	6.2',
                'name': '등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'price',
                'length': '	8',
                'name': '현재가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'opentime',
                'length': '	6',
                'name': '시가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'open',
                'length': '	8',
                'name': '시가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'hightime',
                'length': '	6',
                'name': '고가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'high',
                'length': '	8',
                'name': '고가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lowtime',
                'length': '	6',
                'name': '저가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low',
                'length': '	8',
                'name': '저가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cgubun',
                'length': '	1',
                'name': '체결구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cvolume',
                'length': '	8',
                'name': '체결량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volume',
                'length': '	12',
                'name': '누적거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'value',
                'length': '	12',
                'name': '누적거래대금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume',
                'length': '	12',
                'name': '매도누적체결량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdchecnt',
                'length': '	8',
                'name': '매도누적체결건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume',
                'length': '	12',
                'name': '매수누적체결량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mschecnt',
                'length': '	8',
                'name': '매수누적체결건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cpower',
                'length': '	9.2',
                'name': '체결강도',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'w_avrg',
                'length': '	8',
                'name': '가중평균가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho',
                'length': '	8',
                'name': '매도호가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho',
                'length': '	8',
                'name': '매수호가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'status',
                'length': '	2',
                'name': '장정보',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jnilvolume',
                'length': '	12',
                'name': '전일동시간대거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'premium',
                'length': '	8.2',
                'name': '프리미엄',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'moneyness',
                'length': '	1',
                'name': 'ATM구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': '	6',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lpvolume',
                'length': '	15',
                'name': 'LP보유수량',
                'required': True,
                'type': 'string'
            }
        ]
    },
    's4_': {
        'tr_cd': 's4_',
        'title': 'ELW기세',
        'fields': [
            {
                'key': 'sign',
                'length': '	1',
                'name': '전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': '	8',
                'name': '전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'drate',
                'length': '	6.2',
                'name': '등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'price',
                'length': '	8',
                'name': '현재가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'opentime',
                'length': '	6',
                'name': '시가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'open',
                'length': '	8',
                'name': '시가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'hightime',
                'length': '	6',
                'name': '고가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'high',
                'length': '	8',
                'name': '고가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lowtime',
                'length': '	6',
                'name': '저가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low',
                'length': '	8',
                'name': '저가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': '	6',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    't1950': {
        'tr_cd': 't1950',
        'title': 'ELW현재가(시세)조회',
        'blocks': {
            't1950OutBlock': {
                'fields': [{'key': 'value', 'name': '누적거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'chetime', 'name': '체결시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'recprice', 'name': '기준가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'avg', 'name': '가중평균', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jnilvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jvolume', 'name': '전일동시간거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'volumechg', 'name': '거래량차', 'type': 'float', 'length': 12, 'required': True}, {'key': 'volumediff', 'name': '거래량차등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'odiff', 'name': '시가등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'opentime', 'name': '시가시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'hdiff', 'name': '고가등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'hightime', 'name': '고가시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ldiff', 'name': '저가등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'lowtime', 'name': '저가시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'high52w', 'name': '52최고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high52wdiff', 'name': '52최고가등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high52wdate', 'name': '52최고가일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'low52w', 'name': '52최저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low52wdiff', 'name': '52최저가등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low52wdate', 'name': '52최저가일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'exhratio', 'name': '소진율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'listing', 'name': '상장주식수(천)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'memedan', 'name': '수량단위', 'type': 'string', 'length': 5, 'required': True}, {'key': 'vol', 'name': '회전율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'parity', 'name': '패리티', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'berate', 'name': '손익분기', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'gearing', 'name': '기어링', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'elwexec', 'name': '행사가', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'issueprice', 'name': '발행가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'convrate', 'name': '전환비율', 'type': 'float', 'length': 12.4, 'required': True}, {'key': 'lastdate', 'name': '최종거래일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'capt', 'name': '자본지지', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'egearing', 'name': 'e.기어링', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'premium', 'name': '프리미엄', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'spread', 'name': '스프레드', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'espread', 'name': '최대스프레드', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'theoryprice', 'name': '이론가', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'impv', 'name': '내재변동성', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'moneyness', 'name': '상태', 'type': 'string', 'length': 1, 'required': True}, {'key': 'delt', 'name': '델타', 'type': 'float', 'length': 8.6, 'required': True}, {'key': 'gama', 'name': '감마', 'type': 'float', 'length': 8.6, 'required': True}, {'key': 'vega', 'name': '베가', 'type': 'float', 'length': 13.6, 'required': True}, {'key': 'ceta', 'name': '쎄타', 'type': 'float', 'length': 13.6, 'required': True}, {'key': 'rhox', 'name': '로', 'type': 'float', 'length': 13.6, 'required': True}, {'key': 'bjandatecnt', 'name': '잔존일수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'mmsdate', 'name': '행사개시일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'mmedate', 'name': '행사종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'payday', 'name': '지급일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'listdate', 'name': '발행일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'lpmem', 'name': 'LP회원사', 'type': 'string', 'length': 20, 'required': True}, {'key': 'lp_holdvol', 'name': 'LP보유수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bcode', 'name': '기초자산코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bgubun', 'name': '기초자산구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'bprice', 'name': '기초자산현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bsign', 'name': '기초자산전일비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'bchange', 'name': '기초자산전일비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bdiff', 'name': '기초자산등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bvolume', 'name': '기초자산거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'info1', 'name': '락구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'info2', 'name': '관리/급등구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'info3', 'name': '정지/연장구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'info4', 'name': '투자/불성실구분', 'type': 'string', 'length': 12, 'required': True}, {'key': 'janginfo', 'name': '장구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'basketgb', 'name': '바스켓구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'basketcnt', 'name': '바스켓갯수', 'type': 'float', 'length': 3, 'required': True}, {'key': 'elwtype', 'name': 'ELW권리행사방식', 'type': 'string', 'length': 2, 'required': True}, {'key': 'settletype', 'name': 'ELW결제방법', 'type': 'string', 'length': 2, 'required': True}, {'key': 'lpord', 'name': 'LP사주문가능여부', 'type': 'string', 'length': 2, 'required': True}, {'key': 'elwdetail', 'name': '권리내용', 'type': 'string', 'length': 100, 'required': True}, {'key': 'valuation', 'name': '만기평가가격방식', 'type': 'string', 'length': 100, 'required': True}],
                'type': 'single'
            },
            't1950OutBlock1': {
                'fields': [{'key': 'bskcode', 'name': '기초자산코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bskbno', 'name': '기초자산비율', 'type': 'float', 'length': 3, 'required': True}, {'key': 'bskprice', 'name': '기초자산현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bsksign', 'name': '기초자산전일비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'bskchange', 'name': '기초자산전일비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bskdiff', 'name': '기초자산등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bskvolume', 'name': '기초자산거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bskjnilclose', 'name': '기초자산전일종가', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1951': {
        'tr_cd': 't1951',
        'title': 'ELW시간대별체결조회',
        'blocks': {
            't1951OutBlock': {
                'fields': [{'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            },
            't1951OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'chdegree', 'name': '체결강도', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdvolume', 'name': '매도체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdchecnt', 'name': '매도체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'msvolume', 'name': '매수체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mschecnt', 'name': '매수체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'revolume', 'name': '순체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rechecnt', 'name': '순체결건수', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1954': {
        'tr_cd': 't1954',
        'title': 'ELW일별주가',
        'blocks': {
            't1954OutBlock': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'bsjgubun', 'name': '기초자산구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'bscode', 'name': '기초자산코드(현물)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bjcode', 'name': '기초자산코드(지수)', 'type': 'string', 'length': 3, 'required': True}],
                'type': 'single'
            },
            't1954OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bsprice', 'name': '기초자산(현물)', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bjprice', 'name': '기초자산(지수)', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'bsign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'bschange', 'name': '전일대비(현물)', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bjchange', 'name': '전일대비(지수)', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'bdiff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bvolume', 'name': '기초자산거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'parity', 'name': '패리티', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'egearing', 'name': 'e.기어링', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'premium', 'name': '프리미엄', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'berate', 'name': '손익분기', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'capt', 'name': '자본지지', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gearing', 'name': '기어링', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'mness', 'name': 'Moneyness', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1956': {
        'tr_cd': 't1956',
        'title': 'ELW현재가(확정지급액)조회',
        'blocks': {
            't1956OutBlock': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'chetime', 'name': '체결시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'recprice', 'name': '기준가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'avg', 'name': '가중평균', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jnilvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jvolume', 'name': '전일동시간거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'volumechg', 'name': '거래량차', 'type': 'float', 'length': 12, 'required': True}, {'key': 'volumediff', 'name': '거래량차등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'odiff', 'name': '시가등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'opentime', 'name': '시가시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'hdiff', 'name': '고가등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'hightime', 'name': '고가시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ldiff', 'name': '저가등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'lowtime', 'name': '저가시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'high52w', 'name': '52최고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high52wdiff', 'name': '52최고가등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high52wdate', 'name': '52최고가일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'low52w', 'name': '52최저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low52wdiff', 'name': '52최저가등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low52wdate', 'name': '52최저가일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'exhratio', 'name': '소진율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'listing', 'name': '상장주식수(천)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'memedan', 'name': '수량단위', 'type': 'string', 'length': 5, 'required': True}, {'key': 'vol', 'name': '회전율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'parity', 'name': '패리티', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'berate', 'name': '손익분기', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'gearing', 'name': '기어링', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'elwexec', 'name': '행사가', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'issueprice', 'name': '발행가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'convrate', 'name': '전환비율', 'type': 'float', 'length': 12.4, 'required': True}, {'key': 'lastdate', 'name': '최종거래일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'capt', 'name': '자본지지', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'egearing', 'name': 'e.기어링', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'premium', 'name': '프리미엄', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'spread', 'name': '스프레드', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'espread', 'name': '최대스프레드', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'theoryprice', 'name': '이론가', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'impv', 'name': '내재변동성', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'moneyness', 'name': '상태', 'type': 'string', 'length': 1, 'required': True}, {'key': 'delt', 'name': '델타', 'type': 'float', 'length': 8.6, 'required': True}, {'key': 'gama', 'name': '감마', 'type': 'float', 'length': 8.6, 'required': True}, {'key': 'vega', 'name': '베가', 'type': 'float', 'length': 13.6, 'required': True}, {'key': 'ceta', 'name': '쎄타', 'type': 'float', 'length': 13.6, 'required': True}, {'key': 'rhox', 'name': '로', 'type': 'float', 'length': 13.6, 'required': True}, {'key': 'bjandatecnt', 'name': '잔존일수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'mmsdate', 'name': '행사개시일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'mmedate', 'name': '행사종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'payday', 'name': '지급일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'listdate', 'name': '발행일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'lpmem', 'name': 'LP회원사', 'type': 'string', 'length': 20, 'required': True}, {'key': 'lp_holdvol', 'name': 'LP보유수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bcode', 'name': '기초자산코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bgubun', 'name': '기초자산구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'bprice', 'name': '기초자산현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bsign', 'name': '기초자산전일비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'bchange', 'name': '기초자산전일비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bdiff', 'name': '기초자산등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bvolume', 'name': '기초자산거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'info1', 'name': '락구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'info2', 'name': '관리/급등구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'info3', 'name': '정지/연장구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'info4', 'name': '투자/불성실구분', 'type': 'string', 'length': 12, 'required': True}, {'key': 'janginfo', 'name': '장구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'basketgb', 'name': '바스켓구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'basketcnt', 'name': '바스켓갯수', 'type': 'float', 'length': 3, 'required': True}, {'key': 'elwtype', 'name': 'ELW권리행사방식', 'type': 'string', 'length': 2, 'required': True}, {'key': 'settletype', 'name': 'ELW결제방법', 'type': 'string', 'length': 2, 'required': True}, {'key': 'lpord', 'name': 'LP사주문가능여부', 'type': 'string', 'length': 2, 'required': True}, {'key': 'elwdetail', 'name': '권리내용', 'type': 'string', 'length': 100, 'required': True}, {'key': 'valuation', 'name': '만기평가가격방식', 'type': 'string', 'length': 100, 'required': True}, {'key': 'givemoney', 'name': '확정지급액', 'type': 'float', 'length': 8.3, 'required': True}, {'key': 'intrns_wth_p2', 'name': '내재가치', 'type': 'float', 'length': 6.2, 'desc': '2026.01.15 16시 이후 적용예정', 'required': True}],
                'type': 'single'
            },
            't1956OutBlock1': {
                'fields': [{'key': 'bskcode', 'name': '기초자산코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bskbno', 'name': '기초자산비율', 'type': 'float', 'length': 3, 'required': True}, {'key': 'bskprice', 'name': '기초자산현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bsksign', 'name': '기초자산전일비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'bskchange', 'name': '기초자산전일비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bskdiff', 'name': '기초자산등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bskvolume', 'name': '기초자산거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bskjnilclose', 'name': '기초자산전일종가', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1958': {
        'tr_cd': 't1958',
        'title': 'ELW종목비교',
        'blocks': {
            't1958OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'item1', 'name': '기초자산', 'type': 'string', 'length': 12, 'required': True}, {'key': 'issuernmk', 'name': '발행사', 'type': 'string', 'length': 40, 'required': True}, {'key': 'elwopt', 'name': '콜풋구분', 'type': 'string', 'length': 2, 'required': True}, {'key': 'elwtype', 'name': '행사방식', 'type': 'string', 'length': 2, 'required': True}, {'key': 'settletype', 'name': '결제방법', 'type': 'string', 'length': 2, 'required': True}, {'key': 'elwexec', 'name': '행사가', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'convrate', 'name': '전환비율', 'type': 'float', 'length': 12.4, 'required': True}, {'key': 'listing', 'name': '발행수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mmsdate', 'name': '행사개시일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'lastdate', 'name': '최종거래일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'nofdays', 'name': '거래잔존일수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'payday', 'name': '지급일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'parity', 'name': '패리티', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'premium', 'name': '프리미엄', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'berate', 'name': '손익분기', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'capt', 'name': '자본지지', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gearing', 'name': '기어링', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'egearing', 'name': 'e.기어링', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'price', 'name': '가격', 'type': 'float', 'length': 8, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'single'
            },
            't1958OutBlock1': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'item1', 'name': '기초자산', 'type': 'string', 'length': 12, 'required': True}, {'key': 'issuernmk', 'name': '발행사', 'type': 'string', 'length': 40, 'required': True}, {'key': 'elwopt', 'name': '콜풋구분', 'type': 'string', 'length': 2, 'required': True}, {'key': 'elwtype', 'name': '행사방식', 'type': 'string', 'length': 2, 'required': True}, {'key': 'settletype', 'name': '결제방법', 'type': 'string', 'length': 2, 'required': True}, {'key': 'elwexec', 'name': '행사가', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'convrate', 'name': '전환비율', 'type': 'float', 'length': 12.4, 'required': True}, {'key': 'listing', 'name': '발행수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mmsdate', 'name': '행사개시일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'lastdate', 'name': '최종거래일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'nofdays', 'name': '거래잔존일수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'payday', 'name': '지급일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'parity', 'name': '패리티', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'premium', 'name': '프리미엄', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'berate', 'name': '손익분기', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'capt', 'name': '자본지지', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gearing', 'name': '기어링', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'egearing', 'name': 'e.기어링', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'price', 'name': '가격', 'type': 'float', 'length': 8, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'single'
            },
            't1958OutBlock2': {
                'fields': [{'key': 'hnamecmp', 'name': '종목명비교', 'type': 'string', 'length': 6, 'required': True}, {'key': 'item1cmp', 'name': '기초자산비교', 'type': 'string', 'length': 6, 'required': True}, {'key': 'issuernmkcmp', 'name': '발행사비교', 'type': 'string', 'length': 6, 'required': True}, {'key': 'elwoptcmp', 'name': '콜풋구분비교', 'type': 'string', 'length': 6, 'required': True}, {'key': 'elwtypecmp', 'name': '행사방식비교', 'type': 'string', 'length': 6, 'required': True}, {'key': 'settlecmp', 'name': '결제방법비교', 'type': 'string', 'length': 6, 'required': True}, {'key': 'elwexeccmp', 'name': '행사가비교', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'convcmp', 'name': '전환비율비교', 'type': 'float', 'length': 12.4, 'required': True}, {'key': 'listingcmp', 'name': '발행수량비교', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mmsdatecmp', 'name': '행사개시일비교', 'type': 'string', 'length': 6, 'required': True}, {'key': 'lastdatecmp', 'name': '최종거래일비교', 'type': 'string', 'length': 6, 'required': True}, {'key': 'nofdayscmp', 'name': '거래잔존일수비교', 'type': 'string', 'length': 6, 'required': True}, {'key': 'paydaycmp', 'name': '지급일비교', 'type': 'string', 'length': 6, 'required': True}, {'key': 'paritycmp', 'name': '패리티비교', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'premiumcmp', 'name': '프리미엄비교', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'beratecmp', 'name': '손익분기비교', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'captcmp', 'name': '자본지지비교', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gearingcmp', 'name': '기어링비교', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'egearingcmp', 'name': 'e.기어링비교', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'pricecmp', 'name': '가격비교', 'type': 'float', 'length': 8, 'required': True}, {'key': 'volumecmp', 'name': '거래량비교', 'type': 'float', 'length': 12, 'required': True}, {'key': 'diffcmp', 'name': '등락율비교', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1960': {
        'tr_cd': 't1960',
        'title': 'ELW등락율상위',
        'blocks': {
            't1960OutBlock': {
                'fields': [{'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1960OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'elwexec', 'name': '행사가', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'convrate', 'name': '전환비율', 'type': 'float', 'length': 12.4, 'required': True}, {'key': 'lastdate', 'name': '만기일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'itemcode', 'name': '기초자산종목코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'itemshcode', 'name': '기초자산단축코드', 'type': 'string', 'length': 9, 'required': True}, {'key': 'itemname', 'name': '기초자산종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'itemprice', 'name': '기초자산현재가', 'type': 'string', 'length': 10, 'required': True}, {'key': 'itemsign', 'name': '기초자산대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'itemchange', 'name': '기초자산전일대비', 'type': 'string', 'length': 10, 'required': True}, {'key': 'itemdiff', 'name': '기초자산등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'elwshcode', 'name': 'ELW종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bepoint', 'name': '손익분기점', 'type': 'float', 'length': 12.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1961': {
        'tr_cd': 't1961',
        'title': 'ELW거래량상위',
        'blocks': {
            't1961OutBlock': {
                'fields': [{'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'desc': '연속조회키 연속 조회시 이 값을 InBlock의 idx 필드에 넣어준다.', 'required': True}],
                'type': 'single'
            },
            't1961OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jnilvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'elwexec', 'name': '행사가', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'convrate', 'name': '전환비율', 'type': 'float', 'length': 12.4, 'required': True}, {'key': 'lastdate', 'name': '만기일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'itemcode', 'name': '기초자산종목코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'itemshcode', 'name': '기초자산단축코드', 'type': 'string', 'length': 9, 'required': True}, {'key': 'itemname', 'name': '기초자산종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'itemprice', 'name': '기초자산현재가', 'type': 'string', 'length': 10, 'required': True}, {'key': 'itemsign', 'name': '기초자산대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'itemchange', 'name': '기초자산전일대비', 'type': 'string', 'length': 10, 'required': True}, {'key': 'itemdiff', 'name': '기초자산등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'elwshcode', 'name': 'ELW종목코드', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1964': {
        'tr_cd': 't1964',
        'title': 'ELW전광판',
        'blocks': {
            't1964OutBlock1': {
                'fields': [{'key': 'shcode', 'name': 'ELW코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'item1', 'name': '기초자산코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'itemnm', 'name': '기초자산명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'issuernmk', 'name': '발행사', 'type': 'string', 'length': 40, 'required': True}, {'key': 'elwopt', 'name': '콜풋구분', 'type': 'string', 'length': 4, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'elwexec', 'name': '행사가', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'jandatecnt', 'name': '잔존일수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'convrate', 'name': '전환비율', 'type': 'float', 'length': 8.4, 'required': True}, {'key': 'lastdate', 'name': '최종거래일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'mmsdate', 'name': '행사개시일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'payday', 'name': '지급일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'listing', 'name': '발행수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'atmgbnm', 'name': '머니구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'parity', 'name': '패리티', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'preminum', 'name': '프리미엄', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'spread', 'name': '스프래드', 'type': 'float', 'length': 3.2, 'required': True}, {'key': 'berate', 'name': '손익분기율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'capt', 'name': '자본지지율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gearing', 'name': '기어링', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'egearing', 'name': 'e기어링', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'itemprice', 'name': '기초자산현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'itemsign', 'name': '기초자산전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'itemchange', 'name': '기초자산전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'itemdiff', 'name': '기초자산등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'itemvolume', 'name': '기초자산거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jnilvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'theoryprice', 'name': '이론가', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'lp_rate', 'name': 'LP보유비율', 'type': 'float', 'length': 5.2, 'required': True}, {'key': 'impv', 'name': '내재변동성', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'delta', 'name': '델타', 'type': 'float', 'length': 10.6, 'required': True}, {'key': 'theta', 'name': '쎄타', 'type': 'float', 'length': 10.6, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1966': {
        'tr_cd': 't1966',
        'title': 'ELW거래대금상위',
        'blocks': {
            't1966OutBlock': {
                'fields': [{'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'desc': '연속조회키 연속 조회시 이 값을 InBlock의 idx 필드에 넣어준다.', 'required': True}],
                'type': 'single'
            },
            't1966OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'value', 'name': '누적거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jnilvalue', 'name': '전일거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'elwexec', 'name': '행사가', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'convrate', 'name': '전환비율', 'type': 'float', 'length': 12.4, 'required': True}, {'key': 'lastdate', 'name': '만기일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'itemcode', 'name': '기초자산종목코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'itemshcode', 'name': '기초자산단축코드', 'type': 'string', 'length': 9, 'required': True}, {'key': 'itemname', 'name': '기초자산종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'itemprice', 'name': '기초자산현재가', 'type': 'string', 'length': 10, 'required': True}, {'key': 'itemsign', 'name': '기초자산대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'itemchange', 'name': '기초자산전일대비', 'type': 'string', 'length': 10, 'required': True}, {'key': 'itemdiff', 'name': '기초자산등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'elwshcode', 'name': 'ELW종목코드', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1969': {
        'tr_cd': 't1969',
        'title': 'ELW지표검색',
        'blocks': {
            't1969OutBlock': {
                'fields': [{'key': 'cnt', 'name': '종목갯수', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1969OutBlock1': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'issuernmk', 'name': '발행사', 'type': 'string', 'length': 40, 'required': True}, {'key': 'itemcode', 'name': '기초자산코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'cpgubun', 'name': '콜/풋구분', 'type': 'string', 'length': 2, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jnilvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'elwexec', 'name': '행사가', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'item', 'name': '기초자산명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'bprice', 'name': '기초자산가', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'bsign', 'name': '기초전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'bchange', 'name': '기초전일대비', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'bdiff', 'name': '기초등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'premium', 'name': '프리미엄', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'parity', 'name': '패리티', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'berate', 'name': '손익분기', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'capt', 'name': '자본지지', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'egearing', 'name': 'e.기어링', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gearing', 'name': '기어링', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'lastdate', 'name': '최종거래일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'delta', 'name': '델타', 'type': 'float', 'length': 10.6, 'required': True}, {'key': 'theta', 'name': '쎄타', 'type': 'float', 'length': 10.6, 'required': True}, {'key': 'lpname', 'name': 'LP회원사', 'type': 'string', 'length': 40, 'required': True}, {'key': 'lphold', 'name': 'LP보유율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bjandatecnt', 'name': '잔존일수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'convrate', 'name': '전환비율', 'type': 'float', 'length': 8.4, 'required': True}, {'key': 'tickvalue', 'name': '1틱환산', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'kasis', 'name': '괴리율', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1971': {
        'tr_cd': 't1971',
        'title': 'ELW현재가호가조회',
        'blocks': {
            't1971OutBlock': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho1', 'name': '매도호가1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho1', 'name': '매수호가1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem1', 'name': '매도호가수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_offerrem1', 'name': 'LP매도호가수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem1', 'name': '매수호가수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_bidrem1', 'name': 'LP매수호가수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha1', 'name': '직전매도대비수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha1', 'name': '직전매수대비수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho2', 'name': '매도호가2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho2', 'name': '매수호가2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem2', 'name': '매도호가수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_offerrem2', 'name': 'LP매도호가수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem2', 'name': '매수호가수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_bidrem2', 'name': 'LP매수호가수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha2', 'name': '직전매도대비수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha2', 'name': '직전매수대비수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho3', 'name': '매도호가3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho3', 'name': '매수호가3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem3', 'name': '매도호가수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_offerrem3', 'name': 'LP매도호가수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem3', 'name': '매수호가수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_bidrem3', 'name': 'LP매수호가수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha3', 'name': '직전매도대비수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha3', 'name': '직전매수대비수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho4', 'name': '매도호가4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho4', 'name': '매수호가4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem4', 'name': '매도호가수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_offerrem4', 'name': 'LP매도호가수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem4', 'name': '매수호가수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_bidrem4', 'name': 'LP매수호가수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha4', 'name': '직전매도대비수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha4', 'name': '직전매수대비수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho5', 'name': '매도호가5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho5', 'name': '매수호가5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem5', 'name': '매도호가수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_offerrem5', 'name': 'LP매도호가수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem5', 'name': '매수호가수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_bidrem5', 'name': 'LP매수호가수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha5', 'name': '직전매도대비수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha5', 'name': '직전매수대비수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho6', 'name': '매도호가6', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho6', 'name': '매수호가6', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem6', 'name': '매도호가수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_offerrem6', 'name': 'LP매도호가수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem6', 'name': '매수호가수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_bidrem6', 'name': 'LP매수호가수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha6', 'name': '직전매도대비수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha6', 'name': '직전매수대비수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho7', 'name': '매도호가7', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho7', 'name': '매수호가7', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem7', 'name': '매도호가수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_offerrem7', 'name': 'LP매도호가수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem7', 'name': '매수호가수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_bidrem7', 'name': 'LP매수호가수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha7', 'name': '직전매도대비수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha7', 'name': '직전매수대비수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho8', 'name': '매도호가8', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho8', 'name': '매수호가8', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem8', 'name': '매도호가수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_offerrem8', 'name': 'LP매도호가수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem8', 'name': '매수호가수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_bidrem8', 'name': 'LP매수호가수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha8', 'name': '직전매도대비수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha8', 'name': '직전매수대비수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho9', 'name': '매도호가9', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho9', 'name': '매수호가9', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem9', 'name': '매도호가수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_offerrem9', 'name': 'LP매도호가수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem9', 'name': '매수호가수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_bidrem9', 'name': 'LP매수호가수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha9', 'name': '직전매도대비수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha9', 'name': '직전매수대비수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho10', 'name': '매도호가10', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho10', 'name': '매수호가10', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem10', 'name': '매도호가수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_offerrem10', 'name': 'LP매도호가수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem10', 'name': '매수호가수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'lp_bidrem10', 'name': 'LP매수호가수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha10', 'name': '직전매도대비수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha10', 'name': '직전매수대비수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offer', 'name': '매도호가수량합', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bid', 'name': '매수호가수량합', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha', 'name': '직전매도대비수량합', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha', 'name': '직전매수대비수량합', 'type': 'float', 'length': 12, 'required': True}, {'key': 'hotime', 'name': '수신시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'yeprice', 'name': '예상체결가격', 'type': 'float', 'length': 8, 'required': True}, {'key': 'yevolume', 'name': '예상체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'yesign', 'name': '예상체결전일구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'yechange', 'name': '예상체결전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'yediff', 'name': '예상체결등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'tmoffer', 'name': '시간외매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tmbid', 'name': '시간외매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ho_status', 'name': '동시구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'invidx', 'name': 'ELW권리형태(1:표준2:디지털3:조기종료)', 'type': 'string', 'length': 1, 'desc': '1:표준<br/>2:디지털<br/>3:조기종료', 'required': True}, {'key': 'koba_stdprc', 'name': 'KO베리어', 'type': 'float', 'length': 12.2, 'required': True}, {'key': 'koba_acc_rt', 'name': 'KO접근도', 'type': 'float', 'length': 12.2, 'required': True}, {'key': 'koba_yn', 'name': 'KO발생여부(Y/N)', 'type': 'string', 'length': 1, 'desc': 'Y:Yes<br/>N:No', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1972': {
        'tr_cd': 't1972',
        'title': 'ELW현재가(거래원)조회',
        'blocks': {
            't1972OutBlock': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'expcode', 'name': '표준코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 9, 'required': True}, {'key': 'offerno1', 'name': '매도증권사코드1', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bidno1', 'name': '매수증권사코드1', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dvol1', 'name': '총매도수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svol1', 'name': '총매수수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'dcha1', 'name': '매도증감1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'scha1', 'name': '매수증감1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ddiff1', 'name': '매도비율1', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sdiff1', 'name': '매수비율1', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerno2', 'name': '매도증권사코드2', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bidno2', 'name': '매수증권사코드2', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dvol2', 'name': '총매도수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svol2', 'name': '총매수수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'dcha2', 'name': '매도증감2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'scha2', 'name': '매수증감2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ddiff2', 'name': '매도비율2', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sdiff2', 'name': '매수비율2', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerno3', 'name': '매도증권사코드3', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bidno3', 'name': '매수증권사코드3', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dvol3', 'name': '총매도수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svol3', 'name': '총매수수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'dcha3', 'name': '매도증감3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'scha3', 'name': '매수증감3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ddiff3', 'name': '매도비율3', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sdiff3', 'name': '매수비율3', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerno4', 'name': '매도증권사코드4', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bidno4', 'name': '매수증권사코드4', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dvol4', 'name': '총매도수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svol4', 'name': '총매수수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'dcha4', 'name': '매도증감4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'scha4', 'name': '매수증감4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ddiff4', 'name': '매도비율4', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sdiff4', 'name': '매수비율4', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerno5', 'name': '매도증권사코드5', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bidno5', 'name': '매수증권사코드5', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dvol5', 'name': '총매도수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svol5', 'name': '총매수수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'dcha5', 'name': '매도증감5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'scha5', 'name': '매수증감5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ddiff5', 'name': '매도비율5', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sdiff5', 'name': '매수비율5', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'fwdvl', 'name': '외국계매도합계수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'fwsvl', 'name': '외국계매수합계수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ftradmdcha', 'name': '외국계매도직전대비', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ftradmscha', 'name': '외국계매수직전대비', 'type': 'float', 'length': 12, 'required': True}, {'key': 'fwddiff', 'name': '외국계매도합계비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'fwsdiff', 'name': '외국계매수합계비율', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1973': {
        'tr_cd': 't1973',
        'title': 'ELW시간대별예상체결조회',
        'blocks': {
            't1973OutBlock': {
                'fields': [{'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            },
            't1973OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'yeprice', 'name': '예상체결가격', 'type': 'float', 'length': 8, 'required': True}, {'key': 'yegubun', 'name': '예상체결구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'jnilysign', 'name': '전일종가대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'jnilychange', 'name': '전일종가대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'yediff', 'name': '예상체결등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'yevolume', 'name': '예상체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ymdvolume', 'name': '예상매도체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ymsvolume', 'name': '예상매수체결량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1974': {
        'tr_cd': 't1974',
        'title': 'ELW기초자산동일종목',
        'blocks': {
            't1974OutBlock': {
                'fields': [{'key': 'cnt', 'name': '종목갯수', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1974OutBlock1': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'cpgubun', 'name': '콜/풋구분', 'type': 'string', 'length': 2, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8431': {
        'tr_cd': 't8431',
        'title': 'ELW종목조회',
        'blocks': {
            't8431OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'expcode', 'name': '확장코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'uplmtprice', 'name': '상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dnlmtprice', 'name': '하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'recprice', 'name': '기준가', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't9942': {
        'tr_cd': 't9942',
        'title': 'ELW마스터조회API용',
        'blocks': {
            't9942OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'expcode', 'name': '확장코드', 'type': 'string', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    }
}
