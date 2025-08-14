# debug_open_time_checker.py
"""
모듈 설명: 
    -   설명을 넣으시오
주요 기능:
    -   기능을 넣으시오

# 1) 현재 상태 출력 (+ 트레이싱)
python scripts/debug_open_time_checker.py now --trace

# 2) 특정 시각 확인
python scripts/debug_open_time_checker.py at --at "2025-08-15 09:10" --trace

# 3) 하루 단위로 20분 간격 스캔
python scripts/debug_open_time_checker.py walk-day --day "2025-08-14" --step-min 20 --trace

# 4) 날짜 변경 시 월 캐시 재호출 확인 (예: 8/31 → 9/1)
python scripts/debug_open_time_checker.py sim-refetch --day1 "2025-08-31" --day2 "2025-09-01" --time "09:05" --trace

# 5) 네트워크 없이 페이크 휴일로 테스트(광복절/추석 가정)
python scripts/debug_open_time_checker.py at --at "2025-08-15 10:00" --fake-holidays "2025-08-15,2025-09-16"


작성자: 김도영
작성일: 2025-08-14
버전: 1.0
"""
# scripts/debug_open_time_checker.py
import argparse
import asyncio
from datetime import datetime, timedelta, date, time as dtime
from zoneinfo import ZoneInfo

from backend.domains.market.open_time_checker import OpenTimeChecker, yyyymmdd

# --------------------------------------------------
# 유틸
# --------------------------------------------------
KST = ZoneInfo("Asia/Seoul")

def parse_dt(s: str) -> datetime:
    # "YYYY-MM-DD HH:MM"
    return datetime.strptime(s, "%Y-%m-%d %H:%M").replace(tzinfo=KST)

def parse_d(s: str) -> date:
    # "YYYY-MM-DD"
    return datetime.strptime(s, "%Y-%m-%d").date()

def kst_combine(d: date, t: dtime) -> datetime:
    return datetime(d.year, d.month, d.day, t.hour, t.minute, tzinfo=KST)

def hr(s: str = "-"):
    print(s * 60)

# --------------------------------------------------
# 트레이싱 헬퍼: API 호출 시점 출력
# --------------------------------------------------
def attach_trace(checker: OpenTimeChecker):
    original = checker._fetch_holidays_from_api  # noqa: SLF001 (debug 용)
    async def traced(year: int, month: int):
        print(f"[TRACE] API fetch called for {year}-{month:02d}")
        return await original(year, month)
    checker._fetch_holidays_from_api = traced  # type: ignore[attr-defined]

# --------------------------------------------------
# 페이크 휴일 주입 (네트워크 없이 테스트)
# ex) --fake-holidays 2025-08-15,2025-09-16
# --------------------------------------------------
def attach_fake_holidays(checker: OpenTimeChecker, fake_dates: list[str]):
    # month 캐시에 직접 주입 (debug 용)
    from dataclasses import dataclass, field
    from typing import Set, Tuple, Dict

    @dataclass
    class _MonthCache:
        holidays: Set[str] = field(default_factory=set)
        last_fetch_ymd: str = ""  # 오늘 yyyymmdd

    # 모듈의 _MonthCache와 동일 구조로 만들었지만, 디버그용이라 간단히 사용
    month_map: Dict[Tuple[int, int], _MonthCache] = {}
    for s in fake_dates:
        d = parse_d(s)
        key = (d.year, d.month)
        month_map.setdefault(key, _MonthCache()).holidays.add(yyyymmdd(d))

    checker._month_cache = month_map  # type: ignore[attr-defined]
    checker._today_key = None         # type: ignore[attr-defined]
    checker._today_is_holiday = None  # type: ignore[attr-defined]

    async def fake_fetch(year: int, month: int):
        # API 호출 없이 캐시만 사용. 캐시에 없으면 빈 집합
        print(f"[TRACE] fake fetch for {year}-{month:02d} (no network)")
        return month_map.get((year, month), _MonthCache()).holidays

    checker._fetch_holidays_from_api = fake_fetch  # type: ignore[attr-defined]

# --------------------------------------------------
# 시나리오들
# --------------------------------------------------
async def scenario_now(checker: OpenTimeChecker):
    now = datetime.now(tz=KST)
    print("[NOW]", now.isoformat())
    print("isHoliday:", await checker.isHoliday(now.date()))
    print("isKrxTime:", checker.isKrxTime(now))
    print("isNxtTime:", checker.isNxtTime(now))
    print("getMarket :", await checker.getMarket(now))

