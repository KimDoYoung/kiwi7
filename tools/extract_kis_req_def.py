#!/usr/bin/env python3
"""
KIS API Excel 문서 파싱 스크립트

한국투자증권(KIS) REST API 엑셀 문서를 파싱하여
Python 딕셔너리 형태로 변환합니다.

Usage:
    python extract_kis_req_def.py <excel_file_path>
    
Example:
    python extract_kis_req_def.py "_국내주식__기본시세.xlsx"
"""

import json
import sys
from pathlib import Path

import pandas as pd


def parse_api_list(file_path: str) -> dict:
    """
    'API 목록' 시트에서 기본 정보 추출
    
    Returns:
        dict: {tr_id: {url, title, method, ...}, ...}
    """
    df = pd.read_excel(file_path, sheet_name='API 목록')
    
    api_info = {}
    for _, row in df.iterrows():
        # 실전 TR_ID가 있는 경우만 처리
        tr_id = row.get('실전 TR_ID')
        if pd.isna(tr_id) or tr_id == '모의투자 미지원':
            # 모의 TR_ID 확인
            tr_id = row.get('모의 TR_ID')
            if pd.isna(tr_id) or tr_id == '모의투자 미지원':
                continue
        
        api_info[str(tr_id)] = {
            'url': row.get('URL 명', ''),
            'title': row.get('API 명', ''),
            'method': row.get('HTTP Method', 'GET'),
            'api_id': row.get('API ID', ''),
            'sheet_name': row.get('API 명', '')  # 시트 이름으로 사용
        }
    
    return api_info


