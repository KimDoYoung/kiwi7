"""
KIS(한국투자증권) API 라우트
"""
from fastapi import APIRouter

from backend.core.exceptions import KisApiException
from backend.core.logger import get_logger
from backend.domains.stkcompanys.kis.kis_service import get_kis_api, get_kis_token_manager
from backend.domains.stkcompanys.kis.models.kis_schema import KisApiHelper, KisRequest, KisResponse

router = APIRouter()
logger = get_logger(__name__)


@router.post("/{api_id}", response_model=KisResponse)
async def kis_rest_api(api_id: str, req: KisRequest):
    """KIS REST API 호출"""
    logger.info(f"[KIS] API 요청: api_id={api_id}")

    try:
        kis = await get_kis_api()
        if not kis:
            return KisApiHelper.create_error_response(
                error_code="999",
                error_message="KIS API 인스턴스 생성 실패"
            )

        # URL path의 api_id로 업데이트
        req.api_id = api_id

        # payload 유효성 검증
        validation_errors = req.validate_payload()
        if validation_errors:
            return KisApiHelper.create_error_response(
                error_code="400",
                error_message=f"요청 검증 실패: {', '.join(validation_errors)}"
            )

        # API 요청
        response = await kis.send_request(req)

        # 성공 시 한글 필드명으로 변환
        if response.success and response.data:
            korea_data = KisApiHelper.to_korea_data(response.data, api_id)
            response.data = korea_data

        return response

    except KisApiException as e:
        logger.error(f"[KIS] API 예외: {e}")
        return KisApiHelper.create_error_response(
            error_code=e.error_code or "999",
            error_message=str(e)
        )
    except Exception as e:
        logger.error(f"[KIS] 오류: {e}")
        return KisApiHelper.create_error_response(
            error_code="999",
            error_message=f"Internal server error: {str(e)}"
        )


@router.get("/issue-new-token", response_model=KisResponse)
async def issue_new_token():
    """새로운 토큰 발급"""
    logger.info("[KIS] 토큰 재발급 요청")

    try:
        token_manager = await get_kis_token_manager()
        await token_manager.discard_token()
        result = await token_manager.issue_access_token()

        return KisApiHelper.create_success_response(
            data={
                "message": "새로운 토큰이 발급되었습니다.",
                "expires_dt": result.get('expires_dt')
            },
            api_info={"api_id": "issue_new_token", "title": "토큰 발급"}
        )
    except KisApiException as e:
        logger.error(f"[KIS] 토큰 발급 예외: {e}")
        return KisApiHelper.create_error_response(
            error_code=e.error_code or "999",
            error_message=str(e)
        )
    except Exception as e:
        logger.error(f"[KIS] 토큰 발급 오류: {e}")
        return KisApiHelper.create_error_response(
            error_code="999",
            error_message=str(e)
        )


@router.get("/token-info", response_model=KisResponse)
async def get_token_info():
    """현재 토큰 정보 조회"""
    try:
        token_manager = await get_kis_token_manager()

        return KisApiHelper.create_success_response(
            data={
                "has_token": bool(token_manager.token),
                "expires_dt": token_manager.expires_dt,
                "token_type": token_manager.token_type,
                "is_virtual": token_manager.is_virtual,
            },
            api_info={"api_id": "token_info", "title": "토큰 정보"}
        )
    except Exception as e:
        logger.error(f"[KIS] 토큰 정보 조회 오류: {e}")
        return KisApiHelper.create_error_response(
            error_code="999",
            error_message=str(e)
        )


@router.post("/hashkey", response_model=KisResponse)
async def get_hashkey(payload: dict):
    """해시키 생성 (주문 시 필요)"""
    logger.info("[KIS] 해시키 생성 요청")

    try:
        kis = await get_kis_api()
        hashkey = await kis.get_hashkey(payload)

        return KisApiHelper.create_success_response(
            data={
                "hashkey": hashkey
            },
            api_info={"api_id": "hashkey", "title": "해시키 생성"}
        )
    except KisApiException as e:
        logger.error(f"[KIS] 해시키 생성 예외: {e}")
        return KisApiHelper.create_error_response(
            error_code=e.error_code or "999",
            error_message=str(e)
        )
    except Exception as e:
        logger.error(f"[KIS] 해시키 생성 오류: {e}")
        return KisApiHelper.create_error_response(
            error_code="999",
            error_message=str(e)
        )
