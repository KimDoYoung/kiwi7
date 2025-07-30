# kiwi7-키움 Restful API를 이용한 주식매매

## 개요

- 키움증권의 Restful API를 이용해서 주식매매
- Web app으로 docker에 배포해서 local pc에서 사용하는 것을 메인으로 한다.
- python으로 개발 backend와 frontend로 나누어서 개발.


## 기술스택

- python 3.12
- backend 
  - fastapi
  - uvicorn
  - jinja 2.0
  - sqlite3
  - jwt
  - pydantic
  - dotenv
  - aiohttp 

- frontend
  - alpine.js
  - bootstrap5
  - html5

  
- deploy
  - docker

## 보안

* 쿠키
* client에서 보낼때 header의 bearer사용하지 않음.
* jwtmiddelware.py
* home_routes의 post login, get logout
  

## 참고 사이트

- [키움Restful API 홈](https://openapi.kiwoom.com/main/home)
- [**API문서**](https://openapi.kiwoom.com/guide/apiguide)

## 유틸리티
- code_samples 
- 키움api문서에서 제공하는 excel파일을 읽어서 request definition을 추출
```shell
python extract_kw_req_def.py.py c:\\tmp\\kwapi.xlsx > 1.txt
```