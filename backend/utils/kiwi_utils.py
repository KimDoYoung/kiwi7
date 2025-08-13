def get_today() -> str:
    """오늘 날짜를 'YYYY-MM-DD' 형식으로 반환합니다."""
    from datetime import datetime
    # 요일을 함께 표시하려면 strftime 포맷을 수정합니다.
    weekdays = ['월', '화', '수', '목', '금', '토', '일']
    today = datetime.now()
    weekday_str = weekdays[today.weekday()]
    return f"{today.strftime('%Y-%m-%d')} ({weekday_str})"


def merge_stock_info(response1_data, response2_data):
    """두 개의 주식 정보를 병합합니다."""
    if not response1_data or not response2_data:
        return None
    # 키가 중복되는 경우가 있음     
    merged_data = {
        "stk_cd": response1_data.get("stk_cd"),
        "stk_name": response1_data.get("stk_name"),
        "current_price": response2_data.get("current_price"),
        "high_price": response2_data.get("high_price"),
        "low_price": response2_data.get("low_price"),
    }

    return merged_data


def merge_dicts(dict1: dict, dict2: dict, merge_strategy: str = "override") -> dict:
    """
    두 개의 딕셔너리를 합치는 함수
    
    Args:
        dict1 (dict): 첫 번째 딕셔너리
        dict2 (dict): 두 번째 딕셔너리 
        merge_strategy (str): 키 충돌 시 병합 전략
            - "override": dict2의 값으로 덮어씀 (기본값)
            - "keep_first": dict1의 값을 유지
            - "combine": 가능한 경우 값을 결합 (리스트, 문자열 등)
    
    Returns:
        dict: 병합된 딕셔너리
        
    Examples:
        >>> dict1 = {"a": 1, "b": 2}
        >>> dict2 = {"b": 3, "c": 4}
        >>> merge_dicts(dict1, dict2)
        {"a": 1, "b": 3, "c": 4}
        
        >>> merge_dicts(dict1, dict2, "keep_first")
        {"a": 1, "b": 2, "c": 4}
        
        >>> dict1 = {"tags": ["python"], "name": "John"}
        >>> dict2 = {"tags": ["web"], "age": 30}
        >>> merge_dicts(dict1, dict2, "combine")
        {"tags": ["python", "web"], "name": "John", "age": 30}
    """
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError("Both arguments must be dictionaries")
    
    # 빈 딕셔너리 처리
    if not dict1:
        return dict2.copy()
    if not dict2:
        return dict1.copy()
    
    result = dict1.copy()
    
    for key, value in dict2.items():
        if key not in result:
            # 새로운 키는 그대로 추가
            result[key] = value
        else:
            # 키 충돌 시 병합 전략 적용
            if merge_strategy == "override":
                result[key] = value
            elif merge_strategy == "keep_first":
                # dict1의 값을 유지 (아무것도 하지 않음)
                pass
            elif merge_strategy == "combine":
                # 값 결합 시도
                existing_value = result[key]
                
                # 둘 다 리스트인 경우
                if isinstance(existing_value, list) and isinstance(value, list):
                    result[key] = existing_value + value
                # 둘 다 딕셔너리인 경우 (재귀 호출)
                elif isinstance(existing_value, dict) and isinstance(value, dict):
                    result[key] = merge_dicts(existing_value, value, merge_strategy)
                # 둘 다 문자열인 경우
                elif isinstance(existing_value, str) and isinstance(value, str):
                    result[key] = existing_value + " " + value
                # 둘 다 숫자인 경우
                elif isinstance(existing_value, (int, float)) and isinstance(value, (int, float)):
                    result[key] = existing_value + value
                else:
                    # 결합할 수 없는 타입은 override와 동일하게 처리
                    result[key] = value
            else:
                raise ValueError(f"Unknown merge strategy: {merge_strategy}")
    
    return result


def merge_multiple_dicts(*dicts: dict, merge_strategy: str = "override") -> dict:
    """
    여러 개의 딕셔너리를 한 번에 합치는 함수
    
    Args:
        *dicts: 합칠 딕셔너리들
        merge_strategy (str): 병합 전략 ("override", "keep_first", "combine")
    
    Returns:
        dict: 병합된 딕셔너리
        
    Example:
        >>> dict1 = {"a": 1}
        >>> dict2 = {"b": 2}  
        >>> dict3 = {"c": 3}
        >>> merge_multiple_dicts(dict1, dict2, dict3)
        {"a": 1, "b": 2, "c": 3}
    """
    if not dicts:
        return {}
    
    result = {}
    for d in dicts:
        if isinstance(d, dict):
            result = merge_dicts(result, d, merge_strategy)
    
    return result