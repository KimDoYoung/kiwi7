
from backend.page_contexts.order_context import order_buy, order_sell
from backend.page_contexts.account_context import account_detail, account_list
from backend.page_contexts.settings_context import settings
from backend.page_contexts.stock_context import stock_detail, stock_find, stock_mystock

PAGE_CONTEXT_PROVIDERS = {
    "account/list": account_list,
    "account/detail": account_detail,
    "order/buy": order_buy,
    "order/sell": order_sell,
    "settings/edit": settings,
    "stock/find": stock_find,
    "stock/detail": stock_detail,
    "stock/mystock": stock_mystock,
}
