   
"""
키움증권 API 관련 예외 클래스들
키움 API 호출 시 발생할 수 있는 다양한 오류 상황을 처리합니다.
"""

class KiwoomApiException(Exception):
    """
    키움증권 API 호출 시 발생하는 기본 예외 클래스
    모든 키움 API 관련 예외의 기본 클래스입니다.
    """
    
    def __init__(self, message: str, error_code: str = None):
        """
        키움 API 예외 초기화
        
        Args:
            message: 오류 메시지
            error_code: 키움 API 오류 코드 (선택사항)
        """
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)
    
    def __str__(self):
        """오류 정보를 문자열로 반환"""
        if self.error_code:
            return f"[{self.error_code}] {self.message}"
        return self.message


class KiwoomAuthException(KiwoomApiException):
    """키움증권 API 인증 관련 예외"""
    pass


class KiwoomOrderException(KiwoomApiException):
    """키움증권 주문 관련 예외"""
    pass


class KiwoomDataException(KiwoomApiException):
    """키움증권 데이터 조회 관련 예외"""
    pass