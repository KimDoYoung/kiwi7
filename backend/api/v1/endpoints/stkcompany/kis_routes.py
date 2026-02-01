"""
KIS(한국투자증권) API 라우트
"""

from fastapi import APIRouter

from backend.core.config import config
from backend.core.exceptions import KisApiException
from backend.core.logger import get_logger
from backend.domains.services.prev_price_cache import get_prev_price_cache
from backend.domains.stkcompanys.kis.kis_service import get_kis_api, get_kis_token_manager
from backend.domains.stkcompanys.kis.models.kis_schema import KisApiHelper, KisRequest, KisResponse

router = APIRouter()
logger = get_logger(__name__)


@router.post('/{api_id}', response_model=KisResponse)
async def kis_rest_api(api_id: str, req: KisRequest):
    """KIS REST API 호출"""
    title = req.title
    logger.info(f'[KIS] API 요청: api_id={api_id}, title={title}')

    try:
        kis = await get_kis_api()
        if not kis:
            return KisApiHelper.create_error_response(
                error_code='999', error_message='KIS API 인스턴스 생성 실패'
            )

        # URL path의 api_id로 업데이트
        req.api_id = api_id
        # req.payload의 CANO는 config에서 주입
        req.payload['CANO'] = config.KIS_ACCT_NO[:8]
        req.payload['ACNT_PRDT_CD'] = config.KIS_ACCT_PRDT_CD
        # payload 유효성 검증
        validation_errors = req.validate_payload()
        if validation_errors:
            return KisApiHelper.create_error_response(
                error_code='400', error_message=f'요청 검증 실패: {", ".join(validation_errors)}'
            )

        # API 요청
        response = await kis.send_request(req)

        # 성공 시 한글 필드명으로 변환
        if response.success and response.data:
            korea_data = KisApiHelper.to_korea_data(response.data, api_id)
            response.data = korea_data
            if title == 'stocklist':
                # logger.info(f'[KIS] 보유종목 데이터 변환 완료: {korea_data}')
                await insert_prev_costs_kis(response.data.get('output1', []))
        return response

    except KisApiException as e:
        logger.error(f'[KIS] API 예외: {e}')
        return KisApiHelper.create_error_response(
            error_code=e.error_code or '999', error_message=str(e)
        )
    except Exception as e:
        logger.error(f'[KIS] 오류: {e}')
        return KisApiHelper.create_error_response(
            error_code='999', error_message=f'Internal server error: {str(e)}'
        )


async def insert_prev_costs_kis(stock_list: list):
    """보유종목 데이터에 이전 매입 단가 삽입"""
    cache = get_prev_price_cache()
    for stock in stock_list:
        stk_cd = stock.get('상품번호')
        # A005930 형태에서 005930 형태로 변환
        if stk_cd and len(stk_cd) == 7 and stk_cd.startswith('A'):
            stk_cd = stk_cd[1:]
        price = await cache.get_last_price(stk_cd)
        trend = await cache.get_last_trend(stk_cd)
    
        stock['전일종가'] = price if price else 0
        stock['가격추세'] = trend if trend else '-'


@router.get('/issue-new-token', response_model=KisResponse)
async def issue_new_token():
    """새로운 토큰 발급"""
    logger.info('[KIS] 토큰 재발급 요청')

    try:
        token_manager = await get_kis_token_manager()
        await token_manager.discard_token()
        result = await token_manager.issue_access_token()

        return KisApiHelper.create_success_response(
            data={
                'message': '새로운 토큰이 발급되었습니다.',
                'expires_dt': result.get('expires_dt'),
            },
            api_info={'api_id': 'issue_new_token', 'title': '토큰 발급'},
        )
    except KisApiException as e:
        logger.error(f'[KIS] 토큰 발급 예외: {e}')
        return KisApiHelper.create_error_response(
            error_code=e.error_code or '999', error_message=str(e)
        )
    except Exception as e:
        logger.error(f'[KIS] 토큰 발급 오류: {e}')
        return KisApiHelper.create_error_response(error_code='999', error_message=str(e))


@router.get('/token-info', response_model=KisResponse)
async def get_token_info():
    """현재 토큰 정보 조회"""
    try:
        token_manager = await get_kis_token_manager()

        return KisApiHelper.create_success_response(
            data={
                'has_token': bool(token_manager.token),
                'expires_dt': token_manager.expires_dt,
                'token_type': token_manager.token_type,
                'is_virtual': token_manager.is_virtual,
            },
            api_info={'api_id': 'token_info', 'title': '토큰 정보'},
        )
    except Exception as e:
        logger.error(f'[KIS] 토큰 정보 조회 오류: {e}')
        return KisApiHelper.create_error_response(error_code='999', error_message=str(e))


@router.post('/hashkey', response_model=KisResponse)
async def get_hashkey(payload: dict):
    """해시키 생성 (주문 시 필요)"""
    logger.info('[KIS] 해시키 생성 요청')

    try:
        kis = await get_kis_api()
        hashkey = await kis.get_hashkey(payload)

        return KisApiHelper.create_success_response(
            data={'hashkey': hashkey}, api_info={'api_id': 'hashkey', 'title': '해시키 생성'}
        )
    except KisApiException as e:
        logger.error(f'[KIS] 해시키 생성 예외: {e}')
        return KisApiHelper.create_error_response(
            error_code=e.error_code or '999', error_message=str(e)
        )
    except Exception as e:
        logger.error(f'[KIS] 해시키 생성 오류: {e}')
        return KisApiHelper.create_error_response(error_code='999', error_message=str(e))
