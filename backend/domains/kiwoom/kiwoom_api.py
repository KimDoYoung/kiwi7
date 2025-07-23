# kiwoom_api.py
"""
모듈 설명: 
    - kiwoom 증권 OpenAPI를 활용한 주식 API 구현체

작성자: 김도영
작성일: 2025-07-23
버전: 1.0
"""
from datetime import datetime, timedelta
from typing import Optional
import aiohttp
from backend.domains.stock_api import StockApi
from backend.core.config import config
from backend.domains.user.user_service import UserService
from backend.core.exceptions import KiwoomAuthException


class KiwoomStockApi(StockApi):
    """
    키움증권 OpenAPI를 활용한 주식 API 구현체
    StockApi 인터페이스를 상속받아 키움증권 고유 기능을 구현합니다.
    """
    def __init__(self):
        super().__init__(config.KIWOOM_ACCT_NO, UserService())
        self.BASE_URL ='https://api.kiwoom.com'
        self.APP_KEY = config.KIWOOM_APP_KEY
        self.APP_SECRET = config.KIWOOM_SECRET_KEY
        self.ACCESS_TOKEN: Optional[str] = None
        self.ACCESS_TOKEN_EXPIRED_TIME: Optional[str] = None
    
    async def refresh_token(self) -> bool:
        """
        users DB에서 ACCESS_TOKEN과 ACCESS_TOKEN_TIME을 가져온다.
        없거나 시간이 12시간이 지났다면 ACCESS_TOKEN을 새로 발급받는다.
        table users에 보관한다. 20250724135248
        Returns:
            bool: 초기화 성공 여부
        """
        try:
            # 현재 갖고 있지 않으면 DB에서 가져온다
            if not self.ACCESS_TOKEN or not self.ACCESS_TOKEN_EXPIRED_TIME:
                token_info = await self.user_service.get("ACCESS_TOKEN")
                time_info = await self.user_service.get("ACCESS_TOKEN_EXPIRED_TIME")
                self.ACCESS_TOKEN = token_info.value if token_info else None
                self.ACCESS_TOKEN_EXPIRED_TIME = time_info.value if time_info else None            
            # DB에서도 없다면 발급받는다
            if not self.ACCESS_TOKEN or not self.ACCESS_TOKEN_EXPIRED_TIME:
                await self.issue_access_token()

            # 시각이 만료1시간 전이라면 다시 발급받는다.
            expire_time = datetime.strptime(self.ACCESS_TOKEN_EXPIRED_TIME, '%Y%m%d%H%M%S')
            if expire_time <= (datetime.now() + timedelta(hours=1)):
                await self.issue_access_token()
            
            return True
        except Exception as e:
            raise KiwoomAuthException(f"Failed to refresh token: {str(e)}")
        

    async def issue_access_token(self):
        """
        키움증권 OpenAPI를 통해 ACCESS_TOKEN을 발급받는다. DB에 저장
        """
        url = self.BASE_URL + '/oauth2/token'

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
        }
        params = {
            'grant_type': 'client_credentials',
            'appkey': self.APP_KEY,
            'secretkey': self.APP_SECRET,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=params) as response:
                if response.status != 200:
                    raise KiwoomAuthException(f"Failed to issue access token: {response.status}")
                resp_json = await response.json()
                self.ACCESS_TOKEN = resp_json.get("token")
                self.ACCESS_TOKEN_EXPIRED_TIME = resp_json.get("expires_dt")
                # DB에 저장하는 로직 추가 필요
                await self.user_service.set("ACCESS_TOKEN", self.ACCESS_TOKEN)
                await self.user_service.set("ACCESS_TOKEN_EXPIRED_TIME", self.ACCESS_TOKEN_EXPIRED_TIME)

