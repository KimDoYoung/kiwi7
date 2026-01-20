"""
tokens 테이블 모델
증권사별 API 토큰을 통합 관리
"""
from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel, Field


@dataclass
class Token:
    """토큰 정보 데이터 클래스

    SQL 테이블: tokens
    - 증권사별 API 액세스 토큰 관리
    - broker_type을 PK로 사용하여 증권사당 하나의 토큰만 유지
    """
    broker_type: str                           # PK: 'KIWOOM' | 'KIS' | 'LS'
    access_token: str                          # 액세스 토큰
    expires_at: str                            # 만료 시각 (ISO8601 또는 증권사별 형식)
    created_at: Optional[str] = None           # 생성 시각
    updated_at: Optional[str] = None           # 수정 시각


class TokenCreate(BaseModel):
    """토큰 생성 요청 모델"""
    broker_type: str = Field(..., description='증권사 타입', example='KIWOOM')
    access_token: str = Field(..., description='액세스 토큰')
    expires_at: str = Field(..., description='만료 시각')


class TokenUpdate(BaseModel):
    """토큰 수정 요청 모델 (upsert 시 사용)"""
    access_token: str = Field(..., description='액세스 토큰')
    expires_at: str = Field(..., description='만료 시각')
