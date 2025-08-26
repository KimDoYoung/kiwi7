from fastapi import APIRouter
from typing import List
from backend.core.logger import get_logger
from backend.domains.services.settings_service import get_settings_service
from backend.domains.models.settings_model import SettingInfo
from backend.api.common import (
    handle_api_exception,stk_info_fill
)

# APIRouter 인스턴스 생성
router = APIRouter()
logger = get_logger(__name__)

@router.get("/", response_model=List[SettingInfo])
async def get_all_settings():
    """모든 설정값 목록 조회"""
    settings_service = get_settings_service()
    return await settings_service.list_all()

@router.get("/{setting_key}")
async def get_setting(setting_key: str):
    """특정 설정값 조회"""
    settings_service = get_settings_service()
    value = await settings_service.get(setting_key)
    if value is None:
        return {"key": setting_key, "value": None, "exists": False}
    return {"key": setting_key, "value": value, "exists": True}


@router.put("/stk_info")
async def update_stk_info(force: bool = False):
    """stk_info 테이블 업데이트"""
    try:
       stk_info_fill(force=force)
    except Exception as e:
        await handle_api_exception("update_stk_info", e)