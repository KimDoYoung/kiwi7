# Auto-generated

TRADING_RESPONSES = {
    'CTCA0903R': {
        'output': {
            'fields': [{'description': "'기준일자(YYYYMMDD)'},", 'key': 'bass_dt', 'length': 8, 'name': '기준일자', 'required': True, 'type': 'string'}, {'description': "'01:일요일, 02:월요일, 03:화요일, 04:수요일, 05:목요일, 06:금요일, 07:토요일'},", 'key': 'wday_dvsn_cd', 'length': 2, 'name': '요일구분코드', 'required': True, 'type': 'string'}, {'description': '', 'key': 'bzdy_yn', 'length': 1, 'name': '영업일여부', 'required': True, 'type': 'string'}, {'description': '', 'key': 'tr_day_yn', 'length': 1, 'name': '거래일여부', 'required': True, 'type': 'string'}, {'description': '', 'key': 'opnd_yn', 'length': 1, 'name': '개장일여부', 'required': True, 'type': 'string'}, {'description': '', 'key': 'sttl_day_yn', 'length': 1, 'name': '결제일여부', 'required': True, 'type': 'string'}]
        }
    },
    'CTPF1002R': {
        'output': {
            'fields': [ {'description': "''},", 'key': 'pdno', 'length': 12, 'name': '상품번호', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_type_cd', 'length': 3, 'name': '상품유형코드', 'required': True, 'type': 'string'}, {'description': '', 'key': 'mket_id_cd', 'length': 3, 'name': '시장ID코드', 'required': True, 'type': 'string'}, {'description': '', 'key': 'scty_grp_id_cd', 'length': 2, 'name': '증권그룹ID코드', 'required': True, 'type': 'string'}, {'description': '', 'key': 'excg_dvsn_cd', 'length': 2, 'name': '거래소구분코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'setl_mmdd', 'length': 4, 'name': '결산월일', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'lstg_stqt', 'length': 19, 'name': '상장주수', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'lstg_cptl_amt', 'length': 19, 'name': '상장자본금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'cpta', 'length': 19, 'name': '자본금', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'papr', 'length': 19, 'name': '액면가', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'issu_pric', 'length': 19, 'name': '발행가격', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'kospi200_item_yn', 'length': 1, 'name': '코스피200종목여부', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'scts_mket_lstg_dt', 'length': 8, 'name': '유가증권시장상장일자', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'scts_mket_lstg_abol_dt', 'length': 8, 'name': '유가증권시장상장폐지일자', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'kosdaq_mket_lstg_dt', 'length': 8, 'name': '코스닥시장상장일자', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'kosdaq_mket_lstg_abol_dt', 'length': 8, 'name': '코스닥시장상장폐지일자', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'frbd_mket_lstg_dt', 'length': 8, 'name': '프리보드시장상장일자', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'frbd_mket_lstg_abol_dt', 'length': 8, 'name': '프리보드시장상장폐지일자', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'reits_kind_cd', 'length': 1, 'name': '리츠종류코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'etf_dvsn_cd', 'length': 2, 'name': 'ETF구분코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'oilf_fund_yn', 'length': 1, 'name': '유전펀드여부', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'idx_bztp_lcls_cd', 'length': 3, 'name': '지수업종대분류코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'idx_bztp_mcls_cd', 'length': 3, 'name': '지수업종중분류코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'idx_bztp_scls_cd', 'length': 3, 'name': '지수업종소분류코드', 'required': True, 'type': 'string'}, {'description': '', 'key': 'stck_kind_cd', 'length': 3, 'name': '주식종류코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'mfnd_opng_dt', 'length': 8, 'name': '뮤추얼펀드개시일자', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'mfnd_end_dt', 'length': 8, 'name': '뮤추얼펀드종료일자', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'dpsi_erlm_cncl_dt', 'length': 8, 'name': '예탁등록취소일자', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'etf_cu_qty', 'length': 10, 'name': 'ETFCU수량', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_name', 'length': 60, 'name': '상품명', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_name120', 'length': 120, 'name': '상품명120', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_abrv_name', 'length': 60, 'name': '상품약어명', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'std_pdno', 'length': 12, 'name': '표준상품번호', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_eng_name', 'length': 60, 'name': '상품영문명', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_eng_name120', 'length': 120, 'name': '상품영문명120', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_eng_abrv_name', 'length': 60, 'name': '상품영문약어명', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'dpsi_aptm_erlm_yn', 'length': 1, 'name': '예탁지정등록여부', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'etf_txtn_type_cd', 'length': 2, 'name': 'ETF과세유형코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'etf_type_cd', 'length': 2, 'name': 'ETF유형코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'lstg_abol_dt', 'length': 8, 'name': '상장폐지일자', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'nwst_odst_dvsn_cd', 'length': 2, 'name': '신주구주구분코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'sbst_pric', 'length': 19, 'name': '대용가격', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'thco_sbst_pric', 'length': 19, 'name': '당사대용가격', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'thco_sbst_pric_chng_dt', 'length': 8, 'name': '당사대용가격변경일자', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'tr_stop_yn', 'length': 1, 'name': '거래정지여부', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'admn_item_yn', 'length': 1, 'name': '관리종목여부', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'thdt_clpr', 'length': 19, 'name': '당일종가', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'bfdy_clpr', 'length': 19, 'name': '전일종가', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'clpr_chng_dt', 'length': 8, 'name': '종가변경일자', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'std_idst_clsf_cd', 'length': 6, 'name': '표준산업분류코드', 'required': True, 'type': 'string'}, {'description': '', 'key': 'std_idst_clsf_cd_name', 'length': 130, 'name': '표준산업분류코드명', 'required': True, 'type': 'string'}, {'description': '', 'key': 'idx_bztp_lcls_cd_name', 'length': 60, 'name': '지수업종대분류코드명', 'required': True, 'type': 'string'}, {'description': '', 'key': 'idx_bztp_mcls_cd_name', 'length': 60, 'name': '지수업종중분류코드명', 'required': True, 'type': 'string'}, {'description': "'표준산업소분류코드 참조'},", 'key': 'idx_bztp_scls_cd_name', 'length': 60, 'name': '지수업종소분류코드명', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'ocr_no', 'length': 4, 'name': 'OCR번호', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'crfd_item_yn', 'length': 1, 'name': '크라우드펀딩종목여부', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'elec_scty_yn', 'length': 1, 'name': '전자증권여부', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'issu_istt_cd', 'length': 5, 'name': '발행기관코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'etf_chas_erng_rt_dbnb', 'length': 19, 'name': 'ETF추적수익율배수', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'etf_etn_ivst_heed_item_yn', 'length': 1, 'name': 'ETFETN투자유의종목여부', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stln_int_rt_dvsn_cd', 'length': 2, 'name': '대주이자율구분코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'frnr_psnl_lmt_rt', 'length': 24, 'name': '외국인개인한도비율', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'lstg_rqsr_issu_istt_cd', 'length': 5, 'name': '상장신청인발행기관코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'lstg_rqsr_item_cd', 'length': 12, 'name': '상장신청인종목코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'trst_istt_issu_istt_cd', 'length': 5, 'name': '신탁기관발행기관코드', 'required': True, 'type': 'string'}, {'description': "'NXT 거래가능한 종목은 Y, 그 외 종목은 N'},", 'key': 'cptt_trad_tr_psbl_yn', 'length': 1, 'name': 'NXT 거래종목여부', 'required': True, 'type': 'string'}, {'description': "'NXT 거래종목 중 거래정지가 된 종목은 Y, 그 외 모든 종목은 N'}", 'key': 'nxt_tr_stop_yn', 'length': 1, 'name': 'NXT 거래정지여부', 'required': True, 'type': 'string'}]
        }
    },
    'CTPF1604R': {
        'output': {
            'fields': [{'description': "''},", 'key': 'pdno', 'length': 12, 'name': '상품번호', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_type_cd', 'length': 3, 'name': '상품유형코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_name', 'length': 60, 'name': '상품명', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_name120', 'length': 120, 'name': '상품명120', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_abrv_name', 'length': 60, 'name': '상품약어명', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_eng_name', 'length': 60, 'name': '상품영문명', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_eng_name120', 'length': 120, 'name': '상품영문명120', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_eng_abrv_name', 'length': 60, 'name': '상품영문약어명', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'std_pdno', 'length': 12, 'name': '표준상품번호', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'shtn_pdno', 'length': 12, 'name': '단축상품번호', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_sale_stat_cd', 'length': 2, 'name': '상품판매상태코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_risk_grad_cd', 'length': 2, 'name': '상품위험등급코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_clsf_cd', 'length': 6, 'name': '상품분류코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'prdt_clsf_name', 'length': 60, 'name': '상품분류명', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'sale_strt_dt', 'length': 8, 'name': '판매시작일자', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'sale_end_dt', 'length': 8, 'name': '판매종료일자', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'wrap_asst_type_cd', 'length': 2, 'name': '랩어카운트자산유형코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'ivst_prdt_type_cd', 'length': 4, 'name': '투자상품유형코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'ivst_prdt_type_cd_name', 'length': 60, 'name': '투자상품유형코드명', 'required': True, 'type': 'string'}, {'description': "''}", 'key': 'frst_erlm_dt', 'length': 8, 'name': '최초등록일자', 'required': True, 'type': 'string'}]
        }
    },
    'CTRGA011R': {
        'output': {
            'fields': []
        }
    },
    'CTRP6548R': {
        'output': {
            'fields': []
        }
    },
    'CTSC0004R': {
        'output': {
            'fields': [{'description': "''},", 'key': 'rsvn_ord_seq', 'length': 10, 'name': '예약주문 순번', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'rsvn_ord_ord_dt', 'length': 8, 'name': '예약주문주문일자', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'rsvn_ord_rcit_dt', 'length': 8, 'name': '예약주문접수일자', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'pdno', 'length': 12, 'name': '상품번호', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'ord_dvsn_cd', 'length': 2, 'name': '주문구분코드', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'ord_rsvn_qty', 'length': 10, 'name': '주문예약수량', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'tot_ccld_qty', 'length': 10, 'name': '총체결수량', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'cncl_ord_dt', 'length': 8, 'name': '취소주문일자', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'ord_tmd', 'length': 6, 'name': '주문시각', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'ctac_tlno', 'length': 20, 'name': '연락전화번호', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'rjct_rson2', 'length': 200, 'name': '거부사유2', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'odno', 'length': 10, 'name': '주문번호', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'rsvn_ord_rcit_tmd', 'length': 6, 'name': '예약주문접수시각', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'kor_item_shtn_name', 'length': 60, 'name': '한글종목단축명', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'sll_buy_dvsn_cd', 'length': 2, 'name': '매도매수구분코드', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'ord_rsvn_unpr', 'length': 19, 'name': '주문예약단가', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'tot_ccld_amt', 'length': 19, 'name': '총체결금액', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'loan_dt', 'length': 8, 'name': '대출일자', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'cncl_rcit_tmd', 'length': 6, 'name': '취소접수시각', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'prcs_rslt', 'length': 60, 'name': '처리결과', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'ord_dvsn_name', 'length': 60, 'name': '주문구분명', 'required': False, 'type': 'string'}, {'description': "''},", 'key': 'tmnl_mdia_kind_cd', 'length': 2, 'name': '단말매체종류코드', 'required': False, 'type': 'string'}, {'description': "''}", 'key': 'rsvn_end_dt', 'length': 8, 'name': '예약종료일자', 'required': False, 'type': 'string'}]
        }
    },
    'CTSC0008U': {
        'output': {
            'fields': [{'description': "''}", 'key': 'rsvn_ord_seq', 'length': 10, 'name': '예약주문 순번', 'required': False, 'type': 'string'}, {'description': "''}", 'key': 'nrml_prcs_yn', 'length': 1, 'name': '정상처리여부', 'required': True, 'type': 'string'}]
        }
    },
    'CTSC2702R': {
        'output': {
            'fields': []
        }
    },
    'TTTC0013U': {
        'output': {
            'fields': [{'description': "''},", 'key': 'krx_fwdg_ord_orgno', 'length': 5, 'name': '한국거래소전송주문조직번호', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'odno', 'length': 10, 'name': '주문번호', 'required': True, 'type': 'string'}, {'description': "''}", 'key': 'ord_tmd', 'length': 6, 'name': '주문시각', 'required': True, 'type': 'string'}]
        }
    },
    'TTTC0084R': {
        'output': {
            'fields': [{'description': "'주문시 한국투자증권 시스템에서 지정된 영업점코드'},", 'key': 'ord_gno_brno', 'length': 5, 'name': '주문채번지점번호', 'required': True, 'type': 'string'}, {'description': "'주문시 한국투자증권 시스템에서 채번된 주문번호'},", 'key': 'odno', 'length': 10, 'name': '주문번호', 'required': True, 'type': 'string'}, {'description': "'정정/취소주문 인경우 원주문번호'},", 'key': 'orgn_odno', 'length': 6, 'name': '원주문번호', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'ord_dvsn_name', 'length': 5, 'name': '주문구분명', 'required': True, 'type': 'string'}, {'description': "'종목번호(뒤 6자리만 해당)'},", 'key': 'pdno', 'length': 10, 'name': '상품번호', 'required': True, 'type': 'string'}, {'description': "'종목명'},", 'key': 'prdt_name', 'length': 6, 'name': '상품명', 'required': True, 'type': 'string'}, {'description': "'정정 또는 취소 여부 표시'},", 'key': 'rvse_cncl_dvsn_name', 'length': 5, 'name': '정정취소구분명', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'ord_qty', 'length': 10, 'name': '주문수량', 'required': True, 'type': 'string'}, {'description': "'1주당 주문가격'},", 'key': 'ord_unpr', 'length': 6, 'name': '주문단가', 'required': True, 'type': 'string'}, {'description': "'주문시각(시분초HHMMSS)'},", 'key': 'ord_tmd', 'length': 5, 'name': '주문시각', 'required': True, 'type': 'string'}, {'description': "'주문 수량 중 체결된 수량'},", 'key': 'tot_ccld_qty', 'length': 10, 'name': '총체결수량', 'required': True, 'type': 'string'}, {'description': "'주문금액 중 체결금액'},", 'key': 'tot_ccld_amt', 'length': 6, 'name': '총체결금액', 'required': True, 'type': 'string'}, {'description': "'정정/취소 주문 가능 수량'},", 'key': 'psbl_qty', 'length': 5, 'name': '가능수량', 'required': True, 'type': 'string'}, {'description': "'01 : 매도 / 02 : 매수'},", 'key': 'sll_buy_dvsn_cd', 'length': 10, 'name': '매도매수구분코드', 'required': True, 'type': 'string'}, {'description': '', 'key': 'ord_dvsn_cd', 'length': 6, 'name': '주문구분코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'mgco_aptm_odno', 'length': 5, 'name': '운용사지정주문번호', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'excg_dvsn_cd', 'length': 2, 'name': '거래소구분코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'excg_id_dvsn_cd', 'length': 3, 'name': '거래소ID구분코드', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'excg_id_dvsn_name', 'length': 100, 'name': '거래소ID구분명', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stpm_cndt_pric', 'length': 9, 'name': '스톱지정가조건가격', 'required': True, 'type': 'string'}, {'description': "''}", 'key': 'stpm_efct_occr_yn', 'length': 1, 'name': '스톱지정가효력발생여부', 'required': True, 'type': 'string'}]
        }
    },
    'TTTC0503R': {
        'output': {
            'fields': [{'description': "''},", 'key': 'ord_psbl_cash', 'length': 19, 'name': '주문가능현금', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'ruse_psbl_amt', 'length': 19, 'name': '재사용가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'psbl_qty_calc_unpr', 'length': 19, 'name': '가능수량계산단가', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'max_buy_amt', 'length': 19, 'name': '최대매수금액', 'required': True, 'type': 'string'}, {'description': "''}", 'key': 'max_buy_qty', 'length': 10, 'name': '최대매수수량', 'required': True, 'type': 'string'}]
        }
    },
    'TTTC0506R': {
        'output': {
            'fields': [{'description': "''},", 'key': 'dnca_tota', 'length': 19, 'name': '예수금총액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'nxdy_excc_amt', 'length': 19, 'name': '익일정산액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'nxdy_sttl_amt', 'length': 19, 'name': '익일결제금액', 'required': True, 'type': 'string'}, {'description': "''}", 'key': 'nx2_day_sttl_amt', 'length': 19, 'name': '2익일결제금액', 'required': True, 'type': 'string'}]
        }
    },
    'TTTC0869R': {
        'output': {
            'fields': [{'description': "''},", 'key': 'acmga_rt', 'length': 114, 'name': '계좌증거금율', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'acmga_pct100_aptm_rson', 'length': 100, 'name': '계좌증거금100퍼센트지정사유', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_cash_objt_amt', 'length': 184, 'name': '주식현금대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_sbst_objt_amt', 'length': 184, 'name': '주식대용대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_evlu_objt_amt', 'length': 184, 'name': '주식평가대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_ruse_psbl_objt_amt', 'length': 184, 'name': '주식재사용가능대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_fund_rpch_chgs_objt_amt', 'length': 184, 'name': '주식펀드환매대금대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_fncg_rdpt_objt_atm', 'length': 184, 'name': '주식융자상환금대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'bond_ruse_psbl_objt_amt', 'length': 184, 'name': '채권재사용가능대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_cash_use_amt', 'length': 184, 'name': '주식현금사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_sbst_use_amt', 'length': 184, 'name': '주식대용사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_evlu_use_amt', 'length': 184, 'name': '주식평가사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_ruse_psbl_amt_use_amt', 'length': 184, 'name': '주식재사용가능금사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_fund_rpch_chgs_use_amt', 'length': 184, 'name': '주식펀드환매대금사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_fncg_rdpt_amt_use_amt', 'length': 184, 'name': '주식융자상환금사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'bond_ruse_psbl_amt_use_amt', 'length': 184, 'name': '채권재사용가능금사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_cash_ord_psbl_amt', 'length': 184, 'name': '주식현금주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_sbst_ord_psbl_amt', 'length': 184, 'name': '주식대용주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_evlu_ord_psbl_amt', 'length': 184, 'name': '주식평가주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_ruse_psbl_ord_psbl_amt', 'length': 184, 'name': '주식재사용가능주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_fund_rpch_ord_psbl_amt', 'length': 184, 'name': '주식펀드환매주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'bond_ruse_psbl_ord_psbl_amt', 'length': 184, 'name': '채권재사용가능주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'rcvb_amt', 'length': 19, 'name': '미수금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_loan_grta_ruse_psbl_amt', 'length': 184, 'name': '주식대출보증금재사용가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_cash20_max_ord_psbl_amt', 'length': 184, 'name': '주식현금20최대주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_cash30_max_ord_psbl_amt', 'length': 184, 'name': '주식현금30최대주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_cash40_max_ord_psbl_amt', 'length': 184, 'name': '주식현금40최대주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_cash50_max_ord_psbl_amt', 'length': 184, 'name': '주식현금50최대주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_cash60_max_ord_psbl_amt', 'length': 184, 'name': '주식현금60최대주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_cash100_max_ord_psbl_amt', 'length': 184, 'name': '주식현금100최대주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_rsip100_max_ord_psbl_amt', 'length': 184, 'name': '주식재사용불가100최대주문가능', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'bond_max_ord_psbl_amt', 'length': 184, 'name': '채권최대주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_fncg45_max_ord_psbl_amt', 'length': 182, 'name': '주식융자45최대주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_fncg50_max_ord_psbl_amt', 'length': 184, 'name': '주식융자50최대주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_fncg60_max_ord_psbl_amt', 'length': 184, 'name': '주식융자60최대주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_fncg70_max_ord_psbl_amt', 'length': 182, 'name': '주식융자70최대주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_stln_max_ord_psbl_amt', 'length': 184, 'name': '주식대주최대주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'lmt_amt', 'length': 19, 'name': '한도금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'ovrs_stck_itgr_mgna_dvsn_name', 'length': 40, 'name': '해외주식통합증거금구분명', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'usd_objt_amt', 'length': 182, 'name': '미화대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'usd_use_amt', 'length': 182, 'name': '미화사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'usd_ord_psbl_amt', 'length': 182, 'name': '미화주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'hkd_objt_amt', 'length': 182, 'name': '홍콩달러대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'hkd_use_amt', 'length': 182, 'name': '홍콩달러사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'hkd_ord_psbl_amt', 'length': 182, 'name': '홍콩달러주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'jpy_objt_amt', 'length': 182, 'name': '엔화대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'jpy_use_amt', 'length': 182, 'name': '엔화사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'jpy_ord_psbl_amt', 'length': 182, 'name': '엔화주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'cny_objt_amt', 'length': 182, 'name': '위안화대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'cny_use_amt', 'length': 182, 'name': '위안화사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'cny_ord_psbl_amt', 'length': 182, 'name': '위안화주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'usd_ruse_objt_amt', 'length': 182, 'name': '미화재사용대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'usd_ruse_amt', 'length': 182, 'name': '미화재사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'usd_ruse_ord_psbl_amt', 'length': 182, 'name': '미화재사용주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'hkd_ruse_objt_amt', 'length': 182, 'name': '홍콩달러재사용대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'hkd_ruse_amt', 'length': 182, 'name': '홍콩달러재사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'hkd_ruse_ord_psbl_amt', 'length': 172, 'name': '홍콩달러재사용주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'jpy_ruse_objt_amt', 'length': 182, 'name': '엔화재사용대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'jpy_ruse_amt', 'length': 182, 'name': '엔화재사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'jpy_ruse_ord_psbl_amt', 'length': 182, 'name': '엔화재사용주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'cny_ruse_objt_amt', 'length': 182, 'name': '위안화재사용대상금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'cny_ruse_amt', 'length': 182, 'name': '위안화재사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'cny_ruse_ord_psbl_amt', 'length': 182, 'name': '위안화재사용주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'usd_gnrl_ord_psbl_amt', 'length': 182, 'name': '미화일반주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'usd_itgr_ord_psbl_amt', 'length': 182, 'name': '미화통합주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'hkd_gnrl_ord_psbl_amt', 'length': 182, 'name': '홍콩달러일반주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'hkd_itgr_ord_psbl_amt', 'length': 182, 'name': '홍콩달러통합주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'jpy_gnrl_ord_psbl_amt', 'length': 182, 'name': '엔화일반주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'jpy_itgr_ord_psbl_amt', 'length': 182, 'name': '엔화통합주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'cny_gnrl_ord_psbl_amt', 'length': 182, 'name': '위안화일반주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'cny_itgr_ord_psbl_amt', 'length': 182, 'name': '위안화통합주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_itgr_cash20_ord_psbl_amt', 'length': 182, 'name': '주식통합현금20주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_itgr_cash30_ord_psbl_amt', 'length': 182, 'name': '주식통합현금30주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_itgr_cash40_ord_psbl_amt', 'length': 182, 'name': '주식통합현금40주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_itgr_cash50_ord_psbl_amt', 'length': 182, 'name': '주식통합현금50주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_itgr_cash60_ord_psbl_amt', 'length': 182, 'name': '주식통합현금60주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_itgr_cash100_ord_psbl_amt', 'length': 182, 'name': '주식통합현금100주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_itgr_100_ord_psbl_amt', 'length': 182, 'name': '주식통합100주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_itgr_fncg45_ord_psbl_amt', 'length': 182, 'name': '주식통합융자45주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_itgr_fncg50_ord_psbl_amt', 'length': 182, 'name': '주식통합융자50주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_itgr_fncg60_ord_psbl_amt', 'length': 182, 'name': '주식통합융자60주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_itgr_fncg70_ord_psbl_amt', 'length': 182, 'name': '주식통합융자70주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_itgr_stln_ord_psbl_amt', 'length': 182, 'name': '주식통합대주주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'bond_itgr_ord_psbl_amt', 'length': 182, 'name': '채권통합주문가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_cash_ovrs_use_amt', 'length': 182, 'name': '주식현금해외사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_sbst_ovrs_use_amt', 'length': 182, 'name': '주식대용해외사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_evlu_ovrs_use_amt', 'length': 182, 'name': '주식평가해외사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_re_use_amt_ovrs_use_amt', 'length': 182, 'name': '주식재사용금액해외사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_fund_rpch_ovrs_use_amt', 'length': 182, 'name': '주식펀드환매해외사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'stck_fncg_rdpt_ovrs_use_amt', 'length': 182, 'name': '주식융자상환해외사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'bond_re_use_ovrs_use_amt', 'length': 182, 'name': '채권재사용해외사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'usd_oth_mket_use_amt', 'length': 182, 'name': '미화타시장사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'jpy_oth_mket_use_amt', 'length': 182, 'name': '엔화타시장사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'cny_oth_mket_use_amt', 'length': 182, 'name': '위안화타시장사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'hkd_oth_mket_use_amt', 'length': 182, 'name': '홍콩달러타시장사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'usd_re_use_oth_mket_use_amt', 'length': 182, 'name': '미화재사용타시장사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'jpy_re_use_oth_mket_use_amt', 'length': 182, 'name': '엔화재사용타시장사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'cny_re_use_oth_mket_use_amt', 'length': 182, 'name': '위안화재사용타시장사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'hkd_re_use_oth_mket_use_amt', 'length': 182, 'name': '홍콩달러재사용타시장사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'hgkg_cny_re_use_amt', 'length': 182, 'name': '홍콩위안화재사용금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'usd_frst_bltn_exrt', 'length': 23, 'name': '미국달러최초고시환율', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'hkd_frst_bltn_exrt', 'length': 23, 'name': '홍콩달러최초고시환율', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'jpy_frst_bltn_exrt', 'length': 23, 'name': '일본엔화최초고시환율', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'cny_frst_bltn_exrt', 'length': 23, 'name': '중국위안화최초고시환율', 'required': True, 'type': 'string'}]
        }
    },
    'TTTC2202R': {
        'output': {
            'fields': []
        }
    },
    'TTTC2208R': {
        'output': {
            'fields': []
        }
    },
    'TTTC8408R': {
        'output': {
            'fields': []
        }
    },
    "TTTC8434R": {
        "output": {
            "fields": [
                {
                    "key": "pdno",
                    "name": "종목코드",
                    "type": "string",
                    "length": 12,
                    "required": True,
                    "description": "상품번호"
                },
                {
                    "key": "prdt_name",
                    "name": "종목명",
                    "type": "string",
                    "length": 60,
                    "required": True,
                    "description": "상품명"
                },
                {
                    "key": "trad_dvsn_name",
                    "name": "거래구분명",
                    "type": "string",
                    "length": 20,
                    "required": True,
                    "description": "거래구분명"
                },
                {
                    "key": "hldg_qty",
                    "name": "보유수량",
                    "type": "number",
                    "length": 10,
                    "required": True,
                    "description": "보유수량"
                },
                {
                    "key": "pchs_avg_pric",
                    "name": "매입평균가격",
                    "type": "number",
                    "length": 19,
                    "required": True,
                    "description": "매입평균가격"
                },
                {
                    "key": "prpr",
                    "name": "현재가",
                    "type": "number",
                    "length": 19,
                    "required": True,
                    "description": "현재가"
                },
                {
                    "key": "evlu_amt",
                    "name": "평가금액",
                    "type": "number",
                    "length": 19,
                    "required": True,
                    "description": "평가금액"
                },
                {
                    "key": "evlu_pfls_amt",
                    "name": "평가손익금액",
                    "type": "number",
                    "length": 19,
                    "required": True,
                    "description": "평가손익금액"
                },
                {
                    "key": "evlu_pfls_rt",
                    "name": "평가손익율",
                    "type": "number",
                    "length": 10,
                    "required": True,
                    "description": "평가손익율(%)"
                },
                {
                    "key": "ord_psbl_qty",
                    "name": "주문가능수량",
                    "type": "number",
                    "length": 10,
                    "required": True,
                    "description": "주문가능수량"
                },
                {
                    "key": "loan_amt",
                    "name": "대출금액",
                    "type": "number",
                    "length": 19,
                    "required": True,
                    "description": "대출금액"
                },
                {
                    "key": "loan_dt",
                    "name": "대출일자",
                    "type": "string",
                    "length": 8,
                    "required": True,
                    "description": "대출일자(YYYYMMDD)"
                }
            ]
        },
        "output2": {
            "fields": [
                {
                    "key": "dnca_tota",
                    "name": "예수금총금액",
                    "type": "number",
                    "length": 19,
                    "required": True,
                    "description": "예수금총금액"
                },
                {
                    "key": "tot_evlu_amt",
                    "name": "총평가금액",
                    "type": "number",
                    "length": 19,
                    "required": True,
                    "description": "총평가금액"
                },
                {
                    "key": "tot_pfls_amt",
                    "name": "평가손익합계",
                    "type": "number",
                    "length": 19,
                    "required": True,
                    "description": "평가손익합계"
                },
                {
                    "key": "nass_amt",
                    "name": "순자산금액",
                    "type": "number",
                    "length": 19,
                    "required": True,
                    "description": "순자산금액"
                }
            ]
        }
    },
    'TTTC8494R': {
        'output': {
            'fields': []
        }
    },
    'TTTC8708R': {
        'output': {
            'fields': []
        }
    },
    'TTTC8715R': {
        'output': {
            'fields': []
        }
    },
    'TTTC8908R': {
        'output': {
            'fields': [{'description': "'예수금으로 계산된 주문가능금액'},", 'key': 'ord_psbl_cash', 'length': 19, 'name': '주문가능현금', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'ord_psbl_sbst', 'length': 19, 'name': '주문가능대용', 'required': True, 'type': 'string'}, {'description': "'전일/금일 매도대금으로 계산된 주문가능금액'},", 'key': 'ruse_psbl_amt', 'length': 19, 'name': '재사용가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'fund_rpch_chgs', 'length': 19, 'name': '펀드환매대금', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'psbl_qty_calc_unpr', 'length': 19, 'name': '가능수량계산단가', 'required': True, 'type': 'string'}, {'description': "'미수를 사용하지 않으실 경우 nrcvb_buy_amt(미수없는매수금액)을 확인'},", 'key': 'nrcvb_buy_amt', 'length': 19, 'name': '미수없는매수금액', 'required': True, 'type': 'string'}, {'description': '', 'key': 'nrcvb_buy_qty', 'length': 10, 'name': '미수없는매수수량', 'required': True, 'type': 'string'}, {'description': "'미수를 사용하시는 경우 max_buy_amt(최대매수금액)를 확인'},", 'key': 'max_buy_amt', 'length': 19, 'name': '최대매수금액', 'required': True, 'type': 'string'}, {'description': '', 'key': 'max_buy_qty', 'length': 10, 'name': '최대매수수량', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'cma_evlu_amt', 'length': 19, 'name': 'CMA평가금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'ovrs_re_use_amt_wcrc', 'length': 19, 'name': '해외재사용금액원화', 'required': True, 'type': 'string'}, {'description': "''}", 'key': 'ord_psbl_frcr_amt_wcrc', 'length': 19, 'name': '주문가능외화금액원화', 'required': True, 'type': 'string'}]
        }
    },
    'TTTC8909R': {
        'output': {
            'fields': [{'description': "''},", 'key': 'ord_psbl_cash', 'length': 19, 'name': '주문가능현금', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'ord_psbl_sbst', 'length': 19, 'name': '주문가능대용', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'ruse_psbl_amt', 'length': 19, 'name': '재사용가능금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'fund_rpch_chgs', 'length': 19, 'name': '펀드환매대금', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'psbl_qty_calc_unpr', 'length': 19, 'name': '가능수량계산단가', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'nrcvb_buy_amt', 'length': 19, 'name': '미수없는매수금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'nrcvb_buy_qty', 'length': 10, 'name': '미수없는매수수량', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'max_buy_amt', 'length': 19, 'name': '최대매수금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'max_buy_qty', 'length': 10, 'name': '최대매수수량', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'cma_evlu_amt', 'length': 19, 'name': 'CMA평가금액', 'required': True, 'type': 'string'}, {'description': "''},", 'key': 'ovrs_re_use_amt_wcrc', 'length': 19, 'name': '해외재사용금액원화', 'required': True, 'type': 'string'}, {'description': "''}", 'key': 'ord_psbl_frcr_amt_wcrc', 'length': 19, 'name': '주문가능외화금액원화', 'required': True, 'type': 'string'}]
        }
    }
}
