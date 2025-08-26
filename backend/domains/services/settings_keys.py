# settings_keys.py
"""
모듈 설명: 
    - settings테이블의 key값을 Enum으로 정의
주요 기능:
    - 설정 값을 쉽게 관리하고 접근할 수 있도록 Enum 형태로 제공
    - usage:
        SettingsKey.USER_ID
작성자: 김도영
작성일: 2025-08-24
버전: 1.0
"""
from enum import Enum

class SettingsKey(str, Enum):
    # 사용자 관련
    USER_ID = "user_id"
    USER_PW = "user_pw"
    LAST_STK_INFO_FILL = "마지막으로 stk_info를 채운 시각"
