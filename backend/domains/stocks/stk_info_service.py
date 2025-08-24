# stk_info_service.py
"""
모듈 설명: 
    - stk_info_service
주요 기능:
    - 기본 CRUD 작업: create, get_by_code, update, delete
    - 목록 조회: list_all (필터링, 페이징 지원)
    - 대량 처리: bulk_create (키움 API 데이터 대량 저장)
    - 검색 기능: search_by_name, get_by_market, get_by_sector
    - 통계 및 메타데이터: get_markets, get_sectors, get_stats
    - UPSERT: upsert (존재하면 업데이트, 없으면 생성)
    - 비동기 처리: 모든 메서드가 async/await 패턴으로 구현
작성자: 김도영
작성일: 2025-08-24
버전: 1.0
"""
from backend.core.config import config
from backend.domains.stocks.stk_info_model import StkInfo, StkInfoCreate, StkInfoUpdate, StkInfoFilter, StkInfoBulkCreate
from backend.core.logger import get_logger
from typing import List, Optional, Dict, Tuple
import sqlite3
from datetime import datetime

logger = get_logger(__name__)

class StkInfoService:
    def __init__(self):
        self.db_path = config.DB_PATH

    def _get_conn(self):
        return sqlite3.connect(self.db_path)

    def _row_to_stkinfo(self, row) -> StkInfo:
        """DB row를 StkInfo 객체로 변환"""
        return StkInfo(
            code=row[0],
            name=row[1],
            list_count=row[2],
            audit_info=row[3],
            reg_day=row[4],
            last_price=row[5],
            state=row[6],
            market_code=row[7],
            market_name=row[8],
            up_name=row[9],
            up_size_name=row[10],
            company_class_name=row[11],
            order_warning=row[12],
            nxt_enable=row[13],
            created_at=row[14]
        )

    async def create(self, stk_info: StkInfoCreate) -> StkInfo:
        """새로운 종목 정보 추가"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._create_sync, stk_info)

    def _create_sync(self, stk_info: StkInfoCreate) -> StkInfo:
        with self._get_conn() as conn:
            cur = conn.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            cur.execute("""
                INSERT INTO stk_info (
                    code, name, list_count, audit_info, reg_day, last_price, state,
                    market_code, market_name, up_name, up_size_name, company_class_name,
                    order_warning, nxt_enable, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                stk_info.code,
                stk_info.name,
                stk_info.list_count,
                stk_info.audit_info,
                stk_info.reg_day,
                stk_info.last_price,
                stk_info.state,
                stk_info.market_code,
                stk_info.market_name,
                stk_info.up_name,
                stk_info.up_size_name,
                stk_info.company_class_name,
                stk_info.order_warning,
                stk_info.nxt_enable,
                now
            ))
            conn.commit()
            
            return StkInfo(
                code=stk_info.code,
                name=stk_info.name,
                list_count=stk_info.list_count,
                audit_info=stk_info.audit_info,
                reg_day=stk_info.reg_day,
                last_price=stk_info.last_price,
                state=stk_info.state,
                market_code=stk_info.market_code,
                market_name=stk_info.market_name,
                up_name=stk_info.up_name,
                up_size_name=stk_info.up_size_name,
                company_class_name=stk_info.company_class_name,
                order_warning=stk_info.order_warning,
                nxt_enable=stk_info.nxt_enable,
                created_at=now
            )

    async def get_by_code(self, code: str) -> Optional[StkInfo]:
        """종목코드로 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_by_code_sync, code)

    def _get_by_code_sync(self, code: str) -> Optional[StkInfo]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT code, name, list_count, audit_info, reg_day, last_price, state,
                       market_code, market_name, up_name, up_size_name, company_class_name,
                       order_warning, nxt_enable, created_at
                FROM stk_info
                WHERE code = ?
            """, (code,))
            
            row = cur.fetchone()
            if row:
                return self._row_to_stkinfo(row)
            return None

    async def update(self, code: str, update_data: StkInfoUpdate) -> Optional[StkInfo]:
        """종목 정보 수정"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._update_sync, code, update_data)

    def _update_sync(self, code: str, update_data: StkInfoUpdate) -> Optional[StkInfo]:
        # 기존 데이터 확인
        existing = self._get_by_code_sync(code)
        if not existing:
            return None

        # 업데이트할 필드들만 추출
        update_fields = {}
        if update_data.name is not None:
            update_fields['name'] = update_data.name
        if update_data.list_count is not None:
            update_fields['list_count'] = update_data.list_count
        if update_data.audit_info is not None:
            update_fields['audit_info'] = update_data.audit_info
        if update_data.reg_day is not None:
            update_fields['reg_day'] = update_data.reg_day
        if update_data.last_price is not None:
            update_fields['last_price'] = update_data.last_price
        if update_data.state is not None:
            update_fields['state'] = update_data.state
        if update_data.market_code is not None:
            update_fields['market_code'] = update_data.market_code
        if update_data.market_name is not None:
            update_fields['market_name'] = update_data.market_name
        if update_data.up_name is not None:
            update_fields['up_name'] = update_data.up_name
        if update_data.up_size_name is not None:
            update_fields['up_size_name'] = update_data.up_size_name
        if update_data.company_class_name is not None:
            update_fields['company_class_name'] = update_data.company_class_name
        if update_data.order_warning is not None:
            update_fields['order_warning'] = update_data.order_warning
        if update_data.nxt_enable is not None:
            update_fields['nxt_enable'] = update_data.nxt_enable

        if not update_fields:
            return existing

        # SQL 쿼리 동적 생성
        set_clause = ', '.join([f"{field} = ?" for field in update_fields.keys()])

        with self._get_conn() as conn:
            cur = conn.cursor()
            values = list(update_fields.values()) + [code]
            cur.execute(f"""
                UPDATE stk_info 
                SET {set_clause}
                WHERE code = ?
            """, values)
            conn.commit()

        # 업데이트된 데이터 반환
        return self._get_by_code_sync(code)
    
    async def delete_all(self) ->bool:
        """ 모든 레코드 삭제 """
        import asyncio  
        loop = asyncio.get_event_loop()
        def _delete_all_sync():
            with self._get_conn() as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM stk_info")
                conn.commit()
                return True
        return await loop.run_in_executor(None, _delete_all_sync)

    async def delete(self, code: str) -> bool:
        """종목 정보 삭제"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._delete_sync, code)

    def _delete_sync(self, code: str) -> bool:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM stk_info WHERE code = ?", (code,))
            conn.commit()
            return cur.rowcount > 0

    async def list_all(self, filter_data: Optional[StkInfoFilter] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> List[StkInfo]:
        """모든 종목 목록 조회 (필터링 및 페이징 포함)"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._list_all_sync, filter_data, limit, offset)

    def _list_all_sync(self, filter_data: Optional[StkInfoFilter] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> List[StkInfo]:
        query = """
            SELECT code, name, list_count, audit_info, reg_day, last_price, state,
                   market_code, market_name, up_name, up_size_name, company_class_name,
                   order_warning, nxt_enable, created_at
            FROM stk_info
        """
        params = []
        conditions = []

        if filter_data:
            if filter_data.market_code is not None:
                conditions.append("market_code = ?")
                params.append(filter_data.market_code)
            
            if filter_data.market_name is not None:
                conditions.append("market_name = ?")
                params.append(filter_data.market_name)
            
            if filter_data.up_name is not None:
                conditions.append("up_name = ?")
                params.append(filter_data.up_name)
            
            if filter_data.up_size_name is not None:
                conditions.append("up_size_name = ?")
                params.append(filter_data.up_size_name)
                
            if filter_data.order_warning is not None:
                conditions.append("order_warning = ?")
                params.append(filter_data.order_warning)
                
            if filter_data.nxt_enable is not None:
                conditions.append("nxt_enable = ?")
                params.append(filter_data.nxt_enable)
            
            if filter_data.name_like is not None:
                conditions.append("name LIKE ?")
                params.append(f"%{filter_data.name_like}%")
                
            if filter_data.code_like is not None:
                conditions.append("code LIKE ?")
                params.append(f"%{filter_data.code_like}%")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        query += " ORDER BY code"
        
        if limit is not None:
            query += f" LIMIT {limit}"
            if offset is not None:
                query += f" OFFSET {offset}"

        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            rows = cur.fetchall()
            
            return [self._row_to_stkinfo(row) for row in rows]

    async def count_all(self, filter_data: Optional[StkInfoFilter] = None) -> int:
        """필터링된 종목 총 개수 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._count_all_sync, filter_data)

    def _count_all_sync(self, filter_data: Optional[StkInfoFilter] = None) -> int:
        query = "SELECT COUNT(*) FROM stk_info"
        params = []
        conditions = []

        if filter_data:
            if filter_data.market_code is not None:
                conditions.append("market_code = ?")
                params.append(filter_data.market_code)
            
            if filter_data.market_name is not None:
                conditions.append("market_name = ?")
                params.append(filter_data.market_name)
            
            if filter_data.up_name is not None:
                conditions.append("up_name = ?")
                params.append(filter_data.up_name)
            
            if filter_data.up_size_name is not None:
                conditions.append("up_size_name = ?")
                params.append(filter_data.up_size_name)
                
            if filter_data.order_warning is not None:
                conditions.append("order_warning = ?")
                params.append(filter_data.order_warning)
                
            if filter_data.nxt_enable is not None:
                conditions.append("nxt_enable = ?")
                params.append(filter_data.nxt_enable)
            
            if filter_data.name_like is not None:
                conditions.append("name LIKE ?")
                params.append(f"%{filter_data.name_like}%")
                
            if filter_data.code_like is not None:
                conditions.append("code LIKE ?")
                params.append(f"%{filter_data.code_like}%")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            return cur.fetchone()[0]

    async def bulk_create(self, bulk_data: StkInfoBulkCreate) -> Tuple[int, int]:
        """종목 정보 대량 생성 (키움 API 데이터 저장용)"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._bulk_create_sync, bulk_data)

    def _bulk_create_sync(self, bulk_data: StkInfoBulkCreate) -> Tuple[int, int]:
        """대량 생성 동기 처리 - (성공 건수, 실패 건수) 반환"""
        success_count = 0
        error_count = 0
        
        with self._get_conn() as conn:
            cur = conn.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            for stk_info in bulk_data.stocks:
                try:
                    if bulk_data.overwrite:
                        # REPLACE INTO 사용 (INSERT OR REPLACE)
                        cur.execute("""
                            REPLACE INTO stk_info (
                                code, name, list_count, audit_info, reg_day, last_price, state,
                                market_code, market_name, up_name, up_size_name, company_class_name,
                                order_warning, nxt_enable, created_at
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, (
                            stk_info.code, stk_info.name, stk_info.list_count, stk_info.audit_info,
                            stk_info.reg_day, stk_info.last_price, stk_info.state, stk_info.market_code,
                            stk_info.market_name, stk_info.up_name, stk_info.up_size_name,
                            stk_info.company_class_name, stk_info.order_warning, stk_info.nxt_enable, now
                        ))
                    else:
                        # INSERT OR IGNORE 사용 (중복 시 무시)
                        cur.execute("""
                            INSERT OR IGNORE INTO stk_info (
                                code, name, list_count, audit_info, reg_day, last_price, state,
                                market_code, market_name, up_name, up_size_name, company_class_name,
                                order_warning, nxt_enable, created_at
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, (
                            stk_info.code, stk_info.name, stk_info.list_count, stk_info.audit_info,
                            stk_info.reg_day, stk_info.last_price, stk_info.state, stk_info.market_code,
                            stk_info.market_name, stk_info.up_name, stk_info.up_size_name,
                            stk_info.company_class_name, stk_info.order_warning, stk_info.nxt_enable, now
                        ))
                    success_count += 1
                    
                except Exception as e:
                    logger.error(f"종목 정보 저장 실패 - 코드: {stk_info.code}, 오류: {e}")
                    error_count += 1
                    
            conn.commit()
            
        logger.info(f"종목 정보 대량 저장 완료 - 성공: {success_count}, 실패: {error_count}")
        return success_count, error_count

    async def search_by_name(self, name: str) -> List[StkInfo]:
        """종목명으로 검색"""
        filter_data = StkInfoFilter(name_like=name)
        return await self.list_all(filter_data)

    async def get_by_market(self, market_code: str) -> List[StkInfo]:
        """특정 시장의 모든 종목 조회"""
        filter_data = StkInfoFilter(market_code=market_code)
        return await self.list_all(filter_data)

    async def get_by_sector(self, up_name: str) -> List[StkInfo]:
        """특정 업종의 모든 종목 조회"""
        filter_data = StkInfoFilter(up_name=up_name)
        return await self.list_all(filter_data)

    async def get_markets(self) -> List[Dict[str, str]]:
        """등록된 모든 시장 목록 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_markets_sync)

    def _get_markets_sync(self) -> List[Dict[str, str]]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT DISTINCT market_code, market_name 
                FROM stk_info 
                WHERE market_code IS NOT NULL AND market_name IS NOT NULL
                ORDER BY market_code
            """)
            rows = cur.fetchall()
            return [{"code": row[0], "name": row[1]} for row in rows]

    async def get_sectors(self) -> List[str]:
        """등록된 모든 업종 목록 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._get_sectors_sync)

    def _get_sectors_sync(self) -> List[str]:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT DISTINCT up_name 
                FROM stk_info 
                WHERE up_name IS NOT NULL AND up_name != ''
                ORDER BY up_name
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
            
            # 전체, 시장별, 투자유의 종목 수 조회
            cur.execute("""
                SELECT 
                    COUNT(*) as total,
                    COUNT(CASE WHEN market_code = 'STK' THEN 1 END) as kospi,
                    COUNT(CASE WHEN market_code = 'KSQ' THEN 1 END) as kosdaq,
                    COUNT(CASE WHEN order_warning != '0' THEN 1 END) as warning
                FROM stk_info
            """)
            row = cur.fetchone()
            
            return {
                'total': row[0] or 0,
                'kospi': row[1] or 0,
                'kosdaq': row[2] or 0,
                'warning': row[3] or 0
            }

    async def upsert(self, stk_info: StkInfoCreate) -> StkInfo:
        """종목 정보 생성 또는 업데이트 (UPSERT)"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._upsert_sync, stk_info)

    def _upsert_sync(self, stk_info: StkInfoCreate) -> StkInfo:
        with self._get_conn() as conn:
            cur = conn.cursor()
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            cur.execute("""
                REPLACE INTO stk_info (
                    code, name, list_count, audit_info, reg_day, last_price, state,
                    market_code, market_name, up_name, up_size_name, company_class_name,
                    order_warning, nxt_enable, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                stk_info.code, stk_info.name, stk_info.list_count, stk_info.audit_info,
                stk_info.reg_day, stk_info.last_price, stk_info.state, stk_info.market_code,
                stk_info.market_name, stk_info.up_name, stk_info.up_size_name,
                stk_info.company_class_name, stk_info.order_warning, stk_info.nxt_enable, now
            ))
            conn.commit()
            
            return self._get_by_code_sync(stk_info.code)


#---------------------------------------------------------
# StkInfoService의 싱글턴 인스턴스를 관리하기 위한 전역 변수와 getter 함수
instance_stk_info_service: StkInfoService = None

def get_stk_info_service() -> StkInfoService:
    global instance_stk_info_service
    if instance_stk_info_service is None:
        instance_stk_info_service = StkInfoService()
    return instance_stk_info_service
