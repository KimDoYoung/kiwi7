# KIS REST API Response Definitions
# Auto-generated from Excel file

KIS_RESPONSE_DEF_2 = {
    # === 거래량순위 ===
    'FHPST01710000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'Output': {
            'type': 'array',
            'fields': [
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prdy_vol', 'name': '전일거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'lstn_stcn', 'name': '상장주수', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'avrg_vol', 'name': '평균거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'n_befr_clpr_vrss_prpr_rate', 'name': 'N일전종가대비현재가대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'vol_inrt', 'name': '거래량증가율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'vol_tnrt', 'name': '거래량회전율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nday_vol_tnrt', 'name': 'N일거래량회전율', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'avrg_tr_pbmn', 'name': '평균거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'tr_pbmn_tnrt', 'name': '거래대금회전율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nday_tr_pbmn_tnrt', 'name': 'N일거래대금회전율', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 국내주식 등락률 순위 ===
    'FHPST01700000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'stck_shrn_iscd', 'name': '주식단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'stck_hgpr', 'name': '주식최고가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hgpr_hour', 'name': '최고가시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'acml_hgpr_date', 'name': '누적최고가일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stck_lwpr', 'name': '주식최저가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'lwpr_hour', 'name': '최저가시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'acml_lwpr_date', 'name': '누적최저가일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'lwpr_vrss_prpr_rate', 'name': '최저가대비현재가비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'dsgt_date_clpr_vrss_prpr_rate', 'name': '지정일자종가대비현재가비', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'cnnt_ascn_dynu', 'name': '연속상승일수', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'hgpr_vrss_prpr_rate', 'name': '최고가대비현재가비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'cnnt_down_dynu', 'name': '연속하락일수', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'oprc_vrss_prpr_sign', 'name': '시가2대비현재가부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'oprc_vrss_prpr', 'name': '시가2대비현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'oprc_vrss_prpr_rate', 'name': '시가2대비현재가비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'prd_rsfl', 'name': '기간등락', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prd_rsfl_rate', 'name': '기간등락비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''}
            ]
        }
    },
    # === 국내주식 호가잔량 순위 ===
    'FHPST01720000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'total_askp_rsqn', 'name': '총매도호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'total_bidp_rsqn', 'name': '총매수호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'total_ntsl_bidp_rsqn', 'name': '총순매수호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'shnu_rsqn_rate', 'name': '매수잔량비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'seln_rsqn_rate', 'name': '매도잔량비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''}
            ]
        }
    },
    # === 국내주식 수익자산지표 순위 ===
    'FHPST01730000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'sale_totl_prfi', 'name': '매출총이익', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'bsop_prti', 'name': '영업이익', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'op_prfi', 'name': '경상이익', 'type': 'string', 'required': True, 'length': 182, 'description': ''},
                {'key': 'thtr_ntin', 'name': '당기순이익', 'type': 'string', 'required': True, 'length': 102, 'description': ''},
                {'key': 'total_aset', 'name': '자산총계', 'type': 'string', 'required': True, 'length': 102, 'description': ''},
                {'key': 'total_lblt', 'name': '부채총계', 'type': 'string', 'required': True, 'length': 102, 'description': ''},
                {'key': 'total_cptl', 'name': '자본총계', 'type': 'string', 'required': True, 'length': 102, 'description': ''},
                {'key': 'stac_month', 'name': '결산월', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'stac_month_cls_code', 'name': '결산월구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'iqry_csnu', 'name': '조회건수', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 국내주식 시가총액 상위 ===
    'FHPST01740000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'lstn_stcn', 'name': '상장주수', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'stck_avls', 'name': '시가총액', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'mrkt_whol_avls_rlim', 'name': '시장전체시가총액비중', 'type': 'string', 'required': True, 'length': 52, 'description': ''}
            ]
        }
    },
    # === 국내주식 재무비율 순위 ===
    'FHPST01750000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'cptl_op_prfi', 'name': '총자본경상이익율', 'type': 'string', 'required': True, 'length': 92, 'description': ''},
                {'key': 'cptl_ntin_rate', 'name': '총자본순이익율', 'type': 'string', 'required': True, 'length': 92, 'description': ''},
                {'key': 'sale_totl_rate', 'name': '매출액총이익율', 'type': 'string', 'required': True, 'length': 92, 'description': ''},
                {'key': 'sale_ntin_rate', 'name': '매출액순이익율', 'type': 'string', 'required': True, 'length': 92, 'description': ''},
                {'key': 'bis', 'name': '자기자본비율', 'type': 'string', 'required': True, 'length': 92, 'description': ''},
                {'key': 'lblt_rate', 'name': '부채비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'bram_depn', 'name': '차입금의존도', 'type': 'string', 'required': True, 'length': 92, 'description': ''},
                {'key': 'rsrv_rate', 'name': '유보비율', 'type': 'string', 'required': True, 'length': 124, 'description': ''},
                {'key': 'grs', 'name': '매출액증가율', 'type': 'string', 'required': True, 'length': 124, 'description': ''},
                {'key': 'op_prfi_inrt', 'name': '경상이익증가율', 'type': 'string', 'required': True, 'length': 124, 'description': ''},
                {'key': 'bsop_prfi_inrt', 'name': '영업이익증가율', 'type': 'string', 'required': True, 'length': 124, 'description': ''},
                {'key': 'ntin_inrt', 'name': '순이익증가율', 'type': 'string', 'required': True, 'length': 124, 'description': ''},
                {'key': 'equt_inrt', 'name': '자기자본증가율', 'type': 'string', 'required': True, 'length': 92, 'description': ''},
                {'key': 'cptl_tnrt', 'name': '총자본회전율', 'type': 'string', 'required': True, 'length': 92, 'description': ''},
                {'key': 'sale_bond_tnrt', 'name': '매출채권회전율', 'type': 'string', 'required': True, 'length': 92, 'description': ''},
                {'key': 'totl_aset_inrt', 'name': '총자산증가율', 'type': 'string', 'required': True, 'length': 92, 'description': ''},
                {'key': 'stac_month', 'name': '결산월', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'stac_month_cls_code', 'name': '결산월구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'iqry_csnu', 'name': '조회건수', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 국내주식 시간외잔량 순위 ===
    'FHPST01760000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'stck_shrn_iscd', 'name': '주식단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'ovtm_total_askp_rsqn', 'name': '시간외총매도호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_total_bidp_rsqn', 'name': '시간외총매수호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'mkob_otcp_vol', 'name': '장개시전시간외종가거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'mkfa_otcp_vol', 'name': '장종료후시간외종가거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 국내주식 이격도 순위 ===
    'FHPST01780000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'd5_dsrt', 'name': '5일이격도', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'd10_dsrt', 'name': '10일이격도', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'd20_dsrt', 'name': '20일이격도', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'd60_dsrt', 'name': '60일이격도', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'd120_dsrt', 'name': '120일이격도', 'type': 'string', 'required': True, 'length': 112, 'description': ''}
            ]
        }
    },
    # === 국내주식 시장가치 순위 ===
    'FHPST01790000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'per', 'name': 'PER', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'pbr', 'name': 'PBR', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'pcr', 'name': 'PCR', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'psr', 'name': 'PSR', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'eps', 'name': 'EPS', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'eva', 'name': 'EVA', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'ebitda', 'name': 'EBITDA', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'pv_div_ebitda', 'name': 'PVDIVEBITDA', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'ebitda_div_fnnc_expn', 'name': 'EBITDADIV금융비용', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'stac_month', 'name': '결산월', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'stac_month_cls_code', 'name': '결산월구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'iqry_csnu', 'name': '조회건수', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 국내주식 체결강도 상위 ===
    'FHPST01680000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'stck_shrn_iscd', 'name': '주식단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'tday_rltv', 'name': '당일체결강도', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'seln_cnqn_smtn', 'name': '매도체결량합계', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'shnu_cnqn_smtn', 'name': '매수2체결량합계', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 국내주식 관심종목등록 상위 ===
    'FHPST01800000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'mrkt_div_cls_name', 'name': '시장분류구분명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'askp', 'name': '매도호가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'bidp', 'name': '매수호가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'inter_issu_reg_csnu', 'name': '관심종목등록건수', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 국내주식 당사매매종목 상위 ===
    'FHPST01860000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'seln_cnqn_smtn', 'name': '매도체결량합계', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'shnu_cnqn_smtn', 'name': '매수2체결량합계', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ntby_cnqn', 'name': '순매수체결량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 국내주식 배당률 상위 ===
    'HHKDB13470100': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'rank', 'name': '순위', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
                {'key': 'sht_cd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'isin_name', 'name': '종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'record_date', 'name': '기준일', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'per_sto_divi_amt', 'name': '현금/주식배당금', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'divi_rate', 'name': '현금/주식배당률(%)', 'type': 'string', 'required': True, 'length': 62, 'description': ''},
                {'key': 'divi_kind', 'name': '배당종류', 'type': 'string', 'required': True, 'length': 8, 'description': ''}
            ]
        }
    },
    # === 국내주식 대량체결건수 상위 ===
    'FHKST190900C0': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'data_rank', 'name': '데이터순위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'shnu_cntg_csnu', 'name': '매수2체결건수', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'seln_cntg_csnu', 'name': '매도체결건수', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ntby_cnqn', 'name': '순매수체결량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 국내주식 신용잔고 상위 ===
    'FHKST17010000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'bstp_cls_code', 'name': '업종구분코드', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stnd_date1', 'name': '기준일자1', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stnd_date2', 'name': '기준일자2', 'type': 'string', 'required': True, 'length': 8, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_loan_rmnd_stcn', 'name': '전체융자잔고주수', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_loan_rmnd_amt', 'name': '전체융자잔고금액', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_loan_rmnd_rate', 'name': '전체융자잔고비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'whol_stln_rmnd_stcn', 'name': '전체대주잔고주수', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_stln_rmnd_amt', 'name': '전체대주잔고금액', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'whol_stln_rmnd_rate', 'name': '전체대주잔고비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'nday_vrss_loan_rmnd_inrt', 'name': 'N일대비융자잔고증가율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'nday_vrss_stln_rmnd_inrt', 'name': 'N일대비대주잔고증가율', 'type': 'string', 'required': True, 'length': 84, 'description': ''}
            ]
        }
    },
    # === 국내주식 공매도 상위종목 ===
    'FHPST04820000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ssts_cntg_qty', 'name': '공매도체결수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ssts_vol_rlim', 'name': '공매도거래량비중', 'type': 'string', 'required': True, 'length': 62, 'description': ''},
                {'key': 'ssts_tr_pbmn', 'name': '공매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ssts_tr_pbmn_rlim', 'name': '공매도거래대금비중', 'type': 'string', 'required': True, 'length': 62, 'description': ''},
                {'key': 'stnd_date1', 'name': '기준일자1', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stnd_date2', 'name': '기준일자2', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'avrg_prc', 'name': '평균가격', 'type': 'string', 'required': True, 'length': 11, 'description': ''}
            ]
        }
    },
    # === 국내주식 시간외등락율순위 ===
    'FHPST02340000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'ovtm_untp_uplm_issu_cnt', 'name': '시간외단일가상한종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'ovtm_untp_ascn_issu_cnt', 'name': '시간외단일가상승종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'ovtm_untp_stnr_issu_cnt', 'name': '시간외단일가보합종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'ovtm_untp_lslm_issu_cnt', 'name': '시간외단일가하한종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'ovtm_untp_down_issu_cnt', 'name': '시간외단일가하락종목수', 'type': 'string', 'required': True, 'length': 7, 'description': ''},
                {'key': 'ovtm_untp_acml_vol', 'name': '시간외단일가누적거래량', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ovtm_untp_acml_tr_pbmn', 'name': '시간외단일가누적거래대금', 'type': 'string', 'required': True, 'length': 19, 'description': ''},
                {'key': 'ovtm_untp_exch_vol', 'name': '시간외단일가거래소거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_exch_tr_pbmn', 'name': '시간외단일가거래소거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_kosdaq_vol', 'name': '시간외단일가KOSDAQ거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_kosdaq_tr_pbmn', 'name': '시간외단일가KOSDAQ거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'mksc_shrn_iscd', 'name': '유가증권단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'ovtm_untp_prpr', 'name': '시간외단일가현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_prdy_vrss', 'name': '시간외단일가전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_prdy_vrss_sign', 'name': '시간외단일가전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'ovtm_untp_prdy_ctrt', 'name': '시간외단일가전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'ovtm_untp_askp1', 'name': '시간외단일가매도호가1', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_seln_rsqn', 'name': '시간외단일가매도잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_bidp1', 'name': '시간외단일가매수호가1', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_shnu_rsqn', 'name': '시간외단일가매수잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_vol', 'name': '시간외단일가거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ovtm_vrss_acml_vol_rlim', 'name': '시간외대비누적거래량비중', 'type': 'string', 'required': True, 'length': 52, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bidp', 'name': '매수호가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'askp', 'name': '매도호가', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 국내주식 시간외거래량순위 ===
    'FHPST02350000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'ovtm_untp_exch_vol', 'name': '시간외단일가거래소거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_exch_tr_pbmn', 'name': '시간외단일가거래소거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_kosdaq_vol', 'name': '시간외단일가KOSDAQ거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_kosdaq_tr_pbmn', 'name': '시간외단일가KOSDAQ거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'stck_shrn_iscd', 'name': '주식단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'ovtm_untp_prpr', 'name': '시간외단일가현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_prdy_vrss', 'name': '시간외단일가전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_prdy_vrss_sign', 'name': '시간외단일가전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'ovtm_untp_prdy_ctrt', 'name': '시간외단일가전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'ovtm_untp_seln_rsqn', 'name': '시간외단일가매도잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_shnu_rsqn', 'name': '시간외단일가매수잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_vol', 'name': '시간외단일가거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ovtm_vrss_acml_vol_rlim', 'name': '시간외대비누적거래량비중', 'type': 'string', 'required': True, 'length': 52, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'bidp', 'name': '매수호가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'askp', 'name': '매도호가', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === HTS조회상위20종목 ===
    'HHMCM000100C0': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'mrkt_div_cls_code', 'name': '시장구분', 'type': 'string', 'required': True, 'length': 9, 'description': 'J : 코스피, Q : 코스닥'},
                {'key': 'mksc_shrn_iscd', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 2, 'description': '종목코드'}
            ]
        }
    }
}
