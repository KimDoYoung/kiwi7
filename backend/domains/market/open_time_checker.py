# backend/domains/market/open_time_checker.py
# open_time_checker.py
"""
모듈 설명: 
    - 주식 시장의 개장 및 휴장 시간을 확인하는 기능을 제공하는 모듈입니다.
    - 싱글레톤
    - KST = ZoneInfo("Asia/Seoul")
    - checker = OpenTimeChecker.get()
    - now = datetime.now(tz=KST)
    - await checker.await checker.getMarket(now)
주요 기능:
    -   주식 시장의 개장 및 휴장 시간 확인
    -   정부 공휴일 및 주말에 따른 휴장일 판별
    -   KRX 및 NXT 시장의 영업 시간 확인

작성자: 김도영
작성일: 2025-08-14
버전: 1.0
"""
from __future__ import annotations
import asyncio
import aiohttp
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import Dict, Optional, Set, Tuple, Literal
from zoneinfo import ZoneInfo

from backend.core.config import config  # GODATA_API_KEY, TZ

Market = Literal["KRX", "NXT"]
KST = ZoneInfo(getattr(config, "TIME_ZONE", "Asia/Seoul"))

def now_kst() -> datetime:
    return datetime.now(tz=KST)

def yyyymmdd(d: date) -> str:
    return d.strftime("%Y%m%d")

@dataclass
class _MonthCache:
    holidays: Set[str] = field(default_factory=set)  # {"20250815", ...}
    last_fetch_ymd: str = ""                        # 이 월 데이터를 마지막으로 가져온 '오늘' yyyymmdd

class OpenTimeChecker:
    """정부공휴일 + 주말 기반 휴장/영업시간(KRX/NXT) 판정 (DB 없이 메모리 캐시).
       변경점: 날짜 바뀌면 월 캐시 재조회(1일 1회/월별), 월말엔 다음 달 프리패치.
    """
    _instance: Optional["OpenTimeChecker"] = None
    _fetch_lock = asyncio.Lock()

    def __init__(self):
        self._today_key: Optional[str] = None
        self._today_is_holiday: Optional[bool] = None
        self._month_cache: Dict[Tuple[int, int], _MonthCache] = {}
        self._api_url = getattr(
            config, 
            "GODATA_URL",
            "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo"
        )
        self._api_key = config.GODATA_API_KEY

    @classmethod
    def get(cls) -> "OpenTimeChecker":
        if cls._instance is None:
            cls._instance = OpenTimeChecker()
        return cls._instance

    async def getMarket(self, dt: Optional[datetime] = None) -> Optional[Market]:
        dt = dt.astimezone(KST) if dt else now_kst()
        if await self.isHoliday(dt.date()):
            return None
        if self.isKrxTime(dt):
            return "KRX"
        if self.isNxtTime(dt):
            return "NXT"
        return None

    async def isHoliday(self, d: Optional[date] = None) -> bool:
        d = d or now_kst().date()
        key = yyyymmdd(d)

        # 오늘 캐시
        if self._today_key == key and self._today_is_holiday is not None:
            return self._today_is_holiday

        # 주말
        if d.weekday() >= 5:
            self._set_today_cache(key, True)
            return True

        # (중요) 월별 데이터: '오늘'이 바뀌었으면 이 달을 재조회
        hol_set = await self._get_month_holidays(d.year, d.month, today_ymd=key)

        # 월말(예: 25일 이후)에는 다음 달 프리패치 (비차단; 실패해도 문제 없음)
        if d.day >= 25:
            asyncio.create_task(self._prefetch_next_month(d, today_ymd=key))

        is_hol = key in hol_set
        self._set_today_cache(key, is_hol)
        return is_hol

    def isKrxTime(self, dt: Optional[datetime] = None) -> bool:
        dt = dt.astimezone(KST) if dt else now_kst()
        t = dt.time()
        return time(9, 0) <= t < time(15, 30)

    def isNxtTime(self, dt: Optional[datetime] = None) -> bool:
        dt = dt.astimezone(KST) if dt else now_kst()
        t = dt.time()
        early = time(8, 0) <= t <= time(8, 50)
        late  = time(15, 30) <= t < time(20, 0)
        return early or late

    async def force_refresh(self):
        self._today_key = None
        self._today_is_holiday = None
        self._month_cache.clear()

    def _set_today_cache(self, key: str, value: bool):
        self._today_key = key
        self._today_is_holiday = value

    async def _get_month_holidays(self, year: int, month: int, today_ymd: str) -> Set[str]:
        """월 캐시가 없으면 생성, 있고 'last_fetch_ymd != today'면 재조회 → 일자 바뀌면 다시 호출."""
        k = (year, month)

        # 동시성 보호 (여러 코루틴이 같은 달을 동시에 갱신하려 할 때)
        async with self._fetch_lock:
            mc = self._month_cache.get(k)

            # 캐시 없음 → API 호출
            if mc is None:
                hol, fetched_today = await self._fetch_holidays_from_api(year, month), today_ymd
                self._month_cache[k] = _MonthCache(holidays=hol, last_fetch_ymd=fetched_today)
                return hol

            # 캐시 있음 & 오늘이 바뀌었으면 → API 다시 호출(일 1회)
            if mc.last_fetch_ymd != today_ymd:
                hol, fetched_today = await self._fetch_holidays_from_api(year, month), today_ymd
                mc.holidays = hol
                mc.last_fetch_ymd = fetched_today
                return hol

            # 오늘 이미 최신
            return mc.holidays

    async def _prefetch_next_month(self, d: date, today_ymd: str):
        """월말 근처이면 다음 달도 '오늘' 기준으로 한 번 갱신(비동기)."""
        nm_year = d.year + (1 if d.month == 12 else 0)
        nm_month = 1 if d.month == 12 else d.month + 1
        _ = await self._get_month_holidays(nm_year, nm_month, today_ymd=today_ymd)

    async def _fetch_holidays_from_api(self, year: int, month: int) -> Set[str]:
        # rate-limit 보호
        await asyncio.sleep(1)
        params = {
            "serviceKey": self._api_key,
            "solYear": str(year),
            "solMonth": f"{month:02d}",
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self._api_url, params=params, ssl=False) as resp:
                    if resp.status != 200:
                        return set()
                    text = await resp.text()
        except Exception:
            return set()

        root = ET.fromstring(text)
        holidays = set()
        for item in root.findall(".//item"):
            if item.findtext("isHoliday") == "Y":
                loc = item.findtext("locdate")
                if loc:
                    holidays.add(loc.strip())
        return holidays
