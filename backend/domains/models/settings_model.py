from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel

@dataclass
class SettingInfo:
    """설정 정보 데이터 클래스
    
    시스템 설정값을 name-value 쌍으로 저장하는 클래스
    """
    name: str
    value: str
    created_at: datetime = None  # DB에서 가져올 때만 사용


class LoginFormData(BaseModel):
    """로그인 폼 데이터 모델"""
    userId: str
    password: str


class AccessToken(BaseModel):
    """액세스 토큰 모델"""
    access_token: str
    token_type: str
    user_id: str
