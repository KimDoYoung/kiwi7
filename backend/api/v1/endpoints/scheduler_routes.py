"""
스케줄러 관리 API 엔드포인트

모듈 설명:
    - kscheduler 관련 작업, 실행 이력, 락 관리 API 제공
    - 스케줄러 작업 CRUD 및 제어 기능
    - 실행 이력 조회 및 통계 기능
    - 분산 락 관리 기능

작성자: 김도영
작성일: 2025-09-02
버전: 1.0
"""

from fastapi import APIRouter, Query, Depends
from typing import Optional

from backend.core.logger import get_logger
from backend.domains.models.scheduler_model import (
    SchedulerJobCreate, SchedulerJobUpdate, SchedulerJobFilter,
    SchedulerRunHistoryFilter,
    SchedulerLockCreate
)
from backend.domains.services.scheduler_service import SchedulerService
from backend.domains.stkcompanys.kiwoom.models.kiwoom_schema import KiwoomApiHelper, KiwoomResponse

logger = get_logger(__name__)
router = APIRouter()

def get_scheduler_service():
    """스케줄러 서비스 의존성 주입"""
    return SchedulerService()

# === 스케줄러 작업 관리 API ===

@router.post("/jobs", response_model=KiwoomResponse, summary="스케줄러 작업 생성")
async def create_job(
    job: SchedulerJobCreate,
    service: SchedulerService = Depends(get_scheduler_service)
):
    """새로운 스케줄러 작업을 생성합니다."""
    logger.info(f"스케줄러 작업 생성 요청: {job.name}")
    try:
        # 중복 이름 확인
        existing_job = await service.get_job_by_name(job.name)
        if existing_job:
            logger.warning(f"이미 존재하는 작업명: {job.name}")
            return KiwoomApiHelper.create_error_response(
                error_code="DUPLICATE_JOB_NAME",
                error_message=f"작업명 '{job.name}'이 이미 존재합니다."
            )
        
        created_job = await service.create_job(job)
        logger.info(f"스케줄러 작업 생성 완료: {created_job.name} (ID: {created_job.id})")
        
        return KiwoomApiHelper.create_success_response(data={
            "id": created_job.id,
            "name": created_job.name,
            "func_name": created_job.func_name,
            "schedule_type": created_job.schedule_type,
            "schedule_expr": created_job.schedule_expr,
            "enabled": created_job.enabled,
            "created_at": created_job.created_at
        })
        
    except Exception as e:
        logger.error(f"스케줄러 작업 생성 실패: {e}")
        return KiwoomApiHelper.create_error_response(
            error_code="JOB_CREATE_ERROR",
            error_message=str(e)
        )

@router.get("/jobs", response_model=KiwoomResponse, summary="스케줄러 작업 목록 조회")
async def get_jobs(
    enabled: Optional[int] = Query(None, description="활성화 여부 필터 (0: 비활성, 1: 활성)"),
    schedule_type: Optional[str] = Query(None, description="스케줄 타입 필터"),
    func_name_like: Optional[str] = Query(None, description="함수명 부분 검색"),
    name_like: Optional[str] = Query(None, description="작업명 부분 검색"),
    service: SchedulerService = Depends(get_scheduler_service)
):
    """스케줄러 작업 목록을 조회합니다."""
    logger.info("스케줄러 작업 목록 조회 요청")
    try:
        # 필터 객체 생성
        filters = SchedulerJobFilter(
            enabled=enabled,
            schedule_type=schedule_type,
            func_name_like=func_name_like,
            name_like=name_like
        ) if any([enabled is not None, schedule_type, func_name_like, name_like]) else None
        
        jobs = await service.get_all_jobs(filters)
        
        # 응답 데이터 변환
        job_list = []
        for job in jobs:
            job_list.append({
                "id": job.id,
                "name": job.name,
                "func_name": job.func_name,
                "schedule_type": job.schedule_type,
                "schedule_expr": job.schedule_expr,
                "timezone": job.timezone,
                "enabled": job.enabled,
                "max_conc": job.max_conc,
                "overlap_policy": job.overlap_policy,
                "timeout_sec": job.timeout_sec,
                "retry_max": job.retry_max,
                "retry_backoff": job.retry_backoff,
                "jitter_sec": job.jitter_sec,
                "next_run_at": job.next_run_at,
                "last_run_at": job.last_run_at,
                "created_at": job.created_at,
                "updated_at": job.updated_at
            })
        
        logger.info(f"스케줄러 작업 목록 조회 완료: {len(job_list)}개")
        return KiwoomApiHelper.create_success_response(data={"jobs": job_list, "count": len(job_list)})
        
    except Exception as e:
        logger.error(f"스케줄러 작업 목록 조회 실패: {e}")
        return KiwoomApiHelper.create_error_response(
            error_code="JOB_LIST_ERROR",
            error_message=str(e)
        )

