import asyncio
import os
import sys
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.core.logger import get_logger
from backend.domains.stkcompanys.kiwoom.kiwoom_service import get_kiwoom_api
from backend.domains.stkcompanys.kiwoom.models.kiwoom_schema import KiwoomRequest, KiwoomApiHelper

logger = get_logger(__name__)

async def main():
    kiwoom = await get_kiwoom_api()
    if not kiwoom:
        logger.error("Kiwoom API creation failed")
        return

    # ka10086: 일별주가요청
    api_id = "ka10086"
    
    # 삼성전자(005930), 어제 날짜 기준 조회
    # 실제로는 장이 열린 날짜여야 데이터가 확실함. 
    # 테스트를 위해 최근 날짜 입력
    target_date = datetime.now().strftime("%Y%m%d")
    # target_date = '20260126'
    payload = {
        "stk_cd": "005930",
        "qry_dt": target_date,
        "indc_tp": "1" 
    }

    logger.info(f"Testing Kiwoom API: {api_id} with payload {payload}")

    request = KiwoomRequest(api_id=api_id, payload=payload)
    
    # Validate payload locally if possible (optional but good practice)
    validation_errors = request.validate_payload()
    if validation_errors:
        logger.error(f"Validation failed: {validation_errors}")
        return

    response = await kiwoom.send_request(request)

    if response.success:
        if response.data:
            korea_data = KiwoomApiHelper.to_korea_data(response.data, api_id)
            print(json.dumps(korea_data, ensure_ascii=False, indent=2))
        else:
            print("Success but no data")
    else:
        print(f"Failed: {response.error_code} - {response.error_message}")

if __name__ == "__main__":
    asyncio.run(main())
