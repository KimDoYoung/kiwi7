"""종목 가격 추이 메모리 캐시 (10일치 + 추세 분석 + 멀티 API)"""

import random
from datetime import datetime
from typing import Dict, Literal, Optional

from backend.core.logger import get_logger
from backend.domains.stkcompanys.kis.models.kis_schema import KisApiHelper

logger = get_logger(__name__)

Trend = Literal[
    '5일연속 오름',
    '3연속 오름',
    '5일연속 하락',
    '3연속 하락',
    '등락 중',
    '데이터 부족',
]


class PriceData:
    """종목의 10일치 가격 데이터"""

    def __init__(self):
        self.prices: list[float] = []  # 10일치 가격 (오래된 순)
        self.dates: list[str] = []      # 각 가격의 날짜 (YYYY-MM-DD)
        self.trend: Trend = '데이터 부족'

    def add_price(self, date: str, price: float) -> None:
        """가격 추가 (10일을 초과하면 가장 오래된 날 제거)

        Args:
            date: 날짜 (YYYY-MM-DD)
            price: 종가
        """
        self.dates.append(date)
        self.prices.append(price)

        # 10일 초과시 가장 오래된 날 제거
        if len(self.prices) > 10:
            self.prices.pop(0)
            self.dates.pop(0)

        self._update_trend()

    def set_prices(self, dates: list[str], prices: list[float]) -> None:
        """10일치 가격 한 번에 설정

        Args:
            dates: 날짜 리스트 (오래된 순, YYYY-MM-DD)
            prices: 가격 리스트 (오래된 순)
        """
        if len(dates) != len(prices):
            raise ValueError('dates와 prices의 길이가 맞지 않음')

        # 날짜로 정렬 (오래된 순 보장)
        sorted_data = sorted(zip(dates, prices), key=lambda x: x[0])
        sorted_dates = [d for d, _ in sorted_data]
        sorted_prices = [p for _, p in sorted_data]

        # 10일 초과시만 최근 10일 유지
        if len(sorted_dates) > 10:
            self.dates = sorted_dates[-10:]
            self.prices = sorted_prices[-10:]
        else:
            self.dates = sorted_dates
            self.prices = sorted_prices

        self._update_trend()

    def _update_trend(self) -> None:
        """현재 가격 데이터로 추세 업데이트"""
        self.trend = self._calculate_trend(self.prices)

    @staticmethod
    def _calculate_trend(prices: list[float]) -> Trend:
        """가격 리스트로 추세 판단

        Args:
            prices: 가격 리스트 (오래된 순)

        Returns:
            추세 문자열
        """
        if len(prices) < 2:
            return '데이터 부족'

        # 5일 연속 상승/하락 체크
        if len(prices) >= 5:
            last_5 = prices[-5:]
            # 5일 연속 상승 (각 날이 전날보다 높음)
            if all(last_5[i] < last_5[i + 1] for i in range(4)):
                return '5일연속 오름'
            # 5일 연속 하락
            elif all(last_5[i] > last_5[i + 1] for i in range(4)):
                return '5일연속 하락'

        # 3일 연속 상승/하락 체크
        if len(prices) >= 3:
            last_3 = prices[-3:]
            # 3일 연속 상승
            if all(last_3[i] < last_3[i + 1] for i in range(2)):
                return '3연속 오름'
            # 3일 연속 하락
            elif all(last_3[i] > last_3[i + 1] for i in range(2)):
                return '3연속 하락'

        # 위의 패턴에 해당하지 않으면 등락 중
        return '등락 중'

    def to_dict(self) -> dict:
        """딕셔너리로 변환"""
        return {
            'prices': self.prices,
            'dates': self.dates,
            'trend': self.trend,
        }

    def __repr__(self) -> str:
        return f"PriceData(days={len(self.prices)}, trend={self.trend})"