@router.get("/jobs/{job_id}", response_model=KiwoomResponse, summary="스케줄러 작업 상세 조회")
async def get_job(
    job_id: int,
    service: SchedulerService = Depends(get_scheduler_service)
):
    """특정 스케줄러 작업의 상세 정보를 조회합니다."""
    logger.info(f"스케줄러 작업 상세 조회 요청: job_id={job_id}")
    try:
        job = await service.get_job_by_id(job_id)
        if not job:
            logger.warning(f"존재하지 않는 작업: job_id={job_id}")
            return KiwoomApiHelper.create_error_response(
                error_code="JOB_NOT_FOUND",
                error_message=f"작업을 찾을 수 없습니다: ID {job_id}"
            )
        
        job_data = {
            "id": job.id,
            "name": job.name,
            "func_name": job.func_name,
            "schedule_type": job.schedule_type,
            "schedule_expr": job.schedule_expr,
            "timezone": job.timezone,
            "enabled": job.enabled,
            "max_conc": job.max_conc,
            "overlap_policy": job.overlap_policy,
            "timeout_sec": job.timeout_sec,
            "retry_max": job.retry_max,
            "retry_backoff": job.retry_backoff,
            "jitter_sec": job.jitter_sec,
            "next_run_at": job.next_run_at,
            "last_run_at": job.last_run_at,
            "created_at": job.created_at,
            "updated_at": job.updated_at
        }
        
        logger.info(f"스케줄러 작업 상세 조회 완료: {job.name}")
        return KiwoomApiHelper.create_success_response(data=job_data)
        
    except Exception as e:
        logger.error(f"스케줄러 작업 상세 조회 실패: {e}")
        return KiwoomApiHelper.create_error_response(
            error_code="JOB_GET_ERROR",
            error_message=str(e)
        )

@router.put("/jobs/{job_id}", response_model=KiwoomResponse, summary="스케줄러 작업 수정")
async def update_job(
    job_id: int,
    job_update: SchedulerJobUpdate,
    service: SchedulerService = Depends(get_scheduler_service)
):
    """스케줄러 작업을 수정합니다."""
    logger.info(f"스케줄러 작업 수정 요청: job_id={job_id}")
    try:
        # 작업 존재 여부 확인
        existing_job = await service.get_job_by_id(job_id)
        if not existing_job:
            logger.warning(f"존재하지 않는 작업: job_id={job_id}")
            return KiwoomApiHelper.create_error_response(
                error_code="JOB_NOT_FOUND",
                error_message=f"작업을 찾을 수 없습니다: ID {job_id}"
            )
        
        # 이름 중복 확인 (이름을 변경하는 경우)
        if job_update.name and job_update.name != existing_job.name:
            duplicate_job = await service.get_job_by_name(job_update.name)
            if duplicate_job:
                logger.warning(f"이미 존재하는 작업명: {job_update.name}")
                return KiwoomApiHelper.create_error_response(
                    error_code="DUPLICATE_JOB_NAME",
                    error_message=f"작업명 '{job_update.name}'이 이미 존재합니다."
                )
        
        updated_job = await service.update_job(job_id, job_update)
        if not updated_job:
            logger.error(f"작업 수정 실패: job_id={job_id}")
            return KiwoomApiHelper.create_error_response(
                error_code="JOB_UPDATE_ERROR",
                error_message="작업 수정에 실패했습니다."
            )
        
        logger.info(f"스케줄러 작업 수정 완료: {updated_job.name}")
        return KiwoomApiHelper.create_success_response(data={
            "id": updated_job.id,
            "name": updated_job.name,
            "func_name": updated_job.func_name,
            "enabled": updated_job.enabled,
            "updated_at": updated_job.updated_at
        })
        
    except Exception as e:
        logger.error(f"스케줄러 작업 수정 실패: {e}")
        return KiwoomApiHelper.create_error_response(
            error_code="JOB_UPDATE_ERROR",
            error_message=str(e)
        )

