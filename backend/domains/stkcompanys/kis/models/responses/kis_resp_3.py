# KIS REST API Response Definitions
# Auto-generated from Excel file

KIS_RESPONSE_DEF_3 = {
    # === 종목조건검색 목록조회 ===
    'HHKST03900300': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'user_id', 'name': 'HTSID', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'seq', 'name': '조건키값', 'type': 'string', 'required': True, 'length': 10, 'description': '해당 값을 종목조건검색조회 API의 input으로 사용 (0번부터 시작)'},
                {'key': 'grp_nm', 'name': '그룹명', 'type': 'string', 'required': True, 'length': 40, 'description': 'HTS(eFriend Plus) [0110] "사용자조건검색"화면을 통해 등록한 사용자조건 그룹'},
                {'key': 'condition_nm', 'name': '조건명', 'type': 'string', 'required': True, 'length': 40, 'description': '등록한 사용자 조건명'}
            ]
        }
    },
    # === 종목조건검색조회 ===
    'HHKST03900400': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'code', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'name', 'name': '종목명', 'type': 'string', 'required': True, 'length': 20, 'description': ''},
                {'key': 'daebi', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': '1. 상한 2. 상승 3. 보합 4. 하한 5. 하락'},
                {'key': 'price', 'name': '현재가', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'chgrate', 'name': '등락율', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'acml_vol', 'name': '거래량', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'trade_amt', 'name': '거래대금', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'change', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'cttr', 'name': '체결강도', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'open', 'name': '시가', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'high', 'name': '고가', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'low', 'name': '저가', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'high52', 'name': '52주최고가', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'low52', 'name': '52주최저가', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'expprice', 'name': '예상체결가', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'expchange', 'name': '예상대비', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'expchggrate', 'name': '예상등락률', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'expcvol', 'name': '예상체결수량', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'chgrate2', 'name': '전일거래량대비율', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'expdaebi', 'name': '예상대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'recprice', 'name': '기준가', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'uplmtprice', 'name': '상한가', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'dnlmtprice', 'name': '하한가', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'stotprice', 'name': '시가총액', 'type': 'string', 'required': True, 'length': 16, 'description': ''}
            ]
        }
    },
    # === 관심종목 그룹조회 ===
    'HHKCM113004C7': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output2': {
            'type': 'object',
            'fields': [
                {'key': 'date', 'name': '일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'trnm_hour', 'name': '전송시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'inter_grp_code', 'name': '관심그룹코드', 'type': 'string', 'required': True, 'length': 3, 'description': ''},
                {'key': 'inter_grp_name', 'name': '관심그룹명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'ask_cnt', 'name': '요청개수', 'type': 'string', 'required': True, 'length': 4, 'description': ''}
            ]
        }
    },
    # === 관심종목(멀티종목) 시세조회 ===
    'FHKST11300006': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'kospi_kosdaq_cls_name', 'name': '코스피코스닥구분명', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'mrkt_trtm_cls_name', 'name': '시장조치구분명', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hour_cls_code', 'name': '시간구분코드', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'inter_shrn_iscd', 'name': '관심단축종목코드', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'inter_kor_isnm', 'name': '관심한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'inter2_prpr', 'name': '관심2현재가', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'inter2_prdy_vrss', 'name': '관심2전일대비', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'inter2_oprc', 'name': '관심2시가', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'inter2_hgpr', 'name': '관심2고가', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'inter2_lwpr', 'name': '관심2저가', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'inter2_llam', 'name': '관심2하한가', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'inter2_mxpr', 'name': '관심2상한가', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'inter2_askp', 'name': '관심2매도호가', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'inter2_bidp', 'name': '관심2매수호가', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'seln_rsqn', 'name': '매도잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'shnu_rsqn', 'name': '매수2잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'total_askp_rsqn', 'name': '총매도호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'total_bidp_rsqn', 'name': '총매수호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'inter2_prdy_clpr', 'name': '관심2전일종가', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'oprc_vrss_hgpr_rate', 'name': '시가대비최고가비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'intr_antc_cntg_vrss', 'name': '관심예상체결대비', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'intr_antc_cntg_vrss_sign', 'name': '관심예상체결대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'intr_antc_cntg_prdy_ctrt', 'name': '관심예상체결전일대비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'intr_antc_vol', 'name': '관심예상거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'inter2_sdpr', 'name': '관심2기준가', 'type': 'string', 'required': True, 'length': 11, 'description': ''}
            ]
        }
    },
    # === 관심종목 그룹별 종목조회 ===
    'HHKCM113004C6': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'inter_grp_name', 'name': '관심그룹명', 'type': 'string', 'required': True, 'length': 40, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'fid_mrkt_cls_code', 'name': 'FID시장구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'exch_code', 'name': '거래소코드', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
                {'key': 'jong_code', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'color_code', 'name': '생상코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'memo', 'name': '메모', 'type': 'string', 'required': True, 'length': 128, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'fxdt_ntby_qty', 'name': '기준일순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'cntg_unpr', 'name': '체결단가', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'cntg_cls_code', 'name': '체결구분코드', 'type': 'string', 'required': True, 'length': 1, 'description': ''}
            ]
        }
    },
    # === 국내기관_외국인 매매종목가집계 ===
    'FHPTJ04400000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'Output': {
            'type': 'object',
            'fields': [
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'ntby_qty', 'name': '순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_ntby_qty', 'name': '외국인순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'orgn_ntby_qty', 'name': '기관계순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ivtr_ntby_qty', 'name': '투자신탁순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'bank_ntby_qty', 'name': '은행순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'insu_ntby_qty', 'name': '보험순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'mrbn_ntby_qty', 'name': '종금순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'fund_ntby_qty', 'name': '기금순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'etc_orgt_ntby_vol', 'name': '기타단체순매수거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_ntby_vol', 'name': '기타법인순매수거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_ntby_tr_pbmn', 'name': '외국인순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': 'frgn_ntby_tr_pbmn ~ etc_corp_ntby_tr_pbmn (단위 : 백만원, 수량*현재가)'},
                {'key': 'orgn_ntby_tr_pbmn', 'name': '기관계순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ivtr_ntby_tr_pbmn', 'name': '투자신탁순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bank_ntby_tr_pbmn', 'name': '은행순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'insu_ntby_tr_pbmn', 'name': '보험순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'mrbn_ntby_tr_pbmn', 'name': '종금순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'fund_ntby_tr_pbmn', 'name': '기금순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_orgt_ntby_tr_pbmn', 'name': '기타단체순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_ntby_tr_pbmn', 'name': '기타법인순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 외국계 매매종목 가집계 ===
    'FHKST644100C0': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'stck_shrn_iscd', 'name': '주식단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'glob_ntsl_qty', 'name': '외국계순매도수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'glob_total_seln_qty', 'name': '외국계총매도수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'glob_total_shnu_qty', 'name': '외국계총매수2수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 종목별 투자자매매동향(일별) ===
    'FHPTJ04160001': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prdy_vol', 'name': '전일거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'rprs_mrkt_kor_name', 'name': '대표시장한글명', 'type': 'string', 'required': True, 'length': 40, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식영업일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stck_clpr', 'name': '주식종가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': '단위 : 주'},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': '단위 : 백만원'},
                {'key': 'stck_oprc', 'name': '주식시가2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_hgpr', 'name': '주식최고가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_lwpr', 'name': '주식최저가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'frgn_ntby_qty', 'name': '외국인순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': '단위 : 주'},
                {'key': 'frgn_reg_ntby_qty', 'name': '외국인등록순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_nreg_ntby_qty', 'name': '외국인비등록순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_ntby_qty', 'name': '개인순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'orgn_ntby_qty', 'name': '기관계순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'scrt_ntby_qty', 'name': '증권순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ivtr_ntby_qty', 'name': '투자신탁순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'pe_fund_ntby_vol', 'name': '사모펀드순매수거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bank_ntby_qty', 'name': '은행순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'insu_ntby_qty', 'name': '보험순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'mrbn_ntby_qty', 'name': '종금순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'fund_ntby_qty', 'name': '기금순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'etc_ntby_qty', 'name': '기타순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'etc_corp_ntby_vol', 'name': '기타법인순매수거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_orgt_ntby_vol', 'name': '기타단체순매수거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_reg_ntby_pbmn', 'name': '외국인등록순매수대금', 'type': 'string', 'required': True, 'length': 18, 'description': '단위 : 백만원'},
                {'key': 'frgn_ntby_tr_pbmn', 'name': '외국인순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_nreg_ntby_pbmn', 'name': '외국인비등록순매수대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_ntby_tr_pbmn', 'name': '개인순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_ntby_tr_pbmn', 'name': '기관계순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'scrt_ntby_tr_pbmn', 'name': '증권순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'pe_fund_ntby_tr_pbmn', 'name': '사모펀드순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ivtr_ntby_tr_pbmn', 'name': '투자신탁순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bank_ntby_tr_pbmn', 'name': '은행순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'insu_ntby_tr_pbmn', 'name': '보험순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'mrbn_ntby_tr_pbmn', 'name': '종금순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'fund_ntby_tr_pbmn', 'name': '기금순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_ntby_tr_pbmn', 'name': '기타순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_ntby_tr_pbmn', 'name': '기타법인순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_orgt_ntby_tr_pbmn', 'name': '기타단체순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_seln_vol', 'name': '외국인매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_shnu_vol', 'name': '외국인매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_seln_tr_pbmn', 'name': '외국인매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_shnu_tr_pbmn', 'name': '외국인매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_reg_askp_qty', 'name': '외국인등록매도수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_reg_bidp_qty', 'name': '외국인등록매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_reg_askp_pbmn', 'name': '외국인등록매도대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_reg_bidp_pbmn', 'name': '외국인등록매수대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_nreg_askp_qty', 'name': '외국인비등록매도수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_nreg_bidp_qty', 'name': '외국인비등록매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_nreg_askp_pbmn', 'name': '외국인비등록매도대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_nreg_bidp_pbmn', 'name': '외국인비등록매수대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_seln_vol', 'name': '개인매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_shnu_vol', 'name': '개인매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_seln_tr_pbmn', 'name': '개인매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_shnu_tr_pbmn', 'name': '개인매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_seln_vol', 'name': '기관계매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_shnu_vol', 'name': '기관계매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_seln_tr_pbmn', 'name': '기관계매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_shnu_tr_pbmn', 'name': '기관계매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'scrt_seln_vol', 'name': '증권매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'scrt_shnu_vol', 'name': '증권매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'scrt_seln_tr_pbmn', 'name': '증권매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'scrt_shnu_tr_pbmn', 'name': '증권매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ivtr_seln_vol', 'name': '투자신탁매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ivtr_shnu_vol', 'name': '투자신탁매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ivtr_seln_tr_pbmn', 'name': '투자신탁매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ivtr_shnu_tr_pbmn', 'name': '투자신탁매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'pe_fund_seln_tr_pbmn', 'name': '사모펀드매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'pe_fund_seln_vol', 'name': '사모펀드매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'pe_fund_shnu_tr_pbmn', 'name': '사모펀드매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'pe_fund_shnu_vol', 'name': '사모펀드매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bank_seln_vol', 'name': '은행매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bank_shnu_vol', 'name': '은행매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bank_seln_tr_pbmn', 'name': '은행매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bank_shnu_tr_pbmn', 'name': '은행매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'insu_seln_vol', 'name': '보험매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'insu_shnu_vol', 'name': '보험매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'insu_seln_tr_pbmn', 'name': '보험매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'insu_shnu_tr_pbmn', 'name': '보험매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'mrbn_seln_vol', 'name': '종금매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'mrbn_shnu_vol', 'name': '종금매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'mrbn_seln_tr_pbmn', 'name': '종금매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'mrbn_shnu_tr_pbmn', 'name': '종금매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'fund_seln_vol', 'name': '기금매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'fund_shnu_vol', 'name': '기금매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'fund_seln_tr_pbmn', 'name': '기금매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'fund_shnu_tr_pbmn', 'name': '기금매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_seln_vol', 'name': '기타매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_shnu_vol', 'name': '기타매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_seln_tr_pbmn', 'name': '기타매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_shnu_tr_pbmn', 'name': '기타매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_orgt_seln_vol', 'name': '기타단체매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_orgt_shnu_vol', 'name': '기타단체매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_orgt_seln_tr_pbmn', 'name': '기타단체매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_orgt_shnu_tr_pbmn', 'name': '기타단체매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_seln_vol', 'name': '기타법인매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_shnu_vol', 'name': '기타법인매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_seln_tr_pbmn', 'name': '기타법인매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_shnu_tr_pbmn', 'name': '기타법인매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bold_yn', 'name': 'BOLD여부', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 시장별 투자자매매동향(시세) ===
    'FHPTJ04030000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'frgn_seln_vol', 'name': '외국인매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_shnu_vol', 'name': '외국인매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_ntby_qty', 'name': '외국인순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'frgn_seln_tr_pbmn', 'name': '외국인매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_shnu_tr_pbmn', 'name': '외국인매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_ntby_tr_pbmn', 'name': '외국인순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_seln_vol', 'name': '개인매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_shnu_vol', 'name': '개인매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_ntby_qty', 'name': '개인순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'prsn_seln_tr_pbmn', 'name': '개인매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_shnu_tr_pbmn', 'name': '개인매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_ntby_tr_pbmn', 'name': '개인순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_seln_vol', 'name': '기관계매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_shnu_vol', 'name': '기관계매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_ntby_qty', 'name': '기관계순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_seln_tr_pbmn', 'name': '기관계매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_shnu_tr_pbmn', 'name': '기관계매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_ntby_tr_pbmn', 'name': '기관계순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'scrt_seln_vol', 'name': '증권매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'scrt_shnu_vol', 'name': '증권매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'scrt_ntby_qty', 'name': '증권순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'scrt_seln_tr_pbmn', 'name': '증권매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'scrt_shnu_tr_pbmn', 'name': '증권매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'scrt_ntby_tr_pbmn', 'name': '증권순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ivtr_seln_vol', 'name': '투자신탁매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ivtr_shnu_vol', 'name': '투자신탁매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ivtr_ntby_qty', 'name': '투자신탁순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ivtr_seln_tr_pbmn', 'name': '투자신탁매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ivtr_shnu_tr_pbmn', 'name': '투자신탁매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ivtr_ntby_tr_pbmn', 'name': '투자신탁순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'pe_fund_seln_tr_pbmn', 'name': '사모펀드매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'pe_fund_seln_vol', 'name': '사모펀드매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'pe_fund_ntby_vol', 'name': '사모펀드순매수거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'pe_fund_shnu_tr_pbmn', 'name': '사모펀드매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'pe_fund_shnu_vol', 'name': '사모펀드매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'pe_fund_ntby_tr_pbmn', 'name': '사모펀드순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bank_seln_vol', 'name': '은행매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bank_shnu_vol', 'name': '은행매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bank_ntby_qty', 'name': '은행순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'bank_seln_tr_pbmn', 'name': '은행매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bank_shnu_tr_pbmn', 'name': '은행매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bank_ntby_tr_pbmn', 'name': '은행순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'insu_seln_vol', 'name': '보험매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'insu_shnu_vol', 'name': '보험매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'insu_ntby_qty', 'name': '보험순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'insu_seln_tr_pbmn', 'name': '보험매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'insu_shnu_tr_pbmn', 'name': '보험매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'insu_ntby_tr_pbmn', 'name': '보험순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'mrbn_seln_vol', 'name': '종금매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'mrbn_shnu_vol', 'name': '종금매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'mrbn_ntby_qty', 'name': '종금순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'mrbn_seln_tr_pbmn', 'name': '종금매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'mrbn_shnu_tr_pbmn', 'name': '종금매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'mrbn_ntby_tr_pbmn', 'name': '종금순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'fund_seln_vol', 'name': '기금매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'fund_shnu_vol', 'name': '기금매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'fund_ntby_qty', 'name': '기금순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'fund_seln_tr_pbmn', 'name': '기금매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'fund_shnu_tr_pbmn', 'name': '기금매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'fund_ntby_tr_pbmn', 'name': '기금순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_orgt_seln_vol', 'name': '기타단체매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_orgt_shnu_vol', 'name': '기타단체매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_orgt_ntby_vol', 'name': '기타단체순매수거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_orgt_seln_tr_pbmn', 'name': '기타단체매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_orgt_shnu_tr_pbmn', 'name': '기타단체매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_orgt_ntby_tr_pbmn', 'name': '기타단체순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_seln_vol', 'name': '기타법인매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_shnu_vol', 'name': '기타법인매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_ntby_vol', 'name': '기타법인순매수거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_seln_tr_pbmn', 'name': '기타법인매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_shnu_tr_pbmn', 'name': '기타법인매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_ntby_tr_pbmn', 'name': '기타법인순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 시장별 투자자매매동향(일별) ===
    'FHPTJ04040000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식영업일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'bstp_nmix_prpr', 'name': '업종지수현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_prdy_vrss', 'name': '업종지수전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'bstp_nmix_prdy_ctrt', 'name': '업종지수전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'bstp_nmix_oprc', 'name': '업종지수시가2', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_hgpr', 'name': '업종지수최고가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_lwpr', 'name': '업종지수최저가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'stck_prdy_clpr', 'name': '주식전일종가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'frgn_ntby_qty', 'name': '외국인순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'frgn_reg_ntby_qty', 'name': '외국인등록순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_nreg_ntby_qty', 'name': '외국인비등록순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_ntby_qty', 'name': '개인순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'orgn_ntby_qty', 'name': '기관계순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'scrt_ntby_qty', 'name': '증권순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ivtr_ntby_qty', 'name': '투자신탁순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'pe_fund_ntby_vol', 'name': '사모펀드순매수거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bank_ntby_qty', 'name': '은행순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'insu_ntby_qty', 'name': '보험순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'mrbn_ntby_qty', 'name': '종금순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'fund_ntby_qty', 'name': '기금순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'etc_ntby_qty', 'name': '기타순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'etc_orgt_ntby_vol', 'name': '기타단체순매수거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_ntby_vol', 'name': '기타법인순매수거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_ntby_tr_pbmn', 'name': '외국인순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_reg_ntby_pbmn', 'name': '외국인등록순매수대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_nreg_ntby_pbmn', 'name': '외국인비등록순매수대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_ntby_tr_pbmn', 'name': '개인순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_ntby_tr_pbmn', 'name': '기관계순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'scrt_ntby_tr_pbmn', 'name': '증권순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ivtr_ntby_tr_pbmn', 'name': '투자신탁순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'pe_fund_ntby_tr_pbmn', 'name': '사모펀드순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bank_ntby_tr_pbmn', 'name': '은행순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'insu_ntby_tr_pbmn', 'name': '보험순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'mrbn_ntby_tr_pbmn', 'name': '종금순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'fund_ntby_tr_pbmn', 'name': '기금순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_ntby_tr_pbmn', 'name': '기타순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_orgt_ntby_tr_pbmn', 'name': '기타단체순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etc_corp_ntby_tr_pbmn', 'name': '기타법인순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 종목별 외국계 순매수추이 ===
    'FHKST644400C0': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'bsop_hour', 'name': '영업시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_seln_vol', 'name': '외국인매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_shnu_vol', 'name': '외국인매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'glob_ntby_qty', 'name': '외국계순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'frgn_ntby_qty_icdc', 'name': '외국인순매수수량증감', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 회원사 실시간 매매동향(틱) ===
    'FHPST04320000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'total_seln_qty', 'name': '총매도수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'total_shnu_qty', 'name': '총매수2수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'bsop_hour', 'name': '영업시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'mbcr_name', 'name': '회원사명', 'type': 'string', 'required': True, 'length': 50, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'cntg_vol', 'name': '체결거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_ntby_qty', 'name': '누적순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'glob_ntby_qty', 'name': '외국계순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'frgn_ntby_qty_icdc', 'name': '외국인순매수수량증감', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 주식현재가 회원사 종목매매동향 ===
    'FHPST04540000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식영업일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'total_seln_qty', 'name': '총매도수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'total_shnu_qty', 'name': '총매수2수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ntby_qty', 'name': '순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 종목별 프로그램매매추이(체결) ===
    'FHPPG04650101': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'bsop_hour', 'name': '영업시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_seln_vol', 'name': '전체합계매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_shnu_vol', 'name': '전체합계매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_ntby_qty', 'name': '전체합계순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_seln_tr_pbmn', 'name': '전체합계매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_shnu_tr_pbmn', 'name': '전체합계매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_ntby_tr_pbmn', 'name': '전체합계순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_ntby_vol_icdc', 'name': '전체순매수거래량증감', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'whol_ntby_tr_pbmn_icdc', 'name': '전체순매수거래대금증감', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 종목별 프로그램매매추이(일별) ===
    'FHPPG04650201': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식영업일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stck_clpr', 'name': '주식종가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_seln_vol', 'name': '전체합계매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_shnu_vol', 'name': '전체합계매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_ntby_qty', 'name': '전체합계순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_seln_tr_pbmn', 'name': '전체합계매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_shnu_tr_pbmn', 'name': '전체합계매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_ntby_tr_pbmn', 'name': '전체합계순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_ntby_vol_icdc', 'name': '전체순매수거래량증감', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'whol_ntby_tr_pbmn_icdc2', 'name': '전체순매수거래대금증감2', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 종목별 외인기관 추정가집계 ===
    'HHPTJ04160200': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'bsop_hour_gb', 'name': '입력구분', 'type': 'string', 'required': True, 'length': 1, 'description': '1: 09시 30분 입력 2: 10시 00분 입력  3: 11시 20분 입력  4: 13시 20분 입력  5: 14시 30분 입력'},
                {'key': 'frgn_fake_ntby_qty', 'name': '외국인수량(가집계)', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_fake_ntby_qty', 'name': '기관수량(가집계)', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'sum_fake_ntby_qty', 'name': '합산수량(가집계)', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 종목별일별매수매도체결량 ===
    'FHKST03010800': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'shnu_cnqn_smtn', 'name': '매수체결량합계', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'seln_cnqn_smtn', 'name': '매도체결량합계', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '거래상태정보', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'total_seln_qty', 'name': '총매도수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'total_shnu_qty', 'name': '총매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 프로그램매매 종합현황(시간) ===
    'FHPPG04600101': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'bsop_hour', 'name': '영업시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'arbt_smtn_seln_tr_pbmn', 'name': '차익합계매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_smtm_seln_tr_pbmn_rate', 'name': '차익합계매도거래대금비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'arbt_smtn_shnu_tr_pbmn', 'name': '차익합계매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_smtm_shun_tr_pbmn_rate', 'name': '차익합계매수거래대금비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'nabt_smtn_seln_tr_pbmn', 'name': '비차익합계매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_smtm_seln_tr_pbmn_rate', 'name': '비차익합계매도거래대금비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'nabt_smtn_shnu_tr_pbmn', 'name': '비차익합계매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_smtm_shun_tr_pbmn_rate', 'name': '비차익합계매수거래대금비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'arbt_smtn_ntby_tr_pbmn', 'name': '차익합계순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_smtm_ntby_tr_pbmn_rate', 'name': '차익합계순매수거래대금비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'nabt_smtn_ntby_tr_pbmn', 'name': '비차익합계순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_smtm_ntby_tr_pbmn_rate', 'name': '비차익합계순매수거래대금비', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'whol_smtn_ntby_tr_pbmn', 'name': '전체합계순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_ntby_tr_pbmn_rate', 'name': '전체순매수거래대금비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'bstp_nmix_prpr', 'name': '업종지수현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_prdy_vrss', 'name': '업종지수전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''}
            ]
        }
    },
    # === 프로그램매매 종합현황(일별) ===
    'FHPPG04600001': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식영업일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'nabt_entm_seln_tr_pbmn', 'name': '비차익위탁매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_onsl_seln_vol', 'name': '비차익자기매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_onsl_seln_tr_pbmn', 'name': '전체자기매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_smtn_shnu_vol', 'name': '차익합계매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_smtn_shnu_tr_pbmn', 'name': '비차익합계매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_entm_ntby_qty', 'name': '차익위탁순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_entm_ntby_tr_pbmn', 'name': '비차익위탁순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_entm_seln_vol', 'name': '차익위탁매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_entm_seln_vol_rate', 'name': '비차익위탁매도거래량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nabt_onsl_seln_vol_rate', 'name': '비차익자기매도거래량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'whol_onsl_seln_tr_pbmn_rate', 'name': '전체자기매도거래대금비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'arbt_smtm_shun_vol_rate', 'name': '차익합계매수거래량비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'nabt_smtm_shun_tr_pbmn_rate', 'name': '비차익합계매수거래대금비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'arbt_entm_ntby_qty_rate', 'name': '차익위탁순매수수량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nabt_entm_ntby_tr_pbmn_rate', 'name': '비차익위탁순매수거래대금', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'arbt_entm_seln_vol_rate', 'name': '차익위탁매도거래량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nabt_entm_seln_tr_pbmn_rate', 'name': '비차익위탁매도거래대금비', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nabt_onsl_seln_tr_pbmn', 'name': '비차익자기매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_seln_vol', 'name': '전체합계매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_smtn_shnu_tr_pbmn', 'name': '차익합계매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_entm_shnu_vol', 'name': '전체위탁매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_entm_ntby_tr_pbmn', 'name': '차익위탁순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_onsl_ntby_qty', 'name': '비차익자기순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_entm_seln_tr_pbmn', 'name': '차익위탁매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_onsl_seln_tr_pbmn_rate', 'name': '비차익자기매도거래대금비', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'whol_seln_vol_rate', 'name': '전체매도거래량비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'arbt_smtm_shun_tr_pbmn_rate', 'name': '차익합계매수거래대금비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'whol_entm_shnu_vol_rate', 'name': '전체위탁매수거래량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'arbt_entm_ntby_tr_pbmn_rate', 'name': '차익위탁순매수거래대금비', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nabt_onsl_ntby_qty_rate', 'name': '비차익자기순매수수량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'arbt_entm_seln_tr_pbmn_rate', 'name': '차익위탁매도거래대금비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nabt_smtn_seln_vol', 'name': '비차익합계매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_seln_tr_pbmn', 'name': '전체합계매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_entm_shnu_vol', 'name': '비차익위탁매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_entm_shnu_tr_pbmn', 'name': '전체위탁매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_onsl_ntby_qty', 'name': '차익자기순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_onsl_ntby_tr_pbmn', 'name': '비차익자기순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_onsl_seln_tr_pbmn', 'name': '차익자기매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_smtm_seln_vol_rate', 'name': '비차익합계매도거래량비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'whol_seln_tr_pbmn_rate', 'name': '전체매도거래대금비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'nabt_entm_shnu_vol_rate', 'name': '비차익위탁매수거래량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'whol_entm_shnu_tr_pbmn_rate', 'name': '전체위탁매수거래대금비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'arbt_onsl_ntby_qty_rate', 'name': '차익자기순매수수량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nabt_onsl_ntby_tr_pbmn_rate', 'name': '비차익자기순매수거래대금', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'arbt_onsl_seln_tr_pbmn_rate', 'name': '차익자기매도거래대금비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nabt_smtn_seln_tr_pbmn', 'name': '비차익합계매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_entm_shnu_vol', 'name': '차익위탁매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_entm_shnu_tr_pbmn', 'name': '비차익위탁매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_onsl_shnu_vol', 'name': '전체자기매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_onsl_ntby_tr_pbmn', 'name': '차익자기순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_smtn_ntby_qty', 'name': '비차익합계순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_onsl_seln_vol', 'name': '차익자기매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_smtm_seln_tr_pbmn_rate', 'name': '비차익합계매도거래대금비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'arbt_entm_shnu_vol_rate', 'name': '차익위탁매수거래량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nabt_entm_shnu_tr_pbmn_rate', 'name': '비차익위탁매수거래대금비', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'whol_onsl_shnu_tr_pbmn', 'name': '전체자기매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_onsl_ntby_tr_pbmn_rate', 'name': '차익자기순매수거래대금비', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nabt_smtm_ntby_qty_rate', 'name': '비차익합계순매수수량비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'arbt_onsl_seln_vol_rate', 'name': '차익자기매도거래량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'whol_entm_seln_vol', 'name': '전체위탁매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_entm_shnu_tr_pbmn', 'name': '차익위탁매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_onsl_shnu_vol', 'name': '비차익자기매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_onsl_shnu_tr_pbmn_rate', 'name': '전체자기매수거래대금비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'arbt_smtn_ntby_qty', 'name': '차익합계순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_smtn_ntby_tr_pbmn', 'name': '비차익합계순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_smtn_seln_vol', 'name': '차익합계매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_entm_seln_tr_pbmn', 'name': '전체위탁매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_entm_shnu_tr_pbmn_rate', 'name': '차익위탁매수거래대금비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nabt_onsl_shnu_vol_rate', 'name': '비차익자기매수거래량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'whol_onsl_shnu_vol_rate', 'name': '전체자기매수거래량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'arbt_smtm_ntby_qty_rate', 'name': '차익합계순매수수량비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'nabt_smtm_ntby_tr_pbmn_rate', 'name': '비차익합계순매수거래대금비', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'arbt_smtm_seln_vol_rate', 'name': '차익합계매도거래량비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'whol_entm_seln_vol_rate', 'name': '전체위탁매도거래량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'arbt_onsl_shnu_vol', 'name': '차익자기매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_onsl_shnu_tr_pbmn', 'name': '비차익자기매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_shnu_vol', 'name': '전체합계매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_smtn_ntby_tr_pbmn', 'name': '차익합계순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_entm_ntby_qty', 'name': '전체위탁순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_smtn_seln_tr_pbmn', 'name': '차익합계매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_entm_seln_tr_pbmn_rate', 'name': '전체위탁매도거래대금비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'arbt_onsl_shnu_vol_rate', 'name': '차익자기매수거래량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nabt_onsl_shnu_tr_pbmn_rate', 'name': '비차익자기매수거래대금비', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'whol_shun_vol_rate', 'name': '전체매수거래량비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'arbt_smtm_ntby_tr_pbmn_rate', 'name': '차익합계순매수거래대금비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'whol_entm_ntby_qty_rate', 'name': '전체위탁순매수수량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'arbt_smtm_seln_tr_pbmn_rate', 'name': '차익합계매도거래대금비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'whol_onsl_seln_vol', 'name': '전체자기매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_onsl_shnu_tr_pbmn', 'name': '차익자기매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_smtn_shnu_vol', 'name': '비차익합계매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_smtn_shnu_tr_pbmn', 'name': '전체합계매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_entm_ntby_qty', 'name': '비차익위탁순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_entm_ntby_tr_pbmn', 'name': '전체위탁순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_entm_seln_vol', 'name': '비차익위탁매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_onsl_seln_vol_rate', 'name': '전체자기매도거래량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'arbt_onsl_shnu_tr_pbmn_rate', 'name': '차익자기매수거래대금비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nabt_smtm_shun_vol_rate', 'name': '비차익합계매수거래량비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'whol_shun_tr_pbmn_rate', 'name': '전체매수거래대금비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'nabt_entm_ntby_qty_rate', 'name': '비차익위탁순매수수량비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''}
            ]
        }
    },
    # === 프로그램매매 투자자매매동향(당일) ===
    'HHPPG046600C1': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'invr_cls_code', 'name': '투자자코드', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
                {'key': 'all_seln_qty', 'name': '전체매도수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'all_seln_amt', 'name': '전체매도대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'invr_cls_name', 'name': '투자자구분명', 'type': 'string', 'required': True, 'length': 20, 'description': ''},
                {'key': 'all_shnu_qty', 'name': '전체매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'all_shnu_amt', 'name': '전체매수대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'all_ntby_amt', 'name': '전체순매수대금', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'arbt_seln_qty', 'name': '차익매도수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'all_ntby_qty', 'name': '전체순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'arbt_shnu_qty', 'name': '차익매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_ntby_qty', 'name': '차익순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'arbt_seln_amt', 'name': '차익매도대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_shnu_amt', 'name': '차익매수대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'arbt_ntby_amt', 'name': '차익순매수대금', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'nabt_seln_qty', 'name': '비차익매도수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_shnu_qty', 'name': '비차익매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_ntby_qty', 'name': '비차익순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'nabt_seln_amt', 'name': '비차익매도대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_shnu_amt', 'name': '비차익매수대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nabt_ntby_amt', 'name': '비차익순매수대금', 'type': 'string', 'required': True, 'length': 12, 'description': ''}
            ]
        }
    },
    # === 국내주식 신용잔고 일별추이 ===
    'FHPST04760000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'deal_date', 'name': '매매일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'stlm_date', 'name': '결제일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'whol_loan_new_stcn', 'name': '전체융자신규주수', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 주'},
                {'key': 'whol_loan_rdmp_stcn', 'name': '전체융자상환주수', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 주'},
                {'key': 'whol_loan_rmnd_stcn', 'name': '전체융자잔고주수', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 주'},
                {'key': 'whol_loan_new_amt', 'name': '전체융자신규금액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 만원'},
                {'key': 'whol_loan_rdmp_amt', 'name': '전체융자상환금액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 만원'},
                {'key': 'whol_loan_rmnd_amt', 'name': '전체융자잔고금액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 만원'},
                {'key': 'whol_loan_rmnd_rate', 'name': '전체융자잔고비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'whol_loan_gvrt', 'name': '전체융자공여율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'whol_stln_new_stcn', 'name': '전체대주신규주수', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 주'},
                {'key': 'whol_stln_rdmp_stcn', 'name': '전체대주상환주수', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 주'},
                {'key': 'whol_stln_rmnd_stcn', 'name': '전체대주잔고주수', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 주'},
                {'key': 'whol_stln_new_amt', 'name': '전체대주신규금액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 만원'},
                {'key': 'whol_stln_rdmp_amt', 'name': '전체대주상환금액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 만원'},
                {'key': 'whol_stln_rmnd_amt', 'name': '전체대주잔고금액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 만원'},
                {'key': 'whol_stln_rmnd_rate', 'name': '전체대주잔고비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'whol_stln_gvrt', 'name': '전체대주공여율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'stck_oprc', 'name': '주식시가2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_hgpr', 'name': '주식최고가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_lwpr', 'name': '주식최저가', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 국내주식 예상체결가 추이 ===
    'FHPST01810000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'rprs_mrkt_kor_name', 'name': '대표시장한글명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'antc_cnpr', 'name': '예상체결가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'antc_cntg_vrss_sign', 'name': '예상체결대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'antc_cntg_vrss', 'name': '예상체결대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'antc_cntg_prdy_ctrt', 'name': '예상체결전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'antc_vol', 'name': '예상거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'antc_tr_pbmn', 'name': '예상거래대금', 'type': 'string', 'required': True, 'length': 19, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식영업일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stck_cntg_hour', 'name': '주식체결시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 국내주식 공매도 일별추이 ===
    'FHPST04830000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prdy_vol', 'name': '전일거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식영업일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stck_clpr', 'name': '주식종가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'stnd_vol_smtn', 'name': '기준거래량합계', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ssts_cntg_qty', 'name': '공매도체결수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ssts_vol_rlim', 'name': '공매도거래량비중', 'type': 'string', 'required': True, 'length': 62, 'description': ''},
                {'key': 'acml_ssts_cntg_qty', 'name': '누적공매도체결수량', 'type': 'string', 'required': True, 'length': 13, 'description': ''},
                {'key': 'acml_ssts_cntg_qty_rlim', 'name': '누적공매도체결수량비중', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'stnd_tr_pbmn_smtn', 'name': '기준거래대금합계', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ssts_tr_pbmn', 'name': '공매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ssts_tr_pbmn_rlim', 'name': '공매도거래대금비중', 'type': 'string', 'required': True, 'length': 62, 'description': ''},
                {'key': 'acml_ssts_tr_pbmn', 'name': '누적공매도거래대금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'acml_ssts_tr_pbmn_rlim', 'name': '누적공매도거래대금비중', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'stck_oprc', 'name': '주식시가2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_hgpr', 'name': '주식최고가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_lwpr', 'name': '주식최저가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'avrg_prc', 'name': '평균가격', 'type': 'string', 'required': True, 'length': 11, 'description': ''}
            ]
        }
    },
    # === 국내주식 시간외예상체결등락률 ===
    'FHKST11860000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'iscd_stat_cls_code', 'name': '종목상태구분코드', 'type': 'string', 'required': True, 'length': 3, 'description': ''},
                {'key': 'stck_shrn_iscd', 'name': '주식단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'ovtm_untp_antc_cnpr', 'name': '시간외단일가예상체결가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_antc_cntg_vrss', 'name': '시간외단일가예상체결대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_antc_cntg_vrsssign', 'name': '시간외단일가예상체결대비', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'ovtm_untp_antc_cntg_ctrt', 'name': '시간외단일가예상체결대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'ovtm_untp_askp_rsqn1', 'name': '시간외단일가매도호가잔량1', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_bidp_rsqn1', 'name': '시간외단일가매수호가잔량1', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_antc_cnqn', 'name': '시간외단일가예상체결량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'itmt_vol', 'name': '장중거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 국내주식 체결금액별 매매비중 ===
    'FHKST111900C0': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'prpr_name', 'name': '가격명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'smtn_avrg_prpr', 'name': '합계평균가격', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'acml_vol', 'name': '합계거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_ntby_qty_rate', 'name': '합계순매수비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'ntby_cntg_csnu', 'name': '합계순매수건수', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'seln_cnqn_smtn', 'name': '매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_seln_vol_rate', 'name': '매도거래량비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'seln_cntg_csnu', 'name': '매도건수', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'shnu_cnqn_smtn', 'name': '매수거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_shun_vol_rate', 'name': '매수거래량비율', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'shnu_cntg_csnu', 'name': '매수건수', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 국내 증시자금 종합 ===
    'FHKST649100C0': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'bsop_date', 'name': '영업일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'bstp_nmix_prpr', 'name': '업종지수현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_prdy_vrss', 'name': '업종지수전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': '1. 상한 2. 상승 3. 보합 4. 하한 5. 하락'},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'hts_avls', 'name': 'HTS시가총액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 백만원'},
                {'key': 'cust_dpmn_amt', 'name': '고객예탁금금액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 억원'},
                {'key': 'cust_dpmn_amt_prdy_vrss', 'name': '고객예탁금금액전일대비', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'amt_tnrt', 'name': '금액회전율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'uncl_amt', 'name': '미수금액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 억원'},
                {'key': 'crdt_loan_rmnd', 'name': '신용융자잔고', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 억원'},
                {'key': 'futs_tfam_amt', 'name': '선물예수금금액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 억원'},
                {'key': 'sttp_amt', 'name': '주식형금액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 억원'},
                {'key': 'mxtp_amt', 'name': '혼합형금액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 억원'},
                {'key': 'bntp_amt', 'name': '채권형금액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 억원'},
                {'key': 'mmf_amt', 'name': 'MMF금액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 억원'},
                {'key': 'secu_lend_amt', 'name': '담보대출잔고금액', 'type': 'string', 'required': True, 'length': 18, 'description': '단위: 억원'}
            ]
        }
    },
    # === 종목별 일별 대차거래추이 ===
    'HHPST074500C0': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'bsop_date', 'name': '일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식종가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'new_stcn', 'name': '당일증가주수(체결)', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'rdmp_stcn', 'name': '당일감소주수(상환)', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'prdy_rmnd_vrss', 'name': '대차거래증감', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'rmnd_stcn', 'name': '당일잔고주수', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'rmnd_amt', 'name': '당일잔고금액', 'type': 'string', 'required': True, 'length': 20, 'description': ''}
            ]
        }
    },
    # === 국내주식 상하한가 포착 ===
    'FHKST130000C0': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'total_askp_rsqn', 'name': '총매도호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'total_bidp_rsqn', 'name': '총매수호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'askp_rsqn1', 'name': '매도호가잔량1', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'bidp_rsqn1', 'name': '매수호가잔량1', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'prdy_vol', 'name': '전일거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'seln_cnqn', 'name': '매도체결량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'shnu_cnqn', 'name': '매수2체결량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'stck_llam', 'name': '주식하한가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_mxpr', 'name': '주식상한가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_vol_rate', 'name': '전일대비거래량비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''}
            ]
        }
    }
}
