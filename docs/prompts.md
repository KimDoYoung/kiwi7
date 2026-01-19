# 프롬프트 prompts

## 개요

- 프로젝트에 사용한 프롬프트를 모아둔다.

## kis resp의 수정

- tools/kis_request_definition.py을 수정한다.
- 주어진 xls에서 1번째 sheet에서 작업할 대상 tr_cd 목록을 구한다.
- 두번째 sheet부터 `Response Body` 를 읽어서 json 데이터를 만든다.
- json data
  ```json
     'FHPST02440000': {
        'rt_cd' : { }
        'output1': {
            'fields': [{'description': '', 'key': 'stck_prpr', 'length': 8, 'name': '주식 현재가', 'required': True, 'type': 'string'}, {'description': '', 'key': 'prdy_vrss', 'length': 8, 'name': '전일 대비', 'required': True, 'type': 'string'}, {'description': '', 'key': 'prdy_vrss_sign', 'length': 2, 'name': '전일 대비 부호', 'required': True, 'type': 'string'}, {'description': '', 'key': 'prdy_ctrt', 'length': 4, 'name': '전일 대비율', 'required': True, 'type': 'string'}, {'description': '', 'key': 'acml_vol', 'length': 12, 'name': '누적 거래량', 'required': True, 'type': 'string'}, {'description': '', 'key': 'acml_tr_pbmn', 'length': 60, 'name': '누적 거래 대금', 'required': True, 'type': 'string'}, {'description': '', 'key': 'stck_prdy_clpr', 'length': 10, 'name': '주식 전일 종가', 'required': True, 'type': 'string'}, {'description': '', 'key': 'stck_oprc', 'length': 10, 'name': '주식 시가2', 'required': True, 'type': 'string'}, {'description': '', 'key': 'stck_hgpr', 'length': 10, 'name': '주식 최고가', 'required': True, 'type': 'string'}, {'description': '', 'key': 'stck_lwpr', 'length': 10, 'name': '주식 최저가', 'required': True, 'type': 'string'}, {'description': '', 'key': 'stck_mxpr', 'length': 10, 'name': '주식 상한가', 'required': True, 'type': 'string'}, {'description': '', 'key': 'stck_llam', 'length': 10, 'name': '주식 하한가', 'required': True, 'type': 'string'}],
            'type': 'object'
        },
        'output2': {
            'fields': [{'description': '', 'key': 'nav', 'length': 11, 'name': 'NAV', 'required': True, 'type': 'string'}, {'description': '', 'key': 'nav_prdy_vrss_sign', 'length': 1, 'name': 'NAV 전일 대비 부호', 'required': True, 'type': 'string'}, {'description': '', 'key': 'nav_prdy_vrss', 'length': 11, 'name': 'NAV 전일 대비', 'required': True, 'type': 'string'}, {'description': '', 'key': 'nav_prdy_ctrt', 'length': 8, 'name': 'NAV 전일 대비율', 'required': True, 'type': 'string'}, {'description': '', 'key': 'prdy_clpr_nav', 'length': 11, 'name': 'NAV전일종가', 'required': True, 'type': 'string'}, {'description': '', 'key': 'oprc_nav', 'length': 11, 'name': 'NAV시가', 'required': True, 'type': 'string'}, {'description': '', 'key': 'hprc_nav', 'length': 11, 'name': 'NAV고가', 'required': True, 'type': 'string'}, {'description': '', 'key': 'lprc_nav', 'length': 11, 'name': 'NAV저가', 'required': True, 'type': 'string'}],
            'type': 'object'
        }
    },
  ```

## kis req/response defintion

- kis 에서 받은 excel파일들을 소스로해서 @kis_request_definition.py와 @kis_response_definition.py를 만들때 사용
- code_example/extract_kis_req_def.py 작성
- code_example/extract_kis_resp_def.py 작성
- req용 프롬프트

```text
1. extract_kis_req_def.py을 작성할 것
2. 인자로 excel파일명을 입력받도록 할 것
3. excel 파일을 해석해서 아래 소스와 같은 결과를 출력할 것
KIS_REQUEST_DEF = {
    # === 주식 현재가 조회 ===
    'FHKST01010100': {
        'url': '/uapi/domestic-stock/v1/quotations/inquire-price',
        'title': '주식현재가 시세',
        'method': 'GET',
        'tr_id': 'FHKST01010100',
        'body': [
            {'key': 'FID_COND_MRKT_DIV_CODE', 'name': '시장분류코드', 'type': 'string', 'required': True, 'description': 'J:주식'},
            {'key': 'FID_INPUT_ISCD', 'name': '종목코드', 'type': 'string', 'required': True, 'length': 6},
        ]
    },
    ....
   }

```

- resp용 프롬프트

```text
1. extract_kis_resp_def.py을 작성할 것
2. 인자로 excel파일명을 입력받도록 할 것
3. excel 파일을 해석해서 아래 소스와 같은 결과를 출력할 것
KIS_RESPONSE_DEF = {
    # === 주식현재가 시세 ===
    'FHKST01010100': [
        {'key': 'iscd_stat_cls_code', 'name': '종목상태구분코드'},
        {'key': 'marg_rate', 'name': '증거금율'},
        {'key': 'rprs_mrkt_kor_name', 'name': '대표시장한글명'},
        {'key': 'bstp_kor_isnm', 'name': '업종한글명'},
        {'key': 'temp..
    ]
    ....
   }

```