async def scenario_at(checker: OpenTimeChecker, at_str: str):
    dt = parse_dt(at_str)
    print("[AT]", dt.isoformat())
    print("isHoliday:", await checker.isHoliday(dt.date()))
    print("isKrxTime:", checker.isKrxTime(dt))
    print("isNxtTime:", checker.isNxtTime(dt))
    print("getMarket :", await checker.getMarket(dt))

async def scenario_walk_day(checker: OpenTimeChecker, day_str: str, step_min: int):
    d = parse_d(day_str)
    start = kst_combine(d, dtime(7, 30))
    end   = kst_combine(d, dtime(20, 30))
    cur = start
    first = True
    while cur <= end:
        if first:
            print(f"[DAY WALK] {day_str} / step={step_min}m")
            print("time   | holiday | market | KRX | NXT")
            first = False
        is_h = await checker.isHoliday(cur.date())
        krx = checker.isKrxTime(cur)
        nxt = checker.isNxtTime(cur)
        mk  = await checker.getMarket(cur)
        print(f"{cur.strftime('%H:%M')} | {str(is_h):7} | {str(mk or 'None'):6} | {str(krx):3} | {str(nxt):3}")
        cur += timedelta(minutes=step_min)

async def scenario_sim_refetch(checker: OpenTimeChecker, day1: str, day2: str, check_time: str = "09:05"):
    """날짜가 바뀌면 월 캐시가 다시 갱신되는지(= API 재호출) 확인"""
    t = datetime.strptime(check_time, "%H:%M").time()
    d1, d2 = parse_d(day1), parse_d(day2)

    dt1 = kst_combine(d1, t)
    dt2 = kst_combine(d2, t)

    print("[REFETCH] 첫번째 호출(당일)")
    print("  ->", dt1.isoformat())
    print("  isHoliday:", await checker.isHoliday(dt1.date()))
    print("  market   :", await checker.getMarket(dt1))

    hr("=")
    print("[REFETCH] 날짜가 바뀐 뒤 첫 호출(다음날)")
    print("  ->", dt2.isoformat())
    print("  isHoliday:", await checker.isHoliday(dt2.date()))
    print("  market   :", await checker.getMarket(dt2))

# --------------------------------------------------
# main
# --------------------------------------------------
def build_argparser():
    p = argparse.ArgumentParser(description="OpenTimeChecker Debug CLI (no pytest)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s_now = sub.add_parser("now", help="현재 시각 상태 출력")
    s_now.add_argument("--trace", action="store_true", help="API 호출 트레이싱")

    s_at = sub.add_parser("at", help="특정 시각 상태 출력")
    s_at.add_argument("--at", required=True, help='예: "2025-08-15 09:10" (KST)')
    s_at.add_argument("--trace", action="store_true")

    s_walk = sub.add_parser("walk-day", help="하루를 일정 간격으로 스캔")
    s_walk.add_argument("--day", required=True, help='예: "2025-08-15"')
    s_walk.add_argument("--step-min", type=int, default=30)
    s_walk.add_argument("--trace", action="store_true")

    s_ref = sub.add_parser("sim-refetch", help="날짜 변경 시 월 캐시 재호출 확인")
    s_ref.add_argument("--day1", required=True, help='예: "2025-08-31"')
    s_ref.add_argument("--day2", required=True, help='예: "2025-09-01"')
    s_ref.add_argument("--time", default="09:05", help='예: "09:05"')
    s_ref.add_argument("--trace", action="store_true")

    # 공통 옵션
    for sp in (s_now, s_at, s_walk, s_ref):
        sp.add_argument("--fake-holidays", help='콤마구분: "2025-08-15,2025-09-16" (네트워크 없이)')

    return p

async def amain():
    args = build_argparser().parse_args()
    checker = OpenTimeChecker.get()

    # 트레이스/페이크 옵션
    if getattr(args, "trace", False):
        attach_trace(checker)
    if args.fake_holidays:
        fake = [x.strip() for x in args.fake_holidays.split(",") if x.strip()]
        attach_fake_holidays(checker, fake)

    # 커맨드 실행
    if args.cmd == "now":
        await scenario_now(checker)
    elif args.cmd == "at":
        await scenario_at(checker, args.at)
    elif args.cmd == "walk-day":
        await scenario_walk_day(checker, args.day, args.step_min)
    elif args.cmd == "sim-refetch":
        await scenario_sim_refetch(checker, args.day1, args.day2, args.time)
    else:
        raise SystemExit(2)

def main():
    asyncio.run(amain())

if __name__ == "__main__":
    main()
