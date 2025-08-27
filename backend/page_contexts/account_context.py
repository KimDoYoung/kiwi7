from backend.core.logger import get_logger
logger = get_logger(__name__)

def account_list():
    """계좌 정보를 가져오는 함수"""

    context_data = {
        "title": "계좌정보",
    }
    
    return context_data

def account_detail(context):
    """계좌 상세 정보를 가져오는 함수"""

    context_data = {
        "title": "계좌상세정보",
        "stk_cd" : context.get("stk_cd")
    }

    return context_data