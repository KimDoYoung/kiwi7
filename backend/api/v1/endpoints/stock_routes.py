from fastapi import APIRouter
from backend.api.common.api_helpers import create_error_response, create_success_response
from backend.core.exceptions import KiwoomApiException
from backend.core.logger import get_logger
from backend.domains.kiwoom.kiwoom_service import get_kiwoom_api
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomApiHelper, KiwoomRequest, KiwoomResponse
from backend.utils.kiwi_utils import merge_dicts
from backend.utils.naver_utils import get_summary_from_naver


router = APIRouter()
logger = get_logger(__name__)

@router.get("/info/{stk_code}", response_model=KiwoomResponse)
async def get_stock_info(stk_code: str):
    '''
    stk_code 에 대해서  ka10001(주식기본정보)와 ka10100(종목정보조회) 2개의 api를 호출해서
    데이터를 merge한 후에  주식 정보를 가져온다.
     '''
    logger.info(f"Received request for stock info: stk_code={stk_code}")

    kiwoom = await get_kiwoom_api()
    if not kiwoom:
        return create_error_response(error_code="999", error_message="Kiwoom API 클래스를 생성하는데 실패했습니다")

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

        return create_success_response(
            data=response,
            api_info={"api_id": "ka10001_ka10100", "description": "주식 기본 정보와 종목 정보 조회"}
        )

    except KiwoomApiException as e:
        return create_error_response(error_code="999", error_message=str(e))
    except Exception as e:
        logger.error(f"Error occurred while fetching stock info: {e}")
        return create_error_response(error_code="999", error_message="Internal server error")