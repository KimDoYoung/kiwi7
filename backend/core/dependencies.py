"""
설정 서비스 의존성 주입 모듈
순환 import를 방지하기 위해 별도로 분리된 모듈

작성자: 김도영
작성일: 2025-08-22
"""

from backend.domains.settings.settings_service import SettingsService

def get_settings_service():
    """설정 서비스 인스턴스를 반환하는 함수"""
    return SettingsService()
