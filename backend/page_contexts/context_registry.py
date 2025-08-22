
from backend.page_contexts.order_context import order_buy, order_sell
from backend.page_contexts.account_context import account_list
from backend.page_contexts.settings_context import settings

PAGE_CONTEXT_PROVIDERS = {
    "account/list": account_list,
    "order/buy": order_buy,
    "order/sell": order_sell,
    "settings/edit": settings
}
