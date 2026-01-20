"""
Kiwoom 토큰 매니저
OAuth2 토큰 발급, 갱신, 저장을 관리합니다.
"""
from datetime import datetime
import aiohttp

from backend.domains.base.base_token_manager import BaseTokenManager
from backend.domains.stock_api import BrokerType
from backend.core.config import config
from backend.core.exceptions import KiwoomAuthException
from backend.core.logger import get_logger

logger = get_logger(__name__)


class KiwoomTokenManager(BaseTokenManager):
    """키움증권 토큰 매니저"""

    def __init__(self):
        super().__init__(broker_type=BrokerType.KIWOOM)

    @property
    def base_url(self) -> str:
        return 'https://api.kiwoom.com'

    @property
    def app_key(self) -> str:
        return config.KIWOOM_APP_KEY

    @property
    def app_secret(self) -> str:
        return config.KIWOOM_SECRET_KEY

    async def issue_access_token(self) -> dict:
        """Kiwoom 토큰 발급"""
        url = f'{self.base_url}/oauth2/token'
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        params = {
            'grant_type': 'client_credentials',
            'appkey': self.app_key,
            'secretkey': self.app_secret,
        }

        try:
            logger.info('[KIWOOM] 액세스 토큰 발급 요청 중...')
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=params) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        raise KiwoomAuthException(
                            f'토큰 발급 실패: HTTP {response.status} - {error_text}'
                        )

                    resp_json = await response.json()
                    if (
                        'return_code' not in resp_json
                        or int(resp_json['return_code']) != 0
                    ):
                        error_message = resp_json.get('return_msg', '알 수 없는 오류')
                        raise KiwoomAuthException(f'토큰 발급 실패: {error_message}')

                    self.token_type = resp_json.get('token_type')
                    self.token = resp_json.get('token')
                    self.expires_dt = resp_json.get('expires_dt')

                    if not self.token:
                        raise KiwoomAuthException(
                            '응답에서 액세스 토큰을 찾을 수 없습니다.'
                        )

                    logger.info(
                        f'[KIWOOM] 발급된 토큰: {self.token[:20]}... (만료: {self.expires_dt})'
                    )
                    await self._save_token_to_db()
                    logger.info('[KIWOOM] 액세스 토큰 발급 완료')

                    return {
                        'token': self.token,
                        'expires_dt': self.expires_dt,
                        'token_type': self.token_type,
                    }
        except aiohttp.ClientError as e:
            raise KiwoomAuthException(f'토큰 발급 네트워크 오류: {str(e)}')
        except Exception as e:
            raise KiwoomAuthException(f'토큰 발급 실패: {str(e)}')

    async def discard_token(self):
        """토큰을 폐기합니다. (버그 수정: DB 삭제 로직 추가)"""
        if not self.token or not self.expires_dt:
            logger.warning('[KIWOOM] 폐기할 토큰이 없습니다.')
            self.token = None
            self.expires_dt = None
            return

        url = f'{self.base_url}/oauth2/revoke'
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        params = {
            'appkey': self.app_key,
            'secretkey': self.app_secret,
            'token': self.token,
        }

        try:
            logger.info('[KIWOOM] 액세스 토큰 폐기 요청 중...')
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=params) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        raise KiwoomAuthException(
                            f'토큰 폐기 실패: HTTP {response.status} - {error_text}'
                        )

                    resp_json = await response.json()
                    return_code = int(resp_json.get('return_code', -1))
                    logger.info(f'[KIWOOM] 토큰 폐기 응답: {resp_json}')

                    if return_code != 0:
                        raise KiwoomAuthException(
                            f"토큰 폐기 실패: {resp_json.get('return_msg', '알 수 없는 오류')}"
                        )

                    # 버그 수정: DB에서 토큰 삭제
                    await self._clear_token_from_db()
                    logger.info('[KIWOOM] 액세스 토큰 폐기 완료')

        except aiohttp.ClientError as e:
            raise KiwoomAuthException(f'토큰 폐기 네트워크 오류: {str(e)}')
        except Exception as e:
            raise KiwoomAuthException(f'토큰 폐기 실패: {str(e)}')

    def _is_token_expire_soon(self) -> bool:
        """만료 임박 여부 (1시간 전) - Kiwoom 형식: YYYYMMDDHHMMSS"""
        if not self.expires_dt:
            return True

        try:
            expire_time = datetime.strptime(self.expires_dt, '%Y%m%d%H%M%S')
            return (expire_time - datetime.now()).total_seconds() <= 3600
        except Exception as e:
            logger.warning(f'[KIWOOM] 토큰 만료 시간 파싱 오류: {e}')
            return True

    def _create_auth_exception(self, message: str) -> Exception:
        return KiwoomAuthException(message)
