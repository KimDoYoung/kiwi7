# stk_info_model.py
"""
모듈 설명: 
    - 종목 정보 관련 데이터 모델을 정의
주요 기능:
    - StkInfo: 종목 기본정보를 담는 데이터 클래스
    - StkInfoCreate: 새 종목 정보 생성 시 사용하는 Pydantic 모델
    - StkInfoUpdate: 종목 정보 수정 시 사용하는 Pydantic 모델 (모든 필드 Optional)
    - StkInfoResponse: API 응답용 Pydantic 모델
    - StkInfoFilter: 검색/필터링용 Pydantic 모델
    - StkInfoBulkCreate: 키움 API에서 받은 대량 데이터 저장용 모델
작성자: 김도영
작성일: 2025-08-24
버전: 1.0
"""
from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel, Field

@dataclass
class StkInfo:
    """종목 기본정보 데이터 클래스
    
    SQL 테이블: stk_info
    - 국내주식 > 종목정보 > 종목정보 리스트(ka10099) API 결과 저장
    - 키움 API에서 제공하는 종목의 기본 정보를 관리
    - 종목코드(단축코드)를 PK로 사용
    """
    code: str                                # 종목코드(단축코드) - PK (예: 005930)
    name: Optional[str] = None               # 종목명 (예: 삼성전자)
    list_count: Optional[str] = None         # 상장주식수 (API 원문: String)
    audit_info: Optional[str] = None         # 감리구분
    reg_day: Optional[str] = None            # 상장일 (YYYYMMDD)
    last_price: Optional[str] = None         # 전일종가
    state: Optional[str] = None              # 종목상태
    market_code: Optional[str] = None        # 시장구분코드
    market_name: Optional[str] = None        # 시장명
    up_name: Optional[str] = None            # 업종명
    up_size_name: Optional[str] = None       # 회사크기분류
    company_class_name: Optional[str] = None # 회사분류 (코스닥만 존재)
    order_warning: Optional[str] = None      # 투자유의종목여부: 0 해당없음, 2 정리매매, 3 단기과열, 4 투자위험, 5 투자경과, 1 ETF투자주의요망
    nxt_enable: Optional[str] = None         # NXT 가능여부 (Y/N)
    created_at: Optional[str] = None         # 생성 시각 (DB에서 자동 설정)

class StkInfoCreate(BaseModel):
    """종목 기본정보 생성 요청 모델
    
    새로운 종목 정보를 stk_info 테이블에 추가할 때 사용
    - code는 중복 불가 (PK 제약조건)
    - 키움 API 응답 데이터를 그대로 저장
    """
    code: str = Field(..., description="종목코드(단축코드)", example="005930", max_length=10)
    name: Optional[str] = Field(None, description="종목명", example="삼성전자")
    list_count: Optional[str] = Field(None, description="상장주식수", example="5969782550")
    audit_info: Optional[str] = Field(None, description="감리구분", example="정상")
    reg_day: Optional[str] = Field(None, description="상장일 (YYYYMMDD)", example="19750611")
    last_price: Optional[str] = Field(None, description="전일종가", example="71000")
    state: Optional[str] = Field(None, description="종목상태", example="정상")
    market_code: Optional[str] = Field(None, description="시장구분코드", example="STK")
    market_name: Optional[str] = Field(None, description="시장명", example="코스피")
    up_name: Optional[str] = Field(None, description="업종명", example="전기전자")
    up_size_name: Optional[str] = Field(None, description="회사크기분류", example="대형")
    company_class_name: Optional[str] = Field(None, description="회사분류 (코스닥만 존재)")
    order_warning: Optional[str] = Field(None, description="투자유의종목여부", example="0")
    nxt_enable: Optional[str] = Field(None, description="NXT 가능여부 (Y/N)", example="Y")

