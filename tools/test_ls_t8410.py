import asyncio
import os
import sys
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.core.logger import get_logger
from backend.domains.stkcompanys.ls.ls_service import get_ls_api
from backend.domains.stkcompanys.ls.models.ls_schema import LsRequest, LsApiHelper

logger = get_logger(__name__)

async def main():
    ls = await get_ls_api()
    if not ls:
        logger.error("LS API creation failed")
        return

    # t8410: API전용주식차트(일주월년)
    api_id = "t8410"
    
    target_date = datetime.now().strftime("%Y%m%d")

    payload = {
        "shcode": "005930",
        "gubun": "2",      # 2:일, 3:주, 4:월, 5:년
        "qrycnt": "1",     # 최근 1건
        "sdate": " ",      # 종료일 (Space: 최신) -> Not sure if this means start/end logic inverted or just end date
        "edate": target_date, # 기준일
        "cts_date": " ",
        "comp_yn": "N",
        "sujung": "N"
    }
    
    # If sdate/edate logic is different (e.g. sdate=start, edate=end), I might need to adjust.
    # But description said: sdate: 조회구간종료일, edate: 처음조회기준일.
    # Usually: request from edate backwards for qrycnt. 
    # So edate=target_date, qrycnt=1 should return target_date's data.

    logger.info(f"Testing LS API: {api_id} with payload {payload}")

    request = LsRequest(api_id=api_id, payload=payload)
    
    validation_errors = request.validate_payload()
    if validation_errors:
        logger.error(f"Validation failed: {validation_errors}")
        return

    response = await ls.send_request(request)

    if response.success:
        if response.data:
            korea_data = LsApiHelper.to_korea_data(response.data, api_id)
            print(json.dumps(korea_data, ensure_ascii=False, indent=2))
        else:
            print("Success but no data")
    else:
        print(f"Failed: {response.error_code} - {response.error_message}")

if __name__ == "__main__":
    asyncio.run(main())
