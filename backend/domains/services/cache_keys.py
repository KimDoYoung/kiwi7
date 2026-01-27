# cache_keys.py
"""
캐시 매니저에서 사용되는 캐시 키(name) enum

stk_cache 테이블의 `name` 필드 값을 enum으로 관리하여:
- 타입 안정성 확보
- IDE 자동완성 지원
- 오타 방지
- 유지보수 편의성 증대
"""
from enum import Enum


class CacheKey(str, Enum):
    """
    캐시 데이터를 식별하는 키

    각 enum 값은 캐시되는 데이터의 타입/소스를 나타냅니다.
    str을 상속하면 문자열처럼 사용할 수 있으면서도 타입 안정성을 보장합니다.
    """

    # 종목정보 관련
    STK_INFO_KA10100 = "stk_info_ka10100"  # ka10100 API - 종목정보조회 결과

    def __str__(self) -> str:
        """문자열로 변환될 때 value 반환"""
        return self.value

    @classmethod
    def from_string(cls, value: str) -> "CacheKey":
        """
        문자열에서 CacheKey enum으로 변환

        Args:
            value: 캐시 키 문자열

        Returns:
            CacheKey enum 값

        Raises:
            ValueError: 유효하지 않은 캐시 키인 경우
        """
        for key in cls:
            if key.value == value:
                return key
        raise ValueError(f"유효하지 않은 캐시 키: {value}")
