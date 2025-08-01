from backend.core.logger import get_logger

logger = get_logger(__name__)

def settings():
    context_data = {
        "title": "설정 편집",
        "description": "사용자 설정을 편집합니다.",
    }
    
    return context_data