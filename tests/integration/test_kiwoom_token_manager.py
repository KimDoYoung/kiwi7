"""
Kiwoom 토큰 매니저 통합 테스트
"""
import pytest
from unittest.mock import AsyncMock, patch

from backend.domains.stkcompanys.kiwoom.managers.kiwoom_token_manager import (
    KiwoomTokenManager,
)
from backend.core.exceptions import KiwoomAuthException


@pytest.fixture
def mock_kiwoom_token_response():
    """Kiwoom 토큰 발급 성공 응답 mock"""
    return {
        'return_code': '0',
        'return_msg': 'SUCCESS',
        'token': 'mock_kiwoom_token_1234567890abcdef',
        'token_type': 'Bearer',
        'expires_dt': '20260120143000',
    }


@pytest.fixture
async def kiwoom_token_manager():
    """테스트용 Kiwoom 토큰 매니저"""
    manager = KiwoomTokenManager()
    yield manager
    # 테스트 후 정리
    if manager.token:
        try:
            await manager._clear_token_from_db()
        except Exception:
            pass


@pytest.mark.integration
@pytest.mark.asyncio
async def test_kiwoom_issue_access_token_success(
    kiwoom_token_manager, mock_kiwoom_token_response
):
    """Kiwoom 토큰 발급 성공 테스트"""
    # aiohttp 응답 mock
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json = AsyncMock(return_value=mock_kiwoom_token_response)

    mock_session = AsyncMock()
    mock_session.post = AsyncMock(return_value=mock_response)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock()

    with patch('aiohttp.ClientSession', return_value=mock_session):
        result = await kiwoom_token_manager.issue_access_token()

        assert result['token'] == 'mock_kiwoom_token_1234567890abcdef'
        assert result['expires_dt'] == '20260120143000'
        assert kiwoom_token_manager.token == 'mock_kiwoom_token_1234567890abcdef'

        # DB에 저장 확인
        from backend.domains.services.dependency import get_service

        tokens_service = get_service('tokens')
        token = await tokens_service.get_by_broker('KIWOOM')
        assert token is not None
        assert token.access_token == 'mock_kiwoom_token_1234567890abcdef'


@pytest.mark.integration
@pytest.mark.asyncio
async def test_kiwoom_discard_token_success(kiwoom_token_manager):
    """Kiwoom 토큰 폐기 성공 테스트 (버그 수정 검증)"""
    # 먼저 토큰 저장
    kiwoom_token_manager.token = 'test_token_to_discard'
    kiwoom_token_manager.expires_dt = '20260120143000'
    await kiwoom_token_manager._save_token_to_db()

    # DB에 저장 확인
    from backend.domains.services.dependency import get_service

    tokens_service = get_service('tokens')
    token_before = await tokens_service.get_by_broker('KIWOOM')
    assert token_before is not None

    # 폐기 응답 mock
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json = AsyncMock(
        return_value={'return_code': '0', 'return_msg': 'SUCCESS'}
    )

    mock_session = AsyncMock()
    mock_session.post = AsyncMock(return_value=mock_response)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock()

    with patch('aiohttp.ClientSession', return_value=mock_session):
        await kiwoom_token_manager.discard_token()

        # 버그 수정 검증: DB에서 토큰이 삭제되었는지 확인
        token_after = await tokens_service.get_by_broker('KIWOOM')
        assert token_after is None, '토큰이 DB에서 삭제되지 않았습니다 (버그)'
        assert kiwoom_token_manager.token is None
        assert kiwoom_token_manager.expires_dt is None


@pytest.mark.integration
@pytest.mark.asyncio
async def test_kiwoom_token_refresh():
    """Kiwoom 토큰 갱신 테스트"""
    manager = KiwoomTokenManager()

    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.json = AsyncMock(
        return_value={
            'return_code': '0',
            'return_msg': 'SUCCESS',
            'token': 'refreshed_token_xyz',
            'token_type': 'Bearer',
            'expires_dt': '20260121143000',
        }
    )

    mock_session = AsyncMock()
    mock_session.post = AsyncMock(return_value=mock_response)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock()

    with patch('aiohttp.ClientSession', return_value=mock_session):
        # 토큰 갱신 (DB에서 로드 → 없으면 발급)
        result = await manager.refresh_token()

        assert result is True
        assert manager.token == 'refreshed_token_xyz'

        # 정리
        await manager._clear_token_from_db()
