# APIRouter 인스턴스 생성
from datetime import datetime
from zoneinfo import ZoneInfo
from fastapi import APIRouter
from backend.core.exceptions import KiwoomApiException
from backend.core.logger import get_logger

from backend.domains.kiwoom.kiwoom_service import get_kiwoom_api, get_token_manager
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomApiHelper, KiwoomRequest, KiwoomResponse
from backend.domains.market.open_time_checker import OpenTimeChecker
from backend.utils.kiwi_utils import merge_dicts
from backend.utils.naver_utils import get_summary_from_naver, get_jisu_from_naver
from backend.core.config import config

router = APIRouter()
logger = get_logger(__name__)


@router.post("/{api_id}", response_model=KiwoomResponse)
async def kiwoom_rest_api(api_id: str, req: KiwoomRequest):
    '''kiwoom rest api 호출'''
    logger.info(f"Received Kiwoom API request: api_id={api_id}, req=[{req}]")

    try:
        kiwoom = await get_kiwoom_api()
        if not kiwoom:
            return KiwoomApiHelper.create_error_response(error_code="999", error_message="Kiwoom API 클래스를 생성하는데 실패했습니다")

        # URL path의 api_id로 request body의 api_id 업데이트
        req.api_id = api_id
        
        # payload 유효성 검증 명시적 호출
        validation_errors = req.validate_payload()
        if validation_errors:
            return KiwoomApiHelper.create_error_response(
                error_code="400", 
                error_message=f"요청 데이터 검증 실패: {', '.join(validation_errors)}"
            )
        
        response = await kiwoom.send_request(req)
        if response.success:
            korea_data = KiwoomApiHelper.to_korea_data(response.data, response.api_info['api_id'])
            response.data = korea_data        
        logger.info(f"Kiwoom API response: [{response}]")
        return response
    except KiwoomApiException as e:
        return KiwoomApiHelper.create_error_response(error_code="999", error_message=str(e))    
    except Exception as e:
        logger.error(f"Error occurred while placing order: {e}")
        return KiwoomApiHelper.create_error_response(error_code="999", error_message="Internal server error")

@router.get("/issue-new-token", response_model=KiwoomResponse)
async def issue_new_token():
    '''새로운 토큰 발급'''
    logger.info("새로운 토큰 발급 요청 받음")
    
    try:
        token_manager = await get_token_manager()
        if not token_manager:
            return KiwoomApiHelper.create_error_response(error_code="999", error_message="Kiwoom API 클래스를 생성하는데 실패했습니다")

        await token_manager.discard_token()
        response = await token_manager.issue_access_token()
        return KiwoomApiHelper.create_success_response(
            data={"message": "새로운 토큰이 발급되었습니다."},
            api_info={"api_id": "issue_new_token"}
        )

    except KiwoomApiException as e:
        return KiwoomApiHelper.create_error_response(error_code="999", error_message=str(e))    
    except Exception as e:
        logger.error(f"Error occurred while issuing new token: {e}")
        return KiwoomApiHelper.create_error_response(error_code="999", error_message="Internal server error")
    
@router.get("/stock/{stk_code}", response_model=KiwoomResponse)
async def get_stock_info(stk_code: str):
    '''stk_code 에 대해서  ka10001(주식기본정보)와 ka10100(종목정보조회) 2개의 api를 호출해서
     데이터를 merge한 후에  주식 정보를 가져온다.'''
    logger.info(f"Received request for stock info: stk_code={stk_code}")

    kiwoom = await get_kiwoom_api()
    if not kiwoom:
        return KiwoomApiHelper.create_error_response(error_code="999", error_message="Kiwoom API 클래스를 생성하는데 실패했습니다")

    try:
        req = KiwoomRequest(api_id="ka10001", payload={"stk_cd": stk_code})
        response1 = await kiwoom.send_request(req)
        if response1.success:
            korea_data = KiwoomApiHelper.to_korea_data(response1.data, response1.api_info['api_id'])
            response1.data = korea_data           

        req = KiwoomRequest(api_id="ka10100", payload={"stk_cd": stk_code})
        response2 = await kiwoom.send_request(req)
        if response2.success:
            korea_data = KiwoomApiHelper.to_korea_data(response2.data, response2.api_info['api_id'])
            response2.data = korea_data

        response = merge_dicts(response1.data, response2.data)

        # naver의 company_summary를 구한다.
        company_summary = get_summary_from_naver(stk_code)
        if company_summary:
            response['company_summary'] = company_summary

        return KiwoomApiHelper.create_success_response(
            data=response,
            api_info={"api_id": "ka10001_ka10100", "description": "주식 기본 정보와 종목 정보 조회"}
        )

    except KiwoomApiException as e:
        return KiwoomApiHelper.create_error_response(error_code="999", error_message=str(e))
    except Exception as e:
        logger.error(f"Error occurred while fetching stock info: {e}")
        return KiwoomApiHelper.create_error_response(error_code="999", error_message="Internal server error")

@router.get("/jisu")
async def get_jisu():
    '''지수 정보 조회'''
    logger.info("지수 정보 조회 요청 받음")
    checker = OpenTimeChecker.get()
    now = datetime.now(tz=ZoneInfo(config.TIME_ZONE))
    market = await checker.getMarket(now)
    
    try:
        jisu_data = get_jisu_from_naver()  # await 제거 (동기 함수)
        if not jisu_data:
            return {
                "success": False,
                "error_code": "999",
                "error_message": "지수 정보를 가져오는데 실패했습니다"
            }
        jisu_data['market'] = market if market else '장마감'
        logger.info(f"지수 정보 조회 성공: {jisu_data}")
        return jisu_data
        
    except Exception as e:
        logger.error(f"지수 정보 조회 중 오류 발생: {e}")
        return {
            "success": False,
            "error_code": "999",
            "error_message": "지수 정보 조회 중 오류가 발생했습니다"
        }

