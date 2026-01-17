# 프롬프트 prompts

## 개요

- 프로젝트에 사용한 프롬프트를 모아둔다.

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
