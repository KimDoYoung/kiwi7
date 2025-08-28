def stock_detail(context):
    """종목상세"""

    context_data = {
        "title": "종목상세",
        "stk_cd" : context.get("stk_cd")
    }

    return context_data

def stock_mystock():
    """나의 종목"""

    context_data = {
        "title": "관심 종목",
    }

    return context_data