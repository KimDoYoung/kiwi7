# APIRouter 인스턴스 생성
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from backend.core.logger import get_logger
from fastapi import Request

from backend.domains.kiwoom.kiwoom_service import get_kiwoom_api
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomRequest, KiwoomResponse
router = APIRouter()
logger = get_logger(__name__)

@router.post("/kiwoom", response_class=KiwoomResponse)
async def order(request:Request, req: KiwoomRequest):
    '''kiwoom rest api 호출'''
    
    logger.info(f"Received Kiwoom API request: [{req}]")
    kiwoom = await get_kiwoom_api(request)
    if not kiwoom:
        return JSONResponse(status_code=500, content={"message": "Kiwoom API is not available"})
    
    try:
        response = await kiwoom.send_request(req)
        logger.info(f"Kiwoom API response: [{response}]")
        return response
    except Exception as e:
        logger.error(f"Error occurred while placing order: {e}")
        return JSONResponse(status_code=500, content={"message": "Internal server error"})