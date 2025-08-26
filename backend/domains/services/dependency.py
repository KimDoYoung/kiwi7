"""
서비스 의존성 관리 모듈 - 모든 도메인 서비스를 한 곳에서 관리
"""


# 각 서비스 클래스들을 직접 import

# 싱글톤 인스턴스 저장소
from backend.domains.services.my_stock_service import MyStockService
from backend.domains.services.settings_service import SettingsService
from backend.domains.services.stk_cache_service import StkCacheService
from backend.domains.services.stk_diary_service import StkDiaryService
from backend.domains.services.stk_info_service import StkInfoService
from backend.domains.services.stk_trade_history_service import StkTradeHistoryService


_services = {}

def get_service(name: str):
    """
    서비스명으로 서비스 인스턴스를 가져옴 (싱글톤 패턴)
    
    Args:
        name: 서비스명 ('my_stock', 'stk_info', 'account', 'trading_log', 'watchlist')
    
    Returns:
        서비스 인스턴스
    
    Raises:
        ValueError: 알 수 없는 서비스명인 경우
    """
    if name in _services:
        return _services[name]
    
    # 서비스 클래스 매핑
    service_classes = {
        'my_stock': MyStockService,
        'settings': SettingsService,
        'stk_cache' : StkCacheService,
        'stk_diary' : StkDiaryService,
        'stk_info' : StkInfoService,
        'stk_trade_history' : StkTradeHistoryService
    }
    
    if name not in service_classes:
        raise ValueError(f"알 수 없는 DB 서비스(테이블명과 그에 따른 service가 없음): {name}")
    
    _services[name] = service_classes[name]()
    
    return _services[name]