from backend.core.logger import get_logger
from backend.domains.services.dependency import get_service
from backend.domains.services.settings_keys import SettingsKey
from backend.core.config import config

logger = get_logger(__name__)

async def get_settings_edit_context(context: dict):
    """settings/edit 페이지용 컨텍스트 데이터"""
    try:
        service = get_service("settings")
        last_stk_info_fill = await service.get(SettingsKey.LAST_STK_INFO_FILL)
        
        # None이나 빈 값 처리
        if not last_stk_info_fill:
            last_stk_info_fill = "정보 없음"
        
        return {
            "version": str(config.VERSION) if config.VERSION else "Unknown",
            "last_stk_info_fill": str(last_stk_info_fill)
        }
    except Exception as e:
        logger.error(f"설정 컨텍스트 로딩 중 오류 발생: {e}", exc_info=True)
        return {
            "version": "Unknown",
            "last_stk_info_fill": "정보 없음"
        }