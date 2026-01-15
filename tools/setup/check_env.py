#!/usr/bin/env python3
"""
환경 설정 검증 도구

사용법:
    python -m tools.setup.check_env
    python -m tools.setup.check_env --env local
"""
import os
import sys
import argparse
from pathlib import Path

# 프로젝트 루트를 path에 추가
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from backend.core.config import config


def check_environment():
    """환경 설정 검증"""
    print("="*60)
    print("🔍 Kiwi7 환경 설정 검증")
    print("="*60)
    print()
    
    # 기본 설정
    print("📌 기본 설정")
    print(f"   프로파일: {config.PROFILE_NAME}")
    print(f"   버전: {config.VERSION}")
    print(f"   타임존: {config.TIME_ZONE}")
    print(f"   BASE_DIR: {config.BASE_DIR}")
    print(f"   DB 경로: {config.DB_PATH}")
    print()
    
    # 디렉토리 확인
    print("📁 디렉토리 확인")
    base_dir = Path(config.BASE_DIR)
    dirs_to_check = ['db', 'logs']
    
    for dir_name in dirs_to_check:
        dir_path = base_dir / dir_name
        if dir_path.exists():
            print(f"   ✅ {dir_name}: {dir_path}")
        else:
            print(f"   ❌ {dir_name}: {dir_path} (없음)")
    print()
    
    # 키움증권
    print("🔑 키움증권 설정")
    check_broker_config('KIWOOM', {
        'APP_KEY': config.KIWOOM_APP_KEY,
        'SECRET_KEY': config.KIWOOM_SECRET_KEY,
        'ACCT_NO': config.KIWOOM_ACCT_NO,
        'BASE_URL': config.KIWOOM_BASE_URL,
    })
    print()
    
    # 한국투자증권
    print("🔑 한국투자증권 설정")
    check_broker_config('KIS', {
        'APP_KEY': config.KIS_APP_KEY,
        'SECRET_KEY': config.KIS_SECRET_KEY,
        'ACCT_NO': config.KIS_ACCT_NO,
        'IS_VIRTUAL': config.KIS_IS_VIRTUAL,
        'BASE_URL': config.KIS_BASE_URL,
    })
    print()
    
    # LS증권
    print("🔑 LS증권 설정")
    check_broker_config('LS', {
        'APP_KEY': config.LS_APP_KEY,
        'SECRET_KEY': config.LS_SECRET_KEY,
        'ACCT_NO': config.LS_ACCT_NO,
        'IS_VIRTUAL': config.LS_IS_VIRTUAL,
        'BASE_URL': config.LS_BASE_URL,
    })
    print()
    
    # 공공데이터
    print("🔑 공공데이터 API")
    if config.GODATA_API_KEY:
        print(f"   ✅ API 키: {config.GODATA_API_KEY[:10]}...")
    else:
        print(f"   ⚠️  API 키가 설정되지 않았습니다")
    print()


def check_broker_config(broker_name: str, configs: dict):
    """증권사 설정 확인"""
    for key, value in configs.items():
        if value:
            if 'KEY' in key or 'SECRET' in key:
                # 민감 정보는 일부만 표시
                display_value = f"{str(value)[:10]}..." if len(str(value)) > 10 else "***"
            else:
                display_value = value
            print(f"   ✅ {key}: {display_value}")
        else:
            print(f"   ❌ {key}: (설정 안됨)")


def main():
    parser = argparse.ArgumentParser(description='환경 설정 검증 도구')
    parser.add_argument('--env', help='환경 이름 (local, docker 등)')
    
    args = parser.parse_args()
    
    if args.env:
        os.environ['KIWI7_MODE'] = args.env
    
    check_environment()


if __name__ == '__main__':
    main()
