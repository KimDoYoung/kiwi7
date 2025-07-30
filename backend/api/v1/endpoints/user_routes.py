
from fastapi import APIRouter
from typing import List
from backend.api.v1.endpoints.home_routes import get_user_service
from backend.core.logger import get_logger
from backend.domains.user.user_model import UserInfo
from backend.domains.user.user_service import get_user_service

# APIRouter 인스턴스 생성
router = APIRouter()
logger = get_logger(__name__)

@router.get("/{user_id}", response_model=List[UserInfo])
async def get_user(user_id: str):
    user_service = get_user_service()
    return user_service.list_all()