@router.delete("/jobs/{job_id}", response_model=KiwoomResponse, summary="스케줄러 작업 삭제")
async def delete_job(
    job_id: int,
    service: SchedulerService = Depends(get_scheduler_service)
):
    """스케줄러 작업을 삭제합니다."""
    logger.info(f"스케줄러 작업 삭제 요청: job_id={job_id}")
    try:
        # 작업 존재 여부 확인
        existing_job = await service.get_job_by_id(job_id)
        if not existing_job:
            logger.warning(f"존재하지 않는 작업: job_id={job_id}")
            return KiwoomApiHelper.create_error_response(
                error_code="JOB_NOT_FOUND",
                error_message=f"작업을 찾을 수 없습니다: ID {job_id}"
            )
        
        success = await service.delete_job(job_id)
        if not success:
            logger.error(f"작업 삭제 실패: job_id={job_id}")
            return KiwoomApiHelper.create_error_response(
                error_code="JOB_DELETE_ERROR",
                error_message="작업 삭제에 실패했습니다."
            )
        
        logger.info(f"스케줄러 작업 삭제 완료: {existing_job.name}")
        return KiwoomApiHelper.create_success_response(data={
            "id": job_id,
            "name": existing_job.name,
            "deleted": True
        })
        
    except Exception as e:
        logger.error(f"스케줄러 작업 삭제 실패: {e}")
        return KiwoomApiHelper.create_error_response(
            error_code="JOB_DELETE_ERROR",
            error_message=str(e)
        )

@router.post("/jobs/{job_id}/enable", response_model=KiwoomResponse, summary="스케줄러 작업 활성화")
async def enable_job(
    job_id: int,
    service: SchedulerService = Depends(get_scheduler_service)
):
    """스케줄러 작업을 활성화합니다."""
    logger.info(f"스케줄러 작업 활성화 요청: job_id={job_id}")
    try:
        job_update = SchedulerJobUpdate(enabled=1)
        updated_job = await service.update_job(job_id, job_update)
        
        if not updated_job:
            return KiwoomApiHelper.create_error_response(
                error_code="JOB_NOT_FOUND",
                error_message=f"작업을 찾을 수 없습니다: ID {job_id}"
            )
        
        logger.info(f"스케줄러 작업 활성화 완료: {updated_job.name}")
        return KiwoomApiHelper.create_success_response(data={
            "id": job_id,
            "name": updated_job.name,
            "enabled": updated_job.enabled
        })
        
    except Exception as e:
        logger.error(f"스케줄러 작업 활성화 실패: {e}")
        return KiwoomApiHelper.create_error_response(
            error_code="JOB_ENABLE_ERROR",
            error_message=str(e)
        )

@router.post("/jobs/{job_id}/disable", response_model=KiwoomResponse, summary="스케줄러 작업 비활성화")
async def disable_job(
    job_id: int,
    service: SchedulerService = Depends(get_scheduler_service)
):
    """스케줄러 작업을 비활성화합니다."""
    logger.info(f"스케줄러 작업 비활성화 요청: job_id={job_id}")
    try:
        job_update = SchedulerJobUpdate(enabled=0)
        updated_job = await service.update_job(job_id, job_update)
        
        if not updated_job:
            return KiwoomApiHelper.create_error_response(
                error_code="JOB_NOT_FOUND",
                error_message=f"작업을 찾을 수 없습니다: ID {job_id}"
            )
        
        logger.info(f"스케줄러 작업 비활성화 완료: {updated_job.name}")
        return KiwoomApiHelper.create_success_response(data={
            "id": job_id,
            "name": updated_job.name,
            "enabled": updated_job.enabled
        })
        
    except Exception as e:
        logger.error(f"스케줄러 작업 비활성화 실패: {e}")
        return KiwoomApiHelper.create_error_response(
            error_code="JOB_DISABLE_ERROR",
            error_message=str(e)
        )

