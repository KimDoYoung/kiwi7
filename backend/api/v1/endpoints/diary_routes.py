"""
주식 일지(stk_diary) 관련 API 엔드포인트
"""
from fastapi import APIRouter

from backend.core.logger import get_logger
from backend.domains.kiwoom.models.kiwoom_schema import KiwoomApiHelper, KiwoomRequest, KiwoomResponse
from backend.domains.models.stk_diary_model import StkDiaryFilter
from backend.domains.services.dependency import get_service

logger = get_logger(__name__)

router = APIRouter()

@router.post("/", response_model=KiwoomResponse)
async def create_diary(request: KiwoomRequest):
    """주식 일지 생성
    
    Request payload 예시:
    {
        "ymd": "20240828",
        "stk_cd": "005930", 
        "note": "삼성전자에 대한 분석..."
    }
    """
    logger.info(f"주식 일지 생성 요청: {request}")
    
    try:
        # payload에서 데이터 추출
        ymd = request.payload.get("ymd", "")
        stk_cd = request.payload.get("stk_cd", None)
        note = request.payload.get("note", "")
        
        # 입력 데이터 검증
        if not ymd or len(ymd) != 8:
            return KiwoomApiHelper.create_error_response(
                error_code="INVALID_DATE",
                error_message="날짜는 YYYYMMDD 형식의 8자리여야 합니다.",
                api_info={"api_id": "diary_create", "description": "주식 일지 생성"}
            )
        
        if not note or not note.strip():
            return KiwoomApiHelper.create_error_response(
                error_code="EMPTY_NOTE",
                error_message="일지 내용을 입력해주세요.",
                api_info={"api_id": "diary_create", "description": "주식 일지 생성"}
            )
        
        if stk_cd and len(stk_cd) != 6:
            return KiwoomApiHelper.create_error_response(
                error_code="INVALID_STOCK_CODE",
                error_message="종목코드는 6자리여야 합니다.",
                api_info={"api_id": "diary_create", "description": "주식 일지 생성"}
            )

        # 서비스를 통해 일지 저장
        service = get_service("stk_diary")
        
        from backend.domains.models.stk_diary_model import StkDiaryCreate
        diary_create = StkDiaryCreate(
            ymd=ymd,
            stk_cd=stk_cd,
            note=note.strip()
        )
        
        diary = await service.create(diary_create)
        
        logger.info(f"주식 일지 생성 완료: ID={diary.id}, 날짜={ymd}")
        
        return KiwoomApiHelper.create_success_response(
            data={
                "id": diary.id,
                "ymd": diary.ymd,
                "stk_cd": diary.stk_cd,
                "note": diary.note,
                "message": "주식 일지가 성공적으로 저장되었습니다."
            },
            api_info={"api_id": "diary_create", "description": "주식 일지 생성"}
        )
        
    except Exception as e:
        logger.error(f"주식 일지 생성 중 오류: {str(e)}")
        return KiwoomApiHelper.create_error_response(
            error_code="DIARY_CREATE_ERROR",
            error_message=f"주식 일지 저장 중 오류가 발생했습니다: {str(e)}",
            api_info={"api_id": "diary_create", "description": "주식 일지 생성"}
        )

