"""PrevPriceCache - 005930 단순 테스트"""

import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.core.logger import get_logger
from backend.domains.services.prev_price_cache import get_prev_price_cache

logger = get_logger(__name__)


async def main():
    cache = get_prev_price_cache()
    stk_cd = '005930'

    print(f"\n=== {stk_cd} 테스트 ===\n")

    try:
        # 최신 종가 조회 (캐시 미스 → API 호출)
        print("1. 최신 종가 조회...")
        price = await cache.get_last_price(stk_cd)
        print(f"   결과: {price}\n")

        # 추세 조회
        print("2. 추세 조회...")
        trend = await cache.get_last_trend(stk_cd)
        print(f"   결과: {trend}\n")

        # 전체 데이터 확인
        print("3. 캐시된 데이터 (날짜, 가격):")
        data = await cache.get(stk_cd)
        if data:
            print(f"   총 {len(data.prices)}일 데이터\n")
            for i, (date, price) in enumerate(zip(data.dates, data.prices)):
                print(f"   [{i}] {date} → {price:,.0f}원")
            print(f"\n   최신 종가 (prices[-1]): {data.prices[-1]:,.0f}원")
            print(f"   어제 종가 (prices[-2]): {data.prices[-2]:,.0f}원")
            print(f"   추세: {data.trend}")
        else:
            print("   데이터 없음")
        print("-------------------------------------------")
        price_prev = await cache.get_last_price('005930')
        print(f"=======>   005930 어제종가: {price_prev}\n")

        price_prev = await cache.get_last_price('000720')
        print(f"=======>   000720 어제종가: {price_prev}\n")
        
        price_prev = await cache.get_last_price('000660')
        print(f"=======>   000660 어제종가: {price_prev}\n")
        
        price_prev = await cache.get_last_price('009470')
        print(f"=======>   009470 어제종가: {price_prev}\n")

    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    asyncio.run(main())
