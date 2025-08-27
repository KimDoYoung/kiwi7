#!/usr/bin/env python3
"""
fetch_stk_info 함수 테스트 예제

이 파일은 backend/api/common/stock_functions.py의 fetch_stk_info 함수를 테스트합니다.
fetch_stk_info는 종목 코드 리스트를 받아서 각 종목의 정보를 키움 API로 조회하거나 캐시에서 가져옵니다.

사용법:
    python code_samples/ex_func1.py

작성자: 김도영
작성일: 2025-08-27
"""

import asyncio
import sys
import os
import json
from datetime import datetime

# 상위 디렉토리를 모듈 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.api.common.stock_functions import fetch_stk_info
from backend.core.logger import get_logger

logger = get_logger(__name__)

async def test_fetch_stk_info():
    """fetch_stk_info 함수 테스트"""
    
    print("=" * 60)
    print("fetch_stk_info 함수 테스트 시작")
    print("=" * 60)
    
    # 테스트할 종목 코드 리스트 (삼성전자, SK하이닉스, NAVER, 카카오)
    test_stock_codes = [
        "005930",  # 삼성전자
        "000660",  # SK하이닉스
        "035420",  # NAVER
        "035720"   # 카카오
    ]
    
    try:
        print(f"테스트 종목 코드: {test_stock_codes}")
        print("API 호출 시작...")
        
        start_time = datetime.now()
        
        # fetch_stk_info 함수 호출
        results = await fetch_stk_info(test_stock_codes)
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        print(f"API 호출 완료 - 소요시간: {duration:.2f}초")
        print(f"결과 개수: {len(results)}개")
        print("-" * 60)
        
        # 결과 출력
        for i, result in enumerate(results):
            stock_code = test_stock_codes[i] if i < len(test_stock_codes) else f"index_{i}"
            
            print(f"\n[{i+1}] 종목코드: {stock_code}")
            
            if hasattr(result, 'success'):
                # KiwoomResponse 객체인 경우
                if result.success:
                    print(f"  성공: {result.success}")
                    if result.data:
                        # 주요 정보만 출력
                        data = result.data
                        print(f"  종목명: {data.get('종목명', 'N/A')}")
                        print(f"  시장구분: {data.get('시장구분', 'N/A')}")
                        print(f"  업종명: {data.get('업종명', 'N/A')}")
                        print(f"  현재가: {data.get('현재가', 'N/A')}")
                        print(f"  전일대비: {data.get('전일대비', 'N/A')}")
                        print(f"  등락률: {data.get('등락률', 'N/A')}")
                        print(f"  거래량: {data.get('거래량', 'N/A')}")
                    else:
                        print("  데이터가 없습니다.")
                else:
                    print(f"  실패: {result.error_message}")
            elif isinstance(result, dict):
                # 캐시에서 가져온 딕셔너리 데이터인 경우
                print("  캐시 데이터:")
                print(f"  종목명: {result.get('종목명', 'N/A')}")
                print(f"  시장구분: {result.get('시장구분', 'N/A')}")
                print(f"  업종명: {result.get('업종명', 'N/A')}")
                print(f"  현재가: {result.get('현재가', 'N/A')}")
            else:
                print(f"  알 수 없는 형식: {type(result)}")
                print(f"  내용: {str(result)[:200]}...")
        
        print("\n" + "=" * 60)
        print("테스트 완료")
        print("=" * 60)
        
        return results
        
    except Exception as e:
        logger.error(f"테스트 중 오류 발생: {str(e)}", exc_info=True)
        print(f"오류 발생: {str(e)}")
        return None

async def test_cache_functionality():
    """캐시 기능 테스트"""
    
    print("\n" + "=" * 60)
    print("캐시 기능 테스트")
    print("=" * 60)
    
    # 같은 종목을 두 번 조회해서 캐시가 작동하는지 확인
    test_code = ["005930"]  # 삼성전자
    
    print("첫 번째 조회 (API 호출):")
    start_time1 = datetime.now()
    result1 = await fetch_stk_info(test_code)
    end_time1 = datetime.now()
    duration1 = (end_time1 - start_time1).total_seconds()
    print(f"소요시간: {duration1:.2f}초")
    
    print("\n두 번째 조회 (캐시 사용):")
    start_time2 = datetime.now()
    result2 = await fetch_stk_info(test_code)
    end_time2 = datetime.now()
    duration2 = (end_time2 - start_time2).total_seconds()
    print(f"소요시간: {duration2:.2f}초")
    
    print(f"\n성능 개선: {duration1/duration2:.2f}배 빨라짐" if duration2 > 0 else "\n성능 측정 불가")
    
    return result1, result2

async def test_error_handling():
    """에러 핸들링 테스트"""
    
    print("\n" + "=" * 60)
    print("에러 핸들링 테스트")
    print("=" * 60)
    
    # 잘못된 종목 코드로 테스트
    invalid_codes = ["999999", "INVALID", ""]
    
    try:
        results = await fetch_stk_info(invalid_codes)
        
        for i, result in enumerate(results):
            code = invalid_codes[i] if i < len(invalid_codes) else f"index_{i}"
            print(f"종목코드 '{code}': ", end="")
            
            if hasattr(result, 'success'):
                if result.success:
                    print("성공 (예상치 못한 결과)")
                else:
                    print(f"실패 - {result.error_message}")
            else:
                print(f"알 수 없는 응답: {type(result)}")
        
    except Exception as e:
        print(f"예외 발생: {str(e)}")

def print_json_pretty(data, title="JSON 데이터"):
    """JSON 데이터를 예쁘게 출력"""
    print(f"\n{title}:")
    print(json.dumps(data, ensure_ascii=False, indent=2))

async def main():
    """메인 함수"""
    
    print("fetch_stk_info 테스트 프로그램")
    print(f"실행 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # 1. 기본 기능 테스트
        results = await test_fetch_stk_info()
        
        # 2. 캐시 기능 테스트
        await test_cache_functionality()
        
        # 3. 에러 핸들링 테스트
        await test_error_handling()
        
    except KeyboardInterrupt:
        print("\n사용자에 의해 중단되었습니다.")
    except Exception as e:
        logger.error(f"메인 함수에서 오류 발생: {str(e)}", exc_info=True)
        print(f"예상치 못한 오류: {str(e)}")

if __name__ == "__main__":
    # 이벤트 루프 실행
    asyncio.run(main())
