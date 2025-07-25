
from backend.domains.user.user_service import UserService


async def get_user_data(user_id: str):
    """사용자 정보를 가져오는 함수"""
    user_service_instance = UserService()
    list = await user_service_instance.list_all()
    return {"list": list}