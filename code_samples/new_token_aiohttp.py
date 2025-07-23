import aiohttp
import asyncio
import json
import os
from dotenv import load_dotenv


# 비동기 함수로 토큰 요청
async def fn_au10001(data):
    host = 'https://api.kiwoom.com'  # 실전투자
    endpoint = '/oauth2/token'
    url = host + endpoint

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            print('Code:', response.status)
            
            # 일부 header 값만 추출
            header_subset = {
                key: response.headers.get(key) 
                for key in ['next-key', 'cont-yn', 'api-id'] 
                if key in response.headers
            }
            print('Header:', json.dumps(header_subset, indent=4, ensure_ascii=False))

            # JSON 본문 출력
            resp_json = await response.json()
            print('Body:', json.dumps(resp_json, indent=4, ensure_ascii=False))


# 실행 부분
if __name__ == '__main__':
    load_dotenv('.env.local')
    APP_KEY = os.getenv('KIWOOM_APP_KEY')
    SECRET_KEY = os.getenv('KIWOOM_SECRET_KEY')

    params = {
        'grant_type': 'client_credentials',
        'appkey': APP_KEY,
        'secretkey': SECRET_KEY,
    }

    asyncio.run(fn_au10001(params))
