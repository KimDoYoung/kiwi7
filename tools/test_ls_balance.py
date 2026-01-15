"""
LS증권 주식 잔고 조회 테스트
"""
import sys
from pathlib import Path

# 프로젝트 루트를 Python path에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import asyncio
from pprint import pprint
from backend.domains.ls.ls_rest_api import LsRestApi
from backend.domains.ls.managers.ls_token_manager import LsTokenManager
from backend.domains.ls.models.ls_schema import LsRequest, LsApiHelper
from backend.core.config import config

async def test_balance():
    """주식 잔고 조회 테스트"""
    
    # LS 토큰 매니저 및 API 클라이언트 생성
    token_manager = LsTokenManager()
    api = LsRestApi(token_manager=token_manager)
    
    print(f"=== LS증권 주식 잔고 조회 테스트 ===")
    print(f"계좌번호: {config.LS_ACCT_NO}")
    print(f"Base URL: {config.LS_BASE_URL}")
    print()
    
    # 요청 파라미터
    # t0424: 주식잔고조회
    payload = {
        'pession': '0',  # 단가구분 (0:평균단가, 1:BEP단가)
        'cts_expcode': '',  # 연속조회종목코드 (최초 조회시 공백)
    }
    
    # API 요청
    request = LsRequest(api_id='t0424', payload=payload)
    
    try:
        print("🚀 API 호출 시작...")
        response = await api.send_request(request)
        
        print("\n✅ API 호출 성공!")
        
        # LsResponse 객체를 dict로 변환
        if hasattr(response, 'model_dump'):
            response_dict = response.model_dump()
        elif hasattr(response, 'dict'):
            response_dict = response.dict()
        else:
            response_dict = response
        
        # data 부분만 한글로 변환
        print("\n=== 응답 결과 (한글) ===")
        if response_dict.get('data'):
            korean_data = LsApiHelper.to_korea_data(response_dict['data'], 't0424')
            response_dict['data'] = korean_data
        
        pprint(response_dict)
        print("-----------------------------------------")
        pprint(korean_data)
        print("-----------------------------------------")
        
        # 잔고 정보 출력
        data = response_dict.get('data', {})
        
        # LS API는 output1/output2 대신 t0424OutBlock1 형식 사용
        stocks = data.get('t0424OutBlock1', [])
        
        if stocks and isinstance(stocks, list) and len(stocks) > 0:
            print("\n=== 보유 종목 ===")
            for idx, stock in enumerate(stocks, 1):
                print(f"\n{idx}. {stock.get('종목명', 'N/A')}")
                print(f"   종목코드: {stock.get('종목코드', 'N/A')}")
                print(f"   잔고수량: {stock.get('잔고수량', '0')}")
                print(f"   평균단가: {stock.get('평균단가', '0')}")
                print(f"   현재가: {stock.get('현재가', '0')}")
                print(f"   평가손익: {stock.get('평가손익', '0')}")
                print(f"   수익율: {stock.get('수익율', '0')}%")
                print(f"   매도가능수량: {stock.get('매도가능수량', '0')}")
        else:
            print("\n=== 보유 종목 ===")
            print("보유 종목이 없습니다.")
        
        # 계좌 요약 정보 (t0424OutBlock에 포함)
        summary = data.get('t0424OutBlock', {})
        if summary and isinstance(summary, dict):
            print("\n=== 계좌 요약 ===")
            # LS API 응답 구조에 맞게 출력
            for key, value in summary.items():
                if value:  # 값이 있는 경우만 출력
                    print(f"{key}: {value}")
            
    except Exception as e:
        print(f"\n❌ API 호출 실패: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    asyncio.run(test_balance())
