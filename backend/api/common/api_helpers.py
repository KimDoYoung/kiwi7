"""
API 엔드포인트에서 공통으로 사용하는 헬퍼 함수들
"""
import datetime
from typing import Any, Dict, Optional
from fastapi import HTTPException
from backend.core.logger import get_logger
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomApiHelper

logger = get_logger(__name__)

def create_success_response(data: Any = None, message: str = "성공") -> Dict[str, Any]:
    """성공 응답 생성"""
    return KiwoomApiHelper.create_success_response(data=data, message=message)

def create_error_response(message: str, error_code: Optional[str] = None) -> Dict[str, Any]:
    """에러 응답 생성"""
    return KiwoomApiHelper.create_error_response(message=message, error_code=error_code)

async def handle_api_exception(func_name: str, exception: Exception) -> None:
    """API 예외 처리 및 로깅"""
    logger.error(f"{func_name} 실행 중 오류 발생: {str(exception)}")
    raise HTTPException(
        status_code=500,
        detail=f"{func_name} 처리 중 오류가 발생했습니다: {str(exception)}"
    )

def get_current_timestamp() -> str:
    """현재 시각을 YYYYMMDDHHMMSS 형식으로 반환"""
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def validate_required_params(params: Dict[str, Any], required_keys: list) -> None:
    """필수 파라미터 검증"""
    missing_keys = [key for key in required_keys if key not in params or params[key] is None]
    if missing_keys:
        raise HTTPException(
            status_code=400,
            detail=f"필수 파라미터가 누락되었습니다: {', '.join(missing_keys)}"
        )
