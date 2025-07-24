# api1.py
import asyncio
from backend.domains.kiwoom.kiwoom_service import get_kiwoom_api
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomRequest

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

         
        request_data = KiwoomRequest(
            api_id='ka10001',
            payload={'stk_cd': '005930'}
        )        
        response = await api.send_request(request_data)
        print("API Response:", response)
        
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