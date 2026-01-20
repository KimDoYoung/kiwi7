"""
KIS(한국투자증권) 토큰 매니저
OAuth2 토큰 발급, 갱신, 저장을 관리합니다.
"""
from datetime import datetime
import aiohttp

from backend.domains.base.base_token_manager import BaseTokenManager
from backend.domains.stock_api import BrokerType
from backend.core.config import config
from backend.core.exceptions import KisAuthException
from backend.core.logger import get_logger

logger = get_logger(__name__)


class KisTokenManager(BaseTokenManager):
    """한국투자증권 토큰 매니저"""

    def __init__(self):
        super().__init__(broker_type=BrokerType.KIS)

    @property
    def base_url(self) -> str:
        return config.KIS_BASE_URL

    @property
    def app_key(self) -> str:
        return config.KIS_APP_KEY

    @property
    def app_secret(self) -> str:
        return config.KIS_SECRET_KEY

    async def issue_access_token(self) -> dict:
        """KIS 토큰 발급"""
        url = f"{self.base_url}/oauth2/tokenP"
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        params = {
            'grant_type': 'client_credentials',
            'appkey': self.app_key,
            'appsecret': self.app_secret,
        }

        try:
            logger.info("[KIS] 액세스 토큰 발급 요청...")
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=params) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        raise KisAuthException(f"토큰 발급 실패: {error_text}")

                    resp_json = await response.json()

                    # 에러 응답 체크
                    if 'error_code' in resp_json:
                        raise KisAuthException(
                            f"토큰 발급 실패: {resp_json.get('error_description', resp_json.get('error_code'))}"
                        )

                    self.token = resp_json.get("access_token")
                    self.token_type = resp_json.get("token_type", "Bearer")
                    self.expires_dt = resp_json.get("access_token_token_expired")

                    if not self.token:
                        raise KisAuthException("응답에 토큰이 없습니다")

                    await self._save_token_to_db()
                    logger.info(f"[KIS] 토큰 발급 완료 (만료: {self.expires_dt})")

                    return {
                        'token': self.token,
                        'expires_dt': self.expires_dt,
                        'token_type': self.token_type
                    }

        except aiohttp.ClientError as e:
            raise KisAuthException(f"네트워크 오류: {e}")

    async def discard_token(self):
        """KIS 토큰 폐기"""
        if not self.token:
            logger.info("[KIS] 폐기할 토큰이 없습니다.")
            return

        url = f"{self.base_url}/oauth2/revokeP"
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        params = {
            'appkey': self.app_key,
            'appsecret': self.app_secret,
            'token': self.token,
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=params) as response:
                    if response.status == 200:
                        await self._clear_token_from_db()
                        logger.info("[KIS] 토큰 폐기 완료")
                    else:
                        error_text = await response.text()
                        logger.warning(f"[KIS] 토큰 폐기 실패: {error_text}")
        except Exception as e:
            logger.error(f"[KIS] 토큰 폐기 중 오류: {e}")

    async def get_approval_key(self) -> str:
        """WebSocket 접속용 승인키 발급"""
        url = f"{self.base_url}/oauth2/Approval"
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        body = {
            'grant_type': 'client_credentials',
            'appkey': self.app_key,
            'secretkey': self.app_secret,
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=body) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        raise KisAuthException(f"승인키 발급 실패: {error_text}")

                    data = await response.json()
                    approval_key = data.get('approval_key')

                    if not approval_key:
                        raise KisAuthException("응답에 승인키가 없습니다")

                    logger.info("[KIS] WebSocket 승인키 발급 완료")
                    return approval_key

        except aiohttp.ClientError as e:
            raise KisAuthException(f"승인키 발급 네트워크 오류: {e}")

    def _is_token_expire_soon(self) -> bool:
        """만료 임박 여부 (1시간 전)"""
        if not self.expires_dt:
            return True

        try:
            # KIS 형식: "2024-01-15 12:30:00"
            expire_time = datetime.strptime(self.expires_dt, '%Y-%m-%d %H:%M:%S')
            return (expire_time - datetime.now()).total_seconds() <= 3600
        except Exception as e:
            logger.warning(f"[KIS] 만료 시간 파싱 오류: {e}")
            return True

    def _create_auth_exception(self, message: str) -> Exception:
        return KisAuthException(message)
