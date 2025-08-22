
from backend.api.v1.endpoints.home_routes import get_settings_service



async def user_user(user_id: str):
    """사용자 정보를 가져오는 함수"""
    settings_service = get_settings_service()
    list = await settings_service.list_all()
    return {"list": list}