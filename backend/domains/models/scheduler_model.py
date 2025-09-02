from dataclasses import dataclass
from typing import Optional, Literal
from pydantic import BaseModel, Field

@dataclass
class SchedulerJob:
    """스케줄러 작업 정의 데이터 클래스
    
    SQL 테이블: kscheduler_job
    - 주기적으로 실행될 작업들을 정의하고 관리
    - 스케줄 유형(interval/cron/once)에 따라 다양한 실행 방식 지원
    """
    id: Optional[int] = None                                    # 고유 ID (자동 증가)
    name: str = ""                                             # 작업명 (고유값)
    func_name: str = ""                                        # 실행할 함수 키 (레지스트리에서 찾음)
    schedule_type: str = "interval"                            # 스케줄 타입: 'interval' | 'cron' | 'once'
    schedule_expr: str = ""                                    # 스케줄 표현식
    timezone: str = "Asia/Seoul"                               # 타임존
    enabled: int = 1                                           # 활성화 여부 (0: 비활성, 1: 활성)
    max_conc: int = 1                                          # 최대 동시 실행 수
    overlap_policy: str = "skip"                               # 중복 실행 정책: 'skip' | 'queue' | 'cancel'
    timeout_sec: int = 0                                       # 타임아웃 (초, 0이면 무제한)
    retry_max: int = 0                                         # 최대 재시도 횟수 (0이면 재시도 없음)
    retry_backoff: float = 2.0                                 # 지수 백오프 배수
    jitter_sec: int = 0                                        # 지터 (초, 0이면 지터 없음)
    next_run_at: Optional[str] = None                          # 다음 실행 시각 (ISO8601)
    last_run_at: Optional[str] = None                          # 마지막 실행 시각 (ISO8601)
    created_at: Optional[str] = None                           # 생성 시각
    updated_at: Optional[str] = None                           # 수정 시각

@dataclass
class SchedulerRunHistory:
    """스케줄러 실행 이력 데이터 클래스
    
    SQL 테이블: kscheduler_run_history
    - 각 작업의 실행 결과와 상태를 기록
    - 성공/실패/취소/타임아웃 등의 상태 추적
    """
    id: Optional[int] = None                                    # 고유 ID (자동 증가)
    job_name: str = ""                                         # 작업명
    started_at: str = ""                                       # 시작 시각
    finished_at: Optional[str] = None                          # 완료 시각
    status: Optional[str] = None                               # 상태: 'success' | 'error' | 'cancelled' | 'timeout'
    message: Optional[str] = None                              # 실행 결과 메시지

@dataclass
class SchedulerLock:
    """스케줄러 락 데이터 클래스
    
    SQL 테이블: kscheduler_lock
    - 멀티 프로세스 환경에서 중복 실행 방지용
    - 분산 락 메커니즘 구현
    """
    lock_key: str = ""                                         # 락 키 (예: 'job:nightly_scrape')
    holder: Optional[str] = None                               # 락 소유자 (hostname/pid)
    acquired_at: Optional[str] = None                          # 획득 시각

# === Pydantic 모델들 ===

class SchedulerJobCreate(BaseModel):
    """스케줄러 작업 생성 요청 모델"""
    name: str = Field(..., description="작업명 (고유값)", example="daily_stock_update", max_length=255)
    func_name: str = Field(..., description="실행할 함수 키", example="update_stock_prices", max_length=255)
    schedule_type: Literal["interval", "cron", "once"] = Field(..., description="스케줄 타입")
    schedule_expr: str = Field(..., description="스케줄 표현식", example="seconds=900")
    timezone: str = Field("Asia/Seoul", description="타임존", max_length=50)
    enabled: int = Field(1, description="활성화 여부 (0: 비활성, 1: 활성)", ge=0, le=1)
    max_conc: int = Field(1, description="최대 동시 실행 수", ge=1)
    overlap_policy: Literal["skip", "queue", "cancel"] = Field("skip", description="중복 실행 정책")
    timeout_sec: int = Field(0, description="타임아웃 (초, 0이면 무제한)", ge=0)
    retry_max: int = Field(0, description="최대 재시도 횟수", ge=0)
    retry_backoff: float = Field(2.0, description="지수 백오프 배수", ge=1.0)
    jitter_sec: int = Field(0, description="지터 (초)", ge=0)

