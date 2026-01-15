"""
LS증권 토큰 매니저
OAuth2 토큰 발급, 갱신, 저장을 관리합니다.
"""
from datetime import datetime, timedelta
import aiohttp

from backend.domains.base.base_token_manager import BaseTokenManager
from backend.core.config import config
from backend.core.exceptions import LsAuthException
from backend.core.logger import get_logger

logger = get_logger(__name__)


class LsTokenManager(BaseTokenManager):
    """LS증권 토큰 매니저"""

    def __init__(self):
        super().__init__(broker_name="ls")

    @property
    def base_url(self) -> str:
        return config.LS_BASE_URL

    @property
    def app_key(self) -> str:
        return config.LS_APP_KEY

    @property
    def app_secret(self) -> str:
        return config.LS_SECRET_KEY

    async def issue_access_token(self) -> dict:
        """LS 토큰 발급"""
        url = f"{self.base_url}/oauth2/token"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        params = {
            'grant_type': 'client_credentials',
            'appkey': self.app_key,
            'appsecretkey': self.app_secret,
            'scope': 'oob',
        }

        try:
            logger.info("[LS] 액세스 토큰 발급 요청...")
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, data=params) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        raise LsAuthException(f"토큰 발급 실패: {error_text}")

                    resp_json = await response.json()

                    # 에러 응답 체크
                    if 'error' in resp_json:
                        raise LsAuthException(
                            f"토큰 발급 실패: {resp_json.get('error_description', resp_json.get('error'))}"
                        )

                    self.token = resp_json.get("access_token")
                    self.token_type = resp_json.get("token_type", "Bearer")

                    # LS는 expires_in (초단위)로 제공
                    expires_in = resp_json.get("expires_in", 86400)
                    expire_time = datetime.now() + timedelta(seconds=expires_in)
                    self.expires_dt = expire_time.strftime('%Y-%m-%d %H:%M:%S')

                    if not self.token:
                        raise LsAuthException("응답에 토큰이 없습니다")

                    await self._save_token_to_db()
                    logger.info(f"[LS] 토큰 발급 완료 (만료: {self.expires_dt})")

                    return {
                        'token': self.token,
                        'expires_dt': self.expires_dt,
                        'token_type': self.token_type
                    }

        except aiohttp.ClientError as e:
            raise LsAuthException(f"네트워크 오류: {e}")

    async def discard_token(self):
        """LS 토큰 폐기"""
        if not self.token:
            logger.info("[LS] 폐기할 토큰이 없습니다.")
            return

        url = f"{self.base_url}/oauth2/revoke"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        params = {
            'appkey': self.app_key,
            'appsecretkey': self.app_secret,
            'token': self.token,
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, data=params) as response:
                    if response.status == 200:
                        await self._clear_token_from_db()
                        logger.info("[LS] 토큰 폐기 완료")
                    else:
                        error_text = await response.text()
                        logger.warning(f"[LS] 토큰 폐기 실패: {error_text}")
        except Exception as e:
            logger.error(f"[LS] 토큰 폐기 중 오류: {e}")

    def _is_token_expire_soon(self) -> bool:
        """만료 임박 여부 (1시간 전)"""
        if not self.expires_dt:
            return True

        try:
            # LS 형식: "2024-01-15 12:30:00"
            expire_time = datetime.strptime(self.expires_dt, '%Y-%m-%d %H:%M:%S')
            return (expire_time - datetime.now()).total_seconds() <= 3600
        except Exception as e:
            logger.warning(f"[LS] 만료 시간 파싱 오류: {e}")
            return True

    def _create_auth_exception(self, message: str) -> Exception:
        return LsAuthException(message)
