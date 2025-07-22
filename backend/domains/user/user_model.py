from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel
@dataclass
class UserInfo:
    name: str
    value: str
    created_at: datetime = None  # DB에서 가져올 때만 사용


class LoginFormData(BaseModel):
    userId: str
    password: str


class AccessToken(BaseModel):
    access_token: str
    token_type: str
    user_id: str