"""
3개 증권사 계좌 요약 조회 테스트
Kiwoom, KIS, LS 증권사의 계좌별 자산 정보를 통합 조회
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from datetime import datetime
from typing import Any, Dict, List
from pprint import pprint

from backend.core.config import config
from backend.domains.stkcompanys.kiwoom.kiwoom_rest_api import KiwoomRestApi
from backend.domains.stkcompanys.kiwoom.managers.kiwoom_token_manager import (
    KiwoomTokenManager,
)
from backend.domains.stkcompanys.kis.kis_rest_api import KisRestApi
from backend.domains.stkcompanys.kis.managers.kis_token_manager import KisTokenManager
from backend.domains.stkcompanys.ls.ls_rest_api import LsRestApi
from backend.domains.stkcompanys.ls.managers.ls_token_manager import LsTokenManager


class AccountSummary:
    """계좌 요약 정보"""

    def __init__(self, broker: str, name: str):
        self.broker = broker
        self.name = name
        self.balance = 0  # 평가금액
        self.daily_pl = 0  # 당일 손익
        self.orderable_amount = 0  # 주문가능금액
        self.holdings_count = 0  # 보유종목 개수
        self.return_rate = 0.0  # 수익률
        self.raw_data = {}  # 원본 데이터

    def __repr__(self) -> str:
        return (
            f"AccountSummary(broker={self.broker}, name={self.name}, "
            f"balance={self.balance}, daily_pl={self.daily_pl}, "
            f"holdings={self.holdings_count})"
        )


async def get_kiwoom_account_summary() -> AccountSummary | None:
    """키움 계좌 요약 조회"""
    try:
        print("\n[Kiwoom] 계좌 요약 조회 시작...")

        token_manager = KiwoomTokenManager()
        api = KiwoomRestApi(token_manager=token_manager)

        # kt00004: 계좌평가현황요청
        api_id = "kt00004"
        payload = {
            "qry_tp": "0",  # 상장폐지조회구분: 0=전체
            "dmst_stex_tp": "KRX",  # 국내거래소구분: KRX
        }

        from backend.domains.stkcompanys.kiwoom.models.kiwoom_schema import (
            KiwoomRequest,
        )

        request = KiwoomRequest(api_id=api_id, payload=payload)
        response = await api.send_request(request)

        if hasattr(response, "model_dump"):
            response_dict = response.model_dump()
        else:
            response_dict = response if isinstance(response, dict) else vars(response)

        print(f"✅ Kiwoom 응답 수신")

        # 응답에서 데이터 추출
        account_summary = AccountSummary("Kiwoom", "키움증권")
        if "msg" in response_dict:
            msg = response_dict["msg"]
            if isinstance(msg, dict):
                # 메시지에서 필드 추출
                account_summary.balance = int(msg.get("tot_evlt_amt", 0) or 0)
                account_summary.daily_pl = int(msg.get("tot_evltv_prft", 0) or 0)
                account_summary.orderable_amount = int(msg.get("ord_alow_amt", 0) or 0)
        elif "data" in response_dict:
            data = response_dict["data"]
            if isinstance(data, dict):
                account_summary.balance = int(data.get("tot_evlt_amt", 0) or 0)
                account_summary.daily_pl = int(data.get("tot_evltv_prft", 0) or 0)
                account_summary.orderable_amount = int(data.get("ord_alow_amt", 0) or 0)

        account_summary.raw_data = response_dict
        print(f"✅ Kiwoom 계좌 요약: {account_summary}")
        return account_summary

    except Exception as e:
        print(f"❌ Kiwoom 조회 실패: {e}")
        import traceback

        traceback.print_exc()
        return None


async def get_kis_account_summary() -> AccountSummary | None:
    """KIS(한투) 계좌 요약 조회"""
    try:
        print("\n[KIS] 계좌 요약 조회 시작...")

        token_manager = KisTokenManager()
        api = KisRestApi(token_manager=token_manager)

        # CTRP6548R: 투자계좌자산현황조회
        api_id = "CTRP6548R"

        # 계좌번호 파싱
        acct_no_full = config.KIS_ACCT_NO
        if "-" in acct_no_full:
            parts = acct_no_full.split("-")
            cano = parts[0]
            acnt_prdt_cd = parts[1] if len(parts) > 1 else config.KIS_ACCT_PRDT_CD
        else:
            if len(acct_no_full) == 10:
                cano = acct_no_full[:8]
                acnt_prdt_cd = acct_no_full[8:10]
            elif len(acct_no_full) == 11:
                cano = acct_no_full[:8]
                acnt_prdt_cd = acct_no_full[-2:]
            else:
                cano = acct_no_full[:8] if len(acct_no_full) >= 8 else acct_no_full
                acnt_prdt_cd = config.KIS_ACCT_PRDT_CD

        payload = {
            "CANO": cano,
            "ACNT_PRDT_CD": acnt_prdt_cd,
            "INQR_DVSN_1": " ",
            "BSPR_BF_DT_APLY_YN": " ",
        }

        from backend.domains.stkcompanys.kis.models.kis_schema import KisRequest

        request = KisRequest(api_id=api_id, payload=payload)
        response = await api.send_request(request)

        if hasattr(response, "model_dump"):
            response_dict = response.model_dump()
        else:
            response_dict = response if isinstance(response, dict) else vars(response)

        print(f"✅ KIS 응답 수신")

        # 응답에서 데이터 추출
        account_summary = AccountSummary("KIS", "한국투자증권")

        # 한글 변환
        from backend.domains.stkcompanys.kis.models.kis_schema import KisApiHelper

        if "data" in response_dict and response_dict["data"]:
            response_data_korean = KisApiHelper.to_korea_data(
                response_dict["data"], api_id
            )
        else:
            response_data_korean = response_dict.get("data", {})

        if isinstance(response_data_korean, dict):
            account_summary.balance = int(
                response_data_korean.get("총자산금액", 0) or 0
            )
            account_summary.daily_pl = int(
                response_data_korean.get("총평가손익금액", 0) or 0
            )
            account_summary.orderable_amount = int(
                response_data_korean.get("주문가능금액", 0) or 0
            )

        # 보유 종목 개수 조회 (TTTC8434R)
        try:
            api_id_balance = "TTTC8434R"
            payload_balance = {
                "CANO": cano,
                "ACNT_PRDT_CD": acnt_prdt_cd,
                "AFHR_FLPR_YN": "N",
                "OFL_YN": "",
                "INQR_DVSN": "02",
                "UNPR_DVSN": "01",
                "FUND_STTL_ICLD_YN": "N",
                "FNCG_AMT_AUTO_RDPT_YN": "N",
                "PRCS_DVSN": "00",
                "CTX_AREA_FK100": "",
                "CTX_AREA_NK100": "",
            }
            request_balance = KisRequest(api_id=api_id_balance, payload=payload_balance)
            response_balance = await api.send_request(request_balance)

            if hasattr(response_balance, "model_dump"):
                response_balance_dict = response_balance.model_dump()
            else:
                response_balance_dict = (
                    response_balance
                    if isinstance(response_balance, dict)
                    else vars(response_balance)
                )

            # 보유 종목 개수 파악
            if "data" in response_balance_dict and isinstance(
                response_balance_dict["data"], list
            ):
                account_summary.holdings_count = len(response_balance_dict["data"])

        except Exception as e:
            print(f"⚠️  KIS 보유 종목 조회 실패: {e}")

        account_summary.raw_data = response_dict
        print(f"✅ KIS 계좌 요약: {account_summary}")
        return account_summary

    except Exception as e:
        print(f"❌ KIS 조회 실패: {e}")
        import traceback

        traceback.print_exc()
        return None


async def get_ls_account_summary() -> AccountSummary | None:
    """LS 증권 계좌 요약 조회"""
    try:
        print("\n[LS] 계좌 요약 조회 시작...")

        token_manager = LsTokenManager()
        api = LsRestApi(token_manager=token_manager)

        # CSPAQ12200: 현물계좌예수금 주문가능금액 총평가 조회
        api_id = "CSPAQ12200"
        payload = {
            "BalCreTp": "0",  # 잔고생성구분: 0=전체
        }

        from backend.domains.stkcompanys.ls.models.ls_schema import LsRequest, LsApiHelper

        request = LsRequest(api_id=api_id, payload=payload)
        response = await api.send_request(request)

        if hasattr(response, "model_dump"):
            response_dict = response.model_dump()
        else:
            response_dict = response if isinstance(response, dict) else vars(response)

        print(f"✅ LS 응답 수신")

        # 응답에서 데이터 추출
        account_summary = AccountSummary("LS", "LS증권")

        # 한글로 변환
        if "data" in response_dict and response_dict["data"]:
            response_data_korean = LsApiHelper.to_korea_data(
                response_dict["data"], api_id
            )
        else:
            response_data_korean = response_dict.get("data", {})

        # CSPAQ12200OutBlock2에서 계좌 요약 정보 추출
        if isinstance(response_data_korean, dict):
            block2 = response_data_korean.get("CSPAQ12200OutBlock2", {})
            if isinstance(block2, dict):
                # 잔고평가금액 (총 자산)
                account_summary.balance = int(block2.get("잔고평가금액", 0) or 0)
                # 투자손익금액 (당일 손익)
                account_summary.daily_pl = int(block2.get("투자손익금액", 0) or 0)
                # 현금주문가능금액 (주문가능금액)
                account_summary.orderable_amount = int(
                    block2.get("현금주문가능금액", 0) or 0
                )

        # 보유 종목 개수 계산
        account_summary.holdings_count = 0

        account_summary.raw_data = response_dict
        print(f"✅ LS 계좌 요약: {account_summary}")
        return account_summary

    except Exception as e:
        print(f"❌ LS 조회 실패: {e}")
        import traceback

        traceback.print_exc()
        return None


def format_currency(amount: int) -> str:
    """통화 포맷팅"""
    return f"₩{amount:,.0f}"


def format_return_rate(balance: int, daily_pl: int) -> str:
    """수익률 포맷팅"""
    if balance == 0:
        return "0.00%"
    rate = (daily_pl / balance) * 100
    return f"{rate:+.2f}%"


def display_account_summary(accounts: List[AccountSummary]) -> None:
    """계좌 요약 정보 표시"""
    print("\n" + "=" * 100)
    print("3개 증권사 계좌 요약 정보".center(100))
    print("=" * 100)

    total_balance = 0
    total_daily_pl = 0
    total_holdings = 0

    for account in accounts:
        if account is None:
            continue

        account.return_rate = (
            (account.daily_pl / account.balance * 100)
            if account.balance != 0
            else 0
        )

        total_balance += account.balance
        total_daily_pl += account.daily_pl
        total_holdings += account.holdings_count

        print(f"\n📊 {account.name} ({account.broker})")
        print(f"   총 자산: {format_currency(account.balance)}")
        print(f"   당일 손익: {format_currency(account.daily_pl)}")
        print(f"   주문가능금액: {format_currency(account.orderable_amount)}")
        print(f"   보유종목: {account.holdings_count}개")
        print(f"   수익률: {format_return_rate(account.balance, account.daily_pl)}")

    print("\n" + "-" * 100)
    print(f"🎯 전체 합계")
    print(f"   총 자산: {format_currency(total_balance)}")
    print(f"   당일 손익: {format_currency(total_daily_pl)}")
    print(f"   보유종목: {total_holdings}개")
    print(f"   전체 수익률: {format_return_rate(total_balance, total_daily_pl)}")
    print("=" * 100)


def display_json_format(accounts: List[AccountSummary]) -> None:
    """JSON 형식 데이터 표시 (Alpine.js 호환)"""
    print("\n" + "=" * 100)
    print("JSON 형식 데이터 (Alpine.js용)".center(100))
    print("=" * 100)

    data = {}
    for account in accounts:
        if account is None:
            continue

        account.return_rate = (
            (account.daily_pl / account.balance * 100)
            if account.balance != 0
            else 0
        )

        broker_key = account.broker.lower()
        data[broker_key] = {
            "id": broker_key,
            "name": account.name,
            "balance": account.balance,
            "dailyPL": account.daily_pl,
            "orderableAmount": account.orderable_amount,
            "holdingsCount": account.holdings_count,
            "returnRate": f"{account.return_rate:+.2f}%",
            "holdings": [],  # 상세 종목 정보는 별도 조회 필요
        }

    print("\nAccounts Object:")
    pprint(data)

    # 요약 정보
    total_balance = sum(
        acc.balance for acc in accounts if acc is not None
    )
    total_daily_pl = sum(
        acc.daily_pl for acc in accounts if acc is not None
    )

    print("\nSummary:")
    summary = {
        "totalAssets": total_balance,
        "totalDailyPL": total_daily_pl,
        "totalReturnRate": f"{(total_daily_pl / total_balance * 100):+.2f}%" if total_balance != 0 else "0.00%",
        "accountCount": len([acc for acc in accounts if acc is not None]),
    }
    pprint(summary)


async def main():
    """메인 함수"""
    print("=" * 100)
    print("3개 증권사 계좌 요약 조회 도구".center(100))
    print(f"실행 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}".center(100))
    print("=" * 100)

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

    # 결과 표시
    if accounts:
        display_account_summary(accounts)
        display_json_format(accounts)
    else:
        print("\n❌ 조회된 계좌가 없습니다.")


if __name__ == "__main__":
    asyncio.run(main())