@router.post("/list", response_model=KiwoomResponse)
async def get_diary_list(request : KiwoomRequest):
#     stk_cd: Optional[str] = Query(None, description="종목코드 필터"),
#     start_ymd: Optional[str] = Query(None, description="시작날짜 (YYYYMMDD)"),
#     end_ymd: Optional[str] = Query(None, description="종료날짜 (YYYYMMDD)"),
#     page: int = Query(1, description="페이지 번호"),
#     limit: int = Query(20, description="페이지당 항목 수")
# ):
    """주식 일지 목록 조회"""
    stk_cd = request.payload.get("stk_cd", None)
    start_ymd = request.payload.get("start_ymd", None)
    end_ymd = request.payload.get("end_ymd", None)
    page = request.payload.get("page", 1)
    limit = request.payload.get("limit", 20)
    logger.info(f"주식 일지 목록 조회: 종목코드={stk_cd}, 기간={start_ymd}~{end_ymd}, 페이지={page}")
    
    try:
        service = get_service("stk_diary")
        
        # 필터 조건 구성
        
        filter_data = StkDiaryFilter(
            ymd_from=start_ymd,
            ymd_to=end_ymd,
            stk_cd=stk_cd
        )
        
        # 데이터 조회 (전체 목록)
        all_diaries = await service.list_all(filter_data)
        
        # 페이징 처리
        total_count = len(all_diaries)
        start_idx = (page - 1) * limit
        end_idx = start_idx + limit
        paginated_diaries = all_diaries[start_idx:end_idx]
        
        # 딕셔너리 형태로 변환
        diary_list = []
        for diary in paginated_diaries:
            diary_list.append({
                "id": diary.id,
                "ymd": diary.ymd,
                "stk_cd": diary.stk_cd,
                "note": diary.note,
                "created_at": diary.created_at,
                "updated_at": diary.updated_at
            })
        
        # 응답 데이터 구성
        result_data = {
            "list": diary_list,
            "pagination": {
                "total": total_count,
                "page": page,
                "limit": limit,
                "total_pages": (total_count + limit - 1) // limit
            }
        }
        
        logger.info(f"주식 일지 목록 조회 완료: {len(diary_list)}개 항목 반환")
        
        return KiwoomApiHelper.create_success_response(
            data=result_data,
            api_info={"api_id": "diary_list", "description": "주식 일지 목록 조회"}
        )
        
    except Exception as e:
        logger.error(f"주식 일지 목록 조회 중 오류: {str(e)}")
        return KiwoomApiHelper.create_error_response(
            error_code="DIARY_LIST_ERROR",
            error_message=f"주식 일지 목록 조회 중 오류가 발생했습니다: {str(e)}",
            api_info={"api_id": "diary_list", "description": "주식 일지 목록 조회"}
        )

@router.get("/{diary_id}", response_model=KiwoomResponse)
async def get_diary(diary_id: int):
    """주식 일지 상세 조회"""
    logger.info(f"주식 일지 상세 조회: ID={diary_id}")
    
    try:
        service = get_service("stk_diary")
        diary = await service.get_by_id(diary_id)
        
        if not diary:
            return KiwoomApiHelper.create_error_response(
                error_code="DIARY_NOT_FOUND",
                error_message="주식 일지를 찾을 수 없습니다.",
                api_info={"api_id": "diary_get", "description": "주식 일지 상세 조회"}
            )
        
        diary_data = {
            "id": diary.id,
            "ymd": diary.ymd,
            "stk_cd": diary.stk_cd,
            "note": diary.note,
            "created_at": diary.created_at,
            "updated_at": diary.updated_at
        }
        
        logger.info(f"주식 일지 상세 조회 완료: ID={diary_id}")
        
        return KiwoomApiHelper.create_success_response(
            data=diary_data,
            api_info={"api_id": "diary_get", "description": "주식 일지 상세 조회"}
        )
        
    except Exception as e:
        logger.error(f"주식 일지 상세 조회 중 오류: {str(e)}")
        return KiwoomApiHelper.create_error_response(
            error_code="DIARY_GET_ERROR",
            error_message=f"주식 일지 조회 중 오류가 발생했습니다: {str(e)}",
            api_info={"api_id": "diary_get", "description": "주식 일지 상세 조회"}
        )

