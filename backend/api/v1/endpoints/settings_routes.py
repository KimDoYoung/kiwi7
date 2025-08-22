from fastapi import APIRouter
from typing import List
from backend.core.logger import get_logger
from backend.domains.settings.settings_model import SettingInfo
from backend.domains.settings.settings_service import SettingsService

# APIRouter 인스턴스 생성
router = APIRouter()
logger = get_logger(__name__)

def get_settings_service():
    return SettingsService()

@router.get("/{setting_id}", response_model=List[SettingInfo])
async def get_setting(setting_id: str):
    settings_service = get_settings_service()
    return await settings_service.list_all()
