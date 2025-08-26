from backend.core.config import config
from backend.domains.stocks.stk_trade_history_model import StkTradeHistory, StkTradeHistoryCreate, StkTradeHistoryUpdate, StkTradeHistoryFilter
from backend.core.logger import get_logger
from typing import List, Optional, Dict
import sqlite3
from datetime import datetime

logger = get_logger(__name__)

class StkTradeHistoryService:
    """주식 매매 이력 서비스 클래스
    
    특정 종목에 대한 매매 기록을 관리하는 서비스
    """
    
    def __init__(self):
        self.db_path = config.DB_PATH

    def _get_conn(self):
        """DB 연결 객체 반환"""
        return sqlite3.connect(self.db_path)

    def _row_to_trade_history(self, row) -> StkTradeHistory:
        """DB row를 StkTradeHistory 객체로 변환"""
        return StkTradeHistory(
            id=row[0],
            stk_cd=row[1],
            stk_nm=row[2],
            ymd=row[3],
            note=row[4],
            created_at=row[5],
            updated_at=row[6]
        )

    async def create(self, trade_data: StkTradeHistoryCreate) -> StkTradeHistory:
        """새로운 매매 이력 생성"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._create_sync, trade_data)

    def _create_sync(self, trade_data: StkTradeHistoryCreate) -> StkTradeHistory:
        with self._get_conn() as conn:
            cur = conn.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            cur.execute("""
                INSERT INTO stk_trades_history (stk_cd, stk_nm, ymd, note, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                trade_data.stk_cd,
                trade_data.stk_nm,
                trade_data.ymd,
                trade_data.note,
                now,
                now
            ))
            conn.commit()
            
            # 생성된 ID 조회
            trade_id = cur.lastrowid
            return StkTradeHistory(
                id=trade_id,
                stk_cd=trade_data.stk_cd,
                stk_nm=trade_data.stk_nm,
                ymd=trade_data.ymd,
                note=trade_data.note,
                created_at=now,
                updated_at=now
            )

    async def get_by_id(self, trade_id: int) -> Optional[StkTradeHistory]:
        """ID로 매매 이력 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_by_id_sync, trade_id)

    def _get_by_id_sync(self, trade_id: int) -> Optional[StkTradeHistory]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT id, stk_cd, stk_nm, ymd, note, created_at, updated_at
                FROM stk_trades_history
                WHERE id = ?
            """, (trade_id,))
            
            row = cur.fetchone()
            if row:
                return self._row_to_trade_history(row)
            return None

    async def update(self, trade_id: int, update_data: StkTradeHistoryUpdate) -> Optional[StkTradeHistory]:
        """매매 이력 수정"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._update_sync, trade_id, update_data)

    def _update_sync(self, trade_id: int, update_data: StkTradeHistoryUpdate) -> Optional[StkTradeHistory]:
        # 기존 데이터 확인
        existing = self._get_by_id_sync(trade_id)
        if not existing:
            return None

        # 업데이트할 필드들만 추출
        update_fields = {}
        if update_data.stk_cd is not None:
            update_fields['stk_cd'] = update_data.stk_cd
        if update_data.stk_nm is not None:
            update_fields['stk_nm'] = update_data.stk_nm
        if update_data.ymd is not None:
            update_fields['ymd'] = update_data.ymd
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
            values = list(update_fields.values()) + [trade_id]
            cur.execute(f"""
                UPDATE stk_trades_history 
                SET {set_clause}
                WHERE id = ?
            """, values)
            conn.commit()

        # 업데이트된 데이터 반환
        return self._get_by_id_sync(trade_id)

    async def delete(self, trade_id: int) -> bool:
        """매매 이력 삭제"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._delete_sync, trade_id)

    def _delete_sync(self, trade_id: int) -> bool:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM stk_trades_history WHERE id = ?", (trade_id,))
            conn.commit()
            return cur.rowcount > 0

    async def list_all(self, filter_data: Optional[StkTradeHistoryFilter] = None) -> List[StkTradeHistory]:
        """모든 매매 이력 목록 조회 (필터링 포함)"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._list_all_sync, filter_data)

    def _list_all_sync(self, filter_data: Optional[StkTradeHistoryFilter] = None) -> List[StkTradeHistory]:
        query = """
            SELECT id, stk_cd, stk_nm, ymd, note, created_at, updated_at
            FROM stk_trades_history
        """
        params = []
        conditions = []

        if filter_data:
            if filter_data.stk_cd is not None:
                conditions.append("stk_cd = ?")
                params.append(filter_data.stk_cd)
            
            if filter_data.ymd_from is not None:
                conditions.append("ymd >= ?")
                params.append(filter_data.ymd_from)
            
            if filter_data.ymd_to is not None:
                conditions.append("ymd <= ?")
                params.append(filter_data.ymd_to)
            
            if filter_data.stk_nm_like is not None:
                conditions.append("stk_nm LIKE ?")
                params.append(f"%{filter_data.stk_nm_like}%")
            
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
            
            return [self._row_to_trade_history(row) for row in rows]

    async def get_by_stock(self, stk_cd: str) -> List[StkTradeHistory]:
        """특정 종목의 매매 이력"""
        filter_data = StkTradeHistoryFilter(stk_cd=stk_cd)
        return await self.list_all(filter_data)

    async def get_by_date(self, ymd: str) -> List[StkTradeHistory]:
        """특정 날짜의 매매 이력"""
        filter_data = StkTradeHistoryFilter(ymd_from=ymd, ymd_to=ymd)
        return await self.list_all(filter_data)

    async def get_date_range(self, start_date: str, end_date: str) -> List[StkTradeHistory]:
        """날짜 범위로 매매 이력 조회"""
        filter_data = StkTradeHistoryFilter(ymd_from=start_date, ymd_to=end_date)
        return await self.list_all(filter_data)

    async def search_by_stock_name(self, stock_name: str) -> List[StkTradeHistory]:
        """종목명으로 매매 이력 검색"""
        filter_data = StkTradeHistoryFilter(stk_nm_like=stock_name)
        return await self.list_all(filter_data)

    async def search_by_note(self, keyword: str) -> List[StkTradeHistory]:
        """매매 기록 내용으로 검색"""
        filter_data = StkTradeHistoryFilter(note_like=keyword)
        return await self.list_all(filter_data)

    async def get_stats(self) -> Dict[str, any]:
        """매매 이력 통계 정보"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_stats_sync)

    def _get_stats_sync(self) -> Dict[str, any]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            # 전체 매매 이력 수
            cur.execute("SELECT COUNT(*) FROM stk_trades_history")
            total = cur.fetchone()[0]
            
            # 고유 종목 수
            cur.execute("SELECT COUNT(DISTINCT stk_cd) FROM stk_trades_history")
            unique_stocks = cur.fetchone()[0]
            
            # 최근 거래일
            cur.execute("SELECT MAX(ymd) FROM stk_trades_history")
            latest_date = cur.fetchone()[0]
            
            # 최초 거래일
            cur.execute("SELECT MIN(ymd) FROM stk_trades_history")
            earliest_date = cur.fetchone()[0]
            
            return {
                'total_trades': total or 0,
                'unique_stocks': unique_stocks or 0,
                'latest_trade_date': latest_date,
                'earliest_trade_date': earliest_date
            }

    async def get_stock_trade_summary(self, stk_cd: str) -> Dict[str, any]:
        """특정 종목의 매매 요약 정보"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_stock_trade_summary_sync, stk_cd)

    def _get_stock_trade_summary_sync(self, stk_cd: str) -> Dict[str, any]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            
            # 특정 종목의 매매 횟수
            cur.execute("SELECT COUNT(*) FROM stk_trades_history WHERE stk_cd = ?", (stk_cd,))
            trade_count = cur.fetchone()[0]
            
            # 최근 거래일
            cur.execute("SELECT MAX(ymd) FROM stk_trades_history WHERE stk_cd = ?", (stk_cd,))
            latest_date = cur.fetchone()[0]
            
            # 최초 거래일
            cur.execute("SELECT MIN(ymd) FROM stk_trades_history WHERE stk_cd = ?", (stk_cd,))
            earliest_date = cur.fetchone()[0]
            
            # 종목명
            cur.execute("SELECT stk_nm FROM stk_trades_history WHERE stk_cd = ? LIMIT 1", (stk_cd,))
            result = cur.fetchone()
            stock_name = result[0] if result else None
            
            return {
                'stk_cd': stk_cd,
                'stk_nm': stock_name,
                'trade_count': trade_count or 0,
                'latest_trade_date': latest_date,
                'earliest_trade_date': earliest_date
            }


#---------------------------------------------------------
# StkTradeHistoryService의 싱글턴 인스턴스를 관리하기 위한 전역 변수와 getter 함수
instance_stk_trade_history_service: StkTradeHistoryService = None

def get_stk_trade_history_service() -> StkTradeHistoryService:
    """StkTradeHistoryService 싱글턴 인스턴스 반환"""
    global instance_stk_trade_history_service
    if instance_stk_trade_history_service is None:
        instance_stk_trade_history_service = StkTradeHistoryService()
    return instance_stk_trade_history_service
