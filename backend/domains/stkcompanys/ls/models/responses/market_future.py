# Auto-generated
from typing import Any, Dict, List

MARKET_FUTURE_RESPONSES = {
    'C01': {
        'tr_cd': 'C01',
        'title': '선물주문체결',
        'fields': [
            {
                'key': 'lineseq',
                'length': 10,
                'name': '라인일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'accno',
                'length': '	11',
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'user',
                'length': '	8',
                'name': '조작자ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'seq',
                'length': 11,
                'name': '일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'trcode',
                'length': '	11',
                'name': 'trcode',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'megrpno',
                'length': 2,
                'name': '매칭그룹번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'boardid',
                'length': 2,
                'name': '보드ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'memberno',
                'length': '	5',
                'name': '회원번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bpno',
                'length': '	5',
                'name': '지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordno',
                'length': '	10',
                'name': '주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordordno',
                'length': '	10',
                'name': '원주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'expcode',
                'length': '	12',
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'yakseq',
                'length': '	11',
                'name': '약정번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cheprice',
                'length': '	11.2',
                'name': '체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'chevol',
                'length': '	10',
                'name': '체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sessionid',
                'length': '	2',
                'name': '세션ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'chedate',
                'length': '	8',
                'name': '체결일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'chetime',
                'length': '	9',
                'name': '체결시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'spdprc1',
                'length': '	11.2',
                'name': '최근월체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'spdprc2',
                'length': '	11.2',
                'name': '차근월체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dosugb',
                'length': '	1',
                'name': '매도수구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'accno1',
                'length': '	12',
                'name': '계좌번호1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sihogagb',
                'length': '	1',
                'name': '시장조성호가구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jakino',
                'length': '	5',
                'name': '위탁사번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'daeyong',
                'length': '	12',
                'name': '대용주권계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mem_filler',
                'length': 7,
                'name': 'mem_filler',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mem_accno',
                'length': 11,
                'name': 'mem_accno',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mem_filler',
                'length': 42,
                'name': 'mem_filler1',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'C02': {
        'tr_cd': 'C02',
        'title': 'KRX야간파생 선물체결',
        'fields': [
            {
                'key': 'lineseq',
                'length': 10,
                'name': '라인일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'accno',
                'length': '	11',
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'user',
                'length': '	8',
                'name': '조작자ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'seq',
                'length': 11,
                'name': '일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'trcode',
                'length': '	11',
                'name': 'trcode',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'megrpno',
                'length': 2,
                'name': '매칭그룹번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'boardid',
                'length': 2,
                'name': '보드ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'memberno',
                'length': '	5',
                'name': '회원번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bpno',
                'length': '	5',
                'name': '지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordno',
                'length': '	10',
                'name': '주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordordno',
                'length': '	10',
                'name': '원주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'expcode',
                'length': '	12',
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'yakseq',
                'length': '	11',
                'name': '약정번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cheprice',
                'length': '	11.2',
                'name': '체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'chevol',
                'length': '	10',
                'name': '체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sessionid',
                'length': '	2',
                'name': '세션ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'chedate',
                'length': '	8',
                'name': '체결일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'chetime',
                'length': '	9',
                'name': '체결시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'spdprc1',
                'length': '	11.2',
                'name': '최근월체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'spdprc2',
                'length': '	11.2',
                'name': '차근월체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dosugb',
                'length': '	1',
                'name': '매도수구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'accno1',
                'length': '	12',
                'name': '계좌번호1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sihogagb',
                'length': '	1',
                'name': '시장조성호가구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jakino',
                'length': '	5',
                'name': '위탁사번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'daeyong',
                'length': '	12',
                'name': '대용주권계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mem_filler',
                'length': 7,
                'name': 'mem_filler',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mem_accno',
                'length': 11,
                'name': 'mem_accno',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mem_filler',
                'length': 42,
                'name': 'mem_filler1',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'CCENQ10100': {
        'tr_cd': 'CCENQ10100',
        'title': 'KRX야간파생 주문가능수량 조회',
        'blocks': {
            'CCENQ10100OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryTp', 'name': '조회구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OrdAmt', 'name': '주문금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'RatVal', 'name': '비율값', 'type': 'float', 'length': 19.8, 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'FnoOrdPrc', 'name': '선물옵션주문가격', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'FnoOrdprcPtnCode', 'name': '선물옵션호가유형코드', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            'CCENQ10100OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'QryDt', 'name': '조회일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FnoNowPrc', 'name': '선물옵션현재가', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'OrdAbleQty', 'name': '주문가능수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NewOrdAbleQty', 'name': '신규주문가능수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'LqdtOrdAbleQty', 'name': '청산주문가능수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'UsePreargMgn', 'name': '사용예정증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'UsePreargMnyMgn', 'name': '사용예정현금증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdAbleAmt', 'name': '주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdAbleAmt', 'name': '현금주문가능금액', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CCENQ30100': {
        'tr_cd': 'CCENQ30100',
        'title': 'KRX야간파생 주문/체결내역 조회',
        'blocks': {
            'CCENQ30100OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'InptPwd', 'name': '입력비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QrySrtDt', 'name': '조회시작일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryEndDt', 'name': '조회종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FnoClssCode', 'name': '선물옵션분류코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'PrdgrpCode', 'name': '상품군코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'PrdtExecTpCode', 'name': '체결구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'StnlnSeqTp', 'name': '정렬순서구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'MktTpCode', 'name': '시장구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'CommdaCode', 'name': '통신매체코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'FnoTrdPtnCode', 'name': '선물옵션거래유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'GrpId', 'name': '그룹ID', 'type': 'string', 'length': 20, 'required': True}, {'key': 'UserId', 'name': '사용자ID', 'type': 'string', 'length': 16, 'required': True}, {'key': 'SrtOrdNo2', 'name': '시작주문번호2', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'single'
            },
            'CCENQ30100OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'FutsOrdQty', 'name': '선물주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsExecQty', 'name': '선물체결수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptOrdQty', 'name': '옵션주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptExecQty', 'name': '옵션체결수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            },
            'CCENQ30100OutBlock3': {
                'fields': [{'key': 'OrdDt', 'name': '주문일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OrdNo', 'name': '주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'OrdTime', 'name': '주문시각', 'type': 'string', 'length': 9, 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'BnsTpNm', 'name': '매매구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'MrcTpNm', 'name': '정정취소구분명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'FnoOrdprcPtnCode', 'name': '선물옵션호가유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'FnoOrdprcPtnNm', 'name': '선물옵션호가유형명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'FnoOrdPrc', 'name': '선물옵션주문가격', 'type': 'float', 'length': 27, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdTpNm', 'name': '주문구분명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'ExecTpNm', 'name': '체결구분명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'FnoExecPrc', 'name': '선물옵션체결가', 'type': 'float', 'length': 27, 'required': True}, {'key': 'ExecQty', 'name': '체결수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CtrctTime', 'name': '약정시각', 'type': 'string', 'length': 9, 'required': True}, {'key': 'CtrctNo', 'name': '약정번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'ExecNo', 'name': '체결번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'BnsplAmt', 'name': '매매손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'UnercQty', 'name': '미체결수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'UserId', 'name': '사용자ID', 'type': 'string', 'length': 16, 'required': True}, {'key': 'MktClssCodeNm', 'name': '시장분류코드명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'CommdaCode', 'name': '통신매체코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'CommdaCodeNm', 'name': '통신매체코드명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'IpAddr', 'name': 'IP주소', 'type': 'string', 'length': 16, 'required': True}, {'key': 'TrdPtnTpNm', 'name': '거래유형구분', 'type': 'string', 'length': 20, 'required': True}, {'key': 'GrpId', 'name': '그룹ID', 'type': 'string', 'length': 20, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CCENQ90200': {
        'tr_cd': 'CCENQ90200',
        'title': 'KRX야간파생 잔고조회',
        'blocks': {
            'CCENQ90200OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'InptPwd', 'name': '입력비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'BalEvalTp', 'name': '잔고평가구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'FutsPrcEvalTp', 'name': '선물가격평가구분', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            },
            'CCENQ90200OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'string', 'length': 5, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'EvalDpsamtTotamt', 'name': '평가예탁금총액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'MnyEvalDpstgAmt', 'name': '현금평가예탁금액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'DpsamtTotamt', 'name': '예탁금총액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'DpstgMny', 'name': '예탁현금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'DpstgSubst', 'name': '예탁대용', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PsnOutAbleTotAmt', 'name': '인출가능총금액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'PsnOutAbleCurAmt', 'name': '인출가능현금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PsnOutAbleSubstAmt', 'name': '인출가능대용금액', 'type': 'float', 'length': 16}, {'key': 'OrdAbleTotAmt', 'name': '주문가능총금액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'MnyOrdAbleAmt', 'name': '현금주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CsgnMgnTotamt', 'name': '위탁증거금총액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyCsgnMgn', 'name': '현금위탁증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MtmgnTotamt', 'name': '유지증거금총액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'MnyMaintMgn', 'name': '현금유지증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'EvalAmtSum', 'name': '평가금액합계', 'type': 'float', 'length': 17, 'required': True}, {'key': 'RcvblOdpnt', 'name': '미수연체료', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AddMgnTotamt', 'name': '추가증거금총액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'EvalPnlSum', 'name': '평가손익합계', 'type': 'float', 'length': 15, 'required': True}, {'key': 'RcvblAmt', 'name': '미수금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyAddMgn', 'name': '현금추가증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsEvalPnlAmt', 'name': '선물평가손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptEvalPnlAmt', 'name': '옵션평가손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptEvalAmt', 'name': '옵션평가금액', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            },
            'CCENQ90200OutBlock3': {
                'fields': [{'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'BnsTpNm', 'name': '매매구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'UnsttQty', 'name': '미결제수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FnoAvrPrc', 'name': '평균가', 'type': 'float', 'length': 198, 'required': True}, {'key': 'FnoNowPrc', 'name': '선물옵션현재가', 'type': 'float', 'length': 278, 'required': True}, {'key': 'FnoCmpPrc', 'name': '선물옵션대비가', 'type': 'float', 'length': 278, 'required': True}, {'key': 'EvalPnl', 'name': '평가손익', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PnlRat', 'name': '손익율', 'type': 'float', 'length': 186, 'required': True}, {'key': 'FnoTrdUnitAmt', 'name': '선물옵션거래단위금액', 'type': 'float', 'length': 198, 'required': True}, {'key': 'EvalAmt', 'name': '평가금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'EvalRat', 'name': '평가비율', 'type': 'float', 'length': 72, 'required': True}, {'key': 'BnsplAmt', 'name': '매매손익금액', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CCENT00100': {
        'tr_cd': 'CCENT00100',
        'title': 'KRX야간파생 위탁 신규 주문',
        'blocks': {
            'CCENT00100OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdMktCode', 'name': '주문시장코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'FnoOrdPtnCode', 'name': '선물옵션주문유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'FnoOrdprcPtnCode', 'name': '선물옵션호가유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'FnoTrdPtnCode', 'name': '선물옵션거래유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'FnoOrdPrc', 'name': '선물옵션주문가격', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CommdaCode', 'name': '통신매체코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'DscusBnsCmpltTime', 'name': '협의매매완료시각', 'type': 'string', 'length': 9, 'required': True}, {'key': 'GrpId', 'name': '그룹ID', 'type': 'string', 'length': 20, 'required': True}, {'key': 'OrdSeqno', 'name': '주문일련번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'PtflNo', 'name': '포트폴리오번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'BskNo', 'name': '바스켓번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'TrchNo', 'name': '트렌치번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'ItemNo', 'name': '항목번호', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OpDrtnNo', 'name': '운용지시번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'MgempNo', 'name': '관리사원번호', 'type': 'string', 'length': 9, 'required': True}, {'key': 'FundId', 'name': '펀드ID', 'type': 'string', 'length': 12, 'required': True}, {'key': 'FundOrdNo', 'name': '펀드주문번호', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'single'
            },
            'CCENT00100OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdNo', 'name': '주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'BrnNm', 'name': '지점명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'OrdAbleAmt', 'name': '주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdAbleAmt', 'name': '현금주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdMgn', 'name': '주문증거금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdMgn', 'name': '현금주문증거금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdAbleQty', 'name': '주문가능수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CCENT00200': {
        'tr_cd': 'CCENT00200',
        'title': 'KRX야간파생 위탁 정정 주문',
        'blocks': {
            'CCENT00200OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdMktCode', 'name': '주문시장코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'FnoOrdPtnCode', 'name': '선물옵션주문유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'FnoOrdprcPtnCode', 'name': '선물옵션호가유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'FnoOrdPrc', 'name': '선물옵션주문가격', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'MdfyQty', 'name': '정정수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CommdaCode', 'name': '통신매체코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'DscusBnsCmpltTime', 'name': '협의매매완료시각', 'type': 'string', 'length': 9, 'required': True}, {'key': 'GrpId', 'name': '그룹ID', 'type': 'string', 'length': 20, 'required': True}, {'key': 'OrdSeqno', 'name': '주문일련번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'PtflNo', 'name': '포트폴리오번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'BskNo', 'name': '바스켓번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'TrchNo', 'name': '트렌치번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'ItemNo', 'name': '아이템번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'MgempNo', 'name': '관리사원번호', 'type': 'string', 'length': 9, 'required': True}, {'key': 'FundId', 'name': '펀드ID', 'type': 'string', 'length': 12, 'required': True}, {'key': 'FundOrgOrdNo', 'name': '펀드원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'FundOrdNo', 'name': '펀드주문번호', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'single'
            },
            'CCENT00200OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdNo', 'name': '주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'BrnNm', 'name': '지점명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'OrdAbleAmt', 'name': '주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdAbleAmt', 'name': '현금주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdMgn', 'name': '주문증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdMgn', 'name': '현금주문증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdAbleQty', 'name': '주문가능수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CCENT00300': {
        'tr_cd': 'CCENT00300',
        'title': 'KRX야간파생 위탁 취소 주문',
        'blocks': {
            'CCENT00300OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdMktCode', 'name': '주문시장코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'FnoOrdPtnCode', 'name': '선물옵션주문유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'CancQty', 'name': '취소수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CommdaCode', 'name': '통신매체코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'DscusBnsCmpltTime', 'name': '협의매매완료시각', 'type': 'string', 'length': 9, 'required': True}, {'key': 'GrpId', 'name': '그룹ID', 'type': 'string', 'length': 20, 'required': True}, {'key': 'OrdSeqno', 'name': '주문일련번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'PtflNo', 'name': '포트폴리오번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'BskNo', 'name': '바스켓번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'TrchNo', 'name': '트렌치번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'ItemNo', 'name': '아이템번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'MgempNo', 'name': '관리사원번호', 'type': 'string', 'length': 9, 'required': True}, {'key': 'FundId', 'name': '펀드ID', 'type': 'string', 'length': 12, 'required': True}, {'key': 'FundOrgOrdNo', 'name': '펀드원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'FundOrdNo', 'name': '펀드주문번호', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'single'
            },
            'CCENT00300OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdNo', 'name': '주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'BrnNm', 'name': '지점명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'OrdAbleAmt', 'name': '주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdAbleAmt', 'name': '현금주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdMgn', 'name': '주문증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdMgn', 'name': '현금주문증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdAbleQty', 'name': '주문가능수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CD0': {
        'tr_cd': 'CD0',
        'title': '상품선물실시간상하한가',
        'fields': [
            {
                'key': 'gubun',
                'length': '	1',
                'name': '접속매매여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_gubun',
                'length': '	1',
                'name': '실시간가격제한여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_uplmtprice',
                'length': '	8.2',
                'name': '실시간상한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_dnlmtprice',
                'length': '	8.2',
                'name': '실시간하한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'CFOAQ00600': {
        'tr_cd': 'CFOAQ00600',
        'title': '선물옵션 계좌 주문체결내역 조회',
        'blocks': {
            'CFOAQ00600OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'InptPwd', 'name': '입력비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QrySrtDt', 'name': '조회시작일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryEndDt', 'name': '조회종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FnoClssCode', 'name': '선물옵션분류코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'PrdgrpCode', 'name': '상품군코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'PrdtExecTpCode', 'name': '체결구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'StnlnSeqTp', 'name': '정렬순서구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'CommdaCode', 'name': '통신매체코드', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            'CFOAQ00600OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'FutsOrdQty', 'name': '선물주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsExecQty', 'name': '선물체결수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptOrdQty', 'name': '옵션주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptExecQty', 'name': '옵션체결수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            },
            'CFOAQ00600OutBlock3': {
                'fields': [{'key': 'OrdDt', 'name': '주문일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OrdNo', 'name': '주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'OrdTime', 'name': '주문시각', 'type': 'string', 'length': 9, 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'BnsTpNm', 'name': '매매구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'MrcTpNm', 'name': '정정취소구분명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'FnoOrdprcPtnCode', 'name': '선물옵션호가유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'FnoOrdprcPtnNm', 'name': '선물옵션호가유형명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'OrdPrc', 'name': '주문가', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdTpNm', 'name': '주문구분명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'ExecTpNm', 'name': '체결구분명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'ExecPrc', 'name': '체결가', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'ExecQty', 'name': '체결수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CtrctTime', 'name': '약정시각', 'type': 'string', 'length': 9, 'required': True}, {'key': 'CtrctNo', 'name': '약정번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'ExecNo', 'name': '체결번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'BnsplAmt', 'name': '매매손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'UnercQty', 'name': '미체결수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'UserId', 'name': '사용자ID', 'type': 'string', 'length': 16, 'required': True}, {'key': 'CommdaCode', 'name': '통신매체코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'CommdaCodeNm', 'name': '통신매체코드명', 'type': 'string', 'length': 40, 'required': True}],
                'type': 'array'
            }
        }
    },
    'CFOAQ10100': {
        'tr_cd': 'CFOAQ10100',
        'title': '선물옵션 주문가능수량조회',
        'blocks': {
            'CFOAQ10100OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryTp', 'name': '조회구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OrdAmt', 'name': '주문금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'RatVal', 'name': '비율값', 'type': 'float', 'length': 19.8, 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'FnoOrdPrc', 'name': '선물옵션주문가격', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'FnoOrdprcPtnCode', 'name': '선물옵션호가유형코드', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            'CFOAQ10100OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'QryDt', 'name': '조회일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FnoNowPrc', 'name': '선물옵션현재가', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'OrdAbleQty', 'name': '주문가능수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NewOrdAbleQty', 'name': '신규주문가능수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'LqdtOrdAbleQty', 'name': '청산주문가능수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'UsePreargMgn', 'name': '사용예정증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'UsePreargMnyMgn', 'name': '사용예정현금증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdAbleAmt', 'name': '주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdAbleAmt', 'name': '현금주문가능금액', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOAQ50600': {
        'tr_cd': 'CFOAQ50600',
        'title': '선물옵션 계좌잔고 및 평가현황3',
        'blocks': {
            'CFOAQ50600OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'LqdtQtyQryTp', 'name': '청산수량조회구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'FutsPrcEvalTp', 'name': '선물가격평가구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'BalEvalTp', 'name': '잔고평가구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OrdDt', 'name': '주문일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'InptPwd', 'name': '입력비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}],
                'type': 'single'
            },
            'CFOAQ50600OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'EvalRat', 'name': '평가비율', 'type': 'string', 'length': 7.2, 'required': True}, {'key': 'BaseEvalAmt', 'name': '기준평가금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NetPnlAmt', 'name': '순손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'TotPnlAmt', 'name': '총손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptBnsAmt', 'name': '옵션매매금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsAdjstDfamt', 'name': '선물정산차금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptBnsplAmt', 'name': '옵션매매손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptEvalAmt', 'name': '옵션평가금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptEvalPnlAmt', 'name': '옵션평가손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsEvalPnlAmt', 'name': '선물평가손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'RcvblOdpnt', 'name': '미수연체료', 'type': 'float', 'length': 16, 'required': True}, {'key': 'RcvblAmt', 'name': '미수금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CmsnAmt', 'name': '수수료', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyAddMgn', 'name': '현금추가증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AddMgnTotamt', 'name': '추가증거금총액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'MnyMaintMgn', 'name': '현금유지증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MtmgnTotamt', 'name': '유지증거금총액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'MnyCsgnMgn', 'name': '현금위탁증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CsgnMgnTotamt', 'name': '위탁증거금총액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdAbleAmt', 'name': '현금주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdAbleTotAmt', 'name': '주문가능총금액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'PsnOutAbleSubstAmt', 'name': '인출가능대용금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PsnOutAbleCurAmt', 'name': '인출가능현금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PsnOutAbleTotAmt', 'name': '인출가능총금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FcurrSubstAmt', 'name': '외화대용금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'DpstgSubst', 'name': '예탁대용', 'type': 'float', 'length': 16, 'required': True}, {'key': 'DpstgMny', 'name': '예탁현금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'DpsamtTotamt', 'name': '예탁금총액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyEvalDpstgAmt', 'name': '현금평가예탁금액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'EvalDpsamtTotamt', 'name': '평가예탁금총액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'AcntEvalRat', 'name': '계좌평가비율', 'type': 'string', 'length': 7.2, 'required': True}],
                'type': 'single'
            },
            'CFOAQ50600OutBlock3': {
                'fields': [{'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'float', 'length': 12, 'required': True}, {'key': 'BnsplAmt', 'name': '매매손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'LqdtAbleQty', 'name': '청산가능수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'EvalRat', 'name': '평가비율', 'type': 'string', 'length': 7.2, 'required': True}, {'key': 'EvalPnl', 'name': '평가손익', 'type': 'float', 'length': 16, 'required': True}, {'key': 'EvalAmt', 'name': '평가금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FnoCmpPrc', 'name': '선물옵션대비가', 'type': 'string', 'length': 27.8, 'required': True}, {'key': 'PnlRat', 'name': '손익율', 'type': 'string', 'length': 18.6, 'required': True}, {'key': 'FnoNowPrc', 'name': '선물옵션현재가', 'type': 'string', 'length': 27.8, 'required': True}, {'key': 'FnoAvrPrc', 'name': '평균가', 'type': 'string', 'length': 19.8, 'required': True}, {'key': 'UnsttQty', 'name': '미결제수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'BnsTpNm', 'name': '매매구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOAT00100': {
        'tr_cd': 'CFOAT00100',
        'title': '선물옵션 정상주문',
        'blocks': {
            'CFOAT00100OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdMktCode', 'name': '주문시장코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'FnoOrdPtnCode', 'name': '선물옵션주문유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'FnoOrdprcPtnCode', 'name': '선물옵션호가유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'FnoTrdPtnCode', 'name': '선물옵션거래유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'FnoOrdPrc', 'name': '선물옵션주문가격', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CommdaCode', 'name': '통신매체코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'DscusBnsCmpltTime', 'name': '협의매매완료시각', 'type': 'string', 'length': 9, 'required': True}, {'key': 'GrpId', 'name': '그룹ID', 'type': 'string', 'length': 20, 'required': True}, {'key': 'OrdSeqno', 'name': '주문일련번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'PtflNo', 'name': '포트폴리오번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'BskNo', 'name': '바스켓번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'TrchNo', 'name': '트렌치번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'ItemNo', 'name': '항목번호', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OpDrtnNo', 'name': '운용지시번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'MgempNo', 'name': '관리사원번호', 'type': 'string', 'length': 9, 'required': True}, {'key': 'FundId', 'name': '펀드ID', 'type': 'string', 'length': 12, 'required': True}, {'key': 'FundOrdNo', 'name': '펀드주문번호', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'single'
            },
            'CFOAT00100OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdNo', 'name': '주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'BrnNm', 'name': '지점명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'OrdAbleAmt', 'name': '주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdAbleAmt', 'name': '현금주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdMgn', 'name': '주문증거금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdMgn', 'name': '현금주문증거금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdAbleQty', 'name': '주문가능수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOAT00200': {
        'tr_cd': 'CFOAT00200',
        'title': '선물옵션 정정주문',
        'blocks': {
            'CFOAT00200OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdMktCode', 'name': '주문시장코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'FnoOrdPtnCode', 'name': '선물옵션주문유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'FnoOrdprcPtnCode', 'name': '선물옵션호가유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'FnoOrdPrc', 'name': '선물옵션주문가격', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'MdfyQty', 'name': '정정수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CommdaCode', 'name': '통신매체코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'DscusBnsCmpltTime', 'name': '협의매매완료시각', 'type': 'string', 'length': 9, 'required': True}, {'key': 'GrpId', 'name': '그룹ID', 'type': 'string', 'length': 20, 'required': True}, {'key': 'OrdSeqno', 'name': '주문일련번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'PtflNo', 'name': '포트폴리오번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'BskNo', 'name': '바스켓번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'TrchNo', 'name': '트렌치번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'ItemNo', 'name': '아이템번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'MgempNo', 'name': '관리사원번호', 'type': 'string', 'length': 9, 'required': True}, {'key': 'FundId', 'name': '펀드ID', 'type': 'string', 'length': 12, 'required': True}, {'key': 'FundOrgOrdNo', 'name': '펀드원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'FundOrdNo', 'name': '펀드주문번호', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'single'
            },
            'CFOAT00200OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdNo', 'name': '주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'BrnNm', 'name': '지점명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'OrdAbleAmt', 'name': '주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdAbleAmt', 'name': '현금주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdMgn', 'name': '주문증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdMgn', 'name': '현금주문증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdAbleQty', 'name': '주문가능수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOAT00300': {
        'tr_cd': 'CFOAT00300',
        'title': '선물옵션 취소주문',
        'blocks': {
            'CFOAT00300OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdMktCode', 'name': '주문시장코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'FnoOrdPtnCode', 'name': '선물옵션주문유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'CancQty', 'name': '취소수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CommdaCode', 'name': '통신매체코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'DscusBnsCmpltTime', 'name': '협의매매완료시각', 'type': 'string', 'length': 9, 'required': True}, {'key': 'GrpId', 'name': '그룹ID', 'type': 'string', 'length': 20, 'required': True}, {'key': 'OrdSeqno', 'name': '주문일련번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'PtflNo', 'name': '포트폴리오번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'BskNo', 'name': '바스켓번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'TrchNo', 'name': '트렌치번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'ItemNo', 'name': '아이템번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'MgempNo', 'name': '관리사원번호', 'type': 'string', 'length': 9, 'required': True}, {'key': 'FundId', 'name': '펀드ID', 'type': 'string', 'length': 12, 'required': True}, {'key': 'FundOrgOrdNo', 'name': '펀드원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'FundOrdNo', 'name': '펀드주문번호', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'single'
            },
            'CFOAT00300OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdNo', 'name': '주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'BrnNm', 'name': '지점명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'OrdAbleAmt', 'name': '주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdAbleAmt', 'name': '현금주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdMgn', 'name': '주문증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdMgn', 'name': '현금주문증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdAbleQty', 'name': '주문가능수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOBQ10500': {
        'tr_cd': 'CFOBQ10500',
        'title': '선물옵션 계좌예탁금증거금조회',
        'blocks': {
            'CFOBQ10500OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            },
            'CFOBQ10500OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'DpsamtTotamt', 'name': '예탁금총액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'Dps', 'name': '예수금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SubstAmt', 'name': '대용금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FilupDpsamtTotamt', 'name': '충당예탁금총액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FilupDps', 'name': '충당예수금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsPnlAmt', 'name': '선물손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'WthdwAbleAmt', 'name': '인출가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PsnOutAbleCurAmt', 'name': '인출가능현금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PsnOutAbleSubstAmt', 'name': '인출가능대용금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'Mgn', 'name': '증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyMgn', 'name': '현금증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdAbleAmt', 'name': '주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdAbleAmt', 'name': '현금주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AddMgn', 'name': '추가증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyAddMgn', 'name': '현금추가증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AmtPrdayChckInAmt', 'name': '금전일수표입금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FnoPrdaySubstSellAmt', 'name': '선물옵션전일대용매도금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FnoCrdaySubstSellAmt', 'name': '선물옵션금일대용매도금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FnoPrdayFdamt', 'name': '선물옵션전일가입금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FnoCrdayFdamt', 'name': '선물옵션금일가입금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FcurrSubstAmt', 'name': '외화대용금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FnoAcntAfmgnNm', 'name': '선물옵션계좌사후증거금명', 'type': 'string', 'length': 20, 'required': True}],
                'type': 'single'
            },
            'CFOBQ10500OutBlock3': {
                'fields': [{'key': 'PdGrpCodeNm', 'name': '상품군코드명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'NetRiskMgn', 'name': '순위험증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PrcMgn', 'name': '가격증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SprdMgn', 'name': '스프레드증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PrcFlctMgn', 'name': '가격변동증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MinMgn', 'name': '최소증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdMgn', 'name': '주문증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptNetBuyAmt', 'name': '옵션순매수금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CsgnMgn', 'name': '위탁증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MaintMgn', 'name': '유지증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsBuyExecAmt', 'name': '선물매수체결금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsSellExecAmt', 'name': '선물매도체결금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptBuyExecAmt', 'name': '옵션매수체결금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptSellExecAmt', 'name': '옵션매도체결금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsPnlAmt', 'name': '선물손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'TotRiskCsgnMgn', 'name': '총위험위탁증거금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'UndCsgnMgn', 'name': '인수도위탁증거금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnRdctAmt', 'name': '증거금감면금액', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'array'
            }
        }
    },
    'CFOBQ10800': {
        'tr_cd': 'CFOBQ10800',
        'title': '선물옵션 옵션매도시 주문증거금조회(옵션매도시 1계약당 주문증거금)',
        'blocks': {
            'CFOBQ10800OutBlock1': {
                'fields': [{'key': 'SpclDtPtnCode', 'name': '특별일자유형코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'IsuMdclssCode', 'name': '종목중분류코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'IsuSmclssCode', 'name': '종목소분류코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'DueYymm', 'name': '만기년월', 'type': 'string', 'length': 6, 'required': True}, {'key': 'SettWklyCnt', 'name': '결제주간수', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            'CFOBQ10800OutBlock2': {
                'fields': [{'key': 'ElwXrcPrc', 'name': '행사가', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'FnoIsuNo', 'name': '선물옵션종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'HanglIsuNm1', 'name': '한글종목명1', 'type': 'string', 'length': 40, 'required': True}, {'key': 'TpNm1', 'name': '구분명1', 'type': 'string', 'length': 40, 'required': True}, {'key': 'UpOptRegulThrprc', 'name': '상승옵션조정이론가', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'Thrprc1', 'name': '이론가1', 'type': 'float', 'length': 19.8, 'required': True}, {'key': 'BasePrc1', 'name': '기준가1', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'OrdMgn1', 'name': '주문증거금액1', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FnoIsuNo0', 'name': '선물옵션종목번호0', 'type': 'string', 'length': 12, 'required': True}, {'key': 'HanglIsuNm2', 'name': '한글종목명2', 'type': 'string', 'length': 40, 'required': True}, {'key': 'TpNm2', 'name': '구분명2', 'type': 'string', 'length': 40, 'required': True}, {'key': 'DownOptRegulThrprc', 'name': '하락옵션조정이론가', 'type': 'float', 'length': 27.8, 'required': True}, {'key': 'Thrprc2', 'name': '이론가2', 'type': 'float', 'length': 19.8, 'required': True}, {'key': 'BasePrc2', 'name': '기준가2', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'OrdMgn2', 'name': '주문증거금액2', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'array'
            }
        }
    },
    'CFOEQ11100': {
        'tr_cd': 'CFOEQ11100',
        'title': '선물옵션가정산예탁금상세',
        'blocks': {
            'CFOEQ11100OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'BnsDt', 'name': '매매일', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            },
            'CFOEQ11100OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'OpnmkDpsamtTotamt', 'name': '개장시예탁금총액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OpnmkDps', 'name': '개장시예수금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OpnmkMnyrclAmt', 'name': '개장시현금미수금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OpnmkSubstAmt', 'name': '개장시대용금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'TotAmt', 'name': '총금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'Dps', 'name': '예수금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyrclAmt', 'name': '현금미수금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SubstDsgnAmt', 'name': '대용지정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CsgnMgn', 'name': '위탁증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyCsgnMgn', 'name': '현금위탁증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MaintMgn', 'name': '유지증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyMaintMgn', 'name': '현금유지증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OutAbleAmt', 'name': '출금가능총액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyoutAbleAmt', 'name': '출금가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SubstOutAbleAmt', 'name': '출금가능대용', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdAbleAmt', 'name': '주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyOrdAbleAmt', 'name': '현금주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AddMgnOcrTpCode', 'name': '추가증거금구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'AddMgn', 'name': '추가증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyAddMgn', 'name': '현금추가증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdayTotAmt', 'name': '익일예탁총액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdayDps', 'name': '익일예탁현금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdayMnyrclAmt', 'name': '익일미수금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdaySubstAmt', 'name': '익일예탁대용', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdayCsgnMgn', 'name': '익일위탁증거금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdayMnyCsgnMgn', 'name': '익일위탁증거금현금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdayMaintMgn', 'name': '익일유지증거금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdayMnyMaintMgn', 'name': '익일유지증거금현금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdayOutAbleAmt', 'name': '익일인출가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdayMnyoutAbleAmt', 'name': '익일인출가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdaySubstOutAbleAmt', 'name': '익일인출가능대용', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdayOrdAbleAmt', 'name': '익일주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdayMnyOrdAbleAmt', 'name': '익일주문가능현금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdayAddMgnTp', 'name': '익일추가증거금구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'NtdayAddMgn', 'name': '익일추가증거금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdayMnyAddMgn', 'name': '익일추가증거금현금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'NtdaySettAmt', 'name': '익일결제금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'EvalDpsamtTotamt', 'name': '평가예탁금총액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'MnyEvalDpstgAmt', 'name': '현금평가예탁금액', 'type': 'float', 'length': 15, 'required': True}, {'key': 'DpsamtUtlfeeGivPrergAmt', 'name': '예탁금이용료지급예정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'TaxAmt', 'name': '세금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CsgnMgnrat', 'name': '위탁증거금 비율', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'CsgnMnyMgnrat', 'name': '위탁증거금현금비율', 'type': 'float', 'length': 7.2, 'required': True}, {'key': 'DpstgTotamtLackAmt', 'name': '예탁총액부족금액(위탁증거금기준)', 'type': 'float', 'length': 16, 'required': True}, {'key': 'DpstgMnyLackAmt', 'name': '예탁현금부족금액(위탁증거금기준)', 'type': 'float', 'length': 16, 'required': True}, {'key': 'RealInAmt', 'name': '실입금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'InAmt', 'name': '입금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OutAmt', 'name': '출금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsAdjstDfamt', 'name': '선물정산차금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsThdayDfamt', 'name': '선물당일차금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsUpdtDfamt', 'name': '선물갱신차금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsLastSettDfamt', 'name': '선물최종결제차금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptSettDfamt', 'name': '옵션결제차금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptBuyAmt', 'name': '옵션매수금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptSellAmt', 'name': '옵션매도금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptXrcDfamt', 'name': '옵션행사차금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptAsgnDfamt', 'name': '옵션배정차금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'RealGdsUndAmt', 'name': '실물인수도금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'RealGdsUndAsgnAmt', 'name': '실물인수도배정대금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'RealGdsUndXrcAmt', 'name': '실물인수도행사대금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CmsnAmt', 'name': '수수료', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsCmsn', 'name': '선물수수료', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptCmsn', 'name': '옵션수수료', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsCtrctQty', 'name': '선물약정수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsCtrctAmt', 'name': '선물약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptCtrctQty', 'name': '옵션약정수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptCtrctAmt', 'name': '옵션약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsUnsttQty', 'name': '선물미결제수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsUnsttAmt', 'name': '선물미결제금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptUnsttQty', 'name': '옵션미결제수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptUnsttAmt', 'name': '옵션미결제금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsBuyUnsttQty', 'name': '선물매수미결제수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsBuyUnsttAmt', 'name': '선물매수미결제금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsSellUnsttQty', 'name': '선물매도미결제수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsSellUnsttAmt', 'name': '선물매도미결제금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptBuyUnsttQty', 'name': '옵션매수미결제수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptBuyUnsttAmt', 'name': '옵션매수미결제금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptSellUnsttQty', 'name': '옵션매도미결제수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptSellUnsttAmt', 'name': '옵션매도미결제금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsBuyctrQty', 'name': '선물매수약정수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsBuyctrAmt', 'name': '선물매수약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsSlctrQty', 'name': '선물매도약정수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsSlctrAmt', 'name': '선물매도약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptBuyctrQty', 'name': '옵션매수약정수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptBuyctrAmt', 'name': '옵션매수약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptSlctrQty', 'name': '옵션매도약정수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptSlctrAmt', 'name': '옵션매도약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsBnsplAmt', 'name': '선물매매손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptBnsplAmt', 'name': '옵션매매손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsEvalPnlAmt', 'name': '선물평가손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptEvalPnlAmt', 'name': '옵션평가손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsEvalAmt', 'name': '선물평가금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptEvalAmt', 'name': '옵션평가금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MktEndAfMnyInAmt', 'name': '장종료후현금입금금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MktEndAfMnyOutAmt', 'name': '장종료후현금출금금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MktEndAfSubstDsgnAmt', 'name': '장종료후대용지정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MktEndAfSubstAbndAmt', 'name': '장종료후대용해지금액', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CFOEQ82600': {
        'tr_cd': 'CFOEQ82600',
        'title': '선물옵션 일별 계좌손익내역',
        'blocks': {
            'CFOEQ82600OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QrySrtDt', 'name': '조회시작일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryEndDt', 'name': '조회종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryTp', 'name': '조회구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'StnlnSeqTp', 'name': '정렬순서구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'FnoBalEvalTpCode', 'name': '선물옵션잔고평가구분코드', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            },
            'CFOEQ82600OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'FutsAdjstDfamt', 'name': '선물정산차금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptBnsplAmt', 'name': '옵션매매손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FnoCmsnAmt', 'name': '선물옵션수수료', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PnlSumAmt', 'name': '손익합계금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyinSumAmt', 'name': '입금합계금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyoutSumAmt', 'name': '출금합계금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}],
                'type': 'single'
            },
            'CFOEQ82600OutBlock3': {
                'fields': [{'key': 'QryDt', 'name': '조회일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'DpstgTotamt', 'name': '예탁총액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'DpstgMny', 'name': '예탁현금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FnoMgn', 'name': '선물옵션증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsPnlAmt', 'name': '선물손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptBsnPnlAmt', 'name': '옵션매매손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptEvalPnlAmt', 'name': '옵션평가손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CmsnAmt', 'name': '수수료', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SumAmt1', 'name': '합계금액1', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SumAmt2', 'name': '합계금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PnlSumAmt', 'name': '손익합계금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsBuyAmt', 'name': '선물매수금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsSellAmt', 'name': '선물매도금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptBuyAmt', 'name': '옵션매수금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptSellAmt', 'name': '옵션매도금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'InAmt', 'name': '입금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OutAmt', 'name': '출금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'EvalAmt', 'name': '평가금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AddupEvalAmt', 'name': '합산평가금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'Amt2', 'name': '금액2', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'array'
            }
        }
    },
    'CFOFQ02400': {
        'tr_cd': 'CFOFQ02400',
        'title': '계좌 미결제 약정현황(평균가)',
        'blocks': {
            'CFOFQ02400OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'RegMktCode', 'name': '등록시장코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'BuyDt', 'name': '매수일자', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            },
            'CFOFQ02400OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'FutsCtrctQty', 'name': '선물약정수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptCtrctQty', 'name': '옵션약정수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CtrctQty', 'name': '약정수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsCtrctAmt', 'name': '선물약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsBuyctrAmt', 'name': '선물매수약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsSlctrAmt', 'name': '선물매도약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CalloptCtrctAmt', 'name': '콜옵션약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CallBuyAmt', 'name': '콜매수금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CallSellAmt', 'name': '콜매도금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PutoptCtrctAmt', 'name': '풋옵션약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PutBuyAmt', 'name': '풋매수금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PutSellAmt', 'name': '풋매도금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AllCtrctAmt', 'name': '전체약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'BuyctrAsmAmt', 'name': '매수약정누계금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'SlctrAsmAmt', 'name': '매도약정누계금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsPnlSum', 'name': '선물손익합계', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptPnlSum', 'name': '옵션손익합계', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AllPnlSum', 'name': '전체손익합계', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            },
            'CFOFQ02400OutBlock3': {
                'fields': [{'key': 'FnoClssCode', 'name': '선물옵션품목구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'FutsSellQty', 'name': '선물매도수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsSellPnl', 'name': '선물매도손익', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsBuyQty', 'name': '선물매수수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsBuyPnl', 'name': '선물매수손익', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CallSellQty', 'name': '콜매도수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CallSellPnl', 'name': '콜매도손익', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CallBuyQty', 'name': '콜매수수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CallBuyPnl', 'name': '콜매수손익', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PutSellQty', 'name': '풋매도수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PutSellPnl', 'name': '풋매도손익', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PutBuyQty', 'name': '풋매수수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PutBuyPnl', 'name': '풋매수손익', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'array'
            },
            'CFOFQ02400OutBlock4': {
                'fields': [{'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'BnsTpNm', 'name': '매매구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'BalQty', 'name': '잔고수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FnoAvrPrc', 'name': '평균가', 'type': 'float', 'length': 19.8, 'required': True}, {'key': 'BgnAmt', 'name': '당초금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'ThdayLqdtQty', 'name': '당일청산수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'Curprc', 'name': '현재가', 'type': 'float', 'length': 13.2, 'required': True}, {'key': 'EvalAmt', 'name': '평가금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'EvalPnlAmt', 'name': '평가손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'EvalErnrat', 'name': '평가수익률', 'type': 'float', 'length': 12.6, 'required': True}],
                'type': 'array'
            }
        }
    },
    'DBM': {
        'tr_cd': 'DBM',
        'title': 'KRX야간파생 투자자매매현황',
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
                'key': 'fottjjcode',
                'length': 5,
                'name': '파생상품투자자코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'DBT': {
        'tr_cd': 'DBT',
        'title': 'KRX야간파생 투자자별현황',
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
                'key': 'fottjjcode',
                'length': 5,
                'name': '파생상품투자자코드',
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
    'DC0': {
        'tr_cd': 'DC0',
        'title': 'KRX야간파생 체결',
        'fields': [
            {
                'key': 'date',
                'length': 8,
                'name': '일자',
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
                'key': 'chetime',
                'length': 6,
                'name': '체결시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': '	6.2',
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
                'length': '	6.2',
                'name': '현재가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'open',
                'length': '	6.2',
                'name': '시가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'high',
                'length': '	6.2',
                'name': '고가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low',
                'length': '	6.2',
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
                'length': '	6',
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
                'key': 'offerho1',
                'length': '	6.2',
                'name': '매도호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho1',
                'length': '	6.2',
                'name': '매수호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'openyak',
                'length': '	8',
                'name': '미결제약정수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'k200jisu',
                'length': '	6.2',
                'name': 'KOSPI200지수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'theoryprice',
                'length': '	6.2',
                'name': '이론가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'kasis',
                'length': '	6.2',
                'name': '괴리율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sbasis',
                'length': '	6.2',
                'name': '시장BASIS',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ibasis',
                'length': '	6.2',
                'name': '이론BASIS',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'openyakcha',
                'length': '	8',
                'name': '미결제약정증감',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jgubun',
                'length': '	2',
                'name': '장운영정보',
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
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'eqva',
                'length': 7.2,
                'name': 'KOSPI등가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'impv',
                'length': 6.2,
                'name': '내재변동성',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'timevalue',
                'length': 6.2,
                'name': '시간가치',
                'required': True,
                'type': 'float'
            }
        ]
    },
    'DD0': {
        'tr_cd': 'DD0',
        'title': 'KRX야간파생 실시간상하한가',
        'fields': [
            {
                'key': 'gubun',
                'length': '	1',
                'name': '접속매매여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_gubun',
                'length': '	1',
                'name': '실시간가격제한여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_uplmtprice',
                'length': '	8.2',
                'name': '실시간상한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_dnlmtprice',
                'length': '	8.2',
                'name': '실시간하한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'DH0': {
        'tr_cd': 'DH0',
        'title': 'KRX야간파생 호가',
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
                'length': '	6.2',
                'name': '매도호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho1',
                'length': '	6.2',
                'name': '매수호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem1',
                'length': '	6',
                'name': '매도호가수량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem1',
                'length': '	6',
                'name': '매수호가수량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt1',
                'length': '	5',
                'name': '매도호가건수1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt1',
                'length': '	5',
                'name': '매수호가건수1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho2',
                'length': '	6.2',
                'name': '매도호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho2',
                'length': '	6.2',
                'name': '매수호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem2',
                'length': '	6',
                'name': '매도호가수량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem2',
                'length': '	6',
                'name': '매수호가수량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt2',
                'length': '	5',
                'name': '매도호가건수2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt2',
                'length': '	5',
                'name': '매수호가건수2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho3',
                'length': '	6.2',
                'name': '매도호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho3',
                'length': '	6.2',
                'name': '매수호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem3',
                'length': '	6',
                'name': '매도호가수량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem3',
                'length': '	6',
                'name': '매수호가수량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt3',
                'length': '	5',
                'name': '매도호가건수3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt3',
                'length': '	5',
                'name': '매수호가건수3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho4',
                'length': '	6.2',
                'name': '매도호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho4',
                'length': '	6.2',
                'name': '매수호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem4',
                'length': '	6',
                'name': '매도호가수량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem4',
                'length': '	6',
                'name': '매수호가수량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt4',
                'length': '	5',
                'name': '매도호가건수4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt4',
                'length': '	5',
                'name': '매수호가건수4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho5',
                'length': '	6.2',
                'name': '매도호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho5',
                'length': '	6.2',
                'name': '매수호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem5',
                'length': '	6',
                'name': '매도호가수량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem5',
                'length': '	6',
                'name': '매수호가수량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt5',
                'length': '	5',
                'name': '매도호가건수5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt5',
                'length': '	5',
                'name': '매수호가건수5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totofferrem',
                'length': '	6',
                'name': '매도호가총수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidrem',
                'length': '	6',
                'name': '매수호가총수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totoffercnt',
                'length': '	5',
                'name': '매도호가총건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidcnt',
                'length': '	5',
                'name': '매수호가총건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'danhochk',
                'length': '	1',
                'name': '단일가호가여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'alloc_gubun',
                'length': '	1',
                'name': '배분적용구분',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'DX0': {
        'tr_cd': 'DX0',
        'title': 'KRX야간파생 가격제한폭확대',
        'fields': [
            {
                'key': 'upstep',
                'length': '	2',
                'name': '적용상한단계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dnstep',
                'length': '	2',
                'name': '적용하한단계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'uplmtprice',
                'length': '	6.2',
                'name': '적용상한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dnlmtprice',
                'length': '	6.2',
                'name': '적용하한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'DYC': {
        'tr_cd': 'DYC',
        'title': 'KRX야간파생 예상체결',
        'fields': [
            {
                'key': 'ychetime',
                'length': '	6',
                'name': '예상체결시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'yeprice',
                'length': '	6.2',
                'name': '예상체결가격',
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
                'length': '	6.2',
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
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'expct_ccls_q',
                'length': 9,
                'name': '예상체결수량',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'FC0': {
        'tr_cd': 'FC0',
        'title': 'KOSPI200선물체결',
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
                'length': '	6.2',
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
                'length': '	6.2',
                'name': '현재가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'open',
                'length': '	6.2',
                'name': '시가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'high',
                'length': '	6.2',
                'name': '고가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low',
                'length': '	6.2',
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
                'length': '	6',
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
                'key': 'offerho1',
                'length': '	6.2',
                'name': '매도호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho1',
                'length': '	6.2',
                'name': '매수호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'openyak',
                'length': '	8',
                'name': '미결제약정수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'k200jisu',
                'length': '	6.2',
                'name': 'KOSPI200지수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'theoryprice',
                'length': '	6.2',
                'name': '이론가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'kasis',
                'length': '	6.2',
                'name': '괴리율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sbasis',
                'length': '	6.2',
                'name': '시장BASIS',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ibasis',
                'length': '	6.2',
                'name': '이론BASIS',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'openyakcha',
                'length': '	8',
                'name': '미결제약정증감',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jgubun',
                'length': '	2',
                'name': '장운영정보',
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
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'FD0': {
        'tr_cd': 'FD0',
        'title': 'KOSPI200선물실시간상하한가',
        'fields': [
            {
                'key': 'gubun',
                'length': '	1',
                'name': '접속매매여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_gubun',
                'length': '	1',
                'name': '실시간가격제한여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_uplmtprice',
                'length': '	8.2',
                'name': '실시간상한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_dnlmtprice',
                'length': '	8.2',
                'name': '실시간하한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'FH0': {
        'tr_cd': 'FH0',
        'title': 'KOSPI200선물호가',
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
                'length': '	6.2',
                'name': '매도호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho1',
                'length': '	6.2',
                'name': '매수호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem1',
                'length': '	6',
                'name': '매도호가수량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem1',
                'length': '	6',
                'name': '매수호가수량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt1',
                'length': '	5',
                'name': '매도호가건수1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt1',
                'length': '	5',
                'name': '매수호가건수1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho2',
                'length': '	6.2',
                'name': '매도호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho2',
                'length': '	6.2',
                'name': '매수호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem2',
                'length': '	6',
                'name': '매도호가수량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem2',
                'length': '	6',
                'name': '매수호가수량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt2',
                'length': '	5',
                'name': '매도호가건수2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt2',
                'length': '	5',
                'name': '매수호가건수2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho3',
                'length': '	6.2',
                'name': '매도호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho3',
                'length': '	6.2',
                'name': '매수호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem3',
                'length': '	6',
                'name': '매도호가수량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem3',
                'length': '	6',
                'name': '매수호가수량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt3',
                'length': '	5',
                'name': '매도호가건수3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt3',
                'length': '	5',
                'name': '매수호가건수3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho4',
                'length': '	6.2',
                'name': '매도호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho4',
                'length': '	6.2',
                'name': '매수호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem4',
                'length': '	6',
                'name': '매도호가수량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem4',
                'length': '	6',
                'name': '매수호가수량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt4',
                'length': '	5',
                'name': '매도호가건수4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt4',
                'length': '	5',
                'name': '매수호가건수4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho5',
                'length': '	6.2',
                'name': '매도호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho5',
                'length': '	6.2',
                'name': '매수호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem5',
                'length': '	6',
                'name': '매도호가수량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem5',
                'length': '	6',
                'name': '매수호가수량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt5',
                'length': '	5',
                'name': '매도호가건수5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt5',
                'length': '	5',
                'name': '매수호가건수5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totofferrem',
                'length': '	6',
                'name': '매도호가총수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidrem',
                'length': '	6',
                'name': '매수호가총수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totoffercnt',
                'length': '	5',
                'name': '매도호가총건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidcnt',
                'length': '	5',
                'name': '매수호가총건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'danhochk',
                'length': '	1',
                'name': '단일가호가여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'alloc_gubun',
                'length': '	1',
                'name': '배분적용구분',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'FOCCQ33600': {
        'tr_cd': 'FOCCQ33600',
        'title': '주식계좌 기간별수익률 상세',
        'blocks': {
            'FOCCQ33600OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QrySrtDt', 'name': '조회시작일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryEndDt', 'name': '조회종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'TermTp', 'name': '기간구분', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            },
            'FOCCQ33600OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'BnsctrAmt', 'name': '매매약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyinAmt', 'name': '입금금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyoutAmt', 'name': '출금금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'InvstAvrbalPramt', 'name': '투자원금평잔금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'InvstPlAmt', 'name': '투자손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'InvstErnrat', 'name': '투자수익률', 'type': 'float', 'length': 9.2, 'required': True}],
                'type': 'single'
            },
            'FOCCQ33600OutBlock3': {
                'fields': [{'key': 'BaseDt', 'name': '기준일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FdEvalAmt', 'name': '기초평가금액', 'type': 'float', 'length': 19, 'required': True}, {'key': 'EotEvalAmt', 'name': '기말평가금액', 'type': 'float', 'length': 19, 'required': True}, {'key': 'InvstAvrbalPramt', 'name': '투자원금평잔금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'BnsctrAmt', 'name': '매매약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyinSecinAmt', 'name': '입금고액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyoutSecoutAmt', 'name': '출금고액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'EvalPnlAmt', 'name': '평가손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'TermErnrat', 'name': '기간수익률', 'type': 'float', 'length': 11.3, 'required': True}, {'key': 'Idx', 'name': '지수', 'type': 'float', 'length': 13.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    'FOCCQ33700': {
        'tr_cd': 'FOCCQ33700',
        'title': '선물옵션 기간별 계좌 수익률 현황',
        'blocks': {
            'FOCCQ33700OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QrySrtDt', 'name': '조회시작일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryEndDt', 'name': '조회종료일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryTp', 'name': '조회구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'BaseAmtTp', 'name': '기준금액구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'QryTermTp', 'name': '조회기간구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'PnlCalcTpCode', 'name': '손익산출구분코드', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            },
            'FOCCQ33700OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'InAmt', 'name': '입금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OutAmt', 'name': '출금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FnoCtrctAmt', 'name': '선물옵션약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'InvstPramtAvrbalAmt', 'name': '투자원금평잔금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'FutsAdjstDfamt', 'name': '선물정산차금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptBsnPnlAmt', 'name': '옵션매매손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptEvalPnlAmt', 'name': '옵션평가손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'InvstPlAmt', 'name': '투자손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'ErnRat', 'name': '수익률', 'type': 'float', 'length': 12.6, 'required': True}],
                'type': 'single'
            },
            'FOCCQ33700OutBlock3': {
                'fields': [{'key': 'TrdDt', 'name': '거래일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FdDpsastAmt', 'name': '기초예탁자산금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'EotDpsastAmt', 'name': '기말예탁자산금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'InAmt', 'name': '입금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OutAmt', 'name': '출금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'InvstAvrbalPramt', 'name': '투자원금평잔금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'InvstPlAmt', 'name': '투자손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'Ernrat', 'name': '수익률', 'type': 'float', 'length': 12.6, 'required': True}, {'key': 'FnoCtrctAmt', 'name': '선물옵션약정금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'Trnrat', 'name': '회전율', 'type': 'float', 'length': 12.6, 'required': True}, {'key': 'FutsAdjstDfamt', 'name': '선물정산차금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptBsnPnlAmt', 'name': '옵션매매손익금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OptEvalPnlAmt', 'name': '옵션평가손익금액', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'array'
            }
        }
    },
    'FX0': {
        'tr_cd': 'FX0',
        'title': 'KOSPI200선물가격제한폭확대',
        'fields': [
            {
                'key': 'upstep',
                'length': '	2',
                'name': '적용상한단계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dnstep',
                'length': '	2',
                'name': '적용하한단계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'uplmtprice',
                'length': '	6.2',
                'name': '적용상한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dnlmtprice',
                'length': '	6.2',
                'name': '적용하한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'H01': {
        'tr_cd': 'H01',
        'title': '선물주문정정취소',
        'fields': []
    },
    'H02': {
        'tr_cd': 'H02',
        'title': 'KRX야간파생 선물정정취소',
        'fields': [
            {
                'key': 'lineseq',
                'length': 10,
                'name': '라인일련번호',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'accno',
                'length': 11,
                'name': '계좌번호',
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
                'key': 'seq',
                'length': 11,
                'name': '일련번호',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'trcode',
                'length': 11,
                'name': 'trcode',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'megrpno',
                'length': 2,
                'name': '매칭그룹번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'boardid',
                'length': 2,
                'name': '보드ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'memberno',
                'length': 5,
                'name': '회원번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bpno',
                'length': 5,
                'name': '지점번호',
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
                'key': 'orgordno',
                'length': 10,
                'name': '원주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'expcode',
                'length': 12,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dosugb',
                'length': 1,
                'name': '매도수구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mocagb',
                'length': 1,
                'name': '정정취소구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'accno1',
                'length': 12,
                'name': '계좌번호1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'qty2',
                'length': 10,
                'name': '호가수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'price',
                'length': 11.2,
                'name': '호가가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ordgb',
                'length': 1,
                'name': '주문유형',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'hogagb',
                'length': 1,
                'name': '호가구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sihogagb',
                'length': 11,
                'name': '시장조성호가구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tradid',
                'length': 5,
                'name': '자사주신고서ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'treacode',
                'length': 1,
                'name': '자사주매매방법',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'askcode',
                'length': 2,
                'name': '매도유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'creditcode',
                'length': 2,
                'name': '신용구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jakigb',
                'length': 2,
                'name': '위탁자기구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'trustnum',
                'length': 5,
                'name': '위탁사번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ptgb',
                'length': 2,
                'name': '프로그램구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'substonum',
                'length': 12,
                'name': '대용주권계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'accgb',
                'length': 2,
                'name': '계좌구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'accmarggb',
                'length': 2,
                'name': '계좌증거금코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'nationcode',
                'length': 3,
                'name': '국가코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'investgb',
                'length': 4,
                'name': '투자자구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'forecode',
                'length': 2,
                'name': '외국인코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'medcode',
                'length': 1,
                'name': '주문매체구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordid',
                'length': 12,
                'name': '주문식별자번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'macid',
                'length': 12,
                'name': 'MAC주소',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'orddate',
                'length': 8,
                'name': '호가일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'rcvtime',
                'length': 9,
                'name': '회원사주문시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mem_filler',
                'length': 7,
                'name': 'mem_filler',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mem_accno',
                'length': 11,
                'name': 'mem_accno',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mem_filler1',
                'length': 42,
                'name': 'mem_filler1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordacpttm',
                'length': 9,
                'name': '매칭접수시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'qty',
                'length': 10,
                'name': '실정정취소수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'autogb',
                'length': 1,
                'name': '자동취소구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'rejcode',
                'length': 4,
                'name': '거부사유',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'prgordde',
                'length': 1,
                'name': '프로그램호가신고',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'trdr_id',
                'length': 6,
                'name': '거래자ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ord_grp_no',
                'length': 2,
                'name': '호가그룹번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'smp_cd',
                'length': 1,
                'name': '자전거래방지코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ord_cond_prc',
                'length': 11.2,
                'name': '호가조건가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'trd_mkt_choic_tp_cd',
                'length': 1,
                'name': '거래시장선택구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'srtsell_id',
                'length': 10,
                'name': '공매도ID',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'JC0': {
        'tr_cd': 'JC0',
        'title': '주식선물체결',
        'fields': [
            {
                'key': 'futcode',
                'length': 8,
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
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
                'name': '대비기호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'change',
                'length': 10,
                'name': '전일대비',
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
                'key': 'price',
                'length': 10,
                'name': '현재가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'open',
                'length': 10,
                'name': '시가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'high',
                'length': 10,
                'name': '고가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low',
                'length': 10,
                'name': '저가',
                'required': True,
                'type': 'string'
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
                'length': 6,
                'name': '체결량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'volume',
                'length': 12,
                'name': '누적거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'value',
                'length': 15,
                'name': '누적거래대금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdvolume',
                'length': 12,
                'name': '매도누적체결량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mdchecnt',
                'length': 8,
                'name': '매도누적체결건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume',
                'length': 12,
                'name': '매수누적체결량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mschecnt',
                'length': 8,
                'name': '매수누적체결건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cpower',
                'length': 9.2,
                'name': '체결강도',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho1',
                'length': 10,
                'name': '매도호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho1',
                'length': 10,
                'name': '매수호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'openyak',
                'length': 8,
                'name': '미결제약정수량',
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
                'key': 'theoryprice',
                'length': 8,
                'name': '이론가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'kasis',
                'length': 6.3,
                'name': '괴리율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sbasis',
                'length': 6,
                'name': '시장BASIS',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ibasis',
                'length': 6,
                'name': '이론BASIS',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'openyakcha',
                'length': 8,
                'name': '미결제약정증감',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jgubun',
                'length': 2,
                'name': '장운영정보',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jnilvolume',
                'length': 12,
                'name': '전일동시간대거래량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'basprice',
                'length': 8,
                'name': '기초자산현재가',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'JD0': {
        'tr_cd': 'JD0',
        'title': '주식선물실시간상하한가',
        'fields': [
            {
                'key': 'gubun',
                'length': '	1',
                'name': '접속매매여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_gubun',
                'length': '	1',
                'name': '실시간가격제한여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_uplmtprice',
                'length': '	10',
                'name': '실시간상한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_dnlmtprice',
                'length': '	10',
                'name': '실시간하한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'JH0': {
        'tr_cd': 'JH0',
        'title': '주식선물호가',
        'fields': [
            {
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'hotime',
                'length': '	6',
                'name': '호가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho1',
                'length': '	10',
                'name': '매도호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho1',
                'length': '	10',
                'name': '매수호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem1',
                'length': '	7',
                'name': '매도호가수량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem1',
                'length': '	7',
                'name': '매수호가수량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt1',
                'length': '	5',
                'name': '매도호가건수1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt1',
                'length': '	5',
                'name': '매수호가건수1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho2',
                'length': '	10',
                'name': '매도호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho2',
                'length': '	10',
                'name': '매수호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem2',
                'length': '	7',
                'name': '매도호가수량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem2',
                'length': '	7',
                'name': '매수호가수량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt2',
                'length': '	5',
                'name': '매도호가건수2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt2',
                'length': '	5',
                'name': '매수호가건수2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho3',
                'length': '	10',
                'name': '매도호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho3',
                'length': '	10',
                'name': '매수호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem3',
                'length': '	7',
                'name': '매도호가수량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem3',
                'length': '	7',
                'name': '매수호가수량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt3',
                'length': '	5',
                'name': '매도호가건수3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt3',
                'length': '	5',
                'name': '매수호가건수3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho4',
                'length': '	10',
                'name': '매도호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho4',
                'length': '	10',
                'name': '매수호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem4',
                'length': '	7',
                'name': '매도호가수량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem4',
                'length': '	7',
                'name': '매수호가수량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt4',
                'length': '	5',
                'name': '매도호가건수4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt4',
                'length': '	5',
                'name': '매수호가건수4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho5',
                'length': '	10',
                'name': '매도호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho5',
                'length': '	10',
                'name': '매수호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem5',
                'length': '	7',
                'name': '매도호가수량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem5',
                'length': '	7',
                'name': '매수호가수량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt5',
                'length': '	5',
                'name': '매도호가건수5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt5',
                'length': '	5',
                'name': '매수호가건수5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho6',
                'length': '	10',
                'name': '매도호가6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho6',
                'length': '	10',
                'name': '매수호가6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem6',
                'length': '	7',
                'name': '매도호가수량6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem6',
                'length': '	7',
                'name': '매수호가수량6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt6',
                'length': '	5',
                'name': '매도호가건수6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt6',
                'length': '	5',
                'name': '매수호가건수6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho7',
                'length': '	10',
                'name': '매도호가7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho7',
                'length': '	10',
                'name': '매수호가7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem7',
                'length': '	7',
                'name': '매도호가수량7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem7',
                'length': '	7',
                'name': '매수호가수량7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt7',
                'length': '	5',
                'name': '매도호가건수7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt7',
                'length': '	5',
                'name': '매수호가건수7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho8',
                'length': '	10',
                'name': '매도호가8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho8',
                'length': '	10',
                'name': '매수호가8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem8',
                'length': '	7',
                'name': '매도호가수량8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem8',
                'length': '	7',
                'name': '매수호가수량8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt8',
                'length': '	5',
                'name': '매도호가건수8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt8',
                'length': '	5',
                'name': '매수호가건수8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho9',
                'length': '	10',
                'name': '매도호가9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho9',
                'length': '	10',
                'name': '매수호가9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem9',
                'length': '	7',
                'name': '매도호가수량9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem9',
                'length': '	7',
                'name': '매수호가수량9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt9',
                'length': '	5',
                'name': '매도호가건수9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt9',
                'length': '	5',
                'name': '매수호가건수9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho10',
                'length': '	10',
                'name': '매도호가10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho10',
                'length': '	10',
                'name': '매수호가10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem10',
                'length': '	7',
                'name': '매도호가수량10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem10',
                'length': '	7',
                'name': '매수호가수량10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt10',
                'length': '	5',
                'name': '매도호가건수10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt10',
                'length': '	5',
                'name': '매수호가건수10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totofferrem',
                'length': '	8',
                'name': '매도호가총수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidrem',
                'length': '	8',
                'name': '매수호가총수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totoffercnt',
                'length': '	5',
                'name': '매도호가총건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidcnt',
                'length': '	5',
                'name': '매수호가총건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'danhochk',
                'length': '	1',
                'name': '단일가호가여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'alloc_gubun',
                'length': '	1',
                'name': '배분적용구분',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'JX0': {
        'tr_cd': 'JX0',
        'title': '주식선물가격제한폭확대',
        'fields': [
            {
                'key': 'upstep',
                'length': '	2',
                'name': '적용상한단계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dnstep',
                'length': '	2',
                'name': '적용하한단계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'uplmtprice',
                'length': '	10',
                'name': '적용상한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dnlmtprice',
                'length': '	10',
                'name': '적용하한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'MMDAQ91200': {
        'tr_cd': 'MMDAQ91200',
        'title': '파생상품증거금율조회',
        'blocks': {
            'MMDAQ91200OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'IsuLgclssCode', 'name': '종목대분류코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'IsuMdclssCode', 'name': '종목중분류코드', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            'MMDAQ91200OutBlock2': {
                'fields': [{'key': 'IsuSmclssCode', 'name': '종목소분류코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'IsuMdclssCode', 'name': '종목중분류코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'IsuLrgMdclssNm', 'name': '종목대중분류명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'IsuLrgMidSmclssNm', 'name': '종목대중소분류명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'ShtnHanglIsuNm', 'name': '단축한글종목명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'CsgnMgnrt', 'name': '위탁증거금율', 'type': 'float', 'length': 26.9, 'required': True}, {'key': 'MaintMgnrt', 'name': '유지증거금율', 'type': 'float', 'length': 26.9, 'required': True}, {'key': 'MnyMgnrt', 'name': '현금증거금율', 'type': 'float', 'length': 26.9, 'required': True}, {'key': 'RmndDays', 'name': '잔여일수', 'type': 'float', 'length': 6, 'required': True}, {'key': 'OnePrcntrOrdMgn', 'name': '1계약당주문증거금', 'type': 'float', 'length': 17, 'required': True}],
                'type': 'array'
            }
        }
    },
    'O01': {
        'tr_cd': 'O01',
        'title': '선물접수',
        'fields': []
    },
    'O02': {
        'tr_cd': 'O02',
        'title': 'KRX야간파생 선물접수',
        'fields': [
            {
                'key': 'lineseq',
                'length': 10,
                'name': '라인일련번호',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'accno',
                'length': 11,
                'name': '계좌번호',
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
                'key': 'len',
                'length': 6,
                'name': '헤더길이',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'gubun',
                'length': 1,
                'name': '헤더구분',
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
                'key': 'encrypt',
                'length': 1,
                'name': '암호구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offset',
                'length': 3,
                'name': '공통시작지점',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'trcode',
                'length': 8,
                'name': 'TRCODE',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'compid',
                'length': 3,
                'name': '이용사번호',
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
                'key': 'media',
                'length': 2,
                'name': '접속매체',
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
                'key': 'seq',
                'length': 9,
                'name': '전문일련번호',
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
                'key': 'pcbpno',
                'length': 3,
                'name': '처리지점번호',
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
                'key': 'termno',
                'length': 8,
                'name': '단말번호',
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
                'key': 'proctm',
                'length': 9,
                'name': 'AP처리시간',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'msgcode',
                'length': 4,
                'name': '메세지코드',
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
                'key': 'compreq',
                'length': 1,
                'name': '압축요청구분',
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
                'key': 'reqcnt',
                'length': 4,
                'name': '요청레코드개수',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'filler',
                'length': 6,
                'name': '예비영역',
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
                'key': 'contkey',
                'length': 18,
                'name': '연속키값',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'varlen',
                'length': 2,
                'name': '가변시스템길이',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'varhdlen',
                'length': 2,
                'name': '가변해더길이',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'varmsglen',
                'length': 2,
                'name': '가변메시지길이',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'trsrc',
                'length': 1,
                'name': '조회발원지',
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
                'key': 'ifinfo',
                'length': 4,
                'name': 'I/F정보',
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
                'key': 'trcode1',
                'length': 4,
                'name': 'tr코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'firmno',
                'length': 3,
                'name': '회사번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'acntno',
                'length': 11,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'acntno1',
                'length': 9,
                'name': '계좌번호',
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
                'key': 'brnno',
                'length': 3,
                'name': '지점번호',
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
                'key': 'ordno1',
                'length': 3,
                'name': '주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordno',
                'length': 7,
                'name': '주문번호',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'orgordno1',
                'length': 3,
                'name': '원주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'orgordno',
                'length': 7,
                'name': '원주문번호',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'prntordno',
                'length': 3,
                'name': '모주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'prntordno1',
                'length': 7,
                'name': '모주문번호',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'isuno',
                'length': 12,
                'name': '종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'fnoIsuno',
                'length': 8,
                'name': '선물옵션종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'fnoIsunm',
                'length': 40,
                'name': '선물옵션종목명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'pdgrpcode',
                'length': 2,
                'name': '상품군분류코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'fnoIsuptntp',
                'length': 1,
                'name': '선물옵션종목유형구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bnstp',
                'length': 1,
                'name': '매매구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mrctp',
                'length': 1,
                'name': '정정취소구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordqty',
                'length': 16,
                'name': '주문수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'hogatype',
                'length': 2,
                'name': '호가유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mmgb',
                'length': 2,
                'name': '거래유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordprc',
                'length': 13.2,
                'name': '주문가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'unercqty',
                'length': 16,
                'name': '미체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'commdacode',
                'length': 2,
                'name': '통신매체',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'peeamtcode',
                'length': 2,
                'name': '수수료합산코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mgempno',
                'length': 9,
                'name': '관리사원',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'fnotrdunitamt',
                'length': 19.8,
                'name': '선물옵션거래단위금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'trxtime',
                'length': 9,
                'name': '처리시각',
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
                'key': 'grpId',
                'length': 20,
                'name': '그룹Id',
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
                'key': 'ptflno',
                'length': 10,
                'name': '포트폴리오번호',
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
                'key': 'trchno',
                'length': 10,
                'name': '트렌치번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'Itemno',
                'length': 10,
                'name': '아이템번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'userId',
                'length': 16,
                'name': '주문자Id',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'opdrtnno',
                'length': 12,
                'name': '운영지시번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'rjtcode',
                'length': 3,
                'name': '부적격코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mrccnfqty',
                'length': 16,
                'name': '정정취소확인수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'orgordunercqty',
                'length': 16,
                'name': '원주문미체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'orgordmrcqty',
                'length': 16,
                'name': '원주문정정취소수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ctrcttime',
                'length': 8,
                'name': '약정시각(체결시각)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ctrctno',
                'length': 10,
                'name': '약정번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'execprc',
                'length': 13.2,
                'name': '체결가격',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'execqty',
                'length': 16,
                'name': '체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'newqty',
                'length': 16,
                'name': '신규체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'qdtqty',
                'length': 16,
                'name': '청산체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'lastqty',
                'length': 16,
                'name': '최종결제수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'lallexecqty',
                'length': 16,
                'name': '전체체결수량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'allexecamt',
                'length': 16,
                'name': '전체체결금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'fnobalevaltp',
                'length': 1,
                'name': '잔고평가구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bnsplamt',
                'length': 16,
                'name': '매매손익금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'fnoIsuno1',
                'length': 8,
                'name': '선물옵션종목번호1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bnstp1',
                'length': 1,
                'name': '매매구분1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'execprc1',
                'length': 13.2,
                'name': '체결가1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'newqty1',
                'length': 16,
                'name': '신규체결수량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'qdtqty1',
                'length': 16,
                'name': '청산체결수량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'allexecamt1',
                'length': 16,
                'name': '전체체결금액1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'fnoIsuno2',
                'length': 8,
                'name': '선물옵션종목번호2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bnstp2',
                'length': 1,
                'name': '매매구분2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'execprc2',
                'length': 13.2,
                'name': '체결가2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'newqty2',
                'length': 16,
                'name': '신규체결수량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'lqdtqty2',
                'length': 16,
                'name': '청산체결수량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'allexecamt2',
                'length': 16,
                'name': '전체체결금액2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'dps',
                'length': 16,
                'name': '예수금',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ftsubtdsgnamt',
                'length': 16,
                'name': '선물대용지정금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mgn',
                'length': 16,
                'name': '증거금',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mnymgn',
                'length': 16,
                'name': '증거금현금',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'ordableamt',
                'length': 16,
                'name': '주문가능금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'mnyordableamt',
                'length': 16,
                'name': '주문가능현금액',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'fnoIsuno_1',
                'length': 8,
                'name': '잔고종목번호1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bnstp_1',
                'length': 1,
                'name': '잔고매매구분1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'unsttqty_1',
                'length': 16,
                'name': '미결제수량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'lqdtableqty_1',
                'length': 16,
                'name': '주문가능수량1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'avrprc_1',
                'length': 13.2,
                'name': '평균가1',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'fnoIsuno_2',
                'length': 8,
                'name': '잔고종목번호2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bnstp_2',
                'length': 1,
                'name': '잔고매매구분2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'unsttqty_2',
                'length': 16,
                'name': '미결제수량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'lqdtableqty_2',
                'length': 16,
                'name': '주문가능수량2',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'avrprc_2',
                'length': 13.2,
                'name': '평균가2',
                'required': True,
                'type': 'float'
            }
        ]
    },
    'OC0': {
        'tr_cd': 'OC0',
        'title': 'KOSPI200옵션체결',
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
                'length': '	6.2',
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
                'length': '	6.2',
                'name': '현재가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'open',
                'length': '	6.2',
                'name': '시가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'high',
                'length': '	6.2',
                'name': '고가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low',
                'length': '	6.2',
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
                'length': '	6',
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
                'key': 'offerho1',
                'length': '	6.2',
                'name': '매도호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho1',
                'length': '	6.2',
                'name': '매수호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'openyak',
                'length': '	8',
                'name': '미결제약정수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'k200jisu',
                'length': '	6.2',
                'name': 'KOSPI200지수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'eqva',
                'length': '	7.2',
                'name': 'KOSPI등가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'theoryprice',
                'length': '	6.2',
                'name': '이론가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'impv',
                'length': '	6.2',
                'name': '내재변동성',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'openyakcha',
                'length': '	8',
                'name': '미결제약정증감',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'timevalue',
                'length': '	6.2',
                'name': '시간가치',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jgubun',
                'length': '	2',
                'name': '장운영정보',
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
                'key': 'optcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'OD0': {
        'tr_cd': 'OD0',
        'title': 'KOSPI200옵션실시간상하한가',
        'fields': [
            {
                'key': 'gubun',
                'length': '	1',
                'name': '접속매매여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_gubun',
                'length': '	1',
                'name': '실시간가격제한여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_uplmtprice',
                'length': '	8.2',
                'name': '실시간상한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dy_dnlmtprice',
                'length': '	8.2',
                'name': '실시간하한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'opttcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'OH0': {
        'tr_cd': 'OH0',
        'title': 'KOSPI200옵션호가',
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
                'length': '	6.2',
                'name': '매도호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho1',
                'length': '	6.2',
                'name': '매수호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem1',
                'length': '	7',
                'name': '매도호가수량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem1',
                'length': '	7',
                'name': '매수호가수량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt1',
                'length': '	5',
                'name': '매도호가건수1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt1',
                'length': '	5',
                'name': '매수호가건수1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho2',
                'length': '	6.2',
                'name': '매도호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho2',
                'length': '	6.2',
                'name': '매수호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem2',
                'length': '	7',
                'name': '매도호가수량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem2',
                'length': '	7',
                'name': '매수호가수량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt2',
                'length': '	5',
                'name': '매도호가건수2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt2',
                'length': '	5',
                'name': '매수호가건수2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho3',
                'length': '	6.2',
                'name': '매도호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho3',
                'length': '	6.2',
                'name': '매수호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem3',
                'length': '	7',
                'name': '매도호가수량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem3',
                'length': '	7',
                'name': '매수호가수량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt3',
                'length': '	5',
                'name': '매도호가건수3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt3',
                'length': '	5',
                'name': '매수호가건수3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho4',
                'length': '	6.2',
                'name': '매도호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho4',
                'length': '	6.2',
                'name': '매수호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem4',
                'length': '	7',
                'name': '매도호가수량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem4',
                'length': '	7',
                'name': '매수호가수량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt4',
                'length': '	5',
                'name': '매도호가건수4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt4',
                'length': '	5',
                'name': '매수호가건수4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho5',
                'length': '	6.2',
                'name': '매도호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho5',
                'length': '	6.2',
                'name': '매수호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem5',
                'length': '	7',
                'name': '매도호가수량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem5',
                'length': '	7',
                'name': '매수호가수량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offercnt5',
                'length': '	5',
                'name': '매도호가건수5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidcnt5',
                'length': '	5',
                'name': '매수호가건수5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totofferrem',
                'length': '	7',
                'name': '매도호가총수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidrem',
                'length': '	7',
                'name': '매수호가총수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totoffercnt',
                'length': '	5',
                'name': '매도호가총건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidcnt',
                'length': '	5',
                'name': '매수호가총건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'optcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'danhochk',
                'length': '	1',
                'name': '단일가호가여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'alloc_gubun',
                'length': '	1',
                'name': '배분적용구분',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'OMG': {
        'tr_cd': 'OMG',
        'title': 'KOSPI200옵션민감도',
        'fields': [
            {
                'key': 'chetime',
                'length': 6,
                'name': '체결시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'actprice',
                'length': '	6.2',
                'name': '행사가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'k200jisu',
                'length': '	6.2',
                'name': 'KOSPI200지수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'fut200jisu',
                'length': '	6.2',
                'name': '선물가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'price',
                'length': '	6.2',
                'name': '현재가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'capimpv',
                'length': '	6.2',
                'name': '대표내재변동성',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'impv',
                'length': '	6.2',
                'name': '내재변동성',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'delt',
                'length': '	7.4',
                'name': '델타(블랙숄즈)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'gama',
                'length': '	7.4',
                'name': '감마(블랙숄즈)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ceta',
                'length': '	7.4',
                'name': '세타(블랙숄즈)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'vega',
                'length': '	7.4',
                'name': '베가(블랙숄즈)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'rhox',
                'length': '	7.4',
                'name': '로우(블랙숄즈)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'theoryprice',
                'length': '	6.2',
                'name': '이론가(블랙숄즈)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bimpv',
                'length': '	6.2',
                'name': '전일가내재변동성',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerimpv',
                'length': '	6.2',
                'name': '매도가내재변동성',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidimpv',
                'length': '	6.2',
                'name': '매수가내재변동성',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'optcode',
                'length': '	8',
                'name': '옵션코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'OX0': {
        'tr_cd': 'OX0',
        'title': 'KOSPI200옵션가격제한폭확대',
        'fields': [
            {
                'key': 'upstep',
                'length': '	2',
                'name': '적용상한단계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dnstep',
                'length': '	2',
                'name': '적용하한단계',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'uplmtprice',
                'length': '	6.2',
                'name': '적용상한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dnlmtprice',
                'length': '	6.2',
                'name': '적용하한가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'opttcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'SC0': {
        'tr_cd': 'SC0',
        'title': '주식주문접수',
        'fields': [
            {
                'key': 'lineseq',
                'length': 10,
                'name': '라인일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'accno',
                'length': 11,
                'name': 'Push키',
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
                'key': 'len',
                'length': 6,
                'name': '헤더길이',
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
                'key': 'compress',
                'length': 1,
                'name': '압축구분',
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
                'key': 'offset',
                'length': 3,
                'name': '공통시작지점',
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
                'key': 'compid',
                'length': 3,
                'name': '이용사번호',
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
                'key': 'media',
                'length': 2,
                'name': '접속매체',
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
                'key': 'seq',
                'length': 9,
                'name': '전문일련번호',
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
                'key': 'pcbpno',
                'length': 3,
                'name': '처리지점번호',
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
                'key': 'termno',
                'length': 8,
                'name': '단말번호',
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
                'key': 'proctm',
                'length': 9,
                'name': 'AP처리시간',
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
                'key': 'outgu',
                'length': 1,
                'name': '메세지출력구분',
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
                'key': 'funckey',
                'length': 4,
                'name': '기능키',
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
                'key': 'filler',
                'length': 6,
                'name': '예비영역',
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
                'key': 'contkey',
                'length': 18,
                'name': '연속키값',
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
                'key': 'varhdlen',
                'length': 2,
                'name': '가변해더길이',
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
                'key': 'trsrc',
                'length': 1,
                'name': '조회발원지',
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
                'key': 'ifinfo',
                'length': 4,
                'name': 'I/F정보',
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
                'desc': '01:주문<br/>02:정정<br/>03:취소<br/>11:체결<br/>12:정정확인<br/>13:취소확인<br/>14:거부<br/>A1:접수중<br/>AC:접수완료<br/>',
                'key': 'ordchegb',
                'length': 2,
                'name': '주문체결구분',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '00:비상장<br/>10:코스피<br/>11:채권<br/>19:장외시장<br/>20:코스닥<br/>23:코넥스<br/>30:프리보드<br/>61:동경거래소<br/>62:JASDAQ<br/>',
                'key': 'marketgb',
                'length': 2,
                'name': '시장구분',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '01:현금매도<br/>02:현금매수<br/>03:신용매도<br/>04:신용매수<br/>05:저축매도<br/>06:저축매수<br/>07:상품매도(대차)<br/>09:상품매도<br/>10:상품매수<br/>11:선물대용매도(일반)<br/>12:선물대용매도(반대)<br/>13:현금매도(프)<br/>14:현금매수(프)<br/>15:현금매수(유가)<br/>16:현금매수(정리)<br/>17:상품매도(대차.프)<br/>19:상품매도(프)<br/>20:상품매수(프)<br/>30:장외매매<br/>',
                'key': 'ordgb',
                'length': 2,
                'name': '주문구분',
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
                'key': 'accno1',
                'length': 11,
                'name': '계좌번호',
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
                'key': 'passwd',
                'length': 8,
                'name': '비밀번호',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '표준코드 12자리<br/>',
                'key': 'expcode',
                'length': 12,
                'name': '종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '주식은 단축코드 앞에 A포함 7자리<br/>ELW는 단촉코드 앞에 J포함 7자리<br/>',
                'key': 'shtcode',
                'length': 9,
                'name': '단축종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'hname',
                'length': 40,
                'name': '종목명',
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
                'key': 'ordprice',
                'length': 13,
                'name': '주문가격',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '0:없음<br/>1:IOC<br/>2:FOK<br/>',
                'key': 'hogagb',
                'length': 1,
                'name': '주문조건',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '00:지정가<br/>03:시장가<br/>05:조건부지정가<br/>06:최유리지정가<br/>07:최우선지정가<br/>09:자사주<br/>10:매입인도(일반)<br/>13:시장가 (IOC)<br/>16:최유리지정가 (IOC)<br/>18:사용안함<br/>20:지정가(임의)<br/>23:시장가(임의)<br/>26:최유리지정가 (FOK)<br/>41:부분충족(프리보드)<br/>42:전량충족(프리보드)<br/>51:장중대량<br/>52:장중바스켓<br/>61:장개시전시간외<br/>62:사용안함<br/>63:경매매<br/>66:장전시간외경쟁대량<br/>67:장개시전시간외대량<br/>68:장개시전시간외바스켓<br/>69:장개시전시간외자사주<br/>71:신고대량전장시가<br/>72:사용안함<br/>73:신고대량종가<br/>76:장중경쟁대량<br/>77:장중대량<br/>78:장중바스켓<br/>79:사용안함<br/>80:매입인도(당일)<br/>81:시간외종가<br/>82:시간외단일가<br/>87:시간외대량<br/>88:바스켓주문<br/>89:시간외자사주<br/>91:자사주스톡옵션<br/>A1:stop order',
                'key': 'etfhogagb',
                'length': 2,
                'name': '호가유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '00:일반<br/>01:지수차익<br/>02:지수비차익<br/>03:주식차익<br/>04:ETF차익(비차익제외)<br/>05:ETF설정(비차익제외)<br/>06:ETF차익(비차익)<br/>07:ETF설정(비차익)<br/>08:DR차익<br/>09:ELW LP헷지<br/>10:ETF LP헷지<br/>11:주식옵션 LP헷지<br/>12:장외파생상품헷지<br/>',
                'key': 'pgmtype',
                'length': 2,
                'name': '프로그램호가구분',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '0:일반<br/>1:차입주식매도<br/>2:기타공매도<br/>',
                'key': 'gmhogagb',
                'length': 1,
                'name': '공매도호가구분',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '0:일반<br/>1:공매도<br/>',
                'key': 'gmhogayn',
                'length': 1,
                'name': '공매도가능여부',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '000:보통<br/>001:유통융자신규<br/>003:자기융자신규<br/>005:유통대주신규<br/>007:자기대주신규<br/>011:미사용<br/>070:매도대금담보융자신규<br/>080:예탁주식담보융자신규<br/>082:예탁채권담보융자신규<br/>101:유통융자상환<br/>103:자기융자상환<br/>105:유통대주상환<br/>107:자기대주상환<br/>111:유통융자전액상환<br/>113:자기융자전액상환<br/>170:매도대금담보융자상환<br/>180:예탁주식담보융자상환<br/>182:예탁채권담보융자상환<br/>188:담보대출전액상환<br/>201:유통융자현금상환<br/>203:자기융자현금상환<br/>205:유통대주현물상환<br/>207:자기대주현물상환<br/>280:예탁주식담보융자현금상환<br/>282:예탁채권담보융자현금상환<br/>301:유통융자현금상환취소<br/>303:자기융자현금상환취소<br/>305:유통대주현물상환취소<br/>307:자기대주현물상환취소<br/>',
                'key': 'singb',
                'length': 3,
                'name': '신용구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'loandt',
                'length': 8,
                'name': '대출일',
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
                'key': 'strtgcode',
                'length': 6,
                'name': '전략코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'groupid',
                'length': 20,
                'name': '그룹ID',
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
                'key': 'prtno',
                'length': 10,
                'name': '포트폴리오번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'basketno',
                'length': 10,
                'name': '바스켓번호',
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
                'key': 'itemno',
                'length': 10,
                'name': '아아템번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'brwmgmyn',
                'length': 1,
                'name': '차입구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mbrno',
                'length': 3,
                'name': '회원사번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'procgb',
                'length': 1,
                'name': '처리구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'admbrchno',
                'length': 3,
                'name': '관리지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'futaccno',
                'length': 20,
                'name': '선물계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'futmarketgb',
                'length': 1,
                'name': '선물상품구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'tongsingb',
                'length': 2,
                'name': '통신매체구분',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '0:해당없음<br/>1:유동성공급자<br/>',
                'key': 'lpgb',
                'length': 1,
                'name': '유동성공급자구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dummy',
                'length': 20,
                'name': 'DUMMY',
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
                'key': 'ordtm',
                'length': 9,
                'name': '주문시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'prntordno',
                'length': 10,
                'name': '모주문번호',
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
                'key': 'orgordundrqty',
                'length': 16,
                'name': '원주문미체결수량',
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
                'key': 'ordordcancelqty',
                'length': 16,
                'name': '원주문취소수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'nmcpysndno',
                'length': 10,
                'name': '비회원사송신번호',
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
                'desc': '1:매도<br/>2:매수<br/>',
                'key': 'bnstp',
                'length': 1,
                'name': '매매구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'spareordno',
                'length': 10,
                'name': '예비주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cvrgseqno',
                'length': 10,
                'name': '반대매매일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'rsvordno',
                'length': 10,
                'name': '예약주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mtordseqno',
                'length': 10,
                'name': '복수주문일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'spareordqty',
                'length': 16,
                'name': '예비주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'orduserid',
                'length': 16,
                'name': '주문사원번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'spotordqty',
                'length': 16,
                'name': '실물주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordruseqty',
                'length': 16,
                'name': '재사용주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mnyordamt',
                'length': 16,
                'name': '현금주문금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordsubstamt',
                'length': 16,
                'name': '주문대용금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ruseordamt',
                'length': 16,
                'name': '재사용주문금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordcmsnamt',
                'length': 16,
                'name': '수수료주문금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'crdtuseamt',
                'length': 16,
                'name': '사용신용담보재사용금',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드<br/>',
                'key': 'secbalqty',
                'length': 16,
                'name': '잔고수량',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드<br/>',
                'key': 'spotordableqty',
                'length': 16,
                'name': '실물가능수량',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드<br/>',
                'key': 'ordableruseqty',
                'length': 16,
                'name': '재사용가능수량(매도)',
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
                'desc': '실서버 데이터 미제공 필드<br/>',
                'key': 'secbalqtyd2',
                'length': 16,
                'name': '잔고수량(D2)',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드<br/>',
                'key': 'sellableqty',
                'length': 16,
                'name': '매도주문가능수량',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드<br/>',
                'key': 'unercsellordqty',
                'length': 16,
                'name': '미체결매도주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드<br/>',
                'key': 'avrpchsprc',
                'length': 13,
                'name': '평균매입가',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '실서버 데이터 미제공 필드<br/>',
                'key': 'pchsamt',
                'length': 16,
                'name': '매입금액',
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
                'key': 'substamt',
                'length': 16,
                'name': '대용금',
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
                'key': 'csgnsubstmgn',
                'length': 16,
                'name': '위탁증거금대용',
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
                'key': 'ordablemny',
                'length': 16,
                'name': '주문가능현금',
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
                'key': 'ruseableamt',
                'length': 16,
                'name': '재사용가능금액',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'SC3': {
        'tr_cd': 'SC3',
        'title': '주식주문취소',
        'fields': []
    },
    'YC3': {
        'tr_cd': 'YC3',
        'title': '상품선물예상체결',
        'fields': [
            {
                'key': 'ychetime',
                'length': '	6',
                'name': '예상체결시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'yeprice',
                'length': '	9.2',
                'name': '예상체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'yevolume',
                'length': '	6',
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
                'length': '	9.2',
                'name': '예상체결가전일종가대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'jnilydrate',
                'length': '	9.2',
                'name': '예상체결가전일종가등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'shcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'YFC': {
        'tr_cd': 'YFC',
        'title': '지수선물예상체결',
        'fields': [
            {
                'key': 'ychetime',
                'length': '	6',
                'name': '예상체결시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'yeprice',
                'length': '	6.2',
                'name': '예상체결가격',
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
                'length': '	6.2',
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
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'expct_ccls_q',
                'length': 9,
                'name': '예상체결수량',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'YJC': {
        'tr_cd': 'YJC',
        'title': '주식선물예상체결',
        'fields': [
            {
                'key': 'ychetime',
                'length': '	6',
                'name': '예상체결시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'yeprice',
                'length': '	10',
                'name': '예상체결가격',
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
                'length': '	10',
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
                'key': 'futcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'expct_ccls_q',
                'length': 9,
                'name': '예상체결수량',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'YOC': {
        'tr_cd': 'YOC',
        'title': '지수옵션예상체결',
        'fields': [
            {
                'key': 'ychetime',
                'length': '	6',
                'name': '예상체결시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'yeprice',
                'length': '	6.2',
                'name': '예상체결가격',
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
                'length': '	6.2',
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
                'key': 'optcode',
                'length': '	8',
                'name': '단축코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'expct_ccls_q',
                'length': 9,
                'name': '예상체결수량',
                'required': True,
                'type': 'string'
            }
        ]
    },
    't0434': {
        'tr_cd': 't0434',
        'title': '선물/옵션체결/미체결',
        'blocks': {
            't0434OutBlock': {
                'fields': [{'key': 'cts_ordno', 'name': 'CTS_주문번호', 'type': 'string', 'length': 7, 'desc': '연속조회키<br/>연속 조회시 이 값을 InBlock의 cts_ordno 필드에 넣어준다.', 'required': True}],
                'type': 'single'
            },
            't0434OutBlock1': {
                'fields': [{'key': 'ordno', 'name': '주문번호', 'type': 'float', 'length': 7, 'required': True}, {'key': 'orgordno', 'name': '원주문번호', 'type': 'float', 'length': 7, 'required': True}, {'key': 'medosu', 'name': '구분', 'type': 'string', 'length': 10, 'required': True}, {'key': 'ordgb', 'name': '유형', 'type': 'string', 'length': 20, 'required': True}, {'key': 'qty', 'name': '주문수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'price', 'name': '주문가격', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'cheqty', 'name': '체결수량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'cheprice', 'name': '체결가격', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'ordrem', 'name': '미체결잔량', 'type': 'float', 'length': 9, 'required': True}, {'key': 'status', 'name': '상태', 'type': 'string', 'length': 10, 'required': True}, {'key': 'ordtime', 'name': '주문시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'ordermtd', 'name': '주문매체', 'type': 'string', 'length': 10, 'required': True}, {'key': 'expcode', 'name': '종목번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'rtcode', 'name': '사유코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'sysprocseq', 'name': '처리순번', 'type': 'float', 'length': 10, 'required': True}, {'key': 'hogatype', 'name': '호가타입', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'array'
            }
        }
    },
    't0441': {
        'tr_cd': 't0441',
        'title': '선물/옵션잔고평가(이동평균)',
        'blocks': {
            't0441OutBlock': {
                'fields': [{'key': 'tdtsunik', 'name': '매매손익합계', 'type': 'float', 'length': 18, 'required': True}, {'key': 'cts_expcode', 'name': 'CTS_종목번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_medocd', 'name': 'CTS_매매구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'tappamt', 'name': '평가금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'tsunik', 'name': '평가손익', 'type': 'float', 'length': 18, 'required': True}],
                'type': 'single'
            },
            't0441OutBlock1': {
                'fields': [{'key': 'expcode', 'name': '종목번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'medosu', 'name': '구분', 'type': 'string', 'length': 4, 'required': True}, {'key': 'jqty', 'name': '잔고수량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'cqty', 'name': '청산가능수량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'pamt', 'name': '평균단가', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'mamt', 'name': '총매입금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'medocd', 'name': '매매구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'dtsunik', 'name': '매매손익', 'type': 'float', 'length': 18, 'required': True}, {'key': 'sysprocseq', 'name': '처리순번', 'type': 'float', 'length': 10, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'appamt', 'name': '평가금액', 'type': 'float', 'length': 18, 'required': True}, {'key': 'dtsunik1', 'name': '평가손익', 'type': 'float', 'length': 18, 'required': True}, {'key': 'sunikrt', 'name': '수익율', 'type': 'float', 'length': 10.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't2101': {
        'tr_cd': 't2101',
        'title': '선물/옵션현재가(시세)조회',
        'blocks': {
            't2101OutBlock': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mgjv', 'name': '미결제량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'mgjvdiff', 'name': '미결제증감', 'type': 'float', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'uplmtprice', 'name': '상한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'dnlmtprice', 'name': '하한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high52w', 'name': '52최고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low52w', 'name': '52최저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'basis', 'name': '베이시스', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'recprice', 'name': '기준가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'theoryprice', 'name': '이론가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'glyl', 'name': '괴리율', 'type': 'float', 'length': 6.3, 'required': True}, {'key': 'cbhprice', 'name': 'CB상한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cblprice', 'name': 'CB하한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'lastmonth', 'name': '만기일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'jandatecnt', 'name': '잔여일', 'type': 'float', 'length': 8, 'required': True}, {'key': 'pricejisu', 'name': '종합지수', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jisusign', 'name': '종합지수전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'jisuchange', 'name': '종합지수전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jisudiff', 'name': '종합지수등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'kospijisu', 'name': 'KOSPI200지수', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'kospisign', 'name': 'KOSPI200전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'kospichange', 'name': 'KOSPI200전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'kospidiff', 'name': 'KOSPI200등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'listhprice', 'name': '상장최고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'listlprice', 'name': '상장최저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'delt', 'name': '델타', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'gama', 'name': '감마', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'ceta', 'name': '세타', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'vega', 'name': '베가', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'rhox', 'name': '로우', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'gmprice', 'name': '근월물현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gmsign', 'name': '근월물전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'gmchange', 'name': '근월물전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gmdiff', 'name': '근월물등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'theorypriceg', 'name': '이론가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'histimpv', 'name': '역사적변동성', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'impv', 'name': '내재변동성', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sbasis', 'name': '시장BASIS', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'ibasis', 'name': '이론BASIS', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gmfutcode', 'name': '근월물종목코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'actprice', 'name': '행사가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'greeks_time', 'name': '거래소민감도수신시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'greeks_confirm', 'name': '거래소민감도확정여부', 'type': 'string', 'length': 8, 'required': True}, {'key': 'danhochk', 'name': '단일가호가여부', 'type': 'string', 'length': 1, 'required': True}, {'key': 'yeprice', 'name': '예상체결가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilysign', 'name': '예상체결가전일종가대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'jnilychange', 'name': '예상체결가전일종가대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilydrate', 'name': '예상체결가전일종가등락율\t', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'alloc_gubun', 'name': '배분구분(1:배분개시2:배분해제0:미발생)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'bjandatecnt', 'name': '잔여일(영업일)', 'type': 'float', 'length': 8, 'required': True}, {'key': 'focode', 'name': '종목코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'dy_gubun', 'name': '실시간가격제한여부(0:대상아님1:적용중2:미적용중3:일시해제)\t', 'type': 'string', 'length': 1, 'required': True}, {'key': 'dy_uplmtprice', 'name': '실시간상한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'dy_dnlmtprice', 'name': '실시간하한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'updnstep_gubun', 'name': '가격제한폭확대(0:미확대1:확대2:대상아님)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'upstep', 'name': '상한적용단계', 'type': 'string', 'length': 2, 'required': True}, {'key': 'dnstep', 'name': '하한적용단계', 'type': 'string', 'length': 2, 'required': True}, {'key': 'uplmtprice_3rd', 'name': '3단계상한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'dnlmtprice_3rd', 'name': '3단계하한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'expct_ccls_q', 'name': '예상체결수량', 'type': 'float', 'length': 9, 'required': True}],
                'type': 'single'
            }
        }
    },
    't2105': {
        'tr_cd': 't2105',
        'title': '선물/옵션현재가호가조회',
        'blocks': {
            't2105OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한<br/>2:상승<br/>3:보합<br/>4:하한<br/>5:하락', 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'stimeqrt', 'name': '거래량전일동시간비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerho1', 'name': '매도호가1', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho1', 'name': '매수호가1', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerrem1', 'name': '매도호가수량1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem1', 'name': '매수호가수량1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt1', 'name': '매도호가건수1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt1', 'name': '매수호가건수1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho2', 'name': '매도호가2', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho2', 'name': '매수호가2', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerrem2', 'name': '매도호가수량2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem2', 'name': '매수호가수량2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt2', 'name': '매도호가건수2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt2', 'name': '매수호가건수2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho3', 'name': '매도호가3', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho3', 'name': '매수호가3', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerrem3', 'name': '매도호가수량3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem3', 'name': '매수호가수량3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt3', 'name': '매도호가건수3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt3', 'name': '매수호가건수3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho4', 'name': '매도호가4', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho4', 'name': '매수호가4', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerrem4', 'name': '매도호가수량4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem4', 'name': '매수호가수량4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt4', 'name': '매도호가건수4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt4', 'name': '매수호가건수4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho5', 'name': '매도호가5', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho5', 'name': '매수호가5', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerrem5', 'name': '매도호가수량5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem5', 'name': '매수호가수량5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt5', 'name': '매도호가건수5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt5', 'name': '매수호가건수5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dvol', 'name': '매도호가총수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'svol', 'name': '매수호가총수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'toffernum', 'name': '총매도호가건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'tbidnum', 'name': '총매수호가건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'time', 'name': '수신시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't2106': {
        'tr_cd': 't2106',
        'title': '선물/옵션현재가시세메모',
        'blocks': {
            't2106OutBlock': {
                'fields': [{'key': 'nrec', 'name': '출력건수', 'type': 'string', 'length': 2, 'desc': 't2106OutBlock1 의 개수', 'required': True}],
                'type': 'single'
            },
            't2106OutBlock1': {
                'fields': [{'key': 'indx', 'name': '인덱스', 'type': 'string', 'length': 1, 'desc': 't2106InBlock1 의 indx와 동일', 'required': True}, {'key': 'gubn', 'name': '조건구분', 'type': 'string', 'length': 1, 'desc': '1:시세 2:최고저가 3:Pivot 4:이동평균선 t2106InBlock1의 gubn과 동일', 'required': True}, {'key': 'vals', 'name': '출력값', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't2201': {
        'tr_cd': 't2201',
        'title': '선물옵션시간대별체결조회',
        'blocks': {
            't2201OutBlock': {
                'fields': [{'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 10, 'desc': '연속조회키 연속 조회시 이 값을 InBlock의 cts_time 필드에 넣어준다.', 'required': True}],
                'type': 'single'
            },
            't2201OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'chdegree', 'name': '체결강도', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'offerho', 'name': '매도호가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho', 'name': '매수호가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'openyak', 'name': '미결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jnilopenupdn', 'name': '미결전일증감', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ibasis', 'name': '이론BASIS', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sbasis', 'name': '시장BASIS', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'kasis', 'name': '괴리율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'j_openupdn', 'name': '미결직전증감', 'type': 'float', 'length': 8, 'required': True}, {'key': 'n_msvolume', 'name': '누적매수체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'n_mdvolume', 'name': '누적매도체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 's_msvolume', 'name': '누적순매수체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'n_mschecnt', 'name': '누적매수체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'n_mdchecnt', 'name': '누적매도체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 's_mschecnt', 'name': '누적순매수체결건수', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't2209': {
        'tr_cd': 't2209',
        'title': '선물옵션틱분별체결조회차트',
        'blocks': {
            't2209OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'openyak', 'name': '미결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'openupdn', 'name': '미결증감', 'type': 'float', 'length': 8, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 's_mschecnt', 'name': '매수순간체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 's_mdchecnt', 'name': '매도순간체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ss_mschecnt', 'name': '순매수순간체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 's_mschevol', 'name': '매수순간체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 's_mdchevol', 'name': '매도순간체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ss_mschevol', 'name': '순매수순간체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'chdegvol', 'name': '체결강도(거래량)', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'chdegcnt', 'name': '체결강도(건수)', 'type': 'float', 'length': 8.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't2210': {
        'tr_cd': 't2210',
        'title': '선물옵션시간대별체결조회(단일출력용)',
        'blocks': {
            't2210OutBlock': {
                'fields': [{'key': 'mdvolume', 'name': '매도체결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'mdchecnt', 'name': '매도체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'msvolume', 'name': '매수체결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'mschecnt', 'name': '매수체결건수', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't2301': {
        'tr_cd': 't2301',
        'title': '옵션전광판',
        'blocks': {
            't2301OutBlock': {
                'fields': [{'key': 'histimpv', 'name': '역사적변동성', 'type': 'float', 'length': 4, 'required': True}, {'key': 'jandatecnt', 'name': '옵션잔존일', 'type': 'float', 'length': 4, 'required': True}, {'key': 'cimpv', 'name': '콜옵션대표IV', 'type': 'float', 'length': 6.3, 'required': True}, {'key': 'pimpv', 'name': '풋옵션대표IV', 'type': 'float', 'length': 6.3, 'required': True}, {'key': 'gmprice', 'name': '근월물현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gmsign', 'name': '근월물전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'gmchange', 'name': '근월물전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gmdiff', 'name': '근월물등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gmvolume', 'name': '근월물거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'gmshcode', 'name': '근월물선물코드', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            },
            't2301OutBlock1': {
                'fields': [{'key': 'actprice', 'name': '행사가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'optcode', 'name': '콜옵션코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'iv', 'name': 'IV', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'mgjv', 'name': '미결제약정', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mgjvupdn', 'name': '미결제약정증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho1', 'name': '매도호가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho1', 'name': '매수호가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'delt', 'name': '델타', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'gama', 'name': '감마', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'vega', 'name': '베가', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'ceta', 'name': '쎄타', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'rhox', 'name': '로우', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'theoryprice', 'name': '이론가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'impv', 'name': '내재가치', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'timevl', 'name': '시간가치', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jvolume', 'name': '잔고수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'parpl', 'name': '평가손익', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jngo', 'name': '청산가능수량', 'type': 'float', 'length': 6, 'required': True}, {'key': 'offerrem1', 'name': '매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem1', 'name': '매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'atmgubun', 'name': 'ATM구분', 'type': 'string', 'length': 1, 'desc': '0:선물 1:ATM 2:ITM 3:OTM', 'required': True}, {'key': 'jisuconv', 'name': '지수환산', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            },
            't2301OutBlock2': {
                'fields': [{'key': 'actprice', 'name': '행사가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'optcode', 'name': '풋옵션코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'iv', 'name': 'IV', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'mgjv', 'name': '미결제약정', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mgjvupdn', 'name': '미결제약정증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho1', 'name': '매도호가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho1', 'name': '매수호가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'delt', 'name': '델타', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'gama', 'name': '감마', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'vega', 'name': '베가', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'ceta', 'name': '쎄타', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'rhox', 'name': '로우', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'theoryprice', 'name': '이론가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'impv', 'name': '내재가치', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'timevl', 'name': '시간가치', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jvolume', 'name': '잔고수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'parpl', 'name': '평가손익', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jngo', 'name': '청산가능수량', 'type': 'float', 'length': 6, 'required': True}, {'key': 'offerrem1', 'name': '매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem1', 'name': '매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'atmgubun', 'name': 'ATM구분', 'type': 'string', 'length': 1, 'desc': '0:선물 1:ATM 2:ITM 3:OTM', 'required': True}, {'key': 'jisuconv', 'name': '지수환산', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't2405': {
        'tr_cd': 't2405',
        'title': '선물옵션호가잔량비율챠트',
        'blocks': {
            't2405OutBlock': {
                'fields': [{'key': 'mdvolume', 'name': '매도체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mdchecnt', 'name': '매도체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'msvolume', 'name': '매수체결수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mschecnt', 'name': '매수체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 6, 'desc': '연속조회키 연속 조회시 이 값을 InBlock의 cts_time 필드에 넣어준다.', 'required': True}],
                'type': 'single'
            },
            't2405OutBlock1': {
                'fields': [{'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho1', 'name': '매도1호가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho1', 'name': '매수1호가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerrem', 'name': '매도수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem', 'name': '매수수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offercnt', 'name': '매도건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidcnt', 'name': '매수건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'c_offerrem', 'name': '매도증감수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'c_bidrem', 'name': '매수증감수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'c_offercnt', 'name': '매도증감건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'c_bidcnt', 'name': '매수증감건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'r_bidrem', 'name': '매수수량비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'r_bidcnt', 'name': '매수건수비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'r_sign', 'name': '매수비율구분', 'type': 'string', 'length': 1, 'desc': '2:매수수량비율 > 100 5:매수수량비율 <= 100', 'required': True}, {'key': 'date', 'name': '일자', 'type': 'long', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't2541': {
        'tr_cd': 't2541',
        'title': '상품선물투자자매매동향(실시간)',
        'blocks': {
            't2541OutBlock': {
                'fields': [{'key': 'eitem', 'name': '상품ID', 'type': 'string', 'length': 2, 'required': True}, {'key': 'sgubun', 'name': '시장구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'cts_time', 'name': 'CTSTIME', 'type': 'string', 'length': 8, 'required': True}, {'key': 'tjjcode_08', 'name': '개인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_08', 'name': '개인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_08', 'name': '개인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_08', 'name': '개인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_08', 'name': '개인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_17', 'name': '외국인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_17', 'name': '외국인매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_17', 'name': '외국인매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_17', 'name': '외국인증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_17', 'name': '외국인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_18', 'name': '기관계투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_18', 'name': '기관계매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_18', 'name': '기관계매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_18', 'name': '기관계증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_18', 'name': '기관계순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_01', 'name': '증권투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_01', 'name': '증권매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_01', 'name': '증권매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_01', 'name': '증권증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_01', 'name': '증권순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_03', 'name': '투신투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_03', 'name': '투신매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_03', 'name': '투신매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_03', 'name': '투신증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_03', 'name': '투신순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_04', 'name': '은행투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_04', 'name': '은행매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_04', 'name': '은행매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_04', 'name': '은행증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_04', 'name': '은행순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_02', 'name': '보험투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_02', 'name': '보험매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_02', 'name': '보험매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_02', 'name': '보험증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_02', 'name': '보험순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_05', 'name': '종금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_05', 'name': '종금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_05', 'name': '종금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_05', 'name': '종금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_05', 'name': '종금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_06', 'name': '기금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_06', 'name': '기금매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_06', 'name': '기금매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_06', 'name': '기금증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_06', 'name': '기금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_07', 'name': '기타투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_07', 'name': '기타매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_07', 'name': '기타매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_07', 'name': '기타증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_07', 'name': '기타순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_11', 'name': '국가투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_11', 'name': '국가매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_11', 'name': '국가매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_11', 'name': '국가증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_11', 'name': '국가순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jjcode_00', 'name': '사모펀드코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'ms_00', 'name': '사모펀드매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'md_00', 'name': '사모펀드매도', 'type': 'float', 'length': 12, 'required': True}, {'key': 'rate_00', 'name': '사모펀드증감', 'type': 'float', 'length': 12, 'required': True}, {'key': 'svolume_00', 'name': '사모펀드순매수', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'single'
            },
            't2541OutBlock1': {
                'fields': [{'key': 'time', 'name': '시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'sv_08', 'name': '개인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_17', 'name': '외국인순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_18', 'name': '기관계순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_01', 'name': '증권순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_03', 'name': '투신순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_04', 'name': '은행순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_02', 'name': '보험순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_05', 'name': '종금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_06', 'name': '기금순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_07', 'name': '기타순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_11', 'name': '국가순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_00', 'name': '사모펀드순매수', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't2545': {
        'tr_cd': 't2545',
        'title': '상품선물투자자매매동향(챠트용)',
        'blocks': {
            't2545OutBlock': {
                'fields': [{'key': 'eitem', 'name': '상품ID', 'type': 'string', 'length': 2, 'required': True}, {'key': 'sgubun', 'name': '시장구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'indcode', 'name': '개인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'forcode', 'name': '외국인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'syscode', 'name': '기관계투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'stocode', 'name': '증권투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'invcode', 'name': '투신투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'bancode', 'name': '은행투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'inscode', 'name': '보험투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'fincode', 'name': '종금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'moncode', 'name': '기금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'etccode', 'name': '기타투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'natcode', 'name': '국가투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'pefcode', 'name': '사모펀드투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'jisucd', 'name': '기준지수코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'jisunm', 'name': '기준지수명', 'type': 'string', 'length': 20, 'required': True}],
                'type': 'single'
            },
            't2545OutBlock1': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'datetime', 'name': '일자시간', 'type': 'string', 'length': 14, 'required': True}, {'key': 'indmsvol', 'name': '개인순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'indmsamt', 'name': '개인순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'formsvol', 'name': '외국인순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'formsamt', 'name': '외국인순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sysmsvol', 'name': '기관계순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sysmsamt', 'name': '기관계순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'stomsvol', 'name': '증권순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'stomsamt', 'name': '증권순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'invmsvol', 'name': '투신순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'invmsamt', 'name': '투신순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'banmsvol', 'name': '은행순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'banmsamt', 'name': '은행순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'insmsvol', 'name': '보험순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'insmsamt', 'name': '보험순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'finmsvol', 'name': '종금순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'finmsamt', 'name': '종금순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'monmsvol', 'name': '기금순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'monmsamt', 'name': '기금순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'etcmsvol', 'name': '기타순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'etcmsamt', 'name': '기타순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'natmsvol', 'name': '국가순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'natmsamt', 'name': '국가순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'pefmsvol', 'name': '사모펀드순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'pefmsamt', 'name': '사모펀드순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'upclose', 'name': '기준지수', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'upcvolume', 'name': '기준체결거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'upvolume', 'name': '기준누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'upvalue', 'name': '기준거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8401': {
        'tr_cd': 't8401',
        'title': '주식선물마스터조회(API용)',
        'blocks': {
            't8401OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'expcode', 'name': '확장코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'basecode', 'name': '기초자산코드', 'type': 'string', 'length': 9, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8402': {
        'tr_cd': 't8402',
        'title': '주식선물현재가조회(API용)',
        'blocks': {
            't8402OutBlock': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'stimeqrt', 'name': '거래량전일동시간비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'mgjv', 'name': '미결제량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'mgjvdiff', 'name': '미결제증감', 'type': 'float', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'uplmtprice', 'name': '상한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dnlmtprice', 'name': '하한가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high52w', 'name': '52최고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low52w', 'name': '52최저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'basis', 'name': '베이시스', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'recprice', 'name': '기준가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'theoryprice', 'name': '이론가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'glyl', 'name': '괴리율', 'type': 'float', 'length': 6.3, 'required': True}, {'key': 'lastmonth', 'name': '만기일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'jandatecnt', 'name': '잔여일', 'type': 'float', 'length': 8, 'required': True}, {'key': 'pricejisu', 'name': '종합지수', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jisusign', 'name': '종합지수전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'jisuchange', 'name': '종합지수전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jisudiff', 'name': '종합지수등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'kospijisu', 'name': 'KOSPI200지수', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'kospisign', 'name': 'KOSPI200전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'kospichange', 'name': 'KOSPI200전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'kospidiff', 'name': 'KOSPI200등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'listhprice', 'name': '상장최고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'listlprice', 'name': '상장최저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'delt', 'name': '델타', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'gama', 'name': '감마', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'ceta', 'name': '세타', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'vega', 'name': '베가', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'rhox', 'name': '로우', 'type': 'float', 'length': 6.4, 'required': True}, {'key': 'gmprice', 'name': '근월물현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'gmsign', 'name': '근월물전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'gmchange', 'name': '근월물전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'gmdiff', 'name': '근월물등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'theorypriceg', 'name': '이론가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'histimpv', 'name': '역사적변동성', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'impv', 'name': '내재변동성', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sbasis', 'name': '시장BASIS', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ibasis', 'name': '이론BASIS', 'type': 'float', 'length': 8, 'required': True}, {'key': 'gmfutcode', 'name': '근월물종목코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'actprice', 'name': '행사가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'shcode', 'name': '기초자산단축코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'basehname', 'name': '기초자산한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'baseprice', 'name': '기초자산현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'basesign', 'name': '기초자산현재가대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'basechange', 'name': '기초자산현재가전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'basediff', 'name': '기초자산등락률', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'basevol', 'name': '기초자산거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'baseprevol', 'name': '기초자산전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'basebidprc', 'name': '기초자산매수호가', 'type': 'float', 'length': 9, 'required': True}, {'key': 'baseaskprc', 'name': '기초자산매도호가', 'type': 'float', 'length': 9, 'required': True}, {'key': 'basefornetbid', 'name': '기초자산외국계회원사순매수', 'type': 'float', 'length': 12, 'required': True}, {'key': 'prodgrp', 'name': '상품군', 'type': 'string', 'length': 20, 'required': True}, {'key': 'mulcnt', 'name': '승수', 'type': 'float', 'length': 12.8, 'required': True}, {'key': 'danhochk', 'name': '단일가호가여부', 'type': 'string', 'length': 1, 'required': True}, {'key': 'yeprice', 'name': '예상체결가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jnilysign', 'name': '예상체결가전일종가대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'jnilychange', 'name': '예상체결가전일종가대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jnilydrate', 'name': '예상체결가전일종가등락율', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8403': {
        'tr_cd': 't8403',
        'title': '주식선물호가조회(API용)',
        'blocks': {
            't8403OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'stimeqrt', 'name': '거래량전일동시간비율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho1', 'name': '매도호가1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho1', 'name': '매수호가1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem1', 'name': '매도호가수량1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem1', 'name': '매수호가수량1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt1', 'name': '매도호가건수1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt1', 'name': '매수호가건수1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho2', 'name': '매도호가2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho2', 'name': '매수호가2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem2', 'name': '매도호가수량2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem2', 'name': '매수호가수량2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt2', 'name': '매도호가건수2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt2', 'name': '매수호가건수2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho3', 'name': '매도호가3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho3', 'name': '매수호가3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem3', 'name': '매도호가수량3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem3', 'name': '매수호가수량3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt3', 'name': '매도호가건수3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt3', 'name': '매수호가건수3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho4', 'name': '매도호가4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho4', 'name': '매수호가4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem4', 'name': '매도호가수량4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem4', 'name': '매수호가수량4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt4', 'name': '매도호가건수4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt4', 'name': '매수호가건수4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho5', 'name': '매도호가5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho5', 'name': '매수호가5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem5', 'name': '매도호가수량5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem5', 'name': '매수호가수량5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt5', 'name': '매도호가건수5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt5', 'name': '매수호가건수5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho6', 'name': '매도호가6', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho6', 'name': '매수호가6', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem6', 'name': '매도호가수량6', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem6', 'name': '매수호가수량6', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt6', 'name': '매도호가건수6', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt6', 'name': '매수호가건수6', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho7', 'name': '매도호가7', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho7', 'name': '매수호가7', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem7', 'name': '매도호가수량7', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem7', 'name': '매수호가수량7', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt7', 'name': '매도호가건수7', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt7', 'name': '매수호가건수7', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho8', 'name': '매도호가8', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho8', 'name': '매수호가8', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem8', 'name': '매도호가수량8', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem8', 'name': '매수호가수량8', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt8', 'name': '매도호가건수8', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt8', 'name': '매수호가건수8', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho9', 'name': '매도호가9', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho9', 'name': '매수호가9', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem9', 'name': '매도호가수량9', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem9', 'name': '매수호가수량9', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt9', 'name': '매도호가건수9', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt9', 'name': '매수호가건수9', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho10', 'name': '매도호가10', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho10', 'name': '매수호가10', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerrem10', 'name': '매도호가수량10', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem10', 'name': '매수호가수량10', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt10', 'name': '매도호가건수10', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt10', 'name': '매수호가건수10', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dvol', 'name': '매도호가총수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'svol', 'name': '매수호가총수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'toffernum', 'name': '총매도호가건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'tbidnum', 'name': '총매수호가건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'time', 'name': '수신시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8404': {
        'tr_cd': 't8404',
        'title': '주식선물시간대별체결조회(API용)',
        'blocks': {
            't8404OutBlock': {
                'fields': [{'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 10, 'desc': '연속조회키 연속 조회시 이 값을 InBlock의 cts_time 필드에 넣어준다.', 'required': True}],
                'type': 'single'
            },
            't8404OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'chdegree', 'name': '체결강도', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'offerho', 'name': '매도호가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidho', 'name': '매수호가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'openyak', 'name': '미결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'jnilopenupdn', 'name': '미결전일증감', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ibasis', 'name': '이론BASIS', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sbasis', 'name': '시장BASIS', 'type': 'float', 'length': 8, 'required': True}, {'key': 'kasis', 'name': '괴리율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'j_openupdn', 'name': '미결직전증감', 'type': 'float', 'length': 8, 'required': True}, {'key': 'n_msvolume', 'name': '누적매수체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'n_mdvolume', 'name': '누적매도체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 's_msvolume', 'name': '누적순매수체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'n_mschecnt', 'name': '누적매수체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'n_mdchecnt', 'name': '누적매도체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 's_mschecnt', 'name': '누적순매수체결건수', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8405': {
        'tr_cd': 't8405',
        'title': '주식선물기간별주가(API용)',
        'blocks': {
            't8405OutBlock': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'desc': '연속조회키 연속 조회시 이 값을 InBlock의 date 필드에 넣어준다.', 'required': True}, {'key': 'cts_code', 'name': 'CTS종목코드', 'type': 'string', 'length': 8, 'desc': '연속조회키 연속 조회시 이 값을 InBlock의 cts_code 필드에 넣어준다.', 'required': True}, {'key': 'lastdate', 'name': '전종목만기일', 'type': 'string', 'length': 8, 'desc': '연속조회키 연속 조회시 이 값을 InBlock의 lastdate 필드에 넣어준다.', 'required': True}, {'key': 'nowfutyn', 'name': '최근월선물여부', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            },
            't8405OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'diff_vol', 'name': '거래증가율', 'type': 'float', 'length': 10.2, 'required': True}, {'key': 'openyak', 'name': '미결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'openyakupdn', 'name': '미결증감', 'type': 'float', 'length': 8, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8406': {
        'tr_cd': 't8406',
        'title': '주식선물틱분별체결조회(API용)',
        'blocks': {
            't8406OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'desc': '1:상한 2:상승 3:보합 4:하한 5:하락', 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 8, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'openyak', 'name': '미결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'openupdn', 'name': '미결증감', 'type': 'float', 'length': 8, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 's_mschecnt', 'name': '매수순간체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 's_mdchecnt', 'name': '매도순간체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ss_mschecnt', 'name': '순매수순간체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 's_mschevol', 'name': '매수순간체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 's_mdchevol', 'name': '매도순간체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ss_mschevol', 'name': '순매수순간체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'chdegvol', 'name': '체결강도(거래량)', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'chdegcnt', 'name': '체결강도(건수)', 'type': 'float', 'length': 8.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8414': {
        'tr_cd': 't8414',
        'title': '선물옵션차트(틱/n틱)',
        'blocks': {
            't8414OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jiclose', 'name': '전일종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'highend', 'name': '상한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'lowend', 'name': '하한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 's_time', 'name': '장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'e_time', 'name': '장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dshmin', 'name': '동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}],
                'type': 'single'
            },
            't8414OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jdiff_vol', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'openyak', 'name': '미결제약정', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8415': {
        'tr_cd': 't8415',
        'title': '선물/옵션차트(N분)',
        'blocks': {
            't8415OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jiclose', 'name': '전일종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'highend', 'name': '상한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'lowend', 'name': '하한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 's_time', 'name': '장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'e_time', 'name': '장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dshmin', 'name': '동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}],
                'type': 'single'
            },
            't8415OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jdiff_vol', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'openyak', 'name': '미결제약정', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8416': {
        'tr_cd': 't8416',
        'title': '선물/옵션차트(일주월)',
        'blocks': {
            't8416OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jiclose', 'name': '전일종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'highend', 'name': '상한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'lowend', 'name': '하한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 's_time', 'name': '장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'e_time', 'name': '장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'dshmin', 'name': '동시호가처리시간(MM:분)', 'type': 'string', 'length': 2, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}],
                'type': 'single'
            },
            't8416OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jdiff_vol', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'openyak', 'name': '미결제약정', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8426': {
        'tr_cd': 't8426',
        'title': '상품선물마스터조회(API용)',
        'blocks': {
            't8426OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'expcode', 'name': '확장코드', 'type': 'string', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8432': {
        'tr_cd': 't8432',
        'title': '지수선물마스터조회API용',
        'blocks': {
            't8432OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'expcode', 'name': '확장코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'uplmtprice', 'name': '상한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'dnlmtprice', 'name': '하한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilhigh', 'name': '전일고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnillow', 'name': '전일저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'recprice', 'name': '기준가', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8433': {
        'tr_cd': 't8433',
        'title': '지수옵션마스터조회API용',
        'blocks': {
            't8433OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'expcode', 'name': '확장코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'hprice', 'name': '상한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'lprice', 'name': '하한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilhigh', 'name': '전일고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnillow', 'name': '전일저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'recprice', 'name': '기준가', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8434': {
        'tr_cd': 't8434',
        'title': '선물/옵션멀티현재가조회',
        'blocks': {
            't8434OutBlock1': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'checnt', 'name': '체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'focode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8435': {
        'tr_cd': 't8435',
        'title': '파생종목마스터조회API용',
        'blocks': {
            't8435OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'expcode', 'name': '확장코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'uplmtprice', 'name': '상한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'dnlmtprice', 'name': '하한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilhigh', 'name': '전일고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnillow', 'name': '전일저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'recprice', 'name': '기준가', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8455': {
        'tr_cd': 't8455',
        'title': 'KRX야간파생 마스터조회(API용)',
        'blocks': {
            't8455OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'shcode', 'name': '종목코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'expcode', 'name': '표준코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'tradeunit', 'name': '거래승수', 'type': 'float', 'length': 21.8, 'required': True}, {'key': 'atmgb', 'name': 'ATM구분(1:ATM2:ITM3:OTM)', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8456': {
        'tr_cd': 't8456',
        'title': 'KRX야간파생 시세조회(API용)',
        'blocks': {
            't8456OutBlock': {
                'fields': [{'key': 'hname', 'name': '한글명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'value', 'name': '거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'recprice', 'name': '기준가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'theoryprice', 'name': '이론가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'actprice', 'name': '행사가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'impv', 'name': '내재가치', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'timevl', 'name': '시간가치', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'kospijisu', 'name': 'KOSPI200지수', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'kospisign', 'name': 'KOSPI200전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'kospichange', 'name': 'KOSPI200전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'kospidiff', 'name': 'KOSPI200등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cmeprice', 'name': 'CME야간선물현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cmesign', 'name': 'CME야간선물전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'cmechange', 'name': 'CME야간선물전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cmediff', 'name': 'CME야간선물등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cmefocode', 'name': 'CME야간선물종목코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'uplmtprice', 'name': '정규장적용상한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'dnlmtprice', 'name': '정규장적용하한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'focode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'yeprice', 'name': '예상체결가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'ysign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'ychange', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'ydiff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'danhochk', 'name': '단일가호가여부', 'type': 'string', 'length': 1, 'required': True}, {'key': 'jnilvolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jnilvalue', 'name': '전일거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'uplmtprice_3rd', 'name': '정규장3단계상한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'dnlmtprice_3rd', 'name': '정규장3단계하한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'ndv_uplmtprice', 'name': '야간장_적용상한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'ndv_dnlmtprice', 'name': '야간장_적용하한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'ndv_rt_uplmtprice', 'name': '야간장_실시간상한가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'ndv_rt_dnlmtprice', 'name': '야간장_실시간하한가', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8457': {
        'tr_cd': 't8457',
        'title': 'KRX야간파생 호가조회(API용)',
        'blocks': {
            't8457OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerho1', 'name': '매도호가1', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho1', 'name': '매수호가1', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerrem1', 'name': '매도호가수량1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem1', 'name': '매수호가수량1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt1', 'name': '매도호가건수1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt1', 'name': '매수호가건수1', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho2', 'name': '매도호가2', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho2', 'name': '매수호가2', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerrem2', 'name': '매도호가수량2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem2', 'name': '매수호가수량2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt2', 'name': '매도호가건수2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt2', 'name': '매수호가건수2', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho3', 'name': '매도호가3', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho3', 'name': '매수호가3', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerrem3', 'name': '매도호가수량3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem3', 'name': '매수호가수량3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt3', 'name': '매도호가건수3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt3', 'name': '매수호가건수3', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho4', 'name': '매도호가4', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho4', 'name': '매수호가4', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerrem4', 'name': '매도호가수량4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem4', 'name': '매수호가수량4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt4', 'name': '매도호가건수4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt4', 'name': '매수호가건수4', 'type': 'float', 'length': 8, 'required': True}, {'key': 'offerho5', 'name': '매도호가5', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho5', 'name': '매수호가5', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerrem5', 'name': '매도호가수량5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'bidrem5', 'name': '매수호가수량5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dcnt5', 'name': '매도호가건수5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'scnt5', 'name': '매수호가건수5', 'type': 'float', 'length': 8, 'required': True}, {'key': 'dvol', 'name': '매도호가총수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'svol', 'name': '매수호가총수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'toffernum', 'name': '총매도호가건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'tbidnum', 'name': '총매수호가건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'time', 'name': '수신시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8458': {
        'tr_cd': 't8458',
        'title': 'KRX야간파생 시간대별체결(API용)',
        'blocks': {
            't8458OutBlock': {
                'fields': [{'key': 'cts_time', 'name': '시간CTS', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'single'
            },
            't8458OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'chdegree', 'name': '체결강도', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'offerho', 'name': '매도호가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho', 'name': '매수호가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'n_msvolume', 'name': '누적매수체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'n_mdvolume', 'name': '누적매도체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 's_msvolume', 'name': '누적순매수체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'n_mschecnt', 'name': '누적매수체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'n_mdchecnt', 'name': '누적매도체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 's_mschecnt', 'name': '누적순매수체결건수', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8459': {
        'tr_cd': 't8459',
        'title': 'KRX야간파생 기간별주가(API용)',
        'blocks': {
            't8459OutBlock': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_code', 'name': 'CTS종목코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'lastdate', 'name': '전종목만기일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'nowfutyn', 'name': '최근월선물여부', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            },
            't8459OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'diff_vol', 'name': '거래증가율', 'type': 'float', 'length': 10.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8460': {
        'tr_cd': 't8460',
        'title': 'KRX야간파생 옵션 전광판',
        'blocks': {
            't8460OutBlock': {
                'fields': [{'key': 'gmprice', 'name': '근월물현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gmsign', 'name': '근월물전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'gmchange', 'name': '근월물전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gmdiff', 'name': '근월물등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'gmvolume', 'name': '근월물거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'gmshcode', 'name': '근월물선물코드', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            },
            't8460OutBlock1': {
                'fields': [{'key': 'actprice', 'name': '행사가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'optcode', 'name': '콜옵션코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho1', 'name': '매도호가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho1', 'name': '매수호가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'impv', 'name': '내재가치', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'timevl', 'name': '시간가치', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerrem1', 'name': '매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem1', 'name': '매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'atmgubun', 'name': 'ATM구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'jisuconv', 'name': '지수환산', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'array'
            },
            't8460OutBlock2': {
                'fields': [{'key': 'actprice', 'name': '행사가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'optcode', 'name': '풋옵션코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerho1', 'name': '매도호가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'bidho1', 'name': '매수호가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'impv', 'name': '내재가치', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'timevl', 'name': '시간가치', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'offerrem1', 'name': '매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidrem1', 'name': '매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'atmgubun', 'name': 'ATM구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'jisuconv', 'name': '지수환산', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8461': {
        'tr_cd': 't8461',
        'title': 'KRX야간파생 틱분별조회(API용)',
        'blocks': {
            't8461OutBlock1': {
                'fields': [{'key': 'chetime', 'name': '시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 8, 'required': True}, {'key': 's_mschecnt', 'name': '매수순간체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 's_mdchecnt', 'name': '매도순간체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 'ss_mschecnt', 'name': '순매수순간체결건수', 'type': 'float', 'length': 8, 'required': True}, {'key': 's_mschevol', 'name': '매수순간체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 's_mdchevol', 'name': '매도순간체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'ss_mschevol', 'name': '순매수순간체결량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'chdegvol', 'name': '체결강도(거래량)', 'type': 'float', 'length': 8.2, 'required': True}, {'key': 'chdegcnt', 'name': '체결강도(건수)', 'type': 'float', 'length': 8.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    't8462': {
        'tr_cd': 't8462',
        'title': 'KRX야간파생 투자자기간별(API용)',
        'blocks': {
            't8462OutBlock': {
                'fields': [{'key': 'tm_rng', 'name': '시간대(D/N/U)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'fot_clsf_cd', 'name': '선물옵션구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'bsc_asts_id', 'name': '기초자산코드', 'type': 'string', 'length': 3, 'required': True}],
                'type': 'single'
            },
            't8462OutBlock1': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'sv_08', 'name': '개인수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_17', 'name': '외국인수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_18', 'name': '기관계수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_01', 'name': '증권수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_03', 'name': '투신수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_04', 'name': '은행수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_02', 'name': '보험수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_05', 'name': '종금수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_06', 'name': '기금수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_07', 'name': '기타수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_15', 'name': '선물수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sv_00', 'name': '사모펀드수량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_08', 'name': '개인금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_17', 'name': '외국인금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_18', 'name': '기관계금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_01', 'name': '증권금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_03', 'name': '투신금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_04', 'name': '은행금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_02', 'name': '보험금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_05', 'name': '종금금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_06', 'name': '기금금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_07', 'name': '기타금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_15', 'name': '선물금액', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sa_00', 'name': '사모펀드금액', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'single'
            }
        }
    },
    't8463': {
        'tr_cd': 't8463',
        'title': 'KRX야간파생 투자자시간대별(API용)',
        'blocks': {
            't8463OutBlock': {
                'fields': [{'key': 'tm_rng', 'name': '시간대(D/N/U)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'fot_clsf_cd', 'name': '선물옵션구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'indcode', 'name': '개인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'forcode', 'name': '외국인투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'syscode', 'name': '기관계투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'stocode', 'name': '증권투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'invcode', 'name': '투신투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'bancode', 'name': '은행투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'inscode', 'name': '보험투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'fincode', 'name': '종금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'moncode', 'name': '기금투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'etccode', 'name': '기타투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'natcode', 'name': '국가투자자코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'pefcode', 'name': '사모펀드투자자코드', 'type': 'string', 'length': 4, 'required': True}],
                'type': 'single'
            },
            't8463OutBlock1': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'datetime', 'name': '일자시간', 'type': 'string', 'length': 14, 'required': True}, {'key': 'bsc_asts_id', 'name': '기초자산코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'indmsvol', 'name': '개인순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'indmsamt', 'name': '개인순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'formsvol', 'name': '외국인순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'formsamt', 'name': '외국인순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'sysmsvol', 'name': '기관계순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'sysmsamt', 'name': '기관계순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'stomsvol', 'name': '증권순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'stomsamt', 'name': '증권순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'invmsvol', 'name': '투신순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'invmsamt', 'name': '투신순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'banmsvol', 'name': '은행순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'banmsamt', 'name': '은행순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'insmsvol', 'name': '보험순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'insmsamt', 'name': '보험순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'finmsvol', 'name': '종금순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'finmsamt', 'name': '종금순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'monmsvol', 'name': '기금순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'monmsamt', 'name': '기금순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'etcmsvol', 'name': '기타순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'etcmsamt', 'name': '기타순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'natmsvol', 'name': '국가순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'natmsamt', 'name': '국가순매수거래대금', 'type': 'float', 'length': 12, 'required': True}, {'key': 'pefmsvol', 'name': '사모펀드순매수거래량', 'type': 'float', 'length': 8, 'required': True}, {'key': 'pefmsamt', 'name': '사모펀드순매수거래대금', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't9943': {
        'tr_cd': 't9943',
        'title': '지수선물마스터조회API용',
        'blocks': {
            't9943OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'expcode', 'name': '확장코드', 'type': 'string', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't9944': {
        'tr_cd': 't9944',
        'title': '지수옵션마스터조회API용',
        'blocks': {
            't9944OutBlock': {
                'fields': [{'key': 'hname', 'name': '종목명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'expcode', 'name': '확장코드', 'type': 'string', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    }
}
