"""
tokens 테이블 서비스
증권사별 API 토큰 CRUD 관리
"""
from backend.core.config import config
from backend.domains.models.tokens_model import Token
from backend.core.logger import get_logger
from typing import Optional
import sqlite3
from datetime import datetime

logger = get_logger(__name__)


class TokensService:
    """증권사 토큰 관리 서비스"""

    def __init__(self):
        self.db_path = config.DB_PATH

    def _get_conn(self):
        """DB 연결 객체 반환"""
        return sqlite3.connect(self.db_path)

    def _row_to_token(self, row) -> Token:
        """DB row를 Token 객체로 변환"""
        return Token(
            broker_type=row[0],
            access_token=row[1],
            expires_at=row[2],
            created_at=row[3],
            updated_at=row[4]
        )

    async def get_by_broker(self, broker_type: str) -> Optional[Token]:
        """증권사별 토큰 조회"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None, self._get_by_broker_sync, broker_type
        )

    def _get_by_broker_sync(self, broker_type: str) -> Optional[Token]:
        """동기적으로 증권사별 토큰 조회"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT broker_type, access_token, expires_at, created_at, updated_at
                FROM tokens
                WHERE broker_type = ?
            """, (broker_type.upper(),))

            row = cur.fetchone()
            if row:
                logger.info(f'[{broker_type}] 토큰 조회 완료')
                return self._row_to_token(row)
            return None

    async def upsert(
        self, broker_type: str, access_token: str, expires_at: str
    ) -> Token:
        """토큰 생성 또는 업데이트 (INSERT OR REPLACE)"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None, self._upsert_sync, broker_type, access_token, expires_at
        )

    def _upsert_sync(
        self, broker_type: str, access_token: str, expires_at: str
    ) -> Token:
        """동기적으로 토큰 upsert"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            now = datetime.now().isoformat()

            # 기존 레코드 확인
            existing = self._get_by_broker_sync(broker_type)
            created_at = existing.created_at if existing else now

            cur.execute("""
                INSERT OR REPLACE INTO tokens
                (broker_type, access_token, expires_at, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?)
            """, (
                broker_type.upper(),
                access_token,
                expires_at,
                created_at,
                now
            ))
            conn.commit()

            logger.info(f'[{broker_type}] 토큰 저장 완료')

            return Token(
                broker_type=broker_type.upper(),
                access_token=access_token,
                expires_at=expires_at,
                created_at=created_at,
                updated_at=now
            )

    async def delete_by_broker(self, broker_type: str) -> bool:
        """증권사별 토큰 삭제"""
        import asyncio
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None, self._delete_by_broker_sync, broker_type
        )

    def _delete_by_broker_sync(self, broker_type: str) -> bool:
        """동기적으로 증권사별 토큰 삭제"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                'DELETE FROM tokens WHERE broker_type = ?',
                (broker_type.upper(),)
            )
            conn.commit()
            deleted = cur.rowcount > 0

            if deleted:
                logger.info(f'[{broker_type}] 토큰 삭제 완료')

            return deleted
