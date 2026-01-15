"""
pytest 설정 및 공통 fixture들
"""
import os
import sys
import pytest
from fastapi.testclient import TestClient
from pathlib import Path

# 프로젝트 루트를 Python path에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# 테스트 환경 설정
os.environ['KIWI7_MODE'] = 'test'

from backend.main import create_app


@pytest.fixture
def app():
    """FastAPI 앱 인스턴스를 반환하는 fixture"""
    return create_app()


@pytest.fixture
def client(app):
    """TestClient를 반환하는 fixture"""
    return TestClient(app)


@pytest.fixture
def test_db_path(tmp_path):
    """테스트용 임시 DB 경로를 반환하는 fixture"""
    return tmp_path / "test_kiwi7.db"


@pytest.fixture
def mock_config(monkeypatch):
    """테스트용 설정을 적용하는 fixture"""
    monkeypatch.setenv('KIWOOM_APP_KEY', 'test_key')
    monkeypatch.setenv('KIWOOM_SECRET_KEY', 'test_secret')
    monkeypatch.setenv('KIS_APP_KEY', 'test_key')
    monkeypatch.setenv('KIS_SECRET_KEY', 'test_secret')
    monkeypatch.setenv('LS_APP_KEY', 'test_key')
    monkeypatch.setenv('LS_SECRET_KEY', 'test_secret')
