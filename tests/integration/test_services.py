"""
도메인 로직 통합 테스트
"""
import pytest


@pytest.mark.integration
@pytest.mark.skip(reason="DB 모킹 필요")
def test_mystock_service():
    """MyStock 서비스 통합 테스트 예제"""
    # from backend.domains.stocks.my_stock_service import MyStockService
    # 
    # service = MyStockService(db_path="test.db")
    # 
    # # 종목 추가
    # result = service.add_stock("005930", "삼성전자", is_watch=True)
    # assert result is True
    # 
    # # 종목 조회
    # stock = service.get_stock("005930")
    # assert stock is not None
    # assert stock.stk_nm == "삼성전자"
    pass


@pytest.mark.integration
@pytest.mark.slow
@pytest.mark.skip(reason="외부 API 호출")
async def test_kiwoom_api_integration():
    """키움 API 통합 테스트 (실제 API 호출 필요)"""
    # from backend.domains.kiwoom.kiwoom_service import KiwoomService
    # 
    # service = KiwoomService()
    # 
    # # 토큰 발급 테스트
    # token = await service.get_token()
    # assert token is not None
    pass


@pytest.mark.integration
def test_scheduler_job_registration():
    """스케줄러 잡 등록 테스트 예제"""
    # from backend.domains.kscheduler.k_scheduler import KScheduler
    # 
    # scheduler = KScheduler(db_path=":memory:", poll_sec=1)
    # 
    # # 잡 등록
    # job_id = scheduler.add_job(
    #     job_id="test_job",
    #     func=lambda: print("test"),
    #     interval=60
    # )
    # 
    # assert job_id == "test_job"
    pass
