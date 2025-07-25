# extract_kw_resp_def.py

import sys
import pandas as pd

import pandas as pd

def extract_api_response_definition(sheet_index: int, file_path: str) -> dict:
    xls = pd.ExcelFile(file_path)
    sheet_name = xls.sheet_names[sheet_index]
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

    # API ID 추출
    api_id = str(df.iloc[5, 2]).strip() if pd.notna(df.iloc[5, 2]) else ''

    # 1. Response라는 셀 위치 찾기
    response_idx = None
    for i, row in df.iterrows():
        if row.astype(str).str.contains("Response", na=False).any():
            response_idx = i
            break
    if response_idx is None:
        raise ValueError("Response 셀을 찾을 수 없습니다")

    # 2. Example 포함된 행 찾기
    example_idx = None
    for i in range(response_idx + 1, len(df)):
        if df.iloc[i].astype(str).str.contains("Example", na=False).any():
            example_idx = i
            break
    if example_idx is None:
        raise ValueError("Example 행을 찾을 수 없습니다")

    # 3. 컬럼명 행은 Response 다음 줄
    header_row = df.iloc[response_idx + 1]
    df_data = df.iloc[response_idx + 2 : example_idx].copy()
    df_data.columns = header_row

    # 4. "구분"이 "Body"인 행만 필터링
    # df_data = df_data[df_data["구분"] == "Body"]
    # body_rows = []
    # in_body = False
    # for _, row in df_data.iterrows():
    #     section = str(row.get("구분", "")).strip()
    #     if section == "Body":
    #         in_body = True
    #     elif section not in ("", "Body"):
    #         if in_body:
    #             break  # Body가 끝났다면 중단
    #     if in_body:
    #         body_rows.append(row)
    # df_data = pd.DataFrame(body_rows)        
    # 5. 정리
    body_items = []
    prev_key = ''
    insert_flag = False
    for _, row in df_data.iterrows():
        section = str(row.get("구분") or "").strip()
        if section == "Body":
            insert_flag = True
        key = str(row.get('Element', '')).strip()
        if key.startswith('-'):
            key = key[1:].strip()
        name = str(row.get('한글명', '')).strip()
        dtype = str(row.get('Type', '')).strip().lower()
        required = str(row.get('Required', '')).strip().upper() == 'Y'
        length = int(row['Length']) if str(row.get('Length', '')).isdigit() else None
        desc = str(row.get('Description') or "").replace('\n', ' ').strip().replace("'", "")
        if desc == 'nan':
            desc = None

        if not key:
            continue
        if key != prev_key and insert_flag:
            body_items.append({
                'key': key,
                'name': name,
                'type': dtype,
                'required': required,
                'length': length,
                'description': desc
            })
        prev_key = key

    return {api_id: body_items}


def myprint_resp(result):
    for api_key, body in result.items():
        print(f"'{api_key}': [")
        for i, item in enumerate(body):
            comma = "," if i < len(body) - 1 else ""
            print(f"    {{'key': '{item['key']}', 'name': '{item['name']}', 'type': '{item['type']}', "
                  f"'required': {item['required']}, 'length': {item['length']}, 'description': '{item['description']}'}}{comma}")
        print("],\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python extract_kw_resp_def.py <excel_path>")
        sys.exit(1)

    excel_path = sys.argv[1]

    try:
        xls = pd.ExcelFile(excel_path)
        for i in range(1, len(xls.sheet_names)):  # 2번째 시트부터
            try:
                result = extract_api_response_definition(i, excel_path)
                myprint_resp(result)
            except Exception as e:
                print(f"[시트 {i} - {xls.sheet_names[i]}] 오류 발생: {e}")
    except Exception as e:
        print("전체 오류:", e)
