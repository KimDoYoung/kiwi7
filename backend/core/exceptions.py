"""
증권사 API 관련 예외 클래스들
증권사 API 호출 시 발생할 수 있는 다양한 오류 상황을 처리합니다.
"""


# === 공통 베이스 예외 ===
class BrokerApiException(Exception):
    """증권사 API 공통 예외 베이스 클래스"""

    def __init__(self, message: str, error_code: str = None, broker: str = None):
        self.message = message
        self.error_code = error_code
        self.broker = broker
        super().__init__(self.message)

    def __str__(self):
        prefix = f"[{self.broker}]" if self.broker else ""
        code = f"[{self.error_code}]" if self.error_code else ""
        return f"{prefix}{code} {self.message}"


class BrokerAuthException(BrokerApiException):
    """인증 관련 예외"""
    pass


class BrokerOrderException(BrokerApiException):
    """주문 관련 예외"""
    pass


class BrokerDataException(BrokerApiException):
    """데이터 조회 관련 예외"""
    pass


# === Kiwoom 예외 (기존 호환성 유지) ===
class KiwoomApiException(BrokerApiException):
    """키움증권 API 호출 시 발생하는 예외 클래스"""

    def __init__(self, message: str, error_code: str = None):
        super().__init__(message, error_code, broker="KIWOOM")


class KiwoomAuthException(KiwoomApiException):
    """키움증권 API 인증 관련 예외"""
    pass


class KiwoomOrderException(KiwoomApiException):
    """키움증권 주문 관련 예외"""
    pass


class KiwoomDataException(KiwoomApiException):
    """키움증권 데이터 조회 관련 예외"""
    pass


# === KIS(한국투자증권) 예외 ===
class KisApiException(BrokerApiException):
    """한국투자증권 API 호출 시 발생하는 예외 클래스"""

    def __init__(self, message: str, error_code: str = None):
        super().__init__(message, error_code, broker="KIS")


class KisAuthException(KisApiException):
    """한국투자증권 API 인증 관련 예외"""
    pass


class KisOrderException(KisApiException):
    """한국투자증권 주문 관련 예외"""
    pass


class KisDataException(KisApiException):
    """한국투자증권 데이터 조회 관련 예외"""
    pass


# === LS증권 예외 ===
class LsApiException(BrokerApiException):
    """LS증권 API 호출 시 발생하는 예외 클래스"""

    def __init__(self, message: str, error_code: str = None):
        super().__init__(message, error_code, broker="LS")


class LsAuthException(LsApiException):
    """LS증권 API 인증 관련 예외"""
    pass


class LsOrderException(LsApiException):
    """LS증권 주문 관련 예외"""
    pass


class LsDataException(LsApiException):
    """LS증권 데이터 조회 관련 예외"""
    pass


# === 공통 예외 ===
class InvalidResponseException(BrokerApiException):
    """
    API 응답 형식 오류 예외
    JSON 파싱 실패, 예상치 못한 응답 형식 등의 상황에서 사용됩니다.
    """

    def __init__(self, detail: str, broker: str = None):
        super().__init__(detail, "INVALID_RESPONSE", broker)


class NetworkException(BrokerApiException):
    """
    네트워크 연결 관련 예외
    API 서버 접속 실패, 타임아웃 등의 상황에서 사용됩니다.
    """

    def __init__(self, detail: str, broker: str = None):
        super().__init__(detail, "NETWORK_ERROR", broker)