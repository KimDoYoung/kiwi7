---
applyTo: '**/*.py'
---

- 주석은 주로 한글로 작성되어야 합니다.
- 주석은 코드의 목적과 기능을 명확하게 설명해야 합니다.   
- logger.info(), logger.debug(), logger.error() 등을 사용하여 로그를 남기는데 한글을 주로 쓴다.
- 키움증권 REST API를 사용하여 주식매매를 하는 시스템으로서 문서를 코딩해 놓음, (API 확인시 필히 참조)
    * backend/domains/models/kiwoom_request_definition.py
    * backend/domains/models/kiwoom_response_definition.py
- 위 2가지 문서를 참조하여 키움증권 API를 호출하고 응답을 처리합니다.

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
전반적인 규칙
---
* html을 만들때 alpine.js를 사용합니다.
* bootstrap5를 사용하여 스타일링합니다.
* bootstrap5 icon을 사용합니다.
* ajax동작은 자체적으로 작성한 fetch_util.js를 사용합니다.
    * `fetchUtil.js`는 `GET`, `POST`, `PUT`, `DELETE` 요청을 위한 유틸리티 함수를 포함합니다.
    * kiwoom API와의 통신을 위한 함수도 포함됩니다.
    * 자체적인 KiwiError 클래스를 사용하여 에러 처리를 합니다. 
---
테이블 관련
---

* kiwi7이 실행될 때 sql/kiwi7_ddl.sql로 table들을 생성합니다.
* 각 테이블에 대한 model과 service가 domains/폴더 하위에 생성됩니다.
* 만약 새로운 테이블을 kiwi7_ddl.sql에 생성한다면 그 테이블에 대한 model과 service를 domains/폴더 하위에 생성해야 합니다.
* model의 생성은 pydantic을 사용합니다. 이때 주석을 ddl 을 참조하여 생성합니다.
* 모델의 예는 domains/stocks/my_stock_model.py를 참조합니다.
* service의 예는 domains/stocks/my_stock_service.py를 참조합니다.

---
새로운 메뉴의 생성
---
1. `http://localhost:8001/page?path=stock/find`과 같이 새로운 경로를 추가합니다.
2. /page는 home_routes에 포함되어 있습니다.
3. path가 stock/find라면 frontend/views/template 하위에 stock폴더 그 안에 find.html을 생성합니다.
4. path에 따라서 할당된 함수를 수행한다. 그 결과를 jinja2 템플릿에 전달하여 렌더링합니다.
5. path에 따라서 할당된 함수는 backend.page_contexts.context_registry에서 가져옵니다.
6. 랜더링된 후에는 alpine.js를 사용하여 동적인 기능을 추가합니다.

```python

@router.get("/page", response_class=HTMLResponse, include_in_schema=False)
async def page(
    request: Request, 
    path: str = Query(..., description="template폴더안의 html path")
):
    ''' path에 해당하는 페이지를 가져와서 보낸다. '''
    user_id = await get_current_user(request)
    
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token-현재 사용자 정보가 없습니다")
    
    # 추가적인 쿼리 파라미터를 딕셔너리로 변환
    extra_params = {k: v for k, v in request.query_params.items()}

    today = get_today()
    page_path = path.strip('/')

    context = { "request": request,  
                "user_id":  user_id,
                "version" : config.VERSION,
                "page_path": page_path,
                "today": today,
                **extra_params}

    func = PAGE_CONTEXT_PROVIDERS.get(page_path)
    if func:
        try:
            # 함수가 async인지 확인
            is_async = callable(func) and func.__code__.co_flags & 0x80
            
            # 함수가 매개변수를 받는지 확인
            func_params = func.__code__.co_argcount if callable(func) else 0
            
            if func_params > 0:
                # context를 매개변수로 전달
                data = await func(context) if is_async else func(context)
            else:
                # 매개변수가 없는 기존 함수 호환성 유지
                data = await func() if is_async else func()
                
            context["data"] = data            
        except Exception as e:
            logger.error(f"{path}용 데이터 로딩 실패: {e}")
    else:
        data = {"title":"주식매매"}
        context["data"] = data
    template_page = f"template/{page_path}.html"
    logger.debug(f"template_page 호출됨: {template_page}")
    return render_template(template_page, context)  
```

--- 
api 작성(router파일의 함수)
---
- table의 ddl은 sql/kiwi7_ddl.sql에 정의되어 있습니다.
- table 1개 당 1개의 model파일과 1개의 service파일이 domains/폴더 하위에 있습니다.
- 각 model과 service는 해당 table의 CRUD 기능을 수행합니다.
- get_<tablename>_service로 해당 테이블의 service를 가져옵니다.
- 키움증권의 api호출은 KiwoomRestApi 객체를  `kiwoom_api = await get_kiwoom_api()`  로 생성하고
- 아래와 같이 id와 payload를 전달하여 호출합니다.
```python
 response = await api.send_request(KiwoomRequest(api_id="ka10099", payload={"mrkt_tp": mrkt_tp}))
 ```
- api 호출은 request는 비동기적으로 처리됩니다.
- KiwoomApiHelper를 사용하여 응답을 처리합니다.
- route의 api 함수 코드 예시
```python
@router.put("/stk_info")
async def update_stk_info(force: bool = False):
    """stk_info 테이블 업데이트"""
    try:
        # stk_info_fill은 비동기 함수이므로 await 사용
        await stk_info_fill(force=force)
        service = get_service("settings")
        last_fill_time = await service.get(SettingsKey.LAST_STK_INFO_FILL)
        return KiwoomApiHelper.create_success_response(data={"last_stk_info_fill": last_fill_time})
    except Exception as e:
        logger.error(f"stk_info 테이블 업데이트 중 오류 발생: {str(e)}")
        # api_helpers의 create_error_response 사용 (메시지만 전달)
        return KiwoomApiHelper.create_error_response(
            error_code="STK_INFO_UPDATE_ERROR",
            error_message=f"stk_info 테이블 업데이트 중 오류가 발생했습니다: {str(e)}"
        )
```

---
Html의 작성
---
- html 파일은 frontend/views/template 하위에 생성합니다.
- html 파일은 jinja2 템플릿 엔진을 사용하여 작성합니다.
- html 파일은 bootstrap5를 사용하여 스타일링합니다.
- html 파일은 alpine.js를 사용하여 동적인 기능을 추가합니다.
- 아래 내용을 html파일의 template로 사용할 것
```html
{% extends 'common/base.html' %}
{% block style %}
{% endblock %}
{% block content %}
<div x-data="data_settings"  class="container mt-4">
</div>
{% raw %}
<!--handlebar scripts-->
{% endraw %}
{% endblock %}
{% block script %}
{% raw %}
<script>
// Alpine 컴포넌트 팩토리 함수
function createSettingsComponent() {
    return {
        // === 상태 변수 ===
        data: null,
    
        // === 초기화 ===
        init() {
            console.log('Initializing data_settings');
        },
	
    };
}

// Alpine.js 컴포넌트 등록
document.addEventListener('alpine:init', () => {
    Alpine.data('data_settings', createSettingsComponent);
});
</script>
{% endraw %}
{% endblock %}

```