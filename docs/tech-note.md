# 기술문서

## login/logout

- 쿠키를 사용
- 로그인시 login.js
  ```javascript
    const response = await fetch('/login', {
        method: 'POST',
        body: formData
    });
  ```
- 로그인 서버측  home_routes.py
  ```python
    response.set_cookie(
        key=config.ACCESS_TOKEN_NAME,
        value=jwt_token,
        max_age=EXPIRE_MINUTES * 60,  # 초 단위
        httponly=True,  # JavaScript에서 접근 불가 (보안)
        secure=False,   # HTTPS에서만 전송 (개발시 False)
        samesite="lax"  # CSRF 보호
    ) 
  ```
- 로그아웃시 서버측에서 처리
  ```python
    response = RedirectResponse(url="/login", status_code=302)
    response.delete_cookie(
        key=config.ACCESS_TOKEN_NAME,
        path="/",              # ✅ set_cookie와 동일하게!
        secure=False,          # ✅ set_cookie와 동일하게!
        httponly=True,         # optional (FastAPI 기본값은 True)
        samesite="lax"         # ✅ 동일하게
    )
    return response  
  ```

  ## 페이지 랜더링 

1. client 에서 alpine.js 를 사용하고 있음.
2. server에서 jinja2를 사용하고 있음

```
@router.get("/main", response_class=HTMLResponse, include_in_schema=False)
async def display_main(request: Request):
    ''' 메인 '''
    user_id = await get_current_user(request)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token-현재 사용자 정보가 없습니다")
    
    logger.debug("***************Calling get_today() function for /main endpoint")
    today_str = get_today()
    logger.debug(f"****************today_str in /main: {today_str}")
    stk_code = request.cookies.get("stk_code")
    context = { "request": request,  
                "page_path": '/main',
                "user_id":  user_id, 
                "today": today_str,
                "stk_code": stk_code}    
    return render_template("main.html", context)
```

3. main.html
```
{% extends "common/base.html" %}

{% block content %}
    abc
{% endblock %}

{% block script %}
<script src="/public/js/main.js"></script>
{% endblock %}

</html>
```    
4. home_routes.py의 /page로 대부분의 html을 처리함.
```

@router.get("/page", response_class=HTMLResponse, include_in_schema=False)
async def page(
    request: Request, 
    path: str = Query(..., description="template폴더안의 html path"),
    stk_code: str = Query(None, description="선택적 주식 코드")
):
    ''' path에 해당하는 페이지를 가져와서 보낸다. '''
    user_id = await get_current_user(request)
    
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token-현재 사용자 정보가 없습니다")
    
    # 쿠키에서 stk_code를 가져오거나, 쿼리 파라미터로 전달된 stk_code를 사용
    cookie_stk_code = request.cookies.get("stk_code")
    stk_code = stk_code or cookie_stk_code    
    
    today = get_today()
    context = { "request": request,  
                "page_path": '/main',
                "user_id":  user_id, 
                "today": today,
                "stk_code": stk_code}      
    # id = ipo_calendar 와 같은 형식이고 이를 분리한다.
    template_path = path.lstrip('/') 
    template_page = f"template/{template_path}.html"
    logger.debug(f"template_page 호출됨: {template_page}")
    return render_template(template_page, context)    

```