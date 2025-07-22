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