"""
TokensService 단위 테스트
"""
import pytest
from backend.domains.services.tokens_service import TokensService


@pytest.mark.unit
@pytest.mark.asyncio
async def test_upsert_and_get_token():
    """토큰 생성 및 조회 테스트"""
    service = TokensService()

    # 생성
    token = await service.upsert(
        broker_type='KIWOOM',
        access_token='test_token_12345',
        expires_at='20260120143000',
    )

    assert token.broker_type == 'KIWOOM'
    assert token.access_token == 'test_token_12345'
    assert token.expires_at == '20260120143000'

    # 조회
    retrieved = await service.get_by_broker('KIWOOM')
    assert retrieved is not None
    assert retrieved.access_token == 'test_token_12345'


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_token():
    """토큰 업데이트 테스트"""
    service = TokensService()

    # 생성
    token1 = await service.upsert(
        broker_type='KIS',
        access_token='token_v1',
        expires_at='2026-01-20 14:30:00',
    )

    created_at_v1 = token1.created_at

    # 업데이트
    token2 = await service.upsert(
        broker_type='KIS',
        access_token='token_v2',
        expires_at='2026-01-21 14:30:00',
    )

    assert token2.access_token == 'token_v2'
    assert token2.expires_at == '2026-01-21 14:30:00'
    assert token2.created_at == created_at_v1, 'created_at은 변경되지 않아야 함'


@pytest.mark.unit
@pytest.mark.asyncio
async def test_delete_token():
    """토큰 삭제 테스트"""
    service = TokensService()

    # 생성
    await service.upsert(
        broker_type='LS',
        access_token='ls_token',
        expires_at='2026-01-20 14:30:00',
    )

    # 삭제
    deleted = await service.delete_by_broker('LS')
    assert deleted is True

    # 삭제 확인
    deleted_token = await service.get_by_broker('LS')
    assert deleted_token is None


@pytest.mark.unit
@pytest.mark.asyncio
async def test_get_nonexistent_token():
    """존재하지 않는 토큰 조회 테스트"""
    service = TokensService()

    result = await service.get_by_broker('NONEXISTENT')
    assert result is None


@pytest.mark.unit
@pytest.mark.asyncio
async def test_delete_nonexistent_token():
    """존재하지 않는 토큰 삭제 테스트"""
    service = TokensService()

    result = await service.delete_by_broker('NONEXISTENT')
    assert result is False


@pytest.mark.unit
@pytest.mark.asyncio
async def test_broker_type_case_insensitive():
    """broker_type 대소문자 무시 테스트"""
    service = TokensService()

    # 소문자로 생성
    await service.upsert(
        broker_type='kiwoom',
        access_token='token123',
        expires_at='20260120143000',
    )

    # 대문자로 조회
    token = await service.get_by_broker('KIWOOM')
    assert token is not None
    assert token.broker_type == 'KIWOOM'

    # 소문자로 조회
    token = await service.get_by_broker('kiwoom')
    assert token is not None
    assert token.broker_type == 'KIWOOM'
