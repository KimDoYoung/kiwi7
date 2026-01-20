# KIS REST API Response Definitions
# Auto-generated from Excel file

KIS_RESPONSE_DEF_1 = {
    # === 주식현재가 시세 ===
    'FHKST01010100': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'iscd_stat_cls_code', 'name': '종목상태구분코드', 'type': 'string', 'required': True, 'length': 3, 'description': '51 : 관리종목 52 : 투자위험 53 : 투자경고 54 : 투자주의 55 : 신용가능 57 : 증거금 100% 58 : 거래정지 59 : 단기과열종목'},
                {'key': 'marg_rate', 'name': '증거금비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'rprs_mrkt_kor_name', 'name': '대표시장한글명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'new_hgpr_lwpr_cls_code', 'name': '신고가저가구분코드', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'bstp_kor_isnm', 'name': '업종한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'temp_stop_yn', 'name': '임시정지여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'oprc_rang_cont_yn', 'name': '시가범위연장여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'clpr_rang_cont_yn', 'name': '종가범위연장여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'crdt_able_yn', 'name': '신용가능여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'grmn_rate_cls_code', 'name': '보증금비율구분코드', 'type': 'string', 'required': True, 'length': 3, 'description': ''},
                {'key': 'elw_pblc_yn', 'name': 'ELW발행여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prdy_vrss_vol_rate', 'name': '전일대비거래량비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'stck_oprc', 'name': '주식시가2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_hgpr', 'name': '주식최고가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_lwpr', 'name': '주식최저가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_mxpr', 'name': '주식상한가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_llam', 'name': '주식하한가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_sdpr', 'name': '주식기준가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'wghn_avrg_stck_prc', 'name': '가중평균주식가격', 'type': 'string', 'required': True, 'length': 192, 'description': ''},
                {'key': 'hts_frgn_ehrt', 'name': 'HTS외국인소진율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'frgn_ntby_qty', 'name': '외국인순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'pgtr_ntby_qty', 'name': '프로그램매매순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'pvt_scnd_dmrs_prc', 'name': '피벗2차디저항가격', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'pvt_frst_dmrs_prc', 'name': '피벗1차디저항가격', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'pvt_pont_val', 'name': '피벗포인트값', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'pvt_frst_dmsp_prc', 'name': '피벗1차디지지가격', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'pvt_scnd_dmsp_prc', 'name': '피벗2차디지지가격', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'dmrs_val', 'name': '디저항값', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'dmsp_val', 'name': '디지지값', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'cpfn', 'name': '자본금', 'type': 'string', 'required': True, 'length': 22, 'description': ''},
                {'key': 'rstc_wdth_prc', 'name': '제한폭가격', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_fcam', 'name': '주식액면가', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'stck_sspr', 'name': '주식대용가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'aspr_unit', 'name': '호가단위', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hts_deal_qty_unit_val', 'name': 'HTS매매수량단위값', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'lstn_stcn', 'name': '상장주수', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'hts_avls', 'name': 'HTS시가총액', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'per', 'name': 'PER', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'pbr', 'name': 'PBR', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'stac_month', 'name': '결산월', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'vol_tnrt', 'name': '거래량회전율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'eps', 'name': 'EPS', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'bps', 'name': 'BPS', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'd250_hgpr', 'name': '250일최고가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'd250_hgpr_date', 'name': '250일최고가일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'd250_hgpr_vrss_prpr_rate', 'name': '250일최고가대비현재가비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'd250_lwpr', 'name': '250일최저가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'd250_lwpr_date', 'name': '250일최저가일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'd250_lwpr_vrss_prpr_rate', 'name': '250일최저가대비현재가비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'stck_dryy_hgpr', 'name': '주식연중최고가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'dryy_hgpr_vrss_prpr_rate', 'name': '연중최고가대비현재가비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'dryy_hgpr_date', 'name': '연중최고가일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stck_dryy_lwpr', 'name': '주식연중최저가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'dryy_lwpr_vrss_prpr_rate', 'name': '연중최저가대비현재가비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'dryy_lwpr_date', 'name': '연중최저가일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'w52_hgpr', 'name': '52주일최고가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'w52_hgpr_vrss_prpr_ctrt', 'name': '52주일최고가대비현재가대비', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'w52_hgpr_date', 'name': '52주일최고가일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'w52_lwpr', 'name': '52주일최저가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'w52_lwpr_vrss_prpr_ctrt', 'name': '52주일최저가대비현재가대비', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'w52_lwpr_date', 'name': '52주일최저가일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'whol_loan_rmnd_rate', 'name': '전체융자잔고비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'ssts_yn', 'name': '공매도가능여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'stck_shrn_iscd', 'name': '주식단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'fcam_cnnm', 'name': '액면가통화명', 'type': 'string', 'required': True, 'length': 20, 'description': ''},
                {'key': 'cpfn_cnnm', 'name': '자본금통화명', 'type': 'string', 'required': True, 'length': 20, 'description': ''},
                {'key': 'apprch_rate', 'name': '접근도', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'frgn_hldn_qty', 'name': '외국인보유수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'vi_cls_code', 'name': 'VI적용구분코드', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'ovtm_vi_cls_code', 'name': '시간외단일가VI적용구분코드', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'last_ssts_cntg_qty', 'name': '최종공매도체결수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'invt_caful_yn', 'name': '투자유의여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'mrkt_warn_cls_code', 'name': '시장경고코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'short_over_yn', 'name': '단기과열여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'sltr_yn', 'name': '정리매매여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'mang_issu_cls_code', 'name': '관리종목여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''}
            ]
        }
    },
    # === 주식현재가 시세2 ===
    'FHPST01010000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'rprs_mrkt_kor_name', 'name': '대표시장한글명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'new_hgpr_lwpr_cls_code', 'name': '신고가저가구분코드', 'type': 'string', 'required': True, 'length': 10, 'description': '특정 경우에만 데이터 출력'},
                {'key': 'mxpr_llam_cls_code', 'name': '상하한가구분코드', 'type': 'string', 'required': True, 'length': 10, 'description': '특정 경우에만 데이터 출력'},
                {'key': 'crdt_able_yn', 'name': '신용가능여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'stck_mxpr', 'name': '주식상한가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'elw_pblc_yn', 'name': 'ELW발행여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_clpr_vrss_oprc_rate', 'name': '전일종가대비시가2비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'crdt_rate', 'name': '신용비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'marg_rate', 'name': '증거금비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'lwpr_vrss_prpr', 'name': '최저가대비현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'lwpr_vrss_prpr_sign', 'name': '최저가대비현재가부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_clpr_vrss_lwpr_rate', 'name': '전일종가대비최저가비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'stck_lwpr', 'name': '주식최저가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hgpr_vrss_prpr', 'name': '최고가대비현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'hgpr_vrss_prpr_sign', 'name': '최고가대비현재가부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_clpr_vrss_hgpr_rate', 'name': '전일종가대비최고가비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'stck_hgpr', 'name': '주식최고가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'oprc_vrss_prpr', 'name': '시가2대비현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'oprc_vrss_prpr_sign', 'name': '시가2대비현재가부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'mang_issu_yn', 'name': '관리종목여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'divi_app_cls_code', 'name': '동시호가배분처리코드', 'type': 'string', 'required': True, 'length': 2, 'description': '11:매수상한배분 12:매수하한배분 13: 매도상한배분 14:매도하한배분'},
                {'key': 'short_over_yn', 'name': '단기과열여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'mrkt_warn_cls_code', 'name': '시장경고코드', 'type': 'string', 'required': True, 'length': 2, 'description': '00: 없음 01: 투자주의 02:투자경고 03:투자위험'},
                {'key': 'invt_caful_yn', 'name': '투자유의여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'stange_runup_yn', 'name': '이상급등여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'ssts_hot_yn', 'name': '공매도과열여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'low_current_yn', 'name': '저유동성종목여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'vi_cls_code', 'name': 'VI적용구분코드', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'short_over_cls_code', 'name': '단기과열구분코드', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_llam', 'name': '주식하한가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'new_lstn_cls_name', 'name': '신규상장구분명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'vlnt_deal_cls_name', 'name': '임의매매구분명', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'flng_cls_name', 'name': '락구분이름', 'type': 'string', 'required': True, 'length': 40, 'description': '특정 경우에만 데이터 출력'},
                {'key': 'revl_issu_reas_name', 'name': '재평가종목사유명', 'type': 'string', 'required': True, 'length': 40, 'description': '특정 경우에만 데이터 출력'},
                {'key': 'mrkt_warn_cls_name', 'name': '시장경고구분명', 'type': 'string', 'required': True, 'length': 40, 'description': '특정 경우에만 데이터 출력 "투자환기" / "투자경고"'},
                {'key': 'stck_sdpr', 'name': '주식기준가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'bstp_cls_code', 'name': '업종구분코드', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
                {'key': 'stck_prdy_clpr', 'name': '주식전일종가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'insn_pbnt_yn', 'name': '불성실공시여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'fcam_mod_cls_name', 'name': '액면가변경구분명', 'type': 'string', 'required': True, 'length': 10, 'description': '특정 경우에만 데이터 출력'},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prdy_vrss_vol_rate', 'name': '전일대비거래량비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'bstp_kor_isnm', 'name': '업종한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': '※ 거래소 정보로 특정 종목은 업종구분이 없어 데이터 미회신'},
                {'key': 'sltr_yn', 'name': '정리매매여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'trht_yn', 'name': '거래정지여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'oprc_rang_cont_yn', 'name': '시가범위연장여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'vlnt_fin_cls_code', 'name': '임의종료구분코드', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'stck_oprc', 'name': '주식시가2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vol', 'name': '전일거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 주식현재가 체결 ===
    'FHKST01010300': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'stck_cntg_hour', 'name': '주식체결시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'cntg_vol', 'name': '체결거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'tday_rltv', 'name': '당일체결강도', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''}
            ]
        }
    },
    # === 주식현재가 일자별 ===
    'FHKST01010400': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식영업일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stck_oprc', 'name': '주식시가2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_hgpr', 'name': '주식최고가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_lwpr', 'name': '주식최저가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_clpr', 'name': '주식종가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prdy_vrss_vol_rate', 'name': '전일대비거래량비율', 'type': 'string', 'required': True, 'length': 84, 'description': '13(8.4)'},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': '11(8.2)'},
                {'key': 'hts_frgn_ehrt', 'name': 'HTS외국인소진율', 'type': 'string', 'required': True, 'length': 82, 'description': '11(8.2)'},
                {'key': 'frgn_ntby_qty', 'name': '외국인순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'flng_cls_code', 'name': '락구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': '\'01 : 권리락  02 : 배당락  03 : 분배락  04 : 권배락  05 : 중간(분기)배당락  06 : 권리중간배당락  07 : 권리분기배당락\''},
                {'key': 'acml_prtt_rate', 'name': '누적분할비율', 'type': 'string', 'required': True, 'length': 84, 'description': '13(8.4)'}
            ]
        }
    },
    # === 주식현재가 투자자 ===
    'FHKST01010900': {
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
                {'key': 'prsn_ntby_qty', 'name': '개인순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'frgn_ntby_qty', 'name': '외국인순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'orgn_ntby_qty', 'name': '기관계순매수수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_ntby_tr_pbmn', 'name': '개인순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_ntby_tr_pbmn', 'name': '외국인순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_ntby_tr_pbmn', 'name': '기관계순매수거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_shnu_vol', 'name': '개인매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_shnu_vol', 'name': '외국인매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_shnu_vol', 'name': '기관계매수2거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_shnu_tr_pbmn', 'name': '개인매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_shnu_tr_pbmn', 'name': '외국인매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_shnu_tr_pbmn', 'name': '기관계매수2거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_seln_vol', 'name': '개인매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_seln_vol', 'name': '외국인매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_seln_vol', 'name': '기관계매도거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prsn_seln_tr_pbmn', 'name': '개인매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'frgn_seln_tr_pbmn', 'name': '외국인매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'orgn_seln_tr_pbmn', 'name': '기관계매도거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 주식현재가 회원사 ===
    'FHKST01010600': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': '성공 실패 여부  성공 : 0   실패 : 0외 값'},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': '응답코드'},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': '응답메세지'},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'seln_mbcr_no1', 'name': '매도회원사번호1', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'seln_mbcr_no2', 'name': '매도회원사번호2', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'seln_mbcr_no3', 'name': '매도회원사번호3', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'seln_mbcr_no4', 'name': '매도회원사번호4', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'seln_mbcr_no5', 'name': '매도회원사번호5', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'seln_mbcr_name1', 'name': '매도회원사명1', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'seln_mbcr_name2', 'name': '매도회원사명2', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'seln_mbcr_name3', 'name': '매도회원사명3', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'seln_mbcr_name4', 'name': '매도회원사명4', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'seln_mbcr_name5', 'name': '매도회원사명5', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'total_seln_qty1', 'name': '총매도수량1', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'total_seln_qty2', 'name': '총매도수량2', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'total_seln_qty3', 'name': '총매도수량3', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'total_seln_qty4', 'name': '총매도수량4', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'total_seln_qty5', 'name': '총매도수량5', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'seln_mbcr_rlim1', 'name': '매도회원사비중1', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'seln_mbcr_rlim2', 'name': '매도회원사비중2', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'seln_mbcr_rlim3', 'name': '매도회원사비중3', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'seln_mbcr_rlim4', 'name': '매도회원사비중4', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'seln_mbcr_rlim5', 'name': '매도회원사비중5', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'seln_qty_icdc1', 'name': '매도수량증감1', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'seln_qty_icdc2', 'name': '매도수량증감2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'seln_qty_icdc3', 'name': '매도수량증감3', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'seln_qty_icdc4', 'name': '매도수량증감4', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'seln_qty_icdc5', 'name': '매도수량증감5', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'shnu_mbcr_no1', 'name': '매수2회원사번호1', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'shnu_mbcr_no2', 'name': '매수2회원사번호2', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'shnu_mbcr_no3', 'name': '매수2회원사번호3', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'shnu_mbcr_no4', 'name': '매수2회원사번호4', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'shnu_mbcr_no5', 'name': '매수2회원사번호5', 'type': 'string', 'required': True, 'length': 5, 'description': ''},
                {'key': 'shnu_mbcr_name1', 'name': '매수2회원사명1', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'shnu_mbcr_name2', 'name': '매수2회원사명2', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'shnu_mbcr_name3', 'name': '매수2회원사명3', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'shnu_mbcr_name4', 'name': '매수2회원사명4', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'shnu_mbcr_name5', 'name': '매수2회원사명5', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'total_shnu_qty1', 'name': '총매수2수량1', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'total_shnu_qty2', 'name': '총매수2수량2', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'total_shnu_qty3', 'name': '총매수2수량3', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'total_shnu_qty4', 'name': '총매수2수량4', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'total_shnu_qty5', 'name': '총매수2수량5', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'shnu_mbcr_rlim1', 'name': '매수2회원사비중1', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'shnu_mbcr_rlim2', 'name': '매수2회원사비중2', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'shnu_mbcr_rlim3', 'name': '매수2회원사비중3', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'shnu_mbcr_rlim4', 'name': '매수2회원사비중4', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'shnu_mbcr_rlim5', 'name': '매수2회원사비중5', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'shnu_qty_icdc1', 'name': '매수2수량증감1', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'shnu_qty_icdc2', 'name': '매수2수량증감2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'shnu_qty_icdc3', 'name': '매수2수량증감3', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'shnu_qty_icdc4', 'name': '매수2수량증감4', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'shnu_qty_icdc5', 'name': '매수2수량증감5', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'glob_total_seln_qty', 'name': '외국계총매도수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'glob_seln_rlim', 'name': '외국계매도비중', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'glob_ntby_qty', 'name': '외국계순매수수량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'glob_total_shnu_qty', 'name': '외국계총매수2수량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'glob_shnu_rlim', 'name': '외국계매수2비중', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'seln_mbcr_glob_yn_1', 'name': '매도회원사외국계여부1', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'seln_mbcr_glob_yn_2', 'name': '매도회원사외국계여부2', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'seln_mbcr_glob_yn_3', 'name': '매도회원사외국계여부3', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'seln_mbcr_glob_yn_4', 'name': '매도회원사외국계여부4', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'seln_mbcr_glob_yn_5', 'name': '매도회원사외국계여부5', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'shnu_mbcr_glob_yn_1', 'name': '매수2회원사외국계여부1', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'shnu_mbcr_glob_yn_2', 'name': '매수2회원사외국계여부2', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'shnu_mbcr_glob_yn_3', 'name': '매수2회원사외국계여부3', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'shnu_mbcr_glob_yn_4', 'name': '매수2회원사외국계여부4', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'shnu_mbcr_glob_yn_5', 'name': '매수2회원사외국계여부5', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'glob_total_seln_qty_icdc', 'name': '외국계총매도수량증감', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'glob_total_shnu_qty_icdc', 'name': '외국계총매수2수량증감', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 주식당일분봉조회 ===
    'FHKST03010200': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': '전일 대비 변동 (+-변동차이)'},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': '전일 대비 부호'},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 10, 'description': '소수점 두자리까지 제공'},
                {'key': 'stck_prdy_clpr', 'name': '전일대비종가', 'type': 'string', 'required': True, 'length': 10, 'description': '전일대비 종가'},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': '누적 거래량'},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': '누적 거래대금'},
                {'key': 'hts_kor_isnm', 'name': '한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': '한글 종목명 (HTS 기준)'},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': '주식 현재가'}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식영업일자', 'type': 'string', 'required': True, 'length': 8, 'description': '주식 영업일자'},
                {'key': 'stck_cntg_hour', 'name': '주식체결시간', 'type': 'string', 'required': True, 'length': 6, 'description': '주식 체결시간'},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': '주식 현재가'},
                {'key': 'stck_oprc', 'name': '주식시가', 'type': 'string', 'required': True, 'length': 10, 'description': '주식 시가'},
                {'key': 'stck_hgpr', 'name': '주식최고가', 'type': 'string', 'required': True, 'length': 10, 'description': '주식 최고가'},
                {'key': 'stck_lwpr', 'name': '주식최저가', 'type': 'string', 'required': True, 'length': 10, 'description': '주식 최저가'},
                {'key': 'cntg_vol', 'name': '체결거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 주식일별분봉조회 ===
    'FHKST03010230': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'stck_prdy_clpr', 'name': '주식전일종가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식영업일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stck_cntg_hour', 'name': '주식체결시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_oprc', 'name': '주식시가2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_hgpr', 'name': '주식최고가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_lwpr', 'name': '주식최저가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'cntg_vol', 'name': '체결거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 주식현재가 당일시간대별체결 ===
    'FHPST01060000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'prdy_vol', 'name': '전일거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'rprs_mrkt_kor_name', 'name': '대표시장한글명', 'type': 'string', 'required': True, 'length': 40, 'description': ''}
            ]
        },
        'output2': {
            'type': 'object',
            'fields': [
                {'key': 'stck_cntg_hour', 'name': '주식체결시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'stck_pbpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'askp', 'name': '매도호가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'bidp', 'name': '매수호가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'tday_rltv', 'name': '당일체결강도', 'type': 'string', 'required': True, 'length': 14, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'cnqn', 'name': '체결량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 주식현재가 시간외일자별주가 ===
    'FHPST02320000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'ovtm_untp_prpr', 'name': '시간외단일가현재가', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_prdy_vrss', 'name': '시간외단일가전일대비', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_prdy_vrss_sign', 'name': '시간외단일가전일대비부호', 'type': 'string', 'required': False, 'length': 1, 'description': ''},
                {'key': 'ovtm_untp_prdy_ctrt', 'name': '시간외단일가전일대비율', 'type': 'string', 'required': False, 'length': 11, 'description': '11(8.2)'},
                {'key': 'ovtm_untp_vol', 'name': '시간외단일가거래량', 'type': 'string', 'required': False, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_tr_pbmn', 'name': '시간외단일가거래대금', 'type': 'string', 'required': False, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_mxpr', 'name': '시간외단일가상한가', 'type': 'string', 'required': False, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_llam', 'name': '시간외단일가하한가', 'type': 'string', 'required': False, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_oprc', 'name': '시간외단일가시가2', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_hgpr', 'name': '시간외단일가최고가', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_lwpr', 'name': '시간외단일가최저가', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_antc_cnpr', 'name': '시간외단일가예상체결가', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_antc_cntg_vrss', 'name': '시간외단일가예상체결대비', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_antc_cntg_vrss_sign', 'name': '시간외단일가예상체결대비', 'type': 'string', 'required': False, 'length': 1, 'description': ''},
                {'key': 'ovtm_untp_antc_cntg_ctrt', 'name': '시간외단일가예상체결대비율', 'type': 'string', 'required': False, 'length': 11, 'description': '11(8.2)'},
                {'key': 'ovtm_untp_antc_vol', 'name': '시간외단일가예상거래량', 'type': 'string', 'required': False, 'length': 18, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식영업일자', 'type': 'string', 'required': False, 'length': 8, 'description': ''},
                {'key': 'ovtm_untp_prpr', 'name': '시간외단일가현재가', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_prdy_vrss', 'name': '시간외단일가전일대비', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_prdy_vrss_sign', 'name': '시간외단일가전일대비부호', 'type': 'string', 'required': False, 'length': 1, 'description': ''},
                {'key': 'ovtm_untp_prdy_ctrt', 'name': '시간외단일가전일대비율', 'type': 'string', 'required': False, 'length': 11, 'description': '11(8.2)'},
                {'key': 'ovtm_untp_vol', 'name': '시간외단일가거래량', 'type': 'string', 'required': False, 'length': 18, 'description': ''},
                {'key': 'stck_clpr', 'name': '주식종가', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': False, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': False, 'length': 11, 'description': '11(8.2)'},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': False, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_tr_pbmn', 'name': '시간외단일가거래대금', 'type': 'string', 'required': False, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 주식현재가 시간외시간별체결 ===
    'FHPST02310000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'ovtm_untp_prpr', 'name': '시간외단일가현재가', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_prdy_vrss', 'name': '시간외단일가전일대비', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_prdy_vrss_sign', 'name': '시간외단일가전일대비부호', 'type': 'string', 'required': False, 'length': 1, 'description': ''},
                {'key': 'ovtm_untp_prdy_ctrt', 'name': '시간외단일가전일대비율', 'type': 'string', 'required': False, 'length': 11, 'description': ''},
                {'key': 'ovtm_untp_vol', 'name': '시간외단일가거래량', 'type': 'string', 'required': False, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_tr_pbmn', 'name': '시간외단일가거래대금', 'type': 'string', 'required': False, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_mxpr', 'name': '시간외단일가상한가', 'type': 'string', 'required': False, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_llam', 'name': '시간외단일가하한가', 'type': 'string', 'required': False, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_oprc', 'name': '시간외단일가시가2', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_hgpr', 'name': '시간외단일가최고가', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_lwpr', 'name': '시간외단일가최저가', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_antc_cnpr', 'name': '시간외단일가예상체결가', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_antc_cntg_vrss', 'name': '시간외단일가예상체결대비', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_antc_cntg_vrss_sign', 'name': '시간외단일가예상체결대비', 'type': 'string', 'required': False, 'length': 1, 'description': ''},
                {'key': 'ovtm_untp_antc_cntg_ctrt', 'name': '시간외단일가예상체결대비율', 'type': 'string', 'required': False, 'length': 11, 'description': ''},
                {'key': 'ovtm_untp_antc_vol', 'name': '시간외단일가예상거래량', 'type': 'string', 'required': False, 'length': 18, 'description': ''},
                {'key': 'uplm_sign', 'name': '상한부호', 'type': 'string', 'required': False, 'length': 1, 'description': ''},
                {'key': 'lslm_sign', 'name': '하한부호', 'type': 'string', 'required': False, 'length': 1, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'stck_cntg_hour', 'name': '주식체결시간', 'type': 'string', 'required': False, 'length': 6, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': False, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': False, 'length': 11, 'description': ''},
                {'key': 'askp', 'name': '매도호가', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'bidp', 'name': '매수호가', 'type': 'string', 'required': False, 'length': 10, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': False, 'length': 18, 'description': ''},
                {'key': 'cntg_vol', 'name': '체결거래량', 'type': 'string', 'required': False, 'length': 18, 'description': ''}
            ]
        }
    },
    # === 국내주식 시간외현재가 ===
    'FHPST02300000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'object',
            'fields': [
                {'key': 'bstp_kor_isnm', 'name': '업종한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': '※ 거래소 정보로 특정 종목은 업종구분이 없어 데이터 미회신'},
                {'key': 'mang_issu_cls_name', 'name': '관리종목구분명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'ovtm_untp_prpr', 'name': '시간외단일가현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_prdy_vrss', 'name': '시간외단일가전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_prdy_vrss_sign', 'name': '시간외단일가전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'ovtm_untp_prdy_ctrt', 'name': '시간외단일가전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'ovtm_untp_vol', 'name': '시간외단일가거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_tr_pbmn', 'name': '시간외단일가거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_mxpr', 'name': '시간외단일가상한가', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_llam', 'name': '시간외단일가하한가', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'ovtm_untp_oprc', 'name': '시간외단일가시가2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_hgpr', 'name': '시간외단일가최고가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_lwpr', 'name': '시간외단일가최저가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'marg_rate', 'name': '증거금비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'ovtm_untp_antc_cnpr', 'name': '시간외단일가예상체결가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_antc_cntg_vrss', 'name': '시간외단일가예상체결대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_antc_cntg_vrss_sign', 'name': '시간외단일가예상체결대비', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'ovtm_untp_antc_cntg_ctrt', 'name': '시간외단일가예상체결대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'ovtm_untp_antc_cnqn', 'name': '시간외단일가예상체결량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'crdt_able_yn', 'name': '신용가능여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'new_lstn_cls_name', 'name': '신규상장구분명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'sltr_yn', 'name': '정리매매여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'mang_issu_yn', 'name': '관리종목여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'mrkt_warn_cls_code', 'name': '시장경고구분코드', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'trht_yn', 'name': '거래정지여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'vlnt_deal_cls_name', 'name': '임의매매구분명', 'type': 'string', 'required': True, 'length': 16, 'description': ''},
                {'key': 'ovtm_untp_sdpr', 'name': '시간외단일가기준가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'mrkt_warn_cls_name', 'name': '시장경구구분명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'revl_issu_reas_name', 'name': '재평가종목사유명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'insn_pbnt_yn', 'name': '불성실공시여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'flng_cls_name', 'name': '락구분이름', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'rprs_mrkt_kor_name', 'name': '대표시장한글명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'ovtm_vi_cls_code', 'name': '시간외단일가VI적용구분코드', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'bidp', 'name': '매수호가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'askp', 'name': '매도호가', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 국내주식 시간외호가 ===
    'FHPST02300400': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'ovtm_untp_last_hour', 'name': '시간외단일가최종시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'ovtm_untp_askp1', 'name': '시간외단일가매도호가1', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp2', 'name': '시간외단일가매도호가2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp3', 'name': '시간외단일가매도호가3', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp4', 'name': '시간외단일가매도호가4', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp5', 'name': '시간외단일가매도호가5', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp6', 'name': '시간외단일가매도호가6', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp7', 'name': '시간외단일가매도호가7', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp8', 'name': '시간외단일가매도호가8', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp9', 'name': '시간외단일가매도호가9', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp10', 'name': '시간외단일가매도호가10', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp1', 'name': '시간외단일가매수호가1', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp2', 'name': '시간외단일가매수호가2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp3', 'name': '시간외단일가매수호가3', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp4', 'name': '시간외단일가매수호가4', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp5', 'name': '시간외단일가매수호가5', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp6', 'name': '시간외단일가매수호가6', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp7', 'name': '시간외단일가매수호가7', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp8', 'name': '시간외단일가매수호가8', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp9', 'name': '시간외단일가매수호가9', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp10', 'name': '시간외단일가매수호가10', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp_icdc1', 'name': '시간외단일가매도호가증감1', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp_icdc2', 'name': '시간외단일가매도호가증감2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp_icdc3', 'name': '시간외단일가매도호가증감3', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp_icdc4', 'name': '시간외단일가매도호가증감4', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp_icdc5', 'name': '시간외단일가매도호가증감5', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp_icdc6', 'name': '시간외단일가매도호가증감6', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp_icdc7', 'name': '시간외단일가매도호가증감7', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp_icdc8', 'name': '시간외단일가매도호가증감8', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp_icdc9', 'name': '시간외단일가매도호가증감9', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp_icdc10', 'name': '시간외단일가매도호가증감10', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp_icdc1', 'name': '시간외단일가매수호가증감1', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp_icdc2', 'name': '시간외단일가매수호가증감2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp_icdc3', 'name': '시간외단일가매수호가증감3', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp_icdc4', 'name': '시간외단일가매수호가증감4', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp_icdc5', 'name': '시간외단일가매수호가증감5', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp_icdc6', 'name': '시간외단일가매수호가증감6', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp_icdc7', 'name': '시간외단일가매수호가증감7', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp_icdc8', 'name': '시간외단일가매수호가증감8', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp_icdc9', 'name': '시간외단일가매수호가증감9', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_bidp_icdc10', 'name': '시간외단일가매수호가증감10', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_askp_rsqn1', 'name': '시간외단일가매도호가잔량1', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_askp_rsqn2', 'name': '시간외단일가매도호가잔량2', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_askp_rsqn3', 'name': '시간외단일가매도호가잔량3', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_askp_rsqn4', 'name': '시간외단일가매도호가잔량4', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_askp_rsqn5', 'name': '시간외단일가매도호가잔량5', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_askp_rsqn6', 'name': '시간외단일가매도호가잔량6', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_askp_rsqn7', 'name': '시간외단일가매도호가잔량7', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_askp_rsqn8', 'name': '시간외단일가매도호가잔량8', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_askp_rsqn9', 'name': '시간외단일가매도호가잔량9', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_askp_rsqn10', 'name': '시간외단일가매도호가잔량10', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_bidp_rsqn1', 'name': '시간외단일가매수호가잔량1', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_bidp_rsqn2', 'name': '시간외단일가매수호가잔량2', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_bidp_rsqn3', 'name': '시간외단일가매수호가잔량3', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_bidp_rsqn4', 'name': '시간외단일가매수호가잔량4', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_bidp_rsqn5', 'name': '시간외단일가매수호가잔량5', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_bidp_rsqn6', 'name': '시간외단일가매수호가잔량6', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_bidp_rsqn7', 'name': '시간외단일가매수호가잔량7', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_bidp_rsqn8', 'name': '시간외단일가매수호가잔량8', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_bidp_rsqn9', 'name': '시간외단일가매수호가잔량9', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_bidp_rsqn10', 'name': '시간외단일가매수호가잔량10', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_total_askp_rsqn', 'name': '시간외단일가총매도호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_total_bidp_rsqn', 'name': '시간외단일가총매수호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_untp_total_askp_rsqn_icdc', 'name': '시간외단일가총매도호가잔량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_total_bidp_rsqn_icdc', 'name': '시간외단일가총매수호가잔량', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_untp_ntby_bidp_rsqn', 'name': '시간외단일가순매수호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'total_askp_rsqn', 'name': '총매도호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'total_bidp_rsqn', 'name': '총매수호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'total_askp_rsqn_icdc', 'name': '총매도호가잔량증감', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'total_bidp_rsqn_icdc', 'name': '총매수호가잔량증감', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_total_askp_rsqn', 'name': '시간외총매도호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_total_bidp_rsqn', 'name': '시간외총매수호가잔량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'ovtm_total_askp_icdc', 'name': '시간외총매도호가증감', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'ovtm_total_bidp_icdc', 'name': '시간외총매수호가증감', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        }
    },
    # === 국내주식 장마감 예상체결가 ===
    'FHKST117300C0': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'stck_shrn_iscd', 'name': '주식단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'sdpr_vrss_prpr', 'name': '기준가대비현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'sdpr_vrss_prpr_rate', 'name': '기준가대비현재가비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'cntg_vol', 'name': '체결거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === ETF 구성종목시세 ===
    'FHKST121600C0': {
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
                {'key': 'etf_cnfg_issu_avls', 'name': 'ETF구성종목시가총액', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'nav', 'name': 'NAV', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'nav_prdy_vrss_sign', 'name': 'NAV전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'nav_prdy_vrss', 'name': 'NAV전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'nav_prdy_ctrt', 'name': 'NAV전일대비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'etf_ntas_ttam', 'name': 'ETF순자산총액', 'type': 'string', 'required': True, 'length': 22, 'description': ''},
                {'key': 'prdy_clpr_nav', 'name': 'NAV전일종가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'oprc_nav', 'name': 'NAV시가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'hprc_nav', 'name': 'NAV고가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'lprc_nav', 'name': 'NAV저가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'etf_cu_unit_scrt_cnt', 'name': 'ETFCU단위증권수', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etf_cnfg_issu_cnt', 'name': 'ETF구성종목수', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'stck_shrn_iscd', 'name': '주식단축종목코드', 'type': 'string', 'required': True, 'length': 9, 'description': ''},
                {'key': 'hts_kor_isnm', 'name': 'HTS한글종목명', 'type': 'string', 'required': True, 'length': 40, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'tday_rsfl_rate', 'name': '당일등락비율', 'type': 'string', 'required': True, 'length': 52, 'description': ''},
                {'key': 'prdy_vrss_vol', 'name': '전일대비거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'tr_pbmn_tnrt', 'name': '거래대금회전율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'hts_avls', 'name': 'HTS시가총액', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etf_cnfg_issu_avls', 'name': 'ETF구성종목시가총액', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'etf_cnfg_issu_rlim', 'name': 'ETF구성종목비중', 'type': 'string', 'required': True, 'length': 72, 'description': ''},
                {'key': 'etf_vltn_amt', 'name': 'ETF구성종목내평가금액', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    },
    # === NAV 비교추이(종목) ===
    'FHPST02440000': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output1': {
            'type': 'object',
            'fields': [
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 2, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 4, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 12, 'description': ''},
                {'key': 'acml_tr_pbmn', 'name': '누적거래대금', 'type': 'string', 'required': True, 'length': 60, 'description': ''},
                {'key': 'stck_prdy_clpr', 'name': '주식전일종가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_oprc', 'name': '주식시가2', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_hgpr', 'name': '주식최고가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_lwpr', 'name': '주식최저가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_mxpr', 'name': '주식상한가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'stck_llam', 'name': '주식하한가', 'type': 'string', 'required': True, 'length': 10, 'description': ''}
            ]
        },
        'output2': {
            'type': 'object',
            'fields': [
                {'key': 'nav', 'name': 'NAV', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'nav_prdy_vrss_sign', 'name': 'NAV전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'nav_prdy_vrss', 'name': 'NAV전일대비', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'nav_prdy_ctrt', 'name': 'NAV전일대비율', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'prdy_clpr_nav', 'name': 'NAV전일종가', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'oprc_nav', 'name': 'NAV시가', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'hprc_nav', 'name': 'NAV고가', 'type': 'string', 'required': True, 'length': 11, 'description': ''},
                {'key': 'lprc_nav', 'name': 'NAV저가', 'type': 'string', 'required': True, 'length': 11, 'description': ''}
            ]
        }
    },
    # === NAV 비교추이(일) ===
    'FHPST02440200': {
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
                {'key': 'cntg_vol', 'name': '체결거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'dprt', 'name': '괴리율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nav_vrss_prpr', 'name': 'NAV대비현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'nav', 'name': 'NAV', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'nav_prdy_vrss_sign', 'name': 'NAV전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'nav_prdy_vrss', 'name': 'NAV전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'nav_prdy_ctrt', 'name': 'NAV전일대비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''}
            ]
        }
    },
    # === NAV 비교추이(분) ===
    'FHPST02440100': {
        'rt_cd': {'name': '성공실패여부', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
        'msg_cd': {'name': '응답코드', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
        'msg1': {'name': '응답메세지', 'type': 'string', 'required': True, 'length': 80, 'description': ''},
        'output': {
            'type': 'array',
            'fields': [
                {'key': 'bsop_hour', 'name': '영업시간', 'type': 'string', 'required': True, 'length': 6, 'description': ''},
                {'key': 'nav', 'name': 'NAV', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'nav_prdy_vrss_sign', 'name': 'NAV전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'nav_prdy_vrss', 'name': 'NAV전일대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'nav_prdy_ctrt', 'name': 'NAV전일대비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''},
                {'key': 'nav_vrss_prpr', 'name': 'NAV대비현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'dprt', 'name': '괴리율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'stck_prpr', 'name': '주식현재가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일대비부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'cntg_vol', 'name': '체결거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''}
            ]
        }
    }
}
