from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel, Field

@dataclass
class StkCache:
    """주식 캐시 데이터 클래스
    
    종목에 대한 임시 데이터를 저장 (전일종가, 시가, 거래량 등)
    """
    id: Optional[int] = None                    # 고유 ID (자동 증가)
    stk_cd: str = ""                           # 종목코드 (필수)
    name: str = ""                             # 캐시 데이터 이름 (예: "전일종가", "시가", "거래량")
    value: str = ""                            # 캐시 값 (문자열로 저장)
    created_at: Optional[str] = None           # 생성 시각 (DB에서 자동 설정)

class StkCacheCreate(BaseModel):
    """캐시 데이터 생성 요청 모델"""
    stk_cd: str = Field(..., description="종목코드", example="005930")
    name: str = Field(..., description="캐시 데이터 이름", 
                     example="전일종가", 
                     pattern="^[가-힣a-zA-Z0-9_]+$")
    value: str = Field(..., description="캐시 값", example="75000")

class StkCacheUpdate(BaseModel):
    """캐시 데이터 수정 요청 모델"""
    stk_cd: Optional[str] = Field(None, description="종목코드")
    name: Optional[str] = Field(None, description="캐시 데이터 이름")
    value: Optional[str] = Field(None, description="캐시 값")

class StkCacheResponse(BaseModel):
    """캐시 데이터 응답 모델"""
    id: int = Field(..., description="고유 ID")
    stk_cd: str = Field(..., description="종목코드")
    name: str = Field(..., description="캐시 데이터 이름")
    value: str = Field(..., description="캐시 값")
    created_at: str = Field(..., description="생성 시각")

class StkCacheFilter(BaseModel):
    """캐시 데이터 필터링 모델"""
    stk_cd: Optional[str] = Field(None, description="특정 종목코드 필터")
    name: Optional[str] = Field(None, description="특정 캐시 이름 필터")
    name_like: Optional[str] = Field(None, description="캐시 이름 검색어")
    value_like: Optional[str] = Field(None, description="캐시 값 검색어")

class StkCacheByName(BaseModel):
    """특정 종목의 캐시 데이터 조회용 모델"""
    stk_cd: str = Field(..., description="종목코드")
    name: str = Field(..., description="캐시 데이터 이름")
