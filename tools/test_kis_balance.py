"""
KIS 주식 잔고 조회 테스트
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from pprint import pprint

from backend.core.config import config
from backend.domains.kis.kis_rest_api import KisRestApi
from backend.domains.kis.managers.kis_token_manager import KisTokenManager
from backend.domains.kis.models.kis_request_definition import (
  get_request_definition,
  get_required_fields,
  get_tr_id,
  is_hashkey_required,
)
from backend.domains.kis.models.kis_response_definition import (
  get_field_name,
  get_response_definition,
  get_response_fields,
)
from backend.domains.kis.models.kis_schema import KisApiHelper, KisRequest


async def test_balance():
  """주식 잔고 조회 테스트"""

  # API ID 정의
  api_id = 'TTTC8434R'

  # API 정의 정보 확인
  request_def = get_request_definition(api_id)
  response_def = get_response_definition(api_id)

  print('=== KIS 주식 잔고 조회 테스트 ===')
  print(f'API ID: {api_id}')

  if request_def:
    print(f'API 제목: {request_def.get("title", "N/A")}')
    print(f'HTTP 메소드: {request_def.get("method", "N/A")}')
    print(f'TR ID: {get_tr_id(api_id)}')
    print(f'Hashkey 필요: {is_hashkey_required(api_id)}')
    print(f'필수 필드: {get_required_fields(api_id)}')
  else:
    print(f'⚠️  API 정의를 찾을 수 없습니다: {api_id}')

  if response_def:
    response_fields = get_response_fields(api_id)
    print(f'응답 필드 개수: {len(response_fields)}')

  print()

  # KIS 토큰 매니저 및 API 클라이언트 생성
  token_manager = KisTokenManager()
  api = KisRestApi(token_manager=token_manager)

  # 계좌번호 설정
  # KIS 계좌번호는 보통 "12345678-01" 형식 또는 "1234567801" 형식
  acct_no_full = config.KIS_ACCT_NO
  acct_prdt_cd_config = config.KIS_ACCT_PRDT_CD

  print(f'원본 계좌번호: {acct_no_full}')
  print(f'계좌상품코드(config): {acct_prdt_cd_config}')

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
      print(
        f'⚠️  11자리 계좌번호: 앞 8자리({cano})를 CANO로, 뒤 2자리({acnt_prdt_cd})를 상품코드로 사용'
      )
    elif len(acct_no_full) == 8:
      cano = acct_no_full
      acnt_prdt_cd = acct_prdt_cd_config
    else:
      # 기타 길이
      print(f'⚠️  주의: 예상치 못한 계좌번호 길이 ({len(acct_no_full)})')
      cano = acct_no_full
      acnt_prdt_cd = acct_prdt_cd_config

  print(f'파싱된 계좌번호(CANO): {cano} (길이: {len(cano)})')
  print(f'파싱된 계좌상품코드(ACNT_PRDT_CD): {acnt_prdt_cd} (길이: {len(acnt_prdt_cd)})')
  print(f'Base URL: {config.KIS_BASE_URL}')
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

  # API 요청 생성
  request = KisRequest(api_id=api_id, payload=payload)

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

    # KisResponse 객체를 dict로 변환
    if hasattr(response, 'model_dump'):
      response_dict = response.model_dump()
    elif hasattr(response, 'dict'):
      response_dict = response.dict()
    else:
      response_dict = response

    # data 필드만 한글로 변환
    if 'data' in response_dict and response_dict['data']:
      response_data_korean = KisApiHelper.to_korea_data(response_dict['data'], api_id)
      response_dict_korean = response_dict.copy()
      response_dict_korean['data'] = response_data_korean
    else:
      response_dict_korean = response_dict

    print('\n=== 응답 결과 (한글 변환) ===')
    pprint(response_dict_korean)

    # 필드명 확인 테스트
    print('\n=== 필드명 매핑 테스트 ===')
    test_keys = ['pdno', 'prdt_name', 'hldg_qty', 'pchs_avg_pric', 'evlu_amt']
    for key in test_keys:
      korean_name = get_field_name(api_id, key)
      if korean_name != key:
        print(f'{key} → {korean_name}')

  except Exception as e:
    print(f'\n❌ API 호출 실패: {e}')
    import traceback

    traceback.print_exc()


if __name__ == '__main__':
  asyncio.run(test_balance())