def parse_api_detail(file_path: str, sheet_name: str, tr_id: str) -> dict:
    """
    개별 API 시트에서 상세 파라미터 정보 추출
    
    Returns:
        dict: {header, query, body, path 정보}
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
    except Exception as e:
        print(f"  ⚠ 시트 '{sheet_name}' 읽기 실패: {e}")
        return None
    
    result = {
        'header': [],
        'query': [],
        'body': [],
        'path': []
    }
    
    current_section = None
    
    for idx, row in df.iterrows():
        # 섹션 헤더 확인 (첫 번째 컬럼이 섹션명인 경우)
        if pd.notna(row[0]):
            section_name = str(row[0]).strip()
            
            # 섹션 구분
            if 'Request Header' in section_name:
                current_section = 'header'
                # 같은 행에 첫 번째 파라미터가 있을 수 있음
            elif 'Request Query' in section_name:
                current_section = 'query'
            elif 'Request Body' in section_name:
                current_section = 'body'
            elif 'Request Path' in section_name:
                current_section = 'path'
            elif 'Response' in section_name:
                # Response 섹션은 여기서 중단
                break
            else:
                # 섹션 헤더가 아닌 경우, 다음 행으로
                continue
        
        # 파라미터 파싱
        if current_section:
            # row[1]에 파라미터 키가 있는지 확인 (섹션 헤더 행이거나 파라미터 행)
            if len(row) > 1 and pd.notna(row[1]):
                element = row[1]
                name = row[2] if len(row) > 2 and not pd.isna(row[2]) else ''
                type_val = row[3] if len(row) > 3 and not pd.isna(row[3]) else 'string'
                required = row[4] if len(row) > 4 and not pd.isna(row[4]) else 'N'
                length = row[5] if len(row) > 5 and not pd.isna(row[5]) else None
                description = row[6] if len(row) > 6 and not pd.isna(row[6]) else ''
                
                # 헤더 필터링 (기본 헤더는 제외)
                if current_section == 'header':
                    # 표준 HTTP 헤더와 인증 관련 헤더는 건너뜀
                    skip_headers = [
                        'content-type', 'authorization', 'appkey', 
                        'appsecret', 'personalseckey', 'tr_id',
                        'tr_cont', 'custtype', 'seq_no', 'mac_address',
                        'phone_number', 'ip_addr', 'gt_uid'
                    ]
                    if element.lower() in skip_headers:
                        continue
                
                param = {
                    'key': element,
                    'name': name,
                    'type': type_val.lower() if isinstance(type_val, str) else 'string',
                    'required': required == 'Y',
                }
                
                # length 추가 (있는 경우)
                if length and not pd.isna(length):
                    try:
                        # 숫자가 아닌 경우 처리
                        length_str = str(length).strip()
                        if length_str and length_str != ' ':
                            param['length'] = int(float(length_str))
                    except:
                        pass
                
                # description 추가 (있는 경우)
                if description and str(description).strip() and str(description).strip() != ' ':
                    # 줄바꿈 제거 및 정리
                    desc_clean = str(description).replace('\\r\\n', ' ').replace('\n', ' ').strip()
                    if desc_clean:
                        param['description'] = desc_clean
                
                result[current_section].append(param)
    
    return result


def generate_kis_request_def(file_path: str, output_file: str = None) -> str:
    """
    KIS API 정의를 Python 딕셔너리 형태로 생성
    
    Args:
        file_path: 엑셀 파일 경로
        output_file: 출력 파일 경로 (없으면 stdout)
    
    Returns:
        str: 생성된 Python 코드
    """
    print(f"📖 엑셀 파일 읽기: {file_path}")
    
    # API 목록 파싱
    api_list = parse_api_list(file_path)
    print(f"✓ API 목록 파싱 완료: {len(api_list)}개 API 발견")
    
    # 결과 딕셔너리
    kis_request_def = {}
    
    # 각 API 상세 파싱
    for tr_id, info in api_list.items():
        sheet_name = info['sheet_name']
        print(f"\n처리 중: {tr_id} - {sheet_name}")
        
        # 상세 파라미터 파싱
        detail = parse_api_detail(file_path, sheet_name, tr_id)
        
        if detail is None:
            continue
        
        # 결과 구성
        api_def = {
            'url': info['url'],
            'title': info['title'],
            'method': info['method'],
            'tr_id': tr_id,
        }
        
        # 파라미터가 있는 섹션만 추가
        if detail['header']:
            api_def['header'] = detail['header']
            print(f"  - Header: {len(detail['header'])}개")
        
        if detail['query']:
            api_def['query'] = detail['query']
            print(f"  - Query: {len(detail['query'])}개")
        
        if detail['body']:
            api_def['body'] = detail['body']
            print(f"  - Body: {len(detail['body'])}개")
        
        if detail['path']:
            api_def['path'] = detail['path']
            print(f"  - Path: {len(detail['path'])}개")
        
        kis_request_def[tr_id] = api_def
    
    # Python 코드 생성
    code = "# KIS REST API Request Definitions\n"
    code += "# Auto-generated from Excel file\n\n"
    code += "KIS_REQUEST_DEF = "
    
    # JSON으로 먼저 변환 후 Python 문법으로 변경
    json_str = json.dumps(kis_request_def, ensure_ascii=False, indent=4)
    # true/false를 True/False로 변경
    python_str = json_str.replace('true', 'True').replace('false', 'False').replace('null', 'None')
    code += python_str
    
    # 출력
    if output_file:
        output_path = Path(output_file)
        output_path.write_text(code, encoding='utf-8')
        print(f"\n\n✅ 출력 파일 생성: {output_file}")
        print(f"   총 {len(kis_request_def)}개 API 정의")
    else:
        print("\n" + "="*80)
        print(code)
        print("="*80)
    
    return code


def main():
    """메인 함수"""
    if len(sys.argv) < 2:
        print("Usage: python extract_kis_req_def.py <excel_file_path> [output_file]")
        print("\nExample:")
        print("  python extract_kis_req_def.py '_국내주식__기본시세.xlsx'")
        print("  python extract_kis_req_def.py '_국내주식__기본시세.xlsx' kis_request_def.py")
        sys.exit(1)
    
    excel_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # 파일 존재 확인
    if not Path(excel_file).exists():
        print(f"❌ 파일을 찾을 수 없습니다: {excel_file}")
        sys.exit(1)
    
    try:
        generate_kis_request_def(excel_file, output_file)
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()