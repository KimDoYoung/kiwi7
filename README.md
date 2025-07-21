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

- frontend
  - alpine.js
  - bootstrap5
  - html5

  
- deploy
  - docker

## 참고 사이트

- [키움Restful API 홈](https://openapi.kiwoom.com/main/home)
- [**API문서**](https://openapi.kiwoom.com/guide/apiguide)