class StkInfoUpdate(BaseModel):
    """종목 기본정보 수정 요청 모델
    
    기존 종목 정보를 부분적으로 업데이트할 때 사용
    - 모든 필드가 Optional (수정하고 싶은 필드만 제공)
    - code는 PK이므로 수정 불가 (URL 파라미터로 식별)
    """
    name: Optional[str] = Field(None, description="종목명")
    list_count: Optional[str] = Field(None, description="상장주식수")
    audit_info: Optional[str] = Field(None, description="감리구분")
    reg_day: Optional[str] = Field(None, description="상장일 (YYYYMMDD)")
    last_price: Optional[str] = Field(None, description="전일종가")
    state: Optional[str] = Field(None, description="종목상태")
    market_code: Optional[str] = Field(None, description="시장구분코드")
    market_name: Optional[str] = Field(None, description="시장명")
    up_name: Optional[str] = Field(None, description="업종명")
    up_size_name: Optional[str] = Field(None, description="회사크기분류")
    company_class_name: Optional[str] = Field(None, description="회사분류 (코스닥만 존재)")
    order_warning: Optional[str] = Field(None, description="투자유의종목여부")
    nxt_enable: Optional[str] = Field(None, description="NXT 가능여부 (Y/N)")

class StkInfoResponse(BaseModel):
    """종목 기본정보 응답 모델
    
    API 응답으로 반환되는 완전한 종목 정보
    - DB에서 조회된 모든 필드 포함
    - created_at은 필수 (DB에서 자동 생성)
    """
    code: str = Field(..., description="종목코드(단축코드)", example="005930")
    name: Optional[str] = Field(None, description="종목명", example="삼성전자")
    list_count: Optional[str] = Field(None, description="상장주식수", example="5969782550")
    audit_info: Optional[str] = Field(None, description="감리구분", example="정상")
    reg_day: Optional[str] = Field(None, description="상장일 (YYYYMMDD)", example="19750611")
    last_price: Optional[str] = Field(None, description="전일종가", example="71000")
    state: Optional[str] = Field(None, description="종목상태", example="정상")
    market_code: Optional[str] = Field(None, description="시장구분코드", example="STK")
    market_name: Optional[str] = Field(None, description="시장명", example="코스피")
    up_name: Optional[str] = Field(None, description="업종명", example="전기전자")
    up_size_name: Optional[str] = Field(None, description="회사크기분류", example="대형")
    company_class_name: Optional[str] = Field(None, description="회사분류 (코스닥만 존재)")
    order_warning: Optional[str] = Field(None, description="투자유의종목여부", example="0")
    nxt_enable: Optional[str] = Field(None, description="NXT 가능여부 (Y/N)", example="Y")
    created_at: Optional[str] = Field(None, description="생성 시각", example="2024-08-24 14:30:00")

class StkInfoFilter(BaseModel):
    """종목 기본정보 필터링 모델
    
    종목 목록 조회 시 검색 조건을 지정하는 모델
    - 모든 필드가 Optional (필터링하고 싶은 조건만 제공)
    - 여러 조건을 AND로 결합하여 검색
    """
    market_code: Optional[str] = Field(None, description="시장구분코드 필터", example="STK")
    market_name: Optional[str] = Field(None, description="시장명 필터", example="코스피")
    up_name: Optional[str] = Field(None, description="업종명 필터", example="전기전자")
    up_size_name: Optional[str] = Field(None, description="회사크기분류 필터", example="대형")
    order_warning: Optional[str] = Field(None, description="투자유의종목여부 필터", example="0")
    nxt_enable: Optional[str] = Field(None, description="NXT 가능여부 필터", example="Y")
    name_like: Optional[str] = Field(None, description="종목명 부분 검색", example="삼성")
    code_like: Optional[str] = Field(None, description="종목코드 부분 검색", example="005")

class StkInfoBulkCreate(BaseModel):
    """종목 기본정보 대량 생성 요청 모델
    
    키움 API에서 받은 대량의 종목 정보를 한 번에 저장할 때 사용
    """
    stocks: list[StkInfoCreate] = Field(..., description="종목 정보 리스트")
    overwrite: bool = Field(False, description="기존 데이터 덮어쓰기 여부")
