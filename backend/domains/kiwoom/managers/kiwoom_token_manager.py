

from datetime import datetime
from typing import Optional
import aiohttp
from backend.core.logger import get_logger
from backend.core.config import config
from backend.core.exceptions import KiwoomAuthException
from backend.domains.user.user_service import UserService

logger = get_logger(__name__)

class KiwoomTokenManager:
    def __init__(self, user_service: Optional[UserService] = None):
        self.app_key = config.KIWOOM_APP_KEY
        self.app_secret = config.KIWOOM_SECRET_KEY
        self.base_url = "https://api.kiwoom.com"
        self.user_service = user_service or UserService()

        self.token_type: Optional[str] = None
        self.token: Optional[str] = None
        self.expires_dt: Optional[str] = None

    async def get_token(self) -> str:
        await self.refresh_token()
        return self.token

    async def refresh_token(self) -> bool:
        try:
            if not self.token or not self.expires_dt:
                await self._load_token_from_db()

            if not self.token or not self.expires_dt:
                logger.info("저장된 토큰이 없어 새로 발급받습니다.")
                await self.issue_access_token()
                return True

            if self._is_token_expire_soon():
                logger.info("토큰 만료가 임박하여 새로 발급받습니다.")
                await self.issue_access_token()

            logger.debug("Refresh_token : 토큰 상태 확인 완료")
            return True
        except Exception as e:
            logger.error(f"토큰 갱신 중 오류 발생: {str(e)}")
            raise KiwoomAuthException(f"토큰 갱신 실패: {str(e)}")

    async def issue_access_token(self):
        url = f"{self.base_url}/oauth2/token"
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        params = {
            'grant_type': 'client_credentials',
            'appkey': self.app_key,
            'secretkey': self.app_secret,
        }

        try:
            logger.info("키움 API 액세스 토큰 발급 요청 중...")
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=params) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        raise KiwoomAuthException(f"토큰 발급 실패: HTTP {response.status} - {error_text}")

                    resp_json = await response.json()
                    self.token_type = resp_json.get("token_type")
                    self.token = resp_json.get("token")
                    self.expires_dt = resp_json.get("expires_dt")
                    
                    if not self.token:
                        raise KiwoomAuthException("응답에서 액세스 토큰을 찾을 수 없습니다.")
                    logger.info(f"발급된 토큰: token[{self.token[:20]}], token_type:[{self.token_type}]... (만료 시간: {self.expires_dt})")
                    await self._save_token_to_db()
                    logger.info("키움 API 액세스 토큰 발급 완료")
        except aiohttp.ClientError as e:
            raise KiwoomAuthException(f"토큰 발급 네트워크 오류: {str(e)}")
        except Exception as e:
            raise KiwoomAuthException(f"토큰 발급 실패: {str(e)}")

    def _is_token_expire_soon(self) -> bool:
        try:
            expire_time = datetime.strptime(self.expires_dt, '%Y%m%d%H%M%S')
            return (expire_time - datetime.now()).total_seconds() <= 3600
        except Exception as e:
            logger.warning(f"토큰 만료 시간 파싱 오류: {e}")
            return True

    async def _load_token_from_db(self):
        token_info = await self.user_service.get("ACCESS_TOKEN")
        time_info = await self.user_service.get("ACCESS_TOKEN_EXPIRED_TIME")
        self.token = token_info.value if token_info else None
        self.expires_dt = time_info.value if time_info else None

    async def _save_token_to_db(self):
        await self.user_service.set("ACCESS_TOKEN", self.token)
        await self.user_service.set("ACCESS_TOKEN_EXPIRED_TIME", self.expires_dt)
