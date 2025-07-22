from fastapi import APIRouter, HTTPException
from backend.domains.user.user_model import UserInfo
from backend.domains.user.user_service import UserService

# APIRouter 인스턴스 생성
router = APIRouter()

@router.get("/{user_id}", response_model=UserInfo)
async def get_user(user_id: str, user_service :UserService):
    user = await user_service.get_1(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# @router.put("/{user_id}", response_model=User)
# async def update_user(user_id: str = Path(...), update_data: dict = Body(...), user_service :UserService):
#     user = await user_service.update_user(user_id, update_data)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
