

from backend.page_contexts.user_page import get_user_data  # Adjust the import path as needed

PAGE_CONTEXT_PROVIDERS = {
    "user/user": get_user_data,
}
