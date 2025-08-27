
import json
from backend.api.common.validators import validate_market_type
from backend.domains.kiwoom.kiwoom_service import get_kiwoom_api
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomApiHelper, KiwoomRequest
from backend.domains.services.dependency import get_service
from backend.domains.services.settings_keys import SettingsKey
from backend.domains.models.stk_info_model import StkInfoBulkCreate, StkInfoCreate
# from backend.domains.services.stk_info_service import get_stk_info_service
from backend.utils.kiwi_utils import get_current_timestamp, is_time_exceeded, to_dict, to_str
from backend.core.logger import get_logger

logger = get_logger(__name__)

async def stk_info_fill(force:bool=False):
    """ 
    stk_info 테이블을 채운다. 
    만약 force가 True이면 무조건 채운다. 
    모두 지우고 채운다.
    force가 False이면  settings테이블의 LAST_STK_INFO_FILL을 체크해서 일정시간이 지났다면 채운다.
    """
    # settings 에서 LAST_STK_INFO_FILL 을 찾아서
    settings_service = get_service("settings")
    last_fill_time = await settings_service.get(SettingsKey.LAST_STK_INFO_FILL)
    #  유효시간이 지났거나, force이면
    if not last_fill_time or (not force and is_time_exceeded(last_fill_time)) or force:
        # kiwoom에서 가져온다.
        api = await get_kiwoom_api()
        # 0:코스피,10:코스닥,3:ELW,8:ETF,30:K-OTC,50:코넥스,5:신주인수권,4:뮤추얼펀드,6:리츠,9:하이일드
        mrkt_types = ["0", "10", "3"]
        results = []
        for mrkt_tp in mrkt_types:
            if not validate_market_type(mrkt_tp):
                return KiwoomApiHelper.create_error_response(error_code="999", error_message=f"유효하지 않은 시장 타입: {mrkt_tp}")
            response = await api.send_request(KiwoomRequest(api_id="ka10099", payload={"mrkt_tp": mrkt_tp}))
            if response.success:
                # 성공적으로 데이터를 가져온 경우
                results.extend(response.data.get("list", []))
            else:
                logger.error(f"Failed to fetch stock info for market type {mrkt_tp}: {response.error_message}")
        if results:
            stk_info_service = get_service("stk_info")
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
            
            # 타임스탬프 업데이트
            await settings_service.set(
                SettingsKey.LAST_STK_INFO_FILL, 
                get_current_timestamp()
            )
            logger.info("LAST_STK_INFO_FILL 타임스탬프 업데이트 완료")

async def get_stock_name(stk_code: str) -> str:
    ''' stk_code로 stk_name을 구한다. stk_info테이블에서 구하고 없으면 api로 구함'''
    stk_info_service = get_service("stk_info")
    stk_info = await stk_info_service.get_by_code(stk_code)
    if stk_info and stk_info.name:
        return stk_info.name
    else:
        api = await get_kiwoom_api()
        api_response = await api.send_request(KiwoomRequest(api_id="ka10001", payload={"stk_cd": stk_code}))
        if api_response.success and api_response.data:
            name = api_response.data.get("stk_nm", "")
            if name:
                return name
            else:
                logger.error(f"get_stock_name 함수에서 ka10001 요청은 성공했으나 이름이 없음: {stk_code}")
    return None

async def fetch_stk_info(stk_code_list):
    ''' 
    stk_code_list를 받아서 종목정보조회ka10100을 호출해서 모은 후 리스트로 리턴
    캐시에서 먼저 찾고, 없으면 API 호출
    '''
    api_id = "ka10100"
    cache_service = get_service("stk_cache")
    api = await get_kiwoom_api()
    results = []
    for stk_cd in stk_code_list:
        cached_data = await cache_service.get_by_stock_and_name(stk_cd,f"stk_info_{api_id}")
        if cached_data:
            try:
                cached_value = to_dict(cached_data.value)
                results.append(cached_value)
                continue
            except (json.JSONDecodeError, TypeError) as e:
                logger.error(f"fetch_stk_info함수 내에서 decode 실패 code: {stk_cd}: {e}")
                await cache_service.delete(cached_data.id) # 삭제

        response = await api.send_request(KiwoomRequest(api_id="ka10100", payload={"stk_cd": stk_cd}))
        if response.success:
            # 결과 추가 및 캐시 저장
            korea_data = KiwoomApiHelper.to_korea_data(response.data, api_id)
            results.append(korea_data)
            await cache_service.upsert(stk_cd, f"stk_info_{api_id}", to_str(korea_data))
        else:
            logger.error(f"fetch_stk_info 함수에서 {stk_cd}로 ka10100 요청 실패: {response.error_message}")
    return results