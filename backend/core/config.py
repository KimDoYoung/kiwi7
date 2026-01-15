from dotenv import load_dotenv
import os
class Config:
    def __init__(self):
        self.PROFILE_NAME = os.getenv('KIWI7_MODE', 'local')
        load_dotenv(dotenv_path=f'.env.{self.PROFILE_NAME}')
        self.VERSION = os.getenv('VERSION', '0.0.2')
        self.GODATA_API_KEY = os.getenv('GODATA_API_KEY', '')

        # KIWOOM API 관련 키
        self.KIWOOM_ACCT_NO = os.getenv('KIWOOM_ACCT_NO', '1033-4006')
        self.KIWOOM_APP_KEY = os.getenv('KIWOOM_APP_KEY', '')
        self.KIWOOM_SECRET_KEY = os.getenv('KIWOOM_SECRET_KEY', '')
        self.KIWOOM_BASE_URL = os.getenv('KIWOOM_BASE_URL', 'https://api.kiwoom.com')
        self.KIWOOM_WS_URL = os.getenv('KIWOOM_WS_URL', 'wss://api.kiwoom.com:10000/api/dostk/websocket')

        # KIS(한국투자증권) API 관련 키
        self.KIS_ACCT_NO = os.getenv('KIS_ACCT_NO', '')
        self.KIS_ACCT_PRDT_CD = os.getenv('KIS_ACCT_PRDT_CD', '01')  # 계좌상품코드
        self.KIS_APP_KEY = os.getenv('KIS_APP_KEY', '')
        self.KIS_SECRET_KEY = os.getenv('KIS_SECRET_KEY', '')
        self.KIS_IS_VIRTUAL = os.getenv('KIS_IS_VIRTUAL', 'false').lower() == 'true'
        self.KIS_BASE_URL = os.getenv('KIS_BASE_URL',
            'https://openapivts.koreainvestment.com:29443' if self.KIS_IS_VIRTUAL
            else 'https://openapi.koreainvestment.com:9443'
        )
        self.KIS_WS_URL = os.getenv('KIS_WS_URL',
            'ws://ops.koreainvestment.com:31000' if self.KIS_IS_VIRTUAL
            else 'ws://ops.koreainvestment.com:21000'
        )

        # LS증권 API 관련 키
        self.LS_ACCT_NO = os.getenv('LS_ACCT_NO', '')
        self.LS_APP_KEY = os.getenv('LS_APP_KEY', '')
        self.LS_SECRET_KEY = os.getenv('LS_SECRET_KEY', '')
        self.LS_IS_VIRTUAL = os.getenv('LS_IS_VIRTUAL', 'false').lower() == 'true'
        self.LS_BASE_URL = os.getenv('LS_BASE_URL',
            'https://openapi-vts.ls-sec.co.kr:29443' if self.LS_IS_VIRTUAL
            else 'https://openapi.ls-sec.co.kr:8443'
        )
        self.LS_WS_URL = os.getenv('LS_WS_URL',
            'wss://openapi-vts.ls-sec.co.kr:9443/websocket' if self.LS_IS_VIRTUAL
            else 'wss://openapi.ls-sec.co.kr:9443/websocket'
        )
        # TimeZone
        self.TIME_ZONE = "Asia/Seoul"

        # BASE_DIR 설정
        self.BASE_DIR = os.getenv('BASE_DIR', 'c:\\kiwi7')
        self.DB_PATH =  f'{self.BASE_DIR}/db/kiwi7.db'
        # 로그 설정
        self.LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
        self.LOG_DIR = os.getenv('LOG_DIR', f'{self.BASE_DIR}/logs')
        self.LOG_FILE = self.LOG_DIR + '/kiwi7.log'

        self.JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY','kiwi77_secret_key_1234_!@#$')
        self.ALGORITHM = os.getenv('ALGORITHM','HS256')
        self.ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 60)
        self.ACCESS_TOKEN_NAME = os.getenv('ACCESS_TOKEN_NAME', 'kiwi7_token')
        
        self.DATA_FOLDER = self.BASE_DIR + '/data'
        self.FILE_FOLDER = self.BASE_DIR + '/files'

        # 로그 디렉토리 생성
        log_dir = os.path.dirname(self.LOG_FILE)

        # DATA_FOLDER 디렉토리 생성
        if not os.path.exists(self.DATA_FOLDER):
            os.makedirs(self.DATA_FOLDER, exist_ok=True)
        
        if not os.path.exists(self.FILE_FOLDER):
            os.makedirs(self.FILE_FOLDER, exist_ok=True)

        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

config = Config()