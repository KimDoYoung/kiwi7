from fastapi import APIRouter
from typing import List
from backend.api.common.api_helpers import create_success_response, create_error_response
from backend.core.logger import get_logger
from backend.domains.services.dependency import get_service
from backend.domains.models.settings_model import SettingInfo
from backend.api.common.stock_functions import stk_info_fill

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
        return {"key": setting_key, "value": None, "exists": False}
    return {"key": setting_key, "value": value, "exists": True}

@router.put("/stk_info")
async def update_stk_info(force: bool = False):
    """stk_info 테이블 업데이트"""
    try:
        # stk_info_fill은 비동기 함수이므로 await 사용
        await stk_info_fill(force=force)
        return create_success_response("stk_info 테이블이 업데이트되었습니다.")
    except Exception as e:
        logger.error(f"stk_info 테이블 업데이트 중 오류 발생: {str(e)}")
        # api_helpers의 create_error_response 사용 (메시지만 전달)
        return create_error_response(
            message=f"stk_info 테이블 업데이트 중 오류가 발생했습니다: {str(e)}",
            error_code="STK_INFO_UPDATE_ERROR",
            status_code=500
        )