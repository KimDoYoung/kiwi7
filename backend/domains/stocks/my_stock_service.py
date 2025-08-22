from backend.core.config import config
from backend.domains.stocks.my_stock_model import MyStock, MyStockCreate, MyStockUpdate, MyStockFilter
from backend.core.logger import get_logger
from typing import List, Optional, Dict
import sqlite3
from datetime import datetime

logger = get_logger(__name__)

class MyStockService:
    def __init__(self):
        self.db_path = config.DB_PATH

    def _get_conn(self):
        return sqlite3.connect(self.db_path)

    def _row_to_mystock(self, row) -> MyStock:
        """DB row를 MyStock 객체로 변환"""
        return MyStock(
            stk_cd=row[0],
            stk_nm=row[1],
            sector=row[2],
            is_hold=row[3],
            is_watch=row[4],
            note=row[5],
            created_at=row[6],
            updated_at=row[7]
        )

    async def create(self, my_stock: MyStockCreate) -> MyStock:
        """새로운 종목 추가"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._create_sync, my_stock)

    def _create_sync(self, my_stock: MyStockCreate) -> MyStock:
        with self._get_conn() as conn:
            cur = conn.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            cur.execute("""
                INSERT INTO my_stock (stk_cd, stk_nm, sector, is_hold, is_watch, note, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                my_stock.stk_cd,
                my_stock.stk_nm,
                my_stock.sector,
                my_stock.is_hold,
                my_stock.is_watch,
                my_stock.note,
                now,
                now
            ))
            conn.commit()
            
            return MyStock(
                stk_cd=my_stock.stk_cd,
                stk_nm=my_stock.stk_nm,
                sector=my_stock.sector,
                is_hold=my_stock.is_hold,
                is_watch=my_stock.is_watch,
                note=my_stock.note,
                created_at=now,
                updated_at=now
            )

    async def get_by_code(self, stk_cd: str) -> Optional[MyStock]:
        """종목코드로 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_by_code_sync, stk_cd)

    def _get_by_code_sync(self, stk_cd: str) -> Optional[MyStock]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT stk_cd, stk_nm, sector, is_hold, is_watch, note, created_at, updated_at
                FROM my_stock
                WHERE stk_cd = ?
            """, (stk_cd,))
            
            row = cur.fetchone()
            if row:
                return self._row_to_mystock(row)
            return None

    async def update(self, stk_cd: str, update_data: MyStockUpdate) -> Optional[MyStock]:
        """종목 정보 수정"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._update_sync, stk_cd, update_data)

    def _update_sync(self, stk_cd: str, update_data: MyStockUpdate) -> Optional[MyStock]:
        # 기존 데이터 확인
        existing = self._get_by_code_sync(stk_cd)
        if not existing:
            return None

        # 업데이트할 필드들만 추출
        update_fields = {}
        if update_data.stk_nm is not None:
            update_fields['stk_nm'] = update_data.stk_nm
        if update_data.sector is not None:
            update_fields['sector'] = update_data.sector
        if update_data.is_hold is not None:
            update_fields['is_hold'] = update_data.is_hold
        if update_data.is_watch is not None:
            update_fields['is_watch'] = update_data.is_watch
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
            values = list(update_fields.values()) + [stk_cd]
            cur.execute(f"""
                UPDATE my_stock 
                SET {set_clause}
                WHERE stk_cd = ?
            """, values)
            conn.commit()

        # 업데이트된 데이터 반환
        return self._get_by_code_sync(stk_cd)

    async def delete(self, stk_cd: str) -> bool:
        """종목 삭제"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._delete_sync, stk_cd)

    def _delete_sync(self, stk_cd: str) -> bool:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM my_stock WHERE stk_cd = ?", (stk_cd,))
            conn.commit()
            return cur.rowcount > 0

    async def list_all(self, filter_data: Optional[MyStockFilter] = None) -> List[MyStock]:
        """모든 종목 목록 조회 (필터링 포함)"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._list_all_sync, filter_data)

    def _list_all_sync(self, filter_data: Optional[MyStockFilter] = None) -> List[MyStock]:
        query = """
            SELECT stk_cd, stk_nm, sector, is_hold, is_watch, note, created_at, updated_at
            FROM my_stock
        """
        params = []
        conditions = []

        if filter_data:
            if filter_data.is_hold is not None:
                conditions.append("is_hold = ?")
                params.append(filter_data.is_hold)
            
            if filter_data.is_watch is not None:
                conditions.append("is_watch = ?")
                params.append(filter_data.is_watch)
            
            if filter_data.sector is not None:
                conditions.append("sector = ?")
                params.append(filter_data.sector)
            
            if filter_data.stk_nm_like is not None:
                conditions.append("stk_nm LIKE ?")
                params.append(f"%{filter_data.stk_nm_like}%")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        query += " ORDER BY stk_cd"

        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            rows = cur.fetchall()
            
            return [self._row_to_mystock(row) for row in rows]

    async def get_holding_stocks(self) -> List[MyStock]:
        """보유 종목만 조회"""
        filter_data = MyStockFilter(is_hold=1)
        return await self.list_all(filter_data)

    async def get_watching_stocks(self) -> List[MyStock]:
        """관심 종목만 조회"""
        filter_data = MyStockFilter(is_watch=1)
        return await self.list_all(filter_data)

    async def set_hold_status(self, stk_cd: str, is_hold: bool) -> Optional[MyStock]:
        """보유 상태 변경"""
        update_data = MyStockUpdate(is_hold=1 if is_hold else 0)
        return await self.update(stk_cd, update_data)

    async def set_watch_status(self, stk_cd: str, is_watch: bool) -> Optional[MyStock]:
        """관심 상태 변경"""
        update_data = MyStockUpdate(is_watch=1 if is_watch else 0)
        return await self.update(stk_cd, update_data)

    async def search_by_name(self, stk_nm: str) -> List[MyStock]:
        """종목명으로 검색"""
        filter_data = MyStockFilter(stk_nm_like=stk_nm)
        return await self.list_all(filter_data)

    async def get_sectors(self) -> List[str]:
        """등록된 모든 섹터 목록 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_sectors_sync)

    def _get_sectors_sync(self) -> List[str]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT DISTINCT sector 
                FROM my_stock 
                WHERE sector IS NOT NULL AND sector != ''
                ORDER BY sector
            """)
            rows = cur.fetchall()
            return [row[0] for row in rows]

    async def get_stats(self) -> Dict[str, int]:
        """통계 정보 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_stats_sync)

    def _get_stats_sync(self) -> Dict[str, int]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            # 전체, 보유, 관심 종목 수 조회
            cur.execute("""
                SELECT 
                    COUNT(*) as total,
                    SUM(CASE WHEN is_hold = 1 THEN 1 ELSE 0 END) as holding,
                    SUM(CASE WHEN is_watch = 1 THEN 1 ELSE 0 END) as watching
                FROM my_stock
            """)
            row = cur.fetchone()
            
            return {
                'total': row[0] or 0,
                'holding': row[1] or 0,
                'watching': row[2] or 0
            }


#---------------------------------------------------------
# MyStockService의 싱글턴 인스턴스를 관리하기 위한 전역 변수와 getter 함수
instance_my_stock_service: MyStockService = None

def get_my_stock_service() -> MyStockService:
    global instance_my_stock_service
    if instance_my_stock_service is None:
        instance_my_stock_service = MyStockService()
    return instance_my_stock_service
