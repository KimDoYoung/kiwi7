from backend.core.config import config
from backend.domains.user.user_model import UserInfo
from backend.core.logger import get_logger
from typing import Dict
from backend.domains.user.user_model import UserInfo
import sqlite3

logger = get_logger(__name__)
# user_service.py

class UserService:
    def __init__(self):
        self.db_path = config.DB_PATH
        self.user_infos: Dict[str, UserInfo] = {}
        self._load_userinfos()

    def _get_conn(self):
        return sqlite3.connect(self.db_path)

    def _load_userinfos(self):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT name, value, created_at FROM users")
            for name, value, created_at in cur.fetchall():
                self.user_infos[name] = UserInfo(name=name, value=value, created_at=created_at)

    async def get(self, name: str) -> UserInfo:
        return self.user_infos.get(name)

    async def set(self, name: str, value: str):
        user = UserInfo(name=name, value=value)
        self.user_infos[name] = user
        await self._save_to_db(user)

    async def _save_to_db(self, user: UserInfo):
        # SQLite는 동기이므로 thread pool에서 실행
        import asyncio
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self._save_to_db_sync, user)

    def _save_to_db_sync(self, user: UserInfo):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT OR REPLACE INTO users (name, value) VALUES (?, ?)
            """, (user.name, user.value))
            conn.commit()

    def delete(self, name: str):
        if name in self.user_infos:
            del self.user_infos[name]
            with self._get_conn() as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM users WHERE name = ?", (name,))
                conn.commit()

    def list_all(self):
        return list(self.user_infos.values())

#---------------------------------------------------------
# UserService의 싱글턴 인스턴스를 관리하기 위한 전역 변수와 getter 함수
instance_user_service: UserService = None

def get_user_service() -> UserService:
    global instance_user_service
    if instance_user_service is None:
        instance_user_service = UserService()
    return instance_user_service
