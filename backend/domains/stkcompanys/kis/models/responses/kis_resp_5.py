# KIS REST API Response Definitions
# Auto-generated from Excel file

KIS_RESPONSE_DEF_5 = {
    # === 국내업종 현재지수 ===
    'FHPUP02100000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'bstp_nmix_prpr', 'name': '업종지수현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_prdy_vrss', 'name': '업종지수전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'bstp_nmix_prdy_ctrt', 'name': '업종지수전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prdy_vol', 'name': '전일거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prdy_tr_pbmn', 'name': '전일거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bstp_nmix_oprc', 'name': '업종지수시가2', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_nmix_vrss_nmix_oprc', 'name': '전일지수대비지수시가2', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'oprc_vrss_prpr_sign', 'name': '시가2대비현재가부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'bstp_nmix_oprc_prdy_ctrt', 'name': '업종지수시가2전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'bstp_nmix_hgpr', 'name': '업종지수최고가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_nmix_vrss_nmix_hgpr', 'name': '전일지수대비지수최고가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'hgpr_vrss_prpr_sign', 'name': '최고가대비현재가부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'bstp_nmix_hgpr_prdy_ctrt', 'name': '업종지수최고가전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'bstp_nmix_lwpr', 'name': '업종지수최저가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_clpr_vrss_lwpr', 'name': '전일종가대비최저가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'lwpr_vrss_prpr_sign', 'name': '최저가대비현재가부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_clpr_vrss_lwpr_rate', 'name': '전일종가대비최저가비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'ascn_issu_cnt', 'name': '상승종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'uplm_issu_cnt', 'name': '상한종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'stnr_issu_cnt', 'name': '보합종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'down_issu_cnt', 'name': '하락종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'lslm_issu_cnt', 'name': '하한종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'dryy_bstp_nmix_hgpr', 'name': '연중업종지수최고가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'dryy_hgpr_vrss_prpr_rate', 'name': '연중최고가대비현재가비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'dryy_bstp_nmix_hgpr_date', 'name': '연중업종지수최고가일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'dryy_bstp_nmix_lwpr', 'name': '연중업종지수최저가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'dryy_lwpr_vrss_prpr_rate', 'name': '연중최저가대비현재가비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'dryy_bstp_nmix_lwpr_date', 'name': '연중업종지수최저가일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'total_askp_rsqn', 'name': '총매도호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'total_bidp_rsqn', 'name': '총매수호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'seln_rsqn_rate', 'name': '매도잔량비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'shnu_rsqn_rate', 'name': '매수2잔량비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'ntby_rsqn', 'name': '순매수잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''}
            ]
        }
    },
    # === 국내업종 일자별지수 ===
    'FHPUP02120000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'bstp_nmix_prpr', 'name': '업종지수현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_prdy_vrss', 'name': '업종지수전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'bstp_nmix_prdy_ctrt', 'name': '업종지수전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bstp_nmix_oprc', 'name': '업종지수시가2', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_hgpr', 'name': '업종지수최고가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_lwpr', 'name': '업종지수최저가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vol', 'name': '전일거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ascn_issu_cnt', 'name': '상승종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'down_issu_cnt', 'name': '하락종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'stnr_issu_cnt', 'name': '보합종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'uplm_issu_cnt', 'name': '상한종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'lslm_issu_cnt', 'name': '하한종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'prdy_tr_pbmn', 'name': '전일거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'dryy_bstp_nmix_hgpr_date', 'name': '연중업종지수최고가일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'dryy_bstp_nmix_hgpr', 'name': '연중업종지수최고가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'dryy_bstp_nmix_lwpr', 'name': '연중업종지수최저가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'dryy_bstp_nmix_lwpr_date', 'name': '연중업종지수최저가일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식영업일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'bstp_nmix_prpr', 'name': '업종지수현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'bstp_nmix_prdy_vrss', 'name': '업종지수전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_prdy_ctrt', 'name': '업종지수전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'bstp_nmix_oprc', 'name': '업종지수시가2', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_hgpr', 'name': '업종지수최고가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_lwpr', 'name': '업종지수최저가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'acml_vol_rlim', 'name': '누적거래량비중', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'invt_new_psdg', 'name': '투자신심리도', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'd20_dsrt', 'name': '20일이격도', 'type': 'string', 'required': True, 'length': 112, 'description': ''}
            ]
        }
    },
    # === 국내업종 시간별지수(초) ===
    'FHPUP02110100': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'stck_cntg_hour', 'name': '주식체결시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'bstp_nmix_prpr', 'name': '업종지수현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_prdy_vrss', 'name': '업종지수전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'bstp_nmix_prdy_ctrt', 'name': '업종지수전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'cntg_vol', 'name': '체결거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 국내업종 시간별지수(분) ===
    'FHPUP02110200': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'bsop_hour', 'name': '영업시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'bstp_nmix_prpr', 'name': '업종지수현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_prdy_vrss', 'name': '업종지수전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'bstp_nmix_prdy_ctrt', 'name': '업종지수전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'cntg_vol', 'name': '체결거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 업종 분봉조회 ===
    'FHKUP03500200': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'Output1': {
            'type': 'array',
            'fields': [
                {'key': 'bstp_nmix_prdy_vrss', 'name': '업종지수전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'bstp_nmix_prdy_ctrt', 'name': '업종지수전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'prdy_nmix', 'name': '전일지수', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'bstp_nmix_prpr', 'name': '업종지수현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_cls_code', 'name': '업종구분코드', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
                {'key': 'prdy_vol', 'name': '전일거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bstp_nmix_oprc', 'name': '업종지수시가2', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_hgpr', 'name': '업종지수최고가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_lwpr', 'name': '업종지수최저가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'futs_prdy_oprc', 'name': '선물전일시가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'futs_prdy_hgpr', 'name': '선물전일최고가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'futs_prdy_lwpr', 'name': '선물전일최저가', 'type': 'string', 'required': True, 'length': 112, 'description': ''}
            ]
        },
        'Output2': {
            'type': 'object',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식영업일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stck_cntg_hour', 'name': '주식체결시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'bstp_nmix_prpr', 'name': '업종지수현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_oprc', 'name': '업종지수시가2', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_hgpr', 'name': '업종지수최고가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_lwpr', 'name': '업종지수최저가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'cntg_vol', 'name': '체결거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 국내업종 구분별전체시세 ===
    'FHPUP02140000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'bstp_nmix_prpr', 'name': '업종지수현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_prdy_vrss', 'name': '업종지수전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'bstp_nmix_prdy_ctrt', 'name': '업종지수전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bstp_nmix_oprc', 'name': '업종지수시가2', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_hgpr', 'name': '업종지수최고가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_lwpr', 'name': '업종지수최저가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vol', 'name': '전일거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ascn_issu_cnt', 'name': '상승종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'down_issu_cnt', 'name': '하락종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'stnr_issu_cnt', 'name': '보합종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'uplm_issu_cnt', 'name': '상한종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'lslm_issu_cnt', 'name': '하한종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'prdy_tr_pbmn', 'name': '전일거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'dryy_bstp_nmix_hgpr_date', 'name': '연중업종지수최고가일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'dryy_bstp_nmix_hgpr', 'name': '연중업종지수최고가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'dryy_bstp_nmix_lwpr', 'name': '연중업종지수최저가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'dryy_bstp_nmix_lwpr_date', 'name': '연중업종지수최저가일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'bstp_cls_code', 'name': '업종구분코드', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'bstp_nmix_prpr', 'name': '업종지수현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_prdy_vrss', 'name': '업종지수전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'bstp_nmix_prdy_ctrt', 'name': '업종지수전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_vol_rlim', 'name': '누적거래량비중', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'acml_tr_pbmn_rlim', 'name': '누적거래대금비중', 'type': 'string', 'required': True, 'length': 72, 'description': ''}
            ]
        }
    },
    # === 국내주식 예상체결지수 추이 ===
    'FHPST01840000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'stck_cntg_hour', 'name': '주식단축종목코드', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'bstp_nmix_prpr', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'bstp_nmix_prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '기준가대비현재가', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 국내주식 예상체결 전체지수 ===
    'FHKUP11750000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'bstp_nmix_prpr', 'name': '업종지수현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_prdy_vrss', 'name': '업종지수전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ascn_issu_cnt', 'name': '상승종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'down_issu_cnt', 'name': '하락종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'stnr_issu_cnt', 'name': '보합종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'bstp_cls_code', 'name': '업종구분코드', 'type': 'string', 'required': True, 'length': 4, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'bstp_nmix_prpr', 'name': '업종지수현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bstp_nmix_prdy_vrss', 'name': '업종지수전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'bstp_nmix_prdy_ctrt', 'name': '업종지수전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nmix_sdpr', 'name': '지수기준가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'ascn_issu_cnt', 'name': '상승종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'stnr_issu_cnt', 'name': '보합종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'down_issu_cnt', 'name': '하락종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''}
            ]
        }
    },
    # === 변동성완화장치(VI) 현황 ===
    'FHPST01390000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'vi_cls_code', 'name': 'VI발동상태', 'type': 'string', 'required': True, 'length': 1, 'description': 'Y: 발동 / N: 해제'},
                {'key': 'bsop_date', 'name': '영업일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'cntg_vi_hour', 'name': 'VI발동시간', 'type': 'string', 'required': True, 'length': 6, 'description': 'VI발동시간'},
                {'key': 'vi_cncl_hour', 'name': 'VI해제시간', 'type': 'string', 'required': True, 'length': 6, 'description': 'VI해제시간'},
                {'key': 'vi_kind_code', 'name': 'VI종류코드', 'type': 'string', 'required': True, 'length': 1, 'description': '1:정적 2:동적 3:정적&동적'},
                {'key': 'vi_prc', 'name': 'VI발동가격', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'vi_stnd_prc', 'name': '정적VI발동기준가격', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'vi_dprt', 'name': '정적VI발동괴리율', 'type': 'string', 'required': True, 'length': 82, 'description': '%'},
                {'key': 'vi_dmc_stnd_prc', 'name': '동적VI발동기준가격', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'vi_dmc_dprt', 'name': '동적VI발동괴리율', 'type': 'string', 'required': True, 'length': 82, 'description': '%'},
                {'key': 'vi_count', 'name': 'VI발동횟수', 'type': 'string', 'required': True, 'length': 7, 'description': ''}
            ]
        }
    },
    # === 국내휴장일조회 ===
    'CTCA0903R': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'bass_dt', 'name': '기준일자', 'type': 'string', 'required': True, 'length': 8, 'description': '기준일자(YYYYMMDD)'},
                {'key': 'wday_dvsn_cd', 'name': '요일구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': '01:일요일, 02:월요일, 03:화요일, 04:수요일, 05:목요일, 06:금요일, 07:토요일'},
                {'key': 'bzdy_yn', 'name': '영업일여부', 'type': 'string', 'required': True, 'length': 1, 'description': 'Y/N 금융기관이 업무를 하는 날'},
                {'key': 'tr_day_yn', 'name': '거래일여부', 'type': 'string', 'required': True, 'length': 1, 'description': 'Y/N 증권 업무가 가능한 날(입출금, 이체 등의 업무 포함)'},
                {'key': 'opnd_yn', 'name': '개장일여부', 'type': 'string', 'required': True, 'length': 1, 'description': 'Y/N 주식시장이 개장되는 날 * 주문을 넣고자 할 경우 개장일여부(opnd_yn)를 사용'},
                {'key': 'sttl_day_yn', 'name': '결제일여부', 'type': 'string', 'required': True, 'length': 1, 'description': 'Y/N 주식 거래에서 실제로 주식을 인수하고 돈을 지불하는 날'}
            ]
        }
    },
    # === 국내선물 영업일조회 ===
    'HHMCM000002C0': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'date1', 'name': '영업일1', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'date2', 'name': '영업일2', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'date3', 'name': '영업일3', 'type': 'string', 'required': True, 'length': 8, 'description': '영업일 당일'},
                {'key': 'date4', 'name': '영업일4', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'date5', 'name': '영업일5', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'today', 'name': '오늘일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'time', 'name': '현재시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 's_time', 'name': '장시작시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'e_time', 'name': '장마감시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''}
            ]
        }
    }
}