@router.put("/{diary_id}", response_model=KiwoomResponse)
async def update_diary(diary_id: int, request: KiwoomRequest):
    """주식 일지 수정
    
    Request payload 예시:
    {
        "ymd": "20240828",
        "stk_cd": "005930",
        "note": "수정된 내용..."
    }
    """
    logger.info(f"주식 일지 수정 요청: ID={diary_id}, request={request}")
    
    try:
        service = get_service("stk_diary")
        
        # 기존 일지 확인
        existing_diary = await service.get_by_id(diary_id)
        if not existing_diary:
            return KiwoomApiHelper.create_error_response(
                error_code="DIARY_NOT_FOUND",
                error_message="주식 일지를 찾을 수 없습니다.",
                api_info={"api_id": "diary_update", "description": "주식 일지 수정"}
            )
        
        # payload에서 데이터 추출
        ymd = request.payload.get("ymd", None)
        stk_cd = request.payload.get("stk_cd", None)
        note = request.payload.get("note", None)
        
        # 업데이트할 데이터 구성
        from backend.domains.models.stk_diary_model import StkDiaryUpdate
        
        update_data = StkDiaryUpdate()
        if ymd is not None:
            if len(ymd) != 8:
                return KiwoomApiHelper.create_error_response(
                    error_code="INVALID_DATE",
                    error_message="날짜는 YYYYMMDD 형식의 8자리여야 합니다.",
                    api_info={"api_id": "diary_update", "description": "주식 일지 수정"}
                )
            update_data.ymd = ymd
            
        if stk_cd is not None:
            if stk_cd and len(stk_cd) != 6:
                return KiwoomApiHelper.create_error_response(
                    error_code="INVALID_STOCK_CODE",
                    error_message="종목코드는 6자리여야 합니다.",
                    api_info={"api_id": "diary_update", "description": "주식 일지 수정"}
                )
            update_data.stk_cd = stk_cd
            
        if note is not None:
            if not note.strip():
                return KiwoomApiHelper.create_error_response(
                    error_code="EMPTY_NOTE",
                    error_message="일지 내용을 입력해주세요.",
                    api_info={"api_id": "diary_update", "description": "주식 일지 수정"}
                )
            update_data.note = note.strip()
        
        # 데이터 업데이트
        updated_diary = await service.update(diary_id, update_data)
        
        if not updated_diary:
            return KiwoomApiHelper.create_error_response(
                error_code="DIARY_UPDATE_FAILED",
                error_message="주식 일지 수정에 실패했습니다.",
                api_info={"api_id": "diary_update", "description": "주식 일지 수정"}
            )
        
        # 응답 데이터 구성
        response_data = {
            "id": updated_diary.id,
            "ymd": updated_diary.ymd,
            "stk_cd": updated_diary.stk_cd,
            "note": updated_diary.note,
            "created_at": updated_diary.created_at,
            "updated_at": updated_diary.updated_at,
            "message": "주식 일지가 성공적으로 수정되었습니다."
        }
        
        logger.info(f"주식 일지 수정 완료: ID={diary_id}")
        
        return KiwoomApiHelper.create_success_response(
            data=response_data,
            api_info={"api_id": "diary_update", "description": "주식 일지 수정"}
        )
        
    except Exception as e:
        logger.error(f"주식 일지 수정 중 오류: {str(e)}")
        return KiwoomApiHelper.create_error_response(
            error_code="DIARY_UPDATE_ERROR",
            error_message=f"주식 일지 수정 중 오류가 발생했습니다: {str(e)}",
            api_info={"api_id": "diary_update", "description": "주식 일지 수정"}
        )

@router.delete("/{diary_id}", response_model=KiwoomResponse)
async def delete_diary(diary_id: int):
    """주식 일지 삭제"""
    logger.info(f"주식 일지 삭제 요청: ID={diary_id}")
    
    try:
        service = get_service("stk_diary")
        
        # 기존 일지 확인
        existing_diary = await service.get_by_id(diary_id)
        if not existing_diary:
            return KiwoomApiHelper.create_error_response(
                error_code="DIARY_NOT_FOUND",
                error_message="주식 일지를 찾을 수 없습니다.",
                api_info={"api_id": "diary_delete", "description": "주식 일지 삭제"}
            )
        
        # 일지 삭제
        success = await service.delete(diary_id)
        
        if not success:
            return KiwoomApiHelper.create_error_response(
                error_code="DIARY_DELETE_FAILED",
                error_message="주식 일지 삭제에 실패했습니다.",
                api_info={"api_id": "diary_delete", "description": "주식 일지 삭제"}
            )
        
        logger.info(f"주식 일지 삭제 완료: ID={diary_id}")
        
        return KiwoomApiHelper.create_success_response(
            data={
                "deleted_id": diary_id,
                "message": "주식 일지가 성공적으로 삭제되었습니다."
            },
            api_info={"api_id": "diary_delete", "description": "주식 일지 삭제"}
        )
        
    except Exception as e:
        logger.error(f"주식 일지 삭제 중 오류: {str(e)}")
        return KiwoomApiHelper.create_error_response(
            error_code="DIARY_DELETE_ERROR",
            error_message=f"주식 일지 삭제 중 오류가 발생했습니다: {str(e)}",
            api_info={"api_id": "diary_delete", "description": "주식 일지 삭제"}
        ) 