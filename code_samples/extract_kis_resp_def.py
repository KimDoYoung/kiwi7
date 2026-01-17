#!/usr/bin/env python3
"""
KIS API Response 정의 추출 스크립트

한국투자증권(KIS) REST API 엑셀 문서에서 Response 정의를 파싱하여
Python 딕셔너리 형태로 변환합니다.

Usage:
    python extract_kis_resp_def.py <excel_file_path>
    
Example:
    python extract_kis_resp_def.py "_국내주식__기본시세.xlsx"
"""

import sys
from pathlib import Path

import pandas as pd


def parse_api_list(file_path: str) -> dict:
    """
    'API 목록' 시트에서 기본 정보 추출
    
    Returns:
        dict: {tr_id: {sheet_name, ...}, ...}
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
            'sheet_name': row.get('API 명', ''),
            'title': row.get('API 명', '')
        }
    
    return api_info


def parse_response_fields(file_path: str, sheet_name: str, tr_id: str) -> dict:
    """
    개별 API 시트에서 Response 필드 정보 추출
    
    Returns:
        dict: {output: {type, fields}, output1: {...}, ...}
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
    except Exception as e:
        print(f"  ⚠ 시트 '{sheet_name}' 읽기 실패: {e}")
        return None
    
    result = {}
    current_output = None
    current_fields = []
    in_response = False
    
    for idx, row in df.iterrows():
        # Response Body 섹션 시작 확인
        if pd.notna(row[0]) and 'Response Body' in str(row[0]):
            in_response = True
            
            # 웹소켓 API인 경우: Response Body 바로 다음에 필드가 시작될 수 있음
            # 같은 행에 첫 번째 필드가 있는지 확인
            if len(row) > 1 and pd.notna(row[1]):
                # 이 경우 웹소켓 API로 간주하고 단일 output 구조로 처리
                current_output = {
                    'name': 'output',
                    'type': 'object'
                }
                current_fields = []
            continue
        
        # Response Example 시작하면 종료
        if pd.notna(row[0]) and 'Response Example' in str(row[0]):
            # 마지막 output 저장
            if current_output and current_fields:
                result[current_output['name']] = {
                    'type': current_output['type'],
                    'fields': current_fields
                }
            break
        
        if not in_response:
            continue
        
        # 필드 파싱
        if len(row) > 1 and pd.notna(row[1]):
            field_name = str(row[1]).strip()
            field_desc = str(row[2]).strip() if len(row) > 2 and pd.notna(row[2]) else ''
            field_type = str(row[3]).strip() if len(row) > 3 and pd.notna(row[3]) else ''
            
            # rt_cd, msg_cd, msg1은 공통 응답이므로 제외
            if field_name in ['rt_cd', 'msg_cd', 'msg1']:
                continue
            
            # output, output1, output2 등 확인 (REST API의 경우)
            if 'output' in field_name.lower() and field_type:
                # 이전 output 저장
                if current_output and current_fields:
                    result[current_output['name']] = {
                        'type': current_output['type'],
                        'fields': current_fields
                    }
                
                # 새 output 시작
                output_type = 'array' if 'array' in field_type.lower() else 'object'
                current_output = {
                    'name': field_name,
                    'type': output_type
                }
                current_fields = []
                continue
            
            # 웹소켓 API의 경우: current_output이 아직 설정되지 않았으면 자동으로 설정
            if not current_output:
                current_output = {
                    'name': 'output',
                    'type': 'object'
                }
                current_fields = []
            
            # output의 하위 필드
            if current_output:
                # 빈 필드 이름은 제외
                if not field_name or field_name == ' ':
                    continue
                
                # JSON 예제 등은 제외
                if field_name.startswith('{') or field_name.startswith('['):
                    continue
                
                # type, required, length, description 추출
                field_type = str(row[3]).strip().lower() if len(row) > 3 and pd.notna(row[3]) and str(row[3]).strip() else 'string'
                field_required = str(row[4]).strip() == 'Y' if len(row) > 4 and pd.notna(row[4]) else False
                field_length = None
                if len(row) > 5 and pd.notna(row[5]):
                    try:
                        length_str = str(row[5]).strip()
                        if length_str and length_str != ' ':
                            field_length = int(float(length_str))
                    except:
                        pass
                
                field_description = ''
                if len(row) > 6 and pd.notna(row[6]):
                    desc_str = str(row[6]).strip()
                    if desc_str and desc_str != ' ':
                        # 줄바꿈 제거 및 정리
                        field_description = desc_str.replace('\\r\\n', ' ').replace('\n', ' ').strip()
                
                field_info = {
                    'key': field_name,
                    'name': field_desc if field_desc else field_name,
                    'type': field_type,
                    'required': field_required,
                    'length': field_length,
                    'description': field_description
                }
                
                current_fields.append(field_info)
    
    # 마지막 output 저장 (루프가 끝났는데 아직 저장 안 된 경우)
    if current_output and current_fields and current_output['name'] not in result:
        result[current_output['name']] = {
            'type': current_output['type'],
            'fields': current_fields
        }
    
    return result


