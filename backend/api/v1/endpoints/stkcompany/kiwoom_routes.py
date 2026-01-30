# APIRouter 인스턴스 생성
from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi import APIRouter

from backend.core.config import config
from backend.core.exceptions import KiwoomApiException
from backend.core.logger import get_logger
from backend.domains.market.open_time_checker import OpenTimeChecker
from backend.domains.services.prev_price_cache import get_prev_price_cache
from backend.domains.stkcompanys.kiwoom.kiwoom_service import get_kiwoom_api, get_token_manager
from backend.domains.stkcompanys.kiwoom.models.kiwoom_schema import (
    KiwoomApiHelper,
    KiwoomRequest,
    KiwoomResponse,
)
from backend.utils.naver_utils import get_jisu_from_naver

router = APIRouter()
logger = get_logger(__name__)


@router.post('/{api_id}', response_model=KiwoomResponse)
async def kiwoom_rest_api(api_id: str, req: KiwoomRequest):
    """kiwoom rest api 호출"""
    title = req.title
    logger.info(f'Received Kiwoom API request: api_id={api_id}, title={title}, req=[{req}]')

    try:
        kiwoom = await get_kiwoom_api()
        if not kiwoom:
            return KiwoomApiHelper.create_error_response(
                error_code='999', error_message='Kiwoom API 클래스를 생성하는데 실패했습니다'
            )

        # URL path의 api_id로 request body의 api_id 업데이트
        req.api_id = api_id

        # payload 유효성 검증 명시적 호출
        validation_errors = req.validate_payload()
        if validation_errors:
            return KiwoomApiHelper.create_error_response(
                error_code='400',
                error_message=f'요청 데이터 검증 실패: {", ".join(validation_errors)}',
            )

        response = await kiwoom.send_request(req)
        if response.success:
            korea_data = KiwoomApiHelper.to_korea_data(response.data, response.api_info['api_id'])
            response.data = korea_data
            if title == 'stocklist':
                logger.info(f'보유종목 데이터 변환 완료: {korea_data}')
                await insert_prev_costs_kiwoom(response.data['종목별계좌평가현황'])
            logger.info(f'Kiwoom API response: [{response}]')
        return response
    except KiwoomApiException as e:
        return KiwoomApiHelper.create_error_response(error_code='999', error_message=str(e))
    except Exception as e:
        logger.error(f'Error occurred while placing order: {e}')
        return KiwoomApiHelper.create_error_response(
            error_code='999', error_message='Internal server error'
        )


async def insert_prev_costs_kiwoom(stock_list: list):
    """보유종목 데이터에 이전 매입 단가 삽입"""
    cache = get_prev_price_cache()
    for stock in stock_list:
        stk_cd = stock.get('종목코드')
        # A005930 형태에서 005930 형태로 변환
        if stk_cd and len(stk_cd) == 7 and stk_cd.startswith('A'):
            stk_cd = stk_cd[1:]
        price = await cache.get_last_price(stk_cd)
        stock['전일종가'] = price if price else 0


@router.get('/issue-new-token', response_model=KiwoomResponse)
async def issue_new_token():
    """새로운 토큰 발급"""
    logger.info('새로운 토큰 발급 요청 받음')

    try:
        token_manager = await get_token_manager()
        if not token_manager:
            return KiwoomApiHelper.create_error_response(
                error_code='999', error_message='Kiwoom API 클래스를 생성하는데 실패했습니다'
            )

        await token_manager.discard_token()
        await token_manager.issue_access_token()
        return KiwoomApiHelper.create_success_response(
            data={'message': '새로운 토큰이 발급되었습니다.'},
            api_info={'api_id': 'issue_new_token'},
        )

    except KiwoomApiException as e:
        return KiwoomApiHelper.create_error_response(error_code='999', error_message=str(e))
    except Exception as e:
        logger.error(f'Error occurred while issuing new token: {e}')
        return KiwoomApiHelper.create_error_response(
            error_code='999', error_message='Internal server error'
        )


@router.get('/jisu')
async def get_jisu():
    """지수 정보 조회"""
    logger.info('지수 정보 조회 요청 받음')
    checker = OpenTimeChecker.get()
    now = datetime.now(tz=ZoneInfo(config.TIME_ZONE))
    market = await checker.getMarket(now)

    try:
        jisu_data = get_jisu_from_naver()  # await 제거 (동기 함수)
        if not jisu_data:
            return {
                'success': False,
                'error_code': '999',
                'error_message': '지수 정보를 가져오는데 실패했습니다',
            }
        jisu_data['market'] = market if market else '장마감'
        logger.info(f'지수 정보 조회 성공: {jisu_data}')
        return jisu_data

    except Exception as e:
        logger.error(f'지수 정보 조회 중 오류 발생: {e}')
        return {
            'success': False,
            'error_code': '999',
            'error_message': '지수 정보 조회 중 오류가 발생했습니다',
        }
