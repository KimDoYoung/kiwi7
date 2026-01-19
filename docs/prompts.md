# 프롬프트 prompts

## 개요

- 프로젝트에 사용한 프롬프트를 모아둔다.

## kis resp의 수정

- tools/kis_response_definition.py을 수정한다.
- 주어진 xls에서 1번째 sheet에서 작업할 대상 tr_cd 목록을 구한다.
- 두번째 sheet부터 `Response Body` 를 읽어서 json 데이터를 만든다.
- json data

  ```text
     'FHPST02440000': {
        'rt_cd' : { name:'결과코드', type: 'string', required: True, length : 1, description:''},
        'msg_cd' :{ name:'응답코드', type: 'string', required: True, length : 8, description:'' },
        'msg1' :{ name:'응답메세지', type: 'string', required: True, length : 80, description:'' },
         
        'output1': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식 영업 일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stck_clpr', 'name': '주식 종가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일 대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일 대비 부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일 대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적 거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'cntg_vol', 'name': '체결 거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'dprt', 'name': '괴리율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nav_vrss_prpr', 'name': 'NAV 대비 현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'nav', 'name': 'NAV', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'nav_prdy_vrss_sign', 'name': 'NAV 전일 대비 부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'nav_prdy_vrss', 'name': 'NAV 전일 대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'nav_prdy_ctrt', 'name': 'NAV 전일 대비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''}
            ]
        },
        'output2': {
            'type': 'array',
            'fields': [
                {'key': 'stck_bsop_date', 'name': '주식 영업 일자', 'type': 'string', 'required': True, 'length': 8, 'description': ''},
                {'key': 'stck_clpr', 'name': '주식 종가', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss', 'name': '전일 대비', 'type': 'string', 'required': True, 'length': 10, 'description': ''},
                {'key': 'prdy_vrss_sign', 'name': '전일 대비 부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'prdy_ctrt', 'name': '전일 대비율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'acml_vol', 'name': '누적 거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'cntg_vol', 'name': '체결 거래량', 'type': 'string', 'required': True, 'length': 18, 'description': ''},
                {'key': 'dprt', 'name': '괴리율', 'type': 'string', 'required': True, 'length': 82, 'description': ''},
                {'key': 'nav_vrss_prpr', 'name': 'NAV 대비 현재가', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'nav', 'name': 'NAV', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'nav_prdy_vrss_sign', 'name': 'NAV 전일 대비 부호', 'type': 'string', 'required': True, 'length': 1, 'description': ''},
                {'key': 'nav_prdy_vrss', 'name': 'NAV 전일 대비', 'type': 'string', 'required': True, 'length': 112, 'description': ''},
                {'key': 'nav_prdy_ctrt', 'name': 'NAV 전일 대비율', 'type': 'string', 'required': True, 'length': 84, 'description': ''}
            ]
        }
    },
  ```

- C:\Users\USER\Documents\kiwi7-api\kis\1.xlsx

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
