"""
KIS(한국투자증권) API 통합 테스트
"""
import pytest
from unittest.mock import AsyncMock, patch, MagicMock

from backend.domains.kis.managers.kis_token_manager import KisTokenManager
from backend.core.exceptions import KisAuthException


@pytest.fixture
def mock_kis_token_response():
    """KIS 토큰 발급 성공 응답 mock"""
    return {
        "access_token": "mock_kis_access_token_1234567890abcdef",
        "token_type": "Bearer",
        "access_token_token_expired": "2026-01-16 12:30:00",
        "expires_in": 86400
    }


@pytest.fixture
def mock_kis_approval_response():
    """KIS WebSocket 승인키 응답 mock"""
    return {
        "approval_key": "mock_approval_key_abcd1234"
    }


@pytest.fixture
async def kis_token_manager(test_db_path):
    """테스트용 KIS 토큰 매니저"""
    # DB 경로를 테스트용으로 설정
    with patch('backend.core.config.config.DB_PATH', str(test_db_path)):
        manager = KisTokenManager()
        yield manager
        # 테스트 후 정리
        if manager.token:
            try:
                await manager._clear_token_from_db()
            except:
                pass


@pytest.mark.integration
@pytest.mark.asyncio
async def test_issue_access_token_success(kis_token_manager, mock_kis_token_response):
    """KIS 토큰 발급 성공 테스트"""
    # aiohttp 응답 mock
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json = AsyncMock(return_value=mock_kis_token_response)
    
    # aiohttp.ClientSession mock
    mock_session = MagicMock()
    mock_session.post = MagicMock()
    mock_session.post.return_value.__aenter__ = AsyncMock(return_value=mock_response)
    mock_session.post.return_value.__aexit__ = AsyncMock(return_value=None)
    
    with patch('aiohttp.ClientSession') as mock_client:
        mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_client.return_value.__aexit__ = AsyncMock(return_value=None)
        
        # 토큰 발급 실행
        result = await kis_token_manager.issue_access_token()
        
        # 검증
        assert result['token'] == mock_kis_token_response['access_token']
        assert result['expires_dt'] == mock_kis_token_response['access_token_token_expired']
        assert result['token_type'] == "Bearer"
        
        # 매니저 상태 검증
        assert kis_token_manager.token == mock_kis_token_response['access_token']
        assert kis_token_manager.expires_dt == mock_kis_token_response['access_token_token_expired']


@pytest.mark.integration
@pytest.mark.asyncio
async def test_issue_access_token_error_response(kis_token_manager):
    """KIS 토큰 발급 실패 응답 테스트"""
    # 에러 응답 mock
    error_response = {
        "error_code": "INVALID_APP_KEY",
        "error_description": "유효하지 않은 앱 키입니다"
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
        with pytest.raises(KisAuthException) as exc_info:
            await kis_token_manager.issue_access_token()
        
        assert "유효하지 않은 앱 키입니다" in str(exc_info.value)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_issue_access_token_http_error(kis_token_manager):
    """KIS 토큰 발급 HTTP 오류 테스트"""
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
        with pytest.raises(KisAuthException) as exc_info:
            await kis_token_manager.issue_access_token()
        
        assert "토큰 발급 실패" in str(exc_info.value)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_get_token_with_cache(kis_token_manager, mock_kis_token_response):
    """캐시된 토큰 조회 테스트"""
    # 먼저 토큰 발급
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json = AsyncMock(return_value=mock_kis_token_response)
    
    mock_session = MagicMock()
    mock_session.post = MagicMock()
    mock_session.post.return_value.__aenter__ = AsyncMock(return_value=mock_response)
    mock_session.post.return_value.__aexit__ = AsyncMock(return_value=None)
    
    with patch('aiohttp.ClientSession') as mock_client:
        mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_client.return_value.__aexit__ = AsyncMock(return_value=None)
        
        # 첫 번째 토큰 발급
        await kis_token_manager.issue_access_token()
        
        # 캐시된 토큰 조회 (새로 발급하지 않음)
        token = await kis_token_manager.get_token()
        
        # 검증
        assert token == mock_kis_token_response['access_token']
        # post가 한 번만 호출되었는지 확인 (캐시 사용)
        assert mock_session.post.call_count == 1


@pytest.mark.integration
@pytest.mark.asyncio
async def test_get_approval_key_success(kis_token_manager, mock_kis_approval_response):
    """WebSocket 승인키 발급 성공 테스트"""
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json = AsyncMock(return_value=mock_kis_approval_response)
    
    mock_session = MagicMock()
    mock_session.post = MagicMock()
    mock_session.post.return_value.__aenter__ = AsyncMock(return_value=mock_response)
    mock_session.post.return_value.__aexit__ = AsyncMock(return_value=None)
    
    with patch('aiohttp.ClientSession') as mock_client:
        mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_client.return_value.__aexit__ = AsyncMock(return_value=None)
        
        # 승인키 발급
        approval_key = await kis_token_manager.get_approval_key()
        
        # 검증
        assert approval_key == mock_kis_approval_response['approval_key']


@pytest.mark.integration
@pytest.mark.asyncio
async def test_discard_token_success(kis_token_manager, mock_kis_token_response):
    """토큰 폐기 성공 테스트"""
    # 먼저 토큰 설정
    kis_token_manager.token = mock_kis_token_response['access_token']
    
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
        await kis_token_manager.discard_token()
        
        # post가 호출되었는지 확인
        mock_session.post.assert_called_once()


@pytest.mark.integration
@pytest.mark.asyncio
@pytest.mark.skip(reason="실제 KIS API 호출 필요 - 수동 테스트용")
async def test_real_kis_token_issue():
    """실제 KIS API 토큰 발급 테스트 (수동 실행)"""
    # 실제 환경 변수가 설정되어 있어야 함
    manager = KisTokenManager()
    
    try:
        result = await manager.issue_access_token()
        
        assert result['token'] is not None
        assert result['expires_dt'] is not None
        print(f"✅ 토큰 발급 성공: {result['token'][:20]}...")
        print(f"✅ 만료 시간: {result['expires_dt']}")
        
        # 발급된 토큰으로 조회 테스트
        token = await manager.get_token()
        assert token == result['token']
        
        # 승인키 발급 테스트
        approval_key = await manager.get_approval_key()
        assert approval_key is not None
        print(f"✅ 승인키 발급 성공: {approval_key[:20]}...")
        
    finally:
        # 테스트 후 토큰 폐기
        await manager.discard_token()
