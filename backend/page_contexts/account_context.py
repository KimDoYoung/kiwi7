from backend.core.logger import get_logger
logger = get_logger(__name__)

def account_list():
    """계좌 정보를 가져오는 함수"""

    context_data = {
        "title": "계좌정보",
    }
    
    return context_data
