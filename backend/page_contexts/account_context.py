from datetime import datetime
from backend.core.logger import get_logger
logger = get_logger(__name__)

def account_list():
    """계좌 정보를 가져오는 함수"""

    context_data = {
        "title": "계좌정보",
    }
    
    return context_data

def account_fill():
    """체결내역"""

    context_data = {
        "title": "체결내역",
    }
    
    return context_data


def account_detail(context):
    """계좌 상세 정보를 가져오는 함수"""

    context_data = {
        "title": "계좌상세정보",
    }

    return context_data

def account_profit_lose(context):
    """계좌 손익 정보를 가져오는 함수"""

    today_ymd = datetime.today().strftime("%Y%m%d")
    start_ymd = context.get("start_ymd", today_ymd)
    end_ymd = context.get("end_ymd", today_ymd)

    context_data = {
        "title": "계좌손익정보",
        "start_ymd" : start_ymd,
        "end_ymd" : end_ymd
    }

    return context_data