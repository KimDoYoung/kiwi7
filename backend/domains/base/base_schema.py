"""
공통 스키마 정의
증권사 API의 공통 Request/Response 모델을 정의합니다.
"""
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum


class ContYn(str, Enum):
    """연속조회 여부"""
    Y = 'Y'
    N = 'N'


class BaseRequest(BaseModel):
    """공통 API 요청 베이스 모델"""
    api_id: str
    cont_yn: ContYn = ContYn.N
    next_key: Optional[str] = None
    payload: Dict[str, Any]
    title: Optional[str] = None

    class Config:
        use_enum_values = True


class BaseResponse(BaseModel):
    """공통 API 응답 베이스 모델"""
    data: Optional[Dict[str, Any]] = None
    headers: Optional[Dict[str, str]] = None
    api_info: Optional[Dict[str, str]] = None
    status_code: int = 200
    cont_yn: ContYn = ContYn.N
    next_key: Optional[str] = None
    request_time: Optional[datetime] = None
    response_time: Optional[datetime] = None
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    success: bool = True

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None
        }
