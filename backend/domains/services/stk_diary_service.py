from backend.core.config import config
from backend.domains.models.stk_diary_model import StkDiary, StkDiaryCreate, StkDiaryUpdate, StkDiaryFilter
from backend.core.logger import get_logger
from typing import List, Optional, Dict
import sqlite3
from datetime import datetime

logger = get_logger(__name__)

class StkDiaryService:
    """주식 일지 서비스 클래스
    
    종목에 대한 생각, 분석, 메모를 관리하는 서비스
    """
    
    def __init__(self):
        self.db_path = config.DB_PATH

    def _get_conn(self):
        """DB 연결 객체 반환"""
        return sqlite3.connect(self.db_path)

    def _row_to_diary(self, row) -> StkDiary:
        """DB row를 StkDiary 객체로 변환"""
        return StkDiary(
            id=row[0],
            ymd=row[1],
            stk_cd=row[2],
            note=row[3],
            created_at=row[4],
            updated_at=row[5]
        )

    async def create(self, diary_data: StkDiaryCreate) -> StkDiary:
        """새로운 일지 생성"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._create_sync, diary_data)

    def _create_sync(self, diary_data: StkDiaryCreate) -> StkDiary:
        with self._get_conn() as conn:
            cur = conn.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            cur.execute("""
                INSERT INTO stk_diary (ymd, stk_cd, note, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?)
            """, (
                diary_data.ymd,
                diary_data.stk_cd,
                diary_data.note,
                now,
                now
            ))
            conn.commit()
            
            # 생성된 ID 조회
            diary_id = cur.lastrowid
            return StkDiary(
                id=diary_id,
                ymd=diary_data.ymd,
                stk_cd=diary_data.stk_cd,
                note=diary_data.note,
                created_at=now,
                updated_at=now
            )

    async def get_by_id(self, diary_id: int) -> Optional[StkDiary]:
        """ID로 일지 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_by_id_sync, diary_id)

    def _get_by_id_sync(self, diary_id: int) -> Optional[StkDiary]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT id, ymd, stk_cd, note, created_at, updated_at
                FROM stk_diary
                WHERE id = ?
            """, (diary_id,))
            
            row = cur.fetchone()
            if row:
                return self._row_to_diary(row)
            return None

    async def update(self, diary_id: int, update_data: StkDiaryUpdate) -> Optional[StkDiary]:
        """일지 수정"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._update_sync, diary_id, update_data)

    def _update_sync(self, diary_id: int, update_data: StkDiaryUpdate) -> Optional[StkDiary]:
        # 기존 데이터 확인
        existing = self._get_by_id_sync(diary_id)
        if not existing:
            return None

        # 업데이트할 필드들만 추출
        update_fields = {}
        if update_data.ymd is not None:
            update_fields['ymd'] = update_data.ymd
        if update_data.stk_cd is not None:
            update_fields['stk_cd'] = update_data.stk_cd
        if update_data.note is not None:
            update_fields['note'] = update_data.note

        if not update_fields:
            return existing

        # SQL 쿼리 동적 생성
        set_clause = ', '.join([f"{field} = ?" for field in update_fields.keys()])
        update_fields['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        set_clause += ', updated_at = ?'

        with self._get_conn() as conn:
            cur = conn.cursor()
            values = list(update_fields.values()) + [diary_id]
            cur.execute(f"""
                UPDATE stk_diary 
                SET {set_clause}
                WHERE id = ?
            """, values)
            conn.commit()

        # 업데이트된 데이터 반환
        return self._get_by_id_sync(diary_id)

    async def delete(self, diary_id: int) -> bool:
        """일지 삭제"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._delete_sync, diary_id)

    def _delete_sync(self, diary_id: int) -> bool:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM stk_diary WHERE id = ?", (diary_id,))
            conn.commit()
            return cur.rowcount > 0

    async def list_all(self, filter_data: Optional[StkDiaryFilter] = None) -> List[StkDiary]:
        """모든 일지 목록 조회 (필터링 포함)"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._list_all_sync, filter_data)

    def _list_all_sync(self, filter_data: Optional[StkDiaryFilter] = None) -> List[StkDiary]:
        query = """
            SELECT id, ymd, stk_cd, note, created_at, updated_at
            FROM stk_diary
        """
        params = []
        conditions = []

        if filter_data:
            if filter_data.ymd_from is not None:
                conditions.append("ymd >= ?")
                params.append(filter_data.ymd_from)
            
            if filter_data.ymd_to is not None:
                conditions.append("ymd <= ?")
                params.append(filter_data.ymd_to)
            
            if filter_data.stk_cd is not None:
                conditions.append("stk_cd = ?")
                params.append(filter_data.stk_cd)
            
            if filter_data.note_like is not None:
                conditions.append("note LIKE ?")
                params.append(f"%{filter_data.note_like}%")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        query += " ORDER BY ymd DESC, id DESC"

        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            rows = cur.fetchall()
            
            return [self._row_to_diary(row) for row in rows]

    async def get_by_date(self, ymd: str) -> List[StkDiary]:
        """특정 날짜의 일지 목록"""
        filter_data = StkDiaryFilter(ymd_from=ymd, ymd_to=ymd)
        return await self.list_all(filter_data)

    async def get_by_stock(self, stk_cd: str) -> List[StkDiary]:
        """특정 종목의 일지 목록"""
        filter_data = StkDiaryFilter(stk_cd=stk_cd)
        return await self.list_all(filter_data)

    async def search_by_content(self, keyword: str) -> List[StkDiary]:
        """내용으로 일지 검색"""
        filter_data = StkDiaryFilter(note_like=keyword)
        return await self.list_all(filter_data)

    async def get_date_range(self, start_date: str, end_date: str) -> List[StkDiary]:
        """날짜 범위로 일지 조회"""
        filter_data = StkDiaryFilter(ymd_from=start_date, ymd_to=end_date)
        return await self.list_all(filter_data)

    async def get_stats(self) -> Dict[str, int]:
        """일지 통계 정보"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_stats_sync)

    def _get_stats_sync(self) -> Dict[str, int]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            # 전체 일지 수
            cur.execute("SELECT COUNT(*) FROM stk_diary")
            total = cur.fetchone()[0]
            
            # 종목별 일지 수 (종목코드가 있는 것)
            cur.execute("SELECT COUNT(*) FROM stk_diary WHERE stk_cd IS NOT NULL")
            with_stock = cur.fetchone()[0]
            
            # 전체 시장 일지 수 (종목코드가 없는 것)
            cur.execute("SELECT COUNT(*) FROM stk_diary WHERE stk_cd IS NULL")
            general = cur.fetchone()[0]
            
            return {
                'total': total or 0,
                'with_stock': with_stock or 0,
                'general': general or 0
            }


#---------------------------------------------------------
# StkDiaryService의 싱글턴 인스턴스를 관리하기 위한 전역 변수와 getter 함수
# instance_stk_diary_service: StkDiaryService = None

# def get_stk_diary_service() -> StkDiaryService:
#     """StkDiaryService 싱글턴 인스턴스 반환"""
#     global instance_stk_diary_service
#     if instance_stk_diary_service is None:
#         instance_stk_diary_service = StkDiaryService()
#     return instance_stk_diary_service
