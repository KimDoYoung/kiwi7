"""PrevPriceCache 메모리 캐시 테스트"""

import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.core.logger import get_logger
from backend.domains.services.prev_price_cache import get_prev_price_cache

logger = get_logger(__name__)


async def main():
    cache = get_prev_price_cache()

    # 테스트할 종목 리스트
    stocks = ['005930', '000660', '035720', '055550', '006400']

    print("=" * 70)
    print("PrevPriceCache 테스트")
    print("=" * 70)
    print()

    for stk_cd in stocks:
        print(f"\n[{stk_cd}] 테스트 시작...")
        print("-" * 70)

        try:
            # 1. 최신 종가 조회 (캐시 미스 → API 호출)
            print("  ├─ 최신 종가 조회...")
            price = await cache.get_last_price(stk_cd)
            print(f"  │  └─ 최신 종가: {price:,.0f}원" if price else "  │  └─ 조회 실패")

            # 2. 추세 조회 (캐시 미스 → API 호출)
            print("  ├─ 추세 조회...")
            trend = await cache.get_last_trend(stk_cd)
            print(f"  │  └─ 추세: {trend}")

            # 3. 전체 가격 데이터 조회 (캐시 히트)
            print("  ├─ 전체 가격 데이터 조회...")
            data = await cache.get(stk_cd)
            if data:
                print(f"  │  ├─ 저장된 일수: {len(data.prices)}일")
                print(f"  │  ├─ 날짜 범위: {data.dates[0]} ~ {data.dates[-1]}")
                print(f"  │  ├─ 가격 범위: {min(data.prices):,.0f}원 ~ {max(data.prices):,.0f}원")
                print(f"  │  ├─ 추세: {data.trend}")
                # 날짜-가격 매핑 확인 (최근 3일)
                print("  │  └─ 최근 3일 (인덱스: 날짜 → 가격):")
                for i in range(-3, 0):
                    if len(data.dates) + i >= 0:
                        print(f"  │     [{i}] {data.dates[i]} → {data.prices[i]:,.0f}원")

                # 날짜 정렬 상태 확인
                print("  │  └─ 날짜 정렬 검증: ", end="")
                is_sorted = all(data.dates[i] <= data.dates[i+1] for i in range(len(data.dates)-1))
                status = '오름차순' if is_sorted else '미정렬'
                print(status)
            else:
                print("  │  └─ 데이터 없음")

            # 4. 동일 종목 재조회 (캐시 히트 확인)
            print("  ├─ 재조회 (캐시 히트 확인)...")
            price2 = await cache.get_last_price(stk_cd)
            trend2 = await cache.get_last_trend(stk_cd)
            print(f"  │  ├─ 최신 종가: {price2:,.0f}원" if price2 else "  │  ├─ 조회 실패")
            print(f"  │  └─ 추세: {trend2}")

            print("  └─ [OK] 성공")
            price3 = await cache.get_last_price('005930')
            price4 = await cache.get_last_price('005930')
            print(f" {price3}, {price4}")
        except Exception as e:
            print(f"  └─ [ERROR] 오류: {e}")
            import traceback

            traceback.print_exc()

    # 최종 통계 출력
    print()
    print("=" * 70)
    print("캐시 통계")
    print("=" * 70)
    stats = cache.get_stats()
    print(f"캐시된 종목 수: {stats['count']}")
    print(f"마지막 갱신: {stats['last_update']}")
    print()
    print("추세별 종목 수:")
    for trend, count in stats['trends'].items():
        if count > 0:
            print(f"  {trend}: {count}개")


if __name__ == '__main__':
    asyncio.run(main())
