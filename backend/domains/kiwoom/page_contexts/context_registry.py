
from backend.domains.kiwoom.page_contexts.order_context import order_buy, order_sell
from backend.domains.kiwoom.page_contexts.user_context import user_user
from backend.domains.kiwoom.page_contexts.account_context import account_list
from backend.domains.kiwoom.page_contexts.settings_context import settings

PAGE_CONTEXT_PROVIDERS = {
    "user/user": user_user,
    "account/list": account_list,
    "order/buy": order_buy,
    "order/sell": order_sell,
    "settings/edit": settings
}
