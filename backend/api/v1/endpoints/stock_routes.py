from fastapi import APIRouter
from backend.core.exceptions import KiwoomApiException
from backend.core.logger import get_logger
from backend.domains.stkcompanys.kiwoom.kiwoom_service import get_kiwoom_api
from backend.domains.stkcompanys.kiwoom.models.kiwoom_schema import KiwoomApiHelper, KiwoomRequest, KiwoomResponse
from backend.domains.services import get_service
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
            data=response
        )

    except KiwoomApiException as e:
        return KiwoomApiHelper.create_error_response(error_code="999", error_message=str(e))
    except Exception as e:
        logger.error(f"Error occurred while fetching stock info: {e}")
        return KiwoomApiHelper.create_error_response(error_code="999", error_message= str(e))

@router.post("/find", response_model=KiwoomResponse)
async def find_stock(request: KiwoomRequest):
    """
    종목명 또는 종목코드로 종목을 검색합니다.
    stk_info 테이블에서 키워드를 포함하는 종목들을 찾아서 리스트로 반환합니다.
    
    Request payload 예시:
    {
        "keyword": "삼성전자",
        "limit": 10
    }
    """
    try:
        # payload에서 키워드와 limit 추출
        keyword = request.payload.get("keyword", "")
        limit = request.payload.get("limit", 10)
        
        if not keyword.strip():
            return KiwoomApiHelper.create_error_response(
                error_code="400",
                error_message="검색어를 입력해주세요.",
                status_code=400,
                api_info={"api_id": "stock_find", "description": "종목 검색"}
            )
        
        logger.info(f"종목 검색 요청: keyword={keyword}, limit={limit}")
        
        # stk_info 서비스 가져오기
        stk_info_service = get_service("stk_info")
        
        # 키워드로 종목 검색 (기존 search_by_name 메서드 사용)
        search_results = await stk_info_service.search_by_name(keyword)
        
        # limit 적용
        if limit > 0:
            search_results = search_results[:limit]
        
        # 응답 데이터 변환
        result_data = []
        for stock in search_results:
            result_data.append({
                "stk_cd": stock.stk_cd,
                "stk_nm": stock.stk_nm or "",
                "market_name": stock.market_name or "",
                "up_name": stock.up_name or "",
                "list_count": stock.list_count or "",
                "reg_day": stock.reg_day or "",
                "last_price": stock.last_price or "",
                "nxt_enable": stock.nxt_enable or ""
            })
        
        response_data = {
            "results": result_data,
            "total_count": len(result_data),
            "keyword": keyword,
            "message": f"'{keyword}' 검색 결과 {len(result_data)}건을 찾았습니다."
        }
        
        return KiwoomApiHelper.create_success_response(
            data=response_data,
            api_info={"api_id": "stock_find", "description": "종목 검색"}
        )
        
    except Exception as e:
        logger.error(f"종목 검색 중 오류 발생: {str(e)}")
        return KiwoomApiHelper.create_error_response(
            error_code="500",
            error_message=f"종목 검색 중 오류가 발생했습니다: {str(e)}",
            status_code=500,
            api_info={"api_id": "stock_find", "description": "종목 검색"}
        )
    