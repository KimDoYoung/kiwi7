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

from backend.core.config import config
from backend.domains.ls.ls_rest_api import LsRestApi
from backend.domains.ls.managers.ls_token_manager import LsTokenManager
from backend.domains.ls.models.ls_request_definition import (
    get_request_definition,
    get_required_fields,
    get_tr_cd,
)
from backend.domains.ls.models.ls_response_definition import (
    get_field_name,
    get_response_definition,
    get_response_fields,
)
from backend.domains.ls.models.ls_schema import LsApiHelper, LsRequest


async def test_balance():
    """주식 잔고 조회 테스트"""

    # API ID 정의
    api_id = 't0424'

    # API 정의 정보 확인
    request_def = get_request_definition(api_id)
    response_def = get_response_definition(api_id)

    print('=== LS증권 주식 잔고 조회 테스트 ===')
    print(f'API ID: {api_id}')

    if request_def:
        print(f'API 제목: {request_def.get("title", "N/A")}')
        print(f'HTTP 메소드: {request_def.get("method", "POST")}')
        print(f'TR 코드: {get_tr_cd(api_id)}')
        print(f'필수 필드: {get_required_fields(api_id)}')
    else:
        print(f'⚠️  API 정의를 찾을 수 없습니다: {api_id}')

    if response_def:
        response_fields = get_response_fields(api_id)
        print(f'응답 필드 개수: {len(response_fields)}')

    print()
    print(f'계좌번호: {config.LS_ACCT_NO}')
    print(f'Base URL: {config.LS_BASE_URL}')
    print()

    # LS 토큰 매니저 및 API 클라이언트 생성
    token_manager = LsTokenManager()
    api = LsRestApi(token_manager=token_manager)

    # 요청 파라미터
    # t0424: 주식잔고조회
    payload = {
        'pession': '0',  # 단가구분 (0:평균단가, 1:BEP단가)
        'cts_expcode': '',  # 연속조회종목코드 (최초 조회시 공백)
    }

    # API 요청 생성
    request = LsRequest(api_id=api_id, payload=payload)

    # 요청 유효성 검증
    validation_errors = request.validate_payload()
    if validation_errors:
        print('⚠️  요청 검증 오류:')
        for error in validation_errors:
            print(f'   - {error}')
        return

    print('✅ 요청 검증 성공')
    print()

    try:
        print('🚀 API 호출 시작...')
        response = await api.send_request(request)

        print('\n✅ API 호출 성공!')

        # LsResponse 객체를 dict로 변환
        if hasattr(response, 'model_dump'):
            response_dict = response.model_dump()
        elif hasattr(response, 'dict'):
            response_dict = response.dict()
        else:
            response_dict = response

        # data 필드만 한글로 변환
        if 'data' in response_dict and response_dict['data']:
            response_data_korean = LsApiHelper.to_korea_data(response_dict['data'], api_id)
            response_dict_korean = response_dict.copy()
            response_dict_korean['data'] = response_data_korean
        else:
            response_dict_korean = response_dict

        print('\n=== 응답 결과 (한글 변환) ===')
        pprint(response_dict_korean)

        # 필드명 확인 테스트
        print('\n=== 필드명 매핑 테스트 ===')
        test_keys = ['expcode', 'hname', 'janqty', 'pamt', 'price', 'dtsunik']
        for key in test_keys:
            korean_name = get_field_name(api_id, key)
            if korean_name != key:
                print(f'{key} → {korean_name}')

        print('-----------------------------------------')

        # 잔고 정보 출력
        data = response_dict_korean.get('data', {})

        # LS API는 output1/output2 대신 t0424OutBlock1 형식 사용
        stocks = data.get('t0424OutBlock1', [])

        if stocks and isinstance(stocks, list) and len(stocks) > 0:
            print('\n=== 보유 종목 ===')
            for idx, stock in enumerate(stocks, 1):
                print(f'\n{idx}. {stock.get("종목명", "N/A")}')
                print(f'   종목코드: {stock.get("종목코드", "N/A")}')
                print(f'   잔고수량: {stock.get("잔고수량", "0")}')
                print(f'   평균단가: {stock.get("평균단가", "0")}')
                print(f'   현재가: {stock.get("현재가", "0")}')
                print(f'   평가손익: {stock.get("평가손익", "0")}')
                print(f'   수익율: {stock.get("수익율", "0")}%')
                print(f'   매도가능수량: {stock.get("매도가능수량", "0")}')
        else:
            print('\n=== 보유 종목 ===')
            print('보유 종목이 없습니다.')

        # 계좌 요약 정보 (t0424OutBlock에 포함)
        summary = data.get('t0424OutBlock', {})
        if summary and isinstance(summary, dict):
            print('\n=== 계좌 요약 ===')
            # LS API 응답 구조에 맞게 출력
            for key, value in summary.items():
                if value:  # 값이 있는 경우만 출력
                    print(f'{key}: {value}')

    except Exception as e:
        print(f'\n❌ API 호출 실패: {e}')
        import traceback

        traceback.print_exc()


if __name__ == '__main__':
    asyncio.run(test_balance())
