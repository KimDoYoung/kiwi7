# stock_api.py
"""
모듈 설명:
    - 주식회사 API를 사용하기 위한 추상 클래스
주요 기능:
    - user_id, acctno를 가지고, settings_service를 가지고 있다.
    - BrokerType enum으로 증권사 구분
작성자: 김도영
작성일: 2024-07-08
버전: 1.1
"""
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Optional


class BrokerType(str, Enum):
    """증권사 유형 열거형"""
    KIWOOM = "kiwoom"
    KIS = "kis"
    LS = "ls"


class StockApi(ABC):
    """주식 API 추상 베이스 클래스"""

    def __init__(self, acctno: str, settings_service=None, broker_type: Optional[BrokerType] = None):
        self.acctno = acctno
        self.settings_service = settings_service
        self.broker_type = broker_type

    @abstractmethod
    async def send_request(self, request: Any) -> Any:
        """API 요청 전송 - 각 증권사별 구현 필요"""
        pass

    def get_base_url(self) -> str:
        """증권사 API 베이스 URL"""
        raise NotImplementedError("Subclass must implement get_base_url method")

    @property
    def base_url(self) -> str:
        """증권사 API 베이스 URL (property 래퍼)"""
        return self.get_base_url()

