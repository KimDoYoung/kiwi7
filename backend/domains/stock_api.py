# stock_api.py
"""
모듈 설명: 
    - 주식회사 API를 사용하기 위한 추상 클래스
주요 기능:
    - user_id, acctno를 가지고, user_service를 가지고 있다.
작성자: 김도영
작성일: 2024-07-08
버전: 1.0
"""
from abc import ABC, abstractmethod

class StockApi(ABC):
    def __init__(self, acctno, user_service=None):
        self.acctno = acctno
        self.user_service = user_service


    @abstractmethod  # 추상 메서드로 선언
    async def refresh_token(self)-> bool:
        pass  # stock company api 연결가능여부 확인
