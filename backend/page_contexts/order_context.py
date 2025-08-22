from backend.core.logger import get_logger
logger = get_logger(__name__)

def order_buy():

    context_data = {
        "title": "주식매수",
    }
    
    return context_data

def order_sell():
    context_data = {
        "title": "주식매도",
    }
    
    return context_data
