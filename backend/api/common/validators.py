"""
API에서 사용하는 공통 검증 함수들
"""
import re
from datetime import datetime
from typing import Any
from fastapi import HTTPException

def validate_date_format(date_str: str, format_str: str = "%Y%m%d") -> bool:
    """날짜 형식 검증"""
    try:
        datetime.strptime(date_str, format_str)
        return True
    except ValueError:
        return False

def validate_stock_code(stock_code: str) -> bool:
    """종목코드 형식 검증 (6자리 숫자)"""
    if not stock_code or not isinstance(stock_code, str):
        return False
    return bool(re.match(r'^\d{6}$', stock_code))

def validate_market_type(market_type: str) -> bool:
    """시장 타입 검증"""
    valid_types = ["0", "10", "3", "8", "30", "50", "5", "4", "6", "9"]
    return market_type in valid_types

def validate_positive_number(value: Any, field_name: str) -> None:
    """양수 검증"""
    try:
        num_value = float(value)
        if num_value <= 0:
            raise HTTPException(
                status_code=400,
                detail=f"{field_name}은(는) 양수여야 합니다."
            )
    except (ValueError, TypeError):
        raise HTTPException(
            status_code=400,
            detail=f"{field_name}은(는) 유효한 숫자여야 합니다."
        )
