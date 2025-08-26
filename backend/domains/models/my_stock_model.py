from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel, Field

@dataclass
class MyStock:
    """관심 종목 관리 데이터 클래스
    
    SQL 테이블: my_stock
    - 개인적으로 관심 있거나 보유 중인 종목을 관리
    - 종목코드를 PK로 사용하여 중복 방지
    - 보유 여부와 관심 여부를 분리하여 관리 (각각 0/1)
    """
    stk_cd: str                              # 종목코드 (PK) - 6자리 숫자 (예: 005930)
    stk_nm: str                              # 종목명 (예: 삼성전자)
    sector: Optional[str] = None             # 분야/섹터 (예: 반도체, 바이오 등)
    is_hold: int = 0                         # 보유여부 (0: 미보유, 1: 보유)
    is_watch: int = 0                        # 관심여부 (0: 비관심, 1: 관심)
    note: Optional[str] = None               # 메모 (투자 이유, 분석 내용 등)
    created_at: Optional[str] = None         # 생성 시각 (DB에서 자동 설정)
    updated_at: Optional[str] = None         # 수정 시각 (DB에서 자동 설정)

class MyStockCreate(BaseModel):
    """관심 종목 생성 요청 모델
    
    새로운 종목을 my_stock 테이블에 추가할 때 사용
    - stk_cd는 중복 불가 (PK 제약조건)
    - is_hold, is_watch는 기본값 0
    """
    stk_cd: str = Field(..., description="종목코드 (6자리)", example="005930", max_length=6)
    stk_nm: str = Field(..., description="종목명", example="삼성전자", max_length=100)
    sector: Optional[str] = Field(None, description="분야/섹터", example="반도체")
    is_hold: int = Field(0, description="보유여부 (0: 미보유, 1: 보유)", ge=0, le=1)
    is_watch: int = Field(0, description="관심여부 (0: 비관심, 1: 관심)", ge=0, le=1)
    note: Optional[str] = Field(None, description="메모", example="실적 개선 기대")

class MyStockUpdate(BaseModel):
    """관심 종목 수정 요청 모델
    
    기존 종목 정보를 부분적으로 업데이트할 때 사용
    - 모든 필드가 Optional (수정하고 싶은 필드만 제공)
    - stk_cd는 PK이므로 수정 불가 (URL 파라미터로 식별)
    """
    stk_nm: Optional[str] = Field(None, description="종목명", max_length=100)
    sector: Optional[str] = Field(None, description="분야/섹터")
    is_hold: Optional[int] = Field(None, description="보유여부 (0: 미보유, 1: 보유)", ge=0, le=1)
    is_watch: Optional[int] = Field(None, description="관심여부 (0: 비관심, 1: 관심)", ge=0, le=1)
    note: Optional[str] = Field(None, description="메모")

class MyStockResponse(BaseModel):
    """관심 종목 응답 모델
    
    API 응답으로 반환되는 완전한 종목 정보
    - DB에서 조회된 모든 필드 포함
    - created_at, updated_at은 필수 (DB에서 자동 생성)
    """
    stk_cd: str = Field(..., description="종목코드", example="005930")
    stk_nm: str = Field(..., description="종목명", example="삼성전자")
    sector: Optional[str] = Field(None, description="분야/섹터", example="반도체")
    is_hold: int = Field(..., description="보유여부 (0: 미보유, 1: 보유)")
    is_watch: int = Field(..., description="관심여부 (0: 비관심, 1: 관심)")
    note: Optional[str] = Field(None, description="메모")
    created_at: str = Field(..., description="생성 시각", example="2024-08-22 14:30:00")
    updated_at: str = Field(..., description="수정 시각", example="2024-08-22 14:30:00")

class MyStockFilter(BaseModel):
    """관심 종목 필터링 모델
    
    종목 목록 조회 시 검색 조건을 지정하는 모델
    - 모든 필드가 Optional (필터링하고 싶은 조건만 제공)
    - 여러 조건을 AND로 결합하여 검색
    """
    is_hold: Optional[int] = Field(None, description="보유여부 필터 (0: 미보유, 1: 보유)")
    is_watch: Optional[int] = Field(None, description="관심여부 필터 (0: 비관심, 1: 관심)")
    sector: Optional[str] = Field(None, description="특정 섹터 필터", example="반도체")
    stk_nm_like: Optional[str] = Field(None, description="종목명 부분 검색", example="삼성")