class SchedulerJobUpdate(BaseModel):
    """스케줄러 작업 수정 요청 모델"""
    name: Optional[str] = Field(None, description="작업명", max_length=255)
    func_name: Optional[str] = Field(None, description="실행할 함수 키", max_length=255)
    schedule_type: Optional[Literal["interval", "cron", "once"]] = Field(None, description="스케줄 타입")
    schedule_expr: Optional[str] = Field(None, description="스케줄 표현식")
    timezone: Optional[str] = Field(None, description="타임존", max_length=50)
    enabled: Optional[int] = Field(None, description="활성화 여부", ge=0, le=1)
    max_conc: Optional[int] = Field(None, description="최대 동시 실행 수", ge=1)
    overlap_policy: Optional[Literal["skip", "queue", "cancel"]] = Field(None, description="중복 실행 정책")
    timeout_sec: Optional[int] = Field(None, description="타임아웃 (초)", ge=0)
    retry_max: Optional[int] = Field(None, description="최대 재시도 횟수", ge=0)
    retry_backoff: Optional[float] = Field(None, description="지수 백오프 배수", ge=1.0)
    jitter_sec: Optional[int] = Field(None, description="지터 (초)", ge=0)

class SchedulerJobResponse(BaseModel):
    """스케줄러 작업 응답 모델"""
    id: int = Field(..., description="고유 ID")
    name: str = Field(..., description="작업명")
    func_name: str = Field(..., description="실행할 함수 키")
    schedule_type: str = Field(..., description="스케줄 타입")
    schedule_expr: str = Field(..., description="스케줄 표현식")
    timezone: str = Field(..., description="타임존")
    enabled: int = Field(..., description="활성화 여부")
    max_conc: int = Field(..., description="최대 동시 실행 수")
    overlap_policy: str = Field(..., description="중복 실행 정책")
    timeout_sec: int = Field(..., description="타임아웃 (초)")
    retry_max: int = Field(..., description="최대 재시도 횟수")
    retry_backoff: float = Field(..., description="지수 백오프 배수")
    jitter_sec: int = Field(..., description="지터 (초)")
    next_run_at: Optional[str] = Field(None, description="다음 실행 시각")
    last_run_at: Optional[str] = Field(None, description="마지막 실행 시각")
    created_at: str = Field(..., description="생성 시각")
    updated_at: str = Field(..., description="수정 시각")

class SchedulerRunHistoryCreate(BaseModel):
    """스케줄러 실행 이력 생성 요청 모델"""
    job_name: str = Field(..., description="작업명", max_length=255)
    started_at: str = Field(..., description="시작 시각")
    finished_at: Optional[str] = Field(None, description="완료 시각")
    status: Optional[Literal["success", "error", "cancelled", "timeout"]] = Field(None, description="실행 상태")
    message: Optional[str] = Field(None, description="실행 결과 메시지")

class SchedulerRunHistoryResponse(BaseModel):
    """스케줄러 실행 이력 응답 모델"""
    id: int = Field(..., description="고유 ID")
    job_name: str = Field(..., description="작업명")
    started_at: str = Field(..., description="시작 시각")
    finished_at: Optional[str] = Field(None, description="완료 시각")
    status: Optional[str] = Field(None, description="실행 상태")
    message: Optional[str] = Field(None, description="실행 결과 메시지")

class SchedulerLockCreate(BaseModel):
    """스케줄러 락 생성 요청 모델"""
    lock_key: str = Field(..., description="락 키", example="job:nightly_scrape", max_length=255)
    holder: str = Field(..., description="락 소유자", example="server1/1234", max_length=255)

class SchedulerLockResponse(BaseModel):
    """스케줄러 락 응답 모델"""
    lock_key: str = Field(..., description="락 키")
    holder: str = Field(..., description="락 소유자")
    acquired_at: str = Field(..., description="획득 시각")

class SchedulerJobFilter(BaseModel):
    """스케줄러 작업 필터링 모델"""
    enabled: Optional[int] = Field(None, description="활성화 여부 필터 (0: 비활성, 1: 활성)")
    schedule_type: Optional[Literal["interval", "cron", "once"]] = Field(None, description="스케줄 타입 필터")
    func_name_like: Optional[str] = Field(None, description="함수명 부분 검색")
    name_like: Optional[str] = Field(None, description="작업명 부분 검색")

class SchedulerRunHistoryFilter(BaseModel):
    """스케줄러 실행 이력 필터링 모델"""
    job_name: Optional[str] = Field(None, description="특정 작업명 필터")
    status: Optional[Literal["success", "error", "cancelled", "timeout"]] = Field(None, description="실행 상태 필터")
    started_after: Optional[str] = Field(None, description="시작 시각 이후 필터 (ISO8601)")
    started_before: Optional[str] = Field(None, description="시작 시각 이전 필터 (ISO8601)")
