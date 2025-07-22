
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

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi import status
from datetime import timedelta, datetime

from backend.domains.user.user_model import AccessToken
from backend.domains.user.user_service import UserService
from backend.utils.kiwi_utils import get_today
from backend.core.template_engine import render_template
from backend.core.config import config
from backend.core.security import create_access_token, get_current_user

from backend.core.logger import get_logger

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
    current_user = await get_current_user(request)
    if not current_user:
        raise HTTPException(status_code=401, detail="Invalid token-현재 사용자 정보가 없습니다")
    
    logger.debug("***************Calling get_today() function for /main endpoint")
    today_str = get_today()
    logger.debug(f"****************today_str in /main: {today_str}")
    stk_code = request.cookies.get("stk_code")
    context = { "request": request,  
                "page_path": '/main',
                "user_id":  current_user["user_id"], 
                "user_name": current_user["user_name"], 
                "today": today_str,
                "stk_code": stk_code}    
    return render_template("main.html", context)

@router.get("/page", response_class=HTMLResponse, include_in_schema=False)
async def page(
    request: Request, 
    path: str = Query(..., description="template폴더안의 html path"),
    stk_code: str = Query(None, description="선택적 주식 코드")
):
    ''' path에 해당하는 페이지를 가져와서 보낸다. '''
    current_user = await get_current_user(request)
    
    if not current_user:
        raise HTTPException(status_code=401, detail="Invalid token-현재 사용자 정보가 없습니다")
    
    # 쿠키에서 stk_code를 가져오거나, 쿼리 파라미터로 전달된 stk_code를 사용
    cookie_stk_code = request.cookies.get("stk_code")
    stk_code = stk_code or cookie_stk_code    
    
    today = get_today()
    context = {
        "request": request, 
        "today" : today,
        "page_path": path, 
        "user_id": current_user["user_id"], 
        "user_name": current_user["user_name"],
        "stk_code" : stk_code
    }
    # id = ipo_calendar 와 같은 형식이고 이를 분리한다.
    template_path = path.lstrip('/') 
    template_page = f"template/{template_path}.html"
    logger.debug(f"template_page 호출됨: {template_page}")
    return render_template(template_page, context)    

@router.get("/template", response_class=JSONResponse, include_in_schema=False)
async def handlebar_template(request: Request, path: str = Query(..., description="handlebar-template path")):
    ''' path에 해당하는 html에서 body추출해서 jinja2처리한 JSON을 리턴 '''
    today = get_today()
    context = {
        "request": request, 
        "today" : today
    }
    # '/'로 시작하면 '/' 제거
    if path.startswith('/'):
        path = path.lstrip('/')
    
    # ".html"로 끝나면 ".html" 제거
    path = path.removesuffix('.html')
    
    handlebar_html_filename =  f"handlebar/{path}.html"

    handlebar_html =  render_template(handlebar_html_filename, context)
    data = {
        "template": handlebar_html
    }
    return JSONResponse(content=data)

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    ''' 로그인 페이지 '''
    return render_template("login.html", {"request": request})

@router.get("/logout", response_class=JSONResponse)
async def logout(response: Response):
    ''' 로그아웃 페이지 '''
    response.delete_cookie(config.ACCESS_TOKEN_NAME)
    response = RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    return response

@router.post("/login", response_model=AccessToken)
async def login_for_access_token(
    userId: str = Form(...),
    password: str = Form(...),
    user_service: UserService = Depends(get_user_service)
):
    ''' SQLite 기반 로그인 처리 '''
    saved_user_id = user_service.get("user_id")
    saved_password = user_service.get("password")

    if not saved_user_id or not saved_password:
        raise HTTPException(status_code=400, detail="사용자 정보가 DB에 등록되어 있지 않습니다.")

    if userId != saved_user_id.value or password != saved_password.value:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="아이디 또는 비밀번호가 틀립니다.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    EXPIRE_MINUTES = config.ACCESS_TOKEN_EXPIRE_MINUTES
    access_token_expires = timedelta(minutes=EXPIRE_MINUTES)
    jwt_token_data = {
        "user_id": userId,
        "password": password,
        "login_time": datetime.now().isoformat(),
        "exp": datetime.now() + access_token_expires
    }
    access_token = create_access_token(
        data=jwt_token_data,
        expires_delta=access_token_expires
    )
    return AccessToken(
        access_token=access_token,
        token_type="bearer",
        user_id =userId
    )
