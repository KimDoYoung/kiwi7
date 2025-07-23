# api1.py
import asyncio
from backend.domains.kiwoom.kiwoom_service import get_kiwoom_api

async def main():
    try:
        # Initialize the API
        print("Initializing Kiwoom API...")
        api = await get_kiwoom_api()
        
        if not api:
            print("Failed to initialize Kiwoom API.")
            return
        
        print("Kiwoom API initialized successfully!")
        print(f"Access Token: {api.ACCESS_TOKEN[:20]}..." if api.ACCESS_TOKEN else "No token")
        print(f"Token Expires: {api.ACCESS_TOKEN_EXPIRED_TIME}")
        
        # 여기에 API 테스트 코드를 추가할 수 있습니다
        # 예: 주식 정보 조회 등
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # Python 3.7+에서는 asyncio.run() 사용
    asyncio.run(main())
    
    # 또는 Python 3.6 이하에서는:
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())