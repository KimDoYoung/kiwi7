# extract_kw_resp_def.py

import sys
import pandas as pd

def extract_api_response_definition(sheet_index: int, file_path: str) -> dict:
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names

    if sheet_index < 0 or sheet_index >= len(sheet_names):
        raise IndexError(f"Sheet index out of range. Available range: 0 to {len(sheet_names) - 1}")

    sheet = sheet_names[sheet_index]
    df = pd.read_excel(file_path, sheet_name=sheet)

    title = str(df.iloc[3, 2]).strip() if pd.notna(df.iloc[3, 2]) else ''
    api_id = str(df.iloc[4, 2]).strip() if pd.notna(df.iloc[4, 2]) else ''

    df_body = df.iloc[15:].dropna(how='all', axis=1)
    df_body.columns = df_body.iloc[0]
    df_body = df_body[1:]

    # ✅ Response Body만 추출
    body_rows = []
    in_response = False
    for _, row in df_body.iterrows():
        section = str(row.get("구분")).strip()
        if section == "Response":
            in_response = True
            continue
        if in_response and section != "":
            break  # 다음 section으로 넘어가면 종료
        if in_response:
            body_rows.append(row)

    df_resp = pd.DataFrame(body_rows)

    body_items = []
    prev_key = ''
    for _, row in df_resp.iterrows():
        key = str(row['Element']).strip()
        name = str(row['한글명']).strip()
        dtype = str(row['Type']).strip().lower()
        required = str(row.get('Required', '')).strip().upper() == 'Y'
        length = int(row['Length']) if str(row['Length']).isdigit() else None
        desc = str(row.get('Description', '')).replace('\n', ' ').strip().replace("'", "")

        data = {
            'key': key,
            'name': name,
            'type': dtype,
            'required': required,
            'length': length,
            'description': desc
        }
        if key != prev_key:
            body_items.append(data)
        prev_key = key

    return {
        api_id: body_items
    }

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
