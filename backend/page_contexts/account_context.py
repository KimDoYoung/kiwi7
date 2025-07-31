from backend.core.logger import get_logger
logger = get_logger(__name__)

def account_list():
    """계좌 정보를 가져오는 함수"""

    logger.info("Fetching account list")
    
    return {"name": "홍길동", "list": []}
