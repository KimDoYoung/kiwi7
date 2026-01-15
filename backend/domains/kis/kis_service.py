"""
KIS(한국투자증권) 서비스
API 인스턴스 및 토큰 매니저의 싱글톤 관리
"""
from typing import Optional

from backend.domains.kis.kis_rest_api import KisRestApi
from backend.domains.kis.managers.kis_token_manager import KisTokenManager

# 싱글톤 인스턴스
kis_api_instance: Optional[KisRestApi] = None
token_manager_instance: Optional[KisTokenManager] = None


async def get_kis_api() -> KisRestApi:
    """KIS API 인스턴스 반환"""
    token_manager = await get_kis_token_manager()
    return KisRestApi(token_manager=token_manager)


async def get_kis_token_manager() -> KisTokenManager:
    """KIS 토큰 매니저 싱글톤 인스턴스 반환"""
    global token_manager_instance

    if token_manager_instance is None:
        token_manager_instance = KisTokenManager()
        await token_manager_instance.refresh_token()
    else:
        await token_manager_instance.refresh_token()

    return token_manager_instance


def reset_kis_instances():
    """인스턴스 초기화 (테스트용)"""
    global kis_api_instance, token_manager_instance
    kis_api_instance = None
    token_manager_instance = None
