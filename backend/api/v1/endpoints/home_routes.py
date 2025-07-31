
# home_routes.py
"""
모듈 설명: 
    - /main, /page, /template, /login, /logout, /login 엔드포인트를 정의한다.
    - /main: 메인 페이지
    - /page: path에 해당하는 페이지를 가져와서 보낸다.
    - /template: path에 해당하는 html에서 body추출해서 jinja2처리한 JSON을 리턴
    - /login: 로그인 페이지
    - /logout: 로그아웃 페이지
    - /login: 로그인 프로세스

작성자: 김도영
작성일: 2025-07-21
버전: 1.0
"""

from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, Form, HTTPException, Query, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse

from backend.core import config
from backend.domains.user.user_model import AccessToken
from backend.domains.user.user_service import UserService
from backend.utils.kiwi_utils import get_today
from backend.core.template_engine import render_template
from backend.core.security import create_jwt_access_token, get_current_user

from backend.core.logger import get_logger
from backend.domains.kiwoom.page_contexts.context_registry import PAGE_CONTEXT_PROVIDERS

logger = get_logger(__name__)

router = APIRouter()

def get_user_service():
    return UserService()  # 매번 새로운 인스턴스를 생성하거나, 싱글톤 사용

@router.get("/", response_class=HTMLResponse, include_in_schema=False)
def display_root(request: Request):
    ''' 메인 '''
    return RedirectResponse(url="/main")


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
                "stk_code": stk_code,
                "data": {
                    "title": "주식매매"
                }
    }    
    return render_template("main.html", context)

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

    func = PAGE_CONTEXT_PROVIDERS.get(path.strip('/'))
    if func:
        try:
            data = await func(user_id) if callable(func) and func.__code__.co_flags & 0x80 else func()
            context["data"] = data
        except Exception as e:
            logger.error(f"{path}용 데이터 로딩 실패: {e}")
    else:
        data = {"title":"주식매매"}
        context["data"] = data
    template_page = f"template/{path.lstrip('/')}.html"
    logger.debug(f"template_page 호출됨: {template_page}")
    return render_template(template_page, context)    


@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    ''' 로그인 페이지 '''
    return render_template("login.html", {"request": request})

@router.get("/logout", response_class=JSONResponse)
async def logout(response: Response):
    ''' 로그아웃 페이지 '''
    response = RedirectResponse(url="/login", status_code=302)
    response.delete_cookie(
        key=config.ACCESS_TOKEN_NAME,
        path="/",              # ✅ set_cookie와 동일하게!
        secure=False,          # ✅ set_cookie와 동일하게!
        httponly=True,         # optional (FastAPI 기본값은 True)
        samesite="lax"         # ✅ 동일하게
    )
    return response    

@router.post("/login", response_model=AccessToken)
async def login_for_access_token(
    response: Response,  # Response 추가
    userId: str = Form(...),
    password: str = Form(...),
    user_service: UserService = Depends(get_user_service)
):
    ''' SQLite 기반 로그인 처리 '''
    saved_user_id = await user_service.get("user_id")
    saved_password = await user_service.get("user_pw")

    if not saved_user_id or not saved_password:
        raise HTTPException(status_code=400, detail="사용자 정보가 DB에 등록되어 있지 않습니다.")

    if userId != saved_user_id.value or password != saved_password.value:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="아이디 또는 비밀번호가 틀립니다.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    EXPIRE_MINUTES = int(config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token_expires = timedelta(minutes=EXPIRE_MINUTES)
    jwt_token_data = {
        "user_id": userId,
        "password": password,
        "login_time": datetime.now().isoformat(),
        "exp": datetime.now() + access_token_expires
    }
    jwt_token = create_jwt_access_token(
        data=jwt_token_data,
        expires_delta=access_token_expires
    )
    # 쿠키에 토큰 설정 (자동)
    response.set_cookie(
        key=config.ACCESS_TOKEN_NAME,
        value=jwt_token,
        max_age=EXPIRE_MINUTES * 60,  # 초 단위
        httponly=True,  # JavaScript에서 접근 불가 (보안)
        secure=False,   # HTTPS에서만 전송 (개발시 False)
        samesite="lax"  # CSRF 보호
    )    
    return AccessToken(
        access_token=jwt_token,
        token_type="bearer",
        user_id =userId
    )
