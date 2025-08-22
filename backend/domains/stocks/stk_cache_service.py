from backend.core.config import config
from backend.domains.stocks.stk_cache_model import StkCache, StkCacheCreate, StkCacheUpdate, StkCacheFilter
from backend.core.logger import get_logger
from typing import List, Optional, Dict
import sqlite3
from datetime import datetime

logger = get_logger(__name__)

class StkCacheService:
    """주식 캐시 서비스 클래스
    
    종목에 대한 임시 데이터(전일종가, 시가, 거래량 등)를 관리하는 서비스
    """
    
    def __init__(self):
        self.db_path = config.DB_PATH

    def _get_conn(self):
        """DB 연결 객체 반환"""
        return sqlite3.connect(self.db_path)

    def _row_to_cache(self, row) -> StkCache:
        """DB row를 StkCache 객체로 변환"""
        return StkCache(
            id=row[0],
            stk_cd=row[1],
            name=row[2],
            value=row[3],
            created_at=row[4]
        )

    async def create(self, cache_data: StkCacheCreate) -> StkCache:
        """새로운 캐시 데이터 생성"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._create_sync, cache_data)

    def _create_sync(self, cache_data: StkCacheCreate) -> StkCache:
        with self._get_conn() as conn:
            cur = conn.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            cur.execute("""
                INSERT INTO stk_cache (stk_cd, name, value, created_at)
                VALUES (?, ?, ?, ?)
            """, (
                cache_data.stk_cd,
                cache_data.name,
                cache_data.value,
                now
            ))
            conn.commit()
            
            # 생성된 ID 조회
            cache_id = cur.lastrowid
            return StkCache(
                id=cache_id,
                stk_cd=cache_data.stk_cd,
                name=cache_data.name,
                value=cache_data.value,
                created_at=now
            )

    async def get_by_id(self, cache_id: int) -> Optional[StkCache]:
        """ID로 캐시 데이터 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_by_id_sync, cache_id)

    def _get_by_id_sync(self, cache_id: int) -> Optional[StkCache]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT id, stk_cd, name, value, created_at
                FROM stk_cache
                WHERE id = ?
            """, (cache_id,))
            
            row = cur.fetchone()
            if row:
                return self._row_to_cache(row)
            return None

    async def get_by_stock_and_name(self, stk_cd: str, name: str) -> Optional[StkCache]:
        """종목코드와 캐시명으로 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_by_stock_and_name_sync, stk_cd, name)

    def _get_by_stock_and_name_sync(self, stk_cd: str, name: str) -> Optional[StkCache]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT id, stk_cd, name, value, created_at
                FROM stk_cache
                WHERE stk_cd = ? AND name = ?
                ORDER BY created_at DESC
                LIMIT 1
            """, (stk_cd, name))
            
            row = cur.fetchone()
            if row:
                return self._row_to_cache(row)
            return None

    async def update(self, cache_id: int, update_data: StkCacheUpdate) -> Optional[StkCache]:
        """캐시 데이터 수정"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._update_sync, cache_id, update_data)

    def _update_sync(self, cache_id: int, update_data: StkCacheUpdate) -> Optional[StkCache]:
        # 기존 데이터 확인
        existing = self._get_by_id_sync(cache_id)
        if not existing:
            return None

        # 업데이트할 필드들만 추출
        update_fields = {}
        if update_data.stk_cd is not None:
            update_fields['stk_cd'] = update_data.stk_cd
        if update_data.name is not None:
            update_fields['name'] = update_data.name
        if update_data.value is not None:
            update_fields['value'] = update_data.value

        if not update_fields:
            return existing

        # SQL 쿼리 동적 생성
        set_clause = ', '.join([f"{field} = ?" for field in update_fields.keys()])

        with self._get_conn() as conn:
            cur = conn.cursor()
            values = list(update_fields.values()) + [cache_id]
            cur.execute(f"""
                UPDATE stk_cache 
                SET {set_clause}
                WHERE id = ?
            """, values)
            conn.commit()

        # 업데이트된 데이터 반환
        return self._get_by_id_sync(cache_id)

    async def delete(self, cache_id: int) -> bool:
        """캐시 데이터 삭제"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._delete_sync, cache_id)

    def _delete_sync(self, cache_id: int) -> bool:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM stk_cache WHERE id = ?", (cache_id,))
            conn.commit()
            return cur.rowcount > 0

    async def upsert(self, stk_cd: str, name: str, value: str) -> StkCache:
        """캐시 데이터 생성 또는 업데이트 (종목코드 + 캐시명 기준)"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._upsert_sync, stk_cd, name, value)

    def _upsert_sync(self, stk_cd: str, name: str, value: str) -> StkCache:
        # 기존 데이터 확인
        existing = self._get_by_stock_and_name_sync(stk_cd, name)
        
        if existing:
            # 업데이트
            update_data = StkCacheUpdate(value=value)
            return self._update_sync(existing.id, update_data)
        else:
            # 새로 생성
            create_data = StkCacheCreate(stk_cd=stk_cd, name=name, value=value)
            return self._create_sync(create_data)

    async def list_all(self, filter_data: Optional[StkCacheFilter] = None) -> List[StkCache]:
        """모든 캐시 데이터 목록 조회 (필터링 포함)"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._list_all_sync, filter_data)

    def _list_all_sync(self, filter_data: Optional[StkCacheFilter] = None) -> List[StkCache]:
        query = """
            SELECT id, stk_cd, name, value, created_at
            FROM stk_cache
        """
        params = []
        conditions = []

        if filter_data:
            if filter_data.stk_cd is not None:
                conditions.append("stk_cd = ?")
                params.append(filter_data.stk_cd)
            
            if filter_data.name is not None:
                conditions.append("name = ?")
                params.append(filter_data.name)
            
            if filter_data.name_like is not None:
                conditions.append("name LIKE ?")
                params.append(f"%{filter_data.name_like}%")
            
            if filter_data.value_like is not None:
                conditions.append("value LIKE ?")
                params.append(f"%{filter_data.value_like}%")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        query += " ORDER BY stk_cd, name, created_at DESC"

        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            rows = cur.fetchall()
            
            return [self._row_to_cache(row) for row in rows]

    async def get_by_stock(self, stk_cd: str) -> List[StkCache]:
        """특정 종목의 모든 캐시 데이터"""
        filter_data = StkCacheFilter(stk_cd=stk_cd)
        return await self.list_all(filter_data)

    async def get_by_name(self, name: str) -> List[StkCache]:
        """특정 캐시명의 모든 데이터"""
        filter_data = StkCacheFilter(name=name)
        return await self.list_all(filter_data)

    async def delete_by_stock(self, stk_cd: str) -> int:
        """특정 종목의 모든 캐시 데이터 삭제"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._delete_by_stock_sync, stk_cd)

    def _delete_by_stock_sync(self, stk_cd: str) -> int:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM stk_cache WHERE stk_cd = ?", (stk_cd,))
            conn.commit()
            return cur.rowcount

    async def delete_by_name(self, name: str) -> int:
        """특정 캐시명의 모든 데이터 삭제"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._delete_by_name_sync, name)

    def _delete_by_name_sync(self, name: str) -> int:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM stk_cache WHERE name = ?", (name,))
            conn.commit()
            return cur.rowcount

    async def get_cache_names(self) -> List[str]:
        """등록된 모든 캐시명 목록"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_cache_names_sync)

    def _get_cache_names_sync(self) -> List[str]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT DISTINCT name 
                FROM stk_cache 
                ORDER BY name
            """)
            rows = cur.fetchall()
            return [row[0] for row in rows]

    async def get_stock_codes(self) -> List[str]:
        """캐시된 모든 종목코드 목록"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_stock_codes_sync)

    def _get_stock_codes_sync(self) -> List[str]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT DISTINCT stk_cd 
                FROM stk_cache 
                ORDER BY stk_cd
            """)
            rows = cur.fetchall()
            return [row[0] for row in rows]

    async def get_stats(self) -> Dict[str, any]:
        """캐시 데이터 통계 정보"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_stats_sync)

    def _get_stats_sync(self) -> Dict[str, any]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            # 전체 캐시 데이터 수
            cur.execute("SELECT COUNT(*) FROM stk_cache")
            total = cur.fetchone()[0]
            
            # 고유 종목 수
            cur.execute("SELECT COUNT(DISTINCT stk_cd) FROM stk_cache")
            unique_stocks = cur.fetchone()[0]
            
            # 고유 캐시명 수
            cur.execute("SELECT COUNT(DISTINCT name) FROM stk_cache")
            unique_names = cur.fetchone()[0]
            
            return {
                'total_cache_entries': total or 0,
                'unique_stocks': unique_stocks or 0,
                'unique_cache_names': unique_names or 0
            }


#---------------------------------------------------------
# StkCacheService의 싱글턴 인스턴스를 관리하기 위한 전역 변수와 getter 함수
instance_stk_cache_service: StkCacheService = None

def get_stk_cache_service() -> StkCacheService:
    """StkCacheService 싱글턴 인스턴스 반환"""
    global instance_stk_cache_service
    if instance_stk_cache_service is None:
        instance_stk_cache_service = StkCacheService()
    return instance_stk_cache_service
