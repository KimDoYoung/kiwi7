"""
홈 라우터 API 테스트
"""
import pytest
from fastapi import status


@pytest.mark.api
def test_read_root(client):
    """루트 경로 테스트"""
    response = client.get("/")
    
    # 로그인 페이지로 리다이렉트되거나 200 응답을 받아야 함
    assert response.status_code in [status.HTTP_200_OK, status.HTTP_307_TEMPORARY_REDIRECT]


@pytest.mark.api
def test_health_check(client):
    """헬스체크 엔드포인트가 있다면 테스트"""
    # 헬스체크 엔드포인트가 구현되어 있다면 주석 해제
    # response = client.get("/health")
    # assert response.status_code == status.HTTP_200_OK
    # assert response.json() == {"status": "ok"}
    pass


@pytest.mark.api
@pytest.mark.skip(reason="JWT 인증 구현 필요")
def test_protected_endpoint_without_auth(client):
    """인증 없이 보호된 엔드포인트 접근 테스트"""
    response = client.get("/api/v1/settings/list")
    
    # 인증 없이 접근 시 401 응답을 받아야 함
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
