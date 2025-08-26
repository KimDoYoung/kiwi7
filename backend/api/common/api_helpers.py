# api_helpers.py
"""
모듈 설명: 
    API 응답 생성을 위한 헬퍼 함수들
    라우터에서 일관된 형식의 응답을 생성하기 위해 사용
주요 기능:
    - 성공 응답 생성
    - 에러 응답 생성
    - 검증 에러 응답 생성
    - 페이지네이션 응답 생성

작성자: 김도영
작성일: 2025-08-26
버전: 1.0
"""
from datetime import datetime
from typing import Any, Optional
from fastapi.responses import JSONResponse
from backend.core.logger import get_logger

logger = get_logger(__name__)

def create_success_response(
    message: str = "성공",
    data: Any = None,
    status_code: int = 200
) -> JSONResponse:
    """
    성공 응답을 생성하는 헬퍼 함수
    
    Args:
        message: 성공 메시지
        data: 응답 데이터
        status_code: HTTP 상태 코드
    
    Returns:
        JSONResponse: 성공 응답
    """
    response_data = {
        "success": True,
        "message": message,
        "timestamp": datetime.now().isoformat(),
    }
    
    if data is not None:
        response_data["data"] = data
    
    return JSONResponse(
        status_code=status_code,
        content=response_data
    )

def create_error_response(
    message: str,
    error_code: Optional[str] = None,
    status_code: int = 400,
    details: Any = None
) -> JSONResponse:
    """
    에러 응답을 생성하는 헬퍼 함수 (라우터용)
    
    Args:
        message: 에러 메시지
        error_code: 에러 코드 (선택사항)
        status_code: HTTP 상태 코드
        details: 추가 에러 상세 정보
    
    Returns:
        JSONResponse: 에러 응답
    """
    response_data = {
        "success": False,
        "message": message,
        "timestamp": datetime.now().isoformat(),
    }
    
    if error_code:
        response_data["error_code"] = error_code
    
    if details:
        response_data["details"] = details
    
    logger.error(f"API 에러 응답: {message} (상태코드: {status_code})")
    
    return JSONResponse(
        status_code=status_code,
        content=response_data
    )

def create_validation_error_response(
    message: str = "입력 데이터 검증 실패",
    validation_errors: Any = None
) -> JSONResponse:
    """
    입력 검증 에러 응답을 생성하는 헬퍼 함수
    
    Args:
        message: 검증 에러 메시지
        validation_errors: 검증 에러 상세 정보
    
    Returns:
        JSONResponse: 검증 에러 응답
    """
    return create_error_response(
        message=message,
        error_code="VALIDATION_ERROR",
        status_code=422,
        details=validation_errors
    )

def create_not_found_response(
    resource: str = "리소스"
) -> JSONResponse:
    """
    리소스를 찾을 수 없음 응답을 생성하는 헬퍼 함수
    
    Args:
        resource: 찾을 수 없는 리소스명
    
    Returns:
        JSONResponse: 404 에러 응답
    """
    return create_error_response(
        message=f"{resource}를 찾을 수 없습니다",
        error_code="NOT_FOUND",
        status_code=404
    )

def create_unauthorized_response(
    message: str = "인증이 필요합니다"
) -> JSONResponse:
    """
    인증 실패 응답을 생성하는 헬퍼 함수
    
    Args:
        message: 인증 에러 메시지
    
    Returns:
        JSONResponse: 401 에러 응답
    """
    return create_error_response(
        message=message,
        error_code="UNAUTHORIZED",
        status_code=401
    )

def get_current_timestamp() -> str:
    """
    현재 타임스탬프를 ISO 형식으로 반환하는 헬퍼 함수
    
    Returns:
        str: ISO 형식의 현재 시간
    """
    return datetime.now().isoformat()

# 페이지네이션 응답을 위한 헬퍼 함수
def create_paginated_response(
    data: list,
    total: int,
    page: int = 1,
    size: int = 10,
    message: str = "조회 성공"
) -> JSONResponse:
    """
    페이지네이션된 응답을 생성하는 헬퍼 함수
    
    Args:
        data: 페이지네이션된 데이터 리스트
        total: 전체 데이터 수
        page: 현재 페이지 번호
        size: 페이지 크기
        message: 성공 메시지
    
    Returns:
        JSONResponse: 페이지네이션된 응답
    """
    pagination_info = {
        "current_page": page,
        "page_size": size,
        "total_items": total,
        "total_pages": (total + size - 1) // size,  # 올림 계산
        "has_next": page * size < total,
        "has_previous": page > 1
    }
    
    response_data = {
        "items": data,
        "pagination": pagination_info
    }
    
    return create_success_response(
        message=message,
        data=response_data
    )