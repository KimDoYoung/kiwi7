---
applyTo: '**/*.py'
---

- 주석은 주로 한글로 작성되어야 합니다.
- 주석은 코드의 목적과 기능을 명확하게 설명해야 합니다.   

--
기술스택
--
- Python 3.12
- FastAPI
- SQLite
- uvicorn
- jinja2
- alpine.js
- bootstrap5

---
테이블 관련
---

* 테이블은 소문자로 작성하며, 단어 사이에 언더스코어(_)를 사용합니다.
* 테이블 이름은 명사형으로 작성합니다.
* 테이블은 일반적으로 복수형으로 작성합니다.
* model과 service 2개의 py를 작성합니다.
* 각 테이블에 대한 CRUD 기능을 제공하는 API 엔드포인트를 작성합니다.
* domains/stocks/ 경로에 파일을 생성합니다.
* model에는 주석을 포함하여 만든다.
```python

```
---
routes파일생성
---
* api/v1/endpoints/stk_cache_routes.py와 같이 각 테이블에 대한 라우팅 파일을 생성합니다.
