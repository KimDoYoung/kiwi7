# KIS REST API Request Definitions
# Auto-generated from Excel file

KIS_REQUEST_DEF_2 = {
    "FHPST01710000": {
        "url": "/uapi/domestic-stock/v1/quotations/volume-rank",
        "title": "거래량순위",
        "method": "GET",
        "tr_id": "FHPST01710000",
        "query": [
            {
                "key": "FID_COND_MRKT_DIV_CODE",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "J:KRX, NX:NXT"
            },
            {
                "key": "FID_COND_SCR_DIV_CODE",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "20171"
            },
            {
                "key": "FID_INPUT_ISCD",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000(전체) 기타(업종코드)"
            },
            {
                "key": "FID_DIV_CLS_CODE",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0(전체) 1(보통주) 2(우선주)"
            },
            {
                "key": "FID_BLNG_CLS_CODE",
                "name": "소속 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0 : 평균거래량 1:거래증가율 2:평균거래회전율 3:거래금액순 4:평균거래금액회전율"
            },
            {
                "key": "FID_TRGT_CLS_CODE",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "1 or 0 9자리 (차례대로 증거금 30% 40% 50% 60% 100% 신용보증금 30% 40% 50% 60%)\r ex) \"111111111\""
            },
            {
                "key": "FID_TRGT_EXLS_CLS_CODE",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "1 or 0 10자리 (차례대로 투자위험/경고/주의 관리종목 정리매매 불성실공시 우선주 거래정지 ETF ETN 신용주문불가 SPAC)\r ex) \"0000000000\""
            },
            {
                "key": "FID_INPUT_PRICE_1",
                "name": "입력 가격1",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "가격 ~\r ex) \"0\"\r \r 전체 가격 대상 조회 시 FID_INPUT_PRICE_1, FID_INPUT_PRICE_2 모두 \"\"(공란) 입력"
            },
            {
                "key": "FID_INPUT_PRICE_2",
                "name": "입력 가격2",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "~ 가격\r ex) \"1000000\"\r \r 전체 가격 대상 조회 시 FID_INPUT_PRICE_1, FID_INPUT_PRICE_2 모두 \"\"(공란) 입력"
            },
            {
                "key": "FID_VOL_CNT",
                "name": "거래량 수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "거래량 ~\r ex) \"100000\"\r \r 전체 거래량 대상 조회 시 FID_VOL_CNT \"\"(공란) 입력"
            },
            {
                "key": "FID_INPUT_DATE_1",
                "name": "입력 날짜1",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "\"\"(공란) 입력"
            }
        ]
    },
    "FHPST01700000": {
        "url": "/uapi/domestic-stock/v1/ranking/fluctuation",
        "title": "국내주식 등락률 순위",
        "method": "GET",
        "tr_id": "FHPST01700000",
        "query": [
            {
                "key": "fid_rsfl_rate2",
                "name": "등락 비율2",
                "type": "string",
                "required": True,
                "length": 132,
                "description": "공백 입력 시 전체 (~ 비율"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (J:KRX, NX:NXT)"
            },
            {
                "key": "fid_cond_scr_div_code",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key( 20170 )"
            },
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000(전체) 코스피(0001), 코스닥(1001), 코스피200(2001)"
            },
            {
                "key": "fid_rank_sort_cls_code",
                "name": "순위 정렬 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0:상승율순 1:하락율순 2:시가대비상승율 3:시가대비하락율 4:변동율"
            },
            {
                "key": "fid_input_cnt_1",
                "name": "입력 수1",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0:전체 , 누적일수 입력"
            },
            {
                "key": "fid_prc_cls_code",
                "name": "가격 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "'fid_rank_sort_cls_code :0 상승율 순일때 (0:저가대비, 1:종가대비)\r fid_rank_sort_cls_code :1 하락율 순일때 (0:고가대비, 1:종가대비)\r fid_rank_sort_cls_code : 기타 (0:전체)'"
            },
            {
                "key": "fid_input_price_1",
                "name": "입력 가격1",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "공백 입력 시 전체 (가격 ~)"
            },
            {
                "key": "fid_input_price_2",
                "name": "입력 가격2",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "공백 입력 시 전체 (~ 가격)"
            },
            {
                "key": "fid_vol_cnt",
                "name": "거래량 수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "공백 입력 시 전체 (거래량 ~)"
            },
            {
                "key": "fid_trgt_cls_code",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0:전체"
            },
            {
                "key": "fid_trgt_exls_cls_code",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0:전체"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0:전체"
            },
            {
                "key": "fid_rsfl_rate1",
                "name": "등락 비율1",
                "type": "string",
                "required": True,
                "length": 132,
                "description": "공백 입력 시 전체 (비율 ~)"
            }
        ]
    },
    "FHPST01720000": {
        "url": "/uapi/domestic-stock/v1/ranking/quote-balance",
        "title": "국내주식 호가잔량 순위",
        "method": "GET",
        "tr_id": "FHPST01720000",
        "query": [
            {
                "key": "fid_vol_cnt",
                "name": "거래량 수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (거래량 ~)"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (J:KRX, NX:NXT)"
            },
            {
                "key": "fid_cond_scr_div_code",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key( 20172 )"
            },
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000(전체) 코스피(0001), 코스닥(1001), 코스피200(2001)"
            },
            {
                "key": "fid_rank_sort_cls_code",
                "name": "순위 정렬 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0: 순매수잔량순, 1:순매도잔량순, 2:매수비율순, 3:매도비율순"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0:전체"
            },
            {
                "key": "fid_trgt_cls_code",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0:전체"
            },
            {
                "key": "fid_trgt_exls_cls_code",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0:전체"
            },
            {
                "key": "fid_input_price_1",
                "name": "입력 가격1",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (가격 ~)"
            },
            {
                "key": "fid_input_price_2",
                "name": "입력 가격2",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (~ 가격)"
            }
        ]
    },
    "FHPST01730000": {
        "url": "/uapi/domestic-stock/v1/ranking/profit-asset-index",
        "title": "국내주식 수익자산지표 순위",
        "method": "GET",
        "tr_id": "FHPST01730000",
        "query": [
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (J:KRX, NX:NXT)"
            },
            {
                "key": "fid_trgt_cls_code",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0:전체"
            },
            {
                "key": "fid_cond_scr_div_code",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key( 20173 )"
            },
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0:전체"
            },
            {
                "key": "fid_input_price_1",
                "name": "입력 가격1",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (가격 ~)"
            },
            {
                "key": "fid_input_price_2",
                "name": "입력 가격2",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (~ 가격)"
            },
            {
                "key": "fid_vol_cnt",
                "name": "거래량 수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (거래량 ~)"
            },
            {
                "key": "fid_input_option_1",
                "name": "입력 옵션1",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "회계연도 (2023)"
            },
            {
                "key": "fid_input_option_2",
                "name": "입력 옵션2",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "0: 1/4분기 , 1: 반기, 2: 3/4분기, 3: 결산"
            },
            {
                "key": "fid_rank_sort_cls_code",
                "name": "순위 정렬 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0:매출이익 1:영업이익 2:경상이익 3:당기순이익 4:자산총계 5:부채총계 6:자본총계"
            },
            {
                "key": "fid_blng_cls_code",
                "name": "소속 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0:전체"
            },
            {
                "key": "fid_trgt_exls_cls_code",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0:전체"
            }
        ]
    },
    "FHPST01740000": {
        "url": "/uapi/domestic-stock/v1/ranking/market-cap",
        "title": "국내주식 시가총액 상위",
        "method": "GET",
        "tr_id": "FHPST01740000",
        "query": [
            {
                "key": "fid_input_price_2",
                "name": "입력 가격2",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (~ 가격)"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (J:KRX, NX:NXT)"
            },
            {
                "key": "fid_cond_scr_div_code",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key( 20174 )"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0: 전체,  1:보통주,  2:우선주"
            },
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200"
            },
            {
                "key": "fid_trgt_cls_code",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0 : 전체"
            },
            {
                "key": "fid_trgt_exls_cls_code",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0 : 전체"
            },
            {
                "key": "fid_input_price_1",
                "name": "입력 가격1",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (가격 ~)"
            },
            {
                "key": "fid_vol_cnt",
                "name": "거래량 수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (거래량 ~)"
            }
        ]
    },
    "FHPST01750000": {
        "url": "/uapi/domestic-stock/v1/ranking/finance-ratio",
        "title": "국내주식 재무비율 순위",
        "method": "GET",
        "tr_id": "FHPST01750000",
        "query": [
            {
                "key": "fid_trgt_cls_code",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0 : 전체"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (J:KRX, NX:NXT)"
            },
            {
                "key": "fid_cond_scr_div_code",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key( 20175 )"
            },
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0 : 전체"
            },
            {
                "key": "fid_input_price_1",
                "name": "입력 가격1",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (가격 ~)"
            },
            {
                "key": "fid_input_price_2",
                "name": "입력 가격2",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (~ 가격)"
            },
            {
                "key": "fid_vol_cnt",
                "name": "거래량 수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (거래량 ~)"
            },
            {
                "key": "fid_input_option_1",
                "name": "입력 옵션1",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "회계년도 입력 (ex 2023)"
            },
            {
                "key": "fid_input_option_2",
                "name": "입력 옵션2",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "0: 1/4분기 , 1: 반기, 2: 3/4분기, 3: 결산"
            },
            {
                "key": "fid_rank_sort_cls_code",
                "name": "순위 정렬 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "7: 수익성 분석, 11 : 안정성 분석, 15: 성장성 분석, 20: 활동성 분석"
            },
            {
                "key": "fid_blng_cls_code",
                "name": "소속 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0"
            },
            {
                "key": "fid_trgt_exls_cls_code",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0 : 전체"
            }
        ]
    },
    "FHPST01760000": {
        "url": "/uapi/domestic-stock/v1/ranking/after-hour-balance",
        "title": "국내주식 시간외잔량 순위",
        "method": "GET",
        "tr_id": "FHPST01760000",
        "query": [
            {
                "key": "fid_input_price_1",
                "name": "입력 가격1",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (가격 ~)"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (주식 J)"
            },
            {
                "key": "fid_cond_scr_div_code",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key( 20176 )"
            },
            {
                "key": "fid_rank_sort_cls_code",
                "name": "순위 정렬 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "1: 장전 시간외, 2: 장후 시간외, 3:매도잔량, 4:매수잔량"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0 : 전체"
            },
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200"
            },
            {
                "key": "fid_trgt_exls_cls_code",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0 : 전체"
            },
            {
                "key": "fid_trgt_cls_code",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0 : 전체"
            },
            {
                "key": "fid_vol_cnt",
                "name": "거래량 수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (거래량 ~)"
            },
            {
                "key": "fid_input_price_2",
                "name": "입력 가격2",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (~ 가격)"
            }
        ]
    },
    "FHPST01780000": {
        "url": "/uapi/domestic-stock/v1/ranking/disparity",
        "title": "국내주식 이격도 순위",
        "method": "GET",
        "tr_id": "FHPST01780000",
        "query": [
            {
                "key": "fid_input_price_2",
                "name": "입력 가격2",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (~ 가격)"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (J:KRX, NX:NXT)"
            },
            {
                "key": "fid_cond_scr_div_code",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key( 20178 )"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0: 전체, 1:관리종목, 2:투자주의, 3:투자경고, 4:투자위험예고, 5:투자위험, 6:보톧주, 7:우선주"
            },
            {
                "key": "fid_rank_sort_cls_code",
                "name": "순위 정렬 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0: 이격도상위순, 1:이격도하위순"
            },
            {
                "key": "fid_hour_cls_code",
                "name": "시간 구분 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "5:이격도5, 10:이격도10, 20:이격도20, 60:이격도60, 120:이격도120"
            },
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200"
            },
            {
                "key": "fid_trgt_cls_code",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0 : 전체"
            },
            {
                "key": "fid_trgt_exls_cls_code",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0 : 전체"
            },
            {
                "key": "fid_input_price_1",
                "name": "입력 가격1",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (가격 ~)"
            },
            {
                "key": "fid_vol_cnt",
                "name": "거래량 수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (거래량 ~)"
            }
        ]
    },
    "FHPST01790000": {
        "url": "/uapi/domestic-stock/v1/ranking/market-value",
        "title": "국내주식 시장가치 순위",
        "method": "GET",
        "tr_id": "FHPST01790000",
        "query": [
            {
                "key": "fid_trgt_cls_code",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0 : 전체"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (J:KRX, NX:NXT)"
            },
            {
                "key": "fid_cond_scr_div_code",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key( 20179 )"
            },
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0: 전체, 1:관리종목, 2:투자주의, 3:투자경고, 4:투자위험예고, 5:투자위험, 6:보톧주, 7:우선주"
            },
            {
                "key": "fid_input_price_1",
                "name": "입력 가격1",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (가격 ~)"
            },
            {
                "key": "fid_input_price_2",
                "name": "입력 가격2",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (~ 가격)"
            },
            {
                "key": "fid_vol_cnt",
                "name": "거래량 수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (거래량 ~)"
            },
            {
                "key": "fid_input_option_1",
                "name": "입력 옵션1",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "회계연도 입력 (ex 2023)"
            },
            {
                "key": "fid_input_option_2",
                "name": "입력 옵션2",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "0: 1/4분기 , 1: 반기, 2: 3/4분기, 3: 결산"
            },
            {
                "key": "fid_rank_sort_cls_code",
                "name": "순위 정렬 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "'가치분석(23:PER, 24:PBR, 25:PCR, 26:PSR, 27: EPS, 28:EVA,\r 29: EBITDA, 30: EV/EBITDA, 31:EBITDA/금융비율'"
            },
            {
                "key": "fid_blng_cls_code",
                "name": "소속 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0 : 전체"
            },
            {
                "key": "fid_trgt_exls_cls_code",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0 : 전체"
            }
        ]
    },
    "FHPST01680000": {
        "url": "/uapi/domestic-stock/v1/ranking/volume-power",
        "title": "국내주식 체결강도 상위",
        "method": "GET",
        "tr_id": "FHPST01680000",
        "query": [
            {
                "key": "fid_trgt_exls_cls_code",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "0 : 전체"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (J:KRX, NX:NXT)"
            },
            {
                "key": "fid_cond_scr_div_code",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key( 20168 )"
            },
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0: 전체,  1: 보통주 2: 우선주"
            },
            {
                "key": "fid_input_price_1",
                "name": "입력 가격1",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (가격 ~)"
            },
            {
                "key": "fid_input_price_2",
                "name": "입력 가격2",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (~ 가격)"
            },
            {
                "key": "fid_vol_cnt",
                "name": "거래량 수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (거래량 ~)"
            },
            {
                "key": "fid_trgt_cls_code",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "0 : 전체"
            }
        ]
    },
    "FHPST01800000": {
        "url": "/uapi/domestic-stock/v1/ranking/top-interest-stock",
        "title": "국내주식 관심종목등록 상위",
        "method": "GET",
        "tr_id": "FHPST01800000",
        "query": [
            {
                "key": "fid_input_iscd_2",
                "name": "입력 필수값2",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "000000 : 필수입력값"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (J:KRX, NX:NXT)"
            },
            {
                "key": "fid_cond_scr_div_code",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key(20180)"
            },
            {
                "key": "fid_input_iscd",
                "name": "업종 코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200"
            },
            {
                "key": "fid_trgt_cls_code",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0 : 전체"
            },
            {
                "key": "fid_trgt_exls_cls_code",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0 : 전체"
            },
            {
                "key": "fid_input_price_1",
                "name": "입력 가격1",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "입력값 없을때 전체 (가격 ~)"
            },
            {
                "key": "fid_input_price_2",
                "name": "입력 가격2",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "입력값 없을때 전체 (~ 가격)"
            },
            {
                "key": "fid_vol_cnt",
                "name": "거래량 수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (거래량 ~)"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0: 전체 1: 관리종목 2: 투자주의 3: 투자경고 4: 투자위험예고 5: 투자위험 6: 보통주 7: 우선주"
            },
            {
                "key": "fid_input_cnt_1",
                "name": "순위 입력값",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "순위검색 입력값(1: 1위부터, 10:10위부터)"
            }
        ]
    },
    "FHPST01860000": {
        "url": "/uapi/domestic-stock/v1/ranking/traded-by-company",
        "title": "국내주식 당사매매종목 상위",
        "method": "GET",
        "tr_id": "FHPST01860000",
        "query": [
            {
                "key": "fid_trgt_exls_cls_code",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0: 전체"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (J:KRX, NX:NXT)"
            },
            {
                "key": "fid_cond_scr_div_code",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key(20186)"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0:전체, 1:관리종목, 2:투자주의, 3:투자경고, 4:투자위험예고, 5:투자위험, 6:보통주, 7:우선주"
            },
            {
                "key": "fid_rank_sort_cls_code",
                "name": "순위 정렬 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0:매도상위,1:매수상위"
            },
            {
                "key": "fid_input_date_1",
                "name": "입력 날짜1",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "기간~"
            },
            {
                "key": "fid_input_date_2",
                "name": "입력 날짜2",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "~기간"
            },
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200, 4001: KRX100"
            },
            {
                "key": "fid_trgt_cls_code",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0: 전체"
            },
            {
                "key": "fid_aply_rang_vol",
                "name": "적용 범위 거래량",
                "type": "string",
                "required": True,
                "length": 18,
                "description": "0: 전체, 100: 100주 이상"
            },
            {
                "key": "fid_aply_rang_prc_2",
                "name": "적용 범위 가격2",
                "type": "string",
                "required": True,
                "length": 18,
                "description": "~ 가격"
            },
            {
                "key": "fid_aply_rang_prc_1",
                "name": "적용 범위 가격1",
                "type": "string",
                "required": True,
                "length": 18,
                "description": "가격 ~"
            }
        ]
    },
    "HHKDB13470100": {
        "url": "/uapi/domestic-stock/v1/ranking/dividend-rate",
        "title": "국내주식 배당률 상위",
        "method": "GET",
        "tr_id": "HHKDB13470100",
        "query": [
            {
                "key": "CTS_AREA",
                "name": "CTS_AREA",
                "type": "string",
                "required": True,
                "length": 17,
                "description": "공백"
            },
            {
                "key": "GB1",
                "name": "KOSPI",
                "type": "string",
                "required": True,
                "length": 1,
                "description": "0:전체, 1:코스피,  2: 코스피200, 3: 코스닥,"
            },
            {
                "key": "UPJONG",
                "name": "업종구분",
                "type": "string",
                "required": True,
                "length": 4,
                "description": "'코스피(0001:종합, 0002:대형주.…0027:제조업 ), \r 코스닥(1001:종합, …. 1041:IT부품\r 코스피200 (2001:KOSPI200, 2007:KOSPI100, 2008:KOSPI50)'"
            },
            {
                "key": "GB2",
                "name": "종목선택",
                "type": "string",
                "required": True,
                "length": 1,
                "description": "0:전체, 6:보통주, 7:우선주"
            },
            {
                "key": "GB3",
                "name": "배당구분",
                "type": "string",
                "required": True,
                "length": 1,
                "description": "1:주식배당, 2: 현금배당"
            },
            {
                "key": "F_DT",
                "name": "기준일From",
                "type": "string",
                "required": True,
                "length": 8
            },
            {
                "key": "T_DT",
                "name": "기준일To",
                "type": "string",
                "required": True,
                "length": 8
            },
            {
                "key": "GB4",
                "name": "결산/중간배당",
                "type": "string",
                "required": True,
                "length": 1,
                "description": "0:전체, 1:결산배당, 2:중간배당"
            }
        ]
    },
    "FHKST190900C0": {
        "url": "/uapi/domestic-stock/v1/ranking/bulk-trans-num",
        "title": "국내주식 대량체결건수 상위",
        "method": "GET",
        "tr_id": "FHKST190900C0",
        "query": [
            {
                "key": "fid_aply_rang_prc_2",
                "name": "적용 범위 가격2",
                "type": "string",
                "required": True,
                "length": 18,
                "description": "~ 가격"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (J:KRX, NX:NXT)"
            },
            {
                "key": "fid_cond_scr_div_code",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key(11909)"
            },
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200, 4001: KRX100"
            },
            {
                "key": "fid_rank_sort_cls_code",
                "name": "순위 정렬 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0:매수상위, 1:매도상위"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0:전체"
            },
            {
                "key": "fid_input_price_1",
                "name": "입력 가격1",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "건별금액 ~"
            },
            {
                "key": "fid_aply_rang_prc_1",
                "name": "적용 범위 가격1",
                "type": "string",
                "required": True,
                "length": 18,
                "description": "가격 ~"
            },
            {
                "key": "fid_input_iscd_2",
                "name": "입력 종목코드2",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "공백:전체종목, 개별종목 조회시 종목코드 (000660)"
            },
            {
                "key": "fid_trgt_exls_cls_code",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0:전체"
            },
            {
                "key": "fid_trgt_cls_code",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "0:전체"
            },
            {
                "key": "fid_vol_cnt",
                "name": " 거래량 수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "거래량 ~"
            }
        ]
    },
    "FHKST17010000": {
        "url": "/uapi/domestic-stock/v1/ranking/credit-balance",
        "title": "국내주식 신용잔고 상위",
        "method": "GET",
        "tr_id": "FHKST17010000",
        "query": [
            {
                "key": "FID_COND_SCR_DIV_CODE",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key(11701)"
            },
            {
                "key": "FID_INPUT_ISCD",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200,"
            },
            {
                "key": "FID_OPTION",
                "name": "증가율기간",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "2~999"
            },
            {
                "key": "FID_COND_MRKT_DIV_CODE",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (주식 J)"
            },
            {
                "key": "FID_RANK_SORT_CLS_CODE",
                "name": "순위 정렬 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "'(융자)0:잔고비율 상위, 1: 잔고수량 상위, 2: 잔고금액 상위, 3: 잔고비율 증가상위, 4: 잔고비율 감소상위 \r (대주)5:잔고비율 상위, 6: 잔고수량 상위, 7: 잔고금액 상위, 8: 잔고비율 증가상위, 9: 잔고비율 감소상위 '"
            }
        ]
    },
    "FHPST04820000": {
        "url": "/uapi/domestic-stock/v1/ranking/short-sale",
        "title": "국내주식 공매도 상위종목",
        "method": "GET",
        "tr_id": "FHPST04820000",
        "query": [
            {
                "key": "FID_APLY_RANG_VOL",
                "name": "FID 적용 범위 거래량",
                "type": "string",
                "required": True,
                "length": 18,
                "description": "공백"
            },
            {
                "key": "FID_COND_MRKT_DIV_CODE",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (주식 J)"
            },
            {
                "key": "FID_COND_SCR_DIV_CODE",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key(20482)"
            },
            {
                "key": "FID_INPUT_ISCD",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000:전체, 0001:코스피, 1001:코스닥, 2001:코스피200, 4001: KRX100, 3003: 코스닥150"
            },
            {
                "key": "FID_PERIOD_DIV_CODE",
                "name": "조회구분 (일/월)",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "조회구분 (일/월) D: 일, M:월"
            },
            {
                "key": "FID_INPUT_CNT_1",
                "name": "조회가간(일수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "'조회가간(일수):\r 조회구분(D) 0:1일, 1:2일, 2:3일, 3:4일, 4:1주일, 9:2주일, 14:3주일, \r 조회구분(M) 1:1개월,  2:2개월, 3:3개월'"
            },
            {
                "key": "FID_TRGT_EXLS_CLS_CODE",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "공백"
            },
            {
                "key": "FID_TRGT_CLS_CODE",
                "name": "FID 대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "공백"
            },
            {
                "key": "FID_APLY_RANG_PRC_1",
                "name": "FID 적용 범위 가격1",
                "type": "string",
                "required": True,
                "length": 18,
                "description": "가격 ~"
            },
            {
                "key": "FID_APLY_RANG_PRC_2",
                "name": "FID 적용 범위 가격2",
                "type": "string",
                "required": True,
                "length": 18,
                "description": "~ 가격"
            }
        ]
    },
    "FHPST02340000": {
        "url": "/uapi/domestic-stock/v1/ranking/overtime-fluctuation",
        "title": "국내주식 시간외등락율순위",
        "method": "GET",
        "tr_id": "FHPST02340000",
        "query": [
            {
                "key": "FID_COND_MRKT_DIV_CODE",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (J: 주식)"
            },
            {
                "key": "FID_MRKT_CLS_CODE",
                "name": "시장 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "공백 입력"
            },
            {
                "key": "FID_COND_SCR_DIV_CODE",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key(20234)"
            },
            {
                "key": "FID_INPUT_ISCD",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000(전체), 0001(코스피), 1001(코스닥)"
            },
            {
                "key": "FID_DIV_CLS_CODE",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "1(상한가), 2(상승률), 3(보합),4(하한가),5(하락률)"
            },
            {
                "key": "FID_INPUT_PRICE_1",
                "name": "입력 가격1",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (가격 ~)"
            },
            {
                "key": "FID_INPUT_PRICE_2",
                "name": "입력 가격2",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (~ 가격)"
            },
            {
                "key": "FID_VOL_CNT",
                "name": "거래량 수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "입력값 없을때 전체 (거래량 ~)"
            },
            {
                "key": "FID_TRGT_CLS_CODE",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "공백 입력"
            },
            {
                "key": "FID_TRGT_EXLS_CLS_CODE",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "공백 입력"
            }
        ]
    },
    "FHPST02350000": {
        "url": "/uapi/domestic-stock/v1/ranking/overtime-volume",
        "title": "국내주식 시간외거래량순위",
        "method": "GET",
        "tr_id": "FHPST02350000",
        "query": [
            {
                "key": "FID_COND_MRKT_DIV_CODE",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (J: 주식)"
            },
            {
                "key": "FID_COND_SCR_DIV_CODE",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key(20235)"
            },
            {
                "key": "FID_INPUT_ISCD",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "0000(전체), 0001(코스피), 1001(코스닥)"
            },
            {
                "key": "FID_RANK_SORT_CLS_CODE",
                "name": "순위 정렬 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0(매수잔량),  1(매도잔량), 2(거래량)"
            },
            {
                "key": "FID_INPUT_PRICE_1",
                "name": "입력 가격1",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "가격 ~"
            },
            {
                "key": "FID_INPUT_PRICE_2",
                "name": "입력 가격2",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "~ 가격"
            },
            {
                "key": "FID_VOL_CNT",
                "name": "거래량 수",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "거래량 ~"
            },
            {
                "key": "FID_TRGT_CLS_CODE",
                "name": "대상 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "공백"
            },
            {
                "key": "FID_TRGT_EXLS_CLS_CODE",
                "name": "대상 제외 구분 코드",
                "type": "string",
                "required": True,
                "length": 32,
                "description": "공백"
            }
        ]
    },
    "HHMCM000100C0": {
        "url": "/uapi/domestic-stock/v1/ranking/hts-top-view",
        "title": "HTS조회상위20종목",
        "method": "GET",
        "tr_id": "HHMCM000100C0"
    }
}