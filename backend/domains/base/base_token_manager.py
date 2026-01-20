"""
토큰 매니저 베이스 클래스
증권사별 토큰 관리의 공통 기능을 제공합니다.
"""
from abc import ABC, abstractmethod
from typing import Optional

from backend.domains.services.dependency import get_service
from backend.core.logger import get_logger
from backend.domains.stock_api import BrokerType

logger = get_logger(__name__)


class BaseTokenManager(ABC):
    """토큰 관리 공통 추상 클래스"""

    def __init__(self, broker_type: BrokerType):
        """
        Args:
            broker_type: BrokerType enum (KIWOOM, KIS, LS)
        """
        self.broker_type = broker_type
        self.broker_name = broker_type.value  # "kiwoom", "kis", "ls"
        self.tokens_service = get_service('tokens')

        self.token_type: Optional[str] = None
        self.token: Optional[str] = None
        self.expires_dt: Optional[str] = None

    @property
    @abstractmethod
    def base_url(self) -> str:
        """토큰 발급 API 베이스 URL"""
        pass

    @property
    @abstractmethod
    def app_key(self) -> str:
        """앱 키"""
        pass

    @property
    @abstractmethod
    def app_secret(self) -> str:
        """시크릿 키"""
        pass

    async def get_token(self) -> str:
        """유효한 토큰 반환"""
        await self.refresh_token()
        return self.token

    async def refresh_token(self) -> bool:
        """토큰 갱신 (만료 임박 시 재발급)"""
        try:
            if not self.token or not self.expires_dt:
                await self._load_token_from_db()

            if not self.token or not self.expires_dt:
                logger.info(f'[{self.broker_name}] 저장된 토큰이 없어 새로 발급받습니다.')
                await self.issue_access_token()
                return True

            if self._is_token_expire_soon():
                logger.info(f'[{self.broker_name}] 토큰 만료 임박, 재발급합니다.')
                await self.issue_access_token()

            return True
        except Exception as e:
            logger.error(f'[{self.broker_name}] 토큰 갱신 오류: {e}')
            raise self._create_auth_exception(f'토큰 갱신 실패: {e}')

    @abstractmethod
    async def issue_access_token(self) -> dict:
        """토큰 발급 - 증권사별 구현"""
        pass

    @abstractmethod
    async def discard_token(self):
        """토큰 폐기 - 증권사별 구현"""
        pass

    @abstractmethod
    def _is_token_expire_soon(self) -> bool:
        """만료 임박 여부 확인 - 증권사별 날짜 형식 다름"""
        pass

    @abstractmethod
    def _create_auth_exception(self, message: str) -> Exception:
        """인증 예외 생성 - 증권사별 예외 클래스"""
        pass

    async def _load_token_from_db(self):
        """DB에서 토큰 로드 (tokens 테이블 사용)"""
        token_record = await self.tokens_service.get_by_broker(
            self.broker_type.name
        )

        if token_record:
            self.token = token_record.access_token
            self.expires_dt = token_record.expires_at
            logger.info(f'[{self.broker_name}] 토큰 로드 완료: {self.token[:10]}...')
        else:
            self.token = None
            self.expires_dt = None

    async def _save_token_to_db(self):
        """DB에 토큰 저장 (tokens 테이블 사용)"""
        await self.tokens_service.upsert(
            broker_type=self.broker_type.name,
            access_token=self.token,
            expires_at=self.expires_dt
        )
        logger.info(f'[{self.broker_name}] 토큰 저장 완료')

    async def _clear_token_from_db(self):
        """DB에서 토큰 삭제 (tokens 테이블 사용)"""
        await self.tokens_service.delete_by_broker(self.broker_type.name)

        self.token = None
        self.expires_dt = None
        self.token_type = None

        logger.info(f'[{self.broker_name}] 토큰 삭제 완료')
