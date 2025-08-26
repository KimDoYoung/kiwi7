from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel, Field

@dataclass
class StkDiary:
    """주식 일지 데이터 클래스
    
    종목에 대한 생각, 분석, 메모를 기록하는 일지
    """
    id: Optional[int] = None                    # 고유 ID (자동 증가)
    ymd: str = ""                              # 날짜 (YYYYMMDD 형식)
    stk_cd: Optional[str] = None               # 종목코드 (선택사항, 전체 시장 일지도 가능)
    note: str = ""                             # 일지 내용 (메인 데이터)
    created_at: Optional[str] = None           # 생성 시각 (DB에서 자동 설정)
    updated_at: Optional[str] = None           # 수정 시각 (DB에서 자동 설정)

class StkDiaryCreate(BaseModel):
    """주식 일지 생성 요청 모델"""
    ymd: str = Field(..., description="날짜 (YYYYMMDD 형식)", example="20240822")
    stk_cd: Optional[str] = Field(None, description="종목코드 (선택사항)", example="005930")
    note: str = Field(..., description="일지 내용", example="삼성전자 실적 분석...")

class StkDiaryUpdate(BaseModel):
    """주식 일지 수정 요청 모델"""
    ymd: Optional[str] = Field(None, description="날짜 (YYYYMMDD 형식)")
    stk_cd: Optional[str] = Field(None, description="종목코드")
    note: Optional[str] = Field(None, description="일지 내용")

class StkDiaryResponse(BaseModel):
    """주식 일지 응답 모델"""
    id: int = Field(..., description="고유 ID")
    ymd: str = Field(..., description="날짜 (YYYYMMDD 형식)")
    stk_cd: Optional[str] = Field(None, description="종목코드")
    note: str = Field(..., description="일지 내용")
    created_at: str = Field(..., description="생성 시각")
    updated_at: str = Field(..., description="수정 시각")

class StkDiaryFilter(BaseModel):
    """주식 일지 필터링 모델"""
    ymd_from: Optional[str] = Field(None, description="시작 날짜 (YYYYMMDD)")
    ymd_to: Optional[str] = Field(None, description="종료 날짜 (YYYYMMDD)")
    stk_cd: Optional[str] = Field(None, description="특정 종목코드 필터")
    note_like: Optional[str] = Field(None, description="일지 내용 검색어")
