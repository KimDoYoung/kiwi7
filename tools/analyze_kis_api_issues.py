#!/usr/bin/env python3
"""
KIS API 정의에서 문제가 있는 항목들을 찾아서 분석합니다.
"""
import sys
from pathlib import Path
import re

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from backend.domains.stkcompanys.kis.models.kis_request_definition import KIS_REQUEST_DEF


def extract_tr_ids(tr_id_str: str) -> list:
    """TR ID 문자열에서 실제 TR ID들 추출"""
    if not tr_id_str:
        return []

    # 패턴: (설명) XXXXX 또는 XXXXX(설명) 또는 단순 XXXXX
    pattern = r'([A-Z0-9]{6,10})'
    matches = re.findall(pattern, str(tr_id_str))
    return list(set(matches))  # 중복 제거


def main():
    print("\n🔍 KIS API 정의 분석\n")

    problem_apis = []
    normal_apis = 0

    for api_id, api_def in KIS_REQUEST_DEF.items():
        tr_id = api_def.get('tr_id', '')
        title = api_def.get('title', 'N/A')

        # 문제 있는 것: API ID가 TR ID처럼 보이거나 특수 문자 포함
        if '|' in str(api_id) or '(' in str(api_id) or ')' in str(api_id):
            extracted_ids = extract_tr_ids(api_id)
            problem_apis.append({
                'api_id': api_id,
                'tr_id': tr_id,
                'title': title,
                'extracted': extracted_ids
            })
        else:
            normal_apis += 1

    print(f"📊 통계")
    print(f"  정상 API: {normal_apis}개")
    print(f"  문제 있는 API: {len(problem_apis)}개\n")

    if problem_apis:
        print("=" * 100)
        print("  ⚠️  문제 있는 API ID들")
        print("=" * 100)

        for i, problem in enumerate(problem_apis, 1):
            print(f"\n  {i}. API ID (잘못됨): {problem['api_id']}")
            print(f"     설명: {problem['title']}")
            print(f"     TR ID 필드: {problem['tr_id']}")

            if problem['extracted']:
                print(f"     추출된 실제 TR ID: {', '.join(problem['extracted'])}")
            else:
                print(f"     실제 TR ID를 추출하지 못함 - 수동 확인 필요")

        print("\n" + "=" * 100)
        print("  💡 해결 방법")
        print("=" * 100)
        print("""
  이 API들은 실제로는 하나의 논리적 기능이 여러 TR ID를 사용합니다.

  옵션:
  1. API ID를 올바르게 정정 (예: TTTC0081R)
  2. 또는 별도의 메타데이터로 관리
  3. 또는 API ID를 정규화하고 별도 매핑 테이블 사용
        """)


if __name__ == '__main__':
    main()
