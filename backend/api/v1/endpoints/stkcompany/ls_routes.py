"""
LS증권 API 라우트
"""
from fastapi import APIRouter

from backend.core.exceptions import LsApiException
from backend.core.logger import get_logger
from backend.domains.services.prev_price_cache import get_prev_price_cache
from backend.domains.stkcompanys.ls.ls_service import get_ls_api, get_ls_token_manager
from backend.domains.stkcompanys.ls.models.ls_schema import LsApiHelper, LsRequest, LsResponse

router = APIRouter()
logger = get_logger(__name__)


@router.post("/{api_id}", response_model=LsResponse)
async def ls_rest_api(api_id: str, req: LsRequest):
    """LS REST API 호출"""
    title = req.title
    logger.info(f"[LS] API 요청: api_id={api_id}, title={title}")

    try:
        ls = await get_ls_api()
        if not ls:
            return LsApiHelper.create_error_response(
                error_code="999",
                error_message="LS API 인스턴스 생성 실패"
            )

        # URL path의 api_id로 업데이트
        req.api_id = api_id

        # payload 유효성 검증
        validation_errors = req.validate_payload()
        if validation_errors:
            return LsApiHelper.create_error_response(
                error_code="400",
                error_message=f"요청 검증 실패: {', '.join(validation_errors)}"
            )

        # API 요청
        response = await ls.send_request(req)

        # 성공 시 한글 필드명으로 변환
        if response.success and response.data:
            korea_data = LsApiHelper.to_korea_data(response.data, api_id)
            response.data = korea_data
            if title == "stocklist":
                await insert_prev_costs_ls(response.data.get('t0424OutBlock1', []))
        return response

    except LsApiException as e:
        logger.error(f"[LS] API 예외: {e}")
        return LsApiHelper.create_error_response(
            error_code=e.error_code or "999",
            error_message=str(e)
        )
    except Exception as e:
        logger.error(f"[LS] 오류: {e}")
        return LsApiHelper.create_error_response(
            error_code="999",
            error_message=f"Internal server error: {str(e)}"
        )

async def insert_prev_costs_ls(stock_list: list):
    """보유종목 데이터에 이전 매입 단가 삽입"""
    cache = get_prev_price_cache()
    for stock in stock_list:
        stk_cd = stock.get("종목번호")
        # A005930 형태에서 005930 형태로 변환
        if stk_cd and len(stk_cd) == 7 and stk_cd.startswith("A"):
            stk_cd = stk_cd[1:]
        price = await cache.get_last_price(stk_cd)
        trend = await cache.get_last_trend(stk_cd)
        stock["전일종가"] = price if price else 0
        stock["가격추세"] = trend if trend else "-"

@router.get("/issue-new-token", response_model=LsResponse)
async def issue_new_token():
    """새로운 토큰 발급"""
    logger.info("[LS] 토큰 재발급 요청")

    try:
        token_manager = await get_ls_token_manager()
        await token_manager.discard_token()
        result = await token_manager.issue_access_token()

        return LsApiHelper.create_success_response(
            data={
                "message": "새로운 토큰이 발급되었습니다.",
                "expires_dt": result.get('expires_dt')
            },
            api_info={"api_id": "issue_new_token", "title": "토큰 발급"}
        )
    except LsApiException as e:
        logger.error(f"[LS] 토큰 발급 예외: {e}")
        return LsApiHelper.create_error_response(
            error_code=e.error_code or "999",
            error_message=str(e)
        )
    except Exception as e:
        logger.error(f"[LS] 토큰 발급 오류: {e}")
        return LsApiHelper.create_error_response(
            error_code="999",
            error_message=str(e)
        )

@router.get("/token-info", response_model=LsResponse)
async def get_token_info():
    """현재 토큰 정보 조회"""
    try:
        token_manager = await get_ls_token_manager()

        return LsApiHelper.create_success_response(
            data={
                "has_token": bool(token_manager.token),
                "expires_dt": token_manager.expires_dt,
                "token_type": token_manager.token_type,
                "is_virtual": token_manager.is_virtual,
            },
            api_info={"api_id": "token_info", "title": "토큰 정보"}
        )
    except Exception as e:
        logger.error(f"[LS] 토큰 정보 조회 오류: {e}")
        return LsApiHelper.create_error_response(
            error_code="999",
            error_message=str(e)
        )
