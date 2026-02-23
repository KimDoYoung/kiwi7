# jwtmiddleware.py
"""
모듈 설명:
    -  JWT 토큰을 검증하는 미들웨어
주요 기능:
    -  header에서 토큰 추출 확인
    -  cookie에서 토큰 확인

작성자: 김도영
작성일: 2024-07-19
버전: 1.0
"""

from fastapi import HTTPException, Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

from backend.core.config import config
from backend.core.security import verify_token


class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        root = request.scope.get('root_path', '')

        # 토큰이 필요 없는 URL 경로 정의
        STATIC_PATHS = ['/public', '/favicon.ico']

        # root_path를 제거한 실제 경로로 비교
        path = request.url.path
        if path.startswith(root):
            path = path[len(root) :]

        if path in ['/login', '/logout'] or any(path.startswith(p) for p in STATIC_PATHS):
            response = await call_next(request)
            return response

        # Authorization 헤더에서 토큰 추출
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[len('Bearer ') :]
        else:
            cookie_name = config.ACCESS_TOKEN_NAME
            token = request.cookies.get(cookie_name)

        try:
            if token:
                verify_token(token)
                response = await call_next(request)
            else:
                return RedirectResponse(url=f'{root}/login')
        except HTTPException:
            return RedirectResponse(url=f'{root}/login')

        return response
