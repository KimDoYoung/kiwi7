from backend.page_contexts.account_context import (
    account_detail,
    account_fill,
    account_list,
    account_profit_lose,
)
from backend.page_contexts.order_context import order_buy, order_sell
from backend.page_contexts.settings_context import get_settings_edit_context

PAGE_CONTEXT_PROVIDERS = {
    "stkcompany/kiwoom/account/list": account_list,
    "stkcompany/kiwoom/account/fill": account_fill,
    "stkcompany/kiwoom/account/detail": account_detail,
    "stkcompany/kiwoom/account/profit_lose": account_profit_lose,

    "order/buy": order_buy,
    "order/sell": order_sell,
    
    "settings/edit": get_settings_edit_context,
}
