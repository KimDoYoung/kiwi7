"""
KIS 주식 잔고 조회 테스트
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from pprint import pprint
from backend.domains.kis.kis_rest_api import KisRestApi
from backend.domains.kis.managers.kis_token_manager import KisTokenManager
from backend.domains.kis.models.kis_schema import KisRequest, KisApiHelper
from backend.core.config import config

async def test_balance():
    """주식 잔고 조회 테스트"""
    
    # KIS 토큰 매니저 및 API 클라이언트 생성
    token_manager = KisTokenManager()
    api = KisRestApi(token_manager=token_manager)
    
    # 계좌번호 설정
    # KIS 계좌번호는 보통 "12345678-01" 형식 또는 "1234567801" 형식
    acct_no_full = config.KIS_ACCT_NO
    acct_prdt_cd_config = config.KIS_ACCT_PRDT_CD
    
    print(f"=== KIS 주식 잔고 조회 테스트 ===")
    print(f"원본 계좌번호: {acct_no_full}")
    print(f"계좌상품코드(config): {acct_prdt_cd_config}")
    
    # 계좌번호 파싱
    # KIS 계좌번호는 보통 8자리-2자리 형식 (예: 12345678-01)
    # 하이픈 없이 10자리로 입력될 수도 있음 (예: 1234567801)
    if '-' in acct_no_full:
        # "12345678-01" 형식
        parts = acct_no_full.split('-')
        cano = parts[0]
        acnt_prdt_cd = parts[1] if len(parts) > 1 else acct_prdt_cd_config
    else:
        # 하이픈 없는 형식
        if len(acct_no_full) == 10:
            # 10자리: 앞 8자리가 계좌번호, 뒤 2자리가 상품코드 (표준 형식)
            cano = acct_no_full[:8]
            acnt_prdt_cd = acct_no_full[8:10]
        elif len(acct_no_full) == 11:
            # 11자리: 앞 8자리가 CANO, 뒤 2자리가 ACNT_PRDT_CD
            # (중간 1자리는 체크디지트 또는 기타 용도로 추정)
            # API 문서: CANO는 계좌번호 체계(8-2)의 앞 8자리
            cano = acct_no_full[:8]  # 앞 8자리
            acnt_prdt_cd = acct_no_full[-2:]  # 뒤 2자리
            print(f"⚠️  11자리 계좌번호: 앞 8자리({cano})를 CANO로, 뒤 2자리({acnt_prdt_cd})를 상품코드로 사용")
        elif len(acct_no_full) == 8:
            cano = acct_no_full
            acnt_prdt_cd = acct_prdt_cd_config
        else:
            # 기타 길이
            print(f"⚠️  주의: 예상치 못한 계좌번호 길이 ({len(acct_no_full)})")
            cano = acct_no_full
            acnt_prdt_cd = acct_prdt_cd_config
    
    print(f"파싱된 계좌번호(CANO): {cano} (길이: {len(cano)})")
    print(f"파싱된 계좌상품코드(ACNT_PRDT_CD): {acnt_prdt_cd} (길이: {len(acnt_prdt_cd)})")
    print(f"Base URL: {config.KIS_BASE_URL}")
    print()
    
    # 요청 파라미터
    payload = {
        'CANO': cano,
        'ACNT_PRDT_CD': acnt_prdt_cd,
        'AFHR_FLPR_YN': 'N',  # 시간외단일가여부
        'OFL_YN': '',  # 오프라인여부
        'INQR_DVSN': '02',  # 조회구분 (02:종목별)
        'UNPR_DVSN': '01',  # 단가구분
        'FUND_STTL_ICLD_YN': 'N',  # 펀드결제분포함여부
        'FNCG_AMT_AUTO_RDPT_YN': 'N',  # 융자금액자동상환여부
        'PRCS_DVSN': '00',  # 처리구분 (00:전일매매포함)
        'CTX_AREA_FK100': '',  # 연속조회검색조건100
        'CTX_AREA_NK100': '',  # 연속조회키100
    }
    
    # API 요청
    request = KisRequest(api_id='TTTC8434R', payload=payload)
    
    try:
        print("🚀 API 호출 시작...")
        response = await api.send_request(request)
        
        print("\n✅ API 호출 성공!")
        
        # KisResponse 객체를 dict로 변환
        if hasattr(response, 'model_dump'):
            response_dict = response.model_dump()
        elif hasattr(response, 'dict'):
            response_dict = response.dict()
        else:
            response_dict = response
        
        # data 부분만 한글로 변환
        print("\n=== 응답 결과 (한글) ===")
        if response_dict.get('data'):
            korean_data = KisApiHelper.to_korea_data(response_dict['data'], 'TTTC8434R')
            response_dict['data'] = korean_data
        
        pprint(response_dict)
        
        # 잔고 정보 출력
        data = response_dict.get('data', {})
        if 'output1' in data:
            print("\n=== 보유 종목 ===")
            output1 = data['output1']
            if isinstance(output1, list) and len(output1) > 0:
                for idx, stock in enumerate(output1, 1):
                    print(f"\n{idx}. {stock.get('종목명', 'N/A')}")
                    print(f"   종목코드: {stock.get('종목코드', 'N/A')}")
                    print(f"   보유수량: {stock.get('보유수량', '0')}")
                    print(f"   매입평균가격: {stock.get('매입평균가격', '0')}")
                    print(f"   현재가: {stock.get('현재가', '0')}")
                    print(f"   평가손익금액: {stock.get('평가손익금액', '0')}")
                    print(f"   평가손익율: {stock.get('평가손익율', '0')}%")
            else:
                print("보유 종목이 없습니다.")
        
        if 'output2' in data:
            print("\n=== 계좌 요약 ===")
            output2 = data['output2']
            if isinstance(output2, list) and len(output2) > 0:
                summary = output2[0]
                print(f"예수금총금액: {summary.get('예수금총금액', '0')}원")
                print(f"총평가금액: {summary.get('총평가금액', '0')}원")
                print(f"평가손익합계: {summary.get('평가손익합계', '0')}원")
                print(f"순자산금액: {summary.get('순자산금액', '0')}원")
            else:
                print("계좌 요약 정보가 없습니다.")
            
    except Exception as e:
        print(f"\n❌ API 호출 실패: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    asyncio.run(test_balance())