# === 스케줄러 실행 이력 API ===

@router.get("/history", response_model=KiwoomResponse, summary="스케줄러 실행 이력 조회")
async def get_run_history(
    job_name: Optional[str] = Query(None, description="특정 작업명 필터"),
    status: Optional[str] = Query(None, description="실행 상태 필터"),
    started_after: Optional[str] = Query(None, description="시작 시각 이후 필터 (ISO8601)"),
    started_before: Optional[str] = Query(None, description="시작 시각 이전 필터 (ISO8601)"),
    limit: int = Query(100, description="조회할 최대 개수"),
    service: SchedulerService = Depends(get_scheduler_service)
):
    """스케줄러 실행 이력을 조회합니다."""
    logger.info(f"스케줄러 실행 이력 조회 요청: job_name={job_name}, status={status}, limit={limit}")
    try:
        # 필터 객체 생성
        filters = SchedulerRunHistoryFilter(
            job_name=job_name,
            status=status,
            started_after=started_after,
            started_before=started_before
        ) if any([job_name, status, started_after, started_before]) else None
        
        history_list = await service.get_run_history(filters, limit)
        
        # 응답 데이터 변환
        history_data = []
        for history in history_list:
            history_data.append({
                "id": history.id,
                "job_name": history.job_name,
                "started_at": history.started_at,
                "finished_at": history.finished_at,
                "status": history.status,
                "message": history.message
            })
        
        logger.info(f"스케줄러 실행 이력 조회 완료: {len(history_data)}개")
        return KiwoomApiHelper.create_success_response(data={
            "history": history_data,
            "count": len(history_data)
        })
        
    except Exception as e:
        logger.error(f"스케줄러 실행 이력 조회 실패: {e}")
        return KiwoomApiHelper.create_error_response(
            error_code="HISTORY_GET_ERROR",
            error_message=str(e)
        )

@router.delete("/history/cleanup", response_model=KiwoomResponse, summary="오래된 실행 이력 정리")
async def cleanup_old_history(
    days: int = Query(30, description="보관할 일수 (기본: 30일)"),
    service: SchedulerService = Depends(get_scheduler_service)
):
    """오래된 스케줄러 실행 이력을 정리합니다."""
    logger.info(f"스케줄러 실행 이력 정리 요청: {days}일 전 이력 삭제")
    try:
        deleted_count = await service.cleanup_old_history(days)
        
        logger.info(f"스케줄러 실행 이력 정리 완료: {deleted_count}개 삭제")
        return KiwoomApiHelper.create_success_response(data={
            "deleted_count": deleted_count,
            "cleanup_days": days
        })
        
    except Exception as e:
        logger.error(f"스케줄러 실행 이력 정리 실패: {e}")
        return KiwoomApiHelper.create_error_response(
            error_code="HISTORY_CLEANUP_ERROR",
            error_message=str(e)
        )

# === 스케줄러 락 관리 API ===

@router.post("/locks", response_model=KiwoomResponse, summary="락 획득")
async def acquire_lock(
    lock: SchedulerLockCreate,
    service: SchedulerService = Depends(get_scheduler_service)
):
    """분산 락을 획득합니다."""
    logger.info(f"락 획득 요청: {lock.lock_key} by {lock.holder}")
    try:
        success = await service.acquire_lock(lock)
        
        if success:
            logger.info(f"락 획득 성공: {lock.lock_key}")
            return KiwoomApiHelper.create_success_response(data={
                "lock_key": lock.lock_key,
                "holder": lock.holder,
                "acquired": True
            })
        else:
            logger.warning(f"락 획득 실패 (이미 존재): {lock.lock_key}")
            return KiwoomApiHelper.create_error_response(
                error_code="LOCK_ALREADY_EXISTS",
                error_message=f"락이 이미 존재합니다: {lock.lock_key}"
            )
        
    except Exception as e:
        logger.error(f"락 획득 실패: {e}")
        return KiwoomApiHelper.create_error_response(
            error_code="LOCK_ACQUIRE_ERROR",
            error_message=str(e)
        )