class PrevPriceCache:
    """10일치 가격 정보 메모리 캐시 (싱글톤)

    특징:
    - 각 종목의 10일치 가격 데이터 저장
    - 자동으로 추세 분석 (5일/3일 연속 상/하락, 등락 중)
    - 메모리 기반으로 초고속 조회
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._cache = {}
            cls._instance._last_update = None
        return cls._instance

    async def get(self, stk_cd: str) -> Optional[PriceData]:
        """종목의 10일치 가격 데이터 조회

        Args:
            stk_cd: 종목코드

        Returns:
            PriceData 객체 또는 None
        """
        return self._cache.get(stk_cd)

    async def get_trend(self, stk_cd: str) -> Optional[Trend]:
        """종목의 추세 조회

        Args:
            stk_cd: 종목코드

        Returns:
            추세 문자열 또는 None
        """
        data = self._cache.get(stk_cd)
        return data.trend if data else None

    async def get_prices(self, stk_cd: str) -> Optional[list[float]]:
        """종목의 10일치 가격 조회

        Args:
            stk_cd: 종목코드

        Returns:
            가격 리스트 또는 None
        """
        data = self._cache.get(stk_cd)
        return data.prices if data else None

    async def get_multi(self, stk_cd_list: list[str]) -> Dict[str, Optional[PriceData]]:
        """여러 종목의 가격 데이터 조회

        Args:
            stk_cd_list: 종목코드 리스트

        Returns:
            {종목코드: PriceData} 딕셔너리
        """
        return {stk_cd: self._cache.get(stk_cd) for stk_cd in stk_cd_list}

    async def set(self, stk_cd: str, dates: list[str], prices: list[float]) -> None:
        """종목의 10일치 가격 데이터 저장

        Args:
            stk_cd: 종목코드
            dates: 날짜 리스트 (YYYY-MM-DD)
            prices: 가격 리스트
        """
        data = PriceData()
        data.set_prices(dates, prices)
        self._cache[stk_cd] = data
        logger.debug(
            f"가격 캐시 저장: {stk_cd} - {len(prices)}일치, 추세: {data.trend}"
        )

    async def add_price(self, stk_cd: str, date: str, price: float) -> None:
        """종목에 오늘 가격 추가

        Args:
            stk_cd: 종목코드
            date: 날짜 (YYYY-MM-DD)
            price: 종가
        """
        if stk_cd not in self._cache:
            self._cache[stk_cd] = PriceData()

        self._cache[stk_cd].add_price(date, price)
        logger.debug(f"가격 추가: {stk_cd} {date}={price}, 추세: {self._cache[stk_cd].trend}")

    async def set_multi(self, data_dict: Dict[str, tuple[list[str], list[float]]]) -> None:
        """여러 종목의 10일치 가격 일괄 저장

        Args:
            data_dict: {종목코드: (dates, prices)}
        """
        for stk_cd, (dates, prices) in data_dict.items():
            data = PriceData()
            data.set_prices(dates, prices)
            self._cache[stk_cd] = data

        logger.info(f"가격 캐시 갱신: {len(data_dict)}개 종목 저장됨")

    async def update_all(
        self,
        data_dict: Dict[str, tuple[list[str], list[float]]],
    ) -> None:
        """전체 캐시 갱신 (스케줄러에서 호출)

        Args:
            data_dict: {종목코드: (dates, prices)}
        """
        await self.set_multi(data_dict)
        self._last_update = datetime.now()
        logger.info(f"가격 캐시 전체 갱신 완료 ({self._last_update})")

    async def clear(self, stk_cd: Optional[str] = None) -> None:
        """캐시 초기화

        Args:
            stk_cd: 종목코드 (None이면 전체 초기화)
        """
        if stk_cd:
            self._cache.pop(stk_cd, None)
            logger.info(f"가격 캐시 삭제: {stk_cd}")
        else:
            self._cache.clear()
            self._last_update = None
            logger.info("가격 캐시 전체 초기화됨")

    def get_stats(self) -> dict:
        """캐시 통계 반환

        Returns:
            {
                "count": 캐시된 종목 수,
                "last_update": 마지막 갱신 시각,
                "trends": 추세별 종목 수
            }
        """
        trends: Dict[Trend, int] = {
            '5일연속 오름': 0,
            '3연속 오름': 0,
            '5일연속 하락': 0,
            '3연속 하락': 0,
            '등락 중': 0,
            '데이터 부족': 0,
        }

        for data in self._cache.values():
            trends[data.trend] += 1

        return {
            'count': len(self._cache),
            'last_update': self._last_update,
            'trends': trends,
        }

    def __repr__(self) -> str:
        return f"PrevPriceCache(count={len(self._cache)}, last_update={self._last_update})"

    async def get_last_price(self, stk_cd: str) -> Optional[float]:
        """종목의 최신 종가 조회 (어제 종가, 캐시 미스시 API 호출)

        오늘은 시장이 아직 닫혀있지 않으므로 어제 종가를 반환

        Args:
            stk_cd: 종목코드

        Returns:
            어제 종가 (prices[-2]) 또는 None
        """
        # 캐시에서 먼저 조회
        data = self._cache.get(stk_cd)
        if data and len(data.prices) >= 2:
            return data.prices[-2]

        # 캐시 미스: API 호출로 10일 데이터 로드
        try:
            prices, dates = await self._fetch_price_data(stk_cd)
            if prices and dates and len(prices) >= 2:
                await self.set(stk_cd, dates, prices)
                return prices[-2]
        except Exception as e:
            logger.error(f"가격 데이터 조회 실패 ({stk_cd}): {e}")

        return None

    async def get_last_trend(self, stk_cd: str) -> Optional[Trend]:
        """종목의 최신 추세 조회 (캐시 미스시 API 호출)

        Args:
            stk_cd: 종목코드

        Returns:
            추세 문자열 또는 None
        """
        # 캐시에서 먼저 조회
        data = self._cache.get(stk_cd)
        if data:
            return data.trend

        # 캐시 미스: API 호출로 10일 데이터 로드
        try:
            prices, dates = await self._fetch_price_data(stk_cd)
            if prices and dates:
                await self.set(stk_cd, dates, prices)
                return self._cache[stk_cd].trend
        except Exception as e:
            logger.error(f"가격 데이터 조회 실패 ({stk_cd}): {e}")

        return None

    async def _fetch_price_data(self, stk_cd: str) -> tuple[Optional[list[float]], Optional[list[str]]]:
        """3개 증권사 API 중 랜덤하게 선택하여 10일 가격 데이터 조회

        Args:
            stk_cd: 종목코드

        Returns:
            (가격 리스트, 날짜 리스트) 또는 (None, None)
        """
        # 랜덤 순서로 3개 API 시도
        apis = ['kiwoom', 'kis', 'ls']
        random.shuffle(apis)

        for api_name in apis:
            try:
                if api_name == 'kiwoom':
                    result = await self._fetch_from_kiwoom(stk_cd)
                elif api_name == 'kis':
                    result = await self._fetch_from_kis(stk_cd)
                elif api_name == 'ls':
                    result = await self._fetch_from_ls(stk_cd)
                
                if result != (None, None):  # 데이터 획득 성공
                    return result
                    
            except Exception as e:
                logger.warning(f"{api_name} API 호출 실패 ({stk_cd}): {e}")
                continue


        logger.error(f"모든 API 호출 실패 ({stk_cd})")
        return None, None

    async def _fetch_from_kiwoom(self, stk_cd: str) -> tuple[list[float], list[str]]:
        """Kiwoom API (ka10086) 호출"""
        from backend.domains.stkcompanys.kiwoom.kiwoom_service import get_kiwoom_api
        from backend.domains.stkcompanys.kiwoom.models.kiwoom_schema import KiwoomRequest

        kiwoom = await get_kiwoom_api()
        if not kiwoom:
            raise Exception("Kiwoom API 생성 실패")

        # 현재 날짜로 조회 (YYYYMMDD 형식)
        today = datetime.now().strftime('%Y%m%d')

        response = await kiwoom.send_request(
            KiwoomRequest(api_id='ka10086', payload={'stk_cd': stk_cd, 'qry_dt': today, 'indc_tp': '1'})
        )

        if not response.success or not response.data or 'daly_stkpc' not in response.data:
            raise Exception(f"Kiwoom API 응답 오류: {response.error_message}")

        prices = []
        dates = []
        for item in response.data['daly_stkpc']:
            try:
                date_str = item.get('date', '')
                close_str = item.get('close_pric', '')

                # 날짜 형식: YYYYMMDD -> YYYY-MM-DD
                if len(date_str) == 8:
                    date_str = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"

                # 가격에서 +/- 부호 제거하고 숫자만 추출
                close_price = float(close_str.lstrip('+-'))
                # date_str에서 대쉬제거
                date_str = date_str.replace('-', '')
                dates.append(date_str)
                prices.append(int(close_price))
            except (ValueError, KeyError):
                continue

        # 날짜 기준으로 정렬 (오래된 순)
        if dates and prices:
            sorted_data = sorted(zip(dates, prices), key=lambda x: x[0])
            dates = [d for d, _ in sorted_data]
            prices = [p for _, p in sorted_data]

        return prices, dates

    async def _fetch_from_kis(self, stk_cd: str) -> tuple[list[float], list[str]]:
        """KIS API (FHKST01010400) 호출"""
        from backend.domains.stkcompanys.kis.kis_service import get_kis_api
        from backend.domains.stkcompanys.kis.models.kis_schema import KisRequest

        kis = await get_kis_api()
        if not kis:
            raise Exception("KIS API 생성 실패")

        response = await kis.send_request(
            KisRequest(
                api_id='FHKST01010400',
                payload={
                    'FID_COND_MRKT_DIV_CODE': 'J',
                    'FID_INPUT_ISCD': stk_cd,
                    'FID_PERIOD_DIV_CODE': 'D',
                    'FID_ORG_ADJ_PRC': '0',
                },
            )
        )

        if not response.success or not response.data or 'output' not in response.data:
            raise Exception(f"KIS API 응답 오류: {response.error_message}")
        korea_data = KisApiHelper.to_korea_data(response.data, 'FHKST01010400')
        prices = []
        dates = []
        for item in korea_data['output']:
            try:
                date_str = item.get('주식영업일자', '')  # 한글 키명
                close_str = item.get('주식종가', '')

                # 날짜 형식: YYYYMMDD -> YYYY-MM-DD
                if len(date_str) == 8:
                    date_str = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"

                close_price = float(close_str)

                dates.append(date_str)
                prices.append(close_price)
            except (ValueError, KeyError):
                continue

        # 날짜 기준으로 정렬 (오래된 순)
        if dates and prices:
            sorted_data = sorted(zip(dates, prices), key=lambda x: x[0])
            dates = [d for d, _ in sorted_data]
            prices = [p for _, p in sorted_data]

        return prices, dates

    async def _fetch_from_ls(self, stk_cd: str) -> tuple[list[float], list[str]]:
        """LS API (t8410) 호출"""
        from backend.domains.stkcompanys.ls.ls_service import get_ls_api
        from backend.domains.stkcompanys.ls.models.ls_schema import LsRequest

        ls = await get_ls_api()
        if not ls:
            raise Exception("LS API 생성 실패")

        response = await ls.send_request(
            LsRequest(
                api_id='t8410',
                payload={
                    'shcode': stk_cd,
                    'gubun': '2',  # 일봉
                    'qrycnt': 30,  # 최근 30일
                    'sdate': '',
                    'edate': '',
                    'cts_date': '',
                    'comp_yn': 'N',
                    'sujung': 'Y',
                },
            )
        )

        if not response.success or not response.data or 't8410OutBlock1' not in response.data:
            raise Exception(f"LS API 응답 오류: {response.error_message}")

        prices = []
        dates = []
        for item in response.data['t8410OutBlock1']:
            try:
                date_str = item.get('date', '')
                close_str = item.get('close', '')

                # 날짜 형식: YYYYMMDD -> YYYY-MM-DD
                if len(str(date_str)) == 8:
                    date_str = f"{str(date_str)[:4]}-{str(date_str)[4:6]}-{str(date_str)[6:8]}"

                close_price = float(close_str)

                dates.append(date_str)
                prices.append(int(close_price))
            except (ValueError, KeyError):
                continue

        # 날짜 기준으로 정렬 (오래된 순)
        if dates and prices:
            sorted_data = sorted(zip(dates, prices), key=lambda x: x[0])
            dates = [d for d, _ in sorted_data]
            prices = [p for _, p in sorted_data]

        return prices, dates


def get_prev_price_cache() -> PrevPriceCache:
    """싱글톤 인스턴스 반환"""
    return PrevPriceCache()
