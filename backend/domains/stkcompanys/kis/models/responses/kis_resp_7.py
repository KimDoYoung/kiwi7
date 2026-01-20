# KIS REST API Response Definitions
# Auto-generated from Excel file

KIS_RESPONSE_DEF_7 = {
    # === 주식주문(현금) ===
    '(매도) TTTC0011U (매수) TTTC0012U': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'KRX_FWDG_ORD_ORGNO', 'name': '거래소코드', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'ODNO', 'name': '주문번호', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ORD_TMD', 'name': '주문시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
            ]
        }
    },
    # === 주식주문(신용) ===
    '(매도) TTTC0051U (매수) TTTC0052U': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'krx_fwdg_ord_orgno', 'name': '한국거래소전송주문조직번호', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'odno', 'name': '주문번호', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ord_tmd', 'name': '주문시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
            ]
        }
    },
    # === 주식주문(정정취소) ===
    'TTTC0013U': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'krx_fwdg_ord_orgno', 'name': '한국거래소전송주문조직번호', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'odno', 'name': '주문번호', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ord_tmd', 'name': '주문시각', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
            ]
        }
    },
    # === 주식정정취소가능주문조회 ===
    'TTTC0084R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'ord_gno_brno', 'name': '주문채번지점번호', 'type': 'string', 'required': True, 'length': 5, 'description': '주문시 한국투자증권 시스템에서 지정된 영업점코드'},
                {'key': 'odno', 'name': '주문번호', 'type': 'string', 'required': True, 'length': 10, 'description': '주문시 한국투자증권 시스템에서 채번된 주문번호'},
                {'key': 'orgn_odno', 'name': '원주문번호', 'type': 'string', 'required': True, 'length': 6, 'description': '정정/취소주문 인경우 원주문번호'},
                {'key': 'ord_dvsn_name', 'name': '주문구분명', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'pdno', 'name': '상품번호', 'type': 'string', 'required': True, 'length': 10, 'description': '종목번호(뒤 6자리만 해당)'},
                {'key': 'prdt_name', 'name': '상품명', 'type': 'string', 'required': True, 'length': 6, 'description': '종목명'},
                {'key': 'rvse_cncl_dvsn_name', 'name': '정정취소구분명', 'type': 'string', 'required': True, 'length': 5, 'description': '정정 또는 취소 여부 표시'},
                {'key': 'ord_qty', 'name': '주문수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ord_unpr', 'name': '주문단가', 'type': 'string', 'required': True, 'length': 6, 'description': '1주당 주문가격'},
                {'key': 'ord_tmd', 'name': '주문시각', 'type': 'string', 'required': True, 'length': 5, 'description': '주문시각(시분초HHMMSS)'},
                {'key': 'tot_ccld_qty', 'name': '총체결수량', 'type': 'string', 'required': True, 'length': 10, 'description': '주문 수량 중 체결된 수량'},
                {'key': 'tot_ccld_amt', 'name': '총체결금액', 'type': 'string', 'required': True, 'length': 6, 'description': '주문금액 중 체결금액'},
                {'key': 'psbl_qty', 'name': '가능수량', 'type': 'string', 'required': True, 'length': 5, 'description': '정정/취소 주문 가능 수량'},
                {'key': 'sll_buy_dvsn_cd', 'name': '매도매수구분코드', 'type': 'string', 'required': True, 'length': 10, 'description': '01 : 매도 / 02 : 매수'},
                {'key': 'ord_dvsn_cd', 'name': '주문구분코드', 'type': 'string', 'required': True, 'length': 6, 'description': '[KRX] 00 : 지정가 01 : 시장가 02 : 조건부지정가 03 : 최유리지정가 04 : 최우선지정가 05 : 장전 시간외 06 : 장후 시간외 07 : 시간외 단일가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소) 21 : 중간가 22 : 스톱지정가 23 : 중간가IOC 24 : 중간가FOK  [NXT] 00 : 지정가 03 : 최유리지정가 04 : 최우선지정가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소) 21 : 중간가 22 : 스톱지정가 23 : 중간가IOC 24 : 중간가FOK  [SOR] 00 : 지정가 01 : 시장가 03 : 최유리지정가 04 : 최우선지정가 11 : IOC지정가 (즉시체결,잔량취소) 12 : FOK지정가 (즉시체결,전량취소) 13 : IOC시장가 (즉시체결,잔량취소) 14 : FOK시장가 (즉시체결,전량취소) 15 : IOC최유리 (즉시체결,잔량취소) 16 : FOK최유리 (즉시체결,전량취소)'},
                {'key': 'mgco_aptm_odno', 'name': '운용사지정주문번호', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'excg_dvsn_cd', 'name': '거래소구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'excg_id_dvsn_cd', 'name': '거래소ID구분코드', 'type': 'string', 'required': True, 'length': 3, 'description': ''},
                {'key': 'excg_id_dvsn_name', 'name': '거래소ID구분명', 'type': 'string', 'required': True, 'length': 100, 'description': ''},
                {'key': 'stpm_cndt_pric', 'name': '스톱지정가조건가격', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'stpm_efct_occr_yn', 'name': '스톱지정가효력발생여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''}
            ]
        }
    },
    # === 주식일별주문체결조회 ===
    '(3개월이내) TTTC0081R (3개월이전) CTSC9215R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'ord_dt', 'name': '주문일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'ord_gno_brno', 'name': '주문채번지점번호', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'odno', 'name': '주문번호', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'orgn_odno', 'name': '원주문번호', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ord_dvsn_name', 'name': '주문구분명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'sll_buy_dvsn_cd', 'name': '매도매수구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'sll_buy_dvsn_cd_name', 'name': '매도매수구분코드명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'pdno', 'name': '상품번호', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'prdt_name', 'name': '상품명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'ord_qty', 'name': '주문수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ord_unpr', 'name': '주문단가', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ord_tmd', 'name': '주문시각', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'tot_ccld_qty', 'name': '총체결수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'avg_prvs', 'name': '평균가', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'cncl_yn', 'name': '취소여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'tot_ccld_amt', 'name': '총체결금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'loan_dt', 'name': '대출일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'ordr_empno', 'name': '주문자사번', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'ord_dvsn_cd', 'name': '주문구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'cnc_cfrm_qty', 'name': '취소확인수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'rmn_qty', 'name': '잔여수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'rjct_qty', 'name': '거부수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ccld_cndt_name', 'name': '체결조건명', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'inqr_ip_addr', 'name': '조회IP주소', 'type': 'string', 'required': True, 'length': 15, 'description': ''},
                {'key': 'cpbc_ordp_ord_rcit_dvsn_cd', 'name': '전산주문표주문접수구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'cpbc_ordp_infm_mthd_dvsn_cd', 'name': '전산주문표통보방법구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'infm_tmd', 'name': '통보시각', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'ctac_tlno', 'name': '연락전화번호', 'type': 'string', 'required': True, 'length': 20, 'description': ''},
                {'key': 'prdt_type_cd', 'name': '상품유형코드', 'type': 'string', 'required': True, 'length': 3, 'description': ''},
                {'key': 'excg_dvsn_cd', 'name': '거래소구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'cpbc_ordp_mtrl_dvsn_cd', 'name': '전산주문표자료구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'ord_orgno', 'name': '주문조직번호', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'rsvn_ord_end_dt', 'name': '예약주문종료일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'excg_id_dvsn_Cd', 'name': '거래소ID구분코드', 'type': 'string', 'required': True, 'length': 3, 'description': ''},
                {'key': 'stpm_cndt_pric', 'name': '스톱지정가조건가격', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'stpm_efct_occr_dtmd', 'name': '스톱지정가효력발생상세시각', 'type': 'string', 'required': True, 'length': 9, 'description': ''}
            ]
        },
        'output2': {
            'type': 'object',
            'fields': [
                {'key': 'tot_ord_qty', 'name': '총주문수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'tot_ccld_qty', 'name': '총체결수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'tot_ccld_amt', 'name': '매입평균가격', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'prsm_tlex_smtl', 'name': '총체결금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'pchs_avg_pric', 'name': '추정제비용합계', 'type': 'string', 'required': True, 'length': 184, 'description': ''}
            ]
        }
    },
    # === 주식잔고조회 ===
    'TTTC8434R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': '0 : 성공 0 이외의 값 : 실패'},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': '응답코드'},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': '응답메세지'},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'ctx_area_fk100', 'name': '연속조회검색조건100', 'type': 'string', 'required': True, 'length': 100, 'description': ''},
                {'key': 'ctx_area_nk100', 'name': '연속조회키100', 'type': 'string', 'required': True, 'length': 100, 'description': ''}
            ]
        },
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'pdno', 'name': '상품번호', 'type': 'string', 'required': True, 'length': 12, 'description': '종목번호(뒷 6자리)'},
                {'key': 'prdt_name', 'name': '상품명', 'type': 'string', 'required': True, 'length': 60, 'description': '종목명'},
                {'key': 'trad_dvsn_name', 'name': '매매구분명', 'type': 'string', 'required': True, 'length': 60, 'description': '매수매도구분'},
                {'key': 'bfdy_buy_qty', 'name': '전일매수수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'bfdy_sll_qty', 'name': '전일매도수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'thdt_buyqty', 'name': '금일매수수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'thdt_sll_qty', 'name': '금일매도수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hldg_qty', 'name': '보유수량', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ord_psbl_qty', 'name': '주문가능수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'pchs_avg_pric', 'name': '매입평균가격', 'type': 'string', 'required': True, 'length': 22, 'description': '매입금액 / 보유수량'},
                {'key': 'pchs_amt', 'name': '매입금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'prpr', 'name': '현재가', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_amt', 'name': '평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_pfls_amt', 'name': '평가손익금액', 'type': 'string', 'required': True, 'length': 19, 'description': '평가금액 - 매입금액'},
                {'key': 'evlu_pfls_rt', 'name': '평가손익율', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'evlu_erng_rt', 'name': '평가수익율', 'type': 'string', 'required': True, 'length': 31, 'description': '미사용항목(0으로 출력)'},
                {'key': 'loan_dt', 'name': '대출일자', 'type': 'string', 'required': True, 'length': 8, 'description': 'INQR_DVSN(조회구분)을 01(대출일별)로 설정해야 값이 나옴'},
                {'key': 'loan_amt', 'name': '대출금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'stln_slng_chgs', 'name': '대주매각대금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'expd_dt', 'name': '만기일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'fltt_rt', 'name': '등락율', 'type': 'string', 'required': True, 'length': 31, 'description': ''},
                {'key': 'bfdy_cprs_icdc', 'name': '전일대비증감', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'item_mgna_rt_name', 'name': '종목증거금율명', 'type': 'string', 'required': True, 'length': 20, 'description': ''},
                {'key': 'grta_rt_name', 'name': '보증금율명', 'type': 'string', 'required': True, 'length': 20, 'description': ''},
                {'key': 'sbst_pric', 'name': '대용가격', 'type': 'string', 'required': True, 'length': 19, 'description': '증권매매의 위탁보증금으로서 현금 대신에 사용되는 유가증권 가격'},
                {'key': 'stck_loan_unpr', 'name': '주식대출단가', 'type': 'string', 'required': True, 'length': 22, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'dnca_tot_amt', 'name': '예수금총금액', 'type': 'string', 'required': True, 'length': 19, 'description': '예수금'},
                {'key': 'nxdy_excc_amt', 'name': '익일정산금액', 'type': 'string', 'required': True, 'length': 19, 'description': 'D+1 예수금'},
                {'key': 'prvs_rcdl_excc_amt', 'name': '가수도정산금액', 'type': 'string', 'required': True, 'length': 19, 'description': 'D+2 예수금'},
                {'key': 'cma_evlu_amt', 'name': 'CMA평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'bfdy_buy_amt', 'name': '전일매수금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'thdt_buy_amt', 'name': '금일매수금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'nxdy_auto_rdpt_amt', 'name': '익일자동상환금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'bfdy_sll_amt', 'name': '전일매도금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'thdt_sll_amt', 'name': '금일매도금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'd2_auto_rdpt_amt', 'name': 'D+2자동상환금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'bfdy_tlex_amt', 'name': '전일제비용금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'thdt_tlex_amt', 'name': '금일제비용금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_loan_amt', 'name': '총대출금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'scts_evlu_amt', 'name': '유가평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_evlu_amt', 'name': '총평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': '유가증권 평가금액 합계금액 + D+2 예수금'},
                {'key': 'nass_amt', 'name': '순자산금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'fncg_gld_auto_rdpt_yn', 'name': '융자금자동상환여부', 'type': 'string', 'required': True, 'length': 1, 'description': '보유현금에 대한 융자금만 차감여부 신용융자 매수체결 시점에서는 융자비율을 매매대금 100%로 계산 하였다가 수도결제일에 보증금에 해당하는 금액을 고객의 현금으로 충당하여 융자금을 감소시키는 업무'},
                {'key': 'pchs_amt_smtl_amt', 'name': '매입금액합계금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_amt_smtl_amt', 'name': '평가금액합계금액', 'type': 'string', 'required': True, 'length': 19, 'description': '유가증권 평가금액 합계금액'},
                {'key': 'evlu_pfls_smtl_amt', 'name': '평가손익합계금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_stln_slng_chgs', 'name': '총대주매각대금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'bfdy_tot_asst_evlu_amt', 'name': '전일총자산평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'asst_icdc_amt', 'name': '자산증감액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'asst_icdc_erng_rt', 'name': '자산증감수익율', 'type': 'string', 'required': True, 'length': 31, 'description': '데이터 미제공'}
            ]
        }
    },
    # === 매수가능조회 ===
    'TTTC8908R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': '0 : 성공 0 이외의 값 : 실패'},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': '응답코드'},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': '응답메세지'},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'ord_psbl_cash', 'name': '주문가능현금', 'type': 'string', 'required': True, 'length': 19, 'description': '예수금으로 계산된 주문가능금액'},
                {'key': 'ord_psbl_sbst', 'name': '주문가능대용', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ruse_psbl_amt', 'name': '재사용가능금액', 'type': 'string', 'required': True, 'length': 19, 'description': '전일/금일 매도대금으로 계산된 주문가능금액'},
                {'key': 'fund_rpch_chgs', 'name': '펀드환매대금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'psbl_qty_calc_unpr', 'name': '가능수량계산단가', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'nrcvb_buy_amt', 'name': '미수없는매수금액', 'type': 'string', 'required': True, 'length': 19, 'description': '미수를 사용하지 않으실 경우 nrcvb_buy_amt(미수없는매수금액)을 확인'},
                {'key': 'nrcvb_buy_qty', 'name': '미수없는매수수량', 'type': 'string', 'required': True, 'length': 10, 'description': '미수를 사용하지 않으실 경우 nrcvb_buy_qty(미수없는매수수량)을 확인  * 특정 종목 전량매수 시 가능수량을 확인하실 경우   조회 시 ORD_DVSN:01(시장가)로 지정 필수 * 다만, 조건부지정가 등 특정 주문구분(ex.IOC)으로 주문 시 가능수량을 확인할 경우 주문 시와 동일한 주문구분(ex.IOC) 입력'},
                {'key': 'max_buy_amt', 'name': '최대매수금액', 'type': 'string', 'required': True, 'length': 19, 'description': '미수를 사용하시는 경우 max_buy_amt(최대매수금액)를 확인'},
                {'key': 'max_buy_qty', 'name': '최대매수수량', 'type': 'string', 'required': True, 'length': 10, 'description': '미수를 사용하시는 경우 max_buy_qty(최대매수수량)를 확인  * 특정 종목 전량매수 시 가능수량을 확인하실 경우   조회 시 ORD_DVSN:01(시장가)로 지정 필수 * 다만, 조건부지정가 등 특정 주문구분(ex.IOC)으로 주문 시 가능수량을 확인할 경우 주문 시와 동일한 주문구분(ex.IOC) 입력'},
                {'key': 'cma_evlu_amt', 'name': 'CMA평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ovrs_re_use_amt_wcrc', 'name': '해외재사용금액원화', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ord_psbl_frcr_amt_wcrc', 'name': '주문가능외화금액원화', 'type': 'string', 'required': True, 'length': 19, 'description': ''}
            ]
        }
    },
    # === 매도가능수량조회 ===
    'TTTC8408R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'pdno', 'name': '상품번호', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'prdt_name', 'name': '상품명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'buy_qty', 'name': '매수수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'sll_qty', 'name': '매도수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'cblc_qty', 'name': '잔고수량', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'nsvg_qty', 'name': '비저축수량', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ord_psbl_qty', 'name': '주문가능수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'pchs_avg_pric', 'name': '매입평균가격', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'pchs_amt', 'name': '매입금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'now_pric', 'name': '현재가', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'evlu_amt', 'name': '평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_pfls_amt', 'name': '평가손익금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_pfls_rt', 'name': '평가손익율', 'type': 'string', 'required': True, 'length': 72, 'description': ''}
            ]
        }
    },
    # === 신용매수가능조회 ===
    'TTTC8909R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': '0 : 성공 0 이외의 값 : 실패'},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': '응답코드'},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': '응답메시지'},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'ord_psbl_cash', 'name': '주문가능현금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ord_psbl_sbst', 'name': '주문가능대용', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ruse_psbl_amt', 'name': '재사용가능금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'fund_rpch_chgs', 'name': '펀드환매대금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'psbl_qty_calc_unpr', 'name': '가능수량계산단가', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'nrcvb_buy_amt', 'name': '미수없는매수금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'nrcvb_buy_qty', 'name': '미수없는매수수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'max_buy_amt', 'name': '최대매수금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'max_buy_qty', 'name': '최대매수수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'cma_evlu_amt', 'name': 'CMA평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ovrs_re_use_amt_wcrc', 'name': '해외재사용금액원화', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ord_psbl_frcr_amt_wcrc', 'name': '주문가능외화금액원화', 'type': 'string', 'required': True, 'length': 19, 'description': ''}
            ]
        }
    },
    # === 주식예약주문 ===
    'CTSC0008U': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': '0 : 성공  0 이외의 값 : 실패'},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'rsvn_ord_seq', 'name': '예약주문순번', 'type': 'string', 'required': False, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 주식예약주문정정취소 ===
    '(예약취소) CTSC0009U (예약정정) CTSC0013U': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': '0 : 성공  0 이외의 값 : 실패'},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'nrml_prcs_yn', 'name': '정상처리여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''}
            ]
        }
    },
    # === 주식예약주문조회 ===
    'CTSC0004R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': '0 : 성공  0 이외의 값 : 실패'},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'rsvn_ord_seq', 'name': '예약주문순번', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'rsvn_ord_ord_dt', 'name': '예약주문주문일자', 'type': 'string', 'required': False, 'length': 8, 'description': ''},
                {'key': 'rsvn_ord_rcit_dt', 'name': '예약주문접수일자', 'type': 'string', 'required': False, 'length': 8, 'description': ''},
                {'key': 'pdno', 'name': '상품번호', 'type': 'string', 'required': False, 'length': 12, 'description': ''},
                {'key': 'ord_dvsn_cd', 'name': '주문구분코드', 'type': 'string', 'required': False, 'length': 2, 'description': ''},
                {'key': 'ord_rsvn_qty', 'name': '주문예약수량', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'tot_ccld_qty', 'name': '총체결수량', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'cncl_ord_dt', 'name': '취소주문일자', 'type': 'string', 'required': False, 'length': 8, 'description': ''},
                {'key': 'ord_tmd', 'name': '주문시각', 'type': 'string', 'required': False, 'length': 6, 'description': ''},
                {'key': 'ctac_tlno', 'name': '연락전화번호', 'type': 'string', 'required': False, 'length': 20, 'description': ''},
                {'key': 'rjct_rson2', 'name': '거부사유2', 'type': 'string', 'required': False, 'length': 200, 'description': ''},
                {'key': 'odno', 'name': '주문번호', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'rsvn_ord_rcit_tmd', 'name': '예약주문접수시각', 'type': 'string', 'required': False, 'length': 6, 'description': ''},
                {'key': 'kor_item_shtn_name', 'name': '한글종목단축명', 'type': 'string', 'required': False, 'length': 60, 'description': ''},
                {'key': 'sll_buy_dvsn_cd', 'name': '매도매수구분코드', 'type': 'string', 'required': False, 'length': 2, 'description': ''},
                {'key': 'ord_rsvn_unpr', 'name': '주문예약단가', 'type': 'string', 'required': False, 'length': 19, 'description': ''},
                {'key': 'tot_ccld_amt', 'name': '총체결금액', 'type': 'string', 'required': False, 'length': 19, 'description': ''},
                {'key': 'loan_dt', 'name': '대출일자', 'type': 'string', 'required': False, 'length': 8, 'description': ''},
                {'key': 'cncl_rcit_tmd', 'name': '취소접수시각', 'type': 'string', 'required': False, 'length': 6, 'description': ''},
                {'key': 'prcs_rslt', 'name': '처리결과', 'type': 'string', 'required': False, 'length': 60, 'description': ''},
                {'key': 'ord_dvsn_name', 'name': '주문구분명', 'type': 'string', 'required': False, 'length': 60, 'description': ''},
                {'key': 'tmnl_mdia_kind_cd', 'name': '단말매체종류코드', 'type': 'string', 'required': False, 'length': 2, 'description': ''},
                {'key': 'rsvn_end_dt', 'name': '예약종료일자', 'type': 'string', 'required': False, 'length': 8, 'description': ''}
            ]
        }
    },
    # === 퇴직연금 체결기준잔고 ===
    'TTTC2202R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'cblc_dvsn', 'name': '잔고구분', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'cblc_dvsn_name', 'name': '잔고구분명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'pdno', 'name': '상품번호', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'prdt_name', 'name': '상품명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'hldg_qty', 'name': '보유수량', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'slpsb_qty', 'name': '매도가능수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'pchs_avg_pric', 'name': '매입평균가격', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'evlu_pfls_amt', 'name': '평가손익금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_pfls_rt', 'name': '평가손익율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'prpr', 'name': '현재가', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_amt', 'name': '평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'pchs_amt', 'name': '매입금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'cblc_weit', 'name': '잔고비중', 'type': 'string', 'required': True, 'length': 238, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'pchs_amt_smtl_amt', 'name': '매입금액합계금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_amt_smtl_amt', 'name': '평가금액합계금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_pfls_smtl_amt', 'name': '평가손익합계금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'trad_pfls_smtl', 'name': '매매손익합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'thdt_tot_pfls_amt', 'name': '당일총손익금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'pftrt', 'name': '수익률', 'type': 'string', 'required': True, 'length': 238, 'description': ''}
            ]
        }
    },
    # === 퇴직연금 미체결내역 ===
    'TTTC2201R(기존 KRX만 가능), TTTC2210R (KRX,NXT/SOR)': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'ord_gno_brno', 'name': '주문채번지점번호', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'sll_buy_dvsn_cd', 'name': '매도매수구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'trad_dvsn_name', 'name': '매매구분명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'odno', 'name': '주문번호', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'pdno', 'name': '상품번호', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'prdt_name', 'name': '상품명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'ord_unpr', 'name': '주문단가', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ord_qty', 'name': '주문수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'tot_ccld_qty', 'name': '총체결수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'nccs_qty', 'name': '미체결수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ord_dvsn_cd', 'name': '주문구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'ord_dvsn_name', 'name': '주문구분명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'orgn_odno', 'name': '원주문번호', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ord_tmd', 'name': '주문시각', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'objt_cust_dvsn_name', 'name': '대상고객구분명', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'pchs_avg_pric', 'name': '매입평균가격', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stpm_cndt_pric', 'name': '스톱지정가조건가격', 'type': 'string', 'required': True, 'length': 9, 'description': '신규 API용 필드'},
                {'key': 'stpm_efct_occr_dtmd', 'name': '스톱지정가효력발생상세시각', 'type': 'string', 'required': True, 'length': 9, 'description': '신규 API용 필드'},
                {'key': 'stpm_efct_occr_yn', 'name': '스톱지정가효력발생여부', 'type': 'string', 'required': True, 'length': 1, 'description': '신규 API용 필드'},
                {'key': 'excg_id_dvsn_cd', 'name': '거래소ID구분코드', 'type': 'string', 'required': True, 'length': 3, 'description': '신규 API용 필드'}
            ]
        }
    },
    # === 퇴직연금 매수가능조회 ===
    'TTTC0503R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'ord_psbl_cash', 'name': '주문가능현금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ruse_psbl_amt', 'name': '재사용가능금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'psbl_qty_calc_unpr', 'name': '가능수량계산단가', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'max_buy_amt', 'name': '최대매수금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'max_buy_qty', 'name': '최대매수수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 퇴직연금 예수금조회 ===
    'TTTC0506R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'dnca_tota', 'name': '예수금총액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'nxdy_excc_amt', 'name': '익일정산액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'nxdy_sttl_amt', 'name': '익일결제금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'nx2_day_sttl_amt', 'name': '2익일결제금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''}
            ]
        }
    },
    # === 퇴직연금 잔고조회 ===
    'TTTC2208R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'cblc_dvsn_name', 'name': '잔고구분명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'prdt_name', 'name': '상품명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'pdno', 'name': '상품번호', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'item_dvsn_name', 'name': '종목구분명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'thdt_buyqty', 'name': '금일매수수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'thdt_sll_qty', 'name': '금일매도수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hldg_qty', 'name': '보유수량', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ord_psbl_qty', 'name': '주문가능수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'pchs_avg_pric', 'name': '매입평균가격', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'pchs_amt', 'name': '매입금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'prpr', 'name': '현재가', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_amt', 'name': '평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_pfls_amt', 'name': '평가손익금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_erng_rt', 'name': '평가수익율', 'type': 'string', 'required': True, 'length': 238, 'description': ''}
            ]
        },
        'output2': {
            'type': 'object',
            'fields': [
                {'key': 'dnca_tot_amt', 'name': '예수금총금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'nxdy_excc_amt', 'name': '익일정산금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'prvs_rcdl_excc_amt', 'name': '가수도정산금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'thdt_buy_amt', 'name': '금일매수금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'thdt_sll_amt', 'name': '금일매도금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'thdt_tlex_amt', 'name': '금일제비용금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'scts_evlu_amt', 'name': '유가평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_evlu_amt', 'name': '총평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''}
            ]
        }
    },
    # === 주식잔고조회_실현손익 ===
    'TTTC8494R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'pdno', 'name': '상품번호', 'type': 'string', 'required': True, 'length': 12, 'description': '종목번호(뒷 6자리)'},
                {'key': 'prdt_name', 'name': '상품명', 'type': 'string', 'required': True, 'length': 60, 'description': '종목명'},
                {'key': 'trad_dvsn_name', 'name': '매매구분명', 'type': 'string', 'required': True, 'length': 60, 'description': '매수매도구분'},
                {'key': 'bfdy_buy_qty', 'name': '전일매수수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'bfdy_sll_qty', 'name': '전일매도수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'thdt_buyqty', 'name': '금일매수수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'thdt_sll_qty', 'name': '금일매도수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hldg_qty', 'name': '보유수량', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ord_psbl_qty', 'name': '주문가능수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'pchs_avg_pric', 'name': '매입평균가격', 'type': 'string', 'required': True, 'length': 23, 'description': '매입금액 / 보유수량'},
                {'key': 'pchs_amt', 'name': '매입금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'prpr', 'name': '현재가', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_amt', 'name': '평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_pfls_amt', 'name': '평가손익금액', 'type': 'string', 'required': True, 'length': 19, 'description': '평가금액 - 매입금액'},
                {'key': 'evlu_pfls_rt', 'name': '평가손익율', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'evlu_erng_rt', 'name': '평가수익율', 'type': 'string', 'required': True, 'length': 32, 'description': ''},
                {'key': 'loan_dt', 'name': '대출일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'loan_amt', 'name': '대출금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'stln_slng_chgs', 'name': '대주매각대금', 'type': 'string', 'required': True, 'length': 19, 'description': '신용 거래에서, 고객이 증권 회사로부터 대부받은 주식의 매각 대금'},
                {'key': 'expd_dt', 'name': '만기일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stck_loan_unpr', 'name': '주식대출단가', 'type': 'string', 'required': True, 'length': 23, 'description': ''},
                {'key': 'bfdy_cprs_icdc', 'name': '전일대비증감', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'fltt_rt', 'name': '등락율', 'type': 'string', 'required': True, 'length': 32, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'dnca_tot_amt', 'name': '예수금총금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'nxdy_excc_amt', 'name': '익일정산금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'prvs_rcdl_excc_amt', 'name': '가수도정산금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'cma_evlu_amt', 'name': 'CMA평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'bfdy_buy_amt', 'name': '전일매수금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'thdt_buy_amt', 'name': '금일매수금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'nxdy_auto_rdpt_amt', 'name': '익일자동상환금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'bfdy_sll_amt', 'name': '전일매도금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'thdt_sll_amt', 'name': '금일매도금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'd2_auto_rdpt_amt', 'name': 'D+2자동상환금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'bfdy_tlex_amt', 'name': '전일제비용금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'thdt_tlex_amt', 'name': '금일제비용금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_loan_amt', 'name': '총대출금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'scts_evlu_amt', 'name': '유가평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_evlu_amt', 'name': '총평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'nass_amt', 'name': '순자산금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'fncg_gld_auto_rdpt_yn', 'name': '융자금자동상환여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'pchs_amt_smtl_amt', 'name': '매입금액합계금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_amt_smtl_amt', 'name': '평가금액합계금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_pfls_smtl_amt', 'name': '평가손익합계금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_stln_slng_chgs', 'name': '총대주매각대금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'bfdy_tot_asst_evlu_amt', 'name': '전일총자산평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'asst_icdc_amt', 'name': '자산증감액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'asst_icdc_erng_rt', 'name': '자산증감수익율', 'type': 'string', 'required': True, 'length': 32, 'description': ''},
                {'key': 'rlzt_pfls', 'name': '실현손익', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'rlzt_erng_rt', 'name': '실현수익율', 'type': 'string', 'required': True, 'length': 32, 'description': ''},
                {'key': 'real_evlu_pfls', 'name': '실평가손익', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'real_evlu_pfls_erng_rt', 'name': '실평가손익수익율', 'type': 'string', 'required': True, 'length': 32, 'description': ''}
            ]
        }
    },
    # === 투자계좌자산현황조회 ===
    'CTRP6548R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'Output1': {
            'type': 'array',
            'fields': [
                {'key': 'pchs_amt', 'name': '매입금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_amt', 'name': '평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_pfls_amt', 'name': '평가손익금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'crdt_lnd_amt', 'name': '신용대출금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'real_nass_amt', 'name': '실제순자산금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'whol_weit_rt', 'name': '전체비중율', 'type': 'string', 'required': True, 'length': 228, 'description': ''}
            ]
        },
        'Output2': {
            'type': 'object',
            'fields': [
                {'key': 'pchs_amt_smtl', 'name': '매입금액합계', 'type': 'string', 'required': True, 'length': 19, 'description': '유가매입금액'},
                {'key': 'nass_tot_amt', 'name': '순자산총금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'loan_amt_smtl', 'name': '대출금액합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'evlu_pfls_amt_smtl', 'name': '평가손익금액합계', 'type': 'string', 'required': True, 'length': 19, 'description': '평가손익금액'},
                {'key': 'evlu_amt_smtl', 'name': '평가금액합계', 'type': 'string', 'required': True, 'length': 19, 'description': '유가평가금액'},
                {'key': 'tot_asst_amt', 'name': '총자산금액', 'type': 'string', 'required': True, 'length': 19, 'description': '총 자산금액'},
                {'key': 'tot_lnda_tot_ulst_lnda', 'name': '총대출금액총융자대출금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'cma_auto_loan_amt', 'name': 'CMA자동대출금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_mgln_amt', 'name': '총담보대출금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'stln_evlu_amt', 'name': '대주평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'crdt_fncg_amt', 'name': '신용융자금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ocl_apl_loan_amt', 'name': 'OCL_APL대출금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'pldg_stup_amt', 'name': '질권설정금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'frcr_evlu_tota', 'name': '외화평가총액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_dncl_amt', 'name': '총예수금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'cma_evlu_amt', 'name': 'CMA평가금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'dncl_amt', 'name': '예수금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_sbst_amt', 'name': '총대용금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'thdt_rcvb_amt', 'name': '당일미수금액', 'type': 'string', 'required': True, 'length': 20, 'description': ''},
                {'key': 'ovrs_stck_evlu_amt1', 'name': '해외주식평가금액1', 'type': 'string', 'required': True, 'length': 236, 'description': ''},
                {'key': 'ovrs_bond_evlu_amt', 'name': '해외채권평가금액', 'type': 'string', 'required': True, 'length': 236, 'description': ''},
                {'key': 'mmf_cma_mgge_loan_amt', 'name': 'MMFCMA담보대출금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'sbsc_dncl_amt', 'name': '청약예수금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'pbst_sbsc_fnds_loan_use_amt', 'name': '공모주청약자금대출사용금액', 'type': 'string', 'required': True, 'length': 20, 'description': ''},
                {'key': 'etpr_crdt_grnt_loan_amt', 'name': '기업신용공여대출금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''}
            ]
        }
    },
    # === 기간별손익일별합산조회 ===
    'TTTC8708R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'trad_dt', 'name': '매매일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'buy_amt', 'name': '매수금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'sll_amt', 'name': '매도금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'rlzt_pfls', 'name': '실현손익', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'fee', 'name': '수수료', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'loan_int', 'name': '대출이자', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tl_tax', 'name': '제세금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'pfls_rt', 'name': '손익률', 'type': 'string', 'required': True, 'length': 238, 'description': ''},
                {'key': 'sll_qty1', 'name': '매도수량1', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'buy_qty1', 'name': '매수수량1', 'type': 'string', 'required': True, 'length': 9, 'description': ''}
            ]
        },
        'output2': {
            'type': 'object',
            'fields': [
                {'key': 'sll_qty_smtl', 'name': '매도수량합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'sll_tr_amt_smtl', 'name': '매도거래금액합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'sll_fee_smtl', 'name': '매도수수료합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'sll_tltx_smtl', 'name': '매도제세금합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'sll_excc_amt_smtl', 'name': '매도정산금액합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'buy_qty_smtl', 'name': '매수수량합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'buy_tr_amt_smtl', 'name': '매수거래금액합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'buy_fee_smtl', 'name': '매수수수료합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'buy_tax_smtl', 'name': '매수제세금합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'buy_excc_amt_smtl', 'name': '매수정산금액합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_qty', 'name': '총수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'tot_tr_amt', 'name': '총거래금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_fee', 'name': '총수수료', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_tltx', 'name': '총제세금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_excc_amt', 'name': '총정산금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_rlzt_pfls', 'name': '총실현손익', 'type': 'string', 'required': True, 'length': 19, 'description': '※ HTS[0856] 기간별 매매손익 \'일별\' 화면의 우측 하단 \'총손익률\' 항목은  기간별매매손익현황조회(TTTC8715R) > output2 > tot_pftrt(총수익률) 으로 확인 가능'},
                {'key': 'loan_int', 'name': '대출이자', 'type': 'string', 'required': True, 'length': 19, 'description': ''}
            ]
        }
    },
    # === 기간별매매손익현황조회 ===
    'TTTC8715R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'ctx_area_nk100', 'name': '연속조회키100', 'type': 'string', 'required': True, 'length': 100, 'description': ''},
                {'key': 'ctx_area_fk100', 'name': '연속조회검색조건100', 'type': 'string', 'required': True, 'length': 100, 'description': ''}
            ]
        },
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'trad_dt', 'name': '매매일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'pdno', 'name': '상품번호', 'type': 'string', 'required': True, 'length': 12, 'description': '종목번호(뒤 6자리만 해당)'},
                {'key': 'prdt_name', 'name': '상품명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'trad_dvsn_name', 'name': '매매구분명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'loan_dt', 'name': '대출일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'hldg_qty', 'name': '보유수량', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'pchs_unpr', 'name': '매입단가', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'buy_qty', 'name': '매수수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'buy_amt', 'name': '매수금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'sll_pric', 'name': '매도가격', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'sll_qty', 'name': '매도수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'sll_amt', 'name': '매도금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'rlzt_pfls', 'name': '실현손익', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'pfls_rt', 'name': '손익률', 'type': 'string', 'required': True, 'length': 238, 'description': ''},
                {'key': 'fee', 'name': '수수료', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tl_tax', 'name': '제세금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'loan_int', 'name': '대출이자', 'type': 'string', 'required': True, 'length': 19, 'description': ''}
            ]
        },
        'output2': {
            'type': 'object',
            'fields': [
                {'key': 'sll_qty_smtl', 'name': '매도수량합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'sll_tr_amt_smtl', 'name': '매도거래금액합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'sll_fee_smtl', 'name': '매도수수료합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'sll_tltx_smtl', 'name': '매도제세금합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'sll_excc_amt_smtl', 'name': '매도정산금액합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'buyqty_smtl', 'name': '매수수량합계', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'buy_tr_amt_smtl', 'name': '매수거래금액합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'buy_fee_smtl', 'name': '매수수수료합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'buy_tax_smtl', 'name': '매수제세금합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'buy_excc_amt_smtl', 'name': '매수정산금액합계', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_qty', 'name': '총수량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'tot_tr_amt', 'name': '총거래금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_fee', 'name': '총수수료', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_tltx', 'name': '총제세금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_excc_amt', 'name': '총정산금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_rlzt_pfls', 'name': '총실현손익', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'loan_int', 'name': '대출이자', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_pftrt', 'name': '총수익률', 'type': 'string', 'required': True, 'length': 238, 'description': ''}
            ]
        }
    },
    # === 주식통합증거금 현황 ===
    'TTTC0869R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'acmga_rt', 'name': '계좌증거금율', 'type': 'string', 'required': True, 'length': 114, 'description': ''},
                {'key': 'acmga_pct100_aptm_rson', 'name': '계좌증거금100퍼센트지정사유', 'type': 'string', 'required': True, 'length': 100, 'description': ''},
                {'key': 'stck_cash_objt_amt', 'name': '주식현금대상금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_sbst_objt_amt', 'name': '주식대용대상금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_evlu_objt_amt', 'name': '주식평가대상금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_ruse_psbl_objt_amt', 'name': '주식재사용가능대상금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_fund_rpch_chgs_objt_amt', 'name': '주식펀드환매대금대상금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_fncg_rdpt_objt_atm', 'name': '주식융자상환금대상금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'bond_ruse_psbl_objt_amt', 'name': '채권재사용가능대상금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_cash_use_amt', 'name': '주식현금사용금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_sbst_use_amt', 'name': '주식대용사용금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_evlu_use_amt', 'name': '주식평가사용금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_ruse_psbl_amt_use_amt', 'name': '주식재사용가능금사용금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_fund_rpch_chgs_use_amt', 'name': '주식펀드환매대금사용금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_fncg_rdpt_amt_use_amt', 'name': '주식융자상환금사용금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'bond_ruse_psbl_amt_use_amt', 'name': '채권재사용가능금사용금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_cash_ord_psbl_amt', 'name': '주식현금주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_sbst_ord_psbl_amt', 'name': '주식대용주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_evlu_ord_psbl_amt', 'name': '주식평가주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_ruse_psbl_ord_psbl_amt', 'name': '주식재사용가능주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_fund_rpch_ord_psbl_amt', 'name': '주식펀드환매주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'bond_ruse_psbl_ord_psbl_amt', 'name': '채권재사용가능주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'rcvb_amt', 'name': '미수금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'stck_loan_grta_ruse_psbl_amt', 'name': '주식대출보증금재사용가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_cash20_max_ord_psbl_amt', 'name': '주식현금20최대주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_cash30_max_ord_psbl_amt', 'name': '주식현금30최대주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_cash40_max_ord_psbl_amt', 'name': '주식현금40최대주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_cash50_max_ord_psbl_amt', 'name': '주식현금50최대주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_cash60_max_ord_psbl_amt', 'name': '주식현금60최대주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_cash100_max_ord_psbl_amt', 'name': '주식현금100최대주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_rsip100_max_ord_psbl_amt', 'name': '주식재사용불가100최대주문가능', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'bond_max_ord_psbl_amt', 'name': '채권최대주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_fncg45_max_ord_psbl_amt', 'name': '주식융자45최대주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_fncg50_max_ord_psbl_amt', 'name': '주식융자50최대주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_fncg60_max_ord_psbl_amt', 'name': '주식융자60최대주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'stck_fncg70_max_ord_psbl_amt', 'name': '주식융자70최대주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_stln_max_ord_psbl_amt', 'name': '주식대주최대주문가능금액', 'type': 'string', 'required': True, 'length': 184, 'description': ''},
                {'key': 'lmt_amt', 'name': '한도금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ovrs_stck_itgr_mgna_dvsn_name', 'name': '해외주식통합증거금구분명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'usd_objt_amt', 'name': '미화대상금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'usd_use_amt', 'name': '미화사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'usd_ord_psbl_amt', 'name': '미화주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'hkd_objt_amt', 'name': '홍콩달러대상금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'hkd_use_amt', 'name': '홍콩달러사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'hkd_ord_psbl_amt', 'name': '홍콩달러주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'jpy_objt_amt', 'name': '엔화대상금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'jpy_use_amt', 'name': '엔화사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'jpy_ord_psbl_amt', 'name': '엔화주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'cny_objt_amt', 'name': '위안화대상금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'cny_use_amt', 'name': '위안화사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'cny_ord_psbl_amt', 'name': '위안화주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'usd_ruse_objt_amt', 'name': '미화재사용대상금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'usd_ruse_amt', 'name': '미화재사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'usd_ruse_ord_psbl_amt', 'name': '미화재사용주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'hkd_ruse_objt_amt', 'name': '홍콩달러재사용대상금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'hkd_ruse_amt', 'name': '홍콩달러재사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'hkd_ruse_ord_psbl_amt', 'name': '홍콩달러재사용주문가능금액', 'type': 'string', 'required': True, 'length': 172, 'description': ''},
                {'key': 'jpy_ruse_objt_amt', 'name': '엔화재사용대상금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'jpy_ruse_amt', 'name': '엔화재사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'jpy_ruse_ord_psbl_amt', 'name': '엔화재사용주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'cny_ruse_objt_amt', 'name': '위안화재사용대상금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'cny_ruse_amt', 'name': '위안화재사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'cny_ruse_ord_psbl_amt', 'name': '위안화재사용주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'usd_gnrl_ord_psbl_amt', 'name': '미화일반주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'usd_itgr_ord_psbl_amt', 'name': '미화통합주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'hkd_gnrl_ord_psbl_amt', 'name': '홍콩달러일반주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'hkd_itgr_ord_psbl_amt', 'name': '홍콩달러통합주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'jpy_gnrl_ord_psbl_amt', 'name': '엔화일반주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'jpy_itgr_ord_psbl_amt', 'name': '엔화통합주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'cny_gnrl_ord_psbl_amt', 'name': '위안화일반주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'cny_itgr_ord_psbl_amt', 'name': '위안화통합주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_itgr_cash20_ord_psbl_amt', 'name': '주식통합현금20주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_itgr_cash30_ord_psbl_amt', 'name': '주식통합현금30주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_itgr_cash40_ord_psbl_amt', 'name': '주식통합현금40주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_itgr_cash50_ord_psbl_amt', 'name': '주식통합현금50주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_itgr_cash60_ord_psbl_amt', 'name': '주식통합현금60주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_itgr_cash100_ord_psbl_amt', 'name': '주식통합현금100주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_itgr_100_ord_psbl_amt', 'name': '주식통합100주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_itgr_fncg45_ord_psbl_amt', 'name': '주식통합융자45주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_itgr_fncg50_ord_psbl_amt', 'name': '주식통합융자50주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_itgr_fncg60_ord_psbl_amt', 'name': '주식통합융자60주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_itgr_fncg70_ord_psbl_amt', 'name': '주식통합융자70주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_itgr_stln_ord_psbl_amt', 'name': '주식통합대주주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'bond_itgr_ord_psbl_amt', 'name': '채권통합주문가능금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_cash_ovrs_use_amt', 'name': '주식현금해외사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_sbst_ovrs_use_amt', 'name': '주식대용해외사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_evlu_ovrs_use_amt', 'name': '주식평가해외사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_re_use_amt_ovrs_use_amt', 'name': '주식재사용금액해외사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_fund_rpch_ovrs_use_amt', 'name': '주식펀드환매해외사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'stck_fncg_rdpt_ovrs_use_amt', 'name': '주식융자상환해외사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'bond_re_use_ovrs_use_amt', 'name': '채권재사용해외사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'usd_oth_mket_use_amt', 'name': '미화타시장사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'jpy_oth_mket_use_amt', 'name': '엔화타시장사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'cny_oth_mket_use_amt', 'name': '위안화타시장사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'hkd_oth_mket_use_amt', 'name': '홍콩달러타시장사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'usd_re_use_oth_mket_use_amt', 'name': '미화재사용타시장사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'jpy_re_use_oth_mket_use_amt', 'name': '엔화재사용타시장사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'cny_re_use_oth_mket_use_amt', 'name': '위안화재사용타시장사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'hkd_re_use_oth_mket_use_amt', 'name': '홍콩달러재사용타시장사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'hgkg_cny_re_use_amt', 'name': '홍콩위안화재사용금액', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'usd_frst_bltn_exrt', 'name': '미국달러최초고시환율', 'type': 'string', 'required': True, 'length': 23, 'description': ''},
                {'key': 'hkd_frst_bltn_exrt', 'name': '홍콩달러최초고시환율', 'type': 'string', 'required': True, 'length': 23, 'description': ''},
                {'key': 'jpy_frst_bltn_exrt', 'name': '일본엔화최초고시환율', 'type': 'string', 'required': True, 'length': 23, 'description': ''},
                {'key': 'cny_frst_bltn_exrt', 'name': '중국위안화최초고시환율', 'type': 'string', 'required': True, 'length': 23, 'description': ''}
            ]
        }
    },
    # === 기간별계좌권리현황조회 ===
    'CTRGA011R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'acno10', 'name': '계좌번호10', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'rght_type_cd', 'name': '권리유형코드', 'type': 'string', 'required': True, 'length': 2, 'description': '1	유상 2	무상 3	배당 4	매수청구 5	공개매수 6	주주총회 7	신주인수권증서 8	반대의사 9	신주인수권증권 11	합병 12	회사분할 13	주식교환 14	액면분할 15	액면병합 16	종목변경 17	감자 18	신구주합병 21	후합병 22	후회사분할 23	후주식교환 24	후액면분할 25	후액면병합 26	후종목변경 27	후감자 28	후신구주합병 31	뮤츄얼펀드 32	ETF 33	선박투자회사 34	투융자회사 35	해외자원 36	부동산신탁(Ritz) 37	상장수익증권 41	ELW만기 42	ELS분배 43	DLS분배 44	하일드펀드 45	ETN 51	전환청구 52	교환청구 53	BW청구 54	WRT청구 55	채권풋옵션청구 56	전환우선주청구 57	전환조건부청구 58	전자증권일괄입고 59	클라우드펀딩일괄입고 61	원리금상환 62	스트립채권 71	WRT소멸 72	WRT증권 73	DR전환 74	배당옵션 75	특별배당 76	ISINCODE변경 77	실권주청약 81	해외분배금(청산) 82	해외분배금(조기상환) 83	해외분배금(상장폐지) 84	DR FEE 85	SECTION 871M 86	종목전환 87	재매수 88	종목교환 89	기타이벤트 91	공모주 92	청약 93	환매 99	기타권리사유'},
                {'key': 'bass_dt', 'name': '기준일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'rght_cblc_type_cd', 'name': '권리잔고유형코드', 'type': 'string', 'required': True, 'length': 2, 'description': '1	입고 2	출고 3	출고입고 4	출고입금 5	출고출금 10	현금입금 11	단수주대금입금 12	교부금입금 13	유상감자대금입금 14	지연이자입금 15	이자지급 16	대주권리금출금 17	분할상환 18	만기상환 19	조기상환 20	출금 21	입고&입금 22	입고&입금&단수주대금입금 25	유상환불금입금 26	중도상환 27	분할합병세금출금'},
                {'key': 'rptt_pdno', 'name': '대표상품번호', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'pdno', 'name': '상품번호', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'prdt_type_cd', 'name': '상품유형코드', 'type': 'string', 'required': True, 'length': 3, 'description': ''},
                {'key': 'shtn_pdno', 'name': '단축상품번호', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'prdt_name', 'name': '상품명', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'cblc_qty', 'name': '잔고수량', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'last_alct_qty', 'name': '최종배정수량', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'excs_alct_qty', 'name': '초과배정수량', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tot_alct_qty', 'name': '총배정수량', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'last_ftsk_qty', 'name': '최종단수주수량', 'type': 'string', 'required': True, 'length': 191, 'description': ''},
                {'key': 'last_alct_amt', 'name': '최종배정금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'last_ftsk_chgs', 'name': '최종단수주대금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'rdpt_prca', 'name': '상환원금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'dlay_int_amt', 'name': '지연이자금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'lstg_dt', 'name': '상장일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'sbsc_end_dt', 'name': '청약종료일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'cash_dfrm_dt', 'name': '현금지급일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'rqst_qty', 'name': '신청수량', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'rqst_amt', 'name': '신청금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'rqst_dt', 'name': '신청일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'rfnd_dt', 'name': '환불일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'rfnd_amt', 'name': '환불금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'lstg_stqt', 'name': '상장주수', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'tax_amt', 'name': '세금금액', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'sbsc_unpr', 'name': '청약단가', 'type': 'string', 'required': True, 'length': 224, 'description': ''}
            ]
        }
    }
}