@router.delete("/locks/{lock_key}", response_model=KiwoomResponse, summary="락 해제")
async def release_lock(
    lock_key: str,
    holder: str = Query(..., description="락 소유자"),
    service: SchedulerService = Depends(get_scheduler_service)
):
    """분산 락을 해제합니다."""
    logger.info(f"락 해제 요청: {lock_key} by {holder}")
    try:
        success = await service.release_lock(lock_key, holder)
        
        if success:
            logger.info(f"락 해제 성공: {lock_key}")
            return KiwoomApiHelper.create_success_response(data={
                "lock_key": lock_key,
                "holder": holder,
                "released": True
            })
        else:
            logger.warning(f"락 해제 실패: {lock_key} (락을 소유하지 않음)")
            return KiwoomApiHelper.create_error_response(
                error_code="LOCK_NOT_OWNED",
                error_message=f"락을 소유하지 않습니다: {lock_key}"
            )
        
    except Exception as e:
        logger.error(f"락 해제 실패: {e}")
        return KiwoomApiHelper.create_error_response(
            error_code="LOCK_RELEASE_ERROR",
            error_message=str(e)
        )

@router.get("/locks/{lock_key}", response_model=KiwoomResponse, summary="락 상태 조회")
async def get_lock(
    lock_key: str,
    service: SchedulerService = Depends(get_scheduler_service)
):
    """특정 락의 상태를 조회합니다."""
    logger.info(f"락 상태 조회 요청: {lock_key}")
    try:
        lock = await service.get_lock(lock_key)
        
        if lock:
            logger.info(f"락 상태 조회 성공: {lock_key}")
            return KiwoomApiHelper.create_success_response(data={
                "lock_key": lock.lock_key,
                "holder": lock.holder,
                "acquired_at": lock.acquired_at,
                "exists": True
            })
        else:
            logger.info(f"락이 존재하지 않음: {lock_key}")
            return KiwoomApiHelper.create_success_response(data={
                "lock_key": lock_key,
                "exists": False
            })
        
    except Exception as e:
        logger.error(f"락 상태 조회 실패: {e}")
        return KiwoomApiHelper.create_error_response(
            error_code="LOCK_GET_ERROR",
            error_message=str(e)
        )

@router.delete("/locks/cleanup", response_model=KiwoomResponse, summary="만료된 락 정리")
async def cleanup_expired_locks(
    timeout_minutes: int = Query(60, description="락 만료 시간 (분, 기본: 60분)"),
    service: SchedulerService = Depends(get_scheduler_service)
):
    """만료된 락들을 정리합니다."""
    logger.info(f"만료된 락 정리 요청: {timeout_minutes}분 전 락 삭제")
    try:
        deleted_count = await service.cleanup_expired_locks(timeout_minutes)
        
        logger.info(f"만료된 락 정리 완료: {deleted_count}개 삭제")
        return KiwoomApiHelper.create_success_response(data={
            "deleted_count": deleted_count,
            "timeout_minutes": timeout_minutes
        })
        
    except Exception as e:
        logger.error(f"만료된 락 정리 실패: {e}")
        return KiwoomApiHelper.create_error_response(
            error_code="LOCK_CLEANUP_ERROR",
            error_message=str(e)
        )

# === 스케줄러 통계 API ===

@router.get("/statistics", response_model=KiwoomResponse, summary="스케줄러 통계 정보")
async def get_statistics(
    service: SchedulerService = Depends(get_scheduler_service)
):
    """스케줄러 시스템의 통계 정보를 조회합니다."""
    logger.info("스케줄러 통계 정보 조회 요청")
    try:
        stats = await service.get_job_statistics()
        
        logger.info("스케줄러 통계 정보 조회 완료")
        return KiwoomApiHelper.create_success_response(data=stats)
        
    except Exception as e:
        logger.error(f"스케줄러 통계 정보 조회 실패: {e}")
        return KiwoomApiHelper.create_error_response(
            error_code="STATISTICS_ERROR",
            error_message=str(e)
        )
