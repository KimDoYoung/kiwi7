import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from core.logger import get_logger
from core.config import config
from core.jwtmiddleware import JWTAuthMiddleware
from api.v1.endpoints.user_routes import router as user_router
from api.v1.endpoints.home_routes import router as home_router

from core.exception_handler import add_exception_handlers


logger = get_logger(__name__)

def create_app() -> FastAPI:
    app = FastAPI(title="Kiwi7 - 주식매매(개인용)", version="0.1.1")
    add_middlewares(app)
    add_routes(app)
    add_event_handlers(app)
    add_static_files(app)
    add_exception_handlers(app)
    return app

def add_middlewares(app: FastAPI):
    ''' 미들웨어 설정 '''
    # CORS 설정
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )    
    # JWT 인증 미들웨어 등록
    app.add_middleware(JWTAuthMiddleware)



def add_routes(app: FastAPI):
    # API 라우터 포함
    app.include_router(home_router) # 화면
    app.include_router(user_router, prefix="/api/v1/user", tags=["user"])

def add_event_handlers(app: FastAPI):
    ''' 이벤트 핸들러 설정 '''
    app.add_event_handler("startup", startup_event)
    app.add_event_handler("shutdown", shutdown_event)

def add_static_files(app: FastAPI):
    ''' 정적 파일 설정 '''
    # static
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_files_path = os.path.join(BASE_DIR, 'frontend', 'public')
    app.mount("/public", StaticFiles(directory=static_files_path), name="public")

async def startup_event():
    ''' Kiwi7 application  시작 '''
    mongodb_url = config.DB_URL 
    db_name = config.DB_NAME
    logger.info(f"MongoDB 연결: {mongodb_url} / {db_name}")

async def shutdown_event():
    ''' Kiwi7 application 종료 '''
    logger.info('---------------------------------')
    logger.info('Shutdown 프로세스 시작')
    logger.info('---------------------------------')
    
    logger.info('---------------------------------')
    logger.info('Shutdown 프로세스 종료')
    logger.info('---------------------------------')

app = create_app()

if __name__ == "__main__":
    import uvicorn
    logger.info("Kiwi7 주식매매 웹서비스 시작")
    uvicorn.run(app, host="0.0.0.0", port=8000)
