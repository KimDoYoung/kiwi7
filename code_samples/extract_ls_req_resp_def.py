import json
import time

import requests

# 1. 제공된 데이터를 배열로 구성 (group_id, api_id)
api_list = [
    ("ffd2def7-a118-40f7-a0ab-cd4c6a538a90", "33bd887a-6652-4209-88cd-5324bc7c5e36"),
    ("ffd2def7-a118-40f7-a0ab-cd4c6a538a90", "2d923333-f816-4df9-932d-ad390437b66f"),
    ("f82999f4-eb1a-4ead-a0b1-a4386e8721ab", "88a7c0d3-fb4f-48ef-bc9b-4c47ac72a87b"),
    ("f82999f4-eb1a-4ead-a0b1-a4386e8721ab", "5b483d74-407c-4760-8452-1b2b1dc1dcde"),
    ("f82999f4-eb1a-4ead-a0b1-a4386e8721ab", "3c2b0280-6663-41e2-8995-a179de99e074"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "54a99b02-dbba-4057-8756-9ac759c9a2ed"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "3dbce945-a73c-475c-9758-88d9922ab94e"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "580d2770-a7a9-49e3-9ec1-49ed8bc734a2"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "6b554636-7b2a-4e1a-a615-54b0c131a558"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "c148a42f-51a7-4446-b6df-10d6056dd75b"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "90378c39-f93e-4f95-9670-f76e5c924cc6"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "3d58c125-8b45-46b4-baf2-6f98d0373131"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "30b6dfd6-b0bd-4e63-a510-7d5d94edc740"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "8f027fa6-4177-43e3-9a7a-a76873efd47c"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "6b67369a-dc7a-4cc7-8c33-71bb6336b6bf"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "d3d0ef41-6a0f-4bda-9e28-160071f66206"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "12320341-ad85-429a-90bd-5b3771c5e89f"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "316495d3-6109-45a6-baaf-9e8a0261f30a"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "37d22d4d-83cd-40a4-a375-81b010a4a627"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "d0e216e0-10d9-479f-8a4d-e175b8bae307"),
    ("73142d9f-1983-48d2-8543-89b75535d34c", "9a2800c3-9bf2-4d67-8d83-905074f06646"),
    ("2f1eea77-5606-4512-93c6-31b21d2ece90", "9f467798-6ce6-4d31-ab93-5a0e2860f89f"),
    ("2f1eea77-5606-4512-93c6-31b21d2ece90", "47005ce6-8500-4a3d-ad6c-f96ec3251669"),
    ("2f1eea77-5606-4512-93c6-31b21d2ece90", "a9b39b08-25c2-427d-848b-675c6228a92b"),
    ("2f1eea77-5606-4512-93c6-31b21d2ece90", "09a668df-d7e8-4b5c-977f-91d1429b931a"),
    ("2f1eea77-5606-4512-93c6-31b21d2ece90", "b579d38a-3ce5-4b1b-b94e-b0c4bbbf1d27"),
    ("2f1eea77-5606-4512-93c6-31b21d2ece90", "98373ce4-042a-4fc8-85ef-b9b8f64101ce"),
    ("2f1eea77-5606-4512-93c6-31b21d2ece90", "57936c91-b49d-4702-b7f6-3935c6859462"),
    ("c1ef0e8b-4666-4d8c-a77f-6ab488cfdb39", "d61d4f85-9845-41ef-b915-4efa8fd0aad1"),
    ("c1ef0e8b-4666-4d8c-a77f-6ab488cfdb39", "44c1c082-c899-48fb-bc66-bb5be2f0ab4e"),
    ("c1ef0e8b-4666-4d8c-a77f-6ab488cfdb39", "b820f925-e189-4553-a7d1-8e5f2750fe08"),
    ("c1ef0e8b-4666-4d8c-a77f-6ab488cfdb39", "906d2d0a-7a6d-4ecc-b574-ca2154a70bca"),
    ("c1ef0e8b-4666-4d8c-a77f-6ab488cfdb39", "3dc1c51b-5ff2-456d-ad2a-055e78ba2b03"),
    ("cdb7e1bc-f7c5-425c-8248-aa83dbb6919f", "45b5abe1-a6e1-4833-a9cb-7eb0c408dba3"),
    ("cdb7e1bc-f7c5-425c-8248-aa83dbb6919f", "06f2b1bc-7f44-4368-a564-207658af552d"),
    ("cdb7e1bc-f7c5-425c-8248-aa83dbb6919f", "0c023f96-5137-48cf-8682-8dd30bbc81be"),
    ("cdb7e1bc-f7c5-425c-8248-aa83dbb6919f", "6bafc43c-6080-4541-bfc2-c2608b269ca0"),
    ("cdb7e1bc-f7c5-425c-8248-aa83dbb6919f", "4903400b-731d-42b0-98c7-6d50fc504894"),
    ("6ad419a5-f0ce-47c2-a52a-91685fa86a31", "3c452f0d-715e-43b5-a140-3e26f73dec76"),
    ("6ad419a5-f0ce-47c2-a52a-91685fa86a31", "eddd61f7-d595-4370-b9c3-49c4c6178096"),
    ("cd909627-82e5-40c9-b313-1a8fd2d7b119", "d67d0790-4b26-447b-82eb-e9642f66057c")
]

BASE_URL = "https://openapi.ls-sec.co.kr/api/apis/guide"
# Keep only first 5 items from api_list
api_list = api_list[:5]
def fetch_data():
    for group_id, api_id in api_list:
        print(f"\n{'='*80}")
        print(f"▶ Processing API_ID: {api_id} (Group: {group_id})")
        
        # 2. TR 가이드 정보 가져오기
        tr_url = f"{BASE_URL}/tr/{api_id}"
        try:
            tr_response = requests.get(tr_url)
            tr_response.raise_for_status()
            tr_data_list = tr_response.json() # 결과가 리스트 형태임
            
            for tr_item in tr_data_list:
                tr_internal_id = tr_item.get("id")
                tr_name = tr_item.get("trName")
                tr_code = tr_item.get("trCode")
                
                print(f"\n  [TR 정보]")
                print(f"  - TR Name: {tr_name}")
                print(f"  - TR Code: {tr_code}")
                print(f"  - Internal ID: {tr_internal_id}")
                
                # 3. TR Property(속성) 정보 가져오기
                if tr_internal_id:
                    prop_url = f"{BASE_URL}/tr/property/{tr_internal_id}"
                    prop_response = requests.get(prop_url)
                    prop_response.raise_for_status()
                    prop_data = prop_response.json()
                    
                    print(f"  [Property 상세 데이터]")
                    print(json.dumps(prop_data, indent=2, ensure_ascii=False))
                
                # 서버 부하 방지를 위한 미세 지연 (필요 시 조절)
                time.sleep(0.1)

        except requests.exceptions.RequestException as e:
            print(f"  [Error] Failed to fetch data for api_id {api_id}: {e}")
        except json.JSONDecodeError:
            print(f"  [Error] Failed to decode JSON for api_id {api_id}")

if __name__ == "__main__":
    fetch_data()