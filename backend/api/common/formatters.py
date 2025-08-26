"""
API에서 사용하는 공통 포매팅 함수들
"""
from typing import Any

def format_currency(value: Any, currency: str = "원") -> str:
    """
    숫자를 통화 형식으로 포매팅
    
    Args:
        value: 포매팅할 숫자값
        currency: 통화 단위 (기본값: "원")
    
    Returns:
        포매팅된 통화 문자열
    """
    try:
        if value is None:
            return f"0 {currency}"
        
        # 문자열인 경우 숫자로 변환 시도
        if isinstance(value, str):
            value = value.replace(',', '').replace(currency, '').strip()
            
        num_value = float(value)
        formatted = f"{num_value:,.0f}"
        return f"{formatted} {currency}"
    except (ValueError, TypeError):
        return f"0 {currency}"

def format_percentage(value: Any, decimal_places: int = 2) -> str:
    """
    숫자를 퍼센트 형식으로 포매팅
    
    Args:
        value: 포매팅할 숫자값
        decimal_places: 소수점 자릿수 (기본값: 2)
    
    Returns:
        포매팅된 퍼센트 문자열
    """
    try:
        if value is None:
            return "0.00%"
            
        # 문자열인 경우 숫자로 변환 시도
        if isinstance(value, str):
            value = value.replace('%', '').strip()
            
        num_value = float(value)
        return f"{num_value:.{decimal_places}f}%"
    except (ValueError, TypeError):
        return "0.00%"

def format_stock_code(code: str) -> str:
    """
    종목코드를 표준 형식으로 포매팅 (6자리 0 패딩)
    
    Args:
        code: 종목코드
    
    Returns:
        포매팅된 종목코드
    """
    if not code:
        return ""
    
    # 숫자만 추출
    numeric_code = ''.join(filter(str.isdigit, str(code)))
    
    # 6자리로 0 패딩
    return numeric_code.zfill(6) if numeric_code else ""

def format_number(value: Any, decimal_places: int = 0) -> str:
    """
    숫자를 천단위 구분자와 함께 포매팅
    
    Args:
        value: 포매팅할 숫자값
        decimal_places: 소수점 자릿수 (기본값: 0)
    
    Returns:
        포매팅된 숫자 문자열
    """
    try:
        if value is None:
            return "0"
            
        num_value = float(value)
        
        if decimal_places == 0:
            return f"{num_value:,.0f}"
        else:
            return f"{num_value:,.{decimal_places}f}"
    except (ValueError, TypeError):
        return "0"

def format_date_yyyymmdd(date_str: str) -> str:
    """
    YYYYMMDD 형식의 날짜를 YYYY-MM-DD 형식으로 포매팅
    
    Args:
        date_str: YYYYMMDD 형식의 날짜 문자열
    
    Returns:
        YYYY-MM-DD 형식의 날짜 문자열
    """
    if not date_str or len(date_str) != 8:
        return date_str
    
    try:
        return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    except:
        return date_str

def format_profit_loss(value: Any, format_type: str = "amount") -> dict:
    """
    손익 값을 포매팅하고 색상 클래스를 반환
    
    Args:
        value: 손익 값
        format_type: "amount" (금액) 또는 "percentage" (퍼센트)
    
    Returns:
        formatted_value와 css_class를 포함한 딕셔너리
    """
    try:
        if value is None:
            return {"formatted_value": "0", "css_class": ""}
        
        num_value = float(value)
        
        # CSS 클래스 결정
        if num_value > 0:
            css_class = "text-danger"  # 빨간색 (수익)
        elif num_value < 0:
            css_class = "text-primary"  # 파란색 (손실)
        else:
            css_class = ""
        
        # 값 포매팅
        if format_type == "percentage":
            formatted_value = format_percentage(num_value)
        else:
            formatted_value = format_currency(num_value)
        
        return {
            "formatted_value": formatted_value,
            "css_class": css_class
        }
    except (ValueError, TypeError):
        return {"formatted_value": "0", "css_class": ""}
