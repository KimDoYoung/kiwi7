from backend.core.config import config
from backend.domains.models.scheduler_model import (
    SchedulerJob, SchedulerRunHistory, SchedulerLock,
    SchedulerJobCreate, SchedulerJobUpdate, SchedulerJobFilter,
    SchedulerRunHistoryCreate, SchedulerRunHistoryFilter,
    SchedulerLockCreate
)
from backend.core.logger import get_logger
from typing import List, Optional, Dict
import sqlite3
from datetime import datetime

logger = get_logger(__name__)

class SchedulerService:
    """스케줄러 관련 서비스 클래스
    
    kscheduler_job, kscheduler_run_history, kscheduler_lock 테이블을 관리하는 서비스
    - 작업 정의 CRUD
    - 실행 이력 관리
    - 분산 락 관리
    """
    
    def __init__(self):
        self.db_path = config.DB_PATH

    def _get_conn(self):
        """데이터베이스 연결 반환"""
        return sqlite3.connect(self.db_path)

    # === SchedulerJob 관련 메서드 ===
    
    def _row_to_scheduler_job(self, row) -> SchedulerJob:
        """DB row를 SchedulerJob 객체로 변환"""
        return SchedulerJob(
            id=row[0],
            name=row[1],
            func_name=row[2],
            schedule_type=row[3],
            schedule_expr=row[4],
            timezone=row[5],
            enabled=row[6],
            max_conc=row[7],
            overlap_policy=row[8],
            timeout_sec=row[9],
            retry_max=row[10],
            retry_backoff=row[11],
            jitter_sec=row[12],
            next_run_at=row[13],
            last_run_at=row[14],
            created_at=row[15],
            updated_at=row[16]
        )

    async def create_job(self, job: SchedulerJobCreate) -> SchedulerJob:
        """새로운 스케줄러 작업 생성"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._create_job_sync, job)

    def _create_job_sync(self, job: SchedulerJobCreate) -> SchedulerJob:
        """새로운 스케줄러 작업 생성 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            now = datetime.now().isoformat()
            
            cur.execute("""
                INSERT INTO kscheduler_job (
                    name, func_name, schedule_type, schedule_expr, timezone,
                    enabled, max_conc, overlap_policy, timeout_sec, retry_max,
                    retry_backoff, jitter_sec, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                job.name, job.func_name, job.schedule_type, job.schedule_expr, job.timezone,
                job.enabled, job.max_conc, job.overlap_policy, job.timeout_sec, job.retry_max,
                job.retry_backoff, job.jitter_sec, now, now
            ))
            
            job_id = cur.lastrowid
            logger.info(f"스케줄러 작업 생성됨: {job.name} (ID: {job_id})")
            
            # 생성된 작업 조회 후 반환
            return self._get_job_by_id_sync(job_id)

    async def get_job_by_id(self, job_id: int) -> Optional[SchedulerJob]:
        """ID로 스케줄러 작업 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_job_by_id_sync, job_id)

    def _get_job_by_id_sync(self, job_id: int) -> Optional[SchedulerJob]:
        """ID로 스케줄러 작업 조회 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT id, name, func_name, schedule_type, schedule_expr, timezone,
                       enabled, max_conc, overlap_policy, timeout_sec, retry_max,
                       retry_backoff, jitter_sec, next_run_at, last_run_at,
                       created_at, updated_at
                FROM kscheduler_job WHERE id = ?
            """, (job_id,))
            
            row = cur.fetchone()
            if row:
                return self._row_to_scheduler_job(row)
            return None

    async def get_job_by_name(self, name: str) -> Optional[SchedulerJob]:
        """이름으로 스케줄러 작업 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_job_by_name_sync, name)

    def _get_job_by_name_sync(self, name: str) -> Optional[SchedulerJob]:
        """이름으로 스케줄러 작업 조회 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT id, name, func_name, schedule_type, schedule_expr, timezone,
                       enabled, max_conc, overlap_policy, timeout_sec, retry_max,
                       retry_backoff, jitter_sec, next_run_at, last_run_at,
                       created_at, updated_at
                FROM kscheduler_job WHERE name = ?
            """, (name,))
            
            row = cur.fetchone()
            if row:
                return self._row_to_scheduler_job(row)
            return None

    async def get_all_jobs(self, filters: Optional[SchedulerJobFilter] = None) -> List[SchedulerJob]:
        """모든 스케줄러 작업 조회 (필터링 가능)"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_all_jobs_sync, filters)

    def _get_all_jobs_sync(self, filters: Optional[SchedulerJobFilter] = None) -> List[SchedulerJob]:
        """모든 스케줄러 작업 조회 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            # 기본 쿼리
            query = """
                SELECT id, name, func_name, schedule_type, schedule_expr, timezone,
                       enabled, max_conc, overlap_policy, timeout_sec, retry_max,
                       retry_backoff, jitter_sec, next_run_at, last_run_at,
                       created_at, updated_at
                FROM kscheduler_job
            """
            params = []
            where_conditions = []
            
            # 필터 조건 추가
            if filters:
                if filters.enabled is not None:
                    where_conditions.append("enabled = ?")
                    params.append(filters.enabled)
                
                if filters.schedule_type:
                    where_conditions.append("schedule_type = ?")
                    params.append(filters.schedule_type)
                
                if filters.func_name_like:
                    where_conditions.append("func_name LIKE ?")
                    params.append(f"%{filters.func_name_like}%")
                
                if filters.name_like:
                    where_conditions.append("name LIKE ?")
                    params.append(f"%{filters.name_like}%")
            
            if where_conditions:
                query += " WHERE " + " AND ".join(where_conditions)
            
            query += " ORDER BY created_at DESC"
            
            cur.execute(query, params)
            rows = cur.fetchall()
            
            return [self._row_to_scheduler_job(row) for row in rows]

    async def update_job(self, job_id: int, job_update: SchedulerJobUpdate) -> Optional[SchedulerJob]:
        """스케줄러 작업 수정"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._update_job_sync, job_id, job_update)

    def _update_job_sync(self, job_id: int, job_update: SchedulerJobUpdate) -> Optional[SchedulerJob]:
        """스케줄러 작업 수정 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            # 수정할 필드와 값 준비
            update_fields = []
            params = []
            
            for field, value in job_update.model_dump(exclude_unset=True).items():
                if value is not None:
                    update_fields.append(f"{field} = ?")
                    params.append(value)
            
            if not update_fields:
                logger.warning(f"수정할 필드가 없음: job_id={job_id}")
                return self._get_job_by_id_sync(job_id)
            
            # updated_at 추가
            update_fields.append("updated_at = ?")
            params.append(datetime.now().isoformat())
            params.append(job_id)
            
            query = f"UPDATE kscheduler_job SET {', '.join(update_fields)} WHERE id = ?"
            cur.execute(query, params)
            
            if cur.rowcount > 0:
                logger.info(f"스케줄러 작업 수정됨: job_id={job_id}")
                return self._get_job_by_id_sync(job_id)
            else:
                logger.warning(f"수정할 작업을 찾을 수 없음: job_id={job_id}")
                return None

    async def delete_job(self, job_id: int) -> bool:
        """스케줄러 작업 삭제"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._delete_job_sync, job_id)

    def _delete_job_sync(self, job_id: int) -> bool:
        """스케줄러 작업 삭제 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM kscheduler_job WHERE id = ?", (job_id,))
            
            if cur.rowcount > 0:
                logger.info(f"스케줄러 작업 삭제됨: job_id={job_id}")
                return True
            else:
                logger.warning(f"삭제할 작업을 찾을 수 없음: job_id={job_id}")
                return False

    async def update_job_runtime(self, job_id: int, next_run_at: Optional[str] = None, last_run_at: Optional[str] = None) -> bool:
        """작업의 실행 시간 정보 업데이트"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._update_job_runtime_sync, job_id, next_run_at, last_run_at)

    def _update_job_runtime_sync(self, job_id: int, next_run_at: Optional[str] = None, last_run_at: Optional[str] = None) -> bool:
        """작업의 실행 시간 정보 업데이트 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            update_fields = []
            params = []
            
            if next_run_at is not None:
                update_fields.append("next_run_at = ?")
                params.append(next_run_at)
            
            if last_run_at is not None:
                update_fields.append("last_run_at = ?")
                params.append(last_run_at)
            
            if not update_fields:
                return False
            
            update_fields.append("updated_at = ?")
            params.append(datetime.now().isoformat())
            params.append(job_id)
            
            query = f"UPDATE kscheduler_job SET {', '.join(update_fields)} WHERE id = ?"
            cur.execute(query, params)
            
            return cur.rowcount > 0

    # === SchedulerRunHistory 관련 메서드 ===
    
    def _row_to_run_history(self, row) -> SchedulerRunHistory:
        """DB row를 SchedulerRunHistory 객체로 변환"""
        return SchedulerRunHistory(
            id=row[0],
            job_name=row[1],
            started_at=row[2],
            finished_at=row[3],
            status=row[4],
            message=row[5]
        )

    async def create_run_history(self, history: SchedulerRunHistoryCreate) -> SchedulerRunHistory:
        """새로운 실행 이력 생성"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._create_run_history_sync, history)

    def _create_run_history_sync(self, history: SchedulerRunHistoryCreate) -> SchedulerRunHistory:
        """새로운 실행 이력 생성 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            cur.execute("""
                INSERT INTO kscheduler_run_history (job_name, started_at, finished_at, status, message)
                VALUES (?, ?, ?, ?, ?)
            """, (
                history.job_name, history.started_at, history.finished_at, 
                history.status, history.message
            ))
            
            history_id = cur.lastrowid
            logger.debug(f"실행 이력 생성됨: {history.job_name} (ID: {history_id})")
            
            # 생성된 이력 조회 후 반환
            cur.execute("""
                SELECT id, job_name, started_at, finished_at, status, message
                FROM kscheduler_run_history WHERE id = ?
            """, (history_id,))
            
            row = cur.fetchone()
            return self._row_to_run_history(row)

    async def get_run_history(self, filters: Optional[SchedulerRunHistoryFilter] = None, limit: int = 100) -> List[SchedulerRunHistory]:
        """실행 이력 조회 (필터링 가능)"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_run_history_sync, filters, limit)

    def _get_run_history_sync(self, filters: Optional[SchedulerRunHistoryFilter] = None, limit: int = 100) -> List[SchedulerRunHistory]:
        """실행 이력 조회 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            query = """
                SELECT id, job_name, started_at, finished_at, status, message
                FROM kscheduler_run_history
            """
            params = []
            where_conditions = []
            
            # 필터 조건 추가
            if filters:
                if filters.job_name:
                    where_conditions.append("job_name = ?")
                    params.append(filters.job_name)
                
                if filters.status:
                    where_conditions.append("status = ?")
                    params.append(filters.status)
                
                if filters.started_after:
                    where_conditions.append("started_at >= ?")
                    params.append(filters.started_after)
                
                if filters.started_before:
                    where_conditions.append("started_at <= ?")
                    params.append(filters.started_before)
            
            if where_conditions:
                query += " WHERE " + " AND ".join(where_conditions)
            
            query += " ORDER BY started_at DESC LIMIT ?"
            params.append(limit)
            
            cur.execute(query, params)
            rows = cur.fetchall()
            
            return [self._row_to_run_history(row) for row in rows]

    async def update_run_history(self, history_id: int, finished_at: str, status: str, message: Optional[str] = None) -> bool:
        """실행 이력 업데이트 (완료 시점)"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._update_run_history_sync, history_id, finished_at, status, message)

    def _update_run_history_sync(self, history_id: int, finished_at: str, status: str, message: Optional[str] = None) -> bool:
        """실행 이력 업데이트 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            cur.execute("""
                UPDATE kscheduler_run_history 
                SET finished_at = ?, status = ?, message = ?
                WHERE id = ?
            """, (finished_at, status, message, history_id))
            
            return cur.rowcount > 0

    async def cleanup_old_history(self, days: int = 30) -> int:
        """오래된 실행 이력 정리"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._cleanup_old_history_sync, days)

    def _cleanup_old_history_sync(self, days: int = 30) -> int:
        """오래된 실행 이력 정리 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            cutoff_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            cutoff_date = cutoff_date.timestamp() - (days * 24 * 60 * 60)
            cutoff_date_str = datetime.fromtimestamp(cutoff_date).isoformat()
            
            cur.execute("""
                DELETE FROM kscheduler_run_history 
                WHERE started_at < ?
            """, (cutoff_date_str,))
            
            deleted_count = cur.rowcount
            if deleted_count > 0:
                logger.info(f"오래된 실행 이력 {deleted_count}개 삭제됨 (기준: {days}일 전)")
            
            return deleted_count

    # === SchedulerLock 관련 메서드 ===
    
    def _row_to_scheduler_lock(self, row) -> SchedulerLock:
        """DB row를 SchedulerLock 객체로 변환"""
        return SchedulerLock(
            lock_key=row[0],
            holder=row[1],
            acquired_at=row[2]
        )

    async def acquire_lock(self, lock: SchedulerLockCreate) -> bool:
        """락 획득 시도"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._acquire_lock_sync, lock)

    def _acquire_lock_sync(self, lock: SchedulerLockCreate) -> bool:
        """락 획득 시도 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            try:
                cur.execute("""
                    INSERT INTO kscheduler_lock (lock_key, holder, acquired_at)
                    VALUES (?, ?, ?)
                """, (lock.lock_key, lock.holder, datetime.now().isoformat()))
                
                logger.debug(f"락 획득 성공: {lock.lock_key} by {lock.holder}")
                return True
            except sqlite3.IntegrityError:
                # 이미 락이 존재함
                logger.debug(f"락 획득 실패 (이미 존재): {lock.lock_key}")
                return False

    async def release_lock(self, lock_key: str, holder: str) -> bool:
        """락 해제"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._release_lock_sync, lock_key, holder)

    def _release_lock_sync(self, lock_key: str, holder: str) -> bool:
        """락 해제 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            cur.execute("""
                DELETE FROM kscheduler_lock 
                WHERE lock_key = ? AND holder = ?
            """, (lock_key, holder))
            
            if cur.rowcount > 0:
                logger.debug(f"락 해제 성공: {lock_key} by {holder}")
                return True
            else:
                logger.debug(f"락 해제 실패: {lock_key} (락을 소유하지 않음)")
                return False

    async def get_lock(self, lock_key: str) -> Optional[SchedulerLock]:
        """락 정보 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_lock_sync, lock_key)

    def _get_lock_sync(self, lock_key: str) -> Optional[SchedulerLock]:
        """락 정보 조회 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            cur.execute("""
                SELECT lock_key, holder, acquired_at
                FROM kscheduler_lock WHERE lock_key = ?
            """, (lock_key,))
            
            row = cur.fetchone()
            if row:
                return self._row_to_scheduler_lock(row)
            return None

    async def cleanup_expired_locks(self, timeout_minutes: int = 60) -> int:
        """만료된 락 정리"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._cleanup_expired_locks_sync, timeout_minutes)

    def _cleanup_expired_locks_sync(self, timeout_minutes: int = 60) -> int:
        """만료된 락 정리 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            cutoff_time = datetime.now().timestamp() - (timeout_minutes * 60)
            cutoff_time_str = datetime.fromtimestamp(cutoff_time).isoformat()
            
            cur.execute("""
                DELETE FROM kscheduler_lock 
                WHERE acquired_at < ?
            """, (cutoff_time_str,))
            
            deleted_count = cur.rowcount
            if deleted_count > 0:
                logger.info(f"만료된 락 {deleted_count}개 정리됨 (기준: {timeout_minutes}분 전)")
            
            return deleted_count

    # === 유틸리티 메서드 ===
    
    async def get_job_statistics(self) -> Dict[str, int]:
        """작업 통계 정보 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_job_statistics_sync)

    def _get_job_statistics_sync(self) -> Dict[str, int]:
        """작업 통계 정보 조회 (동기)"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            stats = {}
            
            # 전체 작업 수
            cur.execute("SELECT COUNT(*) FROM kscheduler_job")
            stats['total_jobs'] = cur.fetchone()[0]
            
            # 활성화된 작업 수
            cur.execute("SELECT COUNT(*) FROM kscheduler_job WHERE enabled = 1")
            stats['enabled_jobs'] = cur.fetchone()[0]
            
            # 스케줄 타입별 작업 수
            cur.execute("""
                SELECT schedule_type, COUNT(*) 
                FROM kscheduler_job 
                GROUP BY schedule_type
            """)
            for row in cur.fetchall():
                stats[f'{row[0]}_jobs'] = row[1]
            
            # 최근 24시간 실행 횟수
            yesterday = datetime.now().timestamp() - (24 * 60 * 60)
            yesterday_str = datetime.fromtimestamp(yesterday).isoformat()
            cur.execute("""
                SELECT COUNT(*) FROM kscheduler_run_history 
                WHERE started_at >= ?
            """, (yesterday_str,))
            stats['runs_24h'] = cur.fetchone()[0]
            
            # 활성 락 수
            cur.execute("SELECT COUNT(*) FROM kscheduler_lock")
            stats['active_locks'] = cur.fetchone()[0]
            
            return stats
