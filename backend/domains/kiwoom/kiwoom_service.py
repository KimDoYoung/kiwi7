# kiwoom_service.py
"""
모듈 설명: 
    - KiwoomApi를 사용하기 위한 서비스 모듈
주요 기능:
    - KiwoomApi 인스턴스를 관리하고 제공하는 기능
    - KiwwomTokenManager의 인스턴스를 관리하고 제공하는 기능
    - api = await get_kiwoom_api()
    - token_manager= get_token_manager()

작성자: 김도영
작성일: 2025-07-23
버전: 1.0
"""
from backend.domains.kiwoom.kiwoom_rest_api import KiwoomRestApi
from backend.domains.kiwoom.managers.kiwoom_token_manager import KiwoomTokenManager  

kiwoom_api_instance: KiwoomRestApi | None = None
token_manager_instance: KiwoomTokenManager | None = None

async def get_kiwoom_api() -> KiwoomRestApi:
    token_manager = await get_token_manager()
    return KiwoomRestApi(token_manager=token_manager)

async def get_token_manager() -> KiwoomTokenManager:
    global token_manager_instance
    if token_manager_instance is None:
        token_manager_instance = KiwoomTokenManager()
        await token_manager_instance.refresh_token()
    else:
        await token_manager_instance.refresh_token()
    return token_manager_instance