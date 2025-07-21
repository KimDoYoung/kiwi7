def get_today() -> str:
    """오늘 날짜를 'YYYY-MM-DD' 형식으로 반환합니다."""
    from datetime import datetime
    return datetime.now().strftime('%Y-%m-%d')