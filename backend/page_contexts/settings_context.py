from backend.core.logger import get_logger
from backend.domains.services.dependency import get_service
from backend.domains.services.settings_keys import SettingsKeys

logger = get_logger(__name__)

def settings():
    context_data = {
        "title": "설정 편집",
        "description": "사용자 설정을 편집합니다.",
    }
    service = get_service("settings")
    context_data["last_stk_info_fill_time"] = service.get(SettingsKeys.LAST_STK_INFO_FILL)
    return context_data