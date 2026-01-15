from backend.core.logger import get_logger
from backend.domains.services.dependency import get_service
from backend.domains.services.settings_keys import SettingsKey

logger = get_logger(__name__)

async def settings():
    """설정 페이지를 위한 컨텍스트 데이터를 반환하는 비동기 함수"""
    context_data = {
        "title": "설정 편집",
        "description": "사용자 설정을 편집합니다.",
    }
    
    try:
        # 설정 서비스 가져오기
        service = get_service("settings")
        
        # 마지막 주식 정보 업데이트 시간 가져오기
        last_fill_time = await service.get(SettingsKey.LAST_STK_INFO_FILL)

        context_data["last_stk_info_fill"] = last_fill_time
        context_data["settings_available"] = True
        context_data["version"] = service.config.VERSION
        
    except Exception as e:
        logger.error(f"설정 정보 로딩 중 오류 발생: {e}")
        context_data["last_stk_info_fill"] = None
        context_data["settings_available"] = False
        context_data["version"] = None
    return context_data