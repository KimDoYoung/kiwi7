"""
LS증권 서비스
API 인스턴스 및 토큰 매니저의 싱글톤 관리
"""
from typing import Optional

from backend.domains.stkcompanys.ls.ls_rest_api import LsRestApi
from backend.domains.stkcompanys.ls.managers.ls_token_manager import LsTokenManager

# 싱글톤 인스턴스
ls_api_instance: Optional[LsRestApi] = None
token_manager_instance: Optional[LsTokenManager] = None


async def get_ls_api() -> LsRestApi:
    """LS API 인스턴스 반환"""
    token_manager = await get_ls_token_manager()
    return LsRestApi(token_manager=token_manager)


async def get_ls_token_manager() -> LsTokenManager:
    """LS 토큰 매니저 싱글톤 인스턴스 반환"""
    global token_manager_instance

    if token_manager_instance is None:
        token_manager_instance = LsTokenManager()
        await token_manager_instance.refresh_token()
    else:
        await token_manager_instance.refresh_token()

    return token_manager_instance


def reset_ls_instances():
    """인스턴스 초기화 (테스트용)"""
    global ls_api_instance, token_manager_instance
    ls_api_instance = None
    token_manager_instance = None
