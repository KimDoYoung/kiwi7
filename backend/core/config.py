from dotenv import load_dotenv
import os
class Config:
    def __init__(self):
        self.PROFILE_NAME = os.getenv('KIWI7_MODE', 'local')
        load_dotenv(dotenv_path=f'.env.{self.PROFILE_NAME}')

        self.GODATA_API_KEY = os.getenv('GODATA_API_KEY', '')

        # KIWOOM API 관련 키
        self.KIWOOM_ACCT_NO = os.getenv('KIWOOM_ACCT_NO', '1033-4006')
        self.KIWOOM_APP_KEY = os.getenv('KIWOOM_APP_KEY', '')
        self.KIWOOM_SECRET_KEY = os.getenv('KIWOOM_SECRET_KEY', '')
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
        self.ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 30)
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