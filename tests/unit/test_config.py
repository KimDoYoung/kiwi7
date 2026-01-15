"""
Config 모듈 단위 테스트
"""
import pytest
from backend.core.config import Config


@pytest.mark.unit
def test_config_default_values():
    """Config 기본값 테스트"""
    config = Config()
    
    assert config.VERSION is not None
    assert config.TIME_ZONE == "Asia/Seoul"
    assert config.BASE_DIR is not None


@pytest.mark.unit
def test_config_kiwoom_settings():
    """키움증권 설정 테스트"""
    config = Config()
    
    assert hasattr(config, 'KIWOOM_APP_KEY')
    assert hasattr(config, 'KIWOOM_SECRET_KEY')
    assert hasattr(config, 'KIWOOM_BASE_URL')
    assert config.KIWOOM_BASE_URL == 'https://api.kiwoom.com'


@pytest.mark.unit
def test_config_kis_virtual_mode():
    """한국투자증권 가상/실제 모드 테스트"""
    import os
    
    # 가상 모드 테스트
    os.environ['KIS_IS_VIRTUAL'] = 'true'
    config = Config()
    assert config.KIS_IS_VIRTUAL is True
    assert 'vts' in config.KIS_BASE_URL.lower()
    
    # 실제 모드 테스트
    os.environ['KIS_IS_VIRTUAL'] = 'false'
    config = Config()
    assert config.KIS_IS_VIRTUAL is False
