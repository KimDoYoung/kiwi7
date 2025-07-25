# api1.py
import asyncio
from backend.domains.kiwoom.kiwoom_service import get_kiwoom_api
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomApiHelper, KiwoomRequest

async def main():
    try:
        # Initialize the API
        print("키움 API 초기화 중...")
        api = await get_kiwoom_api()
        
        if not api:
            return

        print("키움 API 초기화 완료!")
        print(f"Access Token: {api.ACCESS_TOKEN[:20]}..." if api.ACCESS_TOKEN else "No token")
        print(f"Token Expires: {api.ACCESS_TOKEN_EXPIRED_TIME}")

         
        request_data = KiwoomRequest(
            api_id='ka10099',
            payload={'mrkt_tp': '0'}
        )        
        response = await api.send_request(request_data)
        print("-----------------------------------------------------------\n")
        print("Response header :", response.headers)
        print("-----------------------------------------------------------\n")
        if response.success:
            korea_data = KiwoomApiHelper.to_korea_data(response.data, response.api_info['api_id'])
            # print("한글 변환 데이터:", korea_data)    
            list = korea_data.get('종목리스트')
            for item in list:
                for key, value in item.items():
                    print(f"{key}: {value}", end=' | ')
                print()  # 줄바꿈
        print("-----------------------------------------------------------\n")
        
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