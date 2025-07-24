
import sys
import pandas as pd

def extract_api_definition(sheet_index: int, file_path: str) -> dict:
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names

    if sheet_index < 0 or sheet_index >= len(sheet_names):
        raise IndexError(f"Sheet index out of range. Available range: 0 to {len(sheet_names) - 1}")

    sheet = sheet_names[sheet_index]
    df = pd.read_excel(file_path, sheet_name=sheet)

    title = str(df.iloc[3, 2]).strip() if pd.notna(df.iloc[3, 2]) else ''
    api_id = str(df.iloc[4, 2]).strip() if pd.notna(df.iloc[4, 2]) else ''
    method = str(df.iloc[6, 2]).strip().upper() if pd.notna(df.iloc[6, 2]) else ''
    base_url = str(df.iloc[7, 2]).strip() if pd.notna(df.iloc[7, 2]) else ''
    url_path = str(df.iloc[9, 2]).strip() if pd.notna(df.iloc[9, 2]) else ''
    url = base_url + url_path if base_url and url_path else ''

    if not (api_id and url and title):
        raise ValueError("필수 메타 정보(api_id, title, url)가 누락되었습니다.")

    df_body = df.iloc[15:].dropna(how='all', axis=1)
    df_body.columns = df_body.iloc[0]
    df_body = df_body[1:]

    # ✅ '구분' 열이 존재하고, 그 안에 'Body'가 있을 때까지만 추출
    body_rows = []
    in_body_section = False

    for _, row in df_body.iterrows():
        section = str(row.get("구분")).strip()
        if section == "Response":
            break
        if section == "Body":
            in_body_section = True
        if in_body_section:
            body_rows.append(row)
    # DataFrame으로 다시 만들기
    df_body = pd.DataFrame(body_rows)

    body_items = []
    prev_key = ''
    for _, row in df_body.iterrows():
        key = str(row['Element']).strip()
        name = str(row['한글명']).strip()
        dtype = str(row['Type']).strip().lower()
        required = str(row['Required']).strip().upper() == 'Y'
        length = int(row['Length']) if str(row['Length']).isdigit() else None
        desc = str(row['Description']).replace('\n', ' ').strip() if pd.notna(row['Description']) else ''
        desc = desc.replace("'", "")
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
def myprint1(result):
    # 실제 출력
    api_id = list(result.keys())[0]
    api_info = result[api_id]

    print(f"API ID: {api_id}")
    print(f"url   : {api_info['url']}")
    print(f"title : {api_info['title']}")
    print("body  :")
    for item in api_info['body']:
        print(f"  - key={item['key']}, name={item['name']}, type={item['type']}, "
            f"required={item['required']}, length={item['length']}, description={item['description']}")

def myprint(result):
    # 외곽 {} 제거하고 원하는 순서로 출력
    for api_key, api_data in result.items():
        print(f"'{api_key}': {{")
        print(f"    'url': '{api_data['url']}',")
        print(f"    'title': '{api_data['title']}',")
        print(f"    'body': [")
        
        for i, body_item in enumerate(api_data['body']):
            # body 배열의 각 객체를 key, name, type, required, length, description 순으로 한 줄에 출력
            comma = "," if i < len(api_data['body']) - 1 else ""
            print(f"        {{'key': '{body_item['key']}', 'name': '{body_item['name']}', 'type': '{body_item['type']}', 'required': {body_item['required']}, 'length': {body_item['length']}, 'description': '{body_item['description']}'}}{comma}")
        
        print(f"    ]")
        print(f"}},\n")    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python extract_kw_api_def.py <excel_path>")
        sys.exit(1)

    excel_path = sys.argv[1]

    try:
        xls = pd.ExcelFile(excel_path)
        for i in range(1, len(xls.sheet_names)):
        # for i in range(13, 15):            
            try:
                result = extract_api_definition(i, excel_path)
                myprint(result)
                # from pprint import pprint
                # pprint(result)
            except Exception as e:
                print(f"[시트 {i} - {xls.sheet_names[i]}] 오류 발생: {e}")
    except Exception as e:
        print("전체 오류:", e)
