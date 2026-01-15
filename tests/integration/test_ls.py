"""
LS증권 API 통합 테스트
"""
import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from datetime import datetime, timedelta

from backend.domains.ls.managers.ls_token_manager import LsTokenManager
from backend.core.exceptions import LsAuthException


@pytest.fixture
def mock_ls_token_response():
    """LS증권 토큰 발급 성공 응답 mock"""
    return {
        "access_token": "mock_ls_access_token_1234567890abcdef",
        "token_type": "Bearer",
        "expires_in": 86400  # 24시간
    }


@pytest.fixture
async def ls_token_manager():
    """테스트용 LS증권 토큰 매니저"""
    manager = LsTokenManager()
    yield manager
    # 테스트 후 정리
    if manager.token:
        try:
            await manager._clear_token_from_db()
        except:
            pass


@pytest.mark.integration
@pytest.mark.asyncio
async def test_issue_access_token_success(ls_token_manager, mock_ls_token_response):
    """LS증권 토큰 발급 성공 테스트"""
    # aiohttp 응답 mock
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json = AsyncMock(return_value=mock_ls_token_response)
    
    # aiohttp.ClientSession mock
    mock_session = MagicMock()
    mock_session.post = MagicMock()
    mock_session.post.return_value.__aenter__ = AsyncMock(return_value=mock_response)
    mock_session.post.return_value.__aexit__ = AsyncMock(return_value=None)
    
    with patch('aiohttp.ClientSession') as mock_client:
        mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_client.return_value.__aexit__ = AsyncMock(return_value=None)
        
        # 토큰 발급 실행
        result = await ls_token_manager.issue_access_token()
        
        # 검증
        assert result['token'] == mock_ls_token_response['access_token']
        assert result['token_type'] == "Bearer"
        
        # 만료 시간 검증 (expires_in 만큼 더해졌는지 확인)
        expected_expiry_dt = datetime.now() + timedelta(seconds=mock_ls_token_response['expires_in'])
        actual_expiry_dt = datetime.strptime(result['expires_dt'], '%Y-%m-%d %H:%M:%S')
        assert abs((expected_expiry_dt - actual_expiry_dt).total_seconds()) < 5  # 5초 이내 오차 허용

        # 매니저 상태 검증
        assert ls_token_manager.token == mock_ls_token_response['access_token']
        assert ls_token_manager.expires_dt == result['expires_dt']


@pytest.mark.integration
@pytest.mark.asyncio
async def test_issue_access_token_error_response(ls_token_manager):
    """LS증권 토큰 발급 실패 응답 테스트"""
    # 에러 응답 mock
    error_response = {
        "error": "invalid_client",
        "error_description": "유효하지 않은 클라이언트 정보"
    }
    
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json = AsyncMock(return_value=error_response)
    
    mock_session = MagicMock()
    mock_session.post = MagicMock()
    mock_session.post.return_value.__aenter__ = AsyncMock(return_value=mock_response)
    mock_session.post.return_value.__aexit__ = AsyncMock(return_value=None)
    
    with patch('aiohttp.ClientSession') as mock_client:
        mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_client.return_value.__aexit__ = AsyncMock(return_value=None)
        
        # 예외 발생 검증
        with pytest.raises(LsAuthException) as exc_info:
            await ls_token_manager.issue_access_token()
        
        assert "유효하지 않은 클라이언트 정보" in str(exc_info.value)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_issue_access_token_http_error(ls_token_manager):
    """LS증권 토큰 발급 HTTP 오류 테스트"""
    # HTTP 500 에러 mock
    mock_response = AsyncMock()
    mock_response.status = 500
    mock_response.text = AsyncMock(return_value="Internal Server Error")
    
    mock_session = MagicMock()
    mock_session.post = MagicMock()
    mock_session.post.return_value.__aenter__ = AsyncMock(return_value=mock_response)
    mock_session.post.return_value.__aexit__ = AsyncMock(return_value=None)
    
    with patch('aiohttp.ClientSession') as mock_client:
        mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_client.return_value.__aexit__ = AsyncMock(return_value=None)
        
        # 예외 발생 검증
        with pytest.raises(LsAuthException) as exc_info:
            await ls_token_manager.issue_access_token()
        
        assert "토큰 발급 실패" in str(exc_info.value)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_get_token_with_cache(ls_token_manager, mock_ls_token_response):
    """캐시된 토큰 조회 테스트"""
    # 먼저 토큰 발급
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json = AsyncMock(return_value=mock_ls_token_response)
    
    mock_session = MagicMock()
    mock_session.post = MagicMock()
    mock_session.post.return_value.__aenter__ = AsyncMock(return_value=mock_response)
    mock_session.post.return_value.__aexit__ = AsyncMock(return_value=None)
    
    with patch('aiohttp.ClientSession') as mock_client:
        mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_client.return_value.__aexit__ = AsyncMock(return_value=None)
        
        # 첫 번째 토큰 발급
        await ls_token_manager.issue_access_token()
        
        # 캐시된 토큰 조회 (새로 발급하지 않음)
        token = await ls_token_manager.get_token()
        
        # 검증
        assert token == mock_ls_token_response['access_token']
        # post가 한 번만 호출되었는지 확인 (캐시 사용)
        assert mock_session.post.call_count == 1


@pytest.mark.integration
@pytest.mark.asyncio
async def test_discard_token_success(ls_token_manager, mock_ls_token_response):
    """토큰 폐기 성공 테스트"""
    # 먼저 토큰 설정
    ls_token_manager.token = mock_ls_token_response['access_token']
    
    # 폐기 응답 mock
    mock_response = AsyncMock()
    mock_response.status = 200
    
    mock_session = MagicMock()
    mock_session.post = MagicMock()
    mock_session.post.return_value.__aenter__ = AsyncMock(return_value=mock_response)
    mock_session.post.return_value.__aexit__ = AsyncMock(return_value=None)
    
    with patch('aiohttp.ClientSession') as mock_client:
        mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_client.return_value.__aexit__ = AsyncMock(return_value=None)
        
        # 토큰 폐기
        await ls_token_manager.discard_token()
        
        # post가 호출되었는지 확인
        mock_session.post.assert_called_once()


@pytest.mark.integration
@pytest.mark.asyncio
async def test_real_ls_token_issue():
    """실제 LS증권 API 토큰 발급 테스트 (수동 실행)"""
    
    # 실제 환경 변수가 설정되어 있어야 함
    manager = LsTokenManager()
    
    try:
        result = await manager.issue_access_token()
        
        assert result['token'] is not None
        assert result['expires_dt'] is not None
        print(f"✅ 토큰 발급 성공: {result['token'][:20]}...")
        print(f"✅ 만료 시간: {result['expires_dt']}")
        
        # 발급된 토큰으로 조회 테스트
        token = await manager.get_token()
        assert token == result['token']
        
    finally:
        # 테스트 후 토큰 폐기
        await manager.discard_token()
