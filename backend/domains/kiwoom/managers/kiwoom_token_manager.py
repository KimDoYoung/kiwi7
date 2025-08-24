

from datetime import datetime
from typing import Optional
import aiohttp
from backend.core.logger import get_logger
from backend.core.config import config
from backend.core.exceptions import KiwoomAuthException
from backend.domains.settings.settings_service import SettingsService


logger = get_logger(__name__)

class KiwoomTokenManager:
    def __init__(self, settings_service: Optional[SettingsService] = None):
        self.app_key = config.KIWOOM_APP_KEY
        self.app_secret = config.KIWOOM_SECRET_KEY
        self.base_url = "https://api.kiwoom.com"
        self.settings_service = settings_service or SettingsService()

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
                    if 'return_code' not in resp_json or int(resp_json['return_code']) != 0:
                        error_message = resp_json.get('return_msg', '알 수 없는 오류')
                        raise KiwoomAuthException(f"토큰 발급 실패: {error_message}")   
                    self.token_type = resp_json.get("token_type")
                    self.token = resp_json.get("token")
                    self.expires_dt = resp_json.get("expires_dt")
                    
                    if not self.token:
                        raise KiwoomAuthException("응답에서 액세스 토큰을 찾을 수 없습니다.")
                    logger.info(f"발급된 토큰: token[{self.token[:20]}], token_type:[{self.token_type}]... (만료 시간: {self.expires_dt})")
                    await self._save_token_to_db()
                    logger.info("키움 API 액세스 토큰 발급 완료")
                    return {
                        'token': self.token,
                        'expires_dt': self.expires_dt,
                        'token_type': self.token_type
                    }
        except aiohttp.ClientError as e:
            raise KiwoomAuthException(f"토큰 발급 네트워크 오류: {str(e)}")
        except Exception as e:
            raise KiwoomAuthException(f"토큰 발급 실패: {str(e)}")
    
    async def discard_token(self):
        """토큰을 폐기합니다."""
        if not self.token or not self.expires_dt:
            self.token = None
            self.expires_dt = None

            logger.warning("폐기할 토큰이 없습니다.")
            return
        url = f"{self.base_url}/oauth2/revoke"
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        params = {
            'appkey': self.app_key,
            'secretkey': self.app_secret,
            'token': self.token,
        }

        try:
            logger.info("키움 API 액세스 토큰 폐기 요청 중...")
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=params) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        raise KiwoomAuthException(f"토큰 폐기 실패: HTTP {response.status} - {error_text}")

                    resp_json = await response.json()
                    return_code = int(resp_json.get("return_code"))
                    logger.info(f"토큰 폐기 응답: {resp_json}")
                    if return_code != 0:
                        raise KiwoomAuthException(f"토큰 폐기 실패: {resp_json.get('return_msg', '알 수 없는 오류')}")
                    return 
                    # self.token = None
                    # self.expires_dt = None
                    # await self._save_token_to_db()
                    logger.info("키움 API 액세스 토큰 폐기 완료")
        except aiohttp.ClientError as e:
            raise KiwoomAuthException(f"토큰 폐기 네트워크 오류: {str(e)}")
        except Exception as e:
            raise KiwoomAuthException(f"토큰 폐기 실패: {str(e)}")


    def _is_token_expire_soon(self) -> bool:
        try:
            expire_time = datetime.strptime(self.expires_dt, '%Y%m%d%H%M%S')
            return (expire_time - datetime.now()).total_seconds() <= 3600
        except Exception as e:
            logger.warning(f"토큰 만료 시간 파싱 오류: {e}")
            return True

    async def _load_token_from_db(self):
        token_info = await self.settings_service.get("ACCESS_TOKEN")
        time_info = await self.settings_service.get("ACCESS_TOKEN_EXPIRED_TIME")
        self.token = token_info if token_info else None
        self.expires_dt = time_info if time_info else None
        logger.info("토큰 정보를 데이터베이스에서 로드했습니다. token: %s, expires_dt: %s", self.token[:10] if self.token else None, self.expires_dt)

    async def _save_token_to_db(self):
        await self.settings_service.set("ACCESS_TOKEN", self.token)
        await self.settings_service.set("ACCESS_TOKEN_EXPIRED_TIME", self.expires_dt)
        logger.info("토큰 정보를 데이터베이스에 저장했습니다. token: %s, expires_dt: %s", self.token[:10] if self.token else None, self.expires_dt)
