import datetime
from fastapi import APIRouter
from typing import List
from backend.core.logger import get_logger
from backend.domains.kiwoom.kiwoom_service import get_kiwoom_api
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomApiHelper, KiwoomRequest
from backend.domains.settings.settings_keys import SettingsKey
from backend.domains.settings.settings_service import get_settings_service
from backend.domains.settings.settings_model import SettingInfo
from backend.domains.stocks.stk_info_service import get_stk_info_service
from backend.domains.stocks.stk_info_model import StkInfoBulkCreate, StkInfoCreate
from backend.utils.kiwi_utils import is_time_exceeded

# APIRouter 인스턴스 생성
router = APIRouter()
logger = get_logger(__name__)

@router.get("/", response_model=List[SettingInfo])
async def get_all_settings():
    """모든 설정값 목록 조회"""
    settings_service = get_settings_service()
    return await settings_service.list_all()

@router.get("/{setting_key}")
async def get_setting(setting_key: str):
    """특정 설정값 조회"""
    settings_service = get_settings_service()
    value = await settings_service.get(setting_key)
    if value is None:
        return {"key": setting_key, "value": None, "exists": False}
    return {"key": setting_key, "value": value, "exists": True}


@router.put("/stk_info")
async def update_stk_info(force: bool = False):
    '''
    stk_info table을 채운다.
    force가 false일 경우
    LAST_STK_INFO_FILL 을 settings에서 찾아서 1. 없으면 또는 2. 1달이상 시간이 경과시  kiwoom에서 가져온다.
    force가 true이면 
    kiwoom(api ka10099)에서 가져온다. 
    '''
    logger.info(f"Received request to update stk_info, force={force}")
    # settings 에서 LAST_STK_INFO_FILL 을 찾아서
    settings_service = get_settings_service()
    last_fill_time = await settings_service.get(SettingsKey.LAST_STK_INFO_FILL)
    #  유효시간이 지났거나, force이면
    if not last_fill_time or (not force and is_time_exceeded(last_fill_time)) or force:
        # kiwoom에서 가져온다.
        api = await get_kiwoom_api()
        # 0:코스피,10:코스닥,3:ELW,8:ETF,30:K-OTC,50:코넥스,5:신주인수권,4:뮤추얼펀드,6:리츠,9:하이일드
        mrkt_types = ["0", "10", "3"]
        results = []
        for mrkt_tp in mrkt_types:
            response = await api.send_request(KiwoomRequest(api_id="ka10099", payload={"mrkt_tp": mrkt_tp}))
            if response.success:
                # 성공적으로 데이터를 가져온 경우
                results.extend(response.data.get("list", []))
            else:
                logger.error(f"Failed to fetch stock info for market type {mrkt_tp}: {response.error_message}")
        if results:
            stk_info_service = get_stk_info_service()
            await stk_info_service.delete_all()
            logger.info("stk_info 테이블의 레코드를 모두 삭제함")
            
            # results 리스트를 StkInfoCreate 객체들로 변환
            stk_info_list = []
            for item in results:
                try:
                    stk_info = StkInfoCreate(
                        code=item.get('code', ''),
                        name=item.get('name', ''),
                        list_count=item.get('listCount', ''),
                        audit_info=item.get('auditInfo', ''),
                        reg_day=item.get('regDay', ''),
                        last_price=item.get('lastPrice', ''),
                        state=item.get('state', ''),
                        market_code=item.get('marketCode', ''),
                        market_name=item.get('marketName', ''),
                        up_name=item.get('upName', ''),
                        up_size_name=item.get('upSizeName', ''),
                        company_class_name=item.get('companyClassName', ''),
                        order_warning=item.get('orderWarning', '0'),
                        nxt_enable=item.get('nxtEnable', 'N')
                    )
                    stk_info_list.append(stk_info)
                except Exception as e:
                    logger.error(f"종목 정보 변환 실패: {item}, 오류: {e}")
                    continue
            
            # StkInfoBulkCreate 객체 생성
            bulk_data = StkInfoBulkCreate(stocks=stk_info_list, overwrite=True)

            # 대량 생성 실행
            success_count, error_count = await stk_info_service.bulk_create(bulk_data)
            logger.info(f"종목 정보 저장 완료 - 성공: {success_count}, 실패: {error_count}")
            
            await settings_service.set(SettingsKey.LAST_STK_INFO_FILL, datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
            logger.info("LAST_STK_INFO_FILL 설정값을 현재 시각으로 업데이트함")

    return KiwoomApiHelper.create_success_response(data={"message": "stk_info 업데이트 작업이 완료되었습니다."})