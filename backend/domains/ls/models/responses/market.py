# Auto-generated
from typing import Any, Dict, List

MARKET_RESPONSES = {
    'AFR': {
        'tr_cd': 'AFR',
        'title': 'API사용자조건검색실시간',
        'fields': [
            {
                'key': 'gsCode',
                'length': 9,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'gshname',
                'length': 40,
                'name': '종목명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'gsPrice',
                'length': 8,
                'name': '현재가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'gsSign',
                'length': 1,
                'name': '전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'gsChange',
                'length': 8,
                'name': '전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'gsChgRate',
                'length': 6,
                'name': '등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'gsVolume',
                'length': 9,
                'name': '거래량',
                'required': True,
                'type': 'string'
            },
            {
                'desc': 'N:진입 R:재진입 O:이탈',
                'key': 'gsJobFlag',
                'length': 1,
                'name': '종목상태',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'BMT': {
        'tr_cd': 'BMT',
        'title': '시간대별투자자매매추이',
        'fields': [
            {
                'key': 'tjjtime',
                'length': 8,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode1',
                'length': 4,
                'name': '투자자코드1(개인)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume1',
                'length': 8,
                'name': '매수거래량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume1',
                'length': 8,
                'name': '매도거래량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvol1',
                'length': 8,
                'name': '거래량순매수1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvalue1',
                'length': 6,
                'name': '매수거래대금1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvalue1',
                'length': 6,
                'name': '매도거래대금1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msval1',
                'length': 6,
                'name': '거래대금순매수1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode2',
                'length': 4,
                'name': '투자자코드2(외국인)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume2',
                'length': 8,
                'name': '매수거래량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume2',
                'length': 8,
                'name': '매도거래량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvol2',
                'length': 8,
                'name': '거래량순매수2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvalue2',
                'length': 6,
                'name': '매수거래대금2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvalue2',
                'length': 6,
                'name': '매도거래대금2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msval2',
                'length': 6,
                'name': '거래대금순매수2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode3',
                'length': 4,
                'name': '투자자코드3(기관계)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume3',
                'length': 8,
                'name': '매수거래량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume3',
                'length': 8,
                'name': '매도거래량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvol3',
                'length': 8,
                'name': '거래량순매수3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvalue3',
                'length': 6,
                'name': '매수거래대금3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvalue3',
                'length': 6,
                'name': '매도거래대금3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msval3',
                'length': 6,
                'name': '거래대금순매수3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode4',
                'length': 4,
                'name': '투자자코드4(증권)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume4',
                'length': 8,
                'name': '매수거래량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume4',
                'length': 8,
                'name': '매도거래량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvol4',
                'length': 8,
                'name': '거래량순매수4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvalue4',
                'length': 6,
                'name': '매수거래대금4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvalue4',
                'length': 6,
                'name': '매도거래대금4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msval4',
                'length': 6,
                'name': '거래대금순매수4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode5',
                'length': 4,
                'name': '투자자코드5(투신)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume5',
                'length': 8,
                'name': '매수거래량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume5',
                'length': 8,
                'name': '매도거래량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvol5',
                'length': 8,
                'name': '거래량순매수5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvalue5',
                'length': 6,
                'name': '매수거래대금5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvalue5',
                'length': 6,
                'name': '매도거래대금5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msval5',
                'length': 6,
                'name': '거래대금순매수5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode6',
                'length': 4,
                'name': '투자자코드6(은행)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume6',
                'length': 8,
                'name': '매수거래량6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume6',
                'length': 8,
                'name': '매도거래량6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvol6',
                'length': 8,
                'name': '거래량순매수6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvalue6',
                'length': 6,
                'name': '매수거래대금6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvalue6',
                'length': 6,
                'name': '매도거래대금6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msval6',
                'length': 6,
                'name': '거래대금순매수6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode7',
                'length': 4,
                'name': '투자자코드7(보험)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume7',
                'length': 8,
                'name': '매수거래량7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume7',
                'length': 8,
                'name': '매도거래량7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvol7',
                'length': 8,
                'name': '거래량순매수7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvalue7',
                'length': 6,
                'name': '매수거래대금7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvalue7',
                'length': 6,
                'name': '매도거래대금7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msval7',
                'length': 6,
                'name': '거래대금순매수7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode8',
                'length': 4,
                'name': '투자자코드8(종금)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume8',
                'length': 8,
                'name': '매수거래량8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume8',
                'length': 8,
                'name': '매도거래량8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvol8',
                'length': 8,
                'name': '거래량순매수8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvalue8',
                'length': 6,
                'name': '매수거래대금8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvalue8',
                'length': 6,
                'name': '매도거래대금8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msval8',
                'length': 6,
                'name': '거래대금순매수8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode9',
                'length': 4,
                'name': '투자자코드9(기금)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume9',
                'length': 8,
                'name': '매수거래량9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume9',
                'length': 8,
                'name': '매도거래량9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvol9',
                'length': 8,
                'name': '거래량순매수9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvalue9',
                'length': 6,
                'name': '매수거래대금9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvalue9',
                'length': 6,
                'name': '매도거래대금9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msval9',
                'length': 6,
                'name': '거래대금순매수9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode10',
                'length': 4,
                'name': '투자자코드10(선물업자)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume10',
                'length': 8,
                'name': '매수거래량10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume10',
                'length': 8,
                'name': '매도거래량10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvol10',
                'length': 8,
                'name': '거래량순매수10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvalue10',
                'length': 6,
                'name': '매수거래대금10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvalue10',
                'length': 6,
                'name': '매도거래대금10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msval10',
                'length': 6,
                'name': '거래대금순매수10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode11',
                'length': 4,
                'name': '투자자코드11(기타)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume11',
                'length': 8,
                'name': '매수거래량11',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume11',
                'length': 8,
                'name': '매도거래량11',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvol11',
                'length': 8,
                'name': '거래량순매수11',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvalue11',
                'length': 6,
                'name': '매수거래대금11',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvalue11',
                'length': 6,
                'name': '매도거래대금11',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msval11',
                'length': 6,
                'name': '거래대금순매수11',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'upcode',
                'length': 3,
                'name': '업종코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode0',
                'length': 4,
                'name': '투자자코드0(사모펀드)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume0',
                'length': 8,
                'name': '매수거래량0',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume0',
                'length': 8,
                'name': '매도거래량0',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvol0',
                'length': 8,
                'name': '거래량순매수0',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvalue0',
                'length': 6,
                'name': '매수거래대금0',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvalue0',
                'length': 6,
                'name': '매도거래대금0',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msval0',
                'length': 6,
                'name': '거래대금순매수0',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'BM_': {
        'tr_cd': 'BM_',
        'title': '업종별투자자별매매현황',
        'fields': [
            {
                'desc': '001:코스피<br/>101:KP200<br/>301:코스닥<br/>900:선  물<br/>700:콜옵션<br/>800:풋옵션<br/>550:ELW<br/>560:ETF',
                'key': 'tjjcode',
                'length': 4,
                'name': '투자자코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjtime',
                'length': 8,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume',
                'length': 8,
                'name': '매수거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume',
                'length': 8,
                'name': '매도거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvol',
                'length': 8,
                'name': '거래량순매수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_msvol',
                'length': 8,
                'name': '거래량순매수직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvalue',
                'length': 6,
                'name': '매수거래대금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvalue',
                'length': 6,
                'name': '매도거래대금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msval',
                'length': 6,
                'name': '거래대금순매수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_msval',
                'length': 6,
                'name': '거래대금순매수직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'upcode',
                'length': 3,
                'name': '업종코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'CDPCQ04700': {
        'tr_cd': 'CDPCQ04700',
        'title': '계좌 거래내역',
        'blocks': {
            'CDPCQ04700OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'QryTp', 'name': '조회구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QrySrtDt', 'name': '조회시작일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryEndDt', 'name': '조회종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'SrtNo', 'name': '시작번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'PdptnCode', 'name': '상품유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'IsuLgclssCode', 'name': '종목대분류코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}],
                'type': 'single'
            },
            'CDPCQ04700OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}],
                'type': 'single'
            },
            'CDPCQ04700OutBlock3': {
                'fields': [{'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'TrdDt', 'name': '거래일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'TrdNo', 'name': '거래번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'TpCodeNm', 'name': '구분코드명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'SmryNo', 'name': '적요번호', 'type': 'string', 'length': 4, 'required': True}, {'key': 'SmryNm', 'name': '적요명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'CancTpNm', 'name': '취소구분', 'type': 'string', 'length': 20, 'required': True}, {'key': 'TrdQty', 'name': '거래수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'Trtax', 'name': '거래세', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FcurrAdjstAmt', 'name': '외화정산금액', 'type': 'float', 'length': 25.4, 'required': True}, {'key': 'AdjstAmt', 'name': '정산금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OvdSum', 'name': '연체합', 'type': 'float', 'length': 16, 'required': True}, {'key': 'DpsBfbalAmt', 'name': '예수금전잔금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SellPldgRfundAmt', 'name': '매도담보상환금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'DpspdgLoanBfbalAmt', 'name': '예탁담보대출전잔금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'TrdmdaNm', 'name': '거래매체명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'OrgTrdNo', 'name': '원거래번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'TrdUprc', 'name': '거래단가', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'CmsnAmt', 'name': '수수료', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FcurrCmsnAmt', 'name': '외화수수료금액', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'RfundDiffAmt', 'name': '상환차이금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'RepayAmtSum', 'name': '변제금합계', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SecCrbalQty', 'name': '유가증권금잔수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CslLoanRfundIntrstAmt', 'name': '매도대금담보대출상환이자금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'DpspdgLoanCrbalAmt', 'name': '예탁담보대출금잔금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'TrxTime', 'name': '처리시각', 'type': 'string', 'length': 9, 'required': True}, {'key': 'Inouno', 'name': '출납번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'TrdAmt', 'name': '거래금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'ChckAmt', 'name': '수표금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'TaxSumAmt', 'name': '세금합계금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FcurrTaxSumAmt', 'name': '외화세금합계금액', 'type': 'float', 'length': 26.6, 'required': True}, {'key': 'IntrstUtlfee', 'name': '이자이용료', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyDvdAmt', 'name': '배당금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'RcvblOcrAmt', 'name': '미수발생금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'TrxBrnNo', 'name': '처리지점번호', 'type': 'string', 'length': 3, 'required': True}, {'key': 'TrxBrnNm', 'name': '처리지점명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'DpspdgLoanAmt', 'name': '예탁담보대출금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'DpspdgLoanRfundAmt', 'name': '예탁담보대출상환금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'BasePrc', 'name': '기준가', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'DpsCrbalAmt', 'name': '예수금금잔금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'BoaAmt', 'name': '과표', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyoutAbleAmt', 'name': '출금가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'BcrLoanOcrAmt', 'name': '수익증권담보대출발생금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'BcrLoanBfbalAmt', 'name': '수익증권담보대출전잔금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'BnsBasePrc', 'name': '매매기준가', 'type': 'float', 'length': 20.1, 'required': True}, {'key': 'TaxchrBasePrc', 'name': '과세기준가', 'type': 'float', 'length': 20.1, 'required': True}, {'key': 'TrdUnit', 'name': '거래좌수', 'type': 'float', 'length': 16, 'required': True}, {'key': 'BalUnit', 'name': '잔고좌수', 'type': 'float', 'length': 16, 'required': True}, {'key': 'EvrTax', 'name': '제세금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'EvalAmt', 'name': '평가금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'BcrLoanRfundAmt', 'name': '수익증권담보대출상환금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'BcrLoanCrbalAmt', 'name': '수익증권담보대출금잔금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AddMgnOcrTotamt', 'name': '추가증거금발생총액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AddMnyMgnOcrAmt', 'name': '추가현금증거금발생금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AddMgnDfryTotamt', 'name': '추가증거금납부총액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AddMnyMgnDfryAmt', 'name': '추가현금증거금납부금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'BnsplAmt', 'name': '매매손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'Ictax', 'name': '소득세', 'type': 'float', 'length': 16, 'required': True}, {'key': 'Ihtax', 'name': '주민세', 'type': 'float', 'length': 16, 'required': True}, {'key': 'LoanDt', 'name': '대출일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'CrcyCode', 'name': '통화코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'FcurrAmt', 'name': '외화금액', 'type': 'float', 'length': 24.4, 'required': True}, {'key': 'FcurrTrdAmt', 'name': '외화거래금액', 'type': 'float', 'length': 24.4, 'required': True}, {'key': 'FcurrDps', 'name': '외화예수금', 'type': 'float', 'length': 21.4, 'required': True}, {'key': 'FcurrDpsBfbalAmt', 'name': '외화예수금전잔금액', 'type': 'float', 'length': 21.4, 'required': True}, {'key': 'OppAcntNm', 'name': '상대계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'OppAcntNo', 'name': '상대계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'LoanRfundAmt', 'name': '대출상환금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'LoanIntrstAmt', 'name': '대출이자금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AskpsnNm', 'name': '의뢰인명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'OrdDt', 'name': '주문일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'TrdXchrat', 'name': '거래환율', 'type': 'float', 'length': 15.4, 'required': True}, {'key': 'RdctCmsn', 'name': '감면수수료', 'type': 'float', 'length': 21.4, 'required': True}, {'key': 'FcurrStmpTx', 'name': '외화인지세', 'type': 'float', 'length': 21.4, 'required': True}, {'key': 'FcurrElecfnTrtax', 'name': '외화전자금융거래세', 'type': 'float', 'length': 21.4, 'required': True}, {'key': 'FcstckTrtax', 'name': '외화증권거래세', 'type': 'float', 'length': 21.4, 'required': True}],
                'type': 'array'
            },
            'CDPCQ04700OutBlock4': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'PnlSumAmt', 'name': '손익합계금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CtrctAsm', 'name': '약정누계', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CmsnAmtSumAmt', 'name': '수수료합계금액', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            },
            'CDPCQ04700OutBlock5': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'MnyinAmt', 'name': '입금금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SecinAmt', 'name': '입고금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyoutAmt', 'name': '출금금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SecoutAmt', 'name': '출고금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'DiffAmt', 'name': '차이금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'DiffAmt0', 'name': '차이금액0', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SellQty', 'name': '매도수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SellAmt', 'name': '매도금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SellCmsn', 'name': '매도수수료', 'type': 'float', 'length': 16, 'required': True}, {'key': 'EvrTax', 'name': '제세금', 'type': 'float', 'length': 19, 'required': True}, {'key': 'FcurrSellAdjstAmt', 'name': '외화매도정산금액', 'type': 'float', 'length': 25.4, 'required': True}, {'key': 'BuyQty', 'name': '매수수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'BuyAmt', 'name': '매수금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'BuyCmsn', 'name': '매수수수료', 'type': 'float', 'length': 16, 'required': True}, {'key': 'ExecTax', 'name': '체결세금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FcurrBuyAdjstAmt', 'name': '외화매수정산금액', 'type': 'float', 'length': 25.4, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CLNAQ00100': {
        'tr_cd': 'CLNAQ00100',
        'title': '예탁담보융자가능종목현황조회',
        'blocks': {
            'CLNAQ00100OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'QryTp', 'name': '조회구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'SecTpCode', 'name': '유가증권구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'LoanIntrstGrdCode', 'name': '대출이자등급코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'LoanTp', 'name': '대출구분', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            },
            'CLNAQ00100OutBlock2': {
                'fields': [{'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'Parprc', 'name': '액면가', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'PrdayCprc', 'name': '전일종가', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'RatVal', 'name': '비율값', 'type': 'float', 'length': 19.8, 'required': True}, {'key': 'SubstPrc', 'name': '대용가', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'RegTpNm', 'name': '등록구분', 'type': 'string', 'length': 20, 'required': True}, {'key': 'SpotMgnLevyClssNm', 'name': '현물증거금징수분류명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'FnoTrdStopRsnCnts', 'name': '거래정지사유', 'type': 'string', 'length': 40, 'required': True}, {'key': 'DgrsPtnNm', 'name': '요주의유형명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'AcdPtnNm', 'name': '사고유형', 'type': 'string', 'length': 40, 'required': True}, {'key': 'MktTpNm', 'name': '시장구분', 'type': 'string', 'length': 20, 'required': True}, {'key': 'LmtVal', 'name': '한도값', 'type': 'float', 'length': 18, 'required': True}, {'key': 'AcntLmtVal', 'name': '계좌한도값', 'type': 'float', 'length': 18, 'required': True}, {'key': 'LoanGrdCode', 'name': '대출등급코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'LoanAmt', 'name': '대출금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'LoanAbleRat', 'name': '대출가능율', 'type': 'float', 'length': 26.9, 'required': True}, {'key': 'LoanIntrat1', 'name': '대출이율1', 'type': 'float', 'length': 14.4, 'required': True}, {'key': 'RegPsnId', 'name': '등록자ID', 'type': 'string', 'length': 16, 'required': True}, {'key': 'Rat01', 'name': '비율값', 'type': 'float', 'length': 19.8, 'required': True}, {'key': 'Rat02', 'name': '비율값', 'type': 'float', 'length': 19.8, 'required': True}],
                'type': 'array'
            },
            'CLNAQ00100OutBlock3': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'LrgMnyoutSumAmt', 'name': '대출금합계금액', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CSPBQ00200': {
        'tr_cd': 'CSPBQ00200',
        'title': '현물계좌증거금률별주문가능수량조회',
        'blocks': {
            'CSPBQ00200OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'InptPwd', 'name': '입력비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'OrdPrc', 'name': '주문가격', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'RegCommdaCode', 'name': '통신매체코드', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            'CSPBQ00200OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'Dps', 'name': '예수금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SubstAmt', 'name': '대용금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CrdtPldgRuseAmt', 'name': '신용담보재사용금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdAbleAmt', 'name': '현금주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SubstOrdAbleAmt', 'name': '대용주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyMgn', 'name': '현금증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SubstMgn', 'name': '대용증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SeOrdAbleAmt', 'name': '거래소금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'KdqOrdAbleAmt', 'name': '코스닥금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PrsmptDpsD1', 'name': '추정예수금(D+1)', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PrsmptDpsD2', 'name': '추정예수금(D+2)', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyoutAbleAmt', 'name': '출금가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'RcvblAmt', 'name': '미수금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CmsnRat', 'name': '수수료율', 'type': 'float', 'length': 15.5, 'required': True}, {'key': 'AddLevyAmt', 'name': '추가징수금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'RuseObjAmt', 'name': '재사용대상금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyRuseObjAmt', 'name': '현금재사용대상금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FirmMgnRat', 'name': '이용사증거금률', 'type': 'float', 'length': 7.4, 'required': True}, {'key': 'SubstRuseObjAmt', 'name': '대용재사용대상금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'IsuMgnRat', 'name': '종목증거금률', 'type': 'float', 'length': 7.4, 'required': True}, {'key': 'AcntMgnRat', 'name': '계좌증거금률', 'type': 'float', 'length': 7.4, 'required': True}, {'key': 'TrdMgnrt', 'name': '거래증거금률', 'type': 'float', 'length': 7.4, 'required': True}, {'key': 'Cmsn', 'name': '수수료', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRat20pctOrdAbleAmt', 'name': '증거금률20퍼센트주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRat20OrdAbleQty', 'name': '증거금률100퍼센트현금주문가능수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRat30pctOrdAbleAmt', 'name': '증거금률30퍼센트주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRat30OrdAbleQty', 'name': '증거금률30퍼센트주문가능수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRat40pctOrdAbleAmt', 'name': '증거금률40퍼센트주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRat40OrdAbleQty', 'name': '증거금률40퍼센트주문가능수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRat100pctOrdAbleAmt', 'name': '증거금률100퍼센트주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRat100OrdAbleQty', 'name': '증거금률100퍼센트주문가능수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRat100MnyOrdAbleAmt', 'name': '증거금률100퍼센트현금주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRat100MnyOrdAbleQty', 'name': '증거금률100퍼센트현금주문가능수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRat20pctRuseAbleAmt', 'name': '증거금률20퍼센트재사용가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRat30pctRuseAbleAmt', 'name': '증거금률30퍼센트재사용가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRat40pctRuseAbleAmt', 'name': '증거금률40퍼센트재사용가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRat100pctRuseAbleAmt', 'name': '증거금률100퍼센트재사용가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdAbleQty', 'name': '주문가능수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdAbleAmt', 'name': '주문가능금액', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CUR': {
        'tr_cd': 'CUR',
        'title': '현물정보USD실시간',
        'fields': [
            {
                'key': 'time',
                'length': '	6',
                'name': '전송시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offer',
                'length': '	7.2',
                'name': '매도호가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bid',
                'length': '	7.2',
                'name': '매수호가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'open',
                'length': '	7.2',
                'name': '시가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'high',
                'length': '	7.2',
                'name': '고가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low',
                'length': '	7.2',
                'name': '저가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'price',
                'length': '	7.2',
                'name': '체결가',
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
                'length': '	7.2',
                'name': '전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'drate',
                'length': '	7.2',
                'name': '등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ctime',
                'length': '	6',
                'name': '데이타발생시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'base_id',
                'length': '	6',
                'name': '기초자산ID',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'DH1': {
        'tr_cd': 'DH1',
        'title': 'KOSPI시간외단일가호가잔량',
        'fields': [
            {
                'key': 'dan_hotime',
                'length': 6,
                'name': '시간외단일가호가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_hstatus',
                'length': 2,
                'name': '시간외단일가장구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerho1',
                'length': 8,
                'name': '시간외단일가매도호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidho1',
                'length': 8,
                'name': '시간외단일가매수호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerrem1',
                'length': 12,
                'name': '시간외단일가매도호가잔량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidrem1',
                'length': 12,
                'name': '시간외단일가매수호가잔량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preoffercha1',
                'length': 12,
                'name': '시간외단일가직전매도대비수량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_prebidcha1',
                'length': 12,
                'name': '시간외단일가직전매수대비수량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerho2',
                'length': 8,
                'name': '시간외단일가매도호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidho2',
                'length': 8,
                'name': '시간외단일가매수호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerrem2',
                'length': 12,
                'name': '시간외단일가매도호가잔량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidrem2',
                'length': 12,
                'name': '시간외단일가매수호가잔량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preoffercha2',
                'length': 12,
                'name': '시간외단일가직전매도대비수량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_prebidcha2',
                'length': 12,
                'name': '시간외단일가직전매수대비수량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerho3',
                'length': 8,
                'name': '시간외단일가매도호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidho3',
                'length': 8,
                'name': '시간외단일가매수호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerrem3',
                'length': 12,
                'name': '시간외단일가매도호가잔량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidrem3',
                'length': 12,
                'name': '시간외단일가매수호가잔량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preoffercha3',
                'length': 12,
                'name': '시간외단일가직전매도대비수량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_prebidcha3',
                'length': 12,
                'name': '시간외단일가직전매수대비수량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerho4',
                'length': 8,
                'name': '시간외단일가매도호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidho4',
                'length': 8,
                'name': '시간외단일가매수호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerrem4',
                'length': 12,
                'name': '시간외단일가매도호가잔량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidrem4',
                'length': 12,
                'name': '시간외단일가매수호가잔량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preoffercha4',
                'length': 12,
                'name': '시간외단일가직전매도대비수량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_prebidcha4',
                'length': 12,
                'name': '시간외단일가직전매수대비수량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerho5',
                'length': 8,
                'name': '시간외단일가매도호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidho5',
                'length': 8,
                'name': '시간외단일가매수호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerrem5',
                'length': 12,
                'name': '시간외단일가매도호가잔량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidrem5',
                'length': 12,
                'name': '시간외단일가매수호가잔량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preoffercha5',
                'length': 12,
                'name': '시간외단일가직전매도대비수량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_prebidcha5',
                'length': 12,
                'name': '시간외단일가직전매수대비수량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_totofferrem',
                'length': 12,
                'name': '시간외단일가총매도호가잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_totbidrem',
                'length': 12,
                'name': '시간외단일가총매수호가잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preoffercha',
                'length': 12,
                'name': '시간외단일가직전매도호가총대비수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_prebidcha',
                'length': 12,
                'name': '시간외단일가직전매수호가총대비수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_yeprice',
                'length': 8,
                'name': '시간외단일가예상체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_yevolume',
                'length': 12,
                'name': '시간외단일가예상체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preysign',
                'length': 1,
                'name': '시간외단일가예상가직전가대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preychange',
                'length': 8,
                'name': '시간외단일가예상가직전가대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_jnilysign',
                'length': 1,
                'name': '시간외단일가예상가전일가대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_jnilychange',
                'length': 8,
                'name': '시간외단일가예상가전일가대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': 6,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volume',
                'length': 12,
                'name': '누적거래량',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'DHA': {
        'tr_cd': 'DHA',
        'title': 'KOSDAQ시간외단일가호가잔량',
        'fields': [
            {
                'key': 'dan_hotime',
                'length': 6,
                'name': '시간외단일가호가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_hstatus',
                'length': 2,
                'name': '시간외단일가장구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerho1',
                'length': 8,
                'name': '시간외단일가매도호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidho1',
                'length': 8,
                'name': '시간외단일가매수호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerrem1',
                'length': 12,
                'name': '시간외단일가매도호가잔량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidrem1',
                'length': 12,
                'name': '시간외단일가매수호가잔량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preoffercha1',
                'length': 12,
                'name': '시간외단일가직전매도대비수량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_prebidcha1',
                'length': 12,
                'name': '시간외단일가직전매수대비수량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerho2',
                'length': 8,
                'name': '시간외단일가매도호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidho2',
                'length': 8,
                'name': '시간외단일가매수호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerrem2',
                'length': 12,
                'name': '시간외단일가매도호가잔량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidrem2',
                'length': 12,
                'name': '시간외단일가매수호가잔량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preoffercha2',
                'length': 12,
                'name': '시간외단일가직전매도대비수량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_prebidcha2',
                'length': 12,
                'name': '시간외단일가직전매수대비수량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerho3',
                'length': 8,
                'name': '시간외단일가매도호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidho3',
                'length': 8,
                'name': '시간외단일가매수호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerrem3',
                'length': 12,
                'name': '시간외단일가매도호가잔량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidrem3',
                'length': 12,
                'name': '시간외단일가매수호가잔량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preoffercha3',
                'length': 12,
                'name': '시간외단일가직전매도대비수량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_prebidcha3',
                'length': 12,
                'name': '시간외단일가직전매수대비수량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerho4',
                'length': 8,
                'name': '시간외단일가매도호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidho4',
                'length': 8,
                'name': '시간외단일가매수호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerrem4',
                'length': 12,
                'name': '시간외단일가매도호가잔량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidrem4',
                'length': 12,
                'name': '시간외단일가매수호가잔량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preoffercha4',
                'length': 12,
                'name': '시간외단일가직전매도대비수량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_prebidcha4',
                'length': 12,
                'name': '시간외단일가직전매수대비수량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerho5',
                'length': 8,
                'name': '시간외단일가매도호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidho5',
                'length': 8,
                'name': '시간외단일가매수호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_offerrem5',
                'length': 12,
                'name': '시간외단일가매도호가잔량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_bidrem5',
                'length': 12,
                'name': '시간외단일가매수호가잔량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preoffercha5',
                'length': 12,
                'name': '시간외단일가직전매도대비수량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_prebidcha5',
                'length': 12,
                'name': '시간외단일가직전매수대비수량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_totofferrem',
                'length': 12,
                'name': '시간외단일가총매도호가잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_totbidrem',
                'length': 12,
                'name': '시간외단일가총매수호가잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preoffercha',
                'length': 12,
                'name': '시간외단일가직전매도호가총대비수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_prebidcha',
                'length': 12,
                'name': '시간외단일가직전매수호가총대비수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_yeprice',
                'length': 8,
                'name': '시간외단일가예상체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_yevolume',
                'length': 12,
                'name': '시간외단일가예상체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preysign',
                'length': 1,
                'name': '시간외단일가예상가직전가대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_preychange',
                'length': 8,
                'name': '시간외단일가예상가직전가대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_jnilysign',
                'length': 1,
                'name': '시간외단일가예상가전일가대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_jnilychange',
                'length': 8,
                'name': '시간외단일가예상가전일가대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': 6,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volume',
                'length': 12,
                'name': '누적거래량',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'DK3': {
        'tr_cd': 'DK3',
        'title': 'KOSDAQ시간외단일가체결',
        'fields': [
            {
                'key': 'dan_chetime',
                'length': '	6',
                'name': '시간외단일가체결시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_sign',
                'length': '	1',
                'name': '시간외단일가전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_change',
                'length': '	8',
                'name': '시간외단일가전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_drate',
                'length': '	6.2',
                'name': '시간외단일가등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_price',
                'length': '	8',
                'name': '시간외단일가현재가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_opentime',
                'length': '	6',
                'name': '시간외단일가시가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_open',
                'length': '	8',
                'name': '시간외단일가시가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_hightime',
                'length': '	6',
                'name': '시간외단일가고가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_high',
                'length': '	8',
                'name': '시간외단일가고가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_lowtime',
                'length': '	6',
                'name': '시간외단일가저가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_low',
                'length': '	8',
                'name': '시간외단일가저가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_cgubun',
                'length': '	1',
                'name': '시간외단일가체결구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_cvolume',
                'length': '	8',
                'name': '시간외단일가체결량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_volume',
                'length': '	12',
                'name': '시간외단일가누적거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_value',
                'length': '	12',
                'name': '시간외단일가누적거래대금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_mdvolume',
                'length': '	12',
                'name': '시간외단일가매도누적체결량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_mdchecnt',
                'length': '	8',
                'name': '시간외단일가매도누적체결건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_msvolume',
                'length': '	12',
                'name': '시간외단일가매수누적체결량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_mschecnt',
                'length': '	8',
                'name': '시간외단일가매수누적체결건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_prevolume',
                'length': '	8',
                'name': '시간외단일가직전거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_precvolume',
                'length': '	8',
                'name': '시간외단일가직전체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_cpower',
                'length': '	9.2',
                'name': '시간외단일가체결강도',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_status',
                'length': '	2',
                'name': '시간외단일가장정보',
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
    'DS3': {
        'tr_cd': 'DS3',
        'title': 'KOSPI시간외단일가체결',
        'fields': [
            {
                'key': 'dan_chetime',
                'length': '	6',
                'name': '시간외단일가체결시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_sign',
                'length': '	1',
                'name': '시간외단일가전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_change',
                'length': '	8',
                'name': '시간외단일가전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_drate',
                'length': '	6.2',
                'name': '시간외단일가등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_price',
                'length': '	8',
                'name': '시간외단일가현재가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_opentime',
                'length': '	6',
                'name': '시간외단일가시가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_open',
                'length': '	8',
                'name': '시간외단일가시가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_hightime',
                'length': '	6',
                'name': '시간외단일가고가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_high',
                'length': '	8',
                'name': '시간외단일가고가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_lowtime',
                'length': '	6',
                'name': '시간외단일가저가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_low',
                'length': '	8',
                'name': '시간외단일가저가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_cgubun',
                'length': '	1',
                'name': '시간외단일가체결구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_cvolume',
                'length': '	8',
                'name': '시간외단일가체결량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_volume',
                'length': '	12',
                'name': '시간외단일가누적거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_value',
                'length': '	12',
                'name': '시간외단일가누적거래대금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_mdvolume',
                'length': '	12',
                'name': '시간외단일가매도누적체결량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_mdchecnt',
                'length': '	8',
                'name': '시간외단일가매도누적체결건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_msvolume',
                'length': '	12',
                'name': '시간외단일가매수누적체결량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_mschecnt',
                'length': '	8',
                'name': '시간외단일가매수누적체결건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_prevolume',
                'length': '	8',
                'name': '시간외단일가직전거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_precvolume',
                'length': '	8',
                'name': '시간외단일가직전체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_cpower',
                'length': '	9.2',
                'name': '시간외단일가체결강도',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dan_status',
                'length': '	2',
                'name': '시간외단일가장정보',
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
    'DVI': {
        'tr_cd': 'DVI',
        'title': '시간외단일가VI발동해제',
        'fields': [
            {
                'key': 'vi_gubun',
                'length': '	1',
                'name': '구분(0:해제 1:정적발동 2:동적발동 3:정적&동적)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'svi_recprice',
                'length': '	8',
                'name': '정적VI발동기준가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dvi_recprice',
                'length': '	8',
                'name': '동적VI발동기준가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'vi_trgprice',
                'length': '	8',
                'name': 'VI발동가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': '	6',
                'name': '단축코드(KEY)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ref_shcode',
                'length': '	6',
                'name': '참조코드(미사용)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'time',
                'length': '	6',
                'name': '시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchname',
                'length': 3,
                'name': '거래소명',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'H1_': {
        'tr_cd': 'H1_',
        'title': 'KOSPI호가잔량',
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
                'key': 'shcode',
                'length': '	6',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'alloc_gubun',
                'length': '	1',
                'name': '배분적용구분',
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
                'key': 'midprice',
                'length': 8,
                'name': '중간가격  ',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offermidsumrem',
                'length': 9,
                'name': '매도중간가잔량합계수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidmidsumrem',
                'length': 9,
                'name': '매수중간가잔량합계수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'midsumrem',
                'length': 9,
                'name': '중간가잔량합계수량',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '\' \'없음<br/>\'1\'매도<br/>\'2\'매수<br/>',
                'key': 'midsumremgubun',
                'length': 1,
                'name': '중간가잔량구분',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'H2_': {
        'tr_cd': 'H2_',
        'title': 'KOSPI장전시간외호가잔량',
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
    'HA_': {
        'tr_cd': 'HA_',
        'title': 'KOSDAQ호가잔량',
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
                'key': 'shcode',
                'length': '	6',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'alloc_gubun',
                'length': '	1',
                'name': '배분적용구분',
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
                'key': 'midprice',
                'length': 8,
                'name': '중간가격 ',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offermidsumrem',
                'length': 9,
                'name': '매도중간가잔량합계수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidmidsumrem',
                'length': 9,
                'name': '매수중간가잔량합계수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'midsumrem',
                'length': 9,
                'name': '중간가잔량합계수량',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '\' \'없음<br/>\'1\'매도<br/>\'2\'매수',
                'key': 'midsumremgubun',
                'length': 1,
                'name': '중간가잔량구분',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'HB_': {
        'tr_cd': 'HB_',
        'title': 'KOSDAQ장전시간외호가잔량',
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
    'IJ_': {
        'tr_cd': 'IJ_',
        'title': '지수',
        'fields': [
            {
                'key': 'time',
                'length': '	6',
                'name': '시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jisu',
                'length': '	8.2',
                'name': '지수',
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
                'length': '	8.2',
                'name': '전일비',
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
                'key': 'cvolume',
                'length': '	8',
                'name': '체결량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volume',
                'length': '	8',
                'name': '거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'value',
                'length': '	8',
                'name': '거래대금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'upjo',
                'length': '	4',
                'name': '상한종목수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'highjo',
                'length': '	4',
                'name': '상승종목수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'unchgjo',
                'length': '	4',
                'name': '보합종목수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lowjo',
                'length': '	4',
                'name': '하락종목수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'downjo',
                'length': '	4',
                'name': '하한종목수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'upjrate',
                'length': '	6.2',
                'name': '상승종목비율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'openjisu',
                'length': '	8.2',
                'name': '시가지수',
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
                'key': 'highjisu',
                'length': '	8.2',
                'name': '고가지수',
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
                'key': 'lowjisu',
                'length': '	8.2',
                'name': '저가지수',
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
                'key': 'frgsvolume',
                'length': '	8',
                'name': '외인순매수수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'orgsvolume',
                'length': '	8',
                'name': '기관순매수수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'frgsvalue',
                'length': '	10',
                'name': '외인순매수금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'orgsvalue',
                'length': '	10',
                'name': '기관순매수금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'upcode',
                'length': '	3',
                'name': '업종코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'JIF': {
        'tr_cd': 'JIF',
        'title': '장운영정보',
        'fields': [
            {
                'desc': '1:코스피<br/>2:코스닥<br/>5:선물/옵션<br/>6:NXT전용<br/>8:KRX야간파생<br/>9:미국주식<br/>A:중국주식오전<br/>B:중국주식오후<br/>C:홍콩주식오전<br/>D:홍콩주식오후<br/>E:일본주식오전<br/>F:일본주식오후',
                'key': 'jangubun',
                'length': '	1',
                'name': '장구분',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '공통사용<br/>11:장전동시호가개시<br/>21:장시작<br/>22:장개시10초전<br/>23:장개시1분전<br/>24:장개시5분전<br/>25:장개시10분전<br/>31:장후동시호가개시<br/>41:장마감<br/>42:장마감10초전<br/>43:장마감1분전<br/>44:장마감5분전<br/>51:시간외종가매매개시<br/>52:시간외종가매매종료,시간외단일가매매개시<br/>53:사용안함<br/>54:시간외단일가매매종료<br/>55:프리마켓 개시<br/>A2:프리마켓 장개시,10초전<br/>A3:프리마켓 장개시,1분전<br/>A4:프리마켓 장개시,5분전<br/>A5:프리마켓 장개시,10분전<br/>56:에프터마켓 개시<br/>B2:에프터마켓 장개시,10초전<br/>B3:에프터마켓 장개시,1분전<br/>B4:에프터마켓 장개시,5분전<br/>B5:에프터마켓 장개시,10분전<br/>57:프리마켓 마감<br/>C2:프리마켓 장마감,10초전<br/>C3:프리마켓 장마감,1분전<br/>C4:프리마켓 장마감,5분전<br/>58:에프터마켓 마감<br/>D2:에프터마켓 장마감,10초전<br/>D3:에프터마켓 장마감,1분전<br/>D4:에프터마켓 장마감,5분전<br/>KOSPI / KOSDAQ (jangubun 1,2 인 경우)<br/>61:서킷브레이크1단계발동<br/>62:서킷브레이크1단계해제,호가접수개시<br/>63:서킷브레이크1단계,동시호가종료<br/>64:사이드카 매도발동<br/>65:사이드카 매도해제<br/>66:사이드카 매수발동<br/>67:사이드카 매수해제<br/>68:서킷브레이크2단계발동<br/>69:서킷브레이크3단계발동,당일 장종료<br/>70:서킷브레이크2단계해제,호가접수개시<br/>71:서킷브레이크2단계,동시호가종료<br/>선물/옵션 (jangubun 5인 경우)<br/>61:코스피관련파생상품,당일 장종료<br/>62:서킷브레이크 해제,호가접수개시<br/>63:서킷브레이크, 장중동시마감<br/>70:2단계상한가,5분 후 확대 예정<br/>71:2단계하한가,5분 후 확대 예정<br/>72:3단계상한가,5분 후 확대 예정<br/>73:3단계하한가,5분 후 확대 예정<br/>74:2단계상한가,확대 적용<br/>75:2단계하한가,확대 적용<br/>76:3단계상한가,확대 적용<br/>77:3단계하한가,확대 적용',
                'key': 'jstatus',
                'length': '	2',
                'name': '장상태',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'K1_': {
        'tr_cd': 'K1_',
        'title': 'KOSPI거래원',
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
            },
            {
                'key': 'tradmdval1',
                'length': 15,
                'name': '매도거래대금1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsval1',
                'length': 15,
                'name': '매수거래대금1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdavg1',
                'length': 7,
                'name': '매도평균단가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsavg1',
                'length': 7,
                'name': '매수평균단가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdval2',
                'length': 15,
                'name': '매도거래대금2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsval2',
                'length': 15,
                'name': '매수거래대금2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdavg2',
                'length': 7,
                'name': '매도평균단가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsavg2',
                'length': 7,
                'name': '매수평균단가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdval3',
                'length': 15,
                'name': '매도거래대금3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsval3',
                'length': 15,
                'name': '매수거래대금3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdavg3',
                'length': 7,
                'name': '매도평균단가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsavg3',
                'length': 7,
                'name': '매수평균단가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdval4',
                'length': 15,
                'name': '매도거래대금4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsval4',
                'length': 15,
                'name': '매수거래대금4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdavg4',
                'length': 7,
                'name': '매도평균단가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsavg4',
                'length': 7,
                'name': '매수평균단가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdval5',
                'length': 15,
                'name': '매도거래대금5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsval5',
                'length': 15,
                'name': '매수거래대금5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdavg5',
                'length': 7,
                'name': '매도평균단가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsavg5',
                'length': 7,
                'name': '매수평균단가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmdval',
                'length': 15,
                'name': '외국계증권사매도거래대금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmsval',
                'length': 15,
                'name': '외국계증권사매수거래대금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmdavg',
                'length': '	7',
                'name': '외국계증권사매도평균단가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmsavg',
                'length': '	7',
                'name': '외국계증권사매수평균단가',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'K3_': {
        'tr_cd': 'K3_',
        'title': 'KOSDAQ체결',
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
                'desc': '+ : 매수<br/>- : 매도',
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
                'key': 'shcode',
                'length': '	6',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchname',
                'length': 3,
                'name': '거래소명',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'KH_': {
        'tr_cd': 'KH_',
        'title': 'KOSDAQ프로그램매매종목별',
        'fields': [
            {
                'key': 'time',
                'length': 6,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'price',
                'length': 8,
                'name': '현재가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sign',
                'length': 1,
                'name': '전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': 8,
                'name': '전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volume',
                'length': 10,
                'name': '누적거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'drate',
                'length': 6.2,
                'name': '등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdhrem',
                'length': 12,
                'name': '차익매도호가 잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cshrem',
                'length': 12,
                'name': '차익매수호가 잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdhrem',
                'length': 12,
                'name': '비차익매도호가 잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bshrem',
                'length': 12,
                'name': '비차익매수호가 잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdhvolume',
                'length': 12,
                'name': '차익매도호가 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cshvolume',
                'length': 12,
                'name': '차익매수호가 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdhvolume',
                'length': 12,
                'name': '비차익매도호가 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bshvolume',
                'length': 12,
                'name': '비차익매수호가 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dwcvolume',
                'length': 12,
                'name': '전체매도위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'swcvolume',
                'length': 12,
                'name': '전체매수위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'djcvolume',
                'length': 12,
                'name': '전체매도자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sjcvolume',
                'length': 12,
                'name': '전체매수자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tdvolume',
                'length': 12,
                'name': '전체매도체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tsvolume',
                'length': 12,
                'name': '전체매수체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tvol',
                'length': 12,
                'name': '전체순매수 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dwcvalue',
                'length': 15,
                'name': '전체매도위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'swcvalue',
                'length': 15,
                'name': '전체매수위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'djcvalue',
                'length': 15,
                'name': '전체매도자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sjcvalue',
                'length': 15,
                'name': '전체매수자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tdvalue',
                'length': 15,
                'name': '전체매도체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tsvalue',
                'length': 15,
                'name': '전체매수체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tval',
                'length': 15,
                'name': '전체순매수 금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'pdgvolume',
                'length': 12,
                'name': '매도 사전공시수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'psgvolume',
                'length': 12,
                'name': '매수 사전공시수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': 6,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'KM_': {
        'tr_cd': 'KM_',
        'title': 'KOSDAQ프로그램매매전체집계',
        'fields': [
            {
                'key': 'time',
                'length': 6,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdhrem',
                'length': 6,
                'name': '차익매도호가 잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cshrem',
                'length': 6,
                'name': '차익매수호가 잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdhrem',
                'length': 6,
                'name': '비차익매도호가 잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bshrem',
                'length': 6,
                'name': '비차익매수호가 잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdhvolume',
                'length': 6,
                'name': '차익매도호가 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cshvolume',
                'length': 6,
                'name': '차익매수호가 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdhvolume',
                'length': 6,
                'name': '비차익매도호가 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bshvolume',
                'length': 6,
                'name': '비차익매수호가 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdwvolume',
                'length': 6,
                'name': '차익매도위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdjvolume',
                'length': 6,
                'name': '차익매도자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cswvolume',
                'length': 6,
                'name': '차익매수위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'csjvolume',
                'length': 6,
                'name': '차익매수자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cwvol',
                'length': 6,
                'name': '차익위탁순매수 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cjvol',
                'length': 6,
                'name': '차익자기순매수 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdwvolume',
                'length': 6,
                'name': '비차익매도위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdjvolume',
                'length': 6,
                'name': '비차익매도자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bswvolume',
                'length': 6,
                'name': '비차익매수위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bsjvolume',
                'length': 6,
                'name': '비차익매수자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bwvol',
                'length': 6,
                'name': '비차익위탁순매수 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bjvol',
                'length': 6,
                'name': '비차익자기순매수 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dwvolume',
                'length': 6,
                'name': '전체매도위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'swvolume',
                'length': 6,
                'name': '전체매수위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'wvol',
                'length': 6,
                'name': '전체위탁순매수 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'djvolume',
                'length': 6,
                'name': '전체매도자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sjvolume',
                'length': 6,
                'name': '전체매수자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jvol',
                'length': 6,
                'name': '전체자기순매수 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdwvalue',
                'length': 8,
                'name': '차익매도위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdjvalue',
                'length': 8,
                'name': '차익매도자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cswvalue',
                'length': 8,
                'name': '차익매수위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'csjvalue',
                'length': 8,
                'name': '차익매수자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cwval',
                'length': 8,
                'name': '차익위탁순매수 금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cjval',
                'length': 8,
                'name': '차익자기순매수 금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdwvalue',
                'length': 8,
                'name': '비차익매도위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdjvalue',
                'length': 8,
                'name': '비차익매도자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bswvalue',
                'length': 8,
                'name': '비차익매수위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bsjvalue',
                'length': 8,
                'name': '비차익매수자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bwval',
                'length': 8,
                'name': '비차익위탁순매수 금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bjval',
                'length': 8,
                'name': '비차익자기순매수 금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dwvalue',
                'length': 8,
                'name': '전체매도위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'swvalue',
                'length': 8,
                'name': '전체매수위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'wval',
                'length': 8,
                'name': '전체위탁순매수 금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'djvalue',
                'length': 8,
                'name': '전체매도자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sjvalue',
                'length': 8,
                'name': '전체매수자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jval',
                'length': 8,
                'name': '전체자기순매수 금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'k50jisu',
                'length': 6.2,
                'name': 'KOSDAQ50 지수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'k50sign',
                'length': 1,
                'name': 'KOSDAQ50 전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': 6.2,
                'name': 'KOSDAQ50 전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'k50basis',
                'length': 4.2,
                'name': 'KOSDAQ50 베이시스',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdvolume',
                'length': 6,
                'name': '차익매도체결수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'csvolume',
                'length': 6,
                'name': '차익매수체결수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cvol',
                'length': 6,
                'name': '차익순매수 수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdvolume',
                'length': 6,
                'name': '비차익매도체결수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bsvolume',
                'length': 6,
                'name': '비차익매수체결수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bvol',
                'length': 6,
                'name': '비차익순매수 수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tdvolume',
                'length': 6,
                'name': '전체매도체결수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tsvolume',
                'length': 6,
                'name': '전체매수체결수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tvol',
                'length': 6,
                'name': '전체순매수 수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdvalue',
                'length': 8,
                'name': '차익매도체결금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'csvalue',
                'length': 8,
                'name': '차익매수체결금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cval',
                'length': 8,
                'name': '차익순매수 금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdvalue',
                'length': 8,
                'name': '비차익매도체결금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bsvalue',
                'length': 8,
                'name': '비차익매수체결금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bval',
                'length': 8,
                'name': '비차익순매수 금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tdvalue',
                'length': 8,
                'name': '전체매도체결금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tsvalue',
                'length': 8,
                'name': '전체매수체결금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tval',
                'length': 8,
                'name': '전체순매수 금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_cdvolcha',
                'length': 6,
                'name': '차익매도체결수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_csvolcha',
                'length': 6,
                'name': '차익매수체결수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_cvolcha',
                'length': 6,
                'name': '차익순매수 수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_bdvolcha',
                'length': 6,
                'name': '비차익매도체결수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_bsvolcha',
                'length': 6,
                'name': '비차익매수체결수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_bvolcha',
                'length': 6,
                'name': '비차익순매수 수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_tdvolcha',
                'length': 6,
                'name': '전체매도체결수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_tsvolcha',
                'length': 6,
                'name': '전체매수체결수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_tvolcha',
                'length': 6,
                'name': '전체순매수 수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_cdvalcha',
                'length': 8,
                'name': '차익매도체결금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_csvalcha',
                'length': 8,
                'name': '차익매수체결금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_cvalcha',
                'length': 8,
                'name': '차익순매수 금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_bdvalcha',
                'length': 8,
                'name': '비차익매도체결금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_bsvalcha',
                'length': 8,
                'name': '비차익매수체결금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_bvalcha',
                'length': 8,
                'name': '비차익순매수 금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_tdvalcha',
                'length': 8,
                'name': '전체매도체결금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_tsvalcha',
                'length': 8,
                'name': '전체매수체결금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_tvalcha',
                'length': 8,
                'name': '전체순매수 금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'gubun',
                'length': 1,
                'name': '구분값',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'KS_': {
        'tr_cd': 'KS_',
        'title': 'KOSDAQ우선호가',
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
    'MK2': {
        'tr_cd': 'MK2',
        'title': 'US지수',
        'fields': [
            {
                'key': 'date',
                'length': '	8',
                'name': '일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'time',
                'length': '	6',
                'name': '시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'kodate',
                'length': '	8',
                'name': '한국일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'kotime',
                'length': '	6',
                'name': '한국시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'open',
                'length': '	9.2',
                'name': '시가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'high',
                'length': '	9.2',
                'name': '고가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low',
                'length': '	9.2',
                'name': '저가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'price',
                'length': '	9.2',
                'name': '현재가',
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
                'length': '	9.2',
                'name': '전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'uprate',
                'length': '	9.2',
                'name': '등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho',
                'length': '	9.2',
                'name': '매수호가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem',
                'length': '	9',
                'name': '매수잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho',
                'length': '	9.2',
                'name': '매도호가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem',
                'length': '	9',
                'name': '매도잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volume',
                'length': '	12.0',
                'name': '누적거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'xsymbol',
                'length': '	16',
                'name': '심벌',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cvolume',
                'length': '	8.0',
                'name': '체결거래량',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'NBM': {
        'tr_cd': 'NBM',
        'title': '(NXT)업종별투자자별매매현황',
        'fields': [
            {
                'key': 'tjjcode',
                'length': 4,
                'name': '투자자코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjtime',
                'length': 8,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume',
                'length': 8,
                'name': '매수거래량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume',
                'length': 8,
                'name': '매도거래량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol',
                'length': 8,
                'name': '거래량순매수',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_msvol',
                'length': 8,
                'name': '거래량순매수직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue',
                'length': 6,
                'name': '매수거래대금',
                'required': True,
                'type': 'float'
            },
            {
                'key': '매도거래대금',
                'length': 6,
                'name': '매도거래대금',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval',
                'length': 6,
                'name': '거래대금순매수',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_msval',
                'length': 6,
                'name': '거래대금순매수직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'upcode',
                'length': 3,
                'name': '업종코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_upcode',
                'length': 4,
                'name': '거래소별업종코드',
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
                'key': 'tjjtime',
                'length': 8,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode1',
                'length': 4,
                'name': '투자자코드1(개인)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume1',
                'length': 8,
                'name': '매수거래량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume1',
                'length': 8,
                'name': '매도거래량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol1',
                'length': 8,
                'name': '거래량순매수1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue1',
                'length': 6,
                'name': '매수거래대금1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue1',
                'length': 6,
                'name': '매도거래대금1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval1',
                'length': 6,
                'name': '거래대금순매수1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode2',
                'length': None,
                'name': '투자자코드2(외국인)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume2',
                'length': 8,
                'name': '매수거래량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume2',
                'length': 8,
                'name': '매도거래량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol2',
                'length': 8,
                'name': '거래량순매수2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue2',
                'length': 6,
                'name': '매수거래대금2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue2',
                'length': 6,
                'name': '매도거래대금2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval2',
                'length': 6,
                'name': '거래대금순매수2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode3',
                'length': 4,
                'name': '투자자코드3(기관계)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume3',
                'length': 8,
                'name': '매수거래량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume3',
                'length': 8,
                'name': '매도거래량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol3',
                'length': 8,
                'name': '거래량순매수3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue3',
                'length': 6,
                'name': '매수거래대금3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue3',
                'length': 6,
                'name': '매도거래대금3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval3',
                'length': 6,
                'name': '거래대금순매수3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode4',
                'length': 4,
                'name': '투자자코드4(증권)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume4',
                'length': 8,
                'name': '매수거래량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume4',
                'length': 8,
                'name': '매도거래량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol4',
                'length': 8,
                'name': '거래량순매수4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue4',
                'length': 6,
                'name': '매수거래대금4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue4',
                'length': 6,
                'name': '매도거래대금4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval4',
                'length': 6,
                'name': '거래대금순매수4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode5',
                'length': 4,
                'name': '투자자코드5(투신)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume5',
                'length': 8,
                'name': '매수거래량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume5',
                'length': 8,
                'name': '매도거래량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol5',
                'length': 8,
                'name': '거래량순매수5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue5',
                'length': 6,
                'name': '매수거래대금5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue5',
                'length': 6,
                'name': '매도거래대금5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval5',
                'length': 6,
                'name': '거래대금순매수5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode6',
                'length': 4,
                'name': '투자자코드6(은행)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume6',
                'length': 8,
                'name': '매수거래량6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume6',
                'length': 8,
                'name': '매도거래량6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol6',
                'length': 8,
                'name': '거래량순매수6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue6',
                'length': 6,
                'name': '매수거래대금6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue6',
                'length': 6,
                'name': '매도거래대금6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval6',
                'length': 6,
                'name': '거래대금순매수6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode7',
                'length': 4,
                'name': '투자자코드7(보험)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume7',
                'length': 8,
                'name': '매수거래량7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume7',
                'length': 8,
                'name': '매도거래량7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol7',
                'length': 8,
                'name': '거래량순매수7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue7',
                'length': 6,
                'name': '매수거래대금7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue7',
                'length': 6,
                'name': '매도거래대금7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval7',
                'length': 6,
                'name': '거래대금순매수7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode8',
                'length': 4,
                'name': '투자자코드8(종금)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume8',
                'length': 8,
                'name': '매수거래량8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume8',
                'length': 8,
                'name': '매도거래량8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol8',
                'length': 8,
                'name': '거래량순매수8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue8',
                'length': 6,
                'name': '매수거래대금8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue8',
                'length': 6,
                'name': '매도거래대금8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval8',
                'length': 6,
                'name': '거래대금순매수8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode9',
                'length': 4,
                'name': '투자자코드9(기금)',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvolume9',
                'length': 8,
                'name': '매수거래량9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume9',
                'length': 8,
                'name': '매도거래량9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol9',
                'length': 8,
                'name': '거래량순매수9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue9',
                'length': 6,
                'name': '매수거래대금9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue9',
                'length': 6,
                'name': '매도거래대금9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval9',
                'length': 6,
                'name': '거래대금순매수9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode10',
                'length': 4,
                'name': '투자자코드10(선물업자)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume10',
                'length': 8,
                'name': '매수거래량10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume10',
                'length': 8,
                'name': '매도거래량10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol10',
                'length': 8,
                'name': '거래량순매수10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue10',
                'length': 8,
                'name': '매수거래대금10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue10',
                'length': 6,
                'name': '매도거래대금10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval10',
                'length': 6,
                'name': '거래대금순매수10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode11',
                'length': 4,
                'name': '투자자코드11(기타)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume11',
                'length': 8,
                'name': '매수거래량11',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume11',
                'length': 8,
                'name': '매도거래량11',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol11',
                'length': 8,
                'name': '거래량순매수11',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue11',
                'length': 6,
                'name': '매수거래대금11',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue11',
                'length': 6,
                'name': '매도거래대금11',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval11',
                'length': 6,
                'name': '거래대금순매수11',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'upcode',
                'length': 3,
                'name': '업종코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode0',
                'length': 4,
                'name': '투자자코드0(사모펀드)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume0',
                'length': 8,
                'name': '매수거래량0',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume0',
                'length': 8,
                'name': '매도거래량0',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol0',
                'length': 8,
                'name': '거래량순매수0',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue0',
                'length': 6,
                'name': '매수거래대금0',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue0',
                'length': 6,
                'name': '매도거래대금0',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval0',
                'length': 6,
                'name': '거래대금순매수0',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ex_upcode',
                'length': 4,
                'name': '거래소별업종코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'NH1': {
        'tr_cd': 'NH1',
        'title': '(NXT)호가잔량',
        'fields': [
            {
                'key': 'hotime',
                'length': 6,
                'name': '호가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho1',
                'length': 7,
                'name': '매도호가1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho1',
                'length': 7,
                'name': '매수호가1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerrem1',
                'length': 9,
                'name': '매도호가잔량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidrem1',
                'length': 9,
                'name': '매수호가잔량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho2',
                'length': 7,
                'name': '매도호가2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho2',
                'length': 7,
                'name': '매수호가2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerrem2',
                'length': 9,
                'name': '매도호가잔량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidrem2',
                'length': 9,
                'name': '매수호가잔량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho3',
                'length': 7,
                'name': '매도호가3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho3',
                'length': 7,
                'name': '매수호가3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerrem3',
                'length': 9,
                'name': '매도호가잔량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidrem3',
                'length': 9,
                'name': '매수호가잔량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho4',
                'length': 7,
                'name': '매도호가4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho4',
                'length': 7,
                'name': '매수호가4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerrem4',
                'length': 9,
                'name': '매도호가잔량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidrem4',
                'length': 9,
                'name': '매수호가잔량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho5',
                'length': 7,
                'name': '매도호가5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho5',
                'length': 7,
                'name': '매수호가5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerrem5',
                'length': 9,
                'name': '매도호가잔량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidrem5',
                'length': 9,
                'name': '매수호가잔량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho6',
                'length': 7,
                'name': '매도호가6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho6',
                'length': 7,
                'name': '매수호가6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerrem6',
                'length': 9,
                'name': '매도호가잔량6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidrem6',
                'length': 9,
                'name': '매수호가잔량6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho7',
                'length': 7,
                'name': '매도호가7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho7',
                'length': 7,
                'name': '매수호가7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerrem7',
                'length': 9,
                'name': '매도호가잔량7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidrem7',
                'length': 9,
                'name': '매수호가잔량7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho8',
                'length': 7,
                'name': '매도호가8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho8',
                'length': 7,
                'name': '매수호가8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerrem8',
                'length': 9,
                'name': '매도호가잔량8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidrem8',
                'length': 9,
                'name': '매수호가잔량8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho9',
                'length': 7,
                'name': '매도호가9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho9',
                'length': 7,
                'name': '매수호가9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerrem9',
                'length': 9,
                'name': '매도호가잔량9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidrem9',
                'length': 9,
                'name': '매수호가잔량9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho10',
                'length': 7,
                'name': '매도호가10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho10',
                'length': 7,
                'name': '매수호가10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerrem10',
                'length': 9,
                'name': '매도호가잔량10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidrem10',
                'length': 9,
                'name': '매수호가잔량10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'totofferrem',
                'length': 9,
                'name': '총매도호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'totbidrem',
                'length': 9,
                'name': '총매수호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'donsigubun',
                'length': 1,
                'name': '동시호가구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': 9,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'alloc_gubun',
                'length': 1,
                'name': '배분적용구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volume',
                'length': 12,
                'name': '누적거래량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'midprice',
                'length': 8,
                'name': '중간가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offermidsumrem',
                'length': 9,
                'name': '매도중간가잔량합계수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidmidsumrem',
                'length': 9,
                'name': '매수중간가잔량합계수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'midsumrem',
                'length': 9,
                'name': '중간가잔량합계수량',
                'required': True,
                'type': 'float'
            },
            {
                'desc': '\'\'없음\'1\'매도\'2\'매수',
                'key': 'midsumremgubun',
                'length': 1,
                'name': '중간가잔량구분(\'\'없음\'1\'매도\'2\'매수)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_shcode',
                'length': 10,
                'name': '거래소별단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'NK1': {
        'tr_cd': 'NK1',
        'title': '(NXT)거래원',
        'fields': [
            {
                'key': 'offerno1',
                'length': 3,
                'name': '매도증권사코드1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno1',
                'length': 3,
                'name': '매수증권사코드1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad1',
                'length': 6,
                'name': '매도회원사명1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad1',
                'length': 6,
                'name': '매수회원사명1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol1',
                'length': 10,
                'name': '매도거래량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsvol1',
                'length': 10,
                'name': '매수거래량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdrate1',
                'length': 6.2,
                'name': '매도거래량비중1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsrate1',
                'length': 6.2,
                'name': '매도거래량비중1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdcha1',
                'length': 10,
                'name': '매도거래량직전대비1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmscha1',
                'length': 10,
                'name': '매수거래량직전대비1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerno2',
                'length': 3,
                'name': '매도증권사코드2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno2',
                'length': 3,
                'name': '매수증권사코드2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad2',
                'length': 6,
                'name': '매도회원사명2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad2',
                'length': 6,
                'name': '매수회원사명2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol2',
                'length': 10,
                'name': '매도거래량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsvol2',
                'length': 10,
                'name': '매수거래량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdrate2',
                'length': 6.2,
                'name': '매도거래량비중2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsrate2',
                'length': 6.2,
                'name': '매수거래량비중2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdcha2',
                'length': 10,
                'name': '매도거래량직전대비2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmscha2',
                'length': 10,
                'name': '매수거래량직전대비2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerno3',
                'length': 3,
                'name': '매도증권사코드3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno3',
                'length': 3,
                'name': '매수증권사코드3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad3',
                'length': 6,
                'name': '매도회원사명3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad3',
                'length': 6,
                'name': '매수회원사명3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol3',
                'length': 10,
                'name': '매도거래량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsvol3',
                'length': 10,
                'name': '매수거래량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdrate3',
                'length': 6.2,
                'name': '매도거래량비중3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsrate3',
                'length': 6.2,
                'name': '매수거래량비중3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdcha3',
                'length': 10,
                'name': '매도거래량직전대비3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmscha3',
                'length': 10,
                'name': '매수거래량직전대비3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerno4',
                'length': 3,
                'name': '매도증권사코드4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno4',
                'length': 3,
                'name': '매수증권사코드4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad4',
                'length': 6,
                'name': '매도회원사명4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad4',
                'length': 6,
                'name': '매수회원사명4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol4',
                'length': 10,
                'name': '매도거래량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsvol4',
                'length': 10,
                'name': '매수거래량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdrate4',
                'length': 6.2,
                'name': '매도거래량비중4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsrate4',
                'length': 6.2,
                'name': '매수거래량비중4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdcha4',
                'length': 10,
                'name': '매도거래량직전대비4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmscha4',
                'length': 10,
                'name': '매수거래량직전대비4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerno5',
                'length': 3,
                'name': '매도증권사코드5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno5',
                'length': 3,
                'name': '매수증권사코드5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad5',
                'length': 6,
                'name': '매도회원사명5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad5',
                'length': 6,
                'name': '매수회원사명5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol5',
                'length': 10,
                'name': '매도거래량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsvol5',
                'length': 10,
                'name': '매수거래량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdrate5',
                'length': 6.2,
                'name': '매도거래량비중5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsrate5',
                'length': 6.2,
                'name': '매수거래량비중5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdcha5',
                'length': 10,
                'name': '매도거래량직전대비5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmscha5',
                'length': 10,
                'name': '매수거래량직전대비5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmdvol',
                'length': 10,
                'name': '외국계증권사매도합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmsvol',
                'length': 10,
                'name': '외국계증권사매수합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmdrate',
                'length': 6.2,
                'name': '외국계증권사매도거래량비중',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmsrate',
                'length': 6.2,
                'name': '외국계증권사매수거래량비중',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmdcha',
                'length': 10,
                'name': '외국계증권사매도거래량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmscha',
                'length': 10,
                'name': '외국계증권사매수거래량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'shcode',
                'length': 9,
                'name': '단축코드',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdval1',
                'length': 15,
                'name': '매도거래대금1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsval1',
                'length': 15,
                'name': '매수거래대금1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdavg1',
                'length': 7,
                'name': '매도평균단가1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsavg1',
                'length': 7,
                'name': '매수평균단가1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdval2',
                'length': 15,
                'name': '매도거래대금2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsval2',
                'length': 15,
                'name': '매수거래대금2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdavg2',
                'length': 7,
                'name': '매도평균단가2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsavg2',
                'length': 7,
                'name': '매수평균단가2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdval3',
                'length': 15,
                'name': '매도거래대금3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsval3',
                'length': 15,
                'name': '매수거래대금3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdavg3',
                'length': 7,
                'name': '매도평균단가3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsavg3',
                'length': 7,
                'name': '매수평균단가3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdval4',
                'length': 15,
                'name': '매도거래대금4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsval4',
                'length': 15,
                'name': '매수거래대금4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdavg4',
                'length': 7,
                'name': '매도평균단가4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsavg4',
                'length': 7,
                'name': '매수평균단가4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdval5',
                'length': 15,
                'name': '매도거래대금5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsval5',
                'length': 15,
                'name': '매수거래대금5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdavg5',
                'length': 7,
                'name': '매도평균단가5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsavg5',
                'length': 7,
                'name': '매수평균단가5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmdval',
                'length': 15,
                'name': '외국계증권사매도거래대금',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmsval',
                'length': 15,
                'name': '외국계증권사매수거래대금',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmdavg',
                'length': 7,
                'name': '외국계증권사매도평균단가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmsavg',
                'length': 7,
                'name': '외국계증권사매수평균단가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'time',
                'length': 6,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchname',
                'length': 3,
                'name': '거래소명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_shcode',
                'length': 10,
                'name': '거래소별단축코드',
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
                'key': 'time',
                'length': 6,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'price',
                'length': 8,
                'name': '현재가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'sign',
                'length': 1,
                'name': '전일대비구분',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'change',
                'length': 8,
                'name': '전일대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'volume',
                'length': 10,
                'name': '누적거래량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'drate',
                'length': 6.2,
                'name': '등락율',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdhrem',
                'length': 12,
                'name': '차익매도호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cshrem',
                'length': 12,
                'name': '차익매수호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdhrem',
                'length': 12,
                'name': '비차익매도호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bshrem',
                'length': 12,
                'name': '비차익매수호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdhvolume',
                'length': 12,
                'name': '차익매도호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cshvolume',
                'length': 12,
                'name': '차익매수호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdhvolume',
                'length': 12,
                'name': '비차익매도호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bshvolume',
                'length': 12,
                'name': '비차익매수호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'dwcvolume',
                'length': 12,
                'name': '전체매도위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'swcvolume',
                'length': 12,
                'name': '전체매수위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'djcvolume',
                'length': 12,
                'name': '전체매도자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'sjcvolume',
                'length': 12,
                'name': '전체매수자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tdvolume',
                'length': 12,
                'name': '전체매도체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tsvolume',
                'length': 12,
                'name': '전체매수체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tvol',
                'length': 12,
                'name': '전체순매수수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'dwcvalue',
                'length': 15,
                'name': '전체매도위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'swcvalue',
                'length': 15,
                'name': '전체매수위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'djcvalue',
                'length': 15,
                'name': '전체매도자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'sjcvalue',
                'length': 15,
                'name': '전체매수자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tdvalue',
                'length': 15,
                'name': '전체매도체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tsvalue',
                'length': 15,
                'name': '전체매수체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tval',
                'length': 15,
                'name': '전체순매수금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'pdgvolume',
                'length': 12,
                'name': '매도사전공시수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'psgvolume',
                'length': 12,
                'name': '매수사전공시수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'shcode',
                'length': 12,
                'name': '종목코드',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ex_shcode',
                'length': 10,
                'name': '거래소별단축코드',
                'required': True,
                'type': 'float'
            }
        ]
    },
    'NPM': {
        'tr_cd': 'NPM',
        'title': '(NXT)프로그램매매전체집계',
        'fields': [
            {
                'key': 'time',
                'length': 6,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdhrem',
                'length': 6,
                'name': '차익매도호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cshrem',
                'length': 6,
                'name': '차익매수호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdhrem',
                'length': 6,
                'name': '비차익매도호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bshrem',
                'length': 6,
                'name': '비차익매수호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdhvolume',
                'length': 6,
                'name': '차익매도호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cshvolume',
                'length': 6,
                'name': '차익매수호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdhvolume',
                'length': 6,
                'name': '비차익매도호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bshvolume',
                'length': 6,
                'name': '비차익매수호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdwvolume',
                'length': 6,
                'name': '차익매도위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdjvolume',
                'length': 6,
                'name': '차익매도자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cswvolume',
                'length': 6,
                'name': '차익매수위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'csjvolume',
                'length': 6,
                'name': '차익매수자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cwvol',
                'length': 6,
                'name': '차익위탁순매수수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cjvol',
                'length': 6,
                'name': '차익자기순매수수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdwvolume',
                'length': 6,
                'name': '비차익매도위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdjvolume',
                'length': 6,
                'name': '비차익매도자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bswvolume',
                'length': 6,
                'name': '비차익매수위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bsjvolume',
                'length': 6,
                'name': '비차익매수자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bwvol',
                'length': 6,
                'name': '비차익위탁순매수수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bjvol',
                'length': 6,
                'name': '비차익자기순매수수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'dwvolume',
                'length': 6,
                'name': '전체매도위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'swvolume',
                'length': 6,
                'name': '전체매수위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'wvol',
                'length': 6,
                'name': '전체위탁순매수수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'djvolume',
                'length': 6,
                'name': '전체매도자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'sjvolume',
                'length': 6,
                'name': '전체매수자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'jvol',
                'length': 6,
                'name': '전체자기순매수수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdwvalue',
                'length': 8,
                'name': '차익매도위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdjvalue',
                'length': 8,
                'name': '차익매도자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cswvalue',
                'length': 8,
                'name': '차익매수위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'csjvalue',
                'length': 8,
                'name': '차익매수자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cwval',
                'length': 8,
                'name': '차익위탁순매수금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cjval',
                'length': 8,
                'name': '차익자기순매수금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdwvalue',
                'length': 8,
                'name': '비차익매도위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdjvalue',
                'length': 8,
                'name': '비차익매도자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bswvalue',
                'length': 8,
                'name': '비차익매수위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bsjvalue',
                'length': 8,
                'name': '비차익매수자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bwval',
                'length': 8,
                'name': '비차익위탁순매수금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bjval',
                'length': 8,
                'name': '비차익자기순매수금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'dwvalue',
                'length': 8,
                'name': '전체매도위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'swvalue',
                'length': 8,
                'name': '전체매수위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'wval',
                'length': 8,
                'name': '전체위탁순매수금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'djvalue',
                'length': 8,
                'name': '전체매도자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'sjvalue',
                'length': 8,
                'name': '전체매수자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'jval',
                'length': 8,
                'name': '전체자기순매수금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'k200jisu',
                'length': 6.2,
                'name': 'KOSPI200지수',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'k200sign',
                'length': 1,
                'name': 'KOSPI200전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': 6.2,
                'name': 'KOSPI200전일대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'k200basis',
                'length': 4.2,
                'name': 'KOSPI200베이시스',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdvolume',
                'length': 6,
                'name': '차익매도체결수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'csvolume',
                'length': 6,
                'name': '차익매수체결수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cvol',
                'length': 6,
                'name': '차익순매수수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdvolume',
                'length': 6,
                'name': '비차익매도체결수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bsvolume',
                'length': 6,
                'name': '비차익매수체결수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bvol',
                'length': 6,
                'name': '비차익순매수수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tdvolume',
                'length': 6,
                'name': '전체매도체결수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tsvolume',
                'length': 6,
                'name': '전체매수체결수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tvol',
                'length': 6,
                'name': '전체순매수수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdvalue',
                'length': 8,
                'name': '차익매도체결금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'csvalue',
                'length': 8,
                'name': '차익매수체결금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cval',
                'length': 8,
                'name': '차익순매수금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdvalue',
                'length': 8,
                'name': '비차익매도체결금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bsvalue',
                'length': 8,
                'name': '비차익매수체결금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bval',
                'length': 8,
                'name': '비차익순매수금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tdvalue',
                'length': 8,
                'name': '전체매도체결금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tsvalue',
                'length': 8,
                'name': '전체매수체결금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tval',
                'length': 8,
                'name': '전체순매수금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_cdvolcha',
                'length': 6,
                'name': '차익매도체결수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_csvolcha',
                'length': 6,
                'name': '차익매수체결수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_cvolcha',
                'length': 6,
                'name': '차익순매수수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_bdvolcha',
                'length': 6,
                'name': '비차익매도체결수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_bsvolcha',
                'length': 6,
                'name': '비차익매수체결수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_bvolcha',
                'length': 6,
                'name': '비차익순매수수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_tdvolcha',
                'length': 6,
                'name': '전체매도체결수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_tsvolcha',
                'length': 6,
                'name': '전체매수체결수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_tvolcha',
                'length': 6,
                'name': '전체순매수수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_cdvalcha',
                'length': 8,
                'name': '차익매도체결금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_csvalcha',
                'length': 8,
                'name': '차익매수체결금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_cvalcha',
                'length': 8,
                'name': '차익순매수금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_bdvalcha',
                'length': 8,
                'name': '비차익매도체결금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_bsvalcha',
                'length': 8,
                'name': '비차익매수체결금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_bvalcha',
                'length': 8,
                'name': '비차익순매수금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_tdvalcha',
                'length': 8,
                'name': '전체매도체결금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_tsvalcha',
                'length': 8,
                'name': '전체매수체결금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_tvalcha',
                'length': 8,
                'name': '전체순매수금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'gubun',
                'length': 1,
                'name': '구분값',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_gubun',
                'length': 2,
                'name': '거래소별구분값',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'NS2': {
        'tr_cd': 'NS2',
        'title': '(NXT)우선호가',
        'fields': [
            {
                'key': 'offerho',
                'length': 8,
                'name': '매도호가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho',
                'length': 8,
                'name': '매수호가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'shcode',
                'length': 9,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_shcode',
                'length': 10,
                'name': '거래소별단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'NS3': {
        'tr_cd': 'NS3',
        'title': '(NXT)체결',
        'fields': [
            {
                'key': 'chetime',
                'length': 6,
                'name': '체결시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sign',
                'length': 1,
                'name': '전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': 8,
                'name': '전일대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'drate',
                'length': 6.2,
                'name': '등락율',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'price',
                'length': 8,
                'name': '현재가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'opentime',
                'length': 6,
                'name': '시가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'open',
                'length': 8,
                'name': '시가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'hightime',
                'length': 8,
                'name': '고가시간',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'lowtime',
                'length': 6,
                'name': '저가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low',
                'length': 8,
                'name': '저가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cgubun',
                'length': 1,
                'name': '체결구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cvolume',
                'length': 8,
                'name': '체결량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'volume',
                'length': 12,
                'name': '누적거래량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'value',
                'length': 12,
                'name': '누적거래대금',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume',
                'length': 12,
                'name': '매도누적체결량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdchecnt',
                'length': 8,
                'name': '매도누적체결건수',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvolume',
                'length': 12,
                'name': '매수누적체결량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mschecnt',
                'length': 8,
                'name': '매수누적체결건수',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cpower',
                'length': 9.2,
                'name': '체결강도',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'w_avrg',
                'length': 8,
                'name': '가중평균가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho',
                'length': 8,
                'name': '매도호가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho',
                'length': 8,
                'name': '매수호가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'status',
                'length': 2,
                'name': '장정보',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jnilvolume',
                'length': 12,
                'name': '전일동시간대거래량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'shcode',
                'length': 9,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchname',
                'length': 3,
                'name': '거래소명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_shcode',
                'length': 10,
                'name': '거래소별단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'NVI': {
        'tr_cd': 'NVI',
        'title': '(NXT)VI 발동 해제',
        'fields': [
            {
                'desc': '0:해제1:정적발동2:동적발동3:정적&동적',
                'key': 'vi_gubun',
                'length': 1,
                'name': '구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'svi_recprice',
                'length': 8,
                'name': '정적VI발동기준가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'dvi_recprice',
                'length': 8,
                'name': '동적VI발동기준가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'vi_trgprice',
                'length': 8,
                'name': 'VI발동가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'shcode',
                'length': 9,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ref_shcode',
                'length': 6,
                'name': '참조코드(미사용)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'time',
                'length': 6,
                'name': '시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchname',
                'length': 3,
                'name': '거래소명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_shcode',
                'length': 10,
                'name': '거래소별단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'NWS': {
        'tr_cd': 'NWS',
        'title': '실시간뉴스제목패킷',
        'fields': [
            {
                'key': 'date',
                'length': 8,
                'name': '날짜',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'time',
                'length': 6,
                'name': '시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'id',
                'length': 2,
                'name': '뉴스구분자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'realkey',
                'length': '	24',
                'name': '키값',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'title',
                'length': '	300',
                'name': '제목',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'code',
                'length': '	240',
                'name': '단축종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bodysize',
                'length': '	8',
                'name': 'BODY길이',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'NYS': {
        'tr_cd': 'NYS',
        'title': '(NXT)예상체결',
        'fields': [
            {
                'key': 'hotime',
                'length': 6,
                'name': '호가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'yeprice',
                'length': 8,
                'name': '예상체결가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'yevolume',
                'length': 12,
                'name': '예상체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'jnilysign',
                'length': 1,
                'name': '예상체결가전일종가대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jnilchange',
                'length': 8,
                'name': '예상체결가전일종가대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'jnilydrate',
                'length': 6.2,
                'name': '예상체결가전일종가등락율',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'yofferho0',
                'length': 8,
                'name': '예상매도호가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ybidho0',
                'length': 8,
                'name': '예상매수호가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'yofferrem0',
                'length': 12,
                'name': '예상매도호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ybidrem0',
                'length': 12,
                'name': '예상매수호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'shcode',
                'length': 9,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchname',
                'length': 3,
                'name': '거래소명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_shcode',
                'length': 10,
                'name': '거래소별단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'OK_': {
        'tr_cd': 'OK_',
        'title': 'KOSDAQ거래원',
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
            },
            {
                'key': 'tradmdval1',
                'length': 15,
                'name': '매도거래대금1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsval1',
                'length': 15,
                'name': '매수거래대금1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdavg1',
                'length': 7,
                'name': '매도평균단가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsavg1',
                'length': 7,
                'name': '매수평균단가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdval2',
                'length': 15,
                'name': '매도거래대금2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsval2',
                'length': 15,
                'name': '매수거래대금2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdavg2',
                'length': 7,
                'name': '매도평균단가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsavg2',
                'length': 7,
                'name': '매수평균단가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdval3',
                'length': 15,
                'name': '매도거래대금3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsval3',
                'length': 15,
                'name': '매수거래대금3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdavg3',
                'length': 7,
                'name': '매도평균단가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsavg3',
                'length': 7,
                'name': '매수평균단가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdval4',
                'length': 15,
                'name': '매도거래대금4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsval4',
                'length': 15,
                'name': '매수거래대금4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdavg4',
                'length': 7,
                'name': '매도평균단가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsavg4',
                'length': 7,
                'name': '매수평균단가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdval5',
                'length': 15,
                'name': '매도거래대금5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsval5',
                'length': 15,
                'name': '매수거래대금5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdavg5',
                'length': 7,
                'name': '매도평균단가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmsavg5',
                'length': 7,
                'name': '매수평균단가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmdval',
                'length': 15,
                'name': '외국계증권사매도거래대금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmsval',
                'length': 15,
                'name': '외국계증권사매수거래대금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmdavg',
                'length': 7,
                'name': '외국계증권사매도평균단가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmsavg',
                'length': 7,
                'name': '외국계증권사매수평균단가',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'PH_': {
        'tr_cd': 'PH_',
        'title': 'KOSPI프로그램매매종목별',
        'fields': [
            {
                'key': 'time',
                'length': 6,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'price',
                'length': 8,
                'name': '현재가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sign',
                'length': 1,
                'name': '전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': 8,
                'name': '전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volume',
                'length': 10,
                'name': '누적거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'drate',
                'length': 6.2,
                'name': '등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdhrem',
                'length': 12,
                'name': '차익매도호가 잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cshrem',
                'length': 12,
                'name': '차익매수호가 잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdhrem',
                'length': 12,
                'name': '비차익매도호가 잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bshrem',
                'length': 12,
                'name': '비차익매수호가 잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdhvolume',
                'length': 12,
                'name': '차익매도호가 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cshvolume',
                'length': 12,
                'name': '차익매수호가 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdhvolume',
                'length': 12,
                'name': '비차익매도호가 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bshvolume',
                'length': 12,
                'name': '비차익매수호가 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dwcvolume',
                'length': 12,
                'name': '전체매도위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'swcvolume',
                'length': 12,
                'name': '전체매수위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'djcvolume',
                'length': 12,
                'name': '전체매도자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sjcvolume',
                'length': 12,
                'name': '전체매수자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tdvolume',
                'length': 12,
                'name': '전체매도체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tsvolume',
                'length': 12,
                'name': '전체매수체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tvol',
                'length': 12,
                'name': '전체순매수 수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dwcvalue',
                'length': 15,
                'name': '전체매도위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'swcvalue',
                'length': 15,
                'name': '전체매수위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'djcvalue',
                'length': 15,
                'name': '전체매도자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sjcvalue',
                'length': 15,
                'name': '전체매수자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tdvalue',
                'length': 15,
                'name': '전체매도체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tsvalue',
                'length': 15,
                'name': '전체매수체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tval',
                'length': 15,
                'name': '전체순매수 금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'pdgvolume',
                'length': 12,
                'name': '매도 사전공시수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'psgvolume',
                'length': 12,
                'name': '매수 사전공시수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': 6,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'PM_': {
        'tr_cd': 'PM_',
        'title': 'KOSPI프로그램매매전체집계',
        'fields': [
            {
                'key': 'time',
                'length': 6,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdhrem',
                'length': 6,
                'name': '차익매도호가잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cshrem',
                'length': 6,
                'name': '차익매수호가잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdhrem',
                'length': 6,
                'name': '비차익매도호가잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bshrem',
                'length': 6,
                'name': '비차익매수호가잔량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdhvolume',
                'length': 6,
                'name': '차익매도호가수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cshvolume',
                'length': 6,
                'name': '차익매수호가수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdhvolume',
                'length': 6,
                'name': '비차익매도호가수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bshvolume',
                'length': 6,
                'name': '비차익매수호가수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdwvolume',
                'length': 6,
                'name': '차익매도위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdjvolume',
                'length': 6,
                'name': '차익매도자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cswvolume',
                'length': 6,
                'name': '차익매수위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'csjvolume',
                'length': 6,
                'name': '차익매수자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cwvol',
                'length': 6,
                'name': '차익위탁순매수수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cjvol',
                'length': 6,
                'name': '차익자기순매수수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdwvolume',
                'length': 6,
                'name': '비차익매도위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdjvolume',
                'length': 6,
                'name': '비차익매도자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bswvolume',
                'length': 6,
                'name': '비차익매수위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bsjvolume',
                'length': 6,
                'name': '비차익매수자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bwvol',
                'length': 6,
                'name': '비차익위탁순매수수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bjvol',
                'length': 6,
                'name': '비차익자기순매수수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dwvolume',
                'length': 6,
                'name': '전체매도위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'swvolume',
                'length': 6,
                'name': '전체매수위탁체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'wvol',
                'length': 6,
                'name': '전체위탁순매수수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'djvolume',
                'length': 6,
                'name': '전체매도자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sjvolume',
                'length': 6,
                'name': '전체매수자기체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jvol',
                'length': 6,
                'name': '전체자기순매수수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdwvalue',
                'length': 8,
                'name': '차익매도위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdjvalue',
                'length': 8,
                'name': '차익매도자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cswvalue',
                'length': 8,
                'name': '차익매수위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'csjvalue',
                'length': 8,
                'name': '차익매수자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cwval',
                'length': 8,
                'name': '차익위탁순매수금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cjval',
                'length': 8,
                'name': '차익자기순매수금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdwvalue',
                'length': 8,
                'name': '비차익매도위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdjvalue',
                'length': 8,
                'name': '비차익매도자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bswvalue',
                'length': 8,
                'name': '비차익매수위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bsjvalue',
                'length': 8,
                'name': '비차익매수자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bwval',
                'length': 8,
                'name': '비차익위탁순매수금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bjval',
                'length': 8,
                'name': '비차익자기순매수금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dwvalue',
                'length': 8,
                'name': '전체매도위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'swvalue',
                'length': 8,
                'name': '전체매수위탁체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'wval',
                'length': 8,
                'name': '전체위탁순매수금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'djvalue',
                'length': 8,
                'name': '전체매도자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sjvalue',
                'length': 8,
                'name': '전체매수자기체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jval',
                'length': 8,
                'name': '전체자기순매수금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'k200jisu',
                'length': 6.2,
                'name': 'KOSPI200지수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'k200sign',
                'length': 1,
                'name': 'KOSPI200전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': 6.2,
                'name': 'KOSPI200전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'k200basis',
                'length': 4.2,
                'name': 'KOSPI200베이시스',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdvolume',
                'length': 6,
                'name': '차익매도체결수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'csvolume',
                'length': 6,
                'name': '차익매수체결수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cvol',
                'length': 6,
                'name': '차익순매수수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdvolume',
                'length': 6,
                'name': '비차익매도체결수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bsvolume',
                'length': 6,
                'name': '비차익매수체결수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bvol',
                'length': 6,
                'name': '비차익순매수수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tdvolume',
                'length': 6,
                'name': '전체매도체결수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tsvolume',
                'length': 6,
                'name': '전체매수체결수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tvol',
                'length': 6,
                'name': '전체순매수수량합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdvalue',
                'length': 8,
                'name': '차익매도체결금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'csvalue',
                'length': 8,
                'name': '차익매수체결금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cval',
                'length': 8,
                'name': '차익순매수금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bdvalue',
                'length': 8,
                'name': '비차익매도체결금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bsvalue',
                'length': 8,
                'name': '비차익매수체결금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bval',
                'length': 8,
                'name': '비차익순매수금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tdvalue',
                'length': 8,
                'name': '전체매도체결금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tsvalue',
                'length': 8,
                'name': '전체매수체결금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tval',
                'length': 8,
                'name': '전체순매수금액합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_cdvolcha',
                'length': 6,
                'name': '차익매도체결수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_csvolcha',
                'length': 6,
                'name': '차익매수체결수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_cvolcha',
                'length': 6,
                'name': '차익순매수수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_bdvolcha',
                'length': 6,
                'name': '비차익매도체결수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_bsvolcha',
                'length': 6,
                'name': '비차익매수체결수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_bvolcha',
                'length': 6,
                'name': '비차익순매수수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_tdvolcha',
                'length': 6,
                'name': '전체매도체결수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_tsvolcha',
                'length': 6,
                'name': '전체매수체결수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_tvolcha',
                'length': 6,
                'name': '전체순매수수량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_cdvalcha',
                'length': 8,
                'name': '차익매도체결금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_csvalcha',
                'length': 8,
                'name': '차익매수체결금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_cvalcha',
                'length': 8,
                'name': '차익순매수금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_bdvalcha',
                'length': 8,
                'name': '비차익매도체결금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_bsvalcha',
                'length': 8,
                'name': '비차익매수체결금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_bvalcha',
                'length': 8,
                'name': '비차익순매수금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_tdvalcha',
                'length': 8,
                'name': '전체매도체결금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_tsvalcha',
                'length': 8,
                'name': '전체매수체결금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'p_tvalcha',
                'length': 8,
                'name': '전체순매수금액직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'gubun',
                'length': 1,
                'name': '구분값',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'S2_': {
        'tr_cd': 'S2_',
        'title': 'KOSPI우선호가',
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
    'S3_': {
        'tr_cd': 'S3_',
        'title': 'KOSPI체결',
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
                'desc': '+ : 매수<br/>- : 매도',
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
                'key': 'shcode',
                'length': '	6',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchname',
                'length': 3,
                'name': '거래소명',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'S4_': {
        'tr_cd': 'S4_',
        'title': 'KOSPI기세',
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
    'SC1': {
        'tr_cd': 'SC1',
        'title': '주식주문체결',
        'fields': [
            {
                'key': 'grpId',
                'length': 20,
                'name': ' 그룹Id',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'trchno',
                'length': 10,
                'name': '트렌치번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'trtzxLevytp',
                'length': 1,
                'name': '거래세징수구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordtrxptncode',
                'length': 4,
                'name': ' 주문처리유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'acntnm',
                'length': 40,
                'name': '계좌명',
                'required': True,
                'type': 'string'
            },
            {
                'desc': 'SONAT000:신규주문<br/>SONAT001:정정주문<br/>SONAT002:취소주문<br/>SONAS100:체결확인',
                'key': 'trcode',
                'length': 8,
                'name': 'TRCODE',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'userid',
                'length': 16,
                'name': '사용자ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'agrgbrnno',
                'length': 3,
                'name': '집계지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'regmktcode',
                'length': 2,
                'name': '등록시장코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'len',
                'length': 6,
                'name': '헤더길이',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'opdrtnno',
                'length': 12,
                'name': '운용지시번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'orgordmdfyqty',
                'length': 16,
                'name': '원주문정정수량',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드',
                'key': 'avrpchsprc',
                'length': 13,
                'name': '평균매입가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exectime',
                'length': 9,
                'name': '체결시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cont',
                'length': 1,
                'name': '연속구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mnymgnrat',
                'length': 7,
                'name': '현금증거금률',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdfycnfqty',
                'length': 16,
                'name': '정정확인수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'orgordcancqty',
                'length': 16,
                'name': '원주문취소수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'compress',
                'length': 1,
                'name': '압축구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'execprc',
                'length': 13,
                'name': '체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdfycnfprc',
                'length': 16,
                'name': '정정확인가격',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드',
                'key': 'unercsellordqty',
                'length': 16,
                'name': '미체결매도주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cmsnamtexecamt',
                'length': 16,
                'name': '수수료체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ruseableamt',
                'length': 16,
                'name': '재사용가능금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'gubun',
                'length': 1,
                'name': '헤더구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'trid',
                'length': 16,
                'name': 'TR추적ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'flctqty',
                'length': 16,
                'name': '변동수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'execno',
                'length': 10,
                'name': '체결번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lptp',
                'length': 1,
                'name': '유동성공급자구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'varmsglen',
                'length': 2,
                'name': '가변메시지길이',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordno',
                'length': 10,
                'name': '주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'futsmkttp',
                'length': 1,
                'name': '선물시장구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'crdtexecamt',
                'length': 16,
                'name': '신용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'deposit',
                'length': 16,
                'name': '예수금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'frgrunqno',
                'length': 6,
                'name': '외국인고유번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'crdayruseexecval',
                'length': 16,
                'name': '금일재사용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'trsrc',
                'length': 1,
                'name': '조회발원지',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordacntno',
                'length': 20,
                'name': '주문계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'reqcnt',
                'length': 4,
                'name': '요청레코드개수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shtnIsuno',
                'length': 9,
                'name': '단축종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'accno1',
                'length': 11,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'strtgcode',
                'length': 6,
                'name': '전략코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordseqno',
                'length': 10,
                'name': '주문회차',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'Isunm',
                'length': 40,
                'name': '종목명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordablesubstamt',
                'length': 16,
                'name': '주문가능대용',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'encrypt',
                'length': 1,
                'name': '암호구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'Isuno',
                'length': 12,
                'name': '종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'accno2',
                'length': 9,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'contkey',
                'length': 18,
                'name': '연속키값',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'Loandt',
                'length': 8,
                'name': '대출일',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'seq',
                'length': 9,
                'name': '전문일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lineseq',
                'length': 10,
                'name': '라인일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'varlen',
                'length': 2,
                'name': '가변시스템길이',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'orduserId',
                'length': 16,
                'name': '주문자Id',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mgmtbrnno',
                'length': 3,
                'name': '관리지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'rjtqty',
                'length': 16,
                'name': '거부수량',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '00:지정가<br/>03:시장가<br/>05:조건부지정가<br/>06:최유리지정가<br/>07:최우선지정가<br/>09:자사주<br/>10:매입인도(일반)<br/>13:시장가 (IOC)<br/>16:최유리지정가 (IOC)<br/>18:사용안함<br/>20:지정가(임의)<br/>23:시장가(임의)<br/>26:최유리지정가 (FOK)<br/>41:부분충족(프리보드)<br/>42:전량충족(프리보드)<br/>51:장중대량<br/>52:장중바스켓<br/>61:장개시전시간외<br/>62:사용안함<br/>63:경매매<br/>66:장전시간외경쟁대량<br/>67:장개시전시간외대량<br/>68:장개시전시간외바스켓<br/>69:장개시전시간외자사주<br/>71:신고대량전장시가<br/>72:사용안함<br/>73:신고대량종가<br/>76:장중경쟁대량<br/>77:장중대량<br/>78:장중바스켓<br/>79:사용안함<br/>80:매입인도(당일)<br/>81:시간외종가<br/>82:시간외단일가<br/>87:시간외대량<br/>88:바스켓주문<br/>89:시간외자사주<br/>91:자사주스톡옵션<br/>A1:stop order',
                'key': 'ordprcptncode',
                'length': 2,
                'name': '호가유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'stdIsuno',
                'length': 12,
                'name': '표준종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드',
                'key': 'pchsant',
                'length': 16,
                'name': '매입금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'filler',
                'length': 6,
                'name': '예비영역',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드',
                'key': 'secbalqty',
                'length': 16,
                'name': '잔고수량',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '01:주문<br/>02:정정<br/>03:취소<br/>11:체결<br/>12 정정확인<br/>13 취소확인<br/>14 거부',
                'key': 'ordxctptncode',
                'length': 2,
                'name': '주문체결유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'canccnfqty',
                'length': 16,
                'name': '취소확인수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordablemny',
                'length': 16,
                'name': '주문가능현금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'pubip',
                'length': 12,
                'name': '공인IP',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'prvip',
                'length': 12,
                'name': '사설IP',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'funckey',
                'length': 4,
                'name': '기능키',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'accno',
                'length': 11,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'compreq',
                'length': 1,
                'name': '압축요청구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'crdtpldgruseamt',
                'length': 16,
                'name': '신용담보재사용금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordamt',
                'length': 16,
                'name': '주문금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'termno',
                'length': 8,
                'name': '단말번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'crdtpldgexecamt',
                'length': 16,
                'name': '신용담보체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordcndi',
                'length': 1,
                'name': '주문조건',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드',
                'key': 'rmndLoanamt',
                'length': 16,
                'name': '잔여대출금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bpno',
                'length': 3,
                'name': '지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'substamt',
                'length': 16,
                'name': '대용금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mgempno',
                'length': 9,
                'name': '관리사원번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'csgnsubstmgn',
                'length': 16,
                'name': '위탁증거금대용',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offset',
                'length': 3,
                'name': '공통시작지점',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'rcptexectime',
                'length': 9,
                'name': '거래소수신체결시각',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드',
                'key': 'sellableqty',
                'length': 16,
                'name': '매도주문가능수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'spotexecqty',
                'length': 16,
                'name': '실물체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'varhdlen',
                'length': 2,
                'name': '가변해더길이',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'substmgnrat',
                'length': 9,
                'name': '대용증거금률',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordavrexecprc',
                'length': 13,
                'name': '주문평균체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'itemno',
                'length': 10,
                'name': '아이템번호',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '[신규]<br/>000 : 보통<br/>001 : 유통융자신규<br/>003 : 자기융자신규<br/>005 : 유통대주신규<br/>007 : 자기대주신규<br/>080 : 예탁주식담보융자신규<br/>082 : 예탁채권담보융자신규<br/>[상환]<br/>101 : 유통융자상환<br/>103 : 자기융자상환<br/>105 : 유통대주상환<br/>107 : 자기대주상환<br/>111 : 유통융자전액상환<br/>113 : 자기융자전액상환<br/>180 : 예탁주식담보융자상환<br/>182 : 예탁채권담보융자상환<br/>188 : 담보대출전액상환',
                'key': 'mgntrncode',
                'length': 3,
                'name': '신용거래코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'nsavtrdqty',
                'length': 16,
                'name': '비저축체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ifinfo',
                'length': 4,
                'name': 'I/F정보',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드',
                'key': 'ordableruseqty',
                'length': 16,
                'name': '재사용가능수량(매도)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ptflno',
                'length': 10,
                'name': '포트폴리오번호',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드',
                'key': 'secbalqtyd2',
                'length': 16,
                'name': '잔고수량(d2)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'brwmgmtYn',
                'length': 1,
                'name': '차입관리여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'eventid',
                'length': 4,
                'name': 'I/F이벤트ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'csgnmnymgn',
                'length': 16,
                'name': '위탁증거금현금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'pcbpno',
                'length': 3,
                'name': '처리지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'orgordno',
                'length': 10,
                'name': '원주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ifid',
                'length': 3,
                'name': 'I/F일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'media',
                'length': 2,
                'name': '접속매체',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mtiordseqno',
                'length': 10,
                'name': '복수주문일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'filler1',
                'length': 41,
                'name': '예비영역',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'orgordunercqty',
                'length': 16,
                'name': '원주문미체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mbrnmbrno',
                'length': 3,
                'name': '회원/비회원사번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'futsLnkbrnno',
                'length': 3,
                'name': '선물연계지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'commdacode',
                'length': 2,
                'name': '통신매체코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'stslexecqty',
                'length': 16,
                'name': '공매도체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'proctm',
                'length': 9,
                'name': 'AP처리시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bfstdIsuno',
                'length': 12,
                'name': '전표준종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'futsLnkacntno',
                'length': 20,
                'name': '선물연계계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lang',
                'length': 1,
                'name': '언어구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'unercqty',
                'length': 16,
                'name': '미체결수량(주문)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'execqty',
                'length': 16,
                'name': '체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'adduptp',
                'length': 2,
                'name': '수수료합산코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bskno',
                'length': 10,
                'name': '바스켓번호',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드',
                'key': 'spotordableqty',
                'length': 16,
                'name': '실물가능수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ubstexecamt',
                'length': 16,
                'name': '대용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '0:일반<br/>1:자동반대매매<br/>2:지점반대매매<br/>3:예비주문에대한 본주문',
                'key': 'cvrgordtp',
                'length': 1,
                'name': '반대매매주문구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordqty',
                'length': 16,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mnyexecamt',
                'length': 16,
                'name': '현금체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'outgu',
                'length': 1,
                'name': '메세지출력구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msgcode',
                'length': 4,
                'name': '메세지코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '00: 위탁<br/>01: 신용<br/>04: 선물대용',
                'key': 'ordtrdptncode',
                'length': 2,
                'name': '주문거래유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordmktcode',
                'length': 2,
                'name': '주문시장코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '00 해당없음<br/>01:현금매도<br/>02:현금매수<br/>03신용매도<br/>04:신용매수',
                'key': 'ordptncode',
                'length': 2,
                'name': '주문유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'prdayruseexecval',
                'length': 16,
                'name': '전일재사용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'comid',
                'length': 3,
                'name': 'COM ID',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '1:매도<br/>2:매수',
                'key': 'bnstp',
                'length': 1,
                'name': '매매구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'user',
                'length': 8,
                'name': '조작자ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordprc',
                'length': 13,
                'name': '주문가격',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'SC2': {
        'tr_cd': 'SC2',
        'title': '주식주문정정',
        'fields': []
    },
    'SC4': {
        'tr_cd': 'SC4',
        'title': '주식주문거부',
        'fields': []
    },
    'SHC': {
        'tr_cd': 'SHC',
        'title': '상/하한가근접진입',
        'fields': [
            {
                'key': 'sijanggubun',
                'length': '	1',
                'name': '거래소/코스닥구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'hname',
                'length': '	20',
                'name': '종목명',
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
                'key': 'volume',
                'length': '	12',
                'name': '누적거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volincrate',
                'length': '	12.2',
                'name': '거래증가율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'updnlmtprice',
                'length': '	8',
                'name': '상/하한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'updnlmtdrate',
                'length': '	6.2',
                'name': '상/하한가대비율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jnilvolume',
                'length': '	12',
                'name': '전일거래량',
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
                'key': 'gwangubun',
                'length': '	1',
                'name': '관리구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'undergubun',
                'length': '	1',
                'name': '이상급등구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tgubun',
                'length': '	1',
                'name': '투자유의구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'wgubun',
                'length': '	1',
                'name': '우선주구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dishonest',
                'length': '	1',
                'name': '불성실구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jkrate',
                'length': '	1',
                'name': '증거금률',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'updnlmtdaycnt',
                'length': 3,
                'name': '상한가/하한가연속일수',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'SHD': {
        'tr_cd': 'SHD',
        'title': '상/하한가근접이탈',
        'fields': [
            {
                'key': 'sijanggubun',
                'length': '	1',
                'name': '거래소/코스닥구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'hname',
                'length': '	20',
                'name': '종목명',
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
                'key': 'volume',
                'length': '	12',
                'name': '누적거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volincrate',
                'length': '	12.2',
                'name': '거래증가율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'updnlmtprice',
                'length': '	8',
                'name': '상/하한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'updnlmtdrate',
                'length': '	6.2',
                'name': '상/하한가대비율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jnilvolume',
                'length': '	12',
                'name': '전일거래량',
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
                'key': 'gwangubun',
                'length': '	1',
                'name': '관리구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'undergubun',
                'length': '	1',
                'name': '이상급등구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tgubun',
                'length': '	1',
                'name': '투자유의구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'wgubun',
                'length': '	1',
                'name': '우선주구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dishonest',
                'length': '	1',
                'name': '불성실구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jkrate',
                'length': '	1',
                'name': '증거금률',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'SHI': {
        'tr_cd': 'SHI',
        'title': '상/하한가진입',
        'fields': [
            {
                'key': 'sijanggubun',
                'length': '	1',
                'name': '거래소/코스닥구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'hname',
                'length': '	20',
                'name': '종목명',
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
                'key': 'volume',
                'length': '	12',
                'name': '누적거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volincrate',
                'length': '	12.2',
                'name': '거래증가율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totofferrem',
                'length': '	12',
                'name': '매도호가총수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidrem',
                'length': '	12',
                'name': '매수호가총수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'updnlmtstime',
                'length': '	6',
                'name': '상한가/하한가최종진입시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'updnlmtdaycnt',
                'length': '	3',
                'name': '상한가/하한가연속일수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jnilvolume',
                'length': '	12',
                'name': '전일거래량',
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
                'key': 'gwangubun',
                'length': '	1',
                'name': '관리구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'undergubun',
                'length': '	1',
                'name': '이상급등구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tgubun',
                'length': '	1',
                'name': '투자유의구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'wgubun',
                'length': '	1',
                'name': '우선주구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dishonest',
                'length': '	1',
                'name': '불성실구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jkrate',
                'length': '	1',
                'name': '증거금률',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'SHO': {
        'tr_cd': 'SHO',
        'title': '상/하한가이탈',
        'fields': [
            {
                'key': 'sijanggubun',
                'length': '	1',
                'name': '거래소/코스닥구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'hname',
                'length': '	20',
                'name': '종목명',
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
                'key': 'volume',
                'length': '	12',
                'name': '누적거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volincrate',
                'length': '	12.2',
                'name': '거래증가율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'updnlmtprice',
                'length': '	8',
                'name': '상/하한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'updnlmtchange',
                'length': '	8',
                'name': '상/하한가대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'updnlmtdrate',
                'length': '	6.2',
                'name': '상/하한가대비율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jnilvolume',
                'length': '	12',
                'name': '전일거래량',
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
                'key': 'gwangubun',
                'length': '	1',
                'name': '관리구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'undergubun',
                'length': '	1',
                'name': '이상급등구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tgubun',
                'length': '	1',
                'name': '투자유의구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'wgubun',
                'length': '	1',
                'name': '우선주구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dishonest',
                'length': '	1',
                'name': '불성실구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jkrate',
                'length': '	1',
                'name': '증거금률',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'UBM': {
        'tr_cd': 'UBM',
        'title': '(통합) 업종별투자자별매매현황',
        'fields': [
            {
                'key': 'tjjcode',
                'length': 4,
                'name': '투자자코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjtime',
                'length': 8,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume',
                'length': 8,
                'name': '매수거래량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume',
                'length': 8,
                'name': '매도거래량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol',
                'length': 8,
                'name': '거래량순매수',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_msvol',
                'length': 8,
                'name': '거래량순매수직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue',
                'length': 6,
                'name': '매수거래대금',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue',
                'length': 6,
                'name': '매도거래대금',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval',
                'length': 6,
                'name': '거래대금순매수',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_msval',
                'length': 6,
                'name': '거래대금순매수직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'upcode',
                'length': 3,
                'name': '업종코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_upcode',
                'length': 4,
                'name': '거래소별업종코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'UBT': {
        'tr_cd': 'UBT',
        'title': '(통합)시간대별투자자매매추이',
        'fields': [
            {
                'key': 'tjjtime',
                'length': 8,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode1',
                'length': 4,
                'name': '투자자코드1(개인)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume1',
                'length': 8,
                'name': '매수거래량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume1',
                'length': 8,
                'name': '매도거래량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol1',
                'length': 8,
                'name': '거래량순매수1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue1',
                'length': 6,
                'name': '매수거래대금1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue1',
                'length': 6,
                'name': '매도거래대금1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval1',
                'length': 6,
                'name': '거래대금순매수1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode2',
                'length': 4,
                'name': '투자자코드2(외국인)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume2',
                'length': 8,
                'name': '매수거래량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume2',
                'length': 8,
                'name': '매도거래량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol2',
                'length': 8,
                'name': '거래량순매수2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue2',
                'length': 6,
                'name': '매수거래대금2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue2',
                'length': 6,
                'name': '매도거래대금2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval2',
                'length': 6,
                'name': '거래대금순매수2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode3',
                'length': 4,
                'name': '투자자코드3(기관계)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume3',
                'length': 8,
                'name': '매수거래량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume3',
                'length': 8,
                'name': '매도거래량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol3',
                'length': 8,
                'name': '거래량순매수3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue3',
                'length': 6,
                'name': '매수거래대금3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue3',
                'length': 6,
                'name': '매도거래대금3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval3',
                'length': None,
                'name': '거래대금순매수3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode4',
                'length': 4,
                'name': '투자자코드4(증권)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume4',
                'length': 8,
                'name': '매수거래량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume4',
                'length': 8,
                'name': '매도거래량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol4',
                'length': 8,
                'name': '거래량순매수4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue4',
                'length': 6,
                'name': '매수거래대금4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue4',
                'length': 6,
                'name': '매도거래대금4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval4',
                'length': 6,
                'name': '거래대금순매수4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode5',
                'length': 4,
                'name': '투자자코드5(투신)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume5',
                'length': 8,
                'name': '매수거래량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume5',
                'length': 8,
                'name': '매도거래량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol5',
                'length': 8,
                'name': '거래량순매수5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue5',
                'length': 6,
                'name': '매수거래대금5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue5',
                'length': 6,
                'name': '매도거래대금5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval5',
                'length': 6,
                'name': '거래대금순매수5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode6',
                'length': 4,
                'name': '투자자코드6(은행)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume6',
                'length': 8,
                'name': '매수거래량6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume6',
                'length': 8,
                'name': '매도거래량6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol6',
                'length': 8,
                'name': '거래량순매수6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue6',
                'length': 6,
                'name': '매수거래대금6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue6',
                'length': 6,
                'name': '매도거래대금6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval6',
                'length': 6,
                'name': '거래대금순매수6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode7',
                'length': 4,
                'name': '투자자코드7(보험)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume7',
                'length': 8,
                'name': '매수거래량7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume7',
                'length': 8,
                'name': '매도거래량7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol7',
                'length': 8,
                'name': '거래량순매수7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue7',
                'length': 6,
                'name': '매수거래대금7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue7',
                'length': 6,
                'name': '매도거래대금7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval7',
                'length': 6,
                'name': '거래대금순매수7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode8',
                'length': 4,
                'name': '투자자코드8(종금)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume8',
                'length': 8,
                'name': '매수거래량8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume8',
                'length': 8,
                'name': '매도거래량8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol8',
                'length': 8,
                'name': '거래량순매수8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue8',
                'length': 6,
                'name': '매수거래대금8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue8',
                'length': 6,
                'name': '매도거래대금8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval8',
                'length': 6,
                'name': '거래대금순매수8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode9',
                'length': 4,
                'name': '투자자코드9(기금)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume9',
                'length': 8,
                'name': '매수거래량9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume9',
                'length': 8,
                'name': '매도거래량9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol9',
                'length': 8,
                'name': '거래량순매수9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue9',
                'length': 6,
                'name': '매수거래대금9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue9',
                'length': 6,
                'name': '매도거래대금9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval9',
                'length': 6,
                'name': '거래대금순매수9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode10',
                'length': 4,
                'name': '투자자코드10(선물업자)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume10',
                'length': 8,
                'name': '매수거래량10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume10',
                'length': 8,
                'name': '매도거래량10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol10',
                'length': 8,
                'name': '거래량순매수10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue10',
                'length': 6,
                'name': '매수거래대금10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue10',
                'length': 6,
                'name': '매도거래대금10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval10',
                'length': 6,
                'name': '거래대금순매수10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tjjcode11',
                'length': 4,
                'name': '투자자코드11(기타)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume11',
                'length': 8,
                'name': '매수거래량11',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume11',
                'length': 8,
                'name': '매도거래량11',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol11',
                'length': 8,
                'name': '거래량순매수11',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue11',
                'length': 6,
                'name': '매수거래대금11',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue11',
                'length': 6,
                'name': '매도거래대금11',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval11',
                'length': 6,
                'name': '거래대금순매수11',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'upcode',
                'length': 3,
                'name': '업종코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tjjcode0',
                'length': 4,
                'name': '투자자코드0(사모펀드)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume0',
                'length': 8,
                'name': '매수거래량0',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume0',
                'length': 8,
                'name': '매도거래량0',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvol0',
                'length': 8,
                'name': '거래량순매수0',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvalue0',
                'length': 6,
                'name': '매수거래대금0',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvalue0',
                'length': 6,
                'name': '매도거래대금0',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msval0',
                'length': 6,
                'name': '거래대금순매수0',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ex_upcode',
                'length': 4,
                'name': '거래소별업종코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'UH1': {
        'tr_cd': 'UH1',
        'title': '(통합)호가잔량',
        'fields': [
            {
                'key': 'hotime',
                'length': 6,
                'name': '호가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho1',
                'length': 7,
                'name': '매도호가1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho1',
                'length': 7,
                'name': '매수호가1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_offerrem1',
                'length': 9,
                'name': 'KRX매도호가잔량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_offerrem1',
                'length': 9,
                'name': 'NXT매도호가잔량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_offerrem1',
                'length': 9,
                'name': '통합매도호가잔량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_bidrem1',
                'length': 9,
                'name': 'KRX매수호가잔량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_bidrem1',
                'length': 9,
                'name': 'NXT매수호가잔량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_bidrem1',
                'length': 9,
                'name': '통합매수호가잔량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho2',
                'length': 7,
                'name': '매도호가2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho2',
                'length': 7,
                'name': '매수호가2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_offerrem2',
                'length': 9,
                'name': 'KRX매도호가잔량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_offerrem2',
                'length': 9,
                'name': 'NXT매도호가잔량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_offerrem2',
                'length': 9,
                'name': '통합매도호가잔량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_bidrem2',
                'length': 9,
                'name': 'KRX매수호가잔량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_bidrem2',
                'length': 9,
                'name': 'NXT매수호가잔량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_bidrem2',
                'length': 9,
                'name': '통합매수호가잔량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho3',
                'length': 7,
                'name': '매도호가3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho3',
                'length': 7,
                'name': '매수호가3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_offerrem3',
                'length': 9,
                'name': 'KRX매도호가잔량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_offerrem3',
                'length': 9,
                'name': 'NXT매도호가잔량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_offerrem3',
                'length': 9,
                'name': '통합매도호가잔량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_bidrem3',
                'length': 9,
                'name': 'KRX매수호가잔량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_bidrem3',
                'length': 9,
                'name': 'NXT매수호가잔량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_bidrem3',
                'length': 9,
                'name': '통합매수호가잔량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho4',
                'length': 7,
                'name': '매도호가4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho4',
                'length': 7,
                'name': '매수호가4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_offerrem4',
                'length': 9,
                'name': 'KRX매도호가잔량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_offerrem4',
                'length': 9,
                'name': 'NXT매도호가잔량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_offerrem4',
                'length': 9,
                'name': '통합매도호가잔량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_bidrem4',
                'length': 9,
                'name': 'KRX매수호가잔량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_bidrem4',
                'length': 9,
                'name': 'NXT매수호가잔량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_bidrem4',
                'length': 9,
                'name': '통합매수호가잔량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho5',
                'length': 7,
                'name': '매도호가5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho5',
                'length': 7,
                'name': '매수호가5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_offerrem5',
                'length': 9,
                'name': 'KRX매도호가잔량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_offerrem5',
                'length': 9,
                'name': 'NXT매도호가잔량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_offerrem5',
                'length': 9,
                'name': '통합매도호가잔량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_bidrem5',
                'length': 9,
                'name': 'KRX매수호가잔량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_bidrem5',
                'length': 9,
                'name': 'NXT매수호가잔량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_bidrem5',
                'length': 9,
                'name': '통합매수호가잔량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho6',
                'length': 7,
                'name': '매도호가6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho6',
                'length': 7,
                'name': '매수호가6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_offerrem6',
                'length': 9,
                'name': 'KRX매도호가잔량6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_offerrem6',
                'length': 9,
                'name': 'NXT매도호가잔량6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_offerrem6',
                'length': 9,
                'name': '통합매도호가잔량6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_bidrem6',
                'length': 9,
                'name': 'KRX매수호가잔량6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_bidrem6',
                'length': 9,
                'name': 'NXT매수호가잔량6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_bidrem6',
                'length': 9,
                'name': '통합매수호가잔량6',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho7',
                'length': 7,
                'name': '매도호가7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho7',
                'length': 7,
                'name': '매수호가7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_offerrem7',
                'length': 9,
                'name': 'KRX매도호가잔량7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_offerrem7',
                'length': 9,
                'name': 'NXT매도호가잔량7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_offerrem7',
                'length': 9,
                'name': '통합매도호가잔량7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_bidrem7',
                'length': 9,
                'name': 'KRX매수호가잔량7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_bidrem7',
                'length': 9,
                'name': 'NXT매수호가잔량7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_bidrem7',
                'length': 9,
                'name': '통합매수호가잔량7',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho8',
                'length': 7,
                'name': '매도호가8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho8',
                'length': 7,
                'name': '매수호가8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_offerrem8',
                'length': 9,
                'name': 'KRX매도호가잔량8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_offerrem8',
                'length': 9,
                'name': 'NXT매도호가잔량8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_offerrem8',
                'length': 9,
                'name': '통합매도호가잔량8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_bidrem8',
                'length': 9,
                'name': 'KRX매수호가잔량8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_bidrem8',
                'length': 9,
                'name': 'NXT매수호가잔량8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_bidrem8',
                'length': 9,
                'name': '통합매수호가잔량8',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho9',
                'length': 7,
                'name': '매도호가9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho9',
                'length': 7,
                'name': '매수호가9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_offerrem9',
                'length': 9,
                'name': 'KRX매도호가잔량9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_offerrem9',
                'length': 9,
                'name': 'NXT매도호가잔량9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_offerrem9',
                'length': 9,
                'name': '통합매도호가잔량9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_bidrem9',
                'length': 9,
                'name': 'KRX매수호가잔량9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_bidrem9',
                'length': 9,
                'name': 'NXT매수호가잔량9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_bidrem9',
                'length': 9,
                'name': '통합매수호가잔량9',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho10',
                'length': 7,
                'name': '매도호가10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho10',
                'length': 7,
                'name': '매수호가10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_offerrem10',
                'length': 9,
                'name': 'KRX매도호가잔량10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_offerrem10',
                'length': 9,
                'name': 'NXT매도호가잔량10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_offerrem10',
                'length': 9,
                'name': '통합매도호가잔량10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_bidrem10',
                'length': 9,
                'name': 'KRX매수호가잔량10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_bidrem10',
                'length': 9,
                'name': 'NXT매수호가잔량10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_bidrem10',
                'length': 9,
                'name': '통합매수호가잔량10',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_totofferrem',
                'length': 9,
                'name': 'KRX총매도호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_totofferrem',
                'length': 9,
                'name': 'NXT총매도호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_totofferrem',
                'length': 9,
                'name': '통합총매도호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_totbidrem',
                'length': 9,
                'name': 'KRX총매수호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_totbidrem',
                'length': 9,
                'name': 'NXT총매수호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unt_totbidrem',
                'length': 9,
                'name': '통합총매수호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_donsigubun',
                'length': 1,
                'name': 'KRX동시호가구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'nxt_donsigubun',
                'length': 1,
                'name': 'NXT동시호가구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': 9,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'alloc_gubun',
                'length': 1,
                'name': '배분적용구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volume',
                'length': 12,
                'name': '누적거래량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_midprice',
                'length': 8,
                'name': 'KRX중간가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_offermidsumrem',
                'length': 9,
                'name': 'KRX매도중간가잔량합계수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_bidmidsumrem',
                'length': 9,
                'name': 'KRX매수중간가잔량합계수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_midprice',
                'length': 8,
                'name': 'NXT중간가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_offermidsumrem',
                'length': 9,
                'name': 'NXT매도중간가잔량합계수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_bidmidsumrem',
                'length': 9,
                'name': 'NXT매수중간가잔량합계수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_midsumrem',
                'length': 9,
                'name': 'KRX중간가잔량합계수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_midsumremgubun',
                'length': 1,
                'name': 'KRX중간가잔량구분(\'\'없음\'1\'매도\'2\'매수)',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_midsumrem',
                'length': 9,
                'name': 'NXT중간가잔량합계수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_midsumremgubun',
                'length': 1,
                'name': 'NXT중간가잔량구분(\'\'없음\'1\'매도\'2\'매수)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_shcode',
                'length': 10,
                'name': '거래소별단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'UK1': {
        'tr_cd': 'UK1',
        'title': '(통합)거래원',
        'fields': [
            {
                'key': 'offerno1',
                'length': 3,
                'name': '매도증권사코드1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno1',
                'length': 3,
                'name': '매수증권사코드1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad1',
                'length': 6,
                'name': '매도회원사명1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad1',
                'length': 6,
                'name': '매수회원사명1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol1',
                'length': 10,
                'name': '매도거래량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsvol1',
                'length': 10,
                'name': '매수거래량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdrate1',
                'length': 6.2,
                'name': '매도거래량비중1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsrate1',
                'length': 6.2,
                'name': '매수거래량비중1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdcha1',
                'length': 10,
                'name': '매도거래량직전대비1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmscha1',
                'length': 10,
                'name': '매수거래량직전대비1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerno2',
                'length': 3,
                'name': '매도증권사코드2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno2',
                'length': 3,
                'name': '매수증권사코드2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad2',
                'length': 6,
                'name': '매도회원사명2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad2',
                'length': 6,
                'name': '매수회원사명2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol2',
                'length': 10,
                'name': '매도거래량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsvol2',
                'length': 10,
                'name': '매수거래량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdrate2',
                'length': 6.2,
                'name': '매도거래량비중2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsrate2',
                'length': 6.2,
                'name': '매수거래량비중2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdcha2',
                'length': 10,
                'name': '매도거래량직전대비2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmscha2',
                'length': 10,
                'name': '매수거래량직전대비2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerno3',
                'length': 3,
                'name': '매도증권사코드3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno3',
                'length': 3,
                'name': '매수증권사코드3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad3',
                'length': 6,
                'name': '매도회원사명3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad3',
                'length': 6,
                'name': '매수회원사명3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol3',
                'length': 10,
                'name': '매도거래량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsvol3',
                'length': 10,
                'name': '매수거래량3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdrate3',
                'length': 6.2,
                'name': '매도거래량비중3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsrate3',
                'length': 6.2,
                'name': '매수거래량비중3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdcha3',
                'length': 10,
                'name': '매도거래량직전대비3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmscha3',
                'length': 10,
                'name': '매수거래량직전대비3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerno4',
                'length': 3,
                'name': '매도증권사코드4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno4',
                'length': 3,
                'name': '매수증권사코드4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad4',
                'length': 6,
                'name': '매도회원사명4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad4',
                'length': 6,
                'name': '매수회원사명4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol4',
                'length': 10,
                'name': '매도거래량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsvol4',
                'length': 10,
                'name': '매수거래량4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdrate4',
                'length': 6.2,
                'name': '매도거래량비중4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsrate4',
                'length': 6.2,
                'name': '매수거래량비중4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdcha4',
                'length': 10,
                'name': '매도거래량직전대비4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmscha4',
                'length': 10,
                'name': '매수거래량직전대비4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerno5',
                'length': 3,
                'name': '매도증권사코드5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno5',
                'length': 3,
                'name': '매수증권사코드5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offertrad5',
                'length': 6,
                'name': '매도회원사명5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidtrad5',
                'length': 6,
                'name': '매수회원사명5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdvol5',
                'length': 10,
                'name': '매도거래량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsvol5',
                'length': 10,
                'name': '매수거래량5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdrate5',
                'length': 6.2,
                'name': '매도거래량비중5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsrate5',
                'length': 6.2,
                'name': '매수거래량비중5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdcha5',
                'length': 10,
                'name': '매도거래량직전대비5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmscha5',
                'length': 10,
                'name': '매수거래량직전대비5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmdvol',
                'length': 10,
                'name': '외국계증권사매도합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmsvol',
                'length': 10,
                'name': '외국계증권사매수합계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmdrate',
                'length': 6.2,
                'name': '외국계증권사매도거래량비중',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmsrate',
                'length': 6.2,
                'name': '외국계증권사매수거래량비중',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmdcha',
                'length': 10,
                'name': '외국계증권사매도거래량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ftradmscha',
                'length': 10,
                'name': '외국계증권사매수거래량직전대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': 9,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradmdval1',
                'length': 15,
                'name': '매도거래대금1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsval1',
                'length': 15,
                'name': '매수거래대금1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdavg1',
                'length': 7,
                'name': '매도평균단가1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsavg1',
                'length': 7,
                'name': '매수평균단가1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdval2',
                'length': 15,
                'name': '매도거래대금2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsval2',
                'length': 15,
                'name': '매수거래대금2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdavg2',
                'length': 7,
                'name': '매도평균단가2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsavg2',
                'length': 7,
                'name': '매수평균단가2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdval3',
                'length': 15,
                'name': '매도거래대금3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsval3',
                'length': 15,
                'name': '매수거래대금3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdavg3',
                'length': 7,
                'name': '매도평균단가3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsavg3',
                'length': 7,
                'name': '매수평균단가3',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdval4',
                'length': 15,
                'name': '매도거래대금4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsval4',
                'length': 15,
                'name': '매수거래대금4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdavg4',
                'length': 7,
                'name': '매도평균단가4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsavg4',
                'length': 7,
                'name': '매수평균단가4',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdval5',
                'length': 15,
                'name': '매도거래대금5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsval5',
                'length': 15,
                'name': '매수거래대금5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmdavg5',
                'length': 7,
                'name': '매도평균단가5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tradmsavg5',
                'length': 7,
                'name': '매수평균단가5',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmdval',
                'length': 15,
                'name': '외국계증권사매도거래대금',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmsval',
                'length': 15,
                'name': '외국계증권사매수거래대금',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmdavg',
                'length': 7,
                'name': '외국계증권사매도평균단가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftradmsavg',
                'length': 7,
                'name': '외국계증권사매수평균단가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'time',
                'length': 6,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchname',
                'length': 3,
                'name': '거래소명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_shcode',
                'length': 10,
                'name': '거래소별단축코드',
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
                'key': 'time',
                'length': 6,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'price',
                'length': 8,
                'name': '현재가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'sign',
                'length': 1,
                'name': '전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': 8,
                'name': '전일대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'volume',
                'length': 10,
                'name': '누적거래량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'drate',
                'length': 6.2,
                'name': '등락율',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdhrem',
                'length': 12,
                'name': '차익매도호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cshrem',
                'length': 12,
                'name': '차익매수호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdhrem',
                'length': 12,
                'name': '비차익매도호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bshrem',
                'length': 12,
                'name': '비차익매수호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdhvolume',
                'length': 12,
                'name': '차익매도호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cshvolume',
                'length': 12,
                'name': '차익매수호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdhvolume',
                'length': 12,
                'name': '비차익매도호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bshvolume',
                'length': 12,
                'name': '비차익매수호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'dwcvolume',
                'length': 12,
                'name': '전체매도위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'swcvolume',
                'length': 12,
                'name': '전체매수위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'djcvolume',
                'length': 12,
                'name': '전체매도자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'sjcvolume',
                'length': 12,
                'name': '전체매수자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tdvolume',
                'length': 12,
                'name': '전체매도체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tsvolume',
                'length': 12,
                'name': '전체매수체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tvol',
                'length': 12,
                'name': '전체순매수수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'dwcvalue',
                'length': 15,
                'name': '전체매도위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'swcvalue',
                'length': 15,
                'name': '전체매수위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'djcvalue',
                'length': 15,
                'name': '전체매도자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'sjcvalue',
                'length': 15,
                'name': '전체매수자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tdvalue',
                'length': 15,
                'name': '전체매도체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tsvalue',
                'length': 15,
                'name': '전체매수체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tval',
                'length': 15,
                'name': '전체순매수금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'pdgvolume',
                'length': 12,
                'name': '매도사전공시수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'psgvolume',
                'length': 12,
                'name': '매수사전공시수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'shcode',
                'length': 9,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_shcode',
                'length': 10,
                'name': '거래소별단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'UPM': {
        'tr_cd': 'UPM',
        'title': '(통합)프로그램매매전체집계',
        'fields': [
            {
                'key': 'time',
                'length': 6,
                'name': '수신시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cdhrem',
                'length': 6,
                'name': '차익매도호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cshrem',
                'length': 6,
                'name': '차익매수호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdhrem',
                'length': 6,
                'name': '비차익매도호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bshrem',
                'length': 6,
                'name': '비차익매수호가잔량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdhvolume',
                'length': 6,
                'name': '차익매도호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cshvolume',
                'length': 6,
                'name': '차익매수호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdhvolume',
                'length': 6,
                'name': '비차익매도호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bshvolume',
                'length': 6,
                'name': '비차익매수호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdwvolume',
                'length': 6,
                'name': '차익매도위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdjvolume',
                'length': 6,
                'name': '차익매도자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cswvolume',
                'length': 6,
                'name': '차익매수위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'csjvolume',
                'length': 6,
                'name': '차익매수자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cwvol',
                'length': 6,
                'name': '차익위탁순매수수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cjvol',
                'length': 6,
                'name': '차익자기순매수수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdwvolume',
                'length': 6,
                'name': '비차익매도위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdjvolume',
                'length': 6,
                'name': '비차익매도자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bswvolume',
                'length': 6,
                'name': '비차익매수위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bsjvolume',
                'length': 6,
                'name': '비차익매수자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bwvol',
                'length': 6,
                'name': '비차익위탁순매수수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bjvol',
                'length': 6,
                'name': '비차익자기순매수수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'dwvolume',
                'length': 6,
                'name': '전체매도위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'swvolume',
                'length': 6,
                'name': '전체매수위탁체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': '전체매도자기체결수량',
                'length': 6,
                'name': '전체위탁순매수수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'sjvolume',
                'length': 6,
                'name': '전체매수자기체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'jvol',
                'length': 6,
                'name': '전체자기순매수수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdwvalue',
                'length': 8,
                'name': '차익매도위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdjvalue',
                'length': 8,
                'name': '차익매도자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cswvalue',
                'length': 8,
                'name': '차익매수위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'csjvalue',
                'length': 8,
                'name': '차익매수자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cwval',
                'length': 8,
                'name': '차익위탁순매수금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cjval',
                'length': 8,
                'name': '차익자기순매수금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdwvalue',
                'length': 8,
                'name': '비차익매도위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdjvalue',
                'length': 8,
                'name': '비차익매도자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bswvalue',
                'length': 8,
                'name': '비차익매수위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bsjvalue',
                'length': 8,
                'name': '비차익매수자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bwval',
                'length': 8,
                'name': '비차익위탁순매수금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bjval',
                'length': 8,
                'name': '비차익자기순매수금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'dwvalue',
                'length': 8,
                'name': '전체매도위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'swvalue',
                'length': 8,
                'name': '전체매수위탁체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'wval',
                'length': 8,
                'name': '전체위탁순매수금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'djvalue',
                'length': 8,
                'name': '전체매도자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'sjvalue',
                'length': 8,
                'name': '전체매수자기체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'jval',
                'length': 8,
                'name': '전체자기순매수금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'k200jisu',
                'length': 6.2,
                'name': 'KOSPI200지수',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'k200sign',
                'length': 1,
                'name': 'KOSPI200전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': 4.2,
                'name': 'KOSPI200전일대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'k200basis',
                'length': 4.2,
                'name': 'KOSPI200베이시스',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdvolume',
                'length': 6,
                'name': '차익매도체결수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'csvolume',
                'length': 6,
                'name': '차익매수체결수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cvol',
                'length': 6,
                'name': '차익순매수수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdvolume',
                'length': 6,
                'name': '비차익매도체결수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bsvolume',
                'length': 6,
                'name': '비차익매수체결수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bvol',
                'length': 6,
                'name': '비차익순매수수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tdvolume',
                'length': 6,
                'name': '전체매도체결수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tsvolume',
                'length': 6,
                'name': '전체매수체결수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tvol',
                'length': 6,
                'name': '전체순매수수량합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cdvalue',
                'length': 8,
                'name': '차익매도체결금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'csvalue',
                'length': 8,
                'name': '차익매수체결금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cval',
                'length': 8,
                'name': '차익순매수금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bdvalue',
                'length': 8,
                'name': '비차익매도체결금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bsvalue',
                'length': 8,
                'name': '비차익매수체결금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bval',
                'length': 8,
                'name': '비차익순매수금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tdvalue',
                'length': 8,
                'name': '전체매도체결금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tsvalue',
                'length': 8,
                'name': '전체매수체결금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'tval',
                'length': 8,
                'name': '전체순매수금액합계',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_cdvolcha',
                'length': 6,
                'name': '차익매도체결수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_csvolcha',
                'length': 6,
                'name': '차익매수체결수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_cvolcha',
                'length': 6,
                'name': '차익순매수수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_bdvolcha',
                'length': 6,
                'name': '비차익매도체결수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_bsvolcha',
                'length': 6,
                'name': '비차익매수체결수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_bvolcha',
                'length': 6,
                'name': '비차익순매수수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_tdvolcha',
                'length': 6,
                'name': '전체매도체결수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_tsvolcha',
                'length': 6,
                'name': '전체매수체결수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_tvolcha',
                'length': 6,
                'name': '전체순매수수량직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_cdvalcha',
                'length': 8,
                'name': '차익매도체결금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_csvalcha',
                'length': 8,
                'name': '차익매수체결금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_cvalcha',
                'length': 8,
                'name': '차익순매수금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_bdvalcha',
                'length': 8,
                'name': '비차익매도체결금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_bsvalcha',
                'length': 8,
                'name': '비차익매수체결금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_bvalcha',
                'length': 8,
                'name': '비차익순매수금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_tdvalcha',
                'length': 8,
                'name': '전체매도체결금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_tsvalcha',
                'length': 8,
                'name': '전체매수체결금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'p_tvalcha',
                'length': 8,
                'name': '전체순매수금액직전대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'gubun',
                'length': 1,
                'name': '구분값',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_gubun',
                'length': 2,
                'name': '거래소별구분값',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'US2': {
        'tr_cd': 'US2',
        'title': '(통합)우선호가',
        'fields': [
            {
                'key': 'offerho',
                'length': 8,
                'name': '매도호가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho',
                'length': 8,
                'name': '매수호가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'shcode',
                'length': 9,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_shcode',
                'length': 10,
                'name': '거래소별단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'US3': {
        'tr_cd': 'US3',
        'title': '(통합)체결',
        'fields': [
            {
                'key': 'chetime',
                'length': 6,
                'name': '체결시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sign',
                'length': 1,
                'name': '전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': 8,
                'name': '전일대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'drate',
                'length': 6.2,
                'name': '등락율',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'price',
                'length': 8,
                'name': '현재가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'opentime',
                'length': 6,
                'name': '시가시간',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'open',
                'length': 8,
                'name': '시가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'hightime',
                'length': 6,
                'name': '고가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'high',
                'length': 8,
                'name': '고가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'lowtime',
                'length': 6,
                'name': '저가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low',
                'length': 8,
                'name': '저가',
                'required': True,
                'type': 'float'
            },
            {
                'desc': '+ : 매수<br/>- : 매도',
                'key': 'cgubun',
                'length': 1,
                'name': '체결구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cvolume',
                'length': 8,
                'name': '체결량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'volume',
                'length': 12,
                'name': '누적거래량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'value',
                'length': 12,
                'name': '누적거래대금',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdvolume',
                'length': 12,
                'name': '매도누적체결량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mdchecnt',
                'length': 8,
                'name': '매도누적체결건수',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msvolume',
                'length': 12,
                'name': '매수누적체결량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mschecnt',
                'length': 8,
                'name': '매수누적체결건수',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'cpower',
                'length': 9.2,
                'name': '체결강도',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'w_avrg',
                'length': 8,
                'name': '가중평균가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'offerho',
                'length': 8,
                'name': '매도호가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'bidho',
                'length': 8,
                'name': '매수호가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'status',
                'length': 2,
                'name': '장정보',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jnilvolume',
                'length': 12,
                'name': '전일동시간대거래량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'shcode',
                'length': 9,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': 'KRX, NXT',
                'key': 'exchname',
                'length': 3,
                'name': '거래소명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_shcode',
                'length': 10,
                'name': '거래소별단축코드',
                'required': True,
                'type': 'float'
            }
        ]
    },
    'UVI': {
        'tr_cd': 'UVI',
        'title': '(통합)VI발동해제',
        'fields': [
            {
                'desc': '0:해제1:정적발동2:동적발동3:정적&동적',
                'key': 'krx_vi_gubun',
                'length': 1,
                'name': 'KRXVI구분 (0:해제1:정적발동2:동적발동3:정적&동적)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'krx_svi_recprice',
                'length': 8,
                'name': 'KRX정적VI발동기준가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_dvi_recprice',
                'length': 8,
                'name': 'KRX동적VI발동기준가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_vi_trgprice',
                'length': 8,
                'name': 'KRXVI발동가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'krx_time',
                'length': 6,
                'name': 'KRX시간',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '0:해제1:정적발동2:동적발동3:정적&동적',
                'key': 'nxt_vi_gubun',
                'length': None,
                'name': 'NXTVI구분(0:해제1:정적발동2:동적발동3:정적&동적)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'nxt_svi_recprice',
                'length': 8,
                'name': 'NXT정적VI발동기준가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_dvi_recprice',
                'length': 8,
                'name': 'NXT동적VI발동기준가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_vi_trgprice',
                'length': 8,
                'name': 'NXTVI발동가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'nxt_time',
                'length': 6,
                'name': 'NXT시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': 9,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ref_shcode',
                'length': 6,
                'name': '참조코드(미사용)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchname',
                'length': 3,
                'name': '거래소명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_shcode',
                'length': 10,
                'name': '거래소별단축코드',
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
                'key': 'hotime',
                'length': 6,
                'name': '호가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'yeprice',
                'length': 8,
                'name': '예상체결가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'yevolume',
                'length': 12,
                'name': '예상체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'jnilysign',
                'length': 1,
                'name': '예상체결가전일종가대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jnilchange',
                'length': 8,
                'name': '예상체결가전일종가대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'jnilydrate',
                'length': 6.2,
                'name': '예상체결가전일종가등락율',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'yofferho0',
                'length': 8,
                'name': '예상매도호가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ybidho0',
                'length': 8,
                'name': '예상매수호가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'yofferrem0',
                'length': 12,
                'name': '예상매도호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ybidrem0',
                'length': 12,
                'name': '예상매수호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'shcode',
                'length': 9,
                'name': '단축코드',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'exchname',
                'length': 3,
                'name': '거래소명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ex_shcode',
                'length': 10,
                'name': '거래소별단축코드',
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
                'key': 'vi_gubun',
                'length': '	1',
                'name': '구분(0:해제1:정적발동2:동적발동3:정적&동적)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'svi_recprice',
                'length': '	8',
                'name': '정적VI발동기준가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dvi_recprice',
                'length': '	8',
                'name': '동적VI발동기준가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'vi_trgprice',
                'length': '	8',
                'name': 'VI발동가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': '	6',
                'name': '단축코드(KEY)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ref_shcode',
                'length': '	6',
                'name': '참조코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'time',
                'length': '	6',
                'name': '시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchname',
                'length': 3,
                'name': '거래소명',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'YJ_': {
        'tr_cd': 'YJ_',
        'title': '예상지수',
        'fields': [
            {
                'key': 'time',
                'length': '	6',
                'name': '시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jisu',
                'length': '	8.2',
                'name': '예상지수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sign',
                'length': '	1',
                'name': '예상전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': '	8.2',
                'name': '예상전일비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'drate',
                'length': '	6.2',
                'name': '예상등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cvolume',
                'length': '	8',
                'name': '예상체결량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volume',
                'length': '	8',
                'name': '누적거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'value',
                'length': '	8',
                'name': '예상거래대금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'upcode',
                'length': '	3',
                'name': '업종코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'YK3': {
        'tr_cd': 'YK3',
        'title': 'KOSDAQ예상체결',
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
            },
            {
                'key': 'exchname',
                'length': 3,
                'name': '거래소명',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'YS3': {
        'tr_cd': 'YS3',
        'title': 'KOSPI예상체결',
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
            },
            {
                'key': 'exchname',
                'length': 3,
                'name': '거래소명',
                'required': True,
                'type': 'string'
            }
        ]
    },
    't0150': {
        'tr_cd': 't0150',
        'title': '주식당일매매일지/수수료',
        'blocks': {
            't0150OutBlock': {
                'fields': [{'key': 'mdqty', 'name': '매도수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'mdamt', 'name': '매도약정금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'mdfee', 'name': '매도수수료', 'type': 'float', 'length': 18, 'required': True}, {'key': 'mdtax', 'name': '매도거래세', 'type': 'float', 'length': 18, 'required': True}, {'key': 'mdargtax', 'name': '매도농특세', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tmdtax', 'name': '매도제비용합', 'type': 'float', 'length': 18, 'required': True}, {'key': 'mdadjamt', 'name': '매도정산금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'msqty', 'name': '매수수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'msamt', 'name': '매수약정금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'msfee', 'name': '매수수수료', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tmstax', 'name': '매수제비용합', 'type': 'float', 'length': 18, 'required': True}, {'key': 'msadjamt', 'name': '매수정산금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tqty', 'name': '합계수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'tamt', 'name': '합계약정금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tfee', 'name': '합계수수료', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tottax', 'name': '합계거래세', 'type': 'float', 'length': 18, 'required': True}, {'key': 'targtax', 'name': '합계농특세', 'type': 'float', 'length': 18, 'required': True}, {'key': 'ttax', 'name': '합계제비용합', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tadjamt', 'name': '합계정산금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'cts_medosu', 'name': 'CTS_매매구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'cts_expcode', 'name': 'CTS_종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'cts_price', 'name': 'CTS_단가', 'type': 'string', 'length': 9, 'required': True}, {'key': 'cts_middiv', 'name': 'CTS_매체', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            't0150OutBlock1': {
                'fields': [{'key': 'medosu', 'name': '매매구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'expcode', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'qty', 'name': '수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'price', 'name': '단가', 'type': 'float', 'length': 9, 'required': True}, {'key': 'amt', 'name': '약정금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'fee', 'name': '수수료', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tax', 'name': '거래세', 'type': 'float', 'length': 18, 'required': True}, {'key': 'argtax', 'name': '농특세', 'type': 'float', 'length': 18, 'required': True}, {'key': 'adjamt', 'name': '정산금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'middiv', 'name': '매체', 'type': 'string', 'length': 20, 'required': True}],
                'type': 'array'
            }
        }
    },
    't0151': {
        'tr_cd': 't0151',
        'title': '주식당일매매일지/수수료(전일)',
        'blocks': {
            't0151OutBlock': {
                'fields': [{'key': 'mdqty', 'name': '매도수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'mdamt', 'name': '매도약정금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'mdfee', 'name': '매도수수료', 'type': 'float', 'length': 18, 'required': True}, {'key': 'mdtax', 'name': '매도거래세', 'type': 'float', 'length': 18, 'required': True}, {'key': 'mdargtax', 'name': '매도농특세', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tmdtax', 'name': '매도제비용합', 'type': 'float', 'length': 18, 'required': True}, {'key': 'mdadjamt', 'name': '매도정산금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'msqty', 'name': '매수수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'msamt', 'name': '매수약정금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'msfee', 'name': '매수수수료', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tmstax', 'name': '매수제비용합', 'type': 'float', 'length': 18, 'required': True}, {'key': 'msadjamt', 'name': '매수정산금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tqty', 'name': '합계수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'tamt', 'name': '합계약정금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tfee', 'name': '합계수수료', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tottax', 'name': '합계거래세', 'type': 'float', 'length': 18, 'required': True}, {'key': 'targtax', 'name': '합계농특세', 'type': 'float', 'length': 18, 'required': True}, {'key': 'ttax', 'name': '합계제비용합', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tadjamt', 'name': '합계정산금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'cts_medosu', 'name': 'CTS_매매구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'cts_expcode', 'name': 'CTS_종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'cts_price', 'name': 'CTS_단가', 'type': 'string', 'length': 9, 'required': True}, {'key': 'cts_middiv', 'name': 'CTS_매체', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            't0151OutBlock1': {
                'fields': [{'key': 'medosu', 'name': '매매구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'expcode', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'qty', 'name': '수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'price', 'name': '단가', 'type': 'float', 'length': 9, 'required': True}, {'key': 'amt', 'name': '약정금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'fee', 'name': '수수료', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tax', 'name': '거래세', 'type': 'float', 'length': 18, 'required': True}, {'key': 'argtax', 'name': '농특세', 'type': 'float', 'length': 18, 'required': True}, {'key': 'adjamt', 'name': '정산금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'middiv', 'name': '매체', 'type': 'string', 'length': 20, 'required': True}],
                'type': 'array'
            }
        }
    },
    't0167': {
        'tr_cd': 't0167',
        'title': '서버시간조회',
        'blocks': {
            't0167OutBlock': {
                'fields': [{'key': 'dt', 'name': '일자(YYYYMMDD)', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간(HHMMSSssssss)', 'type': 'string', 'length': 12, 'required': True}],
                'type': 'single'
            }
        }
    },
    't0424': {
        'tr_cd': 't0424',
        'title': '주식잔고2',
        'blocks': {
            't0424OutBlock': {
                'fields': [{'key': 'sunamt', 'name': '추정순자산', 'type': 'float', 'length': 18, 'required': True}, {'key': 'dtsunik', 'name': '실현손익', 'type': 'float', 'length': 18, 'required': True}, {'key': 'mamt', 'name': '매입금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'sunamt1', 'name': '추정D2예수금', 'type': 'float', 'length': 18, 'required': True}, {'key': 'cts_expcode', 'name': 'CTS_종목번호', 'type': 'string', 'length': 22, 'required': True}, {'key': 'tappamt', 'name': '평가금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tdtsunik', 'name': '평가손익', 'type': 'float', 'length': 18, 'required': True}],
                'type': 'single'
            },
            't0424OutBlock1': {
                'fields': [{'key': 'expcode', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'jangb', 'name': '잔고구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'janqty', 'name': '잔고수량', 'type': 'float', 'length': 18, 'required': True}, {'key': 'mdposqt', 'name': '매도가능수량', 'type': 'float', 'length': 18, 'required': True}, {'key': 'pamt', 'name': '평균단가', 'type': 'float', 'length': 18, 'required': True}, {'key': 'mamt', 'name': '매입금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'sinamt', 'name': '대출금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'lastdt', 'name': '만기일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'msat', 'name': '당일매수금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'mpms', 'name': '당일매수단가', 'type': 'float', 'length': 18, 'required': True}, {'key': 'mdat', 'name': '당일매도금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'mpmd', 'name': '당일매도단가', 'type': 'float', 'length': 18, 'required': True}, {'key': 'jsat', 'name': '전일매수금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'jpms', 'name': '전일매수단가', 'type': 'float', 'length': 18, 'required': True}, {'key': 'jdat', 'name': '전일매도금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'jpmd', 'name': '전일매도단가', 'type': 'float', 'length': 18, 'required': True}, {'key': 'sysprocseq', 'name': '처리순번', 'type': 'float', 'length': 10, 'required': True}, {'key': 'loandt', 'name': '대출일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'marketgb', 'name': '시장구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'jonggb', 'name': '종목구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'janrt', 'name': '보유비중', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'appamt', 'name': '평가금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'dtsunik', 'name': '평가손익', 'type': 'float', 'length': 18, 'required': True}, {'key': 'sunikrt', 'name': '수익율', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'fee', 'name': '수수료', 'type': 'float', 'length': 10, 'required': True}, {'key': 'tax', 'name': '제세금', 'type': 'float', 'length': 10, 'required': True}, {'key': 'sininter', 'name': '신용이자', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'array'
            }
        }
    },
    't0425': {
        'tr_cd': 't0425',
        'title': '주식체결/미체결',
        'blocks': {
            't0425OutBlock': {
                'fields': [{'key': 'tqty', 'name': '총주문수량', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tcheqty', 'name': '총체결수량', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tordrem', 'name': '총미체결수량', 'type': 'float', 'length': 18, 'required': True}, {'key': 'cmss', 'name': '추정수수료', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tamt', 'name': '총주문금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tmdamt', 'name': '총매도체결금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tmsamt', 'name': '총매수체결금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tax', 'name': '추정제세금', 'type': 'float', 'length': 18, 'required': True}, {'key': 'cts_ordno', 'name': '주문번호', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'single'
            },
            't0425OutBlock1': {
                'fields': [{'key': 'ordno', 'name': '주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'expcode', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'medosu', 'name': '구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'qty', 'name': '주문수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'price', 'name': '주문가격', 'type': 'float', 'length': 9, 'required': True}, {'key': 'cheqty', 'name': '체결수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'cheprice', 'name': '체결가격', 'type': 'float', 'length': 9, 'required': True}, {'key': 'ordrem', 'name': '미체결잔량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'cfmqty', 'name': '확인수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'status', 'name': '상태', 'type': 'string', 'length': 20, 'required': True}, {'key': 'orgordno', 'name': '원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'ordgb', 'name': '유형', 'type': 'string', 'length': 20, 'required': True}, {'key': 'ordtime', 'name': '주문시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'ordermtd', 'name': '주문매체', 'type': 'string', 'length': 10, 'required': True}, {'key': 'sysprocseq', 'name': '처리순번', 'type': 'float', 'length': 10, 'required': True}, {'key': 'hogagb', 'name': '호가유형', 'type': 'string', 'length': 2, 'required': True}, {'key': 'price1', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'orggb', 'name': '주문구분', 'type': 'string', 'length': 2, 'required': True}, {'key': 'singb', 'name': '신용구분', 'type': 'string', 'length': 2, 'required': True}, {'key': 'loandt', 'name': '대출일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'exchname', 'name': '거래소명', 'type': 'string', 'length': 3, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1101': {
        'tr_cd': 't1101',
        'title': '주식현재가호가조회',
        'blocks': {
            't1101OutBlock': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho1', 'name': '매도호가1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho1', 'name': '매수호가1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem1', 'name': '매도호가수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem1', 'name': '매수호가수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha1', 'name': '직전매도대비수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha1', 'name': '직전매수대비수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho2', 'name': '매도호가2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho2', 'name': '매수호가2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem2', 'name': '매도호가수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem2', 'name': '매수호가수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha2', 'name': '직전매도대비수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha2', 'name': '직전매수대비수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho3', 'name': '매도호가3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho3', 'name': '매수호가3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem3', 'name': '매도호가수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem3', 'name': '매수호가수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha3', 'name': '직전매도대비수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha3', 'name': '직전매수대비수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho4', 'name': '매도호가4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho4', 'name': '매수호가4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem4', 'name': '매도호가수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem4', 'name': '매수호가수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha4', 'name': '직전매도대비수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha4', 'name': '직전매수대비수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho5', 'name': '매도호가5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho5', 'name': '매수호가5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem5', 'name': '매도호가수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem5', 'name': '매수호가수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha5', 'name': '직전매도대비수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha5', 'name': '직전매수대비수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho6', 'name': '매도호가6', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho6', 'name': '매수호가6', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem6', 'name': '매도호가수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem6', 'name': '매수호가수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha6', 'name': '직전매도대비수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha6', 'name': '직전매수대비수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho7', 'name': '매도호가7', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho7', 'name': '매수호가7', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem7', 'name': '매도호가수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem7', 'name': '매수호가수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha7', 'name': '직전매도대비수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha7', 'name': '직전매수대비수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho8', 'name': '매도호가8', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho8', 'name': '매수호가8', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem8', 'name': '매도호가수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem8', 'name': '매수호가수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha8', 'name': '직전매도대비수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha8', 'name': '직전매수대비수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho9', 'name': '매도호가9', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho9', 'name': '매수호가9', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem9', 'name': '매도호가수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem9', 'name': '매수호가수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha9', 'name': '직전매도대비수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha9', 'name': '직전매수대비수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho10', 'name': '매도호가10', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho10', 'name': '매수호가10', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem10', 'name': '매도호가수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem10', 'name': '매수호가수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha10', 'name': '직전매도대비수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha10', 'name': '직전매수대비수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offer', 'name': '매도호가수량합', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bid', 'name': '매수호가수량합', 'type': 'float', 'length': 12, 'required': True}, {'key': 'preoffercha', 'name': '직전매도대비수량합', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha', 'name': '직전매수대비수량합', 'type': 'float', 'length': 12, 'required': True}, {'key': 'hotime', 'name': '수신시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'yeprice', 'name': '예상체결가격', 'type': 'float', 'length': 8, 'required': True}, {'key': 'yevolume', 'name': '예상체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'yesign', 'name': '예상체결전일구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'yechange', 'name': '예상체결전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'yediff', 'name': '예상체결등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'tmoffer', 'name': '시간외매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tmbid', 'name': '시간외매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ho_status', 'name': '동시구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'uplmtprice', 'name': '상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dnlmtprice', 'name': '하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'krx_midprice', 'name': 'KRX중간가격', 'type': 'float', 'length': 8, 'required': True}, {'key': 'krx_offermidsumrem', 'name': 'KRX매도중간가잔량합계수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'krx_bidmidsumrem', 'name': 'KRX매수중간가잔량합계수량 ', 'type': 'float', 'length': 9, 'required': True}, {'key': 'krx_midsumrem', 'name': 'KRX중간가잔량합계수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'krx_midsumremgubun', 'name': 'KRX중간가잔량구분', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1102': {
        'tr_cd': 't1102',
        'title': '주식현재가(시세)조회',
        'blocks': {
            't1102OutBlock': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'recprice', 'name': '기준가(평가가격)', 'type': 'float', 'length': 8, 'required': True}, {'key': 'avg', 'name': '가중평균', 'type': 'float', 'length': 8, 'required': True}, {'key': 'uplmtprice', 'name': '상한가(최고호가가격)', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dnlmtprice', 'name': '하한가(최저호가가격)', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jnilvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'volumediff', 'name': '거래량차', 'type': 'float', 'length': 12, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'opentime', 'name': '시가시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'hightime', 'name': '고가시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'lowtime', 'name': '저가시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'high52w', 'name': '52최고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high52wdate', 'name': '52최고가일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'low52w', 'name': '52최저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low52wdate', 'name': '52최저가일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'exhratio', 'name': '소진율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'per', 'name': 'PER', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'pbrx', 'name': 'PBRX', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'listing', 'name': '상장주식수(천)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jkrate', 'name': '증거금율', 'type': 'float', 'length': 8, 'required': True}, {'key': 'memedan', 'name': '수량단위', 'type': 'string', 'length': 5, 'required': True}, {'key': 'offernocd1', 'name': '매도증권사코드1', 'type': 'string', 'length': 3, 'required': True}, {'key': 'bidnocd1', 'name': '매수증권사코드1', 'type': 'string', 'length': 3, 'required': True}, {'key': 'offerno1', 'name': '매도증권사명1', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bidno1', 'name': '매수증권사명1', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dvol1', 'name': '총매도수량1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'svol1', 'name': '총매수수량1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcha1', 'name': '매도증감1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scha1', 'name': '매수증감1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ddiff1', 'name': '매도비율1', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sdiff1', 'name': '매수비율1', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offernocd2', 'name': '매도증권사코드2', 'type': 'string', 'length': 3, 'required': True}, {'key': 'bidnocd2', 'name': '매수증권사코드2', 'type': 'string', 'length': 3, 'required': True}, {'key': 'offerno2', 'name': '매도증권사명2', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bidno2', 'name': '매수증권사명2', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dvol2', 'name': '총매도수량2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'svol2', 'name': '총매수수량2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcha2', 'name': '매도증감2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scha2', 'name': '매수증감2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ddiff2', 'name': '매도비율2', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sdiff2', 'name': '매수비율2', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offernocd3', 'name': '매도증권사코드3', 'type': 'string', 'length': 3, 'required': True}, {'key': 'bidnocd3', 'name': '매수증권사코드3', 'type': 'string', 'length': 3, 'required': True}, {'key': 'offerno3', 'name': '매도증권사명3', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bidno3', 'name': '매수증권사명3', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dvol3', 'name': '총매도수량3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'svol3', 'name': '총매수수량3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcha3', 'name': '매도증감3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scha3', 'name': '매수증감3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ddiff3', 'name': '매도비율3', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sdiff3', 'name': '매수비율3', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offernocd4', 'name': '매도증권사코드4', 'type': 'string', 'length': 3, 'required': True}, {'key': 'bidnocd4', 'name': '매수증권사코드4', 'type': 'string', 'length': 3, 'required': True}, {'key': 'offerno4', 'name': '매도증권사명4', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bidno4', 'name': '매수증권사명4', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dvol4', 'name': '총매도수량4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'svol4', 'name': '총매수수량4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcha4', 'name': '매도증감4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scha4', 'name': '매수증감4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ddiff4', 'name': '매도비율4', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sdiff4', 'name': '매수비율4', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offernocd5', 'name': '매도증권사코드5', 'type': 'string', 'length': 3, 'required': True}, {'key': 'bidnocd5', 'name': '매수증권사코드5', 'type': 'string', 'length': 3, 'required': True}, {'key': 'offerno5', 'name': '매도증권사명5', 'type': 'string', 'length': 6, 'required': True}, {'key': 'bidno5', 'name': '매수증권사명5', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dvol5', 'name': '총매도수량5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'svol5', 'name': '총매수수량5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcha5', 'name': '매도증감5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scha5', 'name': '매수증감5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ddiff5', 'name': '매도비율5', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sdiff5', 'name': '매수비율5', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'fwdvl', 'name': '외국계매도합계수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ftradmdcha', 'name': '외국계매도직전대비', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ftradmddiff', 'name': '외국계매도비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'fwsvl', 'name': '외국계매수합계수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ftradmscha', 'name': '외국계매수직전대비', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ftradmsdiff', 'name': '외국계매수비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'vol', 'name': '회전율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'value', 'name': '누적거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jvolume', 'name': '전일동시간거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'highyear', 'name': '연중최고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'highyeardate', 'name': '연중최고일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'lowyear', 'name': '연중최저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'lowyeardate', 'name': '연중최저일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'target', 'name': '목표가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'capital', 'name': '자본금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'abscnt', 'name': '유동주식수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'parprice', 'name': '액면가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'gsmm', 'name': '결산월', 'type': 'string', 'length': 2, 'required': True}, {'key': 'subprice', 'name': '대용가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'total', 'name': '시가총액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'listdate', 'name': '상장일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'name', 'name': '전분기명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'bfsales', 'name': '전분기매출액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bfoperatingincome', 'name': '전분기영업이익', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bfordinaryincome', 'name': '전분기경상이익', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bfnetincome', 'name': '전분기순이익', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bfeps', 'name': '전분기EPS', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'name2', 'name': '전전분기명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'bfsales2', 'name': '전전분기매출액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bfoperatingincome2', 'name': '전전분기영업이익', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bfordinaryincome2', 'name': '전전분기경상이익', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bfnetincome2', 'name': '전전분기순이익', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bfeps2', 'name': '전전분기EPS', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'salert', 'name': '전년대비매출액', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'opert', 'name': '전년대비영업이익', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'ordrt', 'name': '전년대비경상이익', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'netrt', 'name': '전년대비순이익', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'epsrt', 'name': '전년대비EPS', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'info1', 'name': '락구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'info2', 'name': '관리/급등구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'info3', 'name': '정지/연장구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'info4', 'name': '투자/불성실구분', 'type': 'string', 'length': 12, 'required': True}, {'key': 'janginfo', 'name': '장구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 't_per', 'name': 'T.PER', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'tonghwa', 'name': '통화ISO코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'dval1', 'name': '총매도대금1', 'type': 'float', 'length': 18, 'required': True}, {'key': 'sval1', 'name': '총매수대금1', 'type': 'float', 'length': 18, 'required': True}, {'key': 'dval2', 'name': '총매도대금2', 'type': 'float', 'length': 18, 'required': True}, {'key': 'sval2', 'name': '총매수대금2', 'type': 'float', 'length': 18, 'required': True}, {'key': 'dval3', 'name': '총매도대금3', 'type': 'float', 'length': 18, 'required': True}, {'key': 'sval3', 'name': '총매수대금3', 'type': 'float', 'length': 18, 'required': True}, {'key': 'dval4', 'name': '총매도대금4', 'type': 'float', 'length': 18, 'required': True}, {'key': 'sval4', 'name': '총매수대금4', 'type': 'float', 'length': 18, 'required': True}, {'key': 'dval5', 'name': '총매도대금5', 'type': 'float', 'length': 18, 'required': True}, {'key': 'sval5', 'name': '총매수대금5', 'type': 'float', 'length': 18, 'required': True}, {'key': 'davg1', 'name': '총매도평단가1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'savg1', 'name': '총매수평단가1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'davg2', 'name': '총매도평단가2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'savg2', 'name': '총매수평단가2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'davg3', 'name': '총매도평단가3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'savg3', 'name': '총매수평단가3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'davg4', 'name': '총매도평단가4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'savg4', 'name': '총매수평단가4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'davg5', 'name': '총매도평단가5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'savg5', 'name': '총매수평단가5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ftradmdval', 'name': '외국계매도대금', 'type': 'float', 'length': 18, 'required': True}, {'key': 'ftradmsval', 'name': '외국계매수대금', 'type': 'float', 'length': 18, 'required': True}, {'key': 'ftradmdvag', 'name': '외국계매도평단가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ftradmsvag', 'name': '외국계매수평단가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'info5', 'name': '투자주의환기', 'type': 'string', 'length': 8, 'required': True}, {'key': 'spac_gubun', 'name': '기업인수목적회사여부', 'type': 'string', 'length': 1, 'required': True}, {'key': 'issueprice', 'name': '발행가격', 'type': 'float', 'length': 8, 'required': True}, {'key': 'alloc_gubun', 'name': '배분적용구분코드(1:배분발생2:배분해제그외:미발생)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'alloc_text', 'name': '배분적용구분', 'type': 'string', 'length': 8, 'required': True}, {'key': 'shterm_text', 'name': '단기과열/VI발동', 'type': 'string', 'length': 10, 'required': True}, {'key': 'svi_uplmtprice', 'name': '정적VI상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'svi_dnlmtprice', 'name': '정적VI하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low_lqdt_gu', 'name': '저유동성종목여부', 'type': 'string', 'length': 1, 'required': True}, {'key': 'abnormal_rise_gu', 'name': '이상급등종목여부', 'type': 'string', 'length': 1, 'required': True}, {'key': 'lend_text', 'name': '대차불가표시', 'type': 'string', 'length': 8, 'required': True}, {'key': 'ty_text', 'name': 'ETF/ETN투자유의', 'type': 'string', 'length': 8, 'required': True}, {'key': 'nxt_janginfo', 'name': 'NXT장구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'nxt_shterm_text', 'name': 'NXT단기과열/VI발동', 'type': 'string', 'length': 10, 'required': True}, {'key': 'nxt_svi_uplmtprice', 'name': 'NXT정적VI상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'nxt_svi_dnlmtprice', 'name': 'NXT정적VI하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ex_shcode', 'name': '거래소별단축코드', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1104': {
        'tr_cd': 't1104',
        'title': '주식현재가시세메모',
        'blocks': {
            't1104OutBlock': {
                'fields': [{'key': 'nrec', 'name': '출력건수', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            't1104OutBlock1': {
                'fields': [{'key': 'indx', 'name': '인덱스', 'type': 'string', 'length': 1, 'required': True}, {'key': 'gubn', 'name': '조건구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'vals', 'name': '출력값', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1105': {
        'tr_cd': 't1105',
        'title': '주식피봇/디마크조회',
        'blocks': {
            't1105OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'pbot', 'name': '피봇', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offer1', 'name': '1차저항', 'type': 'float', 'length': 8, 'required': True}, {'key': 'supp1', 'name': '1차지지', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offer2', 'name': '2차저항', 'type': 'float', 'length': 8, 'required': True}, {'key': 'supp2', 'name': '2차지지', 'type': 'float', 'length': 8, 'required': True}, {'key': 'stdprc', 'name': '기준가격', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerd', 'name': 'D저항', 'type': 'float', 'length': 8, 'required': True}, {'key': 'suppd', 'name': 'D지지', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1109': {
        'tr_cd': 't1109',
        'title': '시간외체결량',
        'blocks': {
            't1109OutBlock': {
                'fields': [{'key': 'ctsshcode', 'name': '종목cts', 'type': 'string', 'length': 6, 'required': True}, {'key': 'ctschetime', 'name': '체결cts', 'type': 'string', 'length': 10, 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1109OutBlock1': {
                'fields': [{'key': 'dan_chetime', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'dan_price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dan_sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'dan_change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'dan_cvolume', 'name': '체결량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'chdegree', 'name': '체결강도', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'dan_volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1301': {
        'tr_cd': 't1301',
        'title': '주식시간대별체결조회',
        'blocks': {
            't1301OutBlock': {
                'fields': [{'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'single'
            },
            't1301OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'chdegree', 'name': '체결강도', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdvolume', 'name': '매도체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdchecnt', 'name': '매도체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'msvolume', 'name': '매수체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mschecnt', 'name': '매수체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'revolume', 'name': '순체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rechecnt', 'name': '순체결건수', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1302': {
        'tr_cd': 't1302',
        'title': '주식분별주가조회',
        'blocks': {
            't1302OutBlock': {
                'fields': [{'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            },
            't1302OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'chdegree', 'name': '체결강도', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'mdvolume', 'name': '매도체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'msvolume', 'name': '매수체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'revolume', 'name': '순매수체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdchecnt', 'name': '매도체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'mschecnt', 'name': '매수체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'rechecnt', 'name': '순체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'cvolume', 'name': '체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdchecnttm', 'name': '매도체결건수(시간)', 'type': 'float', 'length': 8, 'required': True}, {'key': 'mschecnttm', 'name': '매수체결건수(시간)', 'type': 'float', 'length': 8, 'required': True}, {'key': 'totofferrem', 'name': '매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'totbidrem', 'name': '매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdvolumetm', 'name': '시간별매도체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'msvolumetm', 'name': '시간별매수체결량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1305': {
        'tr_cd': 't1305',
        'title': '기간별주가',
        'blocks': {
            't1305OutBlock': {
                'fields': [{'key': 'cnt', 'name': 'CNT', 'type': 'float', 'length': 4, 'required': True}, {'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}, {'key': 'ex_shcode', 'name': '거래소별단축코드', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'single'
            },
            't1305OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'diff_vol', 'name': '거래증가율', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'chdegree', 'name': '체결강도', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sojinrate', 'name': '소진율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'changerate', 'name': '회전율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'fpvolume', 'name': '외인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'covolume', 'name': '기관순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'value', 'name': '누적거래대금(단위:백만)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ppvolume', 'name': '개인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'o_sign', 'name': '시가대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'o_change', 'name': '시가대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'o_diff', 'name': '시가기준등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'h_sign', 'name': '고가대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'h_change', 'name': '고가대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'h_diff', 'name': '고가기준등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'l_sign', 'name': '저가대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'l_change', 'name': '저가대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'l_diff', 'name': '저가기준등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'marketcap', 'name': '시가총액(단위:백만)', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1308': {
        'tr_cd': 't1308',
        'title': '주식시간대별체결조회챠트',
        'blocks': {
            't1308OutBlock': {
                'fields': [{'key': 'ex_shcode', 'name': '거래소별단축코드', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'single'
            },
            't1308OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'chdegvol', 'name': '체결강도(거래량)', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'chdegcnt', 'name': '체결강도(건수)', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdvolume', 'name': '매도체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdchecnt', 'name': '매도체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'msvolume', 'name': '매수체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mschecnt', 'name': '매수체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1310': {
        'tr_cd': 't1310',
        'title': '주식당일전일분틱조회',
        'blocks': {
            't1310OutBlock': {
                'fields': [{'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'single'
            },
            't1310OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'chdegree', 'name': '체결강도', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdvolume', 'name': '매도체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdchecnt', 'name': '매도체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'msvolume', 'name': '매수체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mschecnt', 'name': '매수체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'revolume', 'name': '순체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rechecnt', 'name': '순체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'exchname', 'name': '거래소명', 'type': 'string', 'length': 3, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1403': {
        'tr_cd': 't1403',
        'title': '신규상장종목조회',
        'blocks': {
            't1403OutBlock': {
                'fields': [{'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1403OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'kmprice', 'name': '공모가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'date', 'name': '등록일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'recprice', 'name': '등록일기준가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'kmdiff', 'name': '기준가등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'close', 'name': '등록일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'recdiff', 'name': '등록일등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1404': {
        'tr_cd': 't1404',
        'title': '관리/불성실/투자유의조회',
        'blocks': {
            't1404OutBlock': {
                'fields': [{'key': 'cts_shcode', 'name': '종목코드_CTS', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            },
            't1404OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'date', 'name': '지정일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'tprice', 'name': '지정일주가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'tchange', 'name': '지정일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'tdiff', 'name': '대비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'reason', 'name': '사유', 'type': 'string', 'length': 4, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'edate', 'name': '해제일', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1405': {
        'tr_cd': 't1405',
        'title': '투자경고/매매정지/정리매매조회',
        'blocks': {
            't1405OutBlock': {
                'fields': [{'key': 'cts_shcode', 'name': '종목코드_CTS', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            },
            't1405OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'date', 'name': '지정일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'edate', 'name': '해제일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1410': {
        'tr_cd': 't1410',
        'title': '초저유동성조회',
        'blocks': {
            't1410OutBlock': {
                'fields': [{'key': 'cts_shcode', 'name': '종목코드_CTS', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            },
            't1410OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1411': {
        'tr_cd': 't1411',
        'title': '증거금율별종목조회',
        'blocks': {
            't1411OutBlock': {
                'fields': [{'key': 'jkrate', 'name': '위탁증거금율', 'type': 'float', 'length': 3, 'required': True}, {'key': 'sjkrate', 'name': '신용증거금율', 'type': 'float', 'length': 3, 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1411OutBlock1': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'jkrate', 'name': '위탁증거금율', 'type': 'float', 'length': 3, 'required': True}, {'key': 'sjkrate', 'name': '신용증거금율', 'type': 'float', 'length': 3, 'required': True}, {'key': 'subprice', 'name': '대용가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'recprice', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1422': {
        'tr_cd': 't1422',
        'title': '상/하한',
        'blocks': {
            't1422OutBlock': {
                'fields': [{'key': 'cnt', 'name': 'CNT', 'type': 'float', 'length': 4, 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1422OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'diff_vol', 'name': '거래증가율', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'offerrem1', 'name': '매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem1', 'name': '매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'last', 'name': '최종진입', 'type': 'string', 'length': 6, 'required': True}, {'key': 'lmtdaycnt', 'name': '연속', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jnilvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'ex_shcode', 'name': '거래소별단축코드', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1427': {
        'tr_cd': 't1427',
        'title': '상/하한가직전',
        'blocks': {
            't1427OutBlock': {
                'fields': [{'key': 'cnt', 'name': 'CNT', 'type': 'float', 'length': 4, 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1427OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'diff_vol', 'name': '거래증가율', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'lmtprice', 'name': '상한가/하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'rate', 'name': '대비율', 'type': 'float', 'length': 12.2, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'jnilvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'lmtdaycnt', 'name': '연속', 'type': 'float', 'length': 8, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'total', 'name': '시가총액', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1441': {
        'tr_cd': 't1441',
        'title': '등락율상위',
        'blocks': {
            't1441OutBlock': {
                'fields': [{'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1441OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerrem1', 'name': '매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho1', 'name': '매도호가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidho1', 'name': '매수호가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem1', 'name': '매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'updaycnt', 'name': '연속', 'type': 'float', 'length': 4, 'required': True}, {'key': 'jnildiff', 'name': '전일등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'voldiff', 'name': '거래량대비율', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 15, 'required': True}, {'key': 'total', 'name': '시가총액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ex_shcode', 'name': '거래소별단축코드', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1442': {
        'tr_cd': 't1442',
        'title': '신고/신저가',
        'blocks': {
            't1442OutBlock': {
                'fields': [{'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1442OutBlock1': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'pastprice', 'name': '이전가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'pastsign', 'name': '이전가대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'pastchange', 'name': '이전가대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'pastdiff', 'name': '이전가대비율', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1444': {
        'tr_cd': 't1444',
        'title': '시가총액상위',
        'blocks': {
            't1444OutBlock': {
                'fields': [{'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1444OutBlock1': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'vol_rate', 'name': '거래비중', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'total', 'name': '시가총액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate', 'name': '비중', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'for_rate', 'name': '외인비중', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1449': {
        'tr_cd': 't1449',
        'title': '가격대별매매비중조회',
        'blocks': {
            't1449OutBlock': {
                'fields': [{'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'msvolume', 'name': '매수체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdvolume', 'name': '매도체결량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'single'
            },
            't1449OutBlock1': {
                'fields': [{'key': 'price', 'name': '체결가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'tickdiff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'diff', 'name': '비중', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'mdvolume', 'name': '매도체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'msvolume', 'name': '매수체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'msdiff', 'name': '매수비율', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1452': {
        'tr_cd': 't1452',
        'title': '거래량상위',
        'blocks': {
            't1452OutBlock': {
                'fields': [{'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1452OutBlock1': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'vol', 'name': '회전율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bef_diff', 'name': '전일비', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1463': {
        'tr_cd': 't1463',
        'title': '거래대금상위',
        'blocks': {
            't1463OutBlock': {
                'fields': [{'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1463OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jnilvalue', 'name': '전일거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bef_diff', 'name': '전일비', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'filler', 'name': 'filler', 'type': 'string', 'length': 1, 'required': True}, {'key': 'jnilvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ex_shcode', 'name': '거래소별단축코드', 'type': 'string', 'length': 10, 'required': True}, {'key': 'total', 'name': '시가총액', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1466': {
        'tr_cd': 't1466',
        'title': '전일동시간대비거래급증',
        'blocks': {
            't1466OutBlock': {
                'fields': [{'key': 'hhmm', 'name': '현재시분', 'type': 'string', 'length': 5, 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1466OutBlock1': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'stdvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'volume', 'name': '당일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'voldiff', 'name': '거래급등율', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ex_shcode', 'name': '거래소별단축코드', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1471': {
        'tr_cd': 't1471',
        'title': '시간대별호가잔량추이',
        'blocks': {
            't1471OutBlock1': {
                'fields': [{'key': 'time', 'name': '체결시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'preoffercha1', 'name': '메도증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerrem1', 'name': '매도우선잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho1', 'name': '매도우선호가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho1', 'name': '매수우선호가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem1', 'name': '매수우선잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prebidcha1', 'name': '매수증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'totofferrem', 'name': '총매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'totbidrem', 'name': '총매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'totsun', 'name': '순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'msrate', 'name': '매수비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1475': {
        'tr_cd': 't1475',
        'title': '체결강도추이',
        'blocks': {
            't1475OutBlock': {
                'fields': [{'key': 'date', 'name': '기준일자', 'type': 'float', 'length': 8, 'required': True}, {'key': 'time', 'name': '기준시간', 'type': 'float', 'length': 6, 'required': True}, {'key': 'rankcnt', 'name': '랭크카운터', 'type': 'float', 'length': 3, 'required': True}],
                'type': 'single'
            },
            't1475OutBlock1': {
                'fields': [{'key': 'datetime', 'name': '일자', 'type': 'string', 'length': 10, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'todayvp', 'name': '당일VP', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'ma5vp', 'name': '5일MAVP', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'ma20vp', 'name': '20일MAVP', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'ma60vp', 'name': '60일MAVP', 'type': 'float', 'length': 8.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1481': {
        'tr_cd': 't1481',
        'title': '시간외등락율상위',
        'blocks': {
            't1481OutBlock': {
                'fields': [{'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1481OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerrem1', 'name': '매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem1', 'name': '매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho1', 'name': '매도호가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidho1', 'name': '매수호가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'value', 'name': '누적거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'total', 'name': '시가총액(억)', 'type': 'float', 'length': 12, 'desc': '2026.01.15 16시 이후 적용예정', 'required': True}],
                'type': 'array'
            }
        }
    },
    't1482': {
        'tr_cd': 't1482',
        'title': '시간외거래량상위',
        'blocks': {
            't1482OutBlock': {
                'fields': [{'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1482OutBlock1': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'vol', 'name': '회전율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'value', 'name': '누적거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1485': {
        'tr_cd': 't1485',
        'title': '예상지수',
        'blocks': {
            't1485OutBlock': {
                'fields': [{'key': 'pricejisu', 'name': '현재지수', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'sign', 'name': '지수전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'yhighjo', 'name': '상승종목수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'yupjo', 'name': '상한종목수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'yunchgjo', 'name': '보합종목수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'ylowjo', 'name': '하락종목수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'ydownjo', 'name': '하한종목수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'ytrajo', 'name': '거래형성수', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1485OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'jisu', 'name': '예상지수', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'volume', 'name': '예상체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'volcha', 'name': '예상체결량직전대비', 'type': 'float', 'length': 12, 'required': True}, {'key': 'diff', 'name': '예상등락율', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1486': {
        'tr_cd': 't1486',
        'title': '시간별예상체결가',
        'blocks': {
            't1486OutBlock': {
                'fields': [{'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 10, 'required': True}, {'key': 'ex_shcode', 'name': '거래소별단축코드', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'single'
            },
            't1486OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'price', 'name': '예상체결가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '예상체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho1', 'name': '매도호가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho1', 'name': '매수호가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem1', 'name': '매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem1', 'name': '매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'exchname', 'name': '거래소명', 'type': 'string', 'length': 3, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1488': {
        'tr_cd': 't1488',
        'title': '예상체결가등락율상위조회',
        'blocks': {
            't1488OutBlock': {
                'fields': [{'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1488OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerrem', 'name': '매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho', 'name': '매도호가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho', 'name': '매수호가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem', 'name': '매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cnt', 'name': '연속일수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'jkrate', 'name': '증거금율', 'type': 'string', 'length': 3, 'required': True}, {'key': 'jnilvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1489': {
        'tr_cd': 't1489',
        'title': '예상체결량상위조회',
        'blocks': {
            't1489OutBlock': {
                'fields': [{'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1489OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '예상거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho', 'name': '매도호가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho', 'name': '매수호가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'jnilvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1492': {
        'tr_cd': 't1492',
        'title': '단일가예상등락율상위',
        'blocks': {
            't1492OutBlock': {
                'fields': [{'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1492OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '예상체결가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'yevolume', 'name': '예상체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerrem1', 'name': '매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem1', 'name': '매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho1', 'name': '매도호가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidho1', 'name': '매수호가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'value', 'name': '누적거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1511': {
        'tr_cd': 't1511',
        'title': '업종현재가',
        'blocks': {
            't1511OutBlock': {
                'fields': [{'key': 'gubun', 'name': '업종구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'hname', 'name': '업종명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'pricejisu', 'name': '현재지수', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jniljisu', 'name': '전일지수', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'diffjisu', 'name': '지수등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'volume', 'name': '당일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'volumechange', 'name': '거래량전일대비', 'type': 'float', 'length': 12, 'required': True}, {'key': 'volumerate', 'name': '거래량비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilvalue', 'name': '전일거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '당일거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'valuechange', 'name': '거래대금전일대비', 'type': 'float', 'length': 12, 'required': True}, {'key': 'valuerate', 'name': '거래대금비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'openjisu', 'name': '시가지수', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'opendiff', 'name': '시가등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'opentime', 'name': '시가시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'highjisu', 'name': '고가지수', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'highdiff', 'name': '고가등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'hightime', 'name': '고가시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'lowjisu', 'name': '저가지수', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'lowdiff', 'name': '저가등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'lowtime', 'name': '저가시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'whjisu', 'name': '52주최고지수', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'whchange', 'name': '52주최고현재가대비', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'whjday', 'name': '52주최고지수일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'wljisu', 'name': '52주최저지수', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'wlchange', 'name': '52주최저현재가대비', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'wljday', 'name': '52주최저지수일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'yhjisu', 'name': '연중최고지수', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'yhchange', 'name': '연중최고현재가대비', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'yhjday', 'name': '연중최고지수일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'yljisu', 'name': '연중최저지수', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'ylchange', 'name': '연중최저현재가대비', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'yljday', 'name': '연중최저지수일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'firstjcode', 'name': '첫번째지수코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'firstjname', 'name': '첫번째지수명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'firstjisu', 'name': '첫번째지수', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'firsign', 'name': '첫번째대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'firchange', 'name': '첫번째전일대비', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'firdiff', 'name': '첫번째등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'secondjcode', 'name': '두번째지수코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'secondjname', 'name': '두번째지수명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'secondjisu', 'name': '두번째지수', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'secsign', 'name': '두번째대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'secchange', 'name': '두번째전일대비', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'secdiff', 'name': '두번째등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'thirdjcode', 'name': '세번째지수코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'thirdjname', 'name': '세번째지수명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'thirdjisu', 'name': '세번째지수', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'thrsign', 'name': '세번째대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'thrchange', 'name': '세번째전일대비', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'thrdiff', 'name': '세번째등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'fourthjcode', 'name': '네번째지수코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'fourthjname', 'name': '네번째지수명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'fourthjisu', 'name': '네번째지수', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'forsign', 'name': '네번째대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'forchange', 'name': '네번째전일대비', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'fordiff', 'name': '네번째등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'highjo', 'name': '상승종목수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'upjo', 'name': '상한종목수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'unchgjo', 'name': '보합종목수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'lowjo', 'name': '하락종목수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'downjo', 'name': '하한종목수', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1514': {
        'tr_cd': 't1514',
        'title': '업종기간별추이',
        'blocks': {
            't1514OutBlock': {
                'fields': [{'key': 'cts_date', 'name': 'CTS_일자', 'type': 'string', 'length': 8, 'desc': '연속조회키값(다음데이타가 있을 경우에 한해서 세팅 됨) 이 필드의 데이터를 다음 조회시 InBlock의 date 필드에 넣어준다.', 'required': True}],
                'type': 'single'
            },
            't1514OutBlock1': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'jisu', 'name': '지수', 'type': 'float', 'length': 12.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'diff_vol', 'name': '거래증가율', 'type': 'float', 'length': 12.2, 'required': True}, {'key': 'value1', 'name': '거래대금1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'high', 'name': '상승', 'type': 'float', 'length': 4, 'required': True}, {'key': 'unchg', 'name': '보합', 'type': 'float', 'length': 4, 'required': True}, {'key': 'low', 'name': '하락', 'type': 'float', 'length': 4, 'required': True}, {'key': 'uprate', 'name': '상승종목비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'frgsvolume', 'name': '외인순매수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'openjisu', 'name': '시가', 'type': 'float', 'length': 12.2, 'required': True}, {'key': 'highjisu', 'name': '고가', 'type': 'float', 'length': 12.2, 'required': True}, {'key': 'lowjisu', 'name': '저가', 'type': 'float', 'length': 12.2, 'required': True}, {'key': 'value2', 'name': '거래대금2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'up', 'name': '상한', 'type': 'float', 'length': 4, 'required': True}, {'key': 'down', 'name': '하한', 'type': 'float', 'length': 4, 'required': True}, {'key': 'totjo', 'name': '종목수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'orgsvolume', 'name': '기관순매수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'upcode', 'name': '업종코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'rate', 'name': '거래비중', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'divrate', 'name': '업종배당수익률', 'type': 'float', 'length': 7.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1516': {
        'tr_cd': 't1516',
        'title': '업종별종목시세',
        'blocks': {
            't1516OutBlock': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'pricejisu', 'name': '지수', 'type': 'float', 'length': 12.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jdiff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'single'
            },
            't1516OutBlock1': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sojinrate', 'name': '소진율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'beta', 'name': '베타계수', 'type': 'float', 'length': 6.5, 'required': True}, {'key': 'perx', 'name': 'PER', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'frgsvolume', 'name': '외인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'orgsvolume', 'name': '기관순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'diff_vol', 'name': '거래증가율', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'total', 'name': '시가총액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1531': {
        'tr_cd': 't1531',
        'title': '테마별종목',
        'blocks': {
            't1531OutBlock': {
                'fields': [{'key': 'tmname', 'name': '테마명', 'type': 'string', 'length': 36, 'required': True}, {'key': 'avgdiff', 'name': '평균등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'tmcode', 'name': '테마코드', 'type': 'string', 'length': 4, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1532': {
        'tr_cd': 't1532',
        'title': '종목별테마',
        'blocks': {
            't1532OutBlock': {
                'fields': [{'key': 'tmname', 'name': '테마명', 'type': 'string', 'length': 36, 'required': True}, {'key': 'avgdiff', 'name': '평균등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'tmcode', 'name': '테마코드', 'type': 'string', 'length': 4, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1533': {
        'tr_cd': 't1533',
        'title': '특이테마',
        'blocks': {
            't1533OutBlock': {
                'fields': [{'key': 'bdate', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            },
            't1533OutBlock1': {
                'fields': [{'key': 'tmname', 'name': '테마명', 'type': 'string', 'length': 36, 'required': True}, {'key': 'totcnt', 'name': '전체', 'type': 'float', 'length': 4, 'required': True}, {'key': 'upcnt', 'name': '상승', 'type': 'float', 'length': 4, 'required': True}, {'key': 'dncnt', 'name': '하락', 'type': 'float', 'length': 4, 'required': True}, {'key': 'uprate', 'name': '상승비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff_vol', 'name': '거래증가율', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'avgdiff', 'name': '평균등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'chgdiff', 'name': '대비등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'tmcode', 'name': '테마코드', 'type': 'string', 'length': 4, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1537': {
        'tr_cd': 't1537',
        'title': '테마종목별시세조회',
        'blocks': {
            't1537OutBlock': {
                'fields': [{'key': 'upcnt', 'name': '상승종목수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'tmcnt', 'name': '테마종목수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'uprate', 'name': '상승종목비율', 'type': 'float', 'length': 4, 'required': True}, {'key': 'tmname', 'name': '테마명', 'type': 'string', 'length': 36, 'required': True}],
                'type': 'single'
            },
            't1537OutBlock1': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jniltime', 'name': '전일동시간', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'yeprice', 'name': '예상체결가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'value', 'name': '누적거래대금(단위:백만)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'marketcap', 'name': '시가총액(단위:백만)', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1601': {
        'tr_cd': 't1601',
        'title': '투자자별종합',
        'blocks': {
            't1601OutBlock1': {
                'fields': [{'key': 'tjjcode_08', 'name': '개인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_08', 'name': '개인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_08', 'name': '개인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_08', 'name': '개인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_08', 'name': '개인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_17', 'name': '외국인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_17', 'name': '외국인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_17', 'name': '외국인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_17', 'name': '외국인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_17', 'name': '외국인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_18', 'name': '기관계투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_18', 'name': '기관계매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_18', 'name': '기관계매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_18', 'name': '기관계증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_18', 'name': '기관계순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_01', 'name': '증권투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_01', 'name': '증권매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_01', 'name': '증권매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_01', 'name': '증권증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_01', 'name': '증권순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_03', 'name': '투신투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_03', 'name': '투신매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_03', 'name': '투신매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_03', 'name': '투신증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_03', 'name': '투신순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_04', 'name': '은행투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_04', 'name': '은행매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_04', 'name': '은행매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_04', 'name': '은행증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_04', 'name': '은행순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_02', 'name': '보험투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_02', 'name': '보험매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_02', 'name': '보험매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_02', 'name': '보험증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_02', 'name': '보험순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_05', 'name': '종금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_05', 'name': '종금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_05', 'name': '종금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_05', 'name': '종금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_05', 'name': '종금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_06', 'name': '기금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_06', 'name': '기금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_06', 'name': '기금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_06', 'name': '기금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_06', 'name': '기금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_11', 'name': '국가투자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_11', 'name': '국가매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_11', 'name': '국가매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_11', 'name': '국가증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_11', 'name': '국가순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_07', 'name': '기타투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_07', 'name': '기타매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_07', 'name': '기타매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_07', 'name': '기타증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_07', 'name': '기타순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_00', 'name': '사모펀드투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_00', 'name': '사모펀드매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_00', 'name': '사모펀드매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_00', 'name': '사모펀드증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_00', 'name': '사모펀드순매수', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'single'
            },
            't1601OutBlock2': {
                'fields': [{'key': 'tjjcode_08', 'name': '개인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_08', 'name': '개인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_08', 'name': '개인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_08', 'name': '개인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_08', 'name': '개인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_17', 'name': '외국인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_17', 'name': '외국인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_17', 'name': '외국인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_17', 'name': '외국인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_17', 'name': '외국인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_18', 'name': '기관계투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_18', 'name': '기관계매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_18', 'name': '기관계매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_18', 'name': '기관계증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_18', 'name': '기관계순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_01', 'name': '증권투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_01', 'name': '증권매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_01', 'name': '증권매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_01', 'name': '증권증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_01', 'name': '증권순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_03', 'name': '투신투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_03', 'name': '투신매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_03', 'name': '투신매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_03', 'name': '투신증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_03', 'name': '투신순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_04', 'name': '은행투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_04', 'name': '은행매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_04', 'name': '은행매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_04', 'name': '은행증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_04', 'name': '은행순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_02', 'name': '보험투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_02', 'name': '보험매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_02', 'name': '보험매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_02', 'name': '보험증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_02', 'name': '보험순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_05', 'name': '종금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_05', 'name': '종금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_05', 'name': '종금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_05', 'name': '종금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_05', 'name': '종금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_06', 'name': '기금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_06', 'name': '기금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_06', 'name': '기금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_06', 'name': '기금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_06', 'name': '기금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_11', 'name': '국가투자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_11', 'name': '국가매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_11', 'name': '국가매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_11', 'name': '국가증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_11', 'name': '국가순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_07', 'name': '기타투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_07', 'name': '기타매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_07', 'name': '기타매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_07', 'name': '기타증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_07', 'name': '기타순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_00', 'name': '사모펀드투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_00', 'name': '사모펀드매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_00', 'name': '사모펀드매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_00', 'name': '사모펀드증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_00', 'name': '사모펀드순매수', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'single'
            },
            't1601OutBlock3': {
                'fields': [{'key': 'tjjcode_08', 'name': '개인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_08', 'name': '개인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_08', 'name': '개인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_08', 'name': '개인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_08', 'name': '개인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_17', 'name': '외국인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_17', 'name': '외국인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_17', 'name': '외국인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_17', 'name': '외국인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_17', 'name': '외국인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_18', 'name': '기관계투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_18', 'name': '기관계매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_18', 'name': '기관계매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_18', 'name': '기관계증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_18', 'name': '기관계순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_01', 'name': '증권투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_01', 'name': '증권매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_01', 'name': '증권매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_01', 'name': '증권증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_01', 'name': '증권순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_03', 'name': '투신투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_03', 'name': '투신매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_03', 'name': '투신매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_03', 'name': '투신증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_03', 'name': '투신순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_04', 'name': '은행투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_04', 'name': '은행매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_04', 'name': '은행매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_04', 'name': '은행증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_04', 'name': '은행순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_02', 'name': '보험투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_02', 'name': '보험매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_02', 'name': '보험매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_02', 'name': '보험증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_02', 'name': '보험순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_05', 'name': '종금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_05', 'name': '종금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_05', 'name': '종금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_05', 'name': '종금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_05', 'name': '종금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_06', 'name': '기금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_06', 'name': '기금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_06', 'name': '기금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_06', 'name': '기금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_06', 'name': '기금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_11', 'name': '국가투자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_11', 'name': '국가매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_11', 'name': '국가매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_11', 'name': '국가증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_11', 'name': '국가순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_07', 'name': '기타투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_07', 'name': '기타매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_07', 'name': '기타매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_07', 'name': '기타증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_07', 'name': '기타순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_00', 'name': '사모펀드투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_00', 'name': '사모펀드매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_00', 'name': '사모펀드매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_00', 'name': '사모펀드증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_00', 'name': '사모펀드순매수', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'single'
            },
            't1601OutBlock4': {
                'fields': [{'key': 'tjjcode_08', 'name': '개인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_08', 'name': '개인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_08', 'name': '개인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_08', 'name': '개인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_08', 'name': '개인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_17', 'name': '외국인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_17', 'name': '외국인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_17', 'name': '외국인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_17', 'name': '외국인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_17', 'name': '외국인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_18', 'name': '기관계투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_18', 'name': '기관계매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_18', 'name': '기관계매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_18', 'name': '기관계증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_18', 'name': '기관계순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_01', 'name': '증권투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_01', 'name': '증권매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_01', 'name': '증권매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_01', 'name': '증권증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_01', 'name': '증권순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_03', 'name': '투신투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_03', 'name': '투신매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_03', 'name': '투신매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_03', 'name': '투신증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_03', 'name': '투신순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_04', 'name': '은행투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_04', 'name': '은행매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_04', 'name': '은행매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_04', 'name': '은행증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_04', 'name': '은행순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_02', 'name': '보험투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_02', 'name': '보험매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_02', 'name': '보험매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_02', 'name': '보험증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_02', 'name': '보험순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_05', 'name': '종금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_05', 'name': '종금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_05', 'name': '종금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_05', 'name': '종금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_05', 'name': '종금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_06', 'name': '기금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_06', 'name': '기금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_06', 'name': '기금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_06', 'name': '기금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_06', 'name': '기금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_11', 'name': '국가투자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_11', 'name': '국가매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_11', 'name': '국가매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_11', 'name': '국가증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_11', 'name': '국가순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_07', 'name': '기타투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_07', 'name': '기타매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_07', 'name': '기타매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_07', 'name': '기타증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_07', 'name': '기타순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_00', 'name': '사모펀드투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_00', 'name': '사모펀드매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_00', 'name': '사모펀드매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_00', 'name': '사모펀드증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_00', 'name': '사모펀드순매수', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'single'
            },
            't1601OutBlock5': {
                'fields': [{'key': 'tjjcode_08', 'name': '개인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_08', 'name': '개인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_08', 'name': '개인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_08', 'name': '개인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_08', 'name': '개인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_17', 'name': '외국인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_17', 'name': '외국인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_17', 'name': '외국인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_17', 'name': '외국인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_17', 'name': '외국인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_18', 'name': '기관계투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_18', 'name': '기관계매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_18', 'name': '기관계매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_18', 'name': '기관계증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_18', 'name': '기관계순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_01', 'name': '증권투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_01', 'name': '증권매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_01', 'name': '증권매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_01', 'name': '증권증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_01', 'name': '증권순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_03', 'name': '투신투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_03', 'name': '투신매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_03', 'name': '투신매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_03', 'name': '투신증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_03', 'name': '투신순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_04', 'name': '은행투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_04', 'name': '은행매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_04', 'name': '은행매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_04', 'name': '은행증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_04', 'name': '은행순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_02', 'name': '보험투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_02', 'name': '보험매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_02', 'name': '보험매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_02', 'name': '보험증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_02', 'name': '보험순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_05', 'name': '종금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_05', 'name': '종금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_05', 'name': '종금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_05', 'name': '종금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_05', 'name': '종금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_06', 'name': '기금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_06', 'name': '기금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_06', 'name': '기금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_06', 'name': '기금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_06', 'name': '기금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_11', 'name': '국가투자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_11', 'name': '국가매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_11', 'name': '국가매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_11', 'name': '국가증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_11', 'name': '국가순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_07', 'name': '기타투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_07', 'name': '기타매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_07', 'name': '기타매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_07', 'name': '기타증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_07', 'name': '기타순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_00', 'name': '사모펀드투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_00', 'name': '사모펀드매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_00', 'name': '사모펀드매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_00', 'name': '사모펀드증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_00', 'name': '사모펀드순매수', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'single'
            },
            't1601OutBlock6': {
                'fields': [{'key': 'tjjcode_08', 'name': '개인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_08', 'name': '개인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_08', 'name': '개인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_08', 'name': '개인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_08', 'name': '개인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_17', 'name': '외국인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_17', 'name': '외국인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_17', 'name': '외국인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_17', 'name': '외국인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_17', 'name': '외국인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_18', 'name': '기관계투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_18', 'name': '기관계매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_18', 'name': '기관계매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_18', 'name': '기관계증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_18', 'name': '기관계순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_01', 'name': '증권투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_01', 'name': '증권매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_01', 'name': '증권매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_01', 'name': '증권증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_01', 'name': '증권순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_03', 'name': '투신투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_03', 'name': '투신매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_03', 'name': '투신매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_03', 'name': '투신증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_03', 'name': '투신순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_04', 'name': '은행투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_04', 'name': '은행매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_04', 'name': '은행매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_04', 'name': '은행증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_04', 'name': '은행순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_02', 'name': '보험투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_02', 'name': '보험매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_02', 'name': '보험매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_02', 'name': '보험증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_02', 'name': '보험순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_05', 'name': '종금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_05', 'name': '종금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_05', 'name': '종금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_05', 'name': '종금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_05', 'name': '종금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_06', 'name': '기금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_06', 'name': '기금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_06', 'name': '기금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_06', 'name': '기금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_06', 'name': '기금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_11', 'name': '국가투자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_11', 'name': '국가매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_11', 'name': '국가매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_11', 'name': '국가증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_11', 'name': '국가순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_07', 'name': '기타투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_07', 'name': '기타매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_07', 'name': '기타매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_07', 'name': '기타증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_07', 'name': '기타순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_00', 'name': '사모펀드투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_00', 'name': '사모펀드매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_00', 'name': '사모펀드매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_00', 'name': '사모펀드증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_00', 'name': '사모펀드순매수', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1602': {
        'tr_cd': 't1602',
        'title': '시간대별투자자매매추이',
        'blocks': {
            't1602OutBlock': {
                'fields': [{'key': 'cts_time', 'name': 'CTSTIME', 'type': 'string', 'length': 8, 'required': True}, {'key': 'tjjcode_08', 'name': '개인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_08', 'name': '개인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_08', 'name': '개인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_08', 'name': '개인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_08', 'name': '개인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_17', 'name': '외국인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_17', 'name': '외국인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_17', 'name': '외국인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_17', 'name': '외국인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_17', 'name': '외국인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_18', 'name': '기관계투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_18', 'name': '기관계매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_18', 'name': '기관계매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_18', 'name': '기관계증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_18', 'name': '기관계순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_01', 'name': '증권투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_01', 'name': '증권매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_01', 'name': '증권매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_01', 'name': '증권증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_01', 'name': '증권순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_03', 'name': '투신투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_03', 'name': '투신매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_03', 'name': '투신매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_03', 'name': '투신증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_03', 'name': '투신순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_04', 'name': '은행투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_04', 'name': '은행매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_04', 'name': '은행매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_04', 'name': '은행증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_04', 'name': '은행순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_02', 'name': '보험투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_02', 'name': '보험매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_02', 'name': '보험매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_02', 'name': '보험증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_02', 'name': '보험순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_05', 'name': '종금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_05', 'name': '종금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_05', 'name': '종금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_05', 'name': '종금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_05', 'name': '종금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_06', 'name': '기금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_06', 'name': '기금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_06', 'name': '기금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_06', 'name': '기금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_06', 'name': '기금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_07', 'name': '기타투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_07', 'name': '기타매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_07', 'name': '기타매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_07', 'name': '기타증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_07', 'name': '기타순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_11', 'name': '국가투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_11', 'name': '국가매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_11', 'name': '국가매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_11', 'name': '국가증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_11', 'name': '국가순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_00', 'name': '사모펀드코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_00', 'name': '사모펀드매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_00', 'name': '사모펀드매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_00', 'name': '사모펀드증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_00', 'name': '사모펀드순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ex_upcode', 'name': '거래소별업종코드', 'type': 'string', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1602OutBlock1': {
                'fields': [{'key': 'time', 'name': '시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'sv_08', 'name': '개인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_17', 'name': '외국인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_18', 'name': '기관계순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_01', 'name': '증권순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_03', 'name': '투신순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_04', 'name': '은행순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_02', 'name': '보험순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_05', 'name': '종금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_06', 'name': '기금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_07', 'name': '기타순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_11', 'name': '국가순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_00', 'name': '사모펀드순매수', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1603': {
        'tr_cd': 't1603',
        'title': '시간대별투자자매매추이상세',
        'blocks': {
            't1603OutBlock': {
                'fields': [{'key': 'cts_idx', 'name': 'CTSIDX', 'type': 'float', 'length': 4, 'required': True}, {'key': 'cts_time', 'name': 'CTSTIME', 'type': 'string', 'length': 8, 'required': True}, {'key': 'ex_upcode', 'name': '거래소별업종코드', 'type': 'string', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1603OutBlock1': {
                'fields': [{'key': 'time', 'name': '시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'tjjcode', 'name': '투자자구분', 'type': 'string', 'length': 4, 'required': True}, {'key': 'msvolume', 'name': '매수수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'mdvolume', 'name': '매도수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'msvalue', 'name': '매수금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdvalue', 'name': '매도금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume', 'name': '순매수수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'svalue', 'name': '순매수금액', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1615': {
        'tr_cd': 't1615',
        'title': '투자자매매종합1',
        'blocks': {
            't1615OutBlock': {
                'fields': [{'key': 'dwvolume', 'name': '위탁매도수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'dwvalue', 'name': '위탁매도금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'djvolume', 'name': '자기매도수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'djvalue', 'name': '자기매도금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sum_volume', 'name': '합계수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sum_value', 'name': '합계금액', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'single'
            },
            't1615OutBlock1': {
                'fields': [{'key': 'hname', 'name': '시장명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'sv_08', 'name': '개인', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_17', 'name': '외국인', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_18', 'name': '기관계', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_07', 'name': '증권', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1617': {
        'tr_cd': 't1617',
        'title': '투자자매매종합2',
        'blocks': {
            't1617OutBlock': {
                'fields': [{'key': 'cts_date', 'name': 'CTSDATE', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': 'CTSTIME', 'type': 'string', 'length': 8, 'required': True}, {'key': 'ms_08', 'name': '개인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_08', 'name': '개인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_08', 'name': '개인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ms_17', 'name': '외국인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_17', 'name': '외국인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_17', 'name': '외국인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ms_18', 'name': '기관계매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_18', 'name': '기관계매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_18', 'name': '기관계순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ms_01', 'name': '증권매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_01', 'name': '증권매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_01', 'name': '증권순매수', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'single'
            },
            't1617OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'sv_08', 'name': '개인', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_17', 'name': '외국인', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_18', 'name': '기관계', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_01', 'name': '증권', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1621': {
        'tr_cd': 't1621',
        'title': '업종별분별투자자매매동향(챠트용)',
        'blocks': {
            't1621OutBlock': {
                'fields': [{'key': 'indcode', 'name': '개인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'forcode', 'name': '외국인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'syscode', 'name': '기관계투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'stocode', 'name': '증권투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'invcode', 'name': '투신투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'bancode', 'name': '은행투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'inscode', 'name': '보험투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'fincode', 'name': '종금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'moncode', 'name': '기금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'etccode', 'name': '기타투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'natcode', 'name': '국가투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'pefcode', 'name': '사모펀드투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'jisucd', 'name': '기준지수코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'jisunm', 'name': '기준지수명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'ex_upcode', 'name': '거래소별업종코드', 'type': 'string', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1621OutBlock1': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'datetime', 'name': '일자시간', 'type': 'string', 'length': 14, 'required': True}, {'key': 'indmsvol', 'name': '개인순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'indmsamt', 'name': '개인순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'formsvol', 'name': '외국인순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'formsamt', 'name': '외국인순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sysmsvol', 'name': '기관계순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sysmsamt', 'name': '기관계순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'stomsvol', 'name': '증권순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'stomsamt', 'name': '증권순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'invmsvol', 'name': '투신순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'invmsamt', 'name': '투신순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'banmsvol', 'name': '은행순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'banmsamt', 'name': '은행순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'insmsvol', 'name': '보험순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'insmsamt', 'name': '보험순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'finmsvol', 'name': '종금순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'finmsamt', 'name': '종금순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'monmsvol', 'name': '기금순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'monmsamt', 'name': '기금순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'etcmsvol', 'name': '기타순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'etcmsamt', 'name': '기타순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'natmsvol', 'name': '국가순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'natmsamt', 'name': '국가순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'pefmsvol', 'name': '사모펀드순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'pefmsamt', 'name': '사모펀드순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'upclose', 'name': '기준지수', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'upcvolume', 'name': '기준체결거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'upvolume', 'name': '기준누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'upvalue', 'name': '기준거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1631': {
        'tr_cd': 't1631',
        'title': '프로그램매매종합조회',
        'blocks': {
            't1631OutBlock': {
                'fields': [{'key': 'cdhrem', 'name': '매도차익미체결잔량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bdhrem', 'name': '매도비차익미체결잔량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'tcdrem', 'name': '매도차익주문수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'tbdrem', 'name': '매도비차익주문수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'cshrem', 'name': '매수차익미체결잔량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bshrem', 'name': '매수비차익미체결잔량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'tcsrem', 'name': '매수차익주문수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'tbsrem', 'name': '매수비차익주문수량', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'single'
            },
            't1631OutBlock1': {
                'fields': [{'key': 'offervolume', 'name': '매도수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offervalue', 'name': '매도금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidvolume', 'name': '매수수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidvalue', 'name': '매수금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'volume', 'name': '순매수수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'value', 'name': '순매수금액', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1632': {
        'tr_cd': 't1632',
        'title': '시간대별프로그램매매추이',
        'blocks': {
            't1632OutBlock': {
                'fields': [{'key': 'date', 'name': '날짜CTS', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간CTS', 'type': 'string', 'length': 6, 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}, {'key': 'ex_gubun', 'name': '거래소별구분코드', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            't1632OutBlock1': {
                'fields': [{'key': 'time', 'name': '시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'k200jisu', 'name': 'KP200', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'k200basis', 'name': 'BASIS', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'tot3', 'name': '전체순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tot1', 'name': '전체매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tot2', 'name': '전체매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cha3', 'name': '차익순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cha1', 'name': '차익매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cha2', 'name': '차익매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bcha3', 'name': '비차익순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bcha1', 'name': '비차익매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bcha2', 'name': '비차익매도', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1633': {
        'tr_cd': 't1633',
        'title': '기간별프로그램매매추이',
        'blocks': {
            't1633OutBlock': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1633OutBlock1': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'jisu', 'name': 'KP200', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'tot3', 'name': '전체순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tot1', 'name': '전체매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tot2', 'name': '전체매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cha3', 'name': '차익순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cha1', 'name': '차익매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cha2', 'name': '차익매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bcha3', 'name': '비차익순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bcha1', 'name': '비차익매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bcha2', 'name': '비차익매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1636': {
        'tr_cd': 't1636',
        'title': '종목별프로그램매매동향',
        'blocks': {
            't1636OutBlock': {
                'fields': [{'key': 'cts_idx', 'name': 'IDXCTS', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1636OutBlock1': {
                'fields': [{'key': 'rank', 'name': '순위', 'type': 'float', 'length': 8, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svalue', 'name': '순매수금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offervalue', 'name': '매도금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'stksvalue', 'name': '매수금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume', 'name': '순매수수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offervolume', 'name': '매도수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'stksvolume', 'name': '매수수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sgta', 'name': '시가총액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'rate', 'name': '비중', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'ex_shcode', 'name': '거래소별단축코드', 'type': 'string', 'length': 10, 'required': True}, {'key': 'mkcap_cmpr_val', 'name': '시총대비순매수비중', 'type': 'float', 'length': 6.2, 'desc': '2026.01.08 16시 이후 적용예정', 'required': True}],
                'type': 'array'
            }
        }
    },
    't1637': {
        'tr_cd': 't1637',
        'title': '종목별프로그램매매추이',
        'blocks': {
            't1637OutBlock': {
                'fields': [{'key': 'cts_idx', 'name': 'IDXCTS', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1637OutBlock1': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svalue', 'name': '순매수금액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'offervalue', 'name': '매도금액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'stksvalue', 'name': '매수금액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'svolume', 'name': '순매수수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offervolume', 'name': '매도수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'stksvolume', 'name': '매수수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'ex_shcode', 'name': '거래소별단축코드', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1638': {
        'tr_cd': 't1638',
        'title': '종목별잔량/사전공시',
        'blocks': {
            't1638OutBlock': {
                'fields': [{'key': 'rank', 'name': '순위', 'type': 'float', 'length': 4, 'required': True}, {'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sigatotrt', 'name': '시총비중', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'obuyvol', 'name': '순매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'buyrem', 'name': '매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'psgvolume', 'name': '매수공시수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sellrem', 'name': '매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'pdgvolume', 'name': '매도공시수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sigatot', 'name': '시가총액', 'type': 'float', 'length': 20, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1640': {
        'tr_cd': 't1640',
        'title': '프로그램매매종합조회(미니)',
        'blocks': {
            't1640OutBlock': {
                'fields': [{'key': 'offervolume', 'name': '매도수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidvolume', 'name': '매수수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'volume', 'name': '순매수수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerdiff', 'name': '매도증감', 'type': 'float', 'length': 8, 'required': True}, {'key': 'biddiff', 'name': '매수증감', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sundiff', 'name': '순매수증감', 'type': 'float', 'length': 8, 'required': True}, {'key': 'basis', 'name': '베이시스', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offervalue', 'name': '매도금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidvalue', 'name': '매수금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '순매수금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offervaldiff', 'name': '매도금액증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidvaldiff', 'name': '매수금액증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sunvaldiff', 'name': '순매수증감', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1662': {
        'tr_cd': 't1662',
        'title': '시간대별프로그램매매추이(차트)',
        'blocks': {
            't1662OutBlock': {
                'fields': [{'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'k200jisu', 'name': 'KP200', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'k200basis', 'name': 'BASIS', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'tot3', 'name': '전체순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tot1', 'name': '전체매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tot2', 'name': '전체매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cha3', 'name': '차익순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cha1', 'name': '차익매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cha2', 'name': '차익매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bcha3', 'name': '비차익순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bcha1', 'name': '비차익매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bcha2', 'name': '비차익매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1664': {
        'tr_cd': 't1664',
        'title': '투자자매매종합(챠트)',
        'blocks': {
            't1664OutBlock1': {
                'fields': [{'key': 'dt', 'name': '일자시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'tjj01', 'name': '증권순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj02', 'name': '보험순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj03', 'name': '투신순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj04', 'name': '은행순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj05', 'name': '종금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj06', 'name': '기금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj07', 'name': '기타순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj08', 'name': '개인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj17', 'name': '외국인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj18', 'name': '기관순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cha', 'name': '차익순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bicha', 'name': '비차익순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'totcha', 'name': '종합순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'basis', 'name': '베이시스', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1665': {
        'tr_cd': 't1665',
        'title': '기간별투자자매매추이(차트)',
        'blocks': {
            't1665OutBlock': {
                'fields': [{'key': 'mcode', 'name': '시장코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'mname', 'name': '시장명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'ex_upcode', 'name': '거래소별업종코드', 'type': 'string', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1665OutBlock1': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'sv_08', 'name': '개인수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_17', 'name': '외인계수량(등록+미등록)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_18', 'name': '기관계수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_01', 'name': '증권수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_03', 'name': '투신수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_04', 'name': '은행수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_02', 'name': '보험수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_05', 'name': '종금수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_06', 'name': '기금수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_07', 'name': '기타수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_00', 'name': '사모펀드수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_09', 'name': '등록외국인수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_10', 'name': '미등록외국인수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_11', 'name': '국가수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_99', 'name': '기타계수량(기타+국가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_08', 'name': '개인금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_17', 'name': '외인계금액(등록+미등록)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_18', 'name': '기관계금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_01', 'name': '증권금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_03', 'name': '투신금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_04', 'name': '은행금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_02', 'name': '보험금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_05', 'name': '종금금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_06', 'name': '기금금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_07', 'name': '기타금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_00', 'name': '사모펀드금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_09', 'name': '등록외국인금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_10', 'name': '미등록외국인금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_11', 'name': '국가금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_99', 'name': '기타계금액(기타+국가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jisu', 'name': '시장지수', 'type': 'float', 'length': 7.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1702': {
        'tr_cd': 't1702',
        'title': '외인기관종목별동향',
        'blocks': {
            't1702OutBlock1': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0000', 'name': '사모펀드', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0001', 'name': '증권', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0002', 'name': '보험', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0003', 'name': '투신', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0004', 'name': '은행', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0005', 'name': '종금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0006', 'name': '기금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0007', 'name': '기타법인', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0008', 'name': '개인', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0009', 'name': '등록외국인', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0010', 'name': '미등록외국인', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0011', 'name': '국가외', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0018', 'name': '기관', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0016', 'name': '외인계(등록+미등록)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'amt0017', 'name': '기타계(기타+국가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1716': {
        'tr_cd': 't1716',
        'title': '외인기관종목별동향',
        'blocks': {
            't1716OutBlock': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'krx_0008', 'name': '거래소_개인', 'type': 'float', 'length': 12, 'required': True}, {'key': 'krx_0018', 'name': '거래소_기관', 'type': 'float', 'length': 12, 'required': True}, {'key': 'krx_0009', 'name': '거래소_외국인', 'type': 'float', 'length': 12, 'required': True}, {'key': 'pgmvol', 'name': '프로그램', 'type': 'float', 'length': 12, 'required': True}, {'key': 'fsc_listing', 'name': '금감원_외인보유주식수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'fsc_sjrate', 'name': '금감원_소진율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'fsc_0009', 'name': '금감원_외국인', 'type': 'float', 'length': 12, 'required': True}, {'key': 'gm_volume', 'name': '공매도수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'gm_value', 'name': '공매도대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1717': {
        'tr_cd': 't1717',
        'title': '외인기관종목별동향',
        'blocks': {
            't1717OutBlock': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0000_vol', 'name': '사모펀드(순매수량)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0001_vol', 'name': '증권(순매수량)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0002_vol', 'name': '보험(순매수량)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0003_vol', 'name': '투신(순매수량)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0004_vol', 'name': '은행(순매수량)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0005_vol', 'name': '종금(순매수량)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0006_vol', 'name': '기금(순매수량)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0007_vol', 'name': '기타법인(순매수량)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0008_vol', 'name': '개인(순매수량)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0009_vol', 'name': '등록외국인(순매수량)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0010_vol', 'name': '미등록외국인(순매수량)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0011_vol', 'name': '국가외(순매수량)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0018_vol', 'name': '기관(순매수량)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0016_vol', 'name': '외인계(순매수량)(등록+미등록)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0017_vol', 'name': '기타계(순매수량)(기타+국가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0000_dan', 'name': '사모펀드(단가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0001_dan', 'name': '증권(단가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0002_dan', 'name': '보험(단가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0003_dan', 'name': '투신(단가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0004_dan', 'name': '은행(단가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0005_dan', 'name': '종금(단가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0006_dan', 'name': '기금(단가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0007_dan', 'name': '기타법인(단가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0008_dan', 'name': '개인(단가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0009_dan', 'name': '등록외국인(단가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0010_dan', 'name': '미등록외국인(단가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0011_dan', 'name': '국가외(단가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0018_dan', 'name': '기관(단가)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0016_dan', 'name': '외인계(단가)(등록+미등록)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tjj0017_dan', 'name': '기타계(단가)(기타+국가)', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1752': {
        'tr_cd': 't1752',
        'title': '종목별상위회원사',
        'blocks': {
            't1752OutBlock': {
                'fields': [{'key': 'fwdvl', 'name': '외국계매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'fwsvl', 'name': '외국계매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cts_idx', 'name': 'CTSIDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1752OutBlock1': {
                'fields': [{'key': 'tradname', 'name': '회원사', 'type': 'string', 'length': 20, 'required': True}, {'key': 'tradmdvol', 'name': '매도수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tradmsvol', 'name': '매수수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tradmssvol', 'name': '순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'wintrd', 'name': '창구거래', 'type': 'float', 'length': 12, 'required': True}, {'key': 'winrat', 'name': '비중', 'type': 'float', 'length': 6.1, 'required': True}, {'key': 'tradno', 'name': '회원사코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'wgubun', 'name': '외국계여부', 'type': 'string', 'length': 1, 'required': True}, {'key': 'swinrat', 'name': '순비중', 'type': 'float', 'length': 6.1, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1764': {
        'tr_cd': 't1764',
        'title': '회원사리스트',
        'blocks': {
            't1764OutBlock': {
                'fields': [{'key': 'rank', 'name': '순위', 'type': 'float', 'length': 4, 'required': True}, {'key': 'tradno', 'name': '거래원번호', 'type': 'string', 'length': 3, 'required': True}, {'key': 'tradname', 'name': '거래원이름', 'type': 'string', 'length': 20, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1771': {
        'tr_cd': 't1771',
        'title': '종목별회원사추이',
        'blocks': {
            't1771OutBlock': {
                'fields': [{'key': 'cts_idx', 'name': 'CTSIDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1771OutBlock2': {
                'fields': [{'key': 'traddate', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'tradtime', 'name': '시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tradmdcha', 'name': '매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tradmscha', 'name': '매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tradmdval', 'name': '매도대금', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tradmsval', 'name': '매수대금', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tradmsscha', 'name': '순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tradmttvolume', 'name': '누적순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tradavg', 'name': '평균단가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'tradmttavg', 'name': '누적평균단가', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1809': {
        'tr_cd': 't1809',
        'title': '신호조회',
        'blocks': {
            't1809OutBlock': {
                'fields': [{'key': 'cts', 'name': 'NEXTKEY', 'type': 'string', 'length': 30, 'required': True}],
                'type': 'single'
            },
            't1809OutBlock1': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'signal_id', 'name': '신호ID', 'type': 'string', 'length': 4, 'required': True}, {'key': 'signal_desc', 'name': '신호명', 'type': 'string', 'length': 300, 'required': True}, {'key': 'point', 'name': '신호강도', 'type': 'string', 'length': 3, 'required': True}, {'key': 'keyword', 'name': '뉴스신호키워드', 'type': 'string', 'length': 40, 'required': True}, {'key': 'seq', 'name': '신호별구분', 'type': 'string', 'length': 24, 'required': True}, {'key': 'gubun', 'name': '신호구분', 'type': 'string', 'length': 2, 'required': True}, {'key': 'jmcode', 'name': '신호종목', 'type': 'string', 'length': 6, 'required': True}, {'key': 'price', 'name': '종목가격', 'type': 'float', 'length': 7, 'required': True}, {'key': 'sign', 'name': '종목등락부호', 'type': 'string', 'length': 1, 'required': True}, {'key': 'chgrate', 'name': '대비등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'datetime', 'name': '신호일시', 'type': 'string', 'length': 16, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1825': {
        'tr_cd': 't1825',
        'title': '종목Q클릭검색(씽큐스마트)',
        'blocks': {
            't1825OutBlock': {
                'fields': [{'key': 'JongCnt', 'name': '검색종목수', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1825OutBlock1': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'signcnt', 'name': '연속봉수', 'type': 'float', 'length': 3, 'required': True}, {'key': 'close', 'name': '현재가', 'type': 'float', 'length': 9, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 9, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'volumerate', 'name': '거래량전일대비율', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1826': {
        'tr_cd': 't1826',
        'title': '종목Q클릭검색리스트조회(씽큐스마트)',
        'blocks': {
            't1826OutBlock': {
                'fields': [{'key': 'search_cd', 'name': '검색코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'search_nm', 'name': '검색명', 'type': 'string', 'length': 40, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1852': {
        'tr_cd': 't1852',
        'title': '파일저장종목 실시간검색',
        'blocks': {
            't1852OutBlock': {
                'fields': [{'key': 'sysfalg', 'name': '전략구분', 'type': 'string', 'length': 1, 'desc': 'S:시스템<br/>U:사용자', 'required': True}, {'key': 'flag', 'name': '등록구분', 'type': 'string', 'length': 1, 'desc': 'E:등록<br/>D:삭제<br/>M:시간상관', 'required': True}, {'key': 'sresultflag', 'name': '결과값', 'type': 'string', 'length': 1, 'desc': 'S : 정상<br/>F : 등록불가<br/>E : 오류', 'required': True}, {'key': 'time', 'name': '등록시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'alertnum', 'name': '신호번호', 'type': 'string', 'length': 11, 'desc': '실시간 키', 'required': True}, {'key': 'errmsg', 'name': '메시지', 'type': 'string', 'length': 40, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1856': {
        'tr_cd': 't1856',
        'title': '파일저장종목검색',
        'blocks': {
            't1856OutBlock': {
                'fields': [{'key': 'sCallGubun', 'name': '콜구분', 'type': 'string', 'length': 4, 'required': True}, {'key': 'OutFieldCount', 'name': 'OutFieldCount', 'type': 'float', 'length': 2, 'required': True}, {'key': 'sOutListPacketSize', 'name': '한종목크기', 'type': 'float', 'length': 4, 'required': True}, {'key': 'sFindTime', 'name': '현재시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'sTotalJongCnt', 'name': '결과종목수', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1856OutBlock1': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 7, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 9, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 9, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'JobFlag', 'name': '종목상태', 'type': 'string', 'length': 1, 'desc': 'N: 진입<br/>R: 재진입<br/>0: 이탈', 'required': True}],
                'type': 'single'
            }
        }
    },
    't1859 ': {
        'tr_cd': 't1859 ',
        'title': '서버저장조건 조건검색',
        'blocks': {
            't1859OutBlock': {
                'fields': [{'key': 'result_count', 'name': '검색종목수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'result_time', 'name': '포착시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'text', 'name': '전략설명', 'type': 'string', 'length': 200, 'required': True}],
                'type': 'single'
            },
            't1859OutBlock1': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 7, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 9, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 9, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1860': {
        'tr_cd': 't1860',
        'title': '서버저장조건 실시간검색',
        'blocks': {
            't1860OutBlock': {
                'fields': [{'key': 'sSysUserFlag', 'name': '사용자구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'sFlag', 'name': 'Flag', 'type': 'string', 'length': 1, 'required': True}, {'key': 'sResultFlag', 'name': '결과플레그', 'type': 'string', 'length': 1, 'desc': "'S':성공, 그 외 실패", 'required': True}, {'key': 'sTime', 'name': '현재시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'sAlertNum', 'name': '실시간키', 'type': 'string', 'length': 11, 'desc': "t1860InBlock의 Flag가 'E:'등록, 일때 수신<br/>'AFR(사용자조건검색실시간)' TR의  'gsRealKey'  입력값 =  sAlertNum 을 입력하면  조건검색 결과를 실시간으로 수신받을 수 있음", 'required': True}, {'key': 'Msg', 'name': '메세지', 'type': 'string', 'length': 40, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1866': {
        'tr_cd': 't1866',
        'title': '서버저장조건 리스트조회',
        'blocks': {
            't1866OutBlock': {
                'fields': [{'key': 'result_count', 'name': '저장조건수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'cont', 'name': '연속여부', 'type': 'string', 'length': 1, 'required': True}, {'key': 'cont_key', 'name': '연속키', 'type': 'string', 'length': 40, 'required': True}],
                'type': 'single'
            },
            't1866OutBlock1': {
                'fields': [{'key': 'query_index', 'name': '서버저장인덱스', 'type': 'string', 'length': 12, 'required': True}, {'key': 'group_name', 'name': '그룹명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'query_name', 'name': '조건저장명', 'type': 'string', 'length': 40, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1921': {
        'tr_cd': 't1921',
        'title': '신용거래동향',
        'blocks': {
            't1921OutBlock': {
                'fields': [{'key': 'cnt', 'name': 'CNT', 'type': 'float', 'length': 4, 'required': True}, {'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1921OutBlock1': {
                'fields': [{'key': 'mmdate', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'jchange', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'nvolume', 'name': '신규', 'type': 'float', 'length': 8, 'required': True}, {'key': 'svolume', 'name': '상환', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jvolume', 'name': '잔고', 'type': 'float', 'length': 8, 'required': True}, {'key': 'price', 'name': '금액', 'type': 'float', 'length': 8, 'required': True}, {'key': 'change', 'name': '대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'gyrate', 'name': '공여율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jkrate', 'name': '잔고율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1926': {
        'tr_cd': 't1926',
        'title': '종목별신용정보',
        'blocks': {
            't1926OutBlock': {
                'fields': [{'key': 'ynvolume', 'name': '융자신규수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ysvolume', 'name': '융자상환수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'yjvolume', 'name': '융자잔고수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'yvchange', 'name': '융자수량대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ygrate', 'name': '융자공여율', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'yjrate', 'name': '융자잔고율', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'ynprice', 'name': '융자신규금액', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ysprice', 'name': '융자상환금액', 'type': 'float', 'length': 8, 'required': True}, {'key': 'yjprice', 'name': '융자잔고금액', 'type': 'float', 'length': 8, 'required': True}, {'key': 'yachange', 'name': '융자금액대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dnvolume', 'name': '대주신규수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dsvolume', 'name': '대주상환수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'djvolume', 'name': '대주잔고수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dvchange', 'name': '대주수량대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dgrate', 'name': '대주공여율', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'djrate', 'name': '대주잔고율', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'dnprice', 'name': '대주신규금액', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dsprice', 'name': '대주상환금액', 'type': 'float', 'length': 8, 'required': True}, {'key': 'djprice', 'name': '대주잔고금액', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dachange', 'name': '대주금액대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'mmdate', 'name': '결제일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'close', 'name': '결제일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'volume', 'name': '결제일거래량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'value', 'name': '결제일거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'pr5days', 'name': '주가5일증가율', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'pr20days', 'name': '주가20일증가율', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'yj5days', 'name': '융자5일증가율', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'yj20days', 'name': '융자20일증가율', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'dj5days', 'name': '대주5일증가율', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'dj20days', 'name': '대주20일증가율', 'type': 'float', 'length': 9.2, 'required': True}],
                'type': 'single'
            }
        }
    },
    't1927': {
        'tr_cd': 't1927',
        'title': '공매도일별추이',
        'blocks': {
            't1927OutBlock': {
                'fields': [{'key': 'date', 'name': '일자CTS', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            },
            't1927OutBlock1': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'gm_vo', 'name': '공매도수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'gm_va', 'name': '공매도대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'gm_per', 'name': '공매도거래비중', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gm_avg', 'name': '평균공매도단가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'gm_vo_sum', 'name': '누적공매도수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'gm_vo1', 'name': '업틱룰적용공매도수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'gm_va1', 'name': '업틱룰적용공매도대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'gm_vo2', 'name': '업틱룰예외공매도수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'gm_va2', 'name': '업틱룰예외공매도대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1941': {
        'tr_cd': 't1941',
        'title': '종목별대차거래일간추이',
        'blocks': {
            't1941OutBlock1': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'price', 'name': '종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'upvolume', 'name': '당일체결', 'type': 'float', 'length': 12, 'required': True}, {'key': 'dnvolume', 'name': '당일상환', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tovolume', 'name': '당일잔고', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tovalue', 'name': '잔고금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'tovoldif', 'name': '대차증감', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1959': {
        'tr_cd': 't1959',
        'title': 'LP대상종목정보조회',
        'blocks': {
            't1959OutBlock1': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'string', 'length': 12, 'required': True}, {'key': 'sign', 'name': '부호', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '대비', 'type': 'string', 'length': 12, 'required': True}, {'key': 'rate', 'name': '등락율', 'type': 'float', 'length': 5.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'string', 'length': 12, 'required': True}, {'key': 'value', 'name': '누적거래대금', 'type': 'string', 'length': 12, 'required': True}, {'key': 'lp_gb', 'name': 'LP주문가능여부', 'type': 'string', 'length': 4, 'required': True}, {'key': 'lp_mem_nm1', 'name': 'LP회원사명1', 'type': 'string', 'length': 20, 'required': True}, {'key': 'lp_mem_nm2', 'name': 'LP회원사명2', 'type': 'string', 'length': 20, 'required': True}, {'key': 'lp_mem_nm3', 'name': 'LP회원사명3', 'type': 'string', 'length': 20, 'required': True}, {'key': 'lp_mem_nm4', 'name': 'LP회원사명4', 'type': 'string', 'length': 20, 'required': True}, {'key': 'lp_mem_nm5', 'name': 'LP회원사명5', 'type': 'string', 'length': 20, 'required': True}, {'key': 'lp_min_qty', 'name': 'LP최소호가수량', 'type': 'string', 'length': 10, 'required': True}, {'key': 'lp_st_date', 'name': 'LP시작일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'lp_end_date', 'name': 'LP종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'lp_spread', 'name': 'LP스프레드', 'type': 'float', 'length': 5.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't1988': {
        'tr_cd': 't1988',
        'title': '기초자산리스트조회',
        'blocks': {
            't1988OutBlock': {
                'fields': [{'key': 'ksp_cnt', 'name': '코스피종목건수', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ksd_cnt', 'name': '코스닥종목건수', 'type': 'string', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't1988OutBlock1': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'expcode', 'name': '표준코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'string', 'length': 12, 'required': True}, {'key': 'sign', 'name': '부호', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '대비', 'type': 'string', 'length': 12, 'required': True}, {'key': 'rate', 'name': '등락율', 'type': 'float', 'length': 5.2, 'required': True}, {'key': 'volume', 'name': '누적거래량(주)', 'type': 'string', 'length': 12, 'required': True}, {'key': 'value', 'name': '누적거래대금(백만)', 'type': 'string', 'length': 12, 'required': True}, {'key': 'mkt_gb', 'name': '시장구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'jvolume', 'name': '전일동시간대거래량(주)', 'type': 'string', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't2203': {
        'tr_cd': 't2203',
        'title': '기간별주가',
        'blocks': {
            't2203OutBlock': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'desc': '연속조회키 연속 조회시 이 값을 InBlock의 date 필드에 넣어준다.', 'required': True}, {'key': 'cts_code', 'name': 'CTS종목코드', 'type': 'string', 'length': 8, 'desc': '연속조회키 연속 조회시 이 값을 InBlock의 cts_code 필드에 넣어준다.', 'required': True}, {'key': 'lastdate', 'name': '전종목만기일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'nowfutyn', 'name': '최근월선물여부', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            },
            't2203OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'diff_vol', 'name': '거래증가율', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'openyak', 'name': '미결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'openyakupdn', 'name': '미결증감', 'type': 'float', 'length': 8, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't2421': {
        'tr_cd': 't2421',
        'title': '미결제약정추이',
        'blocks': {
            't2421OutBlock': {
                'fields': [{'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 15, 'required': True}, {'key': 'openyak', 'name': '미결제수량', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'single'
            },
            't2421OutBlock1': {
                'fields': [{'key': 'dt', 'name': '일자시간', 'type': 'string', 'length': 14, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'openopenyak', 'name': '미결제시량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'highopenyak', 'name': '미결제고량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'lowopenyak', 'name': '미결제저량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'closeopenyak', 'name': '미결제종량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'openupdn', 'name': '미결증감', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't3102': {
        'tr_cd': 't3102',
        'title': '뉴스본문',
        'blocks': {
            't3102OutBlock': {
                'fields': [{'key': 'sJongcode', 'name': '뉴스종목', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'array'
            },
            't3102OutBlock1': {
                'fields': [{'key': 'sBody', 'name': '뉴스본문', 'type': 'string', 'length': 100, 'required': True}],
                'type': 'array'
            },
            't3102OutBlock2': {
                'fields': [{'key': 'sTitle', 'name': '뉴스타이틀', 'type': 'string', 'length': 300, 'required': True}],
                'type': 'single'
            }
        }
    },
    't3202': {
        'tr_cd': 't3202',
        'title': '종목별증시일정',
        'blocks': {
            't3202OutBlock': {
                'fields': [{'key': 'recdt', 'name': '기준일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'tableid', 'name': '테이블아이디', 'type': 'string', 'length': 6, 'required': True}, {'key': 'upgu', 'name': '업무구분', 'type': 'string', 'length': 2, 'desc': '01:유상증자 02:무상증가 03:배당 04:감자 05:합병/분할 06:매수청구 07:실권주 08:액면교체 09:주주총회 10:상호변경 11:국내CB전환 12:해외CB전환 13:해외BW행사 14:스톡옵션행사', 'required': True}, {'key': 'custno', 'name': '발행체번호', 'type': 'string', 'length': 5, 'required': True}, {'key': 'custnm', 'name': '발행회사명', 'type': 'string', 'length': 80, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'upunm', 'name': '업무명', 'type': 'string', 'length': 20, 'required': True}],
                'type': 'array'
            }
        }
    },
    't3320': {
        'tr_cd': 't3320',
        'title': 'FNG_요약',
        'blocks': {
            't3320OutBlock': {
                'fields': [{'key': 'upgubunnm', 'name': '업종구분명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'sijangcd', 'name': '시장구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'marketnm', 'name': '시장구분명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'company', 'name': '한글기업명', 'type': 'string', 'length': 100, 'required': True}, {'key': 'baddress', 'name': '본사주소', 'type': 'string', 'length': 100, 'required': True}, {'key': 'btelno', 'name': '본사전화번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'gsyyyy', 'name': '최근결산년도', 'type': 'string', 'length': 4, 'required': True}, {'key': 'gsmm', 'name': '결산월', 'type': 'string', 'length': 2, 'required': True}, {'key': 'gsym', 'name': '최근결산년월', 'type': 'string', 'length': 6, 'required': True}, {'key': 'lstprice', 'name': '주당액면가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'gstock', 'name': '주식수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'homeurl', 'name': 'Homepage', 'type': 'string', 'length': 50, 'required': True}, {'key': 'grdnm', 'name': '그룹명', 'type': 'string', 'length': 30, 'required': True}, {'key': 'foreignratio', 'name': '외국인', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'irtel', 'name': '주담전화', 'type': 'string', 'length': 30, 'required': True}, {'key': 'capital', 'name': '자본금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sigavalue', 'name': '시가총액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cashsis', 'name': '배당금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cashrate', 'name': '배당수익율', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'notice1', 'name': '위험고지구분1_정리매매', 'type': 'string', 'length': 1, 'required': True}, {'key': 'notice2', 'name': '위험고지구분2_투자위험', 'type': 'string', 'length': 1, 'required': True}, {'key': 'notice3', 'name': '위험고지구분3_단기과열', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            },
            't3320OutBlock1': {
                'fields': [{'key': 'gicode', 'name': '기업코드', 'type': 'string', 'length': 7, 'required': True}, {'key': 'gsym', 'name': '결산년월', 'type': 'string', 'length': 6, 'required': True}, {'key': 'gsgb', 'name': '결산구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'per', 'name': 'PER', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'eps', 'name': 'EPS', 'type': 'float', 'length': 13, 'required': True}, {'key': 'pbr', 'name': 'PBR', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'roa', 'name': 'ROA', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'roe', 'name': 'ROE', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'ebitda', 'name': 'EBITDA', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'evebitda', 'name': 'EVEBITDA', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'par', 'name': '액면가', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'sps', 'name': 'SPS', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'cps', 'name': 'CPS', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'bps', 'name': 'BPS', 'type': 'float', 'length': 13, 'required': True}, {'key': 't_per', 'name': 'T.PER', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 't_eps', 'name': 'T.EPS', 'type': 'float', 'length': 13, 'required': True}, {'key': 'peg', 'name': 'PEG', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 't_peg', 'name': 'T.PEG', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 't_gsym', 'name': '최근분기년도', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            }
        }
    },
    't3341': {
        'tr_cd': 't3341',
        'title': '재무순위종합',
        'blocks': {
            't3341OutBlock': {
                'fields': [{'key': 'cnt', 'name': 'CNT', 'type': 'float', 'length': 4, 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't3341OutBlock1': {
                'fields': [{'key': 'rank', 'name': '순위', 'type': 'float', 'length': 4, 'required': True}, {'key': 'hname', 'name': '기업명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'salesgrowth', 'name': '매출액증가율', 'type': 'float', 'length': 12, 'required': True}, {'key': 'operatingincomegrowt', 'name': '영업이익증가율', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ordinaryincomegrowth', 'name': '경상이익증가율', 'type': 'float', 'length': 12, 'required': True}, {'key': 'liabilitytoequity', 'name': '부채비율', 'type': 'float', 'length': 12, 'required': True}, {'key': 'enterpriseratio', 'name': '유보율', 'type': 'float', 'length': 12, 'required': True}, {'key': 'eps', 'name': 'EPS', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bps', 'name': 'BPS', 'type': 'float', 'length': 12, 'required': True}, {'key': 'roe', 'name': 'ROE', 'type': 'float', 'length': 12, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'per', 'name': 'PER', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'pbr', 'name': 'PBR', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'peg', 'name': 'PEG', 'type': 'float', 'length': 13.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't3401': {
        'tr_cd': 't3401',
        'title': '투자의견',
        'blocks': {
            't3401OutBlock': {
                'fields': [{'key': 'cts_date', 'name': 'IDXDATE', 'type': 'string', 'length': 8, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '대비속성', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'single'
            },
            't3401OutBlock1': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 9, 'required': True}, {'key': 'tradno', 'name': '회원사코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'date', 'name': '의견일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'tradname', 'name': '회원사명', 'type': 'string', 'length': 30, 'required': True}, {'key': 'bopn', 'name': '투자의견변경후', 'type': 'string', 'length': 30, 'required': True}, {'key': 'nopn', 'name': '투자의견변경전', 'type': 'string', 'length': 30, 'required': True}, {'key': 'boga', 'name': '목표가변경전', 'type': 'float', 'length': 12, 'required': True}, {'key': 'noga', 'name': '목표가변경후', 'type': 'float', 'length': 12, 'required': True}, {'key': 'close', 'name': '의견일종가', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't4203': {
        'tr_cd': 't4203',
        'title': '업종차트(종합)',
        'blocks': {
            't4203OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jiclose', 'name': '전일종가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'disvalue', 'name': '당일거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'desc': '연속조회키<br/>연속 조회시 이 값을 InBlock의 cts_date 필드에 넣어준다.', 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 10, 'desc': '연속조회키<br/>연속 조회시 이 값을 InBlock의 cts_time 필드에 넣어준다.', 'required': True}, {'key': 'cts_daygb', 'name': '연속당일구분', 'type': 'string', 'length': 1, 'desc': '연속조회키<br/>연속 조회시 이 값을 InBlock의 cts_daygb 필드에 넣어준다.', 'required': True}],
                'type': 'single'
            },
            't4203OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jdiff_vol', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8407': {
        'tr_cd': 't8407',
        'title': 'API용주식멀티현재가조회',
        'blocks': {
            't8407OutBlock1': {
                'fields': [{'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho', 'name': '매도호가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho', 'name': '매수호가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'chdegree', 'name': '체결강도', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'value', 'name': '거래대금(백만)', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerrem', 'name': '우선매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem', 'name': '우선매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'totofferrem', 'name': '총매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'totbidrem', 'name': '총매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'uplmtprice', 'name': '상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dnlmtprice', 'name': '하한가', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8410': {
        'tr_cd': 't8410',
        'title': 'API전용주식차트(일주월년)',
        'blocks': {
            't8410OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jiclose', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'highend', 'name': '상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'lowend', 'name': '하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 's_time', 'name': '장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'e_time', 'name': '장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dshmin', 'name': '동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}, {'key': 'svi_uplmtprice', 'name': '정적VI상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'svi_dnlmtprice', 'name': '정적VI하한가', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'single'
            },
            't8410OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jdiff_vol', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jongchk', 'name': '수정구분', 'type': 'float', 'length': 13, 'required': True}, {'key': 'rate', 'name': '수정비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'pricechk', 'name': '수정주가반영항목', 'type': 'float', 'length': 13, 'required': True}, {'key': 'ratevalue', 'name': '수정비율반영거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sign', 'name': '종가등락구분(1:상한2:상승3:보합4:하한5:하락주식일만사용)', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8411': {
        'tr_cd': 't8411',
        'title': '주식차트(틱/n틱)',
        'blocks': {
            't8411OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jiclose', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'highend', 'name': '상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'lowend', 'name': '하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 's_time', 'name': '장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'e_time', 'name': '장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dshmin', 'name': '동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}],
                'type': 'single'
            },
            't8411OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jdiff_vol', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jongchk', 'name': '수정구분', 'type': 'float', 'length': 13, 'required': True}, {'key': 'rate', 'name': '수정비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'pricechk', 'name': '수정주가반영항목', 'type': 'float', 'length': 13, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8412': {
        'tr_cd': 't8412',
        'title': '주식차트(N분)',
        'blocks': {
            't8412OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jiclose', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'highend', 'name': '상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'lowend', 'name': '하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 's_time', 'name': '장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'e_time', 'name': '장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dshmin', 'name': '동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}],
                'type': 'single'
            },
            't8412OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jdiff_vol', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jongchk', 'name': '수정구분', 'type': 'float', 'length': 13, 'required': True}, {'key': 'rate', 'name': '수정비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '종가등락구분(1:상한2:상승3:보합4:하한5:하락)', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8417': {
        'tr_cd': 't8417',
        'title': '업종차트(틱/n틱)',
        'blocks': {
            't8417OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jiclose', 'name': '전일종가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 's_time', 'name': '장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'e_time', 'name': '장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dshmin', 'name': '동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}],
                'type': 'single'
            },
            't8417OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jdiff_vol', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8418': {
        'tr_cd': 't8418',
        'title': '업종차트(N분)',
        'blocks': {
            't8418OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jiclose', 'name': '전일종가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'disvalue', 'name': '당일거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 's_time', 'name': '업종시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'e_time', 'name': '업종종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dshmin', 'name': '동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}],
                'type': 'single'
            },
            't8418OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jdiff_vol', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8419': {
        'tr_cd': 't8419',
        'title': '업종차트(일주월)',
        'blocks': {
            't8419OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jiclose', 'name': '전일종가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'disvalue', 'name': '당일거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 's_time', 'name': '업종시작시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'e_time', 'name': '업종종료시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dshmin', 'name': '동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}],
                'type': 'single'
            },
            't8419OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'jdiff_vol', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8424': {
        'tr_cd': 't8424',
        'title': '전체업종',
        'blocks': {
            't8424OutBlock': {
                'fields': [{'key': 'hname', 'name': '업종명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'upcode', 'name': '업종코드', 'type': 'string', 'length': 3, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8425': {
        'tr_cd': 't8425',
        'title': '전체테마',
        'blocks': {
            't8425OutBlock': {
                'fields': [{'key': 'tmname', 'name': '테마명', 'type': 'string', 'length': 36, 'required': True}, {'key': 'tmcode', 'name': '테마코드', 'type': 'string', 'length': 4, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8427': {
        'tr_cd': 't8427',
        'title': '과거데이터시간대별조회',
        'blocks': {
            't8427OutBlock': {
                'fields': [{'key': 'focode', 'name': '선물옵션코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            },
            't8427OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'diff_vol', 'name': '거래증가율', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'openyak', 'name': '미결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'openyakupdn', 'name': '미결증감', 'type': 'float', 'length': 8, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8428': {
        'tr_cd': 't8428',
        'title': '증시주변자금추이',
        'blocks': {
            't8428OutBlock': {
                'fields': [{'key': 'date', 'name': '날짜CTS', 'type': 'string', 'length': 8, 'required': True}, {'key': 'idx', 'name': 'IDX', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't8428OutBlock1': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'jisu', 'name': '지수', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'sign', 'name': '대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'custmoney', 'name': '고객예탁금_억원', 'type': 'float', 'length': 12, 'required': True}, {'key': 'yecha', 'name': '예탁증감_억원', 'type': 'float', 'length': 12, 'required': True}, {'key': 'vol', 'name': '회전율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'outmoney', 'name': '미수금_억원', 'type': 'float', 'length': 12, 'required': True}, {'key': 'trjango', 'name': '신용잔고_억원', 'type': 'float', 'length': 12, 'required': True}, {'key': 'futymoney', 'name': '선물예수금_억원', 'type': 'float', 'length': 12, 'required': True}, {'key': 'stkmoney', 'name': '주식형_억원', 'type': 'float', 'length': 8, 'required': True}, {'key': 'mstkmoney', 'name': '혼합형_억원(주식)', 'type': 'float', 'length': 8, 'required': True}, {'key': 'mbndmoney', 'name': '혼합형_억원(채권)', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bndmoney', 'name': '채권형_억원', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bndsmoney', 'name': '필러(구.단기채권)', 'type': 'float', 'length': 8, 'required': True}, {'key': 'mmfmoney', 'name': 'MMF_억원(주식)', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8430': {
        'tr_cd': 't8430',
        'title': '주식종목조회',
        'blocks': {
            't8430OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'expcode', 'name': '확장코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'etfgubun', 'name': 'ETF구분(1:ETF)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'uplmtprice', 'name': '상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dnlmtprice', 'name': '하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jnilclose', 'name': '전일가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'memedan', 'name': '주문수량단위', 'type': 'string', 'length': 5, 'required': True}, {'key': 'recprice', 'name': '기준가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'gubun', 'name': '구분(1:코스피2:코스닥)', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8436': {
        'tr_cd': 't8436',
        'title': '주식종목조회 API용',
        'blocks': {
            't8436OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'expcode', 'name': '확장코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'etfgubun', 'name': 'ETF구분(1:ETF2:ETN)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'uplmtprice', 'name': '상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dnlmtprice', 'name': '하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jnilclose', 'name': '전일가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'memedan', 'name': '주문수량단위', 'type': 'string', 'length': 5, 'required': True}, {'key': 'recprice', 'name': '기준가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'gubun', 'name': '구분(1:코스피2:코스닥)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'bu12gubun', 'name': '증권그룹', 'type': 'string', 'length': 2, 'required': True}, {'key': 'spac_gubun', 'name': '기업인수목적회사여부(Y/N)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'filler', 'name': 'filler(미사용)', 'type': 'string', 'length': 32, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8450': {
        'tr_cd': 't8450',
        'title': '(통합)주식현재가호가조회2 API용',
        'blocks': {
            't8450OutBlock': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jnilclose', 'name': '전일종가(기준가)', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho1', 'name': '매도호가1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho1', 'name': '매수호가1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem1', 'name': '매도호가수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem1', 'name': '매수호가수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho2', 'name': '매도호가2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho2', 'name': '매수호가2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem2', 'name': '매도호가수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem2', 'name': '매수호가수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho3', 'name': '매도호가3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho3', 'name': '매수호가3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem3', 'name': '매도호가수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem3', 'name': '매수호가수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho4', 'name': '매도호가4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho4', 'name': '매수호가4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem4', 'name': '매도호가수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem4', 'name': '매수호가수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho5', 'name': '매도호가5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho5', 'name': '매수호가5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem5', 'name': '매도호가수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem5', 'name': '매수호가수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho6', 'name': '매도호가6', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho6', 'name': '매수호가6', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem6', 'name': '매도호가수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem6', 'name': '매수호가수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho7', 'name': '매도호가7', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho7', 'name': '매수호가7', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem7', 'name': '매도호가수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem7', 'name': '매수호가수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho8', 'name': '매도호가8', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho8', 'name': '매수호가8', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem8', 'name': '매도호가수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem8', 'name': '매수호가수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho9', 'name': '매도호가9', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho9', 'name': '매수호가9', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem9', 'name': '매도호가수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem9', 'name': '매수호가수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho10', 'name': '매도호가10', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho10', 'name': '매수호가10', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem10', 'name': '매도호가수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem10', 'name': '매수호가수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offer', 'name': '매도호가수량합', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bid', 'name': '매수호가수량합', 'type': 'float', 'length': 12, 'required': True}, {'key': 'hotime', 'name': '수신시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'yeprice', 'name': '예상체결가격', 'type': 'float', 'length': 8, 'required': True}, {'key': 'yevolume', 'name': '예상체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'yesign', 'name': '예상체결전일구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'yechange', 'name': '예상체결전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'yediff', 'name': '예상체결등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'tmoffer', 'name': '시간외매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'tmbid', 'name': '시간외매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ho_status', 'name': '동시구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'uplmtprice', 'name': '상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dnlmtprice', 'name': '하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'nxt_offerrem1', 'name': 'NXT매도호가수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_bidrem1', 'name': 'NXT매수호가수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_offerrem2', 'name': 'NXT매도호가수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_bidrem2', 'name': 'NXT매수호가수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_offerrem3', 'name': 'NXT매도호가수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_bidrem3', 'name': 'NXT매수호가수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_offerrem4', 'name': 'NXT매도호가수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_bidrem4', 'name': 'NXT매수호가수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_offerrem5', 'name': 'NXT매도호가수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_bidrem5', 'name': 'NXT매수호가수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_offerrem6', 'name': 'NXT매도호가수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_bidrem6', 'name': 'NXT매수호가수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_offerrem7', 'name': 'NXT매도호가수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_bidrem7', 'name': 'NXT매수호가수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_offerrem8', 'name': 'NXT매도호가수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_bidrem8', 'name': 'NXT매수호가수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_offerrem9', 'name': 'NXT매도호가수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_bidrem9', 'name': 'NXT매수호가수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_offerrem10', 'name': 'NXT매도호가수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_bidrem10', 'name': 'NXT매수호가수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_offer', 'name': 'NXT매도호가수량합', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_bid', 'name': 'NXT매수호가수량합', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_yeprice', 'name': 'NXT예상체결가격', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_yevolume', 'name': 'NXT예상체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'nxt_yesign', 'name': 'NXT예상체결전일구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'nxt_yechange', 'name': 'NXT예상체결전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'nxt_yediff', 'name': 'NXT예상체결등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'nxt_ho_status', 'name': 'NXT동시구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'unx_offerrem1', 'name': '통합매도호가수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_bidrem1', 'name': '통합매수호가수량1', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_offerrem2', 'name': '통합매도호가수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_bidrem2', 'name': '통합매수호가수량2', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_offerrem3', 'name': '통합매도호가수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_bidrem3', 'name': '통합매수호가수량3', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_offerrem4', 'name': '통합매도호가수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_bidrem4', 'name': '통합매수호가수량4', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_offerrem5', 'name': '통합매도호가수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_bidrem5', 'name': '통합매수호가수량5', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_offerrem6', 'name': '통합매도호가수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_bidrem6', 'name': '통합매수호가수량6', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_offerrem7', 'name': '통합매도호가수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_bidrem7', 'name': '통합매수호가수량7', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_offerrem8', 'name': '통합매도호가수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_bidrem8', 'name': '통합매수호가수량8', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_offerrem9', 'name': '통합매도호가수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_bidrem9', 'name': '통합매수호가수량9', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_offerrem10', 'name': '통합매도호가수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_bidrem10', 'name': '통합매수호가수량10', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_offer', 'name': '통합매도호가수량합', 'type': 'float', 'length': 12, 'required': True}, {'key': 'unx_bid', 'name': '통합매수호가수량합', 'type': 'float', 'length': 12, 'required': True}, {'key': 'krx_midprice', 'name': 'KRX중간가격', 'type': 'float', 'length': 8, 'required': True}, {'key': 'krx_offermidsumrem', 'name': 'KRX매도중간가잔량합계수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'krx_bidmidsumrem', 'name': 'KRX매수중간가잔량합계수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'nxt_midprice', 'name': 'NXT중간가격', 'type': 'float', 'length': 8, 'required': True}, {'key': 'nxt_offermidsumrem', 'name': 'NXT매도중간가잔량합계수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'nxt_bidmidsumrem', 'name': 'NXT매수중간가잔량합계수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'ex_shcode', 'name': '거래소별단축코드', 'type': 'string', 'length': 10, 'required': True}, {'key': 'krx_midsumrem', 'name': 'KRX중간가잔량합계수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'krx_midsumremgubun', 'name': "KRX중간가잔량구분(''없음'1'매도'2'매수)", 'type': 'string', 'length': 1, 'required': True}, {'key': 'nxt_midsumrem', 'name': 'NXT중간가잔량합계수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'nxt_midsumremgubun', 'name': "NXT중간가잔량구분(''없음'1'매도'2'매수)", 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8451': {
        'tr_cd': 't8451',
        'title': '(통합)주식챠트(일주월년) API용',
        'blocks': {
            't8451OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': None, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jiclose', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'highend', 'name': '상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'lowend', 'name': '하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 's_time', 'name': '장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'e_time', 'name': '장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dshmin', 'name': '동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}, {'key': 'svi_uplmtprice', 'name': '정적VI상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'svi_dnlmtprice', 'name': '정적VI하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'nxt_fm_s_time', 'name': 'NXT프리마켓장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'nxt_fm_e_time', 'name': 'NXT프리마켓장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'nxt_fm_dshmin', 'name': 'NXT프리마켓동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'nxt_am_s_time', 'name': 'NXT에프터마켓장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'nxt_am_e_time', 'name': 'NXT에프터마켓장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'nxt_am_dshmin', 'name': 'NXT에프터마켓동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            't8451OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jdiff_vol', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jongchk', 'name': '수정구분', 'type': 'float', 'length': 13, 'required': True}, {'key': 'rate', 'name': '수정비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'pricechk', 'name': '수정주가반영항목', 'type': 'float', 'length': 13, 'required': True}, {'key': 'ratevalue', 'name': '수정비율반영거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sign', 'name': '종가등락구분(1:상한2:상승3:보합4:하한5:하락주식일만사용)', 'type': 'string', 'length': 1, 'desc': '1:상한2:상승3:보합4:하한5:하락주식일만사용', 'required': True}],
                'type': 'array'
            }
        }
    },
    't8452': {
        'tr_cd': 't8452',
        'title': '(통합)주식챠트(N분) API용',
        'blocks': {
            't8452OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jiclosev', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'highend', 'name': '상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'lowend', 'name': '하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'float', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 's_time', 'name': '장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'e_time', 'name': '장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dshmin', 'name': '동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}, {'key': 'nxt_fm_s_time', 'name': 'NXT프리마켓장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'nxt_fm_e_time', 'name': 'NXT프리마켓장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'nxt_fm_dshmin', 'name': 'NXT프리마켓동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'nxt_am_s_time', 'name': 'NXT에프터마켓장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'nxt_am_e_time', 'name': 'NXT에프터마켓장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'nxt_am_dshmin', 'name': 'NXT에프터마켓동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            't8452OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jdiff_vol', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jongchk', 'name': '수정구분', 'type': 'float', 'length': 13, 'required': True}, {'key': 'rate', 'name': '수정비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '종가등락구분(1:상한2:상승3:보합4:하한5:하락)', 'type': 'string', 'length': 1, 'desc': '1:상한2:상승3:보합4:하한5:하락', 'required': True}],
                'type': 'array'
            }
        }
    },
    't8453': {
        'tr_cd': 't8453',
        'title': '(통합)주식챠트(틱/N틱) API용',
        'blocks': {
            't8453OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jicloseㅍ', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'highend', 'name': '상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'lowend', 'name': '하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 's_time', 'name': '장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'e_time', 'name': '장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dshmin', 'name': '동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}, {'key': 'nxt_fm_s_time', 'name': 'NXT프리마켓장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'nxt_fm_e_time', 'name': 'NXT프리마켓장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'nxt_fm_dshmin', 'name': 'NXT프리마켓동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'nxt_am_s_time', 'name': 'NXT에프터마켓장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'nxt_am_e_time', 'name': 'NXT에프터마켓장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'nxt_am_dshmin', 'name': 'NXT에프터마켓동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            't8453OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jdiff_vol', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jongchk', 'name': '수정구분', 'type': 'float', 'length': 13, 'required': True}, {'key': 'rate', 'name': '수정비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'pricechk', 'name': '수정주가반영항목', 'type': 'float', 'length': 13, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8454': {
        'tr_cd': 't8454',
        'title': '(통합)주식시간대별체결2 API용',
        'blocks': {
            't8454OutBlock': {
                'fields': [{'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 10, 'required': True}, {'key': 'ex_shcode', 'name': '거래소별단축코드', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'single'
            },
            't8454OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'chdegree', 'name': '체결강도', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdvolume', 'name': '매도체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdchecnt', 'name': '매도체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'msvolume', 'name': '매수체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mschecnt', 'name': '매수체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'revolume', 'name': '순체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rechecnt', 'name': '순체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'exchname', 'name': '거래소명', 'type': 'string', 'length': 3, 'required': True}],
                'type': 'array'
            }
        }
    },
    't9905': {
        'tr_cd': 't9905',
        'title': '기초자산리스트조회',
        'blocks': {
            't9905OutBlock1': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'expcode', 'name': '표준코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}],
                'type': 'array'
            }
        }
    },
    't9907': {
        'tr_cd': 't9907',
        'title': '만기월조회',
        'blocks': {
            't9907OutBlock1': {
                'fields': [{'key': 'lastym', 'name': '만기월', 'type': 'string', 'length': 6, 'required': True}, {'key': 'lastnm', 'name': '만기월명', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'array'
            }
        }
    },
    't9945': {
        'tr_cd': 't9945',
        'title': '주식마스터조회API용',
        'blocks': {
            't9945OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'expcode', 'name': '확장코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'etfchk', 'name': 'ETF구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'nxt_chk', 'name': 'NXT상장구분', 'type': 'string', 'length': 1, 'desc': '1:NXT 거래소 제공<br/>0:NXT 거래소 미제공', 'required': True}, {'key': 'filler', 'name': 'filler', 'type': 'string', 'length': 4, 'required': True}],
                'type': 'array'
            }
        }
    }
}
