from dotenv import load_dotenv
import os
class Config:
    def __init__(self):
        self.PROFILE_NAME = os.getenv('kiwi7_MODE', 'local')
        load_dotenv(dotenv_path=f'.env.{self.PROFILE_NAME}')
        
        # 디폴트사용자
        self.DEFAULT_USER_ID = os.getenv('DEFAULT_USER_ID', 'kdy987')
        self.DEFAULT_STOCK_ABBR = os.getenv('DEFAULT_STOCK_ABBR','KIS')


        # BASE_DIR 설정
        self.BASE_DIR = os.getenv('BASE_DIR', 'c:\\kiwi7')
        self.DB_PATH = os.getenv('DB_PATH', f'{self.BASE_DIR}/db/kiwi7.db')
        # 로그 설정
        self.LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
        self.LOG_DIR = os.getenv('LOG_DIR', f'{self.BASE_DIR}/logs')
        self.LOG_FILE = self.LOG_DIR + '/kiwi7.log'

        self.SECRET_KEY = os.getenv('SECRET_KEY','kiwi77_secret_key_1234_!@#$')
        self.ALGORITHM = os.getenv('ALGORITHM','HS256')
        self.ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', 30)
        self.ACCESS_TOKEN_NAME = os.getenv('ACCESS_TOKEN_NAME', 'kiwi777_token')
        
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