import asyncio
import os
import sys
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.core.logger import get_logger
from backend.domains.stkcompanys.kis.kis_service import get_kis_api
from backend.domains.stkcompanys.kis.models.kis_schema import KisRequest, KisApiHelper

logger = get_logger(__name__)

async def main():
    kis = await get_kis_api()
    if not kis:
        logger.error("KIS API creation failed")
        return

    # FHKST01010400: 주식현재가 일자별 (Daily Price)
    # This returns the last 30 trading days. For specific date, you filter the result.
    api_id = "FHKST01010400"
    
    payload = {
        "FID_COND_MRKT_DIV_CODE": "J",
        "FID_INPUT_ISCD": "005930",
        "FID_PERIOD_DIV_CODE": "D", # 일별
        "FID_ORG_ADJ_PRC": "0"      # 수정주가 미반영
    }

    logger.info(f"Testing KIS API: {api_id} with payload {payload}")

    request = KisRequest(api_id=api_id, payload=payload)
    
    validation_errors = request.validate_payload()
    if validation_errors:
        logger.error(f"Validation failed: {validation_errors}")
        return

    response = await kis.send_request(request)

    if response.success:
        if response.data:
            korea_data = KisApiHelper.to_korea_data(response.data, api_id)
            print(json.dumps(korea_data, ensure_ascii=False, indent=2))
        else:
            print("Success but no data")
    else:
        print(f"Failed: {response.error_code} - {response.error_message}")

if __name__ == "__main__":
    asyncio.run(main())
