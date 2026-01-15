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
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session")
def test_db(tmp_path_factory):
    """세션 스코프의 테스트 DB fixture"""
    from backend.core.kiwi7_db import create_kiwi7_db
    
    # 세션 전체에서 사용할 임시 디렉토리 생성
    db_dir = tmp_path_factory.mktemp("data")
    db_path = db_dir / "test_kiwi7.db"
    
    # DB 생성 및 테이블 스키마 적용
    create_kiwi7_db(str(db_path))
    
    return str(db_path)


@pytest.fixture(autouse=True)
def mock_db_path(monkeypatch, test_db):
    """모든 테스트에서 DB 경로를 테스트 DB로 설정"""
    monkeypatch.setattr('backend.core.config.config.DB_PATH', test_db)


@pytest.fixture
def mock_config(monkeypatch):
    """테스트용 설정을 적용하는 fixture"""
    monkeypatch.setenv('KIWOOM_APP_KEY', 'test_key')
    monkeypatch.setenv('KIWOOM_SECRET_KEY', 'test_secret')
    monkeypatch.setenv('KIS_APP_KEY', 'test_key')
    monkeypatch.setenv('KIS_SECRET_KEY', 'test_secret')
    monkeypatch.setenv('LS_APP_KEY', 'test_key')
    monkeypatch.setenv('LS_SECRET_KEY', 'test_secret')
