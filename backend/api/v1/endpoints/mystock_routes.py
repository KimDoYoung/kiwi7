from fastapi import APIRouter

from backend.api.common.stock_functions import get_stock_name
from backend.core.logger import get_logger
from backend.domains.kiwoom.kiwoom_service import get_kiwoom_api
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomApiHelper, KiwoomRequest, KiwoomResponse
from backend.domains.services.dependency import get_service


router = APIRouter()
logger = get_logger(__name__)

@router.delete("/{stk_cd}", response_model=KiwoomResponse)
async def delete_code_from_my_stocks(stk_cd:str):
    ''' my_stock에서 종목삭제 '''
    logger.info(f"My Stock에서 종목삭제 요청 받음: stk_cd={stk_cd}")
    try:
        service = get_service("my_stock")
        await service.delete(stk_cd)
        return KiwoomApiHelper.create_success_response(data={"stk_code": stk_cd})
    except Exception as e:
        logger.error(f"나의 관심종목에서 {stk_cd} 코드삭제에 실패함: {e}")
        return KiwoomApiHelper.create_error_response(error_code="MY_STOCK_DELETE_ERROR", error_message=str(e))


@router.get("/", response_model=KiwoomResponse)
async def get_my_stocks():
    ''' my_stock을 모두 조회(추가된 역순으로 최대 50개까지) ka10001을 호출 '''
    logger.info("My Stock 정보를 조회합니다.")
    try:
        service = get_service("my_stock")
        stocks = await service.list_all()  # await 추가
        
        if not stocks:
            logger.info("등록된 My Stock이 없습니다.")
            return KiwoomApiHelper.create_success_response(data={"list":[]})

        api = await get_kiwoom_api()
        result = []
        
        # 최대 50개로 제한
        limited_stocks = stocks[:50]
        logger.info(f"총 {len(stocks)}개 중 {len(limited_stocks)}개 종목의 정보를 조회합니다.")
        
        for i, stock in enumerate(limited_stocks, 1):
            try:
                logger.debug(f"[{i}/{len(limited_stocks)}] {stock.stk_cd} 정보 조회 중...")
                response = await api.send_request(KiwoomRequest(api_id="ka10001", payload={"stk_cd": stock.stk_cd}))
                
                if response.success:
                    korea_data = KiwoomApiHelper.to_korea_data(response.data, response.api_info['api_id'])
                    korea_data['is_hold'] = stock.is_hold
                    korea_data['is_watch'] = stock.is_watch
                    result.append(korea_data)
                    logger.debug(f"✅ {stock.stk_cd} 조회 성공")
                else:
                    logger.warning(f"❌ {stock.stk_cd} 조회 실패: {response.error_message}")
                    
            except Exception as e:
                logger.error(f"❌ {stock.stk_cd} 조회 중 오류: {str(e)}")
                return KiwoomApiHelper.create_error_response(error_code="MY_STOCK_ERROR", error_message=str(e))
        
        logger.info(f"My Stock 조회 완료: {len(result)}개 종목 정보 반환")
        return KiwoomApiHelper.create_success_response(data={"list": result})

    except Exception as e:
        logger.error(f"My Stock 조회 중 오류 발생: {str(e)}")
        return KiwoomApiHelper.create_error_response(error_code="MY_STOCK_ERROR", error_message=str(e))

@router.put("/{stk_code}", response_model=KiwoomResponse)
async def put_stock(stk_code: str):
    ''' my_stock에 종목추가'''
    logger.info(f"stk_code를 my_stock에 추가 요청 받음: stk_code={stk_code}")
    try:
        service = get_service("my_stock")
        stk_name = await get_stock_name(stk_code)
        service.upsert_watching(stk_code, stk_name, None)
        return KiwoomApiHelper.create_success_response(data={"stk_code": stk_code, "stk_name": stk_name})
    except Exception as e:
        logger.error(f"Error occurred while adding stk_code to my_stock: {e}")
        return KiwoomApiHelper.create_error_response(error_code="MY_STOCK_ERROR", error_message=str(e))

@router.post("/bulk", response_model=KiwoomResponse)
async def put_stocks(request: KiwoomRequest):
    """여러 종목을 my_stock에 일괄 추가
    
    Request payload 예시:
    {
        "codes": ["018290", "060250", "094860", "257720"]
    }
    """
    # payload에서 codes 추출
    codes = request.payload.get("codes", [])
    
    if not codes:
        return KiwoomApiHelper.create_error_response(
            error_code="400",
            error_message="종목 코드 목록이 필요합니다.",
            status_code=400,
            api_info={"api_id": "mystock_bulk_add", "description": "종목 일괄 추가"}
        )
    
    logger.info(f"종목 일괄 추가 요청 받음: codes={codes}")
    
    try:
        service = get_service("my_stock")
        success_list = []
        error_list = []
        
        for stk_code in codes:
            try:
                stk_name = await get_stock_name(stk_code)
                service.upsert_holding(stk_code, stk_name, None)
                success_list.append({"stk_code": stk_code, "stk_name": stk_name})
                logger.info(f"종목 추가 성공: {stk_code} - {stk_name}")
            except Exception as e:
                error_info = {"stk_code": stk_code, "error": str(e)}
                error_list.append(error_info)
                logger.error(f"종목 추가 실패: {stk_code} - {str(e)}")
        
        result_data = {
            "total_count": len(codes),
            "success_count": len(success_list),
            "error_count": len(error_list),
            "success_list": success_list,
            "error_list": error_list
        }
        
        if len(error_list) == 0:
            # 모든 종목이 성공한 경우
            return KiwoomApiHelper.create_success_response(
                data=result_data,
                api_info={"api_id": "mystock_bulk_add", "description": "종목 일괄 추가"}
            )
        elif len(success_list) > 0:
            # 일부 성공, 일부 실패한 경우 (부분 성공)
            logger.warning(f"종목 일괄 추가 부분 성공: 성공 {len(success_list)}개, 실패 {len(error_list)}개")
            return KiwoomApiHelper.create_success_response(
                data=result_data,
                api_info={"api_id": "mystock_bulk_add", "description": "종목 일괄 추가 (부분 성공)"}
            )
        else:
            # 모든 종목이 실패한 경우
            return KiwoomApiHelper.create_error_response(
                error_code="MY_STOCK_BULK_ERROR",
                error_message="모든 종목 추가에 실패했습니다.",
                api_info={"api_id": "mystock_bulk_add", "description": "종목 일괄 추가"}
            )
            
    except Exception as e:
        logger.error(f"종목 일괄 추가 중 예상치 못한 오류 발생: {str(e)}")
        return KiwoomApiHelper.create_error_response(
            error_code="MY_STOCK_BULK_SYSTEM_ERROR", 
            error_message=f"종목 일괄 추가 중 시스템 오류가 발생했습니다: {str(e)}",
            api_info={"api_id": "mystock_bulk_add", "description": "종목 일괄 추가"}
        )
