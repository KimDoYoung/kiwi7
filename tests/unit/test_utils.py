"""
유틸리티 함수 단위 테스트
"""
import pytest


@pytest.mark.unit
def test_basic_calculation():
    """기본 계산 테스트 예제"""
    # 매수 가능 수량 계산 예제
    available_cash = 1000000  # 100만원
    stock_price = 50000       # 5만원
    
    max_qty = available_cash // stock_price
    assert max_qty == 20


@pytest.mark.unit
def test_profit_calculation():
    """수익률 계산 테스트 예제"""
    buy_price = 10000
    sell_price = 11000
    
    profit_rate = ((sell_price - buy_price) / buy_price) * 100
    assert profit_rate == 10.0


@pytest.mark.unit
def test_sell_target_prices():
    """목표 매도가 계산 테스트"""
    current_price = 10000
    target_rates = [2, 3, 5, 7, 10]
    
    target_prices = [
        int(current_price * (1 + rate/100))
        for rate in target_rates
    ]
    
    assert target_prices == [10200, 10300, 10500, 10700, 11000]


@pytest.mark.unit
@pytest.mark.asyncio
async def test_async_function():
    """비동기 함수 테스트 예제"""
    import asyncio
    
    async def async_add(a, b):
        await asyncio.sleep(0.01)  # 비동기 작업 시뮬레이션
        return a + b
    
    result = await async_add(1, 2)
    assert result == 3
