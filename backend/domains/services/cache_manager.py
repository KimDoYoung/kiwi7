# cache_manager.py
"""
Singleton 패턴의 캐시 매니저

stk_cache 테이블을 간단한 key-value 인터페이스로 관리합니다.
- 내부적으로 (stk_cd, name) 조합을 사용
- 8시간 만료 정책 자동 적용
- put, get, clear 등의 간단한 API 제공
- CacheKey Enum으로 타입 안전한 캐시 키 관리
"""
from typing import Optional, Union
from backend.core.logger import get_logger
from backend.domains.services.dependency import get_service
from backend.domains.services.cache_keys import CacheKey
import json

logger = get_logger(__name__)


class CacheManager:
    """
    Singleton 캐시 매니저

    stk_cache 서비스를 래핑하여 간단한 인터페이스 제공
    """
    _instance: Optional["CacheManager"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._cache_service = get_service("stk_cache")
        self._initialized = True
        logger.info("CacheManager 싱글톤 초기화 완료")

    @classmethod
    def get_instance(cls) -> "CacheManager":
        """싱글톤 인스턴스 반환"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    async def put(
        self, stk_cd: str, name: Union[str, CacheKey], value: str
    ) -> bool:
        """
        캐시에 데이터 저장 (생성 또는 업데이트)

        Args:
            stk_cd: 종목코드 (예: 005930)
            name: 캐시 이름 (예: CacheKey.STK_INFO_KA10100 또는 "stk_info_ka10100")
            value: 캐시 값 (JSON 문자열)

        Returns:
            성공 여부
        """
        try:
            name_str = name.value if isinstance(name, CacheKey) else name
            await self._cache_service.upsert(stk_cd, name_str, value)
            logger.debug(f"캐시 저장 완료: {stk_cd}/{name_str}")
            return True
        except Exception as e:
            logger.error(f"캐시 저장 실패 {stk_cd}/{name}: {e}")
            return False

    async def get(
        self, stk_cd: str, name: Union[str, CacheKey]
    ) -> Optional[str]:
        """
        캐시에서 데이터 조회

        8시간 내의 데이터만 반환 (자동 만료 정책)

        Args:
            stk_cd: 종목코드 (예: 005930)
            name: 캐시 이름 (예: CacheKey.STK_INFO_KA10100 또는 "stk_info_ka10100")

        Returns:
            캐시 값 (JSON 문자열) 또는 None
        """
        try:
            name_str = name.value if isinstance(name, CacheKey) else name
            cache_data = (
                await self._cache_service.get_by_stock_and_name(
                    stk_cd, name_str
                )
            )
            if cache_data:
                logger.debug(f"캐시 히트: {stk_cd}/{name_str}")
                return cache_data.value
            logger.debug(f"캐시 미스: {stk_cd}/{name_str}")
            return None
        except Exception as e:
            logger.error(f"캐시 조회 실패 {stk_cd}/{name}: {e}")
            return None

    async def get_dict(
        self, stk_cd: str, name: Union[str, CacheKey]
    ) -> Optional[dict]:
        """
        캐시에서 데이터 조회 (자동 JSON 파싱)

        JSON 문자열을 자동으로 파싱하여 dict로 반환
        파싱 실패 시 손상된 캐시 자동 삭제

        Args:
            stk_cd: 종목코드
            name: 캐시 이름 (예: CacheKey.STK_INFO_KA10100 또는 "stk_info_ka10100")

        Returns:
            파싱된 dict 또는 None
        """
        value = await self.get(stk_cd, name)
        if not value:
            return None

        try:
            return json.loads(value)
        except (json.JSONDecodeError, TypeError) as e:
            name_str = name.value if isinstance(name, CacheKey) else name
            logger.error(
                f"캐시 JSON 파싱 실패 {stk_cd}/{name_str}: {e}"
            )
            # 손상된 캐시 삭제
            cache_data = (
                await self._cache_service.get_by_stock_and_name(
                    stk_cd, name_str
                )
            )
            if cache_data:
                await self._cache_service.delete(cache_data.id)
                logger.info(
                    f"손상된 캐시 삭제됨: {stk_cd}/{name_str}"
                )
            return None

    async def clear(
        self, stk_cd: str, name: Union[str, CacheKey]
    ) -> bool:
        """
        특정 캐시 삭제

        Args:
            stk_cd: 종목코드
            name: 캐시 이름 (예: CacheKey.STK_INFO_KA10100 또는 "stk_info_ka10100")

        Returns:
            삭제 성공 여부
        """
        try:
            name_str = name.value if isinstance(name, CacheKey) else name
            # stk_cd와 name으로 데이터 찾기
            caches = await self._cache_service.list_all(
                filter_data=None
            )
            for cache in caches:
                if cache.stk_cd == stk_cd and cache.name == name_str:
                    await self._cache_service.delete(cache.id)
                    logger.info(f"캐시 삭제 완료: {stk_cd}/{name_str}")
                    return True
            return False
        except Exception as e:
            logger.error(f"캐시 삭제 실패 {stk_cd}/{name}: {e}")
            return False

    async def clear_stock(self, stk_cd: str) -> bool:
        """
        특정 종목의 모든 캐시 삭제

        Args:
            stk_cd: 종목코드

        Returns:
            삭제 성공 여부
        """
        try:
            await self._cache_service.delete_by_stock(stk_cd)
            logger.info(f"종목 캐시 전체 삭제: {stk_cd}")
            return True
        except Exception as e:
            logger.error(f"종목 캐시 삭제 실패 {stk_cd}: {e}")
            return False

    async def clear_name(
        self, name: Union[str, CacheKey]
    ) -> bool:
        """
        특정 캐시명의 모든 데이터 삭제

        Args:
            name: 캐시 이름 (예: CacheKey.STK_INFO_KA10100 또는 "stk_info_ka10100")

        Returns:
            삭제 성공 여부
        """
        try:
            name_str = name.value if isinstance(name, CacheKey) else name
            await self._cache_service.delete_by_name(name_str)
            logger.info(f"캐시명 전체 삭제: {name_str}")
            return True
        except Exception as e:
            logger.error(f"캐시명 삭제 실패 {name}: {e}")
            return False

    async def clear_all(self) -> bool:
        """
        전체 캐시 삭제

        Returns:
            삭제 성공 여부
        """
        try:
            caches = await self._cache_service.list_all()
            for cache in caches:
                await self._cache_service.delete(cache.id)
            logger.info("전체 캐시 삭제 완료")
            return True
        except Exception as e:
            logger.error(f"전체 캐시 삭제 실패: {e}")
            return False

    async def get_stats(self) -> dict:
        """
        캐시 통계 정보 반환

        Returns:
            전체 캐시 개수, 고유 종목 수, 고유 캐시명 수 등
        """
        try:
            return await self._cache_service.get_stats()
        except Exception as e:
            logger.error(f"캐시 통계 조회 실패: {e}")
            return {}
