# Auto-generated
from typing import Any, Dict, List

MARKET_OVERSEAS_RESPONSES = {
    'AS0': {
        'tr_cd': 'AS0',
        'title': '해외주식주문접수(미국)',
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
                'key': 'trcode',
                'length': 8,
                'name': 'TRCODE',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'comid',
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
                'key': 'sOrdxctPtnCode',
                'length': 2,
                'name': '주문체결유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdMktCode',
                'length': 2,
                'name': '주문시장코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdPtnCode',
                'length': 2,
                'name': '주문유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdNo',
                'length': 10,
                'name': '원주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAcntNo',
                'length': 20,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sPwd',
                'length': 8,
                'name': '비밀번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sIsuNo',
                'length': 12,
                'name': '종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sShtnIsuNo',
                'length': 9,
                'name': '단축종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sIsuNm',
                'length': 40,
                'name': '종목명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdQty',
                'length': 16,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdPrc',
                'length': 13,
                'name': '주문가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdCndi',
                'length': 1,
                'name': '주문조건',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdprcPtnCode',
                'length': 2,
                'name': '호가유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sStrtgCode',
                'length': 6,
                'name': '전략코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sGrpId',
                'length': 20,
                'name': '그룹ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdSeqno',
                'length': 10,
                'name': '주문회차',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCommdaCode',
                'length': 2,
                'name': '통신매체코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdNo',
                'length': 10,
                'name': '주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdTime',
                'length': 9,
                'name': '주문시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sPrntOrdNo',
                'length': 10,
                'name': '모주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdUnercQty',
                'length': 16,
                'name': '원주문미체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdMdfyQty',
                'length': 16,
                'name': '원주문정정수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdCancQty',
                'length': 16,
                'name': '원주문취소수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sNmcpySndNo',
                'length': 10,
                'name': '비회원사송신번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAmt',
                'length': 16,
                'name': '주문금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sBnsTp',
                'length': 1,
                'name': '매매구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMtiordSeqno',
                'length': 10,
                'name': '복수주문일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdUserId',
                'length': 16,
                'name': '주문사원번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSpotOrdQty',
                'length': 16,
                'name': '실물주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRuseOrdQty',
                'length': 16,
                'name': '재사용주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdMny',
                'length': 16,
                'name': '주문현금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdSubstAmt',
                'length': 16,
                'name': '주문대용금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdRuseAmt',
                'length': 16,
                'name': '주문재사용금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sUseCmsnAmt',
                'length': 16,
                'name': '사용수수료',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSecBalQty',
                'length': 16,
                'name': '잔고수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSpotOrdAbleQty',
                'length': 16,
                'name': '실물주문가능수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAbleRuseQty',
                'length': 16,
                'name': '주문가능재사용수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sFlctQty',
                'length': 16,
                'name': '변동수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSecBalQtyD2',
                'length': 16,
                'name': '잔고수량(D2)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSellAbleQty',
                'length': 16,
                'name': '매도주문가능수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sUnercSellOrdQty',
                'length': 16,
                'name': '미체결매도주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAvrPchsPrc',
                'length': 13,
                'name': '평균매입가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sPchsAmt',
                'length': 16,
                'name': '매입금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sDeposit',
                'length': 16,
                'name': '예수금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSubstAmt',
                'length': 16,
                'name': '대용금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCsgnMnyMgn',
                'length': 16,
                'name': '위탁현금증거금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCsgnSubstMgn',
                'length': 16,
                'name': '위탁대용증거금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAbleMny',
                'length': 16,
                'name': '주문가능현금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAbleSubstAmt',
                'length': 16,
                'name': '주문가능대용금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRuseAbleAmt',
                'length': 16,
                'name': '재사용가능금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMgntrnCode',
                'length': 3,
                'name': '신용거래코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'AS1': {
        'tr_cd': 'AS1',
        'title': '해외주식주문체결(미국)',
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
                'key': 'trcode',
                'length': 8,
                'name': 'TRCODE',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'comid',
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
                'key': 'sOrdxctPtnCode',
                'length': 2,
                'name': '주문체결유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdMktCode',
                'length': 2,
                'name': '주문시장코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdPtnCode',
                'length': 2,
                'name': '주문유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMgmtBrnNo',
                'length': 3,
                'name': '관리지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAcntNo',
                'length': 20,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAcntNm',
                'length': 40,
                'name': '계좌명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sIsuNo',
                'length': 12,
                'name': '종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sIsuNm',
                'length': 40,
                'name': '종목명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdNo',
                'length': 10,
                'name': '주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdNo',
                'length': 10,
                'name': '원주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecNO',
                'length': 10,
                'name': '체결번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAbrdExecId',
                'length': 18,
                'name': '해외체결ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdQty',
                'length': 16,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdPrc',
                'length': 13,
                'name': '주문가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecQty',
                'length': 16,
                'name': '체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecPrc',
                'length': 13,
                'name': '체결가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMdfyCnfQty',
                'length': 16,
                'name': '정정확인수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMdfyCnfPrc',
                'length': 16,
                'name': '정정확인가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCancCnfQty',
                'length': 16,
                'name': '취소확인수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRjtQty',
                'length': 16,
                'name': '거부수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdTrxPtnCode',
                'length': 4,
                'name': '주문처리유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMtiordSeqno',
                'length': 10,
                'name': '복수주문일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdCndi',
                'length': 1,
                'name': '주문조건',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdprcPtnCode',
                'length': 2,
                'name': '호가유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sShtnIsuNo',
                'length': 9,
                'name': '단축종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOpDrtnNo',
                'length': 12,
                'name': '운용지시번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sUnercQty',
                'length': 16,
                'name': '미체결수량(주문)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdUnercQty',
                'length': 16,
                'name': '원주문미체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdMdfyQty',
                'length': 16,
                'name': '원주문정정수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdCancQty',
                'length': 16,
                'name': '원주문취소수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAvrExecPrc',
                'length': 13,
                'name': '주문평균체결가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAmt',
                'length': 16,
                'name': '주문금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sStdIsuNo',
                'length': 12,
                'name': '표준종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sBnsTp',
                'length': 1,
                'name': '매매구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCommdaCode',
                'length': 2,
                'name': '통신매체코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAcntNo',
                'length': 20,
                'name': '주문계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAgrgtBrnNo',
                'length': 3,
                'name': '집계지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRegMktCode',
                'length': 2,
                'name': '등록시장코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMnyMgnRat',
                'length': 7,
                'name': '현금증거금률',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSubstMgnRat',
                'length': 9,
                'name': '대용증거금률',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMnyExecAmt',
                'length': 16,
                'name': '현금체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSubstExecAmt',
                'length': 16,
                'name': '대용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCmsnAmtExecAmt',
                'length': 16,
                'name': '수수료체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sPrdayRuseExecVal',
                'length': 16,
                'name': '전일재사용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCrdayRuseExecVal',
                'length': 16,
                'name': '금일재사용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSpotExecQty',
                'length': 16,
                'name': '실물체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sStslExecQty',
                'length': 16,
                'name': '공매도체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sStrtgCode',
                'length': 6,
                'name': '전략코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sGrpId',
                'length': 20,
                'name': '그룹ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdSeqno',
                'length': 10,
                'name': '주문회차',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdUserId',
                'length': 16,
                'name': '주문자ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecTime',
                'length': 9,
                'name': '체결시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRcptExecTime',
                'length': 9,
                'name': '거래소수신체결시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRjtRsn',
                'length': 8,
                'name': '거부사유',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSecBalQty',
                'length': 16,
                'name': '잔고수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSpotOrdAbleQty',
                'length': 16,
                'name': '실물주문가능수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAbleRuseQty',
                'length': 16,
                'name': '주문가능재사용수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sFlctQty',
                'length': 16,
                'name': '변동수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSecBalQtyD2',
                'length': 16,
                'name': '잔고수량(D2)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSellAbleQty',
                'length': 16,
                'name': '매도주문가능수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sUnercSellOrdQty',
                'length': 16,
                'name': '미체결매도주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAvrPchsPrc',
                'length': 13,
                'name': '평균매입가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sPchsAmt',
                'length': 16,
                'name': '매입금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sDeposit',
                'length': 16,
                'name': '예수금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSubstAmt',
                'length': 16,
                'name': '대용금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCsgnMnyMgn',
                'length': 16,
                'name': '위탁현금증거금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCsgnSubstMgn',
                'length': 16,
                'name': '위탁대용증거금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAbleMny',
                'length': 16,
                'name': '주문가능현금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAbleSubstAmt',
                'length': 16,
                'name': '주문가능대용금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRuseAbleAmt',
                'length': 16,
                'name': '재사용가능금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMgntrnCode',
                'length': 3,
                'name': '신용거래코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'AS2': {
        'tr_cd': 'AS2',
        'title': '해외주식주문정정(미국)',
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
                'key': 'trcode',
                'length': 8,
                'name': 'TRCODE',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'comid',
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
                'key': 'sOrdxctPtnCode',
                'length': 2,
                'name': '주문체결유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdMktCode',
                'length': 2,
                'name': '주문시장코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdPtnCode',
                'length': 2,
                'name': '주문유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMgmtBrnNo',
                'length': 3,
                'name': '관리지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAcntNo',
                'length': 20,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAcntNm',
                'length': 40,
                'name': '계좌명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sIsuNo',
                'length': 12,
                'name': '종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sIsuNm',
                'length': 40,
                'name': '종목명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdNo',
                'length': 10,
                'name': '주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdNo',
                'length': 10,
                'name': '원주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecNO',
                'length': 10,
                'name': '체결번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAbrdExecId',
                'length': 18,
                'name': '해외체결ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdQty',
                'length': 16,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdPrc',
                'length': 13,
                'name': '주문가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecQty',
                'length': 16,
                'name': '체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecPrc',
                'length': 13,
                'name': '체결가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMdfyCnfQty',
                'length': 16,
                'name': '정정확인수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMdfyCnfPrc',
                'length': 16,
                'name': '정정확인가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCancCnfQty',
                'length': 16,
                'name': '취소확인수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRjtQty',
                'length': 16,
                'name': '거부수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdTrxPtnCode',
                'length': 4,
                'name': '주문처리유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMtiordSeqno',
                'length': 10,
                'name': '복수주문일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdCndi',
                'length': 1,
                'name': '주문조건',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdprcPtnCode',
                'length': 2,
                'name': '호가유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sShtnIsuNo',
                'length': 9,
                'name': '단축종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOpDrtnNo',
                'length': 12,
                'name': '운용지시번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sUnercQty',
                'length': 16,
                'name': '미체결수량(주문)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdUnercQty',
                'length': 16,
                'name': '원주문미체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdMdfyQty',
                'length': 16,
                'name': '원주문정정수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdCancQty',
                'length': 16,
                'name': '원주문취소수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAvrExecPrc',
                'length': 13,
                'name': '주문평균체결가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAmt',
                'length': 16,
                'name': '주문금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sStdIsuNo',
                'length': 12,
                'name': '표준종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sBnsTp',
                'length': 1,
                'name': '매매구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCommdaCode',
                'length': 2,
                'name': '통신매체코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAcntNo',
                'length': 20,
                'name': '주문계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAgrgtBrnNo',
                'length': 3,
                'name': '집계지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRegMktCode',
                'length': 2,
                'name': '등록시장코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMnyMgnRat',
                'length': 7,
                'name': '현금증거금률',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSubstMgnRat',
                'length': 9,
                'name': '대용증거금률',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMnyExecAmt',
                'length': 16,
                'name': '현금체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSubstExecAmt',
                'length': 16,
                'name': '대용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCmsnAmtExecAmt',
                'length': 16,
                'name': '수수료체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sPrdayRuseExecVal',
                'length': 16,
                'name': '전일재사용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCrdayRuseExecVal',
                'length': 16,
                'name': '금일재사용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSpotExecQty',
                'length': 16,
                'name': '실물체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sStslExecQty',
                'length': 16,
                'name': '공매도체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sStrtgCode',
                'length': 6,
                'name': '전략코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sGrpId',
                'length': 20,
                'name': '그룹ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdSeqno',
                'length': 10,
                'name': '주문회차',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdUserId',
                'length': 16,
                'name': '주문자ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecTime',
                'length': 9,
                'name': '체결시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRcptExecTime',
                'length': 9,
                'name': '거래소수신체결시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRjtRsn',
                'length': 8,
                'name': '거부사유',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSecBalQty',
                'length': 16,
                'name': '잔고수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSpotOrdAbleQty',
                'length': 16,
                'name': '실물주문가능수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAbleRuseQty',
                'length': 16,
                'name': '주문가능재사용수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sFlctQty',
                'length': 16,
                'name': '변동수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSecBalQtyD2',
                'length': 16,
                'name': '잔고수량(D2)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSellAbleQty',
                'length': 16,
                'name': '매도주문가능수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sUnercSellOrdQty',
                'length': 16,
                'name': '미체결매도주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAvrPchsPrc',
                'length': 13,
                'name': '평균매입가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sPchsAmt',
                'length': 16,
                'name': '매입금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sDeposit',
                'length': 16,
                'name': '예수금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSubstAmt',
                'length': 16,
                'name': '대용금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCsgnMnyMgn',
                'length': 16,
                'name': '위탁현금증거금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCsgnSubstMgn',
                'length': 16,
                'name': '위탁대용증거금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAbleMny',
                'length': 16,
                'name': '주문가능현금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAbleSubstAmt',
                'length': 16,
                'name': '주문가능대용금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRuseAbleAmt',
                'length': 16,
                'name': '재사용가능금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMgntrnCode',
                'length': 3,
                'name': '신용거래코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'AS3': {
        'tr_cd': 'AS3',
        'title': '해외주식주문취소(미국)',
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
                'key': 'trcode',
                'length': 8,
                'name': 'TRCODE',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'comid',
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
                'key': 'sOrdxctPtnCode',
                'length': 2,
                'name': '주문체결유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdMktCode',
                'length': 2,
                'name': '주문시장코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdPtnCode',
                'length': 2,
                'name': '주문유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMgmtBrnNo',
                'length': 3,
                'name': '관리지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAcntNo',
                'length': 20,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAcntNm',
                'length': 40,
                'name': '계좌명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sIsuNo',
                'length': 12,
                'name': '종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sIsuNm',
                'length': 40,
                'name': '종목명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdNo',
                'length': 10,
                'name': '주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdNo',
                'length': 10,
                'name': '원주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecNO',
                'length': 10,
                'name': '체결번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAbrdExecId',
                'length': 18,
                'name': '해외체결ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdQty',
                'length': 16,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdPrc',
                'length': 13,
                'name': '주문가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecQty',
                'length': 16,
                'name': '체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecPrc',
                'length': 13,
                'name': '체결가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMdfyCnfQty',
                'length': 16,
                'name': '정정확인수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMdfyCnfPrc',
                'length': 16,
                'name': '정정확인가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCancCnfQty',
                'length': 16,
                'name': '취소확인수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRjtQty',
                'length': 16,
                'name': '거부수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdTrxPtnCode',
                'length': 4,
                'name': '주문처리유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMtiordSeqno',
                'length': 10,
                'name': '복수주문일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdCndi',
                'length': 1,
                'name': '주문조건',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdprcPtnCode',
                'length': 2,
                'name': '호가유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sShtnIsuNo',
                'length': 9,
                'name': '단축종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOpDrtnNo',
                'length': 12,
                'name': '운용지시번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sUnercQty',
                'length': 16,
                'name': '미체결수량(주문)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdUnercQty',
                'length': 16,
                'name': '원주문미체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdMdfyQty',
                'length': 16,
                'name': '원주문정정수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdCancQty',
                'length': 16,
                'name': '원주문취소수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAvrExecPrc',
                'length': 13,
                'name': '주문평균체결가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAmt',
                'length': 16,
                'name': '주문금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sStdIsuNo',
                'length': 12,
                'name': '표준종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sBnsTp',
                'length': 1,
                'name': '매매구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCommdaCode',
                'length': 2,
                'name': '통신매체코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAcntNo',
                'length': 20,
                'name': '주문계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAgrgtBrnNo',
                'length': 3,
                'name': '집계지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRegMktCode',
                'length': 2,
                'name': '등록시장코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMnyMgnRat',
                'length': 7,
                'name': '현금증거금률',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSubstMgnRat',
                'length': 9,
                'name': '대용증거금률',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMnyExecAmt',
                'length': 16,
                'name': '현금체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSubstExecAmt',
                'length': 16,
                'name': '대용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCmsnAmtExecAmt',
                'length': 16,
                'name': '수수료체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sPrdayRuseExecVal',
                'length': 16,
                'name': '전일재사용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCrdayRuseExecVal',
                'length': 16,
                'name': '금일재사용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSpotExecQty',
                'length': 16,
                'name': '실물체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sStslExecQty',
                'length': 16,
                'name': '공매도체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sStrtgCode',
                'length': 6,
                'name': '전략코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sGrpId',
                'length': 20,
                'name': '그룹ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdSeqno',
                'length': 10,
                'name': '주문회차',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdUserId',
                'length': 16,
                'name': '주문자ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecTime',
                'length': 9,
                'name': '체결시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRcptExecTime',
                'length': 9,
                'name': '거래소수신체결시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRjtRsn',
                'length': 8,
                'name': '거부사유',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSecBalQty',
                'length': 16,
                'name': '잔고수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSpotOrdAbleQty',
                'length': 16,
                'name': '실물주문가능수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAbleRuseQty',
                'length': 16,
                'name': '주문가능재사용수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sFlctQty',
                'length': 16,
                'name': '변동수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSecBalQtyD2',
                'length': 16,
                'name': '잔고수량(D2)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSellAbleQty',
                'length': 16,
                'name': '매도주문가능수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sUnercSellOrdQty',
                'length': 16,
                'name': '미체결매도주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAvrPchsPrc',
                'length': 13,
                'name': '평균매입가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sPchsAmt',
                'length': 16,
                'name': '매입금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sDeposit',
                'length': 16,
                'name': '예수금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSubstAmt',
                'length': 16,
                'name': '대용금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCsgnMnyMgn',
                'length': 16,
                'name': '위탁현금증거금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCsgnSubstMgn',
                'length': 16,
                'name': '위탁대용증거금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAbleMny',
                'length': 16,
                'name': '주문가능현금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAbleSubstAmt',
                'length': 16,
                'name': '주문가능대용금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRuseAbleAmt',
                'length': 16,
                'name': '재사용가능금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMgntrnCode',
                'length': 3,
                'name': '신용거래코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'AS4': {
        'tr_cd': 'AS4',
        'title': '해외주식주문거부(미국)',
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
                'key': 'trcode',
                'length': 8,
                'name': 'TRCODE',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'comid',
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
                'key': 'sOrdxctPtnCode',
                'length': 2,
                'name': '주문체결유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdMktCode',
                'length': 2,
                'name': '주문시장코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdPtnCode',
                'length': 2,
                'name': '주문유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMgmtBrnNo',
                'length': 3,
                'name': '관리지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAcntNo',
                'length': 20,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAcntNm',
                'length': 40,
                'name': '계좌명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sIsuNo',
                'length': 12,
                'name': '종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sIsuNm',
                'length': 40,
                'name': '종목명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdNo',
                'length': 10,
                'name': '주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdNo',
                'length': 10,
                'name': '원주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecNO',
                'length': 10,
                'name': '체결번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAbrdExecId',
                'length': 18,
                'name': '해외체결ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdQty',
                'length': 16,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdPrc',
                'length': 13,
                'name': '주문가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecQty',
                'length': 16,
                'name': '체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecPrc',
                'length': 13,
                'name': '체결가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMdfyCnfQty',
                'length': 16,
                'name': '정정확인수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMdfyCnfPrc',
                'length': 16,
                'name': '정정확인가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCancCnfQty',
                'length': 16,
                'name': '취소확인수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRjtQty',
                'length': 16,
                'name': '거부수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdTrxPtnCode',
                'length': 4,
                'name': '주문처리유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMtiordSeqno',
                'length': 10,
                'name': '복수주문일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdCndi',
                'length': 1,
                'name': '주문조건',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdprcPtnCode',
                'length': 2,
                'name': '호가유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sShtnIsuNo',
                'length': 9,
                'name': '단축종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOpDrtnNo',
                'length': 12,
                'name': '운용지시번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sUnercQty',
                'length': 16,
                'name': '미체결수량(주문)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdUnercQty',
                'length': 16,
                'name': '원주문미체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdMdfyQty',
                'length': 16,
                'name': '원주문정정수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrgOrdCancQty',
                'length': 16,
                'name': '원주문취소수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAvrExecPrc',
                'length': 13,
                'name': '주문평균체결가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAmt',
                'length': 16,
                'name': '주문금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sStdIsuNo',
                'length': 12,
                'name': '표준종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sBnsTp',
                'length': 1,
                'name': '매매구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCommdaCode',
                'length': 2,
                'name': '통신매체코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAcntNo',
                'length': 20,
                'name': '주문계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAgrgtBrnNo',
                'length': 3,
                'name': '집계지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRegMktCode',
                'length': 2,
                'name': '등록시장코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMnyMgnRat',
                'length': 7,
                'name': '현금증거금률',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSubstMgnRat',
                'length': 9,
                'name': '대용증거금률',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sMnyExecAmt',
                'length': 16,
                'name': '현금체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSubstExecAmt',
                'length': 16,
                'name': '대용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCmsnAmtExecAmt',
                'length': 16,
                'name': '수수료체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sPrdayRuseExecVal',
                'length': 16,
                'name': '전일재사용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCrdayRuseExecVal',
                'length': 16,
                'name': '금일재사용체결금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSpotExecQty',
                'length': 16,
                'name': '실물체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sStslExecQty',
                'length': 16,
                'name': '공매도체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sStrtgCode',
                'length': 6,
                'name': '전략코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sGrpId',
                'length': 20,
                'name': '그룹ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdSeqno',
                'length': 10,
                'name': '주문회차',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdUserId',
                'length': 16,
                'name': '주문자ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sExecTime',
                'length': 9,
                'name': '체결시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRcptExecTime',
                'length': 9,
                'name': '거래소수신체결시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sRjtRsn',
                'length': 8,
                'name': '거부사유',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSecBalQty',
                'length': 16,
                'name': '잔고수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSpotOrdAbleQty',
                'length': 16,
                'name': '실물주문가능수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sOrdAbleRuseQty',
                'length': 16,
                'name': '주문가능재사용수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sFlctQty',
                'length': 16,
                'name': '변동수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSecBalQtyD2',
                'length': 16,
                'name': '잔고수량(D2)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSellAbleQty',
                'length': 16,
                'name': '매도주문가능수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sUnercSellOrdQty',
                'length': 16,
                'name': '미체결매도주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sAvrPchsPrc',
                'length': 13,
                'name': '평균매입가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sPchsAmt',
                'length': 16,
                'name': '매입금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sDeposit',
                'length': 16,
                'name': '예수금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sSubstAmt',
                'length': 16,
                'name': '대용금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sCsgnMnyMgn',
                'length': 16,
                'name': '위탁현금증거금액',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'CIDBQ01400': {
        'tr_cd': 'CIDBQ01400',
        'title': '해외선물 체결내역개별 조회(주문가능수량)',
        'blocks': {
            'CIDBQ01400OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'QryTpCode', 'name': '조회구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 18, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OvrsDrvtOrdPrc', 'name': '해외파생주문가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'AbrdFutsOrdPtnCode', 'name': '해외선물주문유형코드', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            },
            'CIDBQ01400OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdAbleQty', 'name': '주문가능수량', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDBQ01500': {
        'tr_cd': 'CIDBQ01500',
        'title': '해외선물 미결제잔고내역 조회',
        'blocks': {
            'CIDBQ01500OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntTpCode', 'name': '계좌구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'FcmAcntNo', 'name': 'FCM계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryDt', 'name': '조회일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'BalTpCode', 'name': '잔고구분코드', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            },
            'CIDBQ01500OutBlock2(Occurs)': {
                'fields': [{'key': 'BaseDt', 'name': '기준일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'Dps', 'name': '예수금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'LpnlAmt', 'name': '청산손익금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'FutsDueBfLpnlAmt', 'name': '선물만기전청산손익금액', 'type': 'float', 'length': 23.2, 'required': True}, {'key': 'FutsDueBfCmsn', 'name': '선물만기전수수료', 'type': 'float', 'length': 23.2, 'required': True}, {'key': 'CsgnMgn', 'name': '위탁증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MaintMgn', 'name': '유지증거금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CtlmtAmt', 'name': '신용한도금액', 'type': 'float', 'length': 23.2, 'required': True}, {'key': 'AddMgn', 'name': '추가증거금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MgnclRat', 'name': '마진콜율', 'type': 'float', 'length': 27.1, 'required': True}, {'key': 'OrdAbleAmt', 'name': '주문가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'WthdwAbleAmt', 'name': '인출가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'CrcyCodeVal', 'name': '통화코드값', 'type': 'string', 'length': 3, 'required': True}, {'key': 'OvrsDrvtPrdtCode', 'name': '해외파생상품코드', 'type': 'string', 'length': 10, 'required': True}, {'key': 'OvrsDrvtOptTpCode', 'name': '해외파생옵션구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'DueDt', 'name': '만기일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OvrsDrvtXrcPrc', 'name': '해외파생행사가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'CmnCodeNm', 'name': '공통코드명', 'type': 'string', 'length': 100, 'required': True}, {'key': 'TpCodeNm', 'name': '구분코드명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'BalQty', 'name': '잔고수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PchsPrc', 'name': '매입가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'OvrsDrvtNowPrc', 'name': '해외파생현재가', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'AbrdFutsEvalPnlAmt', 'name': '해외선물평가손익금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'CsgnCmsn', 'name': '위탁수수료', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'PosNo', 'name': '포지션번호', 'type': 'string', 'length': 13, 'required': True}, {'key': 'EufOneCmsnAmt', 'name': '거래소비용1수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'EufTwoCmsnAmt', 'name': '거래소비용2수수료금액', 'type': 'float', 'length': 19.2, 'required': True}],
                'type': 'array'
            }
        }
    },
    'CIDBQ01800': {
        'tr_cd': 'CIDBQ01800',
        'title': '해외선물 주문내역 조회',
        'blocks': {
            'CIDBQ01800OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'OrdDt', 'name': '주문일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'ThdayTpCode', 'name': '당일구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OrdStatCode', 'name': '주문상태코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'QryTpCode', 'name': '조회구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OrdPtnCode', 'name': '주문유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'OvrsDrvtFnoTpCode', 'name': '해외파생선물옵션구분코드', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            },
            'CIDBQ01800OutBlock2(Occurs)': {
                'fields': [{'key': 'OvrsFutsOrdNo', 'name': '해외선물주문번호', 'type': 'string', 'length': 10, 'required': True}, {'key': 'OvrsFutsOrgOrdNo', 'name': '해외선물원주문번호', 'type': 'string', 'length': 10, 'required': True}, {'key': 'FcmOrdNo', 'name': 'FCM주문번호', 'type': 'string', 'length': 15, 'required': True}, {'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'AbrdFutsXrcPrc', 'name': '해외선물행사가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'FcmAcntNo', 'name': 'FCM계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'BnsTpNm', 'name': '매매구분명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'FutsOrdStatCode', 'name': '선물주문상태코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'TpCodeNm', 'name': '구분코드명', 'type': 'string', 'length': 50, 'desc': '주문, 접수, 확인, 체결, 소멸, 거부', 'required': True}, {'key': 'FutsOrdTpCode', 'name': '선물주문구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'TrdTpNm', 'name': '거래구분명', 'type': 'string', 'length': 20, 'desc': '신규, 정정, 취소, 이관, 수관, 소멸, 장애', 'required': True}, {'key': 'AbrdFutsOrdPtnCode', 'name': '해외선물주문유형코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OrdPtnNm', 'name': '주문유형명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'OrdPtnTermTpCode', 'name': '주문유형기간구분코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'CmnCodeNm', 'name': '공통코드명', 'type': 'string', 'length': 100, 'required': True}, {'key': 'AppSrtDt', 'name': '적용시작일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'AppEndDt', 'name': '적용종료일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OvrsDrvtOrdPrc', 'name': '해외파생주문가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OvrsDrvtExecIsuCode', 'name': '해외파생체결종목코드', 'type': 'string', 'length': 30, 'required': True}, {'key': 'ExecIsuNm', 'name': '체결종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'ExecBnsTpCode', 'name': '체결매매구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'ExecBnsTpNm', 'name': '체결매매구분명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'AbrdFutsExecPrc', 'name': '해외선물체결가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'ExecQty', 'name': '체결수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdCndiPrc', 'name': '주문조건가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'OvrsDrvtNowPrc', 'name': '해외파생현재가', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'MdfyQty', 'name': '정정수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CancQty', 'name': '취소수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'RjtQty', 'name': '거부수량', 'type': 'float', 'length': 13, 'required': True}, {'key': 'CnfQty', 'name': '확인수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'UnercQty', 'name': '미체결수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CvrgYn', 'name': '반대매매여부', 'type': 'string', 'length': 1, 'required': True}, {'key': 'RegTmnlNo', 'name': '등록단말번호', 'type': 'string', 'length': 3, 'required': True}, {'key': 'RegBrnNo', 'name': '등록지점번호', 'type': 'string', 'length': 3, 'required': True}, {'key': 'RegUserId', 'name': '등록사용자ID', 'type': 'string', 'length': 16, 'required': True}, {'key': 'OrdDt', 'name': '주문일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OrdTime', 'name': '주문시각', 'type': 'string', 'length': 9, 'required': True}, {'key': 'OvrsOptXrcRsvTpCode', 'name': '해외옵션행사예약구분코드', 'type': 'string', 'length': 1, 'desc': '1:만기행사', 'required': True}, {'key': 'OvrsDrvtOptTpCode', 'name': '해외파생옵션구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'SprdBaseIsuYn', 'name': '스프레드기준종목여부', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OvrsFutsOrdDt', 'name': '해외선물주문일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OvrsFutsOrdNo2', 'name': '해외선물주문번호2', 'type': 'string', 'length': 10, 'required': True}, {'key': 'OvrsFutsOrgOrdNo2', 'name': '해외선물원주문번호2', 'type': 'string', 'length': 10, 'required': True}, {'key': 'OvrsDrvtIsuCode2', 'name': '해외파생종목코드2', 'type': 'string', 'length': 30, 'required': True}],
                'type': 'array'
            }
        }
    },
    'CIDBQ02400': {
        'tr_cd': 'CIDBQ02400',
        'title': '해외선물 주문체결내역 상세 조회',
        'blocks': {
            'CIDBQ02400OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'QrySrtDt', 'name': '조회시작일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'QryEndDt', 'name': '조회종료일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'ThdayTpCode', 'name': '당일구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OrdStatCode', 'name': '주문상태코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'QryTpCode', 'name': '조회구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OrdPtnCode', 'name': '주문유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'OvrsDrvtFnoTpCode', 'name': '해외파생선물옵션구분코드', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            },
            'CIDBQ02400OutBlock2(Occurs)': {
                'fields': [{'key': 'OrdDt', 'name': '주문일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OvrsFutsOrdNo', 'name': '해외선물주문번호', 'type': 'string', 'length': 10, 'required': True}, {'key': 'OvrsFutsOrgOrdNo', 'name': '해외선물원주문번호', 'type': 'string', 'length': 10, 'required': True}, {'key': 'FcmOrdNo', 'name': 'FCM주문번호', 'type': 'string', 'length': 15, 'required': True}, {'key': 'ExecDt', 'name': '체결일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OvrsFutsExecNo', 'name': '해외선물체결번호', 'type': 'string', 'length': 10, 'required': True}, {'key': 'FcmAcntNo', 'name': 'FCM계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'AbrdFutsXrcPrc', 'name': '해외선물행사가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'desc': '0:전체<br/>1:매도<br/>2:매수', 'required': True}, {'key': 'BnsTpNm', 'name': '매매구분명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'FutsOrdStatCode', 'name': '선물주문상태코드', 'type': 'string', 'length': 1, 'desc': '0:전체<br/>1:체결<br/>2:미체결', 'required': True}, {'key': 'TpCodeNm', 'name': '구분코드명', 'type': 'string', 'length': 50, 'desc': '신규, 정정, 취소, 이관, 수관, 소멸, 장애', 'required': True}, {'key': 'FutsOrdTpCode', 'name': '선물주문구분코드', 'type': 'string', 'length': 1, 'desc': '공백', 'required': True}, {'key': 'TrdTpNm', 'name': '거래구분명', 'type': 'string', 'length': 20, 'desc': '주문, 접수, 확인, 체결, 소멸, 거부', 'required': True}, {'key': 'AbrdFutsOrdPtnCode', 'name': '해외선물주문유형코드', 'type': 'string', 'length': 1, 'desc': '공백', 'required': True}, {'key': 'OrdPtnNm', 'name': '주문유형명', 'type': 'string', 'length': 40, 'desc': '시장가, 지정가, Stop Market, Stop Limit', 'required': True}, {'key': 'OrdPtnTermTpCode', 'name': '주문유형기간구분코드', 'type': 'string', 'length': 2, 'desc': '공백', 'required': True}, {'key': 'CmnCodeNm', 'name': '공통코드명', 'type': 'string', 'length': 100, 'desc': '일반, Spread', 'required': True}, {'key': 'AppSrtDt', 'name': '적용시작일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'AppEndDt', 'name': '적용종료일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OvrsDrvtOrdPrc', 'name': '해외파생주문가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'OvrsDrvtExecIsuCode', 'name': '해외파생체결종목코드', 'type': 'string', 'length': 30, 'required': True}, {'key': 'ExecIsuNm', 'name': '체결종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'ExecBnsTpCode', 'name': '체결매매구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'ExecBnsTpNm', 'name': '체결매매구분명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'ExecQty', 'name': '체결수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'AbrdFutsExecPrc', 'name': '해외선물체결가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'OrdCndiPrc', 'name': '주문조건가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'OvrsDrvtNowPrc', 'name': '해외파생현재가', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'UnercQty', 'name': '미체결수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'TrxStatCode', 'name': '처리상태코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'TrxStatCodeNm', 'name': '처리상태코드명', 'type': 'string', 'length': 40, 'desc': '체결, 체결취소', 'required': True}, {'key': 'CsgnCmsn', 'name': '위탁수수료', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'FcmCmsn', 'name': 'FCM수수료', 'type': 'float', 'length': 21.4, 'required': True}, {'key': 'ThcoCmsn', 'name': '당사수수료', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'MdaCode', 'name': '매체코드', 'type': 'string', 'length': 2, 'desc': '00 창구<br/>22 아이폰<br/>23 안드로이드<br/>41 API<br/>43 로보API<br/>85 HTS<br/>96 최종결제<br/>LP 로스컷<br/>SK CashCall<br/>SO 조건주문', 'required': True}, {'key': 'MdaCodeNm', 'name': '매체코드명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'RegTmnlNo', 'name': '등록단말번호', 'type': 'string', 'length': 3, 'required': True}, {'key': 'RegUserId', 'name': '등록사용자ID', 'type': 'string', 'length': 16, 'required': True}, {'key': 'OrdSndDttm', 'name': '주문발송일시', 'type': 'string', 'length': 17, 'required': True}, {'key': 'ExecDttm', 'name': '체결일시', 'type': 'string', 'length': 17, 'required': True}, {'key': 'EufOneCmsnAmt', 'name': '거래소비용1수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'EufTwoCmsnAmt', 'name': '거래소비용2수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'LchOneCmsnAmt', 'name': '런던청산소1수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'LchTwoCmsnAmt', 'name': '런던청산소2수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'TrdOneCmsnAmt', 'name': '거래1수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'TrdTwoCmsnAmt', 'name': '거래2수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'TrdThreeCmsnAmt', 'name': '거래3수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'StrmOneCmsnAmt', 'name': '단기1수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'StrmTwoCmsnAmt', 'name': '단기2수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'StrmThreeCmsnAmt', 'name': '단기3수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'TransOneCmsnAmt', 'name': '전달1수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'TransTwoCmsnAmt', 'name': '전달2수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'TransThreeCmsnAmt', 'name': '전달3수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'TransFourCmsnAmt', 'name': '전달4수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'OvrsOptXrcRsvTpCode', 'name': '해외옵션행사예약구분코드', 'type': 'string', 'length': 1, 'desc': '1:만기행사', 'required': True}, {'key': 'OvrsDrvtOptTpCode', 'name': '해외파생옵션구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'SprdBaseIsuYn', 'name': '스프레드기준종목여부', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OvrsDrvtIsuCode2', 'name': '해외파생종목코드2', 'type': 'string', 'length': 30, 'required': True}],
                'type': 'array'
            }
        }
    },
    'CIDBQ03000': {
        'tr_cd': 'CIDBQ03000',
        'title': '해외선물 예수금/잔고현황',
        'blocks': {
            'CIDBQ03000OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntTpCode', 'name': '계좌구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'AcntPwd', 'name': '계좌비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'TrdDt', 'name': '거래일자', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            },
            'CIDBQ03000OutBlock2': {
                'fields': [{'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'TrdDt', 'name': '거래일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'CrcyObjCode', 'name': '통화대상코드', 'type': 'string', 'length': 12, 'required': True}, {'key': 'OvrsFutsDps', 'name': '해외선물예수금', 'type': 'float', 'length': 23.2, 'required': True}, {'key': 'CustmMnyioAmt', 'name': '고객입출금금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsLqdtPnlAmt', 'name': '해외선물청산손익금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsCmsnAmt', 'name': '해외선물수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'PrexchDps', 'name': '가환전예수금', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'EvalAssetAmt', 'name': '평가자산금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsCsgnMgn', 'name': '해외선물위탁증거금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsAddMgn', 'name': '해외선물추가증거금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsWthdwAbleAmt', 'name': '해외선물인출가능금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsOrdAbleAmt', 'name': '해외선물주문가능금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsEvalPnlAmt', 'name': '해외선물평가손익금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'LastSettPnlAmt', 'name': '최종결제손익금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'OvrsOptSettAmt', 'name': '해외옵션결제금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'OvrsOptBalEvalAmt', 'name': '해외옵션잔고평가금액', 'type': 'float', 'length': 19.2, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDBQ05300': {
        'tr_cd': 'CIDBQ05300',
        'title': '해외선물 예탁자산 조회',
        'blocks': {
            'CIDBQ05300OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OvrsAcntTpCode', 'name': '해외계좌구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'FcmAcntNo', 'name': 'FCM계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'AcntPwd', 'name': '계좌비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'CrcyCode', 'name': '통화코드', 'type': 'string', 'length': 3, 'required': True}],
                'type': 'single'
            },
            'CIDBQ05300OutBlock2 (Occurs)': {
                'fields': [{'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'CrcyCode', 'name': '통화코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'OvrsFutsDps', 'name': '해외선물예수금', 'type': 'float', 'length': 23.2, 'required': True}, {'key': 'AbrdFutsCsgnMgn', 'name': '해외선물위탁증거금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'OvrsFutsSplmMgn', 'name': '해외선물추가증거금', 'type': 'float', 'length': 23.2, 'required': True}, {'key': 'CustmLpnlAmt', 'name': '고객청산손익금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsEvalPnlAmt', 'name': '해외선물평가손익금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsCmsnAmt', 'name': '해외선물수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsEvalDpstgTotAmt', 'name': '해외선물평가예탁총금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'Xchrat', 'name': '환율', 'type': 'float', 'length': 15.4, 'required': True}, {'key': 'FcurrRealMxchgAmt', 'name': '외화실환전금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsWthdwAbleAmt', 'name': '해외선물인출가능금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsOrdAbleAmt', 'name': '해외선물주문가능금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'FutsDueNarrvLqdtPnlAmt', 'name': '선물만기미도래청산손익금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'FutsDueNarrvCmsn', 'name': '선물만기미도래수수료', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsLqdtPnlAmt', 'name': '해외선물청산손익금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'OvrsFutsDueCmsn', 'name': '해외선물만기수수료', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'OvrsFutsOptBuyAmt', 'name': '해외선물옵션매수금액', 'type': 'float', 'length': 23.2, 'required': True}, {'key': 'OvrsFutsOptSellAmt', 'name': '해외선물옵션매도금액', 'type': 'float', 'length': 23.2, 'required': True}, {'key': 'OptBuyMktWrthAmt', 'name': '옵션매수시장가치금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'OptSellMktWrthAmt', 'name': '옵션매도시장가치금액', 'type': 'float', 'length': 19.2, 'required': True}],
                'type': 'array'
            },
            'CIDBQ05300OutBlock3': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OvrsFutsDps', 'name': '해외선물예수금', 'type': 'float', 'length': 23.2, 'required': True}, {'key': 'AbrdFutsLqdtPnlAmt', 'name': '해외선물청산손익금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'FutsDueNarrvLqdtPnlAmt', 'name': '선물만기미도래청산손익금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsEvalPnlAmt', 'name': '해외선물평가손익금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsEvalDpstgTotAmt', 'name': '해외선물평가예탁총금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'CustmLpnlAmt', 'name': '고객청산손익금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'OvrsFutsDueCmsn', 'name': '해외선물만기수수료', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'FcurrRealMxchgAmt', 'name': '외화실환전금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsCmsnAmt', 'name': '해외선물수수료금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'FutsDueNarrvCmsn', 'name': '선물만기미도래수수료', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsCsgnMgn', 'name': '해외선물위탁증거금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'OvrsFutsMaintMgn', 'name': '해외선물유지증거금', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'OvrsFutsOptBuyAmt', 'name': '해외선물옵션매수금액', 'type': 'float', 'length': 23.2, 'required': True}, {'key': 'OvrsFutsOptSellAmt', 'name': '해외선물옵션매도금액', 'type': 'float', 'length': 23.2, 'required': True}, {'key': 'CtlmtAmt', 'name': '신용한도금액', 'type': 'float', 'length': 23.2, 'required': True}, {'key': 'OvrsFutsSplmMgn', 'name': '해외선물추가증거금', 'type': 'float', 'length': 23.2, 'required': True}, {'key': 'MgnclRat', 'name': '마진콜율', 'type': 'float', 'length': 27.1, 'required': True}, {'key': 'AbrdFutsOrdAbleAmt', 'name': '해외선물주문가능금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'AbrdFutsWthdwAbleAmt', 'name': '해외선물인출가능금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'OptBuyMktWrthAmt', 'name': '옵션매수시장가치금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'OptSellMktWrthAmt', 'name': '옵션매도시장가치금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'OvrsOptSettAmt', 'name': '해외옵션결제금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'OvrsOptBalEvalAmt', 'name': '해외옵션잔고평가금액', 'type': 'float', 'length': 19.2, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDBT00100': {
        'tr_cd': 'CIDBT00100',
        'title': '해외선물 신규주문',
        'blocks': {
            'CIDBT00100OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdDt', 'name': '주문일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'BrnCode', 'name': '지점코드', 'type': 'string', 'length': 7, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'FutsOrdTpCode', 'name': '선물주문구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'AbrdFutsOrdPtnCode', 'name': '해외선물주문유형코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'CrcyCode', 'name': '통화코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'OvrsDrvtOrdPrc', 'name': '해외파생주문가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'CndiOrdPrc', 'name': '조건주문가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PrdtCode', 'name': '상품코드', 'type': 'string', 'length': 6, 'required': True}, {'key': 'DueYymm', 'name': '만기년월', 'type': 'string', 'length': 6, 'required': True}, {'key': 'ExchCode', 'name': '거래소코드', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'single'
            },
            'CIDBT00100OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'OvrsFutsOrdNo', 'name': '해외선물주문번호', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDBT00900': {
        'tr_cd': 'CIDBT00900',
        'title': '해외선물 정정주문',
        'blocks': {
            'CIDBT00900OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdDt', 'name': '주문일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'RegBrnNo', 'name': '등록지점번호', 'type': 'string', 'length': 3, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OvrsFutsOrgOrdNo', 'name': '해외선물원주문번호', 'type': 'string', 'length': 10, 'required': True}, {'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'FutsOrdTpCode', 'name': '선물주문구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'FutsOrdPtnCode', 'name': '선물주문유형코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'CrcyCodeVal', 'name': '통화코드값', 'type': 'string', 'length': 3, 'required': True}, {'key': 'OvrsDrvtOrdPrc', 'name': '해외파생주문가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'CndiOrdPrc', 'name': '조건주문가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OvrsDrvtPrdtCode', 'name': '해외파생상품코드', 'type': 'string', 'length': 10, 'required': True}, {'key': 'DueYymm', 'name': '만기년월', 'type': 'string', 'length': 6, 'required': True}, {'key': 'ExchCode', 'name': '거래소코드', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'single'
            },
            'CIDBT00900OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'OvrsFutsOrdNo', 'name': '해외선물주문번호', 'type': 'string', 'length': 10, 'required': True}, {'key': 'InnerMsgCnts', 'name': '내부메시지내용', 'type': 'string', 'length': 80, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDBT01000': {
        'tr_cd': 'CIDBT01000',
        'title': '해외선물 취소주문',
        'blocks': {
            'CIDBT01000OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdDt', 'name': '주문일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'BrnNo', 'name': '지점번호', 'type': 'string', 'length': 3, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'OvrsFutsOrgOrdNo', 'name': '해외선물원주문번호', 'type': 'string', 'length': 10, 'required': True}, {'key': 'FutsOrdTpCode', 'name': '선물주문구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'PrdtTpCode', 'name': '상품구분코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'ExchCode', 'name': '거래소코드', 'type': 'string', 'length': 10, 'required': True}],
                'type': 'single'
            },
            'CIDBT01000OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'OvrsFutsOrdNo', 'name': '해외선물주문번호', 'type': 'string', 'length': 10, 'required': True}, {'key': 'InnerMsgCnts', 'name': '내부메시지내용', 'type': 'string', 'length': 80, 'required': True}],
                'type': 'single'
            }
        }
    },
    'CIDEQ00800': {
        'tr_cd': 'CIDEQ00800',
        'title': '일자별 미결제 잔고내역',
        'blocks': {
            'CIDEQ00800OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'AcntPwd', 'name': '계좌비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'TrdDt', 'name': '거래일자', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            },
            'CIDEQ00800OutBlock2': {
                'fields': [{'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'TrdDt', 'name': '거래일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'IsuCodeVal', 'name': '종목코드값', 'type': 'string', 'length': 30, 'required': True}, {'key': 'BnsTpNm', 'name': '매매구분명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'BalQty', 'name': '잔고수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'LqdtAbleQty', 'name': '청산가능수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'PchsPrc', 'name': '매입가격', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'OvrsDrvtNowPrc', 'name': '해외파생현재가', 'type': 'float', 'length': 30.11, 'required': True}, {'key': 'AbrdFutsEvalPnlAmt', 'name': '해외선물평가손익금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'CustmBalAmt', 'name': '고객잔고금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'FcurrEvalAmt', 'name': '외화평가금액', 'type': 'float', 'length': 21.4, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'CrcyCodeVal', 'name': '통화코드값', 'type': 'string', 'length': 3, 'required': True}, {'key': 'OvrsDrvtPrdtCode', 'name': '해외파생상품코드', 'type': 'string', 'length': 10, 'required': True}, {'key': 'DueDt', 'name': '만기일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'PrcntrAmt', 'name': '계약당금액', 'type': 'float', 'length': 19.2, 'required': True}, {'key': 'FcurrEvalPnlAmt', 'name': '외화평가손익금액', 'type': 'float', 'length': 21.4, 'required': True}],
                'type': 'single'
            }
        }
    },
    'COSAQ00102': {
        'tr_cd': 'COSAQ00102',
        'title': '해외주식 계좌주문체결내역조회 API',
        'fields': [
            {
                'key': 'COSAQ00102OutBlock1',
                'length': None,
                'name': 'COSAQ00102OutBlock1',
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
                'key': 'QryTpCode',
                'length': 1,
                'name': '조회구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'BkseqTpCode',
                'length': 1,
                'name': '역순구분코드',
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
                'key': 'AcntNo',
                'length': 20,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'Pwd',
                'length': 8,
                'name': '비밀번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'BnsTpCode',
                'length': 1,
                'name': '매매구분코드',
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
                'key': 'SrtOrdNo',
                'length': 10,
                'name': '시작주문번호',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'OrdDt',
                'length': 8,
                'name': '주문일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ExecYn',
                'length': 1,
                'name': '체결여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CrcyCode',
                'length': 3,
                'name': '통화코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ThdayBnsAppYn',
                'length': 1,
                'name': '당일매매적용여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'LoanBalHldYn',
                'length': 1,
                'name': '대출잔고보유여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'COSAQ00102OutBlock2',
                'length': None,
                'name': 'COSAQ00102OutBlock2',
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
                'key': 'AcntNm',
                'length': 40,
                'name': '계좌명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'JpnMktHanglIsuNm',
                'length': 100,
                'name': '일본시장한글종목명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'MgmtBrnNm',
                'length': 40,
                'name': '관리지점명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'SellExecFcurrAmt',
                'length': 21.4,
                'name': '매도체결외화금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'SellExecQty',
                'length': 16,
                'name': '매도체결수량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'BuyExecFcurrAmt',
                'length': 21.4,
                'name': '매수체결외화금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'BuyExecQty',
                'length': 16,
                'name': '매수체결수량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'COSAQ00102OutBlock3',
                'length': None,
                'name': 'COSAQ00102OutBlock3',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'MgmtBrnNo',
                'length': 3,
                'name': '관리지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'AcntNo',
                'length': 20,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'AcntNm',
                'length': 40,
                'name': '계좌명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ExecTime',
                'length': 9,
                'name': '체결시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'OrdTime',
                'length': 9,
                'name': '주문시각',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'OrdNo',
                'length': 10,
                'name': '주문번호',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'OrgOrdNo',
                'length': 10,
                'name': '원주문번호',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'ShtnIsuNo',
                'length': 9,
                'name': '단축종목번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'OrdTrxPtnNm',
                'length': 50,
                'name': '주문처리유형명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'OrdTrxPtnCode',
                'length': 9,
                'name': '주문처리유형코드',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'MrcAbleQty',
                'length': 16,
                'name': '정정취소가능수량',
                'required': True,
                'type': 'long'
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
                'length': 22.7,
                'name': '해외주문가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'ExecQty',
                'length': 16,
                'name': '체결수량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'OvrsExecPrc',
                'length': 28.7,
                'name': '해외체결가',
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
                'key': 'OrdprcPtnNm',
                'length': 40,
                'name': '호가유형명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'OrdPtnNm',
                'length': 40,
                'name': '주문유형명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'OrdPtnCode',
                'length': 2,
                'name': '주문유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'MrcTpCode',
                'length': 1,
                'name': '정정취소구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'MrcTpNm',
                'length': 10,
                'name': '정정취소구분명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'AllExecQty',
                'length': 16,
                'name': '전체체결수량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'CommdaCode',
                'length': 2,
                'name': '통신매체코드',
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
                'key': 'MktNm',
                'length': 40,
                'name': '시장명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CommdaNm',
                'length': 40,
                'name': '통신매체명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'JpnMktHanglIsuNm',
                'length': 100,
                'name': '일본시장한글종목명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'UnercQty',
                'length': 16,
                'name': '미체결수량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'CnfQty',
                'length': 16,
                'name': '확인수량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'CrcyCode',
                'length': 3,
                'name': '통화코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'RegMktCode',
                'length': 2,
                'name': '등록시장코드',
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
                'key': 'BrkTpCode',
                'length': 2,
                'name': '중개인구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'OppBrkNm',
                'length': 40,
                'name': '상대중개인명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'BnsTpCode',
                'length': 1,
                'name': '매매구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'LoanDt',
                'length': 8,
                'name': '대출일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'LoanAmt',
                'length': 16,
                'name': '대출금액',
                'required': True,
                'type': 'long'
            }
        ]
    },
    'COSAQ01400': {
        'tr_cd': 'COSAQ01400',
        'title': '예약주문 처리결과 조회',
        'blocks': {
            'COSAQ01400OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'QryTpCode', 'name': '조회구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'CntryCode', 'name': '국가코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'SrtDt', 'name': '시작일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'EndDt', 'name': '종료일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'BnsTpCode', 'name': '매매구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'RsvOrdCndiCode', 'name': '예약주문조건코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'RsvOrdStatCode', 'name': '예약주문상태코드', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            },
            'COSAQ01400OutBlock2': {
                'fields': [{'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'OrdDt', 'name': '주문일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OrdNo', 'name': '주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'RsvOrdInptDt', 'name': '예약주문입력일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'RsvOrdNo', 'name': '예약주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'ShtnIsuNo', 'name': '단축종목번호', 'type': 'string', 'length': 9, 'required': True}, {'key': 'JpnMktHanglIsuNm', 'name': '일본시장한글종목명', 'type': 'string', 'length': 100, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OrdprcPtnNm', 'name': '호가유형명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'OvrsOrdPrc', 'name': '해외주문가', 'type': 'long', 'length': 28.7, 'required': True}, {'key': 'BnsTpNm', 'name': '매매구분명', 'type': 'string', 'length': 10, 'required': True}, {'key': 'ExecQty', 'name': '체결수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'UnercQty', 'name': '미체결수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'TotExecQty', 'name': '총체결수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'CrcyCode', 'name': '통화코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'RsvOrdStatCode', 'name': '예약주문상태코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'MktTpNm', 'name': '시장구분명', 'type': 'string', 'length': 20, 'required': True}, {'key': 'ErrCnts', 'name': '오류내용', 'type': 'string', 'length': 100, 'required': True}, {'key': 'LoanDt', 'name': '대출일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'MgntrnCode', 'name': '신용거래코드', 'type': 'string', 'length': 3, 'required': True}],
                'type': 'single'
            }
        }
    },
    'COSAT00301': {
        'tr_cd': 'COSAT00301',
        'title': '미국시장주문 API',
        'blocks': {
            'COSAT00301OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdPtnCode', 'name': '주문유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'OrgOrdNo', 'name': '원주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'InptPwd', 'name': '입력비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OrdMktCode', 'name': '주문시장코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'IsuNo', 'name': '종목번호', 'type': 'string', 'length': 12, 'required': True}, {'key': 'OrdQty', 'name': '주문수량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OvrsOrdPrc', 'name': '해외주문가', 'type': 'float', 'length': 28.7, 'required': True}, {'key': 'OrdprcPtnCode', 'name': '호가유형코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'RegCommdaCode', 'name': '등록통신매체코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'BrkTpCode', 'name': '중개인구분코드', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            'COSAT00301OutBlock2': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OrdNo', 'name': '주문번호', 'type': 'float', 'length': 10, 'required': True}, {'key': 'AcntNm', 'name': '계좌명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'IsuNm', 'name': '종목명', 'type': 'string', 'length': 40, 'required': True}],
                'type': 'single'
            }
        }
    },
    'COSAT00311': {
        'tr_cd': 'COSAT00311',
        'title': '미국시장정정주문 API',
        'fields': [
            {
                'key': 'COSAT00311OutBlock1',
                'length': None,
                'name': 'COSAT00311OutBlock1',
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
                'key': 'RegCommdaCode',
                'length': 2,
                'name': '등록통신매체코드',
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
                'key': 'COSAT00311OutBlock2',
                'length': None,
                'name': 'COSAT00311OutBlock2',
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
                'key': 'OrdNo',
                'length': 10,
                'name': '주문번호',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'AcntNm',
                'length': 40,
                'name': '계좌명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'IsuNm',
                'length': 40,
                'name': '종목명',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'COSAT00400': {
        'tr_cd': 'COSAT00400',
        'title': '해외주식 예약주문 등록 및 취소',
        'fields': [
            {
                'key': 'COSAT00400OutBlock1',
                'length': None,
                'name': 'COSAT00400OutBlock1',
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
                'key': 'TrxTpCode',
                'length': 1,
                'name': '처리구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CntryCode',
                'length': 3,
                'name': '국가코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'RsvOrdInptDt',
                'length': 8,
                'name': '예약주문입력일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'RsvOrdNo',
                'length': 10,
                'name': '예약주문번호',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'BnsTpCode',
                'length': 1,
                'name': '매매구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'AcntNo',
                'length': 20,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'Pwd',
                'length': 8,
                'name': '비밀번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'FcurrMktCode',
                'length': 2,
                'name': '외화시장코드',
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
                'key': 'RegCommdaCode',
                'length': 2,
                'name': '등록통신매체코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'OrdprcPtnCode',
                'length': 2,
                'name': '호가유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'RsvOrdSrtDt',
                'length': 8,
                'name': '예약주문시작일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'RsvOrdEndDt',
                'length': 8,
                'name': '예약주문종료일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'RsvOrdCndiCode',
                'length': 2,
                'name': '예약주문조건코드',
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
            },
            {
                'key': 'LoanDtlClssCode',
                'length': 2,
                'name': '대출상세분류코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'COSAT00400OutBlock2',
                'length': None,
                'name': 'COSAT00400OutBlock2',
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
                'key': 'RsvOrdNo',
                'length': 10,
                'name': '예약주문번호',
                'required': True,
                'type': 'long'
            }
        ]
    },
    'COSMT00300': {
        'tr_cd': 'COSMT00300',
        'title': '해외증권 매도상환주문(미국)',
        'fields': [
            {
                'key': 'LoanDtlClssCode',
                'length': 2,
                'name': '대출상세분류코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'COSMT00300OutBlock1',
                'length': None,
                'name': 'COSMT00300OutBlock1',
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
                'key': 'RegCommdaCode',
                'length': 2,
                'name': '등록통신매체코드',
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
            },
            {
                'key': 'LoanDtlClssCode',
                'length': 2,
                'name': '대출상세분류코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'COSMT00300OutBlock2',
                'length': None,
                'name': 'COSMT00300OutBlock2',
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
                'key': 'OrdNo',
                'length': 10,
                'name': '주문번호',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'AcntNm',
                'length': 40,
                'name': '계좌명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'IsuNm',
                'length': 40,
                'name': '종목명',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'COSOQ00201': {
        'tr_cd': 'COSOQ00201',
        'title': '해외주식 종합잔고평가 API',
        'fields': [
            {
                'key': 'COSOQ00201OutBlock1',
                'length': None,
                'name': 'COSOQ00201OutBlock1',
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
                'key': 'AcntNo',
                'length': 20,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'Pwd',
                'length': 8,
                'name': '비밀번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'BaseDt',
                'length': 8,
                'name': '기준일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'CrcyCode',
                'length': 3,
                'name': '통화코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'AstkBalTpCode',
                'length': 2,
                'name': '해외증권잔고구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'COSOQ00201OutBlock2',
                'length': None,
                'name': 'COSOQ00201OutBlock2',
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
                'key': 'ErnRat',
                'length': 18.6,
                'name': '수익율',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'DpsConvEvalAmt',
                'length': 16,
                'name': '예수금환산평가금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'StkConvEvalAmt',
                'length': 16,
                'name': '주식환산평가금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'DpsastConvEvalAmt',
                'length': 16,
                'name': '예탁자산환산평가금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'WonEvalSumAmt',
                'length': 16,
                'name': '원화평가합계금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'ConvEvalPnlAmt',
                'length': 16,
                'name': '환산평가손익금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'WonDpsBalAmt',
                'length': 16,
                'name': '원화예수금잔고금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'D2EstiDps',
                'length': 16,
                'name': 'D2추정예수금',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'LoanAmt',
                'length': 16,
                'name': '대출금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'COSOQ00201OutBlock3',
                'length': None,
                'name': 'COSOQ00201OutBlock3',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'CrcyCode',
                'length': 3,
                'name': '통화코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'FcurrDps',
                'length': 21.4,
                'name': '외화예수금',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'FcurrEvalAmt',
                'length': 21.4,
                'name': '외화평가금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'FcurrEvalPnlAmt',
                'length': 21.4,
                'name': '외화평가손익금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'PnlRat',
                'length': 18.6,
                'name': '손익율',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'BaseXchrat',
                'length': 15.4,
                'name': '기준환율',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'DpsConvEvalAmt',
                'length': 16,
                'name': '예수금환산평가금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'PchsAmt',
                'length': 16,
                'name': '매입금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'StkConvEvalAmt',
                'length': 16,
                'name': '주식환산평가금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'ConvEvalPnlAmt',
                'length': 16,
                'name': '환산평가손익금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'FcurrBuyAmt',
                'length': 21.4,
                'name': '외화매수금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'FcurrOrdAbleAmt',
                'length': 19.2,
                'name': '외화주문가능금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'LoanAmt',
                'length': 16,
                'name': '대출금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'COSOQ00201OutBlock4',
                'length': None,
                'name': 'COSOQ00201OutBlock4',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'CrcyCode',
                'length': 3,
                'name': '통화코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ShtnIsuNo',
                'length': 9,
                'name': '단축종목번호',
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
                'key': 'JpnMktHanglIsuNm',
                'length': 100,
                'name': '일본시장한글종목명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'AstkBalTpCode',
                'length': 2,
                'name': '해외증권잔고구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'AstkBalTpCodeNm',
                'length': 40,
                'name': '해외증권잔고구분코드명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'AstkBalQty',
                'length': 28.6,
                'name': '해외증권잔고수량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'AstkSellAbleQty',
                'length': 28.6,
                'name': '해외증권매도가능수량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'FcstckUprc',
                'length': 24.4,
                'name': '외화증권단가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'FcurrBuyAmt',
                'length': 21.4,
                'name': '외화매수금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'FcstckMktIsuCode',
                'length': 18,
                'name': '외화증권시장종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'OvrsScrtsCurpri',
                'length': 28.7,
                'name': '해외증권시세',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'FcurrEvalAmt',
                'length': 21.4,
                'name': '외화평가금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'FcurrEvalPnlAmt',
                'length': 21.4,
                'name': '외화평가손익금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'PnlRat',
                'length': 18.6,
                'name': '손익율',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'BaseXchrat',
                'length': 15.4,
                'name': '기준환율',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'PchsAmt',
                'length': 16,
                'name': '매입금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'DpsConvEvalAmt',
                'length': 16,
                'name': '예수금환산평가금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'StkConvEvalAmt',
                'length': 16,
                'name': '주식환산평가금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'ConvEvalPnlAmt',
                'length': 16,
                'name': '환산평가손익금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'AstkSettQty',
                'length': 28.6,
                'name': '해외증권결제수량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'MktTpNm',
                'length': 20,
                'name': '시장구분명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'FcurrMktCode',
                'length': 2,
                'name': '외화시장코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'LoanDt',
                'length': 8,
                'name': '대출일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'LoanDtlClssCode',
                'length': 2,
                'name': '대출상세분류코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'LoanAmt',
                'length': 16,
                'name': '대출금액',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'DueDt',
                'length': 8,
                'name': '만기일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'AstkBasePrc',
                'length': 28.6,
                'name': '해외증권기준가격',
                'required': True,
                'type': 'long'
            }
        ]
    },
    'COSOQ02701': {
        'tr_cd': 'COSOQ02701',
        'title': '해외주식 예수금 조회 API',
        'blocks': {
            'COSOQ02701OutBlock1': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'AcntNo', 'name': '계좌번호', 'type': 'string', 'length': 20, 'required': True}, {'key': 'Pwd', 'name': '비밀번호', 'type': 'string', 'length': 8, 'required': True}, {'key': 'CrcyCode', 'name': '통화코드', 'type': 'string', 'length': 3, 'required': True}],
                'type': 'single'
            },
            'COSOQ02701OutBlock2': {
                'fields': [{'key': 'CrcyCode', 'name': '통화코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'FcurrBuyAdjstAmt1', 'name': '외화매수정산금1', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'FcurrBuyAdjstAmt2', 'name': '외화매수정산금2', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'FcurrBuyAdjstAmt3', 'name': '외화매수정산금3', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'FcurrBuyAdjstAmt4', 'name': '외화매수정산금4', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'FcurrSellAdjstAmt1', 'name': '외화매도정산금1', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'FcurrSellAdjstAmt2', 'name': '외화매도정산금2', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'FcurrSellAdjstAmt3', 'name': '외화매도정산금3', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'FcurrSellAdjstAmt4', 'name': '외화매도정산금4', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'PrsmptFcurrDps1', 'name': '추정외화예수금1', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'PrsmptFcurrDps2', 'name': '추정외화예수금2', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'PrsmptFcurrDps3', 'name': '추정외화예수금3', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'PrsmptFcurrDps4', 'name': '추정외화예수금4', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'PrsmptMxchgAbleAmt1', 'name': '추정환전가능금1', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'PrsmptMxchgAbleAmt2', 'name': '추정환전가능금2', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'PrsmptMxchgAbleAmt3', 'name': '추정환전가능금3', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'PrsmptMxchgAbleAmt4', 'name': '추정환전가능금4', 'type': 'float', 'length': 17.4, 'required': True}],
                'type': 'array'
            },
            'COSOQ02701OutBlock3': {
                'fields': [{'key': 'CntryNm', 'name': '국가명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'CrcyCode', 'name': '통화코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'T4FcurrDps', 'name': 'T4외화예수금', 'type': 'float', 'length': 21.4, 'required': True}, {'key': 'FcurrDps', 'name': '외화예수금', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'FcurrOrdAbleAmt', 'name': '외화주문가능금액', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'PrexchOrdAbleAmt', 'name': '가환전주문가능금액', 'type': 'float', 'length': 21.4, 'required': True}, {'key': 'FcurrOrdAmt', 'name': '외화주문금액', 'type': 'float', 'length': 24.4, 'required': True}, {'key': 'FcurrPldgAmt', 'name': '외화담보금액', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'ExecRuseFcurrAmt', 'name': '체결재사용외화금액', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'FcurrMxchgAbleAmt', 'name': '외화환전가능금', 'type': 'float', 'length': 17.4, 'required': True}, {'key': 'BaseXchrat', 'name': '기준환율', 'type': 'float', 'length': 15.4, 'required': True}],
                'type': 'array'
            },
            'COSOQ02701OutBlock4': {
                'fields': [{'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'WonDpsBalAmt', 'name': '원화예수금잔고금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'MnyoutAbleAmt', 'name': '출금가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'WonPrexchAbleAmt', 'name': '원화가환전가능금액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'OvrsMgn', 'name': '해외증거금', 'type': 'float', 'length': 17, 'required': True}, {'key': 'RecCnt', 'name': '레코드갯수', 'type': 'float', 'length': 5, 'required': True}, {'key': 'NrfCode', 'name': '내외국인코드', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            }
        }
    },
    'GSC': {
        'tr_cd': 'GSC',
        'title': '해외주식 체결',
        'fields': [
            {
                'key': 'symbol',
                'length': 16,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ovsdate',
                'length': 8,
                'name': '체결일자(현지)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'kordate',
                'length': 8,
                'name': '체결일자(한국)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'trdtm',
                'length': 6,
                'name': '체결시간(현지)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'kortm',
                'length': 6,
                'name': '체결시간(한국)',
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
                'key': 'price',
                'length': 15.6,
                'name': '체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'diff',
                'length': 15.6,
                'name': '전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'rate',
                'length': 6.2,
                'name': '등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'open',
                'length': 15.6,
                'name': '시가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'high',
                'length': 15.6,
                'name': '고가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low',
                'length': 15.6,
                'name': '저가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'trdq',
                'length': 10,
                'name': '건별체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totq',
                'length': 15,
                'name': '누적체결수량',
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
                'key': 'lSeq',
                'length': 3,
                'name': '초당시퀀스',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'amount',
                'length': 16,
                'name': '누적거래대금',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'high52p',
                'length': 15.6,
                'name': '52주고가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low52p',
                'length': 15.6,
                'name': '52주저가',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'GSH': {
        'tr_cd': 'GSH',
        'title': '해외주식 호가',
        'fields': [
            {
                'key': 'symbol',
                'length': 16,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'loctime',
                'length': 6,
                'name': '현지호가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'kortime',
                'length': 6,
                'name': '한국호가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho1',
                'length': 15.6,
                'name': '매도호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho1',
                'length': 15.6,
                'name': '매수호가1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem1',
                'length': 10,
                'name': '매도호가잔량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem1',
                'length': 10,
                'name': '매수호가잔량1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno1',
                'length': 10,
                'name': '매도호가건수1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno1',
                'length': 10,
                'name': '매수호가건수1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho2',
                'length': 15.6,
                'name': '매도호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho2',
                'length': 15.6,
                'name': '매수호가2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem2',
                'length': 10,
                'name': '매도호가잔량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem2',
                'length': 10,
                'name': '매수호가잔량2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno2',
                'length': 10,
                'name': '매도호가건수2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno2',
                'length': 10,
                'name': '매수호가건수2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho3',
                'length': 15.6,
                'name': '매도호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho3',
                'length': 15.6,
                'name': '매수호가3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem3',
                'length': 10,
                'name': '매도호가잔량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem3',
                'length': 10,
                'name': '매수호가잔량3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno3',
                'length': 10,
                'name': '매도호가건수3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno3',
                'length': 10,
                'name': '매수호가건수3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho4',
                'length': 15.6,
                'name': '매도호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho4',
                'length': 15.6,
                'name': '매수호가4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem4',
                'length': 10,
                'name': '매도호가잔량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem4',
                'length': 10,
                'name': '매수호가잔량4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno4',
                'length': 10,
                'name': '매도호가건수4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno4',
                'length': 10,
                'name': '매수호가건수4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho5',
                'length': 15.6,
                'name': '매도호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho5',
                'length': 15.6,
                'name': '매수호가5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem5',
                'length': 10,
                'name': '매도호가잔량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem5',
                'length': 10,
                'name': '매수호가잔량5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno5',
                'length': 10,
                'name': '매도호가건수5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno5',
                'length': 10,
                'name': '매수호가건수5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho6',
                'length': 15.6,
                'name': '매도호가6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho6',
                'length': 15.6,
                'name': '매수호가6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem6',
                'length': 10,
                'name': '매도호가잔량6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem6',
                'length': 10,
                'name': '매수호가잔량6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno6',
                'length': 10,
                'name': '매도호가건수6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno6',
                'length': 10,
                'name': '매수호가건수6',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho7',
                'length': 15.6,
                'name': '매도호가7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho7',
                'length': 15.6,
                'name': '매수호가7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem7',
                'length': 10,
                'name': '매도호가잔량7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem7',
                'length': 10,
                'name': '매수호가잔량7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno7',
                'length': 10,
                'name': '매도호가건수7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno7',
                'length': 10,
                'name': '매수호가건수7',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho8',
                'length': 15.6,
                'name': '매도호가8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho8',
                'length': 15.6,
                'name': '매수호가8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem8',
                'length': 10,
                'name': '매도호가잔량8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem8',
                'length': 10,
                'name': '매수호가잔량8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno8',
                'length': 10,
                'name': '매도호가건수8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno8',
                'length': 10,
                'name': '매수호가건수8',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho9',
                'length': 15.6,
                'name': '매도호가9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho9',
                'length': 15.6,
                'name': '매수호가9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem9',
                'length': 10,
                'name': '매도호가잔량9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem9',
                'length': 10,
                'name': '매수호가잔량9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno9',
                'length': 10,
                'name': '매도호가건수9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno9',
                'length': 10,
                'name': '매수호가건수9',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho10',
                'length': 15.6,
                'name': '매도호가10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho10',
                'length': 15.6,
                'name': '매수호가10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem10',
                'length': 10,
                'name': '매도호가잔량10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem10',
                'length': 10,
                'name': '매수호가잔량10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno10',
                'length': 10,
                'name': '매도호가건수10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno10',
                'length': 10,
                'name': '매수호가건수10',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totoffercnt',
                'length': 10,
                'name': '매도호가총건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidcnt',
                'length': 10,
                'name': '매수호가총건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totofferrem',
                'length': 10,
                'name': '매도호가총수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidrem',
                'length': 10,
                'name': '매수호가총수량',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'OVC': {
        'tr_cd': 'OVC',
        'title': '해외선물 체결',
        'fields': [
            {
                'key': 'symbol',
                'length': 8,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ovsdate',
                'length': 8,
                'name': '체결일자(현지)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'kordate',
                'length': 8,
                'name': '체결일자(한국)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'trdtm',
                'length': 6,
                'name': '체결시간(현지)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'kortm',
                'length': 6,
                'name': '체결시간(한국)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'curpr',
                'length': 15.9,
                'name': '체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ydiffpr',
                'length': 15.9,
                'name': '전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ydiffSign',
                'length': 1,
                'name': '전일대비기호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'open',
                'length': 15.9,
                'name': '시가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'high',
                'length': 15.9,
                'name': '고가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low',
                'length': 15.9,
                'name': '저가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'chgrate',
                'length': 6.2,
                'name': '등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'trdq',
                'length': 10,
                'name': '건별체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totq',
                'length': 15,
                'name': '누적체결수량',
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
                'key': 'mdvolume',
                'length': 15,
                'name': '매도누적체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume',
                'length': 15,
                'name': '매수누적체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ovsmkend',
                'length': 8,
                'name': '장마감일',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'OVH': {
        'tr_cd': 'OVH',
        'title': '해외선물 호가',
        'fields': [
            {
                'key': 'symbol',
                'length': 8,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'hotime',
                'length': 6,
                'name': '호가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho1',
                'length': 15.9,
                'name': '매도호가 1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho1',
                'length': 15.9,
                'name': '매수호가 1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem1',
                'length': 10,
                'name': '매도호가 잔량 1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem1',
                'length': 10,
                'name': '매수호가 잔량 1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno1',
                'length': 10,
                'name': '매도호가 건수 1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno1',
                'length': 10,
                'name': '매수호가 건수 1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho2',
                'length': 15.9,
                'name': '매도호가 2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho2',
                'length': 15.9,
                'name': '매수호가 2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem2',
                'length': 10,
                'name': '매도호가 잔량 2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem2',
                'length': 10,
                'name': '매수호가 잔량 2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno2',
                'length': 10,
                'name': '매도호가 건수 2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno2',
                'length': 10,
                'name': '매수호가 건수 2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho3',
                'length': 15.9,
                'name': '매도호가 3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho3',
                'length': 15.9,
                'name': '매수호가 3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem3',
                'length': 10,
                'name': '매도호가 잔량 3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem3',
                'length': 10,
                'name': '매수호가 잔량 3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno3',
                'length': 10,
                'name': '매도호가 건수 3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno3',
                'length': 10,
                'name': '매수호가 건수 3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho4',
                'length': 15.9,
                'name': '매도호가 4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho4',
                'length': 15.9,
                'name': '매수호가 4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem4',
                'length': 10,
                'name': '매도호가 잔량 4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem4',
                'length': 10,
                'name': '매수호가 잔량 4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno4',
                'length': 10,
                'name': '매도호가 건수 4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno4',
                'length': 10,
                'name': '매수호가 건수 4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho5',
                'length': 15.9,
                'name': '매도호가 5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho5',
                'length': 15.9,
                'name': '매수호가 5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem5',
                'length': 10,
                'name': '매도호가 잔량 5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem5',
                'length': 10,
                'name': '매수호가 잔량 5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno5',
                'length': 10,
                'name': '매도호가 건수 5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno5',
                'length': 10,
                'name': '매수호가 건수 5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totoffercnt',
                'length': 10,
                'name': '매도호가총건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidcnt',
                'length': 10,
                'name': '매수호가총건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totofferrem',
                'length': 10,
                'name': '매도호가총수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidrem',
                'length': 10,
                'name': '매수호가총수량',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TC1': {
        'tr_cd': 'TC1',
        'title': '해외선물 주문접수',
        'fields': [
            {
                'key': 'lineseq',
                'length': 10,
                'name': '라인일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'key',
                'length': 11,
                'name': 'KEY',
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
                'desc': 'HO01:주문ACK<br/>HO04:주문Pending',
                'key': 'svc_id',
                'length': 4,
                'name': '서비스ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_dt',
                'length': 8,
                'name': '주문일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'brn_cd',
                'length': 3,
                'name': '지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_no',
                'length': 10,
                'name': '주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'orgn_ordr_no',
                'length': 10,
                'name': '원주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mthr_ordr_no',
                'length': 10,
                'name': '모주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ac_no',
                'length': 11,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'is_cd',
                'length': 30,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '1:매도<br/>2:매수',
                'key': 's_b_ccd',
                'length': 1,
                'name': '매도매수유형',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '1:신규<br/>2:정정<br/>3:취소',
                'key': 'ordr_ccd',
                'length': 1,
                'name': '정정취소유형',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '1:시장가<br/>2:지정가<br/>3:Stop Market<br/>4:Stop Limit',
                'key': 'ordr_typ_cd',
                'length': 1,
                'name': '주문유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '01:일반<br/>02:Average<br/>03:Spread',
                'key': 'ordr_typ_prd_ccd',
                'length': 2,
                'name': '주문기간코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_aplc_strt_dt',
                'length': 8,
                'name': '주문적용시작일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_aplc_end_dt',
                'length': 8,
                'name': '주문적용종료일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_prc',
                'length': 18.11,
                'name': '주문가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cndt_ordr_prc',
                'length': 18.11,
                'name': '주문조건가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_q',
                'length': 12,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_tm',
                'length': 9,
                'name': '주문시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'userid',
                'length': 8,
                'name': '사용자ID',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '1: 옵션행사예약<br/>0: 옵션행사예약아님',
                'key': 'xrc_rsv_tp_code',
                'length': 1,
                'name': '행사예약구분코드',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TC2': {
        'tr_cd': 'TC2',
        'title': '해외선물 주문응답',
        'fields': [
            {
                'key': 'lineseq',
                'length': 10,
                'name': '라인일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'key',
                'length': 11,
                'name': 'KEY',
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
                'desc': 'HO02:확인<br/>HO03:거부',
                'key': 'svc_id',
                'length': 4,
                'name': '서비스ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_dt',
                'length': 8,
                'name': '주문일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'brn_cd',
                'length': 3,
                'name': '지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_no',
                'length': 10,
                'name': '주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'orgn_ordr_no',
                'length': 10,
                'name': '원주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mthr_ordr_no',
                'length': 10,
                'name': '모주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ac_no',
                'length': 11,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'is_cd',
                'length': 30,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '1:매도<br/>2:매수',
                'key': 's_b_ccd',
                'length': 1,
                'name': '매도매수유형',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '1:신규<br/>2:정정<br/>3:취소',
                'key': 'ordr_ccd',
                'length': 1,
                'name': '정정취소유형',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '1:시장가<br/>2:지정가<br/>3:Stop Market<br/>4:Stop Limit',
                'key': 'ordr_typ_cd',
                'length': 1,
                'name': '주문유형코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '01:일반<br/>02:Average<br/>03:Spread',
                'key': 'ordr_typ_prd_ccd',
                'length': 2,
                'name': '주문기간코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_aplc_strt_dt',
                'length': 8,
                'name': '주문적용시작일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_aplc_end_dt',
                'length': 8,
                'name': '주문적용종료일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_prc',
                'length': 18.11,
                'name': '주문가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cndt_ordr_prc',
                'length': 18.11,
                'name': '주문조건가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_q',
                'length': 12,
                'name': '주문수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_tm',
                'length': 9,
                'name': '주문시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cnfr_q',
                'length': 12,
                'name': '호가확인수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'rfsl_cd',
                'length': 4,
                'name': '호가거부사유코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'text',
                'length': 80,
                'name': '호가거부사유코드명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'userid',
                'length': 8,
                'name': '사용자ID',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'TC3': {
        'tr_cd': 'TC3',
        'title': '해외선물 주문체결',
        'fields': [
            {
                'key': 'lineseq',
                'length': 10,
                'name': '라인일련번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'key',
                'length': 11,
                'name': 'KEY',
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
                'desc': 'CH01',
                'key': 'svc_id',
                'length': 4,
                'name': '서비스ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_dt',
                'length': 8,
                'name': '주문일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'brn_cd',
                'length': 3,
                'name': '지점번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ordr_no',
                'length': 10,
                'name': '주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'orgn_ordr_no',
                'length': 10,
                'name': '원주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mthr_ordr_no',
                'length': 10,
                'name': '모주문번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ac_no',
                'length': 11,
                'name': '계좌번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'is_cd',
                'length': 30,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '1:매도<br/>2:매수',
                'key': 's_b_ccd',
                'length': 1,
                'name': '매도매수유형',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '1:신규<br/>2:정정<br/>3:취소',
                'key': 'ordr_ccd',
                'length': 1,
                'name': '정정취소유형',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ccls_q',
                'length': 15,
                'name': '체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ccls_prc',
                'length': 18.11,
                'name': '체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ccls_no',
                'length': 10,
                'name': '체결번호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ccls_tm',
                'length': 9,
                'name': '체결시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'avg_byng_uprc',
                'length': 18.11,
                'name': '매입평균단가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'byug_amt',
                'length': 25.8,
                'name': '매입금액',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'clr_pl_amt',
                'length': 19.2,
                'name': '청산손익',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ent_fee',
                'length': 19.2,
                'name': '위탁수수료',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'fcm_fee',
                'length': 19,
                'name': '매입잔고수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'userid',
                'length': 8,
                'name': '사용자ID',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'now_prc',
                'length': 18.11,
                'name': '현재가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'crncy_cd',
                'length': 3,
                'name': '통화코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'mtrt_dt',
                'length': 8,
                'name': '만기일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ord_prdt_tp_code',
                'length': 1,
                'name': '주문상품구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exec_prdt_tp_code',
                'length': 1,
                'name': '주문상품구분코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sprd_base_isu_yn',
                'length': 1,
                'name': '스프레드종목여부',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ccls_dt',
                'length': 8,
                'name': '체결일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'filler2',
                'length': 30,
                'name': 'FILLER2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'sprd_is_cd',
                'length': 30,
                'name': '스프레드종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '1:LME(월물상품)<br/>2:LME(3M상품)<br/>0:LME외',
                'key': 'lme_prdt_ccd',
                'length': 1,
                'name': 'LME상품유형',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'lme_sprd_prc',
                'length': 18.11,
                'name': 'LME스프레드가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'last_now_prc',
                'length': 18.11,
                'name': '최종현재가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bf_mtrt_dt',
                'length': 8,
                'name': '이전만기일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'clr_q',
                'length': 15,
                'name': '청산수량',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'WOC': {
        'tr_cd': 'WOC',
        'title': '해외옵션 체결',
        'fields': [
            {
                'key': 'symbol',
                'length': 16,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ovsdate',
                'length': 8,
                'name': '체결일자(현지)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'kordate',
                'length': 8,
                'name': '체결일자(한국)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'trdtm',
                'length': 6,
                'name': '체결시간(현지)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'kortm',
                'length': 6,
                'name': '체결시간(한국)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'curpr',
                'length': 15.9,
                'name': '체결가격',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ydiffpr',
                'length': 15.9,
                'name': '전일대비',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ydiffSign',
                'length': 1,
                'name': '전일대비기호',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'open',
                'length': 15.9,
                'name': '시가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'high',
                'length': 15.9,
                'name': '고가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low',
                'length': 15.9,
                'name': '저가',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'chgrate',
                'length': 6.2,
                'name': '등락율',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'trdq',
                'length': 10,
                'name': '건별체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totq',
                'length': 15,
                'name': '누적체결수량',
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
                'key': 'mdvolume',
                'length': 15,
                'name': '매도누적체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'msvolume',
                'length': 15,
                'name': '매수누적체결수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'ovsmkend',
                'length': 8,
                'name': '장마감일',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'WOH': {
        'tr_cd': 'WOH',
        'title': '해외옵션 호가',
        'fields': [
            {
                'key': 'symbol',
                'length': 16,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'hotime',
                'length': 6,
                'name': '호가시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho1',
                'length': 15.9,
                'name': '매도호가 1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho1',
                'length': 15.9,
                'name': '매수호가 1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem1',
                'length': 10,
                'name': '매도호가 잔량 1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem1',
                'length': 10,
                'name': '매수호가 잔량 1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno1',
                'length': 10,
                'name': '매도호가 건수 1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno1',
                'length': 10,
                'name': '매수호가 건수 1',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho2',
                'length': 15.9,
                'name': '매도호가 2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho2',
                'length': 15.9,
                'name': '매수호가 2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem2',
                'length': 10,
                'name': '매도호가 잔량 2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem2',
                'length': 10,
                'name': '매수호가 잔량 2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno2',
                'length': 10,
                'name': '매도호가 건수 2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno2',
                'length': 10,
                'name': '매수호가 건수 2',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho3',
                'length': 15.9,
                'name': '매도호가 3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho3',
                'length': 15.9,
                'name': '매수호가 3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem3',
                'length': 10,
                'name': '매도호가 잔량 3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem3',
                'length': 10,
                'name': '매수호가 잔량 3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno3',
                'length': 10,
                'name': '매도호가 건수 3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno3',
                'length': 10,
                'name': '매수호가 건수 3',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho4',
                'length': 15.9,
                'name': '매도호가 4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho4',
                'length': 15.9,
                'name': '매수호가 4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem4',
                'length': 10,
                'name': '매도호가 잔량 4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem4',
                'length': 10,
                'name': '매수호가 잔량 4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno4',
                'length': 10,
                'name': '매도호가 건수 4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno4',
                'length': 10,
                'name': '매수호가 건수 4',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerho5',
                'length': 15.9,
                'name': '매도호가 5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidho5',
                'length': 15.9,
                'name': '매수호가 5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerrem5',
                'length': 10,
                'name': '매도호가 잔량 5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidrem5',
                'length': 10,
                'name': '매수호가 잔량 5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'offerno5',
                'length': 10,
                'name': '매도호가 건수 5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'bidno5',
                'length': 10,
                'name': '매수호가 건수 5',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totoffercnt',
                'length': 10,
                'name': '매도호가총건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidcnt',
                'length': 10,
                'name': '매수호가총건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totofferrem',
                'length': 10,
                'name': '매도호가총수량',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'totbidrem',
                'length': 10,
                'name': '매수호가총수량',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'g3101': {
        'tr_cd': 'g3101',
        'title': '해외주식 API 현재가 조회',
        'fields': [
            {
                'key': 'g3101OutBlock',
                'length': None,
                'name': 'g3101OutBlock',
                'required': True,
                'type': 'long'
            },
            {
                'desc': 'R',
                'key': 'delaygb',
                'length': 1,
                'name': '지연구분',
                'required': True,
                'type': 'string'
            },
            {
                'desc': 'ex)82TSLA',
                'key': 'keysymbol',
                'length': 18,
                'name': 'KEY종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '81 : 뉴욕/아멕스, 82 : 나스닥',
                'key': 'exchcd',
                'length': 2,
                'name': '거래소코드',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '81 : 뉴욕/아멕스, 82 : 나스닥',
                'key': 'exchange',
                'length': 4,
                'name': '거래소ID',
                'required': True,
                'type': 'string'
            },
            {
                'desc': 'Y:정지 N: 보통',
                'key': 'suspend',
                'length': 1,
                'name': '거래상태',
                'required': True,
                'type': 'string'
            },
            {
                'desc': '0:매매가능<br/>1:매도만가능<br/>2:매매불가',
                'key': 'sellonly',
                'length': 1,
                'name': '매매구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'symbol',
                'length': 16,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'korname',
                'length': 64,
                'name': '한글종목명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'induname',
                'length': 40,
                'name': '업종한글명',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'low52p',
                'length': 15.6,
                'name': '52주최저가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'floatpoint',
                'length': 1,
                'name': '소숫점자릿수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'currency',
                'length': 4,
                'name': '외환코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'price',
                'length': 15.6,
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
                'key': 'diff',
                'length': 15.6,
                'name': '전일대비',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'rate',
                'length': 6.2,
                'name': '등락률',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'volume',
                'length': 16,
                'name': '거래량',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'amount',
                'length': 15,
                'name': '거래대금',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'high52p',
                'length': 15.6,
                'name': '52주최고가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'uplimit',
                'length': 15.6,
                'name': '상한가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'dnlimit',
                'length': 15.6,
                'name': '하한가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'open',
                'length': 15.6,
                'name': '시가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'high',
                'length': 15.6,
                'name': '고가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'low',
                'length': 15.6,
                'name': '저가',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'perv',
                'length': 9.2,
                'name': 'PER',
                'required': True,
                'type': 'float'
            },
            {
                'key': 'epsv',
                'length': 9.2,
                'name': 'EPS',
                'required': True,
                'type': 'float'
            }
        ]
    },
    'g3102': {
        'tr_cd': 'g3102',
        'title': '해외주식 API 시간대별',
        'blocks': {
            'g3102OutBlock': {
                'fields': [{'key': 'delaygb', 'name': '지연구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'keysymbol', 'name': 'KEY종목코드', 'type': 'string', 'length': 18, 'required': True}, {'key': 'exchcd', 'name': '거래소코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'symbol', 'name': '종목코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'cts_seq', 'name': '연속시퀀스', 'type': 'float', 'length': 17, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}],
                'type': 'single'
            },
            'g3102OutBlock1': {
                'fields': [{'key': 'locdate', 'name': '현지일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'loctime', 'name': '현지시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'kordate', 'name': '한국일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'kortime', 'name': '한국시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'diff', 'name': '전일대비', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'rate', 'name': '등락률', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'exevol', 'name': '체결량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'cgubun', 'name': '체결구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'floatpoint', 'name': '소숫점자릿수', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'array'
            }
        }
    },
    'g3103': {
        'tr_cd': 'g3103',
        'title': '해외주식 API 일주월 조회',
        'fields': [
            {
                'key': 'g3103OutBlock',
                'length': None,
                'name': 'g3103OutBlock',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'delaygb',
                'length': 1,
                'name': '지연구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'keysymbol',
                'length': 18,
                'name': 'KEY종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchcd',
                'length': 2,
                'name': '거래소코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'symbol',
                'length': 16,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'gubun',
                'length': 1,
                'name': '주기구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'date',
                'length': 8,
                'name': '조회일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'g3103OutBlock1',
                'length': None,
                'name': 'g3103OutBlock1',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'chedate',
                'length': 8,
                'name': '영업일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'price',
                'length': 15.6,
                'name': '현재가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'sign',
                'length': 1,
                'name': '전일대비구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'diff',
                'length': 15.6,
                'name': '전일대비',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'rate',
                'length': 6.2,
                'name': '등락률',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'volume',
                'length': 16,
                'name': '누적거래량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'open',
                'length': 15.6,
                'name': '시가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'high',
                'length': 15.6,
                'name': '고가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'low',
                'length': 15.6,
                'name': '저가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'floatpoint',
                'length': 1,
                'name': '소숫점자릿수',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'g3104': {
        'tr_cd': 'g3104',
        'title': '해외주식 API 종목정보 조회',
        'blocks': {
            'g3104OutBlock': {
                'fields': [{'key': 'delaygb', 'name': '지연구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'keysymbol', 'name': 'KEY종목코드', 'type': 'string', 'length': 18, 'required': True}, {'key': 'exchcd', 'name': '거래소코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'exchange', 'name': '거래소ID', 'type': 'string', 'length': 4, 'required': True}, {'key': 'symbol', 'name': '종목코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'korname', 'name': '한글종목명', 'type': 'string', 'length': 64, 'required': True}, {'key': 'engname', 'name': '영문종목명', 'type': 'string', 'length': 64, 'required': True}, {'key': 'exchange_name', 'name': '거래소명', 'type': 'string', 'length': 16, 'required': True}, {'key': 'nation_name', 'name': '국가명', 'type': 'string', 'length': 16, 'required': True}, {'key': 'induname', 'name': '업종명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'instname', 'name': '증권종류', 'type': 'string', 'length': 16, 'required': True}, {'key': 'floatpoint', 'name': '소숫점자릿수', 'type': 'string', 'length': 1, 'required': True}, {'key': 'currency', 'name': '거래통화', 'type': 'string', 'length': 4, 'required': True}, {'key': 'suspend', 'name': '거래상태', 'type': 'string', 'length': 1, 'required': True}, {'key': 'sellonly', 'name': '매매구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'share', 'name': '발행주식수', 'type': 'float', 'length': 16, 'required': True}, {'key': 'untprc', 'name': '호가단위', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'bidlotsize', 'name': '매수주문단위', 'type': 'string', 'length': 4, 'required': True}, {'key': 'asklotsize', 'name': '매도주문단위', 'type': 'string', 'length': 4, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'amount', 'name': '거래대금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'pcls', 'name': '전일종가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'clos', 'name': '기준가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'high52p', 'name': '52주고가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'low52p', 'name': '52주저가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'shareprc', 'name': '시가총액', 'type': 'float', 'length': 16, 'required': True}, {'key': 'perv', 'name': 'PER', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'epsv', 'name': 'EPS', 'type': 'float', 'length': 9.2, 'required': True}, {'key': 'exrate', 'name': '환율', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'bidlotsize2', 'name': '매수주문단위2', 'type': 'string', 'length': 8, 'required': True}, {'key': 'asklotsize2', 'name': '매도주문단위2', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'single'
            }
        }
    },
    'g3106': {
        'tr_cd': 'g3106',
        'title': '해외주식 API 현재가호가 조회',
        'blocks': {
            'g3106OutBlock': {
                'fields': [{'key': 'delaygb', 'name': '지연구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'keysymbol', 'name': 'KEY종목코드', 'type': 'string', 'length': 18, 'required': True}, {'key': 'exchcd', 'name': '거래소코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'symbol', 'name': '종목코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'korname', 'name': '한글종목명', 'type': 'string', 'length': 64, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'floatpoint', 'name': '소숫점자릿수', 'type': 'string', 'length': 1, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'diff', 'name': '전일대비', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'rate', 'name': '등락률', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'amount', 'name': '누적거래대금', 'type': 'float', 'length': 15, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'hotime', 'name': '호가수신시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'offerho1', 'name': '매도호가1', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'bidho1', 'name': '매수호가1', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'offercnt1', 'name': '매도호가건수1', 'type': 'string', 'length': 10, 'required': True}, {'key': 'bidcnt1', 'name': '매수호가건수1', 'type': 'string', 'length': 10, 'required': True}, {'key': 'offerrem1', 'name': '매도호가잔량1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem1', 'name': '매수호가잔량1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho2', 'name': '매도호가2', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'bidho2', 'name': '매수호가2', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'offercnt2', 'name': '매도호가건수2', 'type': 'string', 'length': 10, 'required': True}, {'key': 'bidcnt2', 'name': '매수호가건수2', 'type': 'string', 'length': 10, 'required': True}, {'key': 'offerrem2', 'name': '매도호가잔량2', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem2', 'name': '매수호가잔량2', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho3', 'name': '매도호가3', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'bidho3', 'name': '매수호가3', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'offercnt3', 'name': '매도호가건수3', 'type': 'string', 'length': 10, 'required': True}, {'key': 'bidcnt3', 'name': '매수호가건수3', 'type': 'string', 'length': 10, 'required': True}, {'key': 'offerrem3', 'name': '매도호가잔량3', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem3', 'name': '매수호가잔량3', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho4', 'name': '매도호가4', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'bidho4', 'name': '매수호가4', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'offercnt4', 'name': '매도호가건수4', 'type': 'string', 'length': 10, 'required': True}, {'key': 'bidcnt4', 'name': '매수호가건수4', 'type': 'string', 'length': 10, 'required': True}, {'key': 'offerrem4', 'name': '매도호가잔량4', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem4', 'name': '매수호가잔량4', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho5', 'name': '매도호가5', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'bidho5', 'name': '매수호가5', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'offercnt5', 'name': '매도호가건수5', 'type': 'string', 'length': 10, 'required': True}, {'key': 'bidcnt5', 'name': '매수호가건수5', 'type': 'string', 'length': 10, 'required': True}, {'key': 'offerrem5', 'name': '매도호가잔량5', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem5', 'name': '매수호가잔량5', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho6', 'name': '매도호가6', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'bidho6', 'name': '매수호가6', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'offercnt6', 'name': '매도호가건수6', 'type': 'string', 'length': 10, 'required': True}, {'key': 'bidcnt6', 'name': '매수호가건수6', 'type': 'string', 'length': 10, 'required': True}, {'key': 'offerrem6', 'name': '매도호가잔량6', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem6', 'name': '매수호가잔량6', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho7', 'name': '매도호가7', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'bidho7', 'name': '매수호가7', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'offercnt7', 'name': '매도호가건수7', 'type': 'string', 'length': 10, 'required': True}, {'key': 'bidcnt7', 'name': '매수호가건수7', 'type': 'string', 'length': 10, 'required': True}, {'key': 'offerrem7', 'name': '매도호가잔량7', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem7', 'name': '매수호가잔량7', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho8', 'name': '매도호가8', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'bidho8', 'name': '매수호가8', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'offercnt8', 'name': '매도호가건수8', 'type': 'string', 'length': 10, 'required': True}, {'key': 'bidcnt8', 'name': '매수호가건수8', 'type': 'string', 'length': 10, 'required': True}, {'key': 'offerrem8', 'name': '매도호가잔량8', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem8', 'name': '매수호가잔량8', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho9', 'name': '매도호가9', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'bidho9', 'name': '매수호가9', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'offercnt9', 'name': '매도호가건수9', 'type': 'string', 'length': 10, 'required': True}, {'key': 'bidcnt9', 'name': '매수호가건수9', 'type': 'string', 'length': 10, 'required': True}, {'key': 'offerrem9', 'name': '매도호가잔량9', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem9', 'name': '매수호가잔량9', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho10', 'name': '매도호가10', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'bidho10', 'name': '매수호가10', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'offercnt10', 'name': '매도호가건수10', 'type': 'string', 'length': 10, 'required': True}, {'key': 'bidcnt10', 'name': '매수호가건수10', 'type': 'string', 'length': 10, 'required': True}, {'key': 'offerrem10', 'name': '매도호가잔량10', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem10', 'name': '매수호가잔량10', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offercnt', 'name': '매도호가건수합', 'type': 'string', 'length': 10, 'required': True}, {'key': 'bidcnt', 'name': '매수호가건수합', 'type': 'string', 'length': 10, 'required': True}, {'key': 'offer', 'name': '매도호가잔량합', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bid', 'name': '매수호가잔량합', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'single'
            }
        }
    },
    'g3190': {
        'tr_cd': 'g3190',
        'title': '해외주식 API 마스터 조회',
        'blocks': {
            'g3190OutBlock': {
                'fields': [{'key': 'delaygb', 'name': '지연구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'natcode', 'name': '국가구분', 'type': 'string', 'length': 2, 'required': True}, {'key': 'exgubun', 'name': '거래소구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'cts_value', 'name': '연속구분', 'type': 'string', 'length': 16, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}, {'key': 'g3190OutBlock1', 'name': 'g3190OutBlock1', 'type': 'long', 'length': None, 'required': True}, {'key': 'keysymbol', 'name': 'KEY종목코드', 'type': 'string', 'length': 18, 'required': True}, {'key': 'natcode', 'name': '국가코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'exchcd', 'name': '거래소코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'symbol', 'name': '종목코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'seccode', 'name': '거래소종목코드', 'type': 'string', 'length': 18, 'required': True}, {'key': 'korname', 'name': '한글종목명', 'type': 'string', 'length': 64, 'required': True}, {'key': 'engname', 'name': '영문종목명', 'type': 'string', 'length': 64, 'required': True}, {'key': 'currency', 'name': '외환코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'isin', 'name': 'ISIN', 'type': 'string', 'length': 12, 'required': True}, {'key': 'floatpoint', 'name': 'FLOATPOINT', 'type': 'string', 'length': 1, 'required': True}, {'key': 'indusury', 'name': '업종코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'share', 'name': '상장주식수', 'type': 'float', 'length': 16, 'required': True}, {'key': 'marketcap', 'name': '자본금', 'type': 'float', 'length': 16, 'required': True}, {'key': 'par', 'name': '액면가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'parcurr', 'name': '액면가외환코드', 'type': 'string', 'length': 4, 'required': True}, {'key': 'bidlotsize2', 'name': '매수주문단위2', 'type': 'string', 'length': 8, 'required': True}, {'key': 'asklotsize2', 'name': '매도주문단위2', 'type': 'string', 'length': 8, 'required': True}, {'key': 'clos', 'name': '기준가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'listed_date', 'name': '상장일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'expire_date', 'name': '만기일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'suspend', 'name': '거래정지여부', 'type': 'string', 'length': 1, 'required': True}, {'key': 'bymd', 'name': '영업일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'sellonly', 'name': 'SELLONLY구분', 'type': 'string', 'length': 8, 'required': True}, {'key': 'stamp', 'name': '인지세여부', 'type': 'string', 'length': 1, 'required': True}, {'key': 'ticktype', 'name': 'TICKSIZETYPE', 'type': 'string', 'length': 8, 'required': True}, {'key': 'pcls', 'name': '전일종가', 'type': 'float', 'length': 15.6, 'required': True}, {'key': 'vcmf', 'name': 'VCM대상종목', 'type': 'string', 'length': 1, 'required': True}, {'key': 'casf', 'name': 'CAS대상종목', 'type': 'string', 'length': 1, 'required': True}, {'key': 'posf', 'name': 'POS대상종목', 'type': 'string', 'length': 1, 'required': True}, {'key': 'point', 'name': '소수점매매가능종목', 'type': 'string', 'length': 1, 'required': True}],
                'type': 'single'
            }
        }
    },
    'g3202': {
        'tr_cd': 'g3202',
        'title': '해외주식 API 차트NTICK 조회',
        'fields': [
            {
                'key': 'g3202OutBlock',
                'length': None,
                'name': 'g3202OutBlock',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'delaygb',
                'length': 1,
                'name': '지연구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'keysymbol',
                'length': 18,
                'name': 'KEY종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchcd',
                'length': 2,
                'name': '거래소코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'symbol',
                'length': 16,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cts_seq',
                'length': 17,
                'name': '연속시퀀스',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'rec_count',
                'length': 7,
                'name': '레코드카운트',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'preopen',
                'length': 15.8,
                'name': '전일시가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'prehigh',
                'length': 15.8,
                'name': '전일고가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'prelow',
                'length': 15.8,
                'name': '전일저가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'preclose',
                'length': 15.8,
                'name': '전일종가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'prevolume',
                'length': 16,
                'name': '전일거래량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'open',
                'length': 15.8,
                'name': '당일시가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'high',
                'length': 15.8,
                'name': '당일고가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'low',
                'length': 15.8,
                'name': '당일저가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'close',
                'length': 15.8,
                'name': '당일종가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 's_time',
                'length': 6,
                'name': '장시작시간(HHMMSS)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'e_time',
                'length': 6,
                'name': '장종료시간(HHMMSS)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'last_count',
                'length': 4,
                'name': '마지막Tick건수',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'timediff',
                'length': 4,
                'name': '시차',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'prtt_rate',
                'length': 6.2,
                'name': '수정비율',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'g3202OutBlock1',
                'length': None,
                'name': 'g3202OutBlock1',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'date',
                'length': 8,
                'name': '날짜',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'loctime',
                'length': 6,
                'name': '현지시간',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'open',
                'length': 15.8,
                'name': '시가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'high',
                'length': 15.8,
                'name': '고가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'low',
                'length': 15.8,
                'name': '저가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'close',
                'length': 15.8,
                'name': '종가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'exevol',
                'length': 16,
                'name': '체결량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'jongchk',
                'length': 13,
                'name': '수정구분',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'pricechk',
                'length': 13,
                'name': '수정주가반영항목',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'sign',
                'length': 1,
                'name': '종가등락구분(1:상한2:상승3:보합',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'g3203': {
        'tr_cd': 'g3203',
        'title': '해외주식 API 차트NMIN 조회',
        'blocks': {
            'g3203OutBlock': {
                'fields': [{'key': 'delaygb', 'name': '지연구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'keysymbol', 'name': 'KEY종목코드', 'type': 'string', 'length': 18, 'required': True}, {'key': 'exchcd', 'name': '거래소코드', 'type': 'string', 'length': 2, 'required': True}, {'key': 'symbol', 'name': '종목코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}, {'key': 'preopen', 'name': '전일시가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'prehigh', 'name': '전일고가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'prelow', 'name': '전일저가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'preclose', 'name': '전일종가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'prevolume', 'name': '전일거래량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'open', 'name': '당일시가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'high', 'name': '당일고가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'low', 'name': '당일저가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'close', 'name': '당일종가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 's_time', 'name': '장시작시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'e_time', 'name': '장종료시간(HHMMSS)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'timediff', 'name': '시차', 'type': 'string', 'length': 4, 'required': True}],
                'type': 'single'
            },
            'g3203OutBlock1': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'loctime', 'name': '현지시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'exevol', 'name': '체결량', 'type': 'float', 'length': 16, 'required': True}, {'key': 'amount', 'name': '거래대금', 'type': 'float', 'length': 16, 'required': True}],
                'type': 'single'
            }
        }
    },
    'g3204': {
        'tr_cd': 'g3204',
        'title': '해외주식 API 차트일주월년별 조회',
        'fields': [
            {
                'key': 'g3204OutBlock',
                'length': None,
                'name': 'g3204OutBlock',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'delaygb',
                'length': 1,
                'name': '지연구분',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'keysymbol',
                'length': 18,
                'name': 'KEY종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'exchcd',
                'length': 2,
                'name': '거래소코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'symbol',
                'length': 16,
                'name': '종목코드',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cts_date',
                'length': 8,
                'name': '연속일자',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'cts_info',
                'length': 6,
                'name': '연속정보',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'rec_count',
                'length': 7,
                'name': '레코드카운트',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'preopen',
                'length': 15.8,
                'name': '전일시가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'prehigh',
                'length': 15.8,
                'name': '전일고가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'prelow',
                'length': 15.8,
                'name': '전일저가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'preclose',
                'length': 15.8,
                'name': '전일종가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'prevolume',
                'length': 16,
                'name': '전일거래량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'open',
                'length': 15.8,
                'name': '당일시가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'high',
                'length': 15.8,
                'name': '당일고가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'low',
                'length': 15.8,
                'name': '당일저가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'close',
                'length': 15.8,
                'name': '당일종가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'uplimit',
                'length': 15.8,
                'name': '상한가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'dnlimit',
                'length': 15.8,
                'name': '하한가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 's_time',
                'length': 6,
                'name': '장시작시간(HHMMSS)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'e_time',
                'length': 6,
                'name': '장종료시간(HHMMSS)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'dshmin',
                'length': 2,
                'name': '동시호가처리시간(MM:분)',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'g3204OutBlock1',
                'length': None,
                'name': 'g3204OutBlock1',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'date',
                'length': 8,
                'name': '날짜',
                'required': True,
                'type': 'string'
            },
            {
                'key': 'open',
                'length': 15.8,
                'name': '시가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'high',
                'length': 15.8,
                'name': '고가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'low',
                'length': 15.8,
                'name': '저가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'close',
                'length': 15.8,
                'name': '종가',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'volume',
                'length': 16,
                'name': '거래량',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'amount',
                'length': 16,
                'name': '거래대금',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'jongchk',
                'length': 13,
                'name': '수정구분',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'prtt_rate',
                'length': 6.2,
                'name': '수정비율',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'pricechk',
                'length': 13,
                'name': '수정주가반영항목',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'ratevalue',
                'length': 12,
                'name': '수정비율반영거래대금',
                'required': True,
                'type': 'long'
            },
            {
                'key': 'sign',
                'length': 1,
                'name': '종가등락구분(1:상한2:상승3:보합',
                'required': True,
                'type': 'string'
            }
        ]
    },
    'o3101': {
        'tr_cd': 'o3101',
        'title': '해외선물마스터조회',
        'blocks': {
            'o3101OutBlock': {
                'fields': [{'key': 'Symbol', 'name': '종목코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'SymbolNm', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'ApplDate', 'name': '종목배치수신일(한국일자)', 'type': 'string', 'length': 8, 'required': True}, {'key': 'BscGdsCd', 'name': '기초상품코드', 'type': 'string', 'length': 10, 'required': True}, {'key': 'BscGdsNm', 'name': '기초상품명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'ExchCd', 'name': '거래소코드', 'type': 'string', 'length': 10, 'required': True}, {'key': 'ExchNm', 'name': '거래소명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'CrncyCd', 'name': '기준통화코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'NotaCd', 'name': '진법구분코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'UntPrc', 'name': '호가단위가격', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'MnChgAmt', 'name': '최소가격변동금액', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'RgltFctr', 'name': '가격조정계수', 'type': 'float', 'length': 15.1, 'required': True}, {'key': 'CtrtPrAmt', 'name': '계약당금액', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'GdsCd', 'name': '상품구분코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'LstngYr', 'name': '월물(년)', 'type': 'string', 'length': 4, 'required': True}, {'key': 'LstngM', 'name': '월물(월)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'EcPrc', 'name': '정산가격', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'DlStrtTm', 'name': '거래시작시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'DlEndTm', 'name': '거래종료시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'DlPsblCd', 'name': '거래가능구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'MgnCltCd', 'name': '증거금징수구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OpngMgn', 'name': '개시증거금', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'MntncMgn', 'name': '유지증거금', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'OpngMgnR', 'name': '개시증거금율', 'type': 'float', 'length': 7.3, 'required': True}, {'key': 'MntncMgnR', 'name': '유지증거금율', 'type': 'float', 'length': 7.3, 'required': True}, {'key': 'DotGb', 'name': '유효소수점자리수', 'type': 'float', 'length': 2, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3103': {
        'tr_cd': 'o3103',
        'title': '해외선물차트 분봉 조회',
        'blocks': {
            'o3103OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'timediff', 'name': '시차', 'type': 'float', 'length': 4, 'required': True}, {'key': 'readcnt', 'name': '조회건수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            },
            'o3103OutBlock1 (Occurs)': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '현지시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    'o3104': {
        'tr_cd': 'o3104',
        'title': '해외선물 일별체결 조회',
        'blocks': {
            'o3104OutBlock1 (Occurs)': {
                'fields': [{'key': 'chedate', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'sign', 'name': '대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '대비', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'cgubun', 'name': '체결구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'array'
            }
        }
    },
    'o3105': {
        'tr_cd': 'o3105',
        'title': '해외선물 현재가(종목정보) 조회',
        'blocks': {
            'o3105OutBlock': {
                'fields': [{'key': 'Symbol', 'name': '종목코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'SymbolNm', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'ApplDate', 'name': '종목배치수신일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'BscGdsCd', 'name': '기초상품코드', 'type': 'string', 'length': 10, 'required': True}, {'key': 'BscGdsNm', 'name': '기초상품명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'ExchCd', 'name': '거래소코드', 'type': 'string', 'length': 10, 'required': True}, {'key': 'ExchNm', 'name': '거래소명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'EcCd', 'name': '정산구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'CrncyCd', 'name': '기준통화코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'NotaCd', 'name': '진법구분코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'UntPrc', 'name': '호가단위가격', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'MnChgAmt', 'name': '최소가격변동금액', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'RgltFctr', 'name': '가격조정계수', 'type': 'float', 'length': 15.1, 'required': True}, {'key': 'CtrtPrAmt', 'name': '계약당금액', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'LstngMCnt', 'name': '상장개월수', 'type': 'float', 'length': 2, 'required': True}, {'key': 'GdsCd', 'name': '상품구분코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'MrktCd', 'name': '시장구분코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'EminiCd', 'name': 'Emini구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'LstngYr', 'name': '상장년', 'type': 'string', 'length': 4, 'required': True}, {'key': 'LstngM', 'name': '상장월', 'type': 'string', 'length': 1, 'required': True}, {'key': 'SeqNo', 'name': '월물순서', 'type': 'float', 'length': 5, 'required': True}, {'key': 'LstngDt', 'name': '상장일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'MtrtDt', 'name': '만기일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FnlDlDt', 'name': '최종거래일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FstTrsfrDt', 'name': '최초인도통지일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'EcPrc', 'name': '정산가격', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'DlDt', 'name': '거래시작일자(한국)', 'type': 'string', 'length': 8, 'required': True}, {'key': 'DlStrtTm', 'name': '거래시작시간(한국)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'DlEndTm', 'name': '거래종료시간(한국)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'OvsStrDay', 'name': '거래시작일자(현지)', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OvsStrTm', 'name': '거래시작시간(현지)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'OvsEndDay', 'name': '거래종료일자(현지)', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OvsEndTm', 'name': '거래종료시간(현지)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'DlPsblCd', 'name': '거래가능구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'MgnCltCd', 'name': '증거금징수구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OpngMgn', 'name': '개시증거금', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'MntncMgn', 'name': '유지증거금', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'OpngMgnR', 'name': '개시증거금율', 'type': 'float', 'length': 7.3, 'required': True}, {'key': 'MntncMgnR', 'name': '유지증거금율', 'type': 'float', 'length': 7.3, 'required': True}, {'key': 'DotGb', 'name': '유효소수점자리수', 'type': 'float', 'length': 2, 'required': True}, {'key': 'TimeDiff', 'name': '시차', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OvsDate', 'name': '현지체결일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'KorDate', 'name': '한국체결일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'TrdTm', 'name': '현지체결시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'RcvTm', 'name': '한국체결시각', 'type': 'string', 'length': 6, 'required': True}, {'key': 'TrdP', 'name': '체결가격', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'TrdQ', 'name': '체결수량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'TotQ', 'name': '누적거래량', 'type': 'float', 'length': 15, 'required': True}, {'key': 'TrdAmt', 'name': '체결거래대금', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'TotAmt', 'name': '누적거래대금', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'OpenP', 'name': '시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'HighP', 'name': '고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'LowP', 'name': '저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'CloseP', 'name': '전일종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'YdiffP', 'name': '전일대비', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'YdiffSign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'Cgubun', 'name': '체결구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'Diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3106': {
        'tr_cd': 'o3106',
        'title': '해외선물 현재가호가 조회',
        'blocks': {
            'o3106OutBlock': {
                'fields': [{'key': 'symbol', 'name': '종목코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'symbolname', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'hotime', 'name': '호가수신시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'offerho1', 'name': '매도호가1', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'bidho1', 'name': '매수호가1', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'offercnt1', 'name': '매도호가건수1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt1', 'name': '매수호가건수1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerrem1', 'name': '매도호가수량1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem1', 'name': '매수호가수량1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho2', 'name': '매도호가2', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'bidho2', 'name': '매수호가2', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'offercnt2', 'name': '매도호가건수2', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt2', 'name': '매수호가건수2', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerrem2', 'name': '매도호가수량2', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem2', 'name': '매수호가수량2', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho3', 'name': '매도호가3', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'bidho3', 'name': '매수호가3', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'offercnt3', 'name': '매도호가건수3', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt3', 'name': '매수호가건수3', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerrem3', 'name': '매도호가수량3', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem3', 'name': '매수호가수량3', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho4', 'name': '매도호가4', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'bidho4', 'name': '매수호가4', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'offercnt4', 'name': '매도호가건수4', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt4', 'name': '매수호가건수4', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerrem4', 'name': '매도호가수량4', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem4', 'name': '매수호가수량4', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho5', 'name': '매도호가5', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'bidho5', 'name': '매수호가5', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'offercnt5', 'name': '매도호가건수5', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt5', 'name': '매수호가건수5', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerrem5', 'name': '매도호가수량5', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem5', 'name': '매수호가수량5', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offercnt', 'name': '매도호가건수합', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt', 'name': '매수호가건수합', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offer', 'name': '매도호가수량합', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bid', 'name': '매수호가수량합', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3107': {
        'tr_cd': 'o3107',
        'title': '해외선물 관심종목 조회',
        'blocks': {
            'o3107OutBlock (Occurs)': {
                'fields': [{'key': 'symbol', 'name': '종목코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'symbolname', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'offerho1', 'name': '매도호가1', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'bidho1', 'name': '매수호가1', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'offercnt1', 'name': '매도호가건수1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt1', 'name': '매수호가건수1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerrem1', 'name': '매도호가수량1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem1', 'name': '매수호가수량1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offercnt', 'name': '매도호가건수합', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt', 'name': '매수호가건수합', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offer', 'name': '매도호가수량합', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bid', 'name': '매수호가수량합', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'array'
            }
        }
    },
    'o3108': {
        'tr_cd': 'o3108',
        'title': '해외선물차트(일주월) 조회',
        'blocks': {
            'o3108OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'jiclose', 'name': '존일종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'mk_stime', 'name': '장시작시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'mk_etime', 'name': '장마감시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}],
                'type': 'single'
            },
            'o3108OutBlock1 (Occurs)': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    'o3116': {
        'tr_cd': 'o3116',
        'title': '해외선물 시간대별(Tick)체결 조회',
        'blocks': {
            'o3116OutBlock': {
                'fields': [{'key': 'cts_seq', 'name': '순번CTS', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'single'
            },
            'o3116OutBlock1 (Occurs)': {
                'fields': [{'key': 'ovsdate', 'name': '현지일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'ovstime', 'name': '현지시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'array'
            }
        }
    },
    'o3117': {
        'tr_cd': 'o3117',
        'title': '해외선물 차트 NTick 체결 조회',
        'blocks': {
            'o3117OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 8, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}, {'key': 'cts_seq', 'name': '순번CTS', 'type': 'string', 'length': 10, 'required': True}, {'key': 'cts_daygb', 'name': '당일구분CTS', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            'o3117OutBlock1 (Occurs)': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    'o3121': {
        'tr_cd': 'o3121',
        'title': '해외선물옵션 마스터 조회',
        'blocks': {
            'o3121OutBlock': {
                'fields': [{'key': 'Symbol', 'name': '종목코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'SymbolNm', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'ApplDate', 'name': '종목배치수신일(한국일자)', 'type': 'string', 'length': 8, 'required': True}, {'key': 'BscGdsCd', 'name': '기초상품코드', 'type': 'string', 'length': 10, 'desc': '시장구분 공란 시 옵션기초상품코드 받는 필드', 'required': True}, {'key': 'BscGdsNm', 'name': '기초상품명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'ExchCd', 'name': '거래소코드', 'type': 'string', 'length': 10, 'required': True}, {'key': 'ExchNm', 'name': '거래소명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'CrncyCd', 'name': '기준통화코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'NotaCd', 'name': '진법구분코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'UntPrc', 'name': '호가단위가격', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'MnChgAmt', 'name': '최소가격변동금액', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'RgltFctr', 'name': '가격조정계수', 'type': 'float', 'length': 15.1, 'required': True}, {'key': 'CtrtPrAmt', 'name': '계약당금액', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'GdsCd', 'name': '상품구분코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'LstngYr', 'name': '월물(년)', 'type': 'string', 'length': 4, 'required': True}, {'key': 'LstngM', 'name': '월물(월)', 'type': 'string', 'length': 1, 'required': True}, {'key': 'EcPrc', 'name': '정산가격', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'DlStrtTm', 'name': '거래시작시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'DlEndTm', 'name': '거래종료시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'DlPsblCd', 'name': '거래가능구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'MgnCltCd', 'name': '증거금징수구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OpngMgn', 'name': '개시증거금', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'MntncMgn', 'name': '유지증거금', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'OpngMgnR', 'name': '개시증거금율', 'type': 'float', 'length': 7.3, 'required': True}, {'key': 'MntncMgnR', 'name': '유지증거금율', 'type': 'float', 'length': 7.3, 'required': True}, {'key': 'DotGb', 'name': '유효소수점자리수', 'type': 'float', 'length': 2, 'required': True}, {'key': 'XrcPrc', 'name': '옵션행사가', 'type': 'string', 'length': 15, 'required': True}, {'key': 'FdasBasePrc', 'name': '기초자산기준가격', 'type': 'string', 'length': 15, 'required': True}, {'key': 'OptTpCode', 'name': '옵션콜풋구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'RgtXrcPtnCode', 'name': '권리행사구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'Moneyness', 'name': 'ATM구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'LastSettPtnCode', 'name': '해외파생기초자산종목코드', 'type': 'string', 'length': 30, 'required': True}, {'key': 'OptMinOrcPrc', 'name': '해외옵션최소호가', 'type': 'string', 'length': 15, 'required': True}, {'key': 'OptMinBaseOrcPrc', 'name': '해외옵션최소기준호가', 'type': 'string', 'length': 15, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3123': {
        'tr_cd': 'o3123',
        'title': '해외선물옵션 차트 분봉 조회',
        'blocks': {
            'o3123OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'timediff', 'name': '시차', 'type': 'float', 'length': 4, 'required': True}, {'key': 'readcnt', 'name': '조회건수', 'type': 'float', 'length': 4, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': '연속시간', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            },
            'o3123OutBlock1 (Occurs)': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '현지시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    'o3125': {
        'tr_cd': 'o3125',
        'title': '해외선물옵션 현재가(종목정보) 조회',
        'blocks': {
            'o3125OutBlock': {
                'fields': [{'key': 'Symbol', 'name': '종목코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'SymbolNm', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'ApplDate', 'name': '종목배치수신일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'BscGdsCd', 'name': '기초상품코드', 'type': 'string', 'length': 10, 'required': True}, {'key': 'BscGdsNm', 'name': '기초상품명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'ExchCd', 'name': '거래소코드', 'type': 'string', 'length': 10, 'required': True}, {'key': 'ExchNm', 'name': '거래소명', 'type': 'string', 'length': 40, 'required': True}, {'key': 'EcCd', 'name': '정산구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'CrncyCd', 'name': '기준통화코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'NotaCd', 'name': '진법구분코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'UntPrc', 'name': '호가단위가격', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'MnChgAmt', 'name': '최소가격변동금액', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'RgltFctr', 'name': '가격조정계수', 'type': 'float', 'length': 15.1, 'required': True}, {'key': 'CtrtPrAmt', 'name': '계약당금액', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'LstngMCnt', 'name': '상장개월수', 'type': 'float', 'length': 2, 'required': True}, {'key': 'GdsCd', 'name': '상품구분코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'MrktCd', 'name': '시장구분코드', 'type': 'string', 'length': 3, 'required': True}, {'key': 'EminiCd', 'name': 'Emini구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'LstngYr', 'name': '상장년', 'type': 'string', 'length': 4, 'required': True}, {'key': 'LstngM', 'name': '상장월', 'type': 'string', 'length': 1, 'required': True}, {'key': 'SeqNo', 'name': '월물순서', 'type': 'float', 'length': 5, 'required': True}, {'key': 'LstngDt', 'name': '상장일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'MtrtDt', 'name': '만기일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FnlDlDt', 'name': '최종거래일', 'type': 'string', 'length': 8, 'required': True}, {'key': 'FstTrsfrDt', 'name': '최초인도통지일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'EcPrc', 'name': '정산가격', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'DlDt', 'name': '거래시작일자(한국)', 'type': 'string', 'length': 8, 'required': True}, {'key': 'DlStrtTm', 'name': '거래시작시간(한국)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'DlEndTm', 'name': '거래종료시간(한국)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'OvsStrDay', 'name': '거래시작일자(현지)', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OvsStrTm', 'name': '거래시작시간(현지)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'OvsEndDay', 'name': '거래종료일자(현지)', 'type': 'string', 'length': 8, 'required': True}, {'key': 'OvsEndTm', 'name': '거래종료시간(현지)', 'type': 'string', 'length': 6, 'required': True}, {'key': 'DlPsblCd', 'name': '거래가능구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'MgnCltCd', 'name': '증거금징수구분코드', 'type': 'string', 'length': 1, 'required': True}, {'key': 'OpngMgn', 'name': '개시증거금', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'MntncMgn', 'name': '유지증거금', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'OpngMgnR', 'name': '개시증거금율', 'type': 'float', 'length': 7.3, 'required': True}, {'key': 'MntncMgnR', 'name': '유지증거금율', 'type': 'float', 'length': 7.3, 'required': True}, {'key': 'DotGb', 'name': '유효소수점자리수', 'type': 'float', 'length': 2, 'required': True}, {'key': 'TimeDiff', 'name': '시차', 'type': 'float', 'length': 5, 'required': True}, {'key': 'OvsDate', 'name': '현지체결일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'KorDate', 'name': '한국체결일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'TrdTm', 'name': '현지체결시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'RcvTm', 'name': '한국체결시각', 'type': 'string', 'length': 6, 'required': True}, {'key': 'TrdP', 'name': '체결가격', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'TrdQ', 'name': '체결수량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'TotQ', 'name': '누적거래량', 'type': 'float', 'length': 15, 'required': True}, {'key': 'TrdAmt', 'name': '체결거래대금', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'TotAmt', 'name': '누적거래대금', 'type': 'float', 'length': 15.2, 'required': True}, {'key': 'OpenP', 'name': '시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'HighP', 'name': '고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'LowP', 'name': '저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'CloseP', 'name': '전일종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'YdiffP', 'name': '전일대비', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'YdiffSign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'Cgubun', 'name': '체결구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'Diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'MinOrcPrc', 'name': '최소호가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'MinBaseOrcPrc', 'name': '최소기준호가', 'type': 'float', 'length': 15.9, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3126': {
        'tr_cd': 'o3126',
        'title': '해외선물옵션 현재가호가 조회',
        'blocks': {
            'o3126OutBlock': {
                'fields': [{'key': 'symbol', 'name': '종목코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'symbolname', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'hotime', 'name': '호가수신시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'offerho1', 'name': '매도호가1', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'bidho1', 'name': '매수호가1', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'offercnt1', 'name': '매도호가건수1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt1', 'name': '매수호가건수1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerrem1', 'name': '매도호가수량1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem1', 'name': '매수호가수량1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho2', 'name': '매도호가2', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'bidho2', 'name': '매수호가2', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'offercnt2', 'name': '매도호가건수2', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt2', 'name': '매수호가건수2', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerrem2', 'name': '매도호가수량2', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem2', 'name': '매수호가수량2', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho3', 'name': '매도호가3', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'bidho3', 'name': '매수호가3', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'offercnt3', 'name': '매도호가건수3', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt3', 'name': '매수호가건수3', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerrem3', 'name': '매도호가수량3', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem3', 'name': '매수호가수량3', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho4', 'name': '매도호가4', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'bidho4', 'name': '매수호가4', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'offercnt4', 'name': '매도호가건수4', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt4', 'name': '매수호가건수4', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerrem4', 'name': '매도호가수량4', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem4', 'name': '매수호가수량4', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerho5', 'name': '매도호가5', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'bidho5', 'name': '매수호가5', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'offercnt5', 'name': '매도호가건수5', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt5', 'name': '매수호가건수5', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerrem5', 'name': '매도호가수량5', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem5', 'name': '매수호가수량5', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offercnt', 'name': '매도호가건수합', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt', 'name': '매수호가건수합', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offer', 'name': '매도호가수량합', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bid', 'name': '매수호가수량합', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'single'
            }
        }
    },
    'o3127': {
        'tr_cd': 'o3127',
        'title': '해외선물옵션 관심종목 조회',
        'blocks': {
            'o3127OutBlock (Occurs)': {
                'fields': [{'key': 'symbol', 'name': '종목코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'symbolname', 'name': '종목명', 'type': 'string', 'length': 50, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'jnilclose', 'name': '전일종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'offerho1', 'name': '매도호가1', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'bidho1', 'name': '매수호가1', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'offercnt1', 'name': '매도호가건수1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt1', 'name': '매수호가건수1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offerrem1', 'name': '매도호가수량1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidrem1', 'name': '매수호가수량1', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offercnt', 'name': '매도호가건수합', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bidcnt', 'name': '매수호가건수합', 'type': 'float', 'length': 10, 'required': True}, {'key': 'offer', 'name': '매도호가수량합', 'type': 'float', 'length': 10, 'required': True}, {'key': 'bid', 'name': '매수호가수량합', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'array'
            }
        }
    },
    'o3128': {
        'tr_cd': 'o3128',
        'title': '해외선물옵션 차트 일주월 조회',
        'blocks': {
            'o3128OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'jisiga', 'name': '전일시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'jihigh', 'name': '전일고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'jilow', 'name': '전일저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'jiclose', 'name': '존일종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'jivolume', 'name': '전일거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'disiga', 'name': '당일시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'dihigh', 'name': '당일고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'dilow', 'name': '당일저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'diclose', 'name': '당일종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'mk_stime', 'name': '장시작시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'mk_etime', 'name': '장마감시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'cts_date', 'name': '연속일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}],
                'type': 'single'
            },
            'o3128OutBlock1 (Occurs)': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    'o3136': {
        'tr_cd': 'o3136',
        'title': '해외선물옵션 시간대별 Tick 체결 조회',
        'blocks': {
            'o3136OutBlock': {
                'fields': [{'key': 'cts_seq', 'name': '순번CTS', 'type': 'float', 'length': 8, 'required': True}],
                'type': 'single'
            },
            'o3136OutBlock1 (Occurs)': {
                'fields': [{'key': 'ovsdate', 'name': '현지일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'ovstime', 'name': '현지시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'diff', 'name': '등락율', 'type': 'float', 'length': 6.2, 'required': True}, {'key': 'cvolume', 'name': '체결수량', 'type': 'float', 'length': 10, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 10, 'required': True}],
                'type': 'array'
            }
        }
    },
    'o3137': {
        'tr_cd': 'o3137',
        'title': '해외선물옵션 차트 NTick 체결 조회',
        'blocks': {
            'o3137OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}, {'key': 'cts_seq', 'name': '연속시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'cts_daygb', 'name': '연속당일구분', 'type': 'string', 'length': 2, 'required': True}],
                'type': 'single'
            },
            'o3137OutBlock1 (Occurs)': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 15.9, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    'o3139': {
        'tr_cd': 'o3139',
        'title': '해외선물옵션차트용NTick(고정형)-API용',
        'blocks': {
            'o3139OutBlock': {
                'fields': [{'key': 'shcode', 'name': '단축코드', 'type': 'string', 'length': 16, 'required': True}, {'key': 'rec_count', 'name': '레코드카운트', 'type': 'float', 'length': 7, 'required': True}, {'key': 'cts_seq', 'name': '연속시간', 'type': 'string', 'length': 10, 'required': True}, {'key': 'cts_daygb', 'name': '연속당일구분', 'type': 'string', 'length': 2, 'required': True}, {'key': 'last_count', 'name': '마지막Tick건수', 'type': 'float', 'length': 4, 'required': True}],
                'type': 'single'
            },
            'o3139OutBlock1 (Occurs)': {
                'fields': [{'key': 'date', 'name': '날짜', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 6, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'close', 'name': '종가', 'type': 'float', 'length': 15.8, 'required': True}, {'key': 'volume', 'name': '거래량', 'type': 'float', 'length': 12, 'required': True}],
                'type': 'array'
            }
        }
    },
    't3518': {
        'tr_cd': 't3518',
        'title': '해외실시간지수',
        'blocks': {
            't3518OutBlock': {
                'fields': [{'key': 'cts_date', 'name': 'CTS_DATE', 'type': 'string', 'length': 8, 'required': True}, {'key': 'cts_time', 'name': 'CTS_TIME', 'type': 'string', 'length': 6, 'required': True}],
                'type': 'single'
            },
            't3518OutBlock1': {
                'fields': [{'key': 'date', 'name': '일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'time', 'name': '시간', 'type': 'string', 'length': 8, 'required': True}, {'key': 'open', 'name': '시가', 'type': 'float', 'length': 9.4, 'desc': '※ 종목종류별 가격 소수점 자리수  - S(해외지수) : 9.2  - F(해외선물) : 9.2  - R(환율/금리) : 9.4', 'required': True}, {'key': 'high', 'name': '고가', 'type': 'float', 'length': 9.4, 'desc': '※ 종목종류별 가격 소수점 자리수  - S(해외지수) : 9.2  - F(해외선물) : 9.2  - R(환율/금리) : 9.4', 'required': True}, {'key': 'low', 'name': '저가', 'type': 'float', 'length': 9.4, 'desc': '※ 종목종류별 가격 소수점 자리수  - S(해외지수) : 9.2  - F(해외선물) : 9.2  - R(환율/금리) : 9.4', 'required': True}, {'key': 'price', 'name': '현재가', 'type': 'float', 'length': 9.4, 'required': True}, {'key': 'sign', 'name': '전일대비구분', 'type': 'string', 'length': 1, 'required': True}, {'key': 'change', 'name': '전일대비', 'type': 'float', 'length': 9.4, 'required': True}, {'key': 'uprate', 'name': '등락율', 'type': 'float', 'length': 9.4, 'required': True}, {'key': 'volume', 'name': '누적거래량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'bidho', 'name': '매수호가', 'type': 'float', 'length': 9.4, 'required': True}, {'key': 'offerho', 'name': '매도호가', 'type': 'float', 'length': 9.4, 'required': True}, {'key': 'bidrem', 'name': '매수잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'offerrem', 'name': '매도잔량', 'type': 'float', 'length': 12, 'required': True}, {'key': 'kind', 'name': '종목종류', 'type': 'string', 'length': 1, 'required': True}, {'key': 'symbol', 'name': 'SYMBOL', 'type': 'string', 'length': 16, 'required': True}, {'key': 'exid', 'name': 'EXID', 'type': 'string', 'length': 4, 'required': True}, {'key': 'kodate', 'name': '한국일자', 'type': 'string', 'length': 8, 'required': True}, {'key': 'kotime', 'name': '한국시간', 'type': 'string', 'length': 8, 'required': True}],
                'type': 'array'
            }
        }
    },
    't3521': {
        'tr_cd': 't3521',
        'title': '해외지수조회(API용)',
        'fields': []
    }
}
