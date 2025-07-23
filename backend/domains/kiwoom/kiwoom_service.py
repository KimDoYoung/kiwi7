# kiwoom_service.py
"""
모듈 설명: 
    - KiwoomApi를 사용하기 위한 서비스 모듈
주요 기능:
    - KiwoomApi 인스턴스를 관리하고 제공하는 기능
    - api = get_kiwoom_api() 형태로 사용

작성자: 김도영
작성일: 2025-07-23
버전: 1.0
"""
from backend.domains.kiwoom.kiwoom_api import KiwoomStockApi  # Adjust the import path as needed

kiwoom_api_instance: KiwoomStockApi | None = None

async def get_kiwoom_api() -> KiwoomStockApi:
    global kiwoom_api_instance
    if kiwoom_api_instance is None:
        kiwoom_api_instance = KiwoomStockApi()
        await kiwoom_api_instance.refresh_token()
    else:
        await kiwoom_api_instance.refresh_token()
    return kiwoom_api_instance