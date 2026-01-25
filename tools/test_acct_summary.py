"""
3개 증권사 계좌 요약 조회 테스트
Kiwoom, KIS, LS 증권사의 계좌별 자산 정보를 통합 조회

routes에서 제공하는 API 함수와 동일한 구조 사용
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import json
from datetime import date, datetime
from typing import List

from backend.core.config import config
from backend.core.logger import get_logger
from backend.utils.kiwi_utils import format_account_number
from backend.domains.stkcompanys.kis.kis_service import get_kis_api
from backend.domains.stkcompanys.kis.models.kis_response_definition import (
    get_response_definition as get_kis_response_def,
)
from backend.domains.stkcompanys.kis.models.kis_schema import KisApiHelper, KisRequest
from backend.domains.stkcompanys.kiwoom.kiwoom_service import get_kiwoom_api
from backend.domains.stkcompanys.kiwoom.models.kiwoom_schema import KiwoomApiHelper, KiwoomRequest
from backend.domains.stkcompanys.ls.ls_service import get_ls_api
from backend.domains.stkcompanys.ls.models.ls_schema import LsApiHelper, LsRequest

logger = get_logger(__name__)


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    return str(obj)


def extract_holdings_from_kis_response(response_data: dict, api_id: str) -> list:
    """
    KIS API 응답에서 response definition을 활용하여 보유종목 데이터 추출

    Args:
        response_data: API 응답 데이터
        api_id: API ID (예: 'TTTC8434R')

    Returns:
        보유종목 리스트
    """
    resp_def = get_kis_response_def(api_id)
    if not resp_def:
        logger.warning(f'[KIS] Response definition not found for {api_id}')
        return []

    # output1이 보유종목 배열
    if 'output1' in resp_def and isinstance(response_data, dict):
        output1_key = 'output1'
        if output1_key in response_data:
            data = response_data[output1_key]
            if isinstance(data, list):
                return data

    return []


def get_kis_output1_field_definition(api_id: str) -> list:
    """
    KIS API의 output1 필드 정의 조회

    Args:
        api_id: API ID (예: 'TTTC8434R')

    Returns:
        필드 정의 리스트: [{'key': 'pdno', 'name': '상품번호', ...}, ...]
    """
    resp_def = get_kis_response_def(api_id)
    if not resp_def or 'output1' not in resp_def:
        return []

    output1_def = resp_def['output1']
    if isinstance(output1_def, dict) and 'fields' in output1_def:
        return output1_def['fields']

    return []


def summarize_kis_holdings(holdings: list, api_id: str) -> dict:
    """
    KIS 보유종목 정보를 요약

    Args:
        holdings: 보유종목 리스트
        api_id: API ID (예: 'TTTC8434R')

    Returns:
        요약 정보 딕셔너리
    """
    summary = {
        '총보유종목수': len(holdings),
        '평가금액합계': 0,
        '매입금액합계': 0,
        '평가손익합계': 0,
        '상위3종목': [],
    }

    if not holdings:
        return summary

    # 평가금액 기준으로 정렬하여 상위 3개 종목 추출
    sorted_holdings = sorted(
        [h for h in holdings if isinstance(h, dict)],
        key=lambda x: int(str(x.get('평가금액', 0)).replace(',', '') or 0),
        reverse=True,
    )

    for holding in holdings:
        if isinstance(holding, dict):
            try:
                pchs_amt = int(str(holding.get('매입금액', 0)).replace(',', '') or 0)
                evlu_amt = int(str(holding.get('평가금액', 0)).replace(',', '') or 0)
                evlu_pfls_amt = int(str(holding.get('평가손익금액', 0)).replace(',', '') or 0)

                summary['매입금액합계'] += pchs_amt
                summary['평가금액합계'] += evlu_amt
                summary['평가손익합계'] += evlu_pfls_amt
            except (ValueError, TypeError):
                pass

    # 상위 3개 종목 정보 추출
    for holding in sorted_holdings[:3]:
        if isinstance(holding, dict):
            summary['상위3종목'].append({
                '종목명': holding.get('상품명', '미분류'),
                '보유수량': holding.get('보유수량', 0),
                '매입평균가': holding.get('매입평균가격', 0),
                '현재가': holding.get('현재가', 0),
                '평가금액': holding.get('평가금액', 0),
                '평가손익': holding.get('평가손익금액', 0),
            })

    return summary


class AccountSummary:
    """계좌 요약 정보"""

    def __init__(self, broker: str, name: str):
        self.broker = broker  # 증권사약어
        self.data = {}
        self.data['증권사명'] = name
        self.data['계좌번호'] = ''
        self.data['총자산'] = 0
        self.data['매입금액'] = 0
        self.data['평가손익'] = 0
        self.data['수익률'] = 0.0
        self.data['주문가능금액'] = 0
        self.data['보유종목수'] = 0

    def _calculate_pl_and_rate(self):
        """평가손익과 수익률 자동 계산"""
        total_assets = self.data['총자산']
        purchase_amount = self.data['매입금액']

        # 평가손익 = 총자산 - 매입금액
        self.data['평가손익'] = total_assets - purchase_amount

        # 수익률 = (평가손익 / 매입금액) × 100
        if purchase_amount != 0:
            self.data['수익률'] = (self.data['평가손익'] / purchase_amount) * 100
        else:
            self.data['수익률'] = 0.0

    def __repr__(self) -> str:
        return (
            f'AccountSummary(broker={self.broker}, '
            f'name={self.data["증권사명"]}, '
            f'balance={self.data["총자산"]}, pl={self.data["평가손익"]}, '
            f'holdings={self.data["보유종목수"]})'
        )

    def to_dict(self) -> dict:
        """
        JSON 직렬화 가능한 딕셔너리로 변환
        """
        return {
            'id': self.broker.lower(),
            '증권사': self.broker,
            **self.data,
            '수익률': f'{self.data["수익률"]:+.2f}%',
        }

    def to_json(self) -> str:
        """JSON 문자열로 변환"""
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def __getitem__(self, key: str):
        """딕셔너리 스타일 접근 지원"""
        return self.to_dict().get(key)


async def get_kiwoom_account_summary() -> AccountSummary | None:
    """키움 계좌 요약 조회 (routes 구조와 동일)"""
    try:
        # routes/kiwoom_routes.py의 kiwoom_rest_api 함수와 동일 구조
        kiwoom = await get_kiwoom_api()
        if not kiwoom:
            logger.error('Kiwoom API 인스턴스 생성 실패')
            return None

        # kt00004: 계좌평가현황요청
        api_id = 'kt00004'
        payload = {
            'qry_tp': '0',  # 상장폐지조회구분: 0=전체
            'dmst_stex_tp': 'KRX',  # 국내거래소구분: KRX
        }

        request = KiwoomRequest(api_id=api_id, payload=payload)

        # payload 유효성 검증
        validation_errors = request.validate_payload()
        if validation_errors:
            logger.error(f'요청 검증 실패: {", ".join(validation_errors)}')
            return None

        logger.info(f'[Kiwoom] API 요청: api_id={api_id}')
        response = await kiwoom.send_request(request)

        # 성공 시 한글 필드명으로 변환 (routes와 동일)
        if response.success and response.data:
            korea_data = KiwoomApiHelper.to_korea_data(response.data, api_id)
            response.data = korea_data

        logger.info('Kiwoom 응답 수신')

        # 응답에서 데이터 추출 (to_korea_data 적용 후 한글 필드명 사용)
        account_summary = AccountSummary('Kiwoom', '키움증권')
        account_summary.data['계좌번호'] = format_account_number('KIWOOM', config.KIWOOM_ACCT_NO)

        if response.success and response.data:
            data = response.data
            if isinstance(data, dict):
                # 예탁자산평가액 = 총자산 (예수금 + 유가잔고)
                #account_summary.data['총자산'] = int(data.get('예탁자산평가액', 0) or 0)
                account_summary.data['총자산'] = int(data.get('유가잔고평가액', 0) or 0)
                
                # 매입금액 계산
                orderable = int(data.get('예수금', 0) or 0)
                account_summary.data['주문가능금액'] = orderable
                account_summary.data['매입금액'] = int(data.get('총매입금액', 0) or 0)
                # 계좌명
                # account_summary.data['증권사명'] = data.get('계좌명', '키움증권')
                # 종목별계좌평가현황 리스트의 길이 = 보유종목 개수
                holdings_list = data.get('종목별계좌평가현황', [])
                if isinstance(holdings_list, list):
                    account_summary.data['보유종목수'] = len(holdings_list)
                # 평가손익과 수익률 자동 계산
                account_summary._calculate_pl_and_rate()

        if hasattr(response, 'model_dump'):
            account_summary.raw_data = response.model_dump()
        else:
            account_summary.raw_data = vars(response)
        logger.info("---------------------------------")
        logger.info(f'Kiwoom 응답 데이터: {json.dumps(account_summary.raw_data, ensure_ascii=False, indent=2, default=json_serial)}')
        logger.info("---------------------------------")
        logger.info(f'Kiwoom 계좌 요약: {account_summary}')
        return account_summary

    except Exception as e:
        logger.error(f'[Kiwoom] 조회 실패: {e}')
        return None


async def get_kis_account_summary() -> AccountSummary | None:
    """
    KIS(한국투자증권) 계좌 요약 정보를 조회하는 비동기 함수입니다.
    이 함수는 한국투자증권 API를 통해 계좌의 자산 현황과 보유 종목 정보를 조회하여
    표준화된 AccountSummary 객체로 반환합니다.
    주요 기능:
    - CTRP6548R API를 사용한 투자계좌자산현황조회
    - TTTC8434R API를 사용한 보유종목 개수 조회
    - 한글 필드명으로 데이터 변환
    - 평가손익 및 수익률 자동 계산
    조회되는 정보:
    - 계좌번호: 설정에서 가져온 KIS 계좌번호
    - 총자산: 평가금액합계
    - 매입금액: 매입금액합계
    - 주문가능금액: 총예수금액
    - 보유종목수: 현재 보유 중인 종목 개수
    - 평가손익: 자동 계산 (총자산 - 매입금액)
    - 수익률: 자동 계산 (평가손익 / 매입금액 * 100)
    Returns:
        AccountSummary | None: 
            성공 시 계좌 요약 정보가 담긴 AccountSummary 객체
            실패 시 None 반환
    Raises:
        Exception: API 호출 실패, 네트워크 오류, 인증 실패 등의 경우
    Note:
        - KIS API 인스턴스가 정상적으로 생성되어야 함
        - config.KIS_ACCT_NO가 10자리 계좌번호 형식이어야 함 (8자리 CANO + 2자리 ACNT_PRDT_CD)
        - 보유종목 조회 실패 시에도 기본 계좌 정보는 반환됨
    """
    """KIS(한투) 계좌 요약 조회 (routes 구조와 동일)"""
    try:
        # routes/kis_routes.py의 kis_rest_api 함수와 동일 구조
        kis = await get_kis_api()
        if not kis:
            logger.error('KIS API 인스턴스 생성 실패')
            return None

        # CTRP6548R: 투자계좌자산현황조회
        api_id = 'CTRP6548R'

        # 계좌번호 파싱 (10자리 기준)
        acct_no_full = config.KIS_ACCT_NO
        # 계좌번호: 앞 8자리(CANO) + 뒤 2자리(ACNT_PRDT_CD)
        cano = acct_no_full[:8]
        acnt_prdt_cd = acct_no_full[8:10]

        payload = {
            'CANO': cano,
            'ACNT_PRDT_CD': acnt_prdt_cd,
            'INQR_DVSN_1': ' ',
            'BSPR_BF_DT_APLY_YN': ' ',
        }

        request = KisRequest(api_id=api_id, payload=payload)

        # payload 유효성 검증
        validation_errors = request.validate_payload()
        if validation_errors:
            logger.error(f'요청 검증 실패: {", ".join(validation_errors)}')
            return None

        logger.info(f'[KIS] API 요청: api_id={api_id}')
        response = await kis.send_request(request)

        # 성공 시 한글 필드명으로 변환 (routes와 동일)
        if response.success and response.data:
            korea_data = KisApiHelper.to_korea_data(response.data, api_id)
            response.data = korea_data

        logger.info('KIS 응답 수신')
        # 디버그: response.data 출력
        logger.info("--- KIS Account Summary Response Data ---")
        if response.data:
            logger.info(f'[KIS] Response data: {json.dumps(response.data, ensure_ascii=False, indent=2, default=json_serial)}')
        else:
            logger.info('[KIS] Response data: None')
        logger.info("----------------------------------------")
        # 응답에서 데이터 추출 (to_korea_data 적용 후 한글 필드명 사용)
        account_summary = AccountSummary('KIS', '한국투자증권')
        account_summary.data['계좌번호'] = config.KIS_ACCT_NO

        if response.success and response.data:
            data = response.data
            if isinstance(data, dict):
                # output2에 계좌 요약 정보가 있음
                output2 = data.get('output2', {})
                if isinstance(output2, dict):
                    # 총자산금액
                    account_summary.data['총자산'] = int(output2.get('평가금액합계', 0) or 0)
                    # 평가손익금액합계 = 당일 손익 (매입금액으로 사용)
                    account_summary.data['매입금액'] = int(output2.get('매입금액합계', 0) or 0)
                    # 총예수금액 = 주문가능금액
                    account_summary.data['주문가능금액'] = int(output2.get('총예수금액', 0) or 0)
                    # 평가손익과 수익률 자동 계산
                    account_summary._calculate_pl_and_rate()

        # 보유 종목 개수 조회 (TTTC8434R)
        try:
            api_id_balance = 'TTTC8434R'
            payload_balance = {
                'CANO': cano,
                'ACNT_PRDT_CD': acnt_prdt_cd,
                'AFHR_FLPR_YN': 'N',
                'OFL_YN': '',
                'INQR_DVSN': '02',
                'UNPR_DVSN': '01',
                'FUND_STTL_ICLD_YN': 'N',
                'FNCG_AMT_AUTO_RDPT_YN': 'N',
                'PRCS_DVSN': '00',
                'CTX_AREA_FK100': '',
                'CTX_AREA_NK100': '',
            }
            request_balance = KisRequest(api_id=api_id_balance, payload=payload_balance)
            response_balance = await kis.send_request(request_balance)

            # 보유 종목 개수 파악 (response definition 활용)
            if response_balance.success and response_balance.data:
                account_summary.data['보유종목수'] = len(response_balance.data.get('output1', []))

        except Exception as e:
            logger.warning(f'[KIS] 보유 종목 조회 실패: {e}')

        if hasattr(response, 'model_dump'):
            account_summary.raw_data = response.model_dump()
        else:
            account_summary.raw_data = vars(response)

        logger.info(f'KIS 계좌 요약: {account_summary}')
        return account_summary

    except Exception as e:
        logger.error(f'[KIS] 조회 실패: {e}')
        return None


async def get_ls_account_summary() -> AccountSummary | None:
    """LS 증권 계좌 요약 조회 (routes 구조와 동일)"""
    try:
        # routes/ls_routes.py의 ls_rest_api 함수와 동일 구조
        ls = await get_ls_api()
        if not ls:
            logger.error('LS API 인스턴스 생성 실패')
            return None

        # t0424: 주식잔고2
        api_id = 't0424'
        payload = {
            'prcgb': '0',  # 단가구분: 0=기준가
            'chegb': '0',  # 체결구분: 0=전체
            'dangb': '0',  # 단일가구분: 0=전체
            'charge': '0',  # 제비용포함여부: 0=미포함
        }

        request = LsRequest(api_id=api_id, payload=payload)

        # payload 유효성 검증
        validation_errors = request.validate_payload()
        if validation_errors:
            logger.error(f'요청 검증 실패: {", ".join(validation_errors)}')
            return None

        logger.info(f'[LS] API 요청: api_id={api_id}')
        response = await ls.send_request(request)

        # 응답 상태 확인
        if not response.success:
            logger.warning(
                f'[LS] API 조회 실패: error_code={response.error_code}, message={response.error_message}'
            )
            # 실패한 경우에도 기본 계좌 정보로 반환
            account_summary = AccountSummary('LS', 'LS증권')
            account_summary.data['계좌번호'] = config.LS_ACCT_NO
            if hasattr(response, 'model_dump'):
                account_summary.raw_data = response.model_dump()
            else:
                account_summary.raw_data = vars(response)
            logger.info("---------------------------------")
            logger.info(f'LS 응답 데이터: {json.dumps(account_summary.raw_data, ensure_ascii=False, indent=2, default=json_serial)}')
            logger.info("---------------------------------")
            logger.info(f'LS 계좌 요약: {account_summary}')
            return account_summary

        # 성공 시 한글 필드명으로 변환 (routes와 동일)
        if response.success and response.data:
            korea_data = LsApiHelper.to_korea_data(response.data, api_id)
            response.data = korea_data

        logger.info('LS 응답 수신')

        # 응답에서 데이터 추출
        account_summary = AccountSummary('LS', 'LS증권')
        account_summary.data['계좌번호'] = config.LS_ACCT_NO

        # t0424OutBlock에서 계좌 요약 정보 추출
        if response.success and response.data:
            data = response.data
            logger.info("---------------------------------")
            logger.info(f'LS 응답 데이터: {json.dumps(data, ensure_ascii=False, indent=2, default=json_serial)}')
            logger.info("---------------------------------")

            if isinstance(data, dict):
                block = data.get('t0424OutBlock', {})
                if isinstance(block, dict):
                    # 추정순자산 = 총자산
                    account_summary.data['총자산'] = int(block.get('추정순자산', 0) or 0)
                    # 평가손익 = 매입금액 (이미 평가손익임)
                    account_summary.data['매입금액'] = int(block.get('평가손익', 0) or 0)
                    # 추정D2예수금 = 주문가능금액
                    account_summary.data['주문가능금액'] = int(block.get('추정D2예수금', 0) or 0)

        # 보유 종목 개수 계산 (t0424OutBlock1 배열)
        if response.success and response.data:
            data = response.data
            if isinstance(data, dict):
                block1 = data.get('t0424OutBlock1', [])
                if isinstance(block1, list):
                    account_summary.data['보유종목수'] = len(block1)
                # 평가손익과 수익률 자동 계산
                account_summary._calculate_pl_and_rate()

        if hasattr(response, 'model_dump'):
            account_summary.raw_data = response.model_dump()
        else:
            account_summary.raw_data = vars(response)

        logger.info(f'LS 계좌 요약: {account_summary}')
        return account_summary

    except Exception as e:
        logger.error(f'[LS] 조회 실패: {e}')
        return None


def get_summary_json(accounts: List[AccountSummary]) -> dict:
    """
    모든 계좌 정보를 통합 JSON 형식으로 반환

    Args:
        accounts: AccountSummary 리스트

    Returns:
        {'summary': {...}, 'accounts': {...}} 형식의 딕셔너리
    """
    valid_accounts = [acc for acc in accounts if acc is not None]

    # 계좌별 정보 생성
    accounts_data = {}
    for account in valid_accounts:
        broker_key = account.broker.lower()
        accounts_data[broker_key] = account.to_dict()

    # 전체 요약 정보 계산
    total_balance = sum(acc.data['총자산'] for acc in valid_accounts)
    total_purchase_amount = sum(acc.data['매입금액'] for acc in valid_accounts)
    total_pl = total_balance - total_purchase_amount
    total_return_rate = (
        (total_pl / total_purchase_amount * 100) if total_purchase_amount != 0 else 0
    )

    summary = {
        '전체자산': total_balance,
        '전체매입금액': total_purchase_amount,
        '전체평가손익': total_pl,
        '전체수익률': f'{total_return_rate:+.2f}%',
        '계좌개수': len(valid_accounts),
    }

    return {'summary': summary, 'accounts': accounts_data}


async def main():
    """메인 함수"""
    # 각 증권사별 계좌 조회
    accounts = []

    kiwoom_account = await get_kiwoom_account_summary()
    if kiwoom_account:
        accounts.append(kiwoom_account)

    kis_account = await get_kis_account_summary()
    if kis_account:
        accounts.append(kis_account)

    ls_account = await get_ls_account_summary()
    if ls_account:
        accounts.append(ls_account)

    # 결과 출력
    if accounts:
        summary_json = get_summary_json(accounts)
        print(json.dumps(summary_json, ensure_ascii=False, indent=2))
    else:
        logger.error('조회된 계좌가 없습니다.')


if __name__ == '__main__':
    asyncio.run(main())
