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
def test_config_kis_urls():
    """한국투자증권 URL 설정 테스트"""
    config = Config()
    assert hasattr(config, 'KIS_BASE_URL')
    assert hasattr(config, 'KIS_WS_URL')
    assert config.KIS_BASE_URL == 'https://openapi.koreainvestment.com:9443'
    assert config.KIS_WS_URL == 'ws://ops.koreainvestment.com:21000'
