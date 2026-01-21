"""
계좌관련 API 엔드포인트
"""

from fastapi import APIRouter

from backend.core.logger import get_logger
from backend.utils.acct_summary import (
    get_kiwoom_account_summary,
    get_kis_account_summary,
    get_ls_account_summary,
    get_summary_json,
)

logger = get_logger(__name__)

router = APIRouter()


@router.get('/summary')
async def get_summary():
    """계좌 요약 정보 조회"""
    logger.info('계좌 요약 정보 조회 요청 받음')

    accounts = []

    # 각 증권사별 계좌 조회
    kiwoom_account = await get_kiwoom_account_summary()
    if kiwoom_account:
        accounts.append(kiwoom_account)

    kis_account = await get_kis_account_summary()
    if kis_account:
        accounts.append(kis_account)

    ls_account = await get_ls_account_summary()
    if ls_account:
        accounts.append(ls_account)

    # 결과 반환
    if accounts:
        return get_summary_json(accounts)
    else:
        logger.error('조회된 계좌가 없습니다.')
        return {'summary': {}, 'accounts': {}}
