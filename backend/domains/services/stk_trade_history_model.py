from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel, Field

@dataclass
class StkTradeHistory:
    """주식 매매 이력 데이터 클래스
    
    특정 종목에 대한 매매 기록을 저장
    """
    id: Optional[int] = None                    # 고유 ID (자동 증가)
    stk_cd: str = ""                           # 종목코드 (필수)
    stk_nm: str = ""                           # 종목명 (필수)
    ymd: str = ""                              # 거래일 (YYYYMMDD 형식)
    note: str = ""                             # 매매 기록 메모 (가격, 수량, 이유 등)
    created_at: Optional[str] = None           # 생성 시각 (DB에서 자동 설정)
    updated_at: Optional[str] = None           # 수정 시각 (DB에서 자동 설정)

class StkTradeHistoryCreate(BaseModel):
    """매매 이력 생성 요청 모델"""
    stk_cd: str = Field(..., description="종목코드", example="005930")
    stk_nm: str = Field(..., description="종목명", example="삼성전자")
    ymd: str = Field(..., description="거래일 (YYYYMMDD 형식)", example="20240822")
    note: str = Field(..., description="매매 기록 (가격, 수량, 매매 이유 등)", 
                     example="매수 100주 @ 75,000원 - 실적 개선 기대")

class StkTradeHistoryUpdate(BaseModel):
    """매매 이력 수정 요청 모델"""
    stk_cd: Optional[str] = Field(None, description="종목코드")
    stk_nm: Optional[str] = Field(None, description="종목명")
    ymd: Optional[str] = Field(None, description="거래일 (YYYYMMDD 형식)")
    note: Optional[str] = Field(None, description="매매 기록")

class StkTradeHistoryResponse(BaseModel):
    """매매 이력 응답 모델"""
    id: int = Field(..., description="고유 ID")
    stk_cd: str = Field(..., description="종목코드")
    stk_nm: str = Field(..., description="종목명")
    ymd: str = Field(..., description="거래일 (YYYYMMDD 형식)")
    note: str = Field(..., description="매매 기록")
    created_at: str = Field(..., description="생성 시각")
    updated_at: str = Field(..., description="수정 시각")

class StkTradeHistoryFilter(BaseModel):
    """매매 이력 필터링 모델"""
    stk_cd: Optional[str] = Field(None, description="특정 종목코드 필터")
    ymd_from: Optional[str] = Field(None, description="시작 날짜 (YYYYMMDD)")
    ymd_to: Optional[str] = Field(None, description="종료 날짜 (YYYYMMDD)")
    stk_nm_like: Optional[str] = Field(None, description="종목명 검색어")
    note_like: Optional[str] = Field(None, description="매매 기록 검색어")
