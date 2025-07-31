
from backend.page_contexts.user_countext import user_user
from backend.page_contexts.account_context import account_list

PAGE_CONTEXT_PROVIDERS = {
    "user/user": user_user,
    "account/list": account_list,
}
