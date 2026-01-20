# kiwi7-키움,KIS,LS 증권 Restful API를 이용한 주식매매

## 개요

- 원래 kiwi7은 키움증권의 계좌1개만을 대상으로 하려고 했는데. 이제 KIS(한국투자증권)과 LS증권의 계좌도 포함해서 나의 전체 증권계좌(현재3개)를 한 눈에 관리하고자 한다.
- Web app으로 docker에 배포해서 local pc에서 사용하는 것을 메인으로 한다.
- python으로 개발 backend와 frontend로 나누어서 개발.
- 기본 PORT 는 8002로 한다.

## 기술스택

- python 3.12
- uv 를 사용함
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

- 쿠키
- client에서 보낼때 header의 bearer사용하지 않음.
- jwtmiddelware.py
- home_routes의 post login, get logout
  
## 참고 사이트

### 키움

- [키움Restful API 홈](https://openapi.kiwoom.com/main/home)
- [**API문서**](https://openapi.kiwoom.com/guide/apiguide)

### KIS-한국투자증권

- [API 문서](https://apiportal.koreainvestment.com/apiservice-apiservice)

### LS-LS증권

- [API 문서](https://openapi.ls-sec.co.kr/apiservice?group_id=ffd2def7-a118-40f7-a0ab-cd4c6a538a90&api_id=33bd887a-6652-4209-88cd-5324bc7c5e36)

## 유틸리티

- code_samples
- 키움api문서에서 제공하는 excel파일을 읽어서 request definition을 추출

```shell
python extract_kw_req_def.py.py c:\\tmp\\kwapi.xlsx > 1.txt
```

## fedora에 설치

1. .env.docker 에서 folder 경로를 수정
2. sudo docker-compose up -d
3. 로그보기 : sudo docker logs -f kiwi7-app
