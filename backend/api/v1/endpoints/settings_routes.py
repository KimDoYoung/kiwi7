from fastapi import APIRouter
from typing import List

from backend.core.logger import get_logger
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomApiHelper
from backend.domains.services.dependency import get_service
from backend.domains.models.settings_model import SettingInfo
from backend.api.common.stock_functions import stk_info_fill
from backend.domains.services.settings_keys import SettingsKey

# APIRouter 인스턴스 생성
router = APIRouter()
logger = get_logger(__name__)

@router.get("/", response_model=List[SettingInfo])
async def get_all_settings():
    """모든 설정값 목록 조회"""
    settings_service = get_service("settings")
    return await settings_service.list_all()

@router.get("/{setting_key}")
async def get_setting(setting_key: str):
    """특정 설정값 조회"""
    settings_service = get_service("settings")
    value = await settings_service.get(setting_key)
    if value is None:
        return KiwoomApiHelper.create_error_response(error_code="SETTING_NOT_FOUND", error_message=f"설정값을 찾을 수 없습니다: {setting_key}")
    return {"key": setting_key, "value": value, "exists": True}

@router.put("/stk_info")
async def update_stk_info(force: bool = False):
    """stk_info 테이블 업데이트"""
    try:
        # stk_info_fill은 비동기 함수이므로 await 사용
        await stk_info_fill(force=force)
        service = get_service("settings")
        last_fill_time = await service.get(SettingsKey.LAST_STK_INFO_FILL)
        return KiwoomApiHelper.create_success_response(data={"last_stk_info_fill": last_fill_time})
    except Exception as e:
        logger.error(f"stk_info 테이블 업데이트 중 오류 발생: {str(e)}")
        # api_helpers의 create_error_response 사용 (메시지만 전달)
        return KiwoomApiHelper.create_error_response(
            error_code="STK_INFO_UPDATE_ERROR",
            error_message=f"stk_info 테이블 업데이트 중 오류가 발생했습니다: {str(e)}"
        )