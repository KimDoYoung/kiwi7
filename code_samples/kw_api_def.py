
import sys
import pandas as pd

def extract_api_definition(sheet_index: int, file_path: str = "키움 REST API 문서.xlsx") -> dict:
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names

    if sheet_index < 0 or sheet_index >= len(sheet_names):
        raise IndexError(f"Sheet index out of range. Available range: 0 to {len(sheet_names) - 1}")

    sheet = sheet_names[sheet_index]
    df = pd.read_excel(file_path, sheet_name=sheet)

    title = str(df.iloc[3, 2]).strip() if pd.notna(df.iloc[3, 2]) else ''
    api_id = str(df.iloc[4, 2]).strip() if pd.notna(df.iloc[4, 2]) else ''
    method = str(df.iloc[6, 2]).strip().upper() if pd.notna(df.iloc[6, 2]) else ''
    url = str(df.iloc[9, 2]).strip() if pd.notna(df.iloc[9, 2]) else ''

    if not (api_id and url and title):
        raise ValueError("필수 메타 정보(api_id, title, url)가 누락되었습니다.")

    df_body = df.iloc[15:].dropna(how='all', axis=1)
    df_body.columns = df_body.iloc[0]
    df_body = df_body[1:]
    df_body = df_body[df_body['구분'] == 'Body']

    body_items = []
    prev_key = ''
    for _, row in df_body.iterrows():
        key = str(row['Element']).strip()
        name = str(row['한글명']).strip()
        dtype = str(row['Type']).strip().lower()
        required = str(row['Required']).strip().upper() == 'Y'
        length = int(row['Length']) if str(row['Length']).isdigit() else None
        desc = str(row['Description']).replace('\n', ' ').strip() if pd.notna(row['Description']) else ''

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
        api_id: {
            'url': url,
            'title': title,
            'body': body_items
        }
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python kw_api_def.py <sheet_index>")
        sys.exit(1)

    try:
        index = int(sys.argv[1])
        result = extract_api_definition(index, 'c:\\tmp\\kwapi.xlsx')
        print(result)
    except Exception as e:
        print("오류:", e)
