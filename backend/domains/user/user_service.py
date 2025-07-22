from backend.core.config import config
from backend.domains.user.user_model import UserInfo
from backend.core.logger import get_logger
from typing import Dict
from backend.domains.user.user_model import UserInfo
import sqlite3

logger = get_logger(__name__)
# user_service.py

class UserService:
    def __init__(self, db_path: str = "app.db"):
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

    def get(self, name: str) -> UserInfo:
        return self.user_infos.get(name)

    def set(self, name: str, value: str):
        user = UserInfo(name=name, value=value)
        self.user_infos[name] = user
        self._save_to_db(user)

    def _save_to_db(self, user: UserInfo):
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
