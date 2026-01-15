#!/usr/bin/env python3
"""
증권사별 토큰 상태 확인 도구

사용법:
    python -m tools.token.check_token --broker kiwoom
    python -m tools.token.check_token --all
"""
import asyncio
import sys
import argparse
from pathlib import Path

# 프로젝트 루트를 path에 추가
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from backend.domains.kiwoom.managers.kiwoom_token_manager import KiwoomTokenManager
from backend.domains.kis.managers.kis_token_manager import KisTokenManager


async def check_kiwoom_token():
    """키움증권 토큰 확인"""
    print("\n" + "="*50)
    print("🔍 키움증권 토큰 상태")
    print("="*50)
    
    try:
        manager = KiwoomTokenManager()
        await manager._load_token_from_db()
        
        if manager.token:
            print(f"✅ 토큰 있음")
            print(f"   Token: {manager.token[:30]}...")
            print(f"   만료: {manager.expires_dt}")
            
            # 만료 임박 여부
            if manager._is_token_expire_soon():
                print(f"   ⚠️  토큰이 곧 만료됩니다!")
            else:
                print(f"   ✅ 토큰이 유효합니다")
        else:
            print(f"❌ 저장된 토큰이 없습니다")
            
    except Exception as e:
        print(f"❌ 확인 실패: {e}")


async def check_kis_token():
    """한국투자증권 토큰 확인"""
    print("\n" + "="*50)
    print("🔍 한국투자증권 토큰 상태")
    print("="*50)
    
    try:
        manager = KisTokenManager()
        await manager._load_token_from_db()
        
        if manager.token:
            print(f"✅ 토큰 있음")
            print(f"   Token: {manager.token[:30]}...")
            print(f"   만료: {manager.expires_dt}")
            
            # 만료 임박 여부
            if manager._is_token_expire_soon():
                print(f"   ⚠️  토큰이 곧 만료됩니다!")
            else:
                print(f"   ✅ 토큰이 유효합니다")
        else:
            print(f"❌ 저장된 토큰이 없습니다")
            
    except Exception as e:
        print(f"❌ 확인 실패: {e}")


async def check_all_tokens():
    """모든 증권사 토큰 확인"""
    await check_kiwoom_token()
    await check_kis_token()
    print("\n")


async def main():
    parser = argparse.ArgumentParser(description='증권사 토큰 상태 확인 도구')
    parser.add_argument('--broker', choices=['kiwoom', 'kis', 'ls'], help='증권사 선택')
    parser.add_argument('--all', action='store_true', help='모든 증권사 토큰 확인')
    
    args = parser.parse_args()
    
    if args.all:
        await check_all_tokens()
    elif args.broker == 'kiwoom':
        await check_kiwoom_token()
    elif args.broker == 'kis':
        await check_kis_token()
    else:
        parser.print_help()


if __name__ == '__main__':
    asyncio.run(main())
