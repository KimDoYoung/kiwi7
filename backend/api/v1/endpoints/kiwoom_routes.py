# APIRouter 인스턴스 생성
from fastapi import APIRouter
from backend.core.exceptions import KiwoomApiException
from backend.core.logger import get_logger

from backend.domains.kiwoom.kiwoom_service import get_kiwoom_api
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomApiHelper, KiwoomRequest, KiwoomResponse
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
    