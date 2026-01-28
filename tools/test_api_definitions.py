#!/usr/bin/env python3
"""
Kiwoom, KIS, LS API 정의 조회 도구
각 플랫폼의 모든 API ID와 설명을 출력합니다.
"""
import sys
from pathlib import Path

# 프로젝트 경로 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from backend.domains.stkcompanys.kiwoom.models.kiwoom_request_definition import KIWOOM_REQUEST_DEF
from backend.domains.stkcompanys.kis.models.kis_request_definition import KIS_REQUEST_DEF
from backend.domains.stkcompanys.ls.models.ls_request_definition import LS_REQUEST_DEF


def print_section(title: str):
    """섹션 헤더 출력"""
    print(f"\n{'='*80}")
    print(f"  {title}")
    print(f"{'='*80}\n")


def print_api_list(name: str, api_dict: dict):
    """API 목록 출력"""
    # Kiwoom의 경우 WebSocket과 REST API 분리
    if name == "🥝 Kiwoom":
        ws_apis = {}
        rest_apis = {}

        for api_id, api_def in api_dict.items():
            url = api_def.get('url', '')
            if url.startswith('wss://'):
                ws_apis[api_id] = api_def
            else:
                rest_apis[api_id] = api_def

        print_section(f"{name} API 정의 ({len(api_dict)}개 총 {len(rest_apis)}개 REST + {len(ws_apis)}개 WebSocket)")

        if rest_apis:
            print("  📡 REST API:")
            for api_id, api_def in sorted(rest_apis.items()):
                title = api_def.get('title', 'N/A')
                print(f"    {api_id:18} | {title}")

        if ws_apis:
            print(f"\n  🔌 WebSocket API ({len(ws_apis)}개):")
            for api_id, api_def in sorted(ws_apis.items()):
                title = api_def.get('title', 'N/A')
                print(f"    {api_id:18} | {title}")
    else:
        print_section(f"{name} API 정의 ({len(api_dict)}개)")

        for api_id, api_def in sorted(api_dict.items()):
            title = api_def.get('title', 'N/A')
            tr_id = api_def.get('tr_id') or api_def.get('tr_cd', '')

            if tr_id and tr_id != api_id:
                print(f"  {api_id:20} | {tr_id:15} | {title}")
            else:
                print(f"  {api_id:20} | {title}")


def print_summary(kiwoom_dict: dict, kis_count: int, ls_count: int):
    """요약 정보 출력"""
    # Kiwoom API 타입별 분류
    kiwoom_ws = sum(1 for api in kiwoom_dict.values() if api.get('url', '').startswith('wss://'))
    kiwoom_rest = len(kiwoom_dict) - kiwoom_ws

    total = len(kiwoom_dict) + kis_count + ls_count
    print_section("요약")
    print(f"  Kiwoom  : {kiwoom_rest:4}개 (REST) + {kiwoom_ws:4}개 (WebSocket) = {len(kiwoom_dict):4}개")
    print(f"  KIS     : {kis_count:4}개")
    print(f"  LS      : {ls_count:4}개")
    print(f"  {'─'*50}")
    print(f"  합계     : {total:4}개\n")


def main():
    """메인 함수"""
    print("\n📊 API 정의 조회 도구\n")

    # 각 플랫폼의 API 출력
    print_api_list("🥝 Kiwoom", KIWOOM_REQUEST_DEF)
    print_api_list("📈 KIS", KIS_REQUEST_DEF)
    print_api_list("🏢 LS", LS_REQUEST_DEF)

    # 요약 출력
    print_summary(
        KIWOOM_REQUEST_DEF,
        len(KIS_REQUEST_DEF),
        len(LS_REQUEST_DEF)
    )


if __name__ == '__main__':
    main()