def generate_kis_response_def(file_path: str, output_file: str = None) -> str:
    """
    KIS API Response 정의를 Python 딕셔너리 형태로 생성
    
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
    kis_response_def = {}
    
    # 각 API Response 파싱
    for tr_id, info in api_list.items():
        sheet_name = info['sheet_name']
        print(f"\n처리 중: {tr_id} - {sheet_name}")
        
        # Response 필드 파싱
        outputs = parse_response_fields(file_path, sheet_name, tr_id)
        
        if outputs is None or not outputs:
            continue
        
        # 결과 구성
        kis_response_def[tr_id] = outputs
        
        # 출력 정보 표시
        for output_name, output_info in outputs.items():
            field_count = len(output_info['fields'])
            output_type = output_info['type']
            print(f"  - {output_name} ({output_type}): {field_count}개 필드")
    
    # Python 코드 생성
    code = "# KIS REST API Response Definitions\n"
    code += "# Auto-generated from Excel file\n\n"
    code += "KIS_RESPONSE_DEF = {\n"
    
    # 각 API를 수동으로 포맷팅
    for idx, (tr_id, outputs) in enumerate(kis_response_def.items()):
        code += f"    '{tr_id}': {{\n"
        
        # 각 output 처리
        for output_idx, (output_name, output_info) in enumerate(outputs.items()):
            code += f"        '{output_name}': {{\n"
            code += f"            'type': '{output_info['type']}',\n"
            code += f"            'fields': [\n"
            
            # 각 필드를 한 줄로
            for field_idx, field in enumerate(output_info['fields']):
                # 필드를 한 줄로 표현
                field_str = "{"
                field_str += f"'key': '{field['key']}', "
                field_str += f"'name': '{field['name']}', "
                field_str += f"'type': '{field['type']}', "
                field_str += f"'required': {field['required']}, "
                field_str += f"'length': {field['length']}, "
                field_str += f"'description': '{field['description']}'"
                field_str += "}"
                
                # 마지막 필드가 아니면 쉼표 추가
                if field_idx < len(output_info['fields']) - 1:
                    field_str += ","
                
                code += f"                {field_str}\n"
            
            code += "            ]\n"
            
            # 마지막 output이 아니면 쉼표 추가
            if output_idx < len(outputs) - 1:
                code += "        },\n"
            else:
                code += "        }\n"
        
        # 마지막 API가 아니면 쉼표 추가
        if idx < len(kis_response_def) - 1:
            code += "    },\n"
        else:
            code += "    }\n"
    
    code += "}\n"
    
    # 출력
    if output_file:
        output_path = Path(output_file)
        output_path.write_text(code, encoding='utf-8')
        print(f"\n\n✅ 출력 파일 생성: {output_file}")
        print(f"   총 {len(kis_response_def)}개 API 정의")
        
        # 통계 출력
        total_outputs = sum(len(v) for v in kis_response_def.values())
        total_fields = sum(
            len(output_info['fields']) 
            for api_outputs in kis_response_def.values() 
            for output_info in api_outputs.values()
        )
        print(f"   총 {total_outputs}개 output")
        print(f"   총 {total_fields}개 필드")
    else:
        print("\n" + "="*80)
        print(code)
        print("="*80)
    
    return code


def main():
    """메인 함수"""
    if len(sys.argv) < 2:
        print("Usage: python extract_kis_resp_def.py <excel_file_path> [output_file]")
        print("\nExample:")
        print("  python extract_kis_resp_def.py '_국내주식__기본시세.xlsx'")
        print("  python extract_kis_resp_def.py '_국내주식__기본시세.xlsx' kis_response_def.py")
        sys.exit(1)
    
    excel_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # 파일 존재 확인
    if not Path(excel_file).exists():
        print(f"❌ 파일을 찾을 수 없습니다: {excel_file}")
        sys.exit(1)
    
    try:
        generate_kis_response_def(excel_file, output_file)
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()