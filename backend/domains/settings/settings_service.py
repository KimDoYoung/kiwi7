from backend.core.config import config
from backend.domains.settings.settings_model import SettingInfo
from backend.core.logger import get_logger
from typing import Dict
import sqlite3

logger = get_logger(__name__)

class SettingsService:
    """시스템 설정 서비스 클래스
    
    설정값을 name-value 쌍으로 관리하는 서비스
    """
    
    def __init__(self):
        self.db_path = config.DB_PATH
        self.settings: Dict[str, SettingInfo] = {}
        self._load_settings()

    def _get_conn(self):
        """DB 연결 객체 반환"""
        return sqlite3.connect(self.db_path)

    def _load_settings(self):
        """DB에서 모든 설정값을 메모리로 로드"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT name, value, created_at FROM settings")
            for name, value, created_at in cur.fetchall():
                self.settings[name] = SettingInfo(name=name, value=value, created_at=created_at)

    async def get(self, name: str) -> SettingInfo:
        """설정값 조회"""
        return self.settings.get(name)

    async def set(self, name: str, value: str):
        """설정값 저장"""
        setting = SettingInfo(name=name, value=value)
        self.settings[name] = setting
        await self._save_to_db(setting)

    async def _save_to_db(self, setting: SettingInfo):
        """설정값을 DB에 비동기로 저장"""
        import asyncio
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self._save_to_db_sync, setting)

    def _save_to_db_sync(self, setting: SettingInfo):
        """설정값을 DB에 동기로 저장"""
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT OR REPLACE INTO settings (name, value) VALUES (?, ?)
            """, (setting.name, setting.value))
            conn.commit()

    def delete(self, name: str):
        """설정값 삭제"""
        if name in self.settings:
            del self.settings[name]
            with self._get_conn() as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM settings WHERE name = ?", (name,))
                conn.commit()

    def list_all(self):
        """모든 설정값 목록 반환"""
        return list(self.settings.values())


#---------------------------------------------------------
# SettingsService의 싱글턴 인스턴스를 관리하기 위한 전역 변수와 getter 함수
instance_settings_service: SettingsService = None

def get_settings_service() -> SettingsService:
    """SettingsService 싱글턴 인스턴스 반환"""
    global instance_settings_service
    if instance_settings_service is None:
        instance_settings_service = SettingsService()
    return instance_settings_service
