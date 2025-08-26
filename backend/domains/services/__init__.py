
"""
services domain package - 서비스 의존성 관리
"""
from .dependency import get_service# stocks domain package
# 외부 사용 가능 함수들
__all__ = [
    'SettingsKey',
    'get_service',
]