def get_today() -> str:
    """오늘 날짜를 'YYYY-MM-DD' 형식으로 반환합니다."""
    from datetime import datetime
    # 요일을 함께 표시하려면 strftime 포맷을 수정합니다.
    weekdays = ['월', '화', '수', '목', '금', '토', '일']
    today = datetime.now()
    weekday_str = weekdays[today.weekday()]
    return f"{today.strftime('%Y-%m-%d')} ({weekday_str})"