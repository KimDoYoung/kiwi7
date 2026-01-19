# KIS REST API Request Definitions
# Auto-generated from Excel file

KIS_REQUEST_DEF_6 = {
    "CTPF1604R": {
        "url": "/uapi/domestic-stock/v1/quotations/search-info",
        "title": "상품기본조회",
        "method": "GET",
        "tr_id": "CTPF1604R",
        "query": [
            {
                "key": "PDNO",
                "name": "상품번호",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "'주식(하이닉스) :  000660 (코드 : 300)\r 선물(101S12) :  KR4101SC0009 (코드 : 301)\r 미국(AAPL) : AAPL (코드 : 512)'"
            },
            {
                "key": "PRDT_TYPE_CD",
                "name": "상품유형코드",
                "type": "string",
                "required": True,
                "length": 3,
                "description": "'300 주식\r 301 선물옵션\r 302 채권\r 512  미국 나스닥 / 513  미국 뉴욕 / 529  미국 아멕스 \r 515  일본\r 501  홍콩 / 543  홍콩CNY / 558  홍콩USD\r 507  베트남 하노이 / 508  베트남 호치민\r 551  중국 상해A / 552  중국 심천A'"
            }
        ]
    },
    "CTPF1002R": {
        "url": "/uapi/domestic-stock/v1/quotations/search-stock-info",
        "title": "주식기본조회",
        "method": "GET",
        "tr_id": "CTPF1002R",
        "query": [
            {
                "key": "PRDT_TYPE_CD",
                "name": "상품유형코드",
                "type": "string",
                "required": True,
                "length": 3,
                "description": "300: 주식, ETF, ETN, ELW \r 301 : 선물옵션 \r 302 : 채권 \r 306 : ELS'"
            },
            {
                "key": "PDNO",
                "name": "상품번호",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "종목번호 (6자리)\r ETN의 경우, Q로 시작 (EX. Q500001)"
            }
        ]
    },
    "FHKST66430100": {
        "url": "/uapi/domestic-stock/v1/finance/balance-sheet",
        "title": "국내주식 대차대조표",
        "method": "GET",
        "tr_id": "FHKST66430100",
        "query": [
            {
                "key": "FID_DIV_CLS_CODE",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0: 년, 1: 분기"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "J"
            },
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "000660 : 종목코드"
            }
        ]
    },
    "FHKST66430200": {
        "url": "/uapi/domestic-stock/v1/finance/income-statement",
        "title": "국내주식 손익계산서",
        "method": "GET",
        "tr_id": "FHKST66430200",
        "query": [
            {
                "key": "FID_DIV_CLS_CODE",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0: 년, 1: 분기\r \r ※ 분기데이터는 연단위 누적합산"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "J"
            },
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "000660 : 종목코드"
            }
        ]
    },
    "FHKST66430300": {
        "url": "/uapi/domestic-stock/v1/finance/financial-ratio",
        "title": "국내주식 재무비율",
        "method": "GET",
        "tr_id": "FHKST66430300",
        "query": [
            {
                "key": "FID_DIV_CLS_CODE",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0: 년, 1: 분기"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "J"
            },
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "000660 : 종목코드"
            }
        ]
    },
    "FHKST66430400": {
        "url": "/uapi/domestic-stock/v1/finance/profit-ratio",
        "title": "국내주식 수익성비율",
        "method": "GET",
        "tr_id": "FHKST66430400",
        "query": [
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "000660 : 종목코드"
            },
            {
                "key": "FID_DIV_CLS_CODE",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0: 년, 1: 분기"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "J"
            }
        ]
    },
    "FHKST66430500": {
        "url": "/uapi/domestic-stock/v1/finance/other-major-ratios",
        "title": "국내주식 기타주요비율",
        "method": "GET",
        "tr_id": "FHKST66430500",
        "query": [
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "000660 : 종목코드"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0: 년, 1: 분기"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "J"
            }
        ]
    },
    "FHKST66430600": {
        "url": "/uapi/domestic-stock/v1/finance/stability-ratio",
        "title": "국내주식 안정성비율",
        "method": "GET",
        "tr_id": "FHKST66430600",
        "query": [
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "000660 : 종목코드"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0: 년, 1: 분기"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "J"
            }
        ]
    },
    "FHKST66430800": {
        "url": "/uapi/domestic-stock/v1/finance/growth-ratio",
        "title": "국내주식 성장성비율",
        "method": "GET",
        "tr_id": "FHKST66430800",
        "query": [
            {
                "key": "fid_input_iscd",
                "name": "입력 종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "ex : 000660"
            },
            {
                "key": "fid_div_cls_code",
                "name": "분류 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0: 년, 1: 분기"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (주식 J)"
            }
        ]
    },
    "FHPST04770000": {
        "url": "/uapi/domestic-stock/v1/quotations/credit-by-company",
        "title": "국내주식 당사 신용가능종목",
        "method": "GET",
        "tr_id": "FHPST04770000",
        "query": [
            {
                "key": "fid_rank_sort_cls_code",
                "name": "순위 정렬 구분 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "0:코드순, 1:이름순"
            },
            {
                "key": "fid_slct_yn",
                "name": "선택 여부",
                "type": "string",
                "required": True,
                "length": 1,
                "description": "0:신용주문가능, 1: 신용주문불가"
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
                "key": "fid_cond_scr_div_code",
                "name": "조건 화면 분류 코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "Unique key(20477)"
            },
            {
                "key": "fid_cond_mrkt_div_code",
                "name": "조건 시장 분류 코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "시장구분코드 (주식 J)"
            }
        ]
    },
    "HHKDB669102C0": {
        "url": "/uapi/domestic-stock/v1/ksdinfo/dividend",
        "title": "예탁원정보(배당일정)",
        "method": "GET",
        "tr_id": "HHKDB669102C0",
        "query": [
            {
                "key": "CTS",
                "name": "CTS",
                "type": "string",
                "required": True,
                "length": 17,
                "description": "공백"
            },
            {
                "key": "GB1",
                "name": "조회구분",
                "type": "string",
                "required": True,
                "length": 1,
                "description": "0:배당전체, 1:결산배당, 2:중간배당"
            },
            {
                "key": "F_DT",
                "name": "조회일자From",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "일자 ~"
            },
            {
                "key": "T_DT",
                "name": "조회일자To",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "~ 일자"
            },
            {
                "key": "SHT_CD",
                "name": "종목코드",
                "type": "string",
                "required": True,
                "length": 9,
                "description": "공백: 전체,  특정종목 조회시 : 종목코드"
            },
            {
                "key": "HIGH_GB",
                "name": "고배당여부",
                "type": "string",
                "required": True,
                "length": 1,
                "description": "공백"
            }
        ]
    },
    "HHKDB669103C0": {
        "url": "/uapi/domestic-stock/v1/ksdinfo/purreq",
        "title": "예탁원정보(주식매수청구일정)",
        "method": "GET",
        "tr_id": "HHKDB669103C0",
        "query": [
            {
                "key": "SHT_CD",
                "name": "종목코드",
                "type": "string",
                "required": True,
                "length": 9,
                "description": "공백: 전체,  특정종목 조회시 : 종목코드"
            },
            {
                "key": "T_DT",
                "name": "조회일자To",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "~ 일자"
            },
            {
                "key": "F_DT",
                "name": "조회일자From",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "일자 ~"
            },
            {
                "key": "CTS",
                "name": "CTS",
                "type": "string",
                "required": True,
                "length": 17,
                "description": "공백"
            }
        ]
    },
    "HHKDB669105C0": {
        "url": "/uapi/domestic-stock/v1/ksdinfo/rev-split",
        "title": "예탁원정보(액면교체일정)",
        "method": "GET",
        "tr_id": "HHKDB669105C0",
        "query": [
            {
                "key": "SHT_CD",
                "name": "종목코드",
                "type": "string",
                "required": True,
                "length": 9,
                "description": "공백: 전체,  특정종목 조회시 : 종목코드"
            },
            {
                "key": "CTS",
                "name": "CTS",
                "type": "string",
                "required": True,
                "length": 17,
                "description": "공백"
            },
            {
                "key": "F_DT",
                "name": "조회일자From",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "일자 ~"
            },
            {
                "key": "T_DT",
                "name": "조회일자To",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "~ 일자"
            },
            {
                "key": "MARKET_GB",
                "name": "시장구분",
                "type": "string",
                "required": True,
                "length": 1,
                "description": "0:전체, 1:코스피, 2:코스닥"
            }
        ]
    },
    "HHKDB669106C0": {
        "url": "/uapi/domestic-stock/v1/ksdinfo/cap-dcrs",
        "title": "예탁원정보(자본감소일정)",
        "method": "GET",
        "tr_id": "HHKDB669106C0",
        "query": [
            {
                "key": "CTS",
                "name": "CTS",
                "type": "string",
                "required": True,
                "length": 17,
                "description": "공백"
            },
            {
                "key": "F_DT",
                "name": "조회일자From",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "일자 ~"
            },
            {
                "key": "T_DT",
                "name": "조회일자To",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "~ 일자"
            },
            {
                "key": "SHT_CD",
                "name": "종목코드",
                "type": "string",
                "required": True,
                "length": 9,
                "description": "공백: 전체,  특정종목 조회시 : 종목코드"
            }
        ]
    },
    "HHKDB669107C0": {
        "url": "/uapi/domestic-stock/v1/ksdinfo/list-info",
        "title": "예탁원정보(상장정보일정)",
        "method": "GET",
        "tr_id": "HHKDB669107C0",
        "query": [
            {
                "key": "SHT_CD",
                "name": "종목코드",
                "type": "string",
                "required": True,
                "length": 9,
                "description": "공백: 전체,  특정종목 조회시 : 종목코드"
            },
            {
                "key": "T_DT",
                "name": "조회일자To",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "~ 일자"
            },
            {
                "key": "F_DT",
                "name": "조회일자From",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "일자 ~"
            },
            {
                "key": "CTS",
                "name": "CTS",
                "type": "string",
                "required": True,
                "length": 17,
                "description": "공백"
            }
        ]
    },
    "HHKDB669108C0": {
        "url": "/uapi/domestic-stock/v1/ksdinfo/pub-offer",
        "title": "예탁원정보(공모주청약일정)",
        "method": "GET",
        "tr_id": "HHKDB669108C0",
        "query": [
            {
                "key": "SHT_CD",
                "name": "종목코드",
                "type": "string",
                "required": True,
                "length": 9,
                "description": "공백: 전체,  특정종목 조회시 : 종목코드"
            },
            {
                "key": "CTS",
                "name": "CTS",
                "type": "string",
                "required": True,
                "length": 17,
                "description": "공백"
            },
            {
                "key": "F_DT",
                "name": "조회일자From",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "일자 ~"
            },
            {
                "key": "T_DT",
                "name": "조회일자To",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "~ 일자"
            }
        ]
    },
    "HHKDB669109C0": {
        "url": "/uapi/domestic-stock/v1/ksdinfo/forfeit",
        "title": "예탁원정보(실권주일정)",
        "method": "GET",
        "tr_id": "HHKDB669109C0",
        "query": [
            {
                "key": "SHT_CD",
                "name": "종목코드",
                "type": "string",
                "required": True,
                "length": 9,
                "description": "공백: 전체,  특정종목 조회시 : 종목코드"
            },
            {
                "key": "T_DT",
                "name": "조회일자To",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "~ 일자"
            },
            {
                "key": "F_DT",
                "name": "조회일자From",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "일자 ~"
            },
            {
                "key": "CTS",
                "name": "CTS",
                "type": "string",
                "required": True,
                "length": 17,
                "description": "공백"
            }
        ]
    },
    "HHKDB669110C0": {
        "url": "/uapi/domestic-stock/v1/ksdinfo/mand-deposit",
        "title": "예탁원정보(의무예치일정)",
        "method": "GET",
        "tr_id": "HHKDB669110C0",
        "query": [
            {
                "key": "T_DT",
                "name": "조회일자To",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "~ 일자"
            },
            {
                "key": "SHT_CD",
                "name": "종목코드",
                "type": "string",
                "required": True,
                "length": 9,
                "description": "공백: 전체,  특정종목 조회시 : 종목코드"
            },
            {
                "key": "F_DT",
                "name": "조회일자From",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "일자 ~"
            },
            {
                "key": "CTS",
                "name": "CTS",
                "type": "string",
                "required": True,
                "length": 17,
                "description": "공백"
            }
        ]
    },
    "HHKDB669100C0": {
        "url": "/uapi/domestic-stock/v1/ksdinfo/paidin-capin",
        "title": "예탁원정보(유상증자일정)",
        "method": "GET",
        "tr_id": "HHKDB669100C0",
        "query": [
            {
                "key": "CTS",
                "name": "CTS",
                "type": "string",
                "required": True,
                "length": 17,
                "description": "공백"
            },
            {
                "key": "GB1",
                "name": "조회구분",
                "type": "string",
                "required": True,
                "length": 1,
                "description": "1(청약일별), 2(기준일별)"
            },
            {
                "key": "F_DT",
                "name": "조회일자From",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "일자 ~"
            },
            {
                "key": "T_DT",
                "name": "조회일자To",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "~ 일자"
            },
            {
                "key": "SHT_CD",
                "name": "종목코드",
                "type": "string",
                "required": True,
                "length": 9,
                "description": "공백(전체),  특정종목 조회시(종목코드)"
            }
        ]
    },
    "HHKDB669101C0": {
        "url": "/uapi/domestic-stock/v1/ksdinfo/bonus-issue",
        "title": "예탁원정보(무상증자일정)",
        "method": "GET",
        "tr_id": "HHKDB669101C0",
        "query": [
            {
                "key": "CTS",
                "name": "CTS",
                "type": "string",
                "required": True,
                "length": 17,
                "description": "공백"
            },
            {
                "key": "F_DT",
                "name": "조회일자From",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "일자 ~"
            },
            {
                "key": "T_DT",
                "name": "조회일자To",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "~ 일자"
            },
            {
                "key": "SHT_CD",
                "name": "종목코드",
                "type": "string",
                "required": True,
                "length": 9,
                "description": "공백: 전체,  특정종목 조회시 : 종목코드"
            }
        ]
    },
    "HHKDB669111C0": {
        "url": "/uapi/domestic-stock/v1/ksdinfo/sharehld-meet",
        "title": "예탁원정보(주주총회일정)",
        "method": "GET",
        "tr_id": "HHKDB669111C0",
        "query": [
            {
                "key": "CTS",
                "name": "CTS",
                "type": "string",
                "required": True,
                "length": 17,
                "description": "공백"
            },
            {
                "key": "F_DT",
                "name": "조회일자From",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "일자 ~"
            },
            {
                "key": "T_DT",
                "name": "조회일자To",
                "type": "string",
                "required": True,
                "length": 8,
                "description": "~ 일자"
            },
            {
                "key": "SHT_CD",
                "name": "종목코드",
                "type": "string",
                "required": True,
                "length": 9,
                "description": "공백: 전체,  특정종목 조회시 : 종목코드"
            }
        ]
    },
    "HHKST668300C0": {
        "url": "/uapi/domestic-stock/v1/quotations/estimate-perform",
        "title": "국내주식 종목추정실적",
        "method": "GET",
        "tr_id": "HHKST668300C0",
        "query": [
            {
                "key": "SHT_CD",
                "name": "종목코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "ex) 265520"
            }
        ]
    },
    "CTSC2702R": {
        "url": "/uapi/domestic-stock/v1/quotations/lendable-by-company",
        "title": "당사 대주가능 종목",
        "method": "GET",
        "tr_id": "CTSC2702R",
        "query": [
            {
                "key": "EXCG_DVSN_CD",
                "name": "거래소구분코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "00(전체), 02(거래소), 03(코스닥)"
            },
            {
                "key": "PDNO",
                "name": "상품번호",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "공백 : 전체조회, 종목코드 입력 시 해당종목만 조회"
            },
            {
                "key": "THCO_STLN_PSBL_YN",
                "name": "당사대주가능여부",
                "type": "string",
                "required": True,
                "length": 1,
                "description": "Y"
            },
            {
                "key": "INQR_DVSN_1",
                "name": "조회구분1",
                "type": "string",
                "required": True,
                "length": 1,
                "description": "0 : 전체조회, 1: 종목코드순 정렬"
            },
            {
                "key": "CTX_AREA_FK200",
                "name": "연속조회검색조건200",
                "type": "string",
                "required": True,
                "length": 200,
                "description": "미입력 (다음조회 불가)"
            },
            {
                "key": "CTX_AREA_NK100",
                "name": "연속조회키100",
                "type": "string",
                "required": True,
                "length": 100,
                "description": "미입력 (다음조회 불가)"
            }
        ]
    },
    "FHKST663300C0": {
        "url": "/uapi/domestic-stock/v1/quotations/invest-opinion",
        "title": "국내주식 종목투자의견",
        "method": "GET",
        "tr_id": "FHKST663300C0",
        "query": [
            {
                "key": "FID_COND_MRKT_DIV_CODE",
                "name": "조건시장분류코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "J(시장 구분 코드)"
            },
            {
                "key": "FID_COND_SCR_DIV_CODE",
                "name": "조건화면분류코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "16633(Primary key)"
            },
            {
                "key": "FID_INPUT_ISCD",
                "name": "입력종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "종목코드(ex) 005930(삼성전자))"
            },
            {
                "key": "FID_INPUT_DATE_1",
                "name": "입력날짜1",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "이후 ~(ex) 0020231113)"
            },
            {
                "key": "FID_INPUT_DATE_2",
                "name": "입력날짜2",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "~ 이전(ex) 0020240513)"
            }
        ]
    },
    "FHKST663400C0": {
        "url": "/uapi/domestic-stock/v1/quotations/invest-opbysec",
        "title": "국내주식 증권사별 투자의견",
        "method": "GET",
        "tr_id": "FHKST663400C0",
        "query": [
            {
                "key": "FID_COND_MRKT_DIV_CODE",
                "name": "조건시장분류코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "J(시장 구분 코드)"
            },
            {
                "key": "FID_COND_SCR_DIV_CODE",
                "name": "조건화면분류코드",
                "type": "string",
                "required": True,
                "length": 5,
                "description": "16634(Primary key)"
            },
            {
                "key": "FID_INPUT_ISCD",
                "name": "입력종목코드",
                "type": "string",
                "required": True,
                "length": 12,
                "description": "회원사코드 (kis developers 포탈 사이트 포럼-> FAQ -> 종목정보 다운로드(국내) 참조)"
            },
            {
                "key": "FID_DIV_CLS_CODE",
                "name": "분류구분코드",
                "type": "string",
                "required": True,
                "length": 2,
                "description": "전체(0) 매수(1) 중립(2) 매도(3)"
            },
            {
                "key": "FID_INPUT_DATE_1",
                "name": "입력날짜1",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "이후 ~"
            },
            {
                "key": "FID_INPUT_DATE_2",
                "name": "입력날짜2",
                "type": "string",
                "required": True,
                "length": 10,
                "description": "~ 이전"
            }
        ]
    }
}