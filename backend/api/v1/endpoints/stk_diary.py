from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from backend.domains.stocks.stk_diary_model import StkDiaryCreate, StkDiaryUpdate, StkDiaryResponse, StkDiaryFilter
from backend.domains.stocks.stk_diary_service import get_stk_diary_service, StkDiaryService
from backend.core.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()

@router.post("/", response_model=StkDiaryResponse)
async def create_diary(
    diary_data: StkDiaryCreate,
    diary_service: StkDiaryService = Depends(get_stk_diary_service)
):
    """새로운 주식 일지 생성"""
    try:
        diary = await diary_service.create(diary_data)
        return StkDiaryResponse(**diary.__dict__)
    except Exception as e:
        logger.error(f"Error creating diary: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{diary_id}", response_model=StkDiaryResponse)
async def get_diary(
    diary_id: int,
    diary_service: StkDiaryService = Depends(get_stk_diary_service)
):
    """ID로 일지 조회"""
    try:
        diary = await diary_service.get_by_id(diary_id)
        if not diary:
            raise HTTPException(status_code=404, detail=f"Diary {diary_id} not found")
        
        return StkDiaryResponse(**diary.__dict__)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting diary {diary_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{diary_id}", response_model=StkDiaryResponse)
async def update_diary(
    diary_id: int,
    update_data: StkDiaryUpdate,
    diary_service: StkDiaryService = Depends(get_stk_diary_service)
):
    """일지 수정"""
    try:
        diary = await diary_service.update(diary_id, update_data)
        if not diary:
            raise HTTPException(status_code=404, detail=f"Diary {diary_id} not found")
        
        return StkDiaryResponse(**diary.__dict__)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating diary {diary_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{diary_id}")
async def delete_diary(
    diary_id: int,
    diary_service: StkDiaryService = Depends(get_stk_diary_service)
):
    """일지 삭제"""
    try:
        success = await diary_service.delete(diary_id)
        if not success:
            raise HTTPException(status_code=404, detail=f"Diary {diary_id} not found")
        
        return {"message": f"Diary {diary_id} deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting diary {diary_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[StkDiaryResponse])
async def list_diaries(
    ymd_from: Optional[str] = Query(None, description="시작 날짜 (YYYYMMDD)"),
    ymd_to: Optional[str] = Query(None, description="종료 날짜 (YYYYMMDD)"),
    stk_cd: Optional[str] = Query(None, description="종목코드 필터"),
    note_like: Optional[str] = Query(None, description="일지 내용 검색어"),
    diary_service: StkDiaryService = Depends(get_stk_diary_service)
):
    """일지 목록 조회 (필터링 지원)"""
    try:
        filter_data = StkDiaryFilter(
            ymd_from=ymd_from,
            ymd_to=ymd_to,
            stk_cd=stk_cd,
            note_like=note_like
        )
        
        diaries = await diary_service.list_all(filter_data)
        return [StkDiaryResponse(**diary.__dict__) for diary in diaries]
    except Exception as e:
        logger.error(f"Error listing diaries: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/date/{ymd}", response_model=List[StkDiaryResponse])
async def get_diaries_by_date(
    ymd: str,
    diary_service: StkDiaryService = Depends(get_stk_diary_service)
):
    """특정 날짜의 일지 목록"""
    try:
        diaries = await diary_service.get_by_date(ymd)
        return [StkDiaryResponse(**diary.__dict__) for diary in diaries]
    except Exception as e:
        logger.error(f"Error getting diaries by date {ymd}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stock/{stk_cd}", response_model=List[StkDiaryResponse])
async def get_diaries_by_stock(
    stk_cd: str,
    diary_service: StkDiaryService = Depends(get_stk_diary_service)
):
    """특정 종목의 일지 목록"""
    try:
        diaries = await diary_service.get_by_stock(stk_cd)
        return [StkDiaryResponse(**diary.__dict__) for diary in diaries]
    except Exception as e:
        logger.error(f"Error getting diaries by stock {stk_cd}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search/content", response_model=List[StkDiaryResponse])
async def search_diaries_by_content(
    keyword: str = Query(..., description="검색할 키워드"),
    diary_service: StkDiaryService = Depends(get_stk_diary_service)
):
    """일지 내용으로 검색"""
    try:
        diaries = await diary_service.search_by_content(keyword)
        return [StkDiaryResponse(**diary.__dict__) for diary in diaries]
    except Exception as e:
        logger.error(f"Error searching diaries by content '{keyword}': {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/date-range/{start_date}/{end_date}", response_model=List[StkDiaryResponse])
async def get_diaries_by_date_range(
    start_date: str,
    end_date: str,
    diary_service: StkDiaryService = Depends(get_stk_diary_service)
):
    """날짜 범위로 일지 조회"""
    try:
        diaries = await diary_service.get_date_range(start_date, end_date)
        return [StkDiaryResponse(**diary.__dict__) for diary in diaries]
    except Exception as e:
        logger.error(f"Error getting diaries by date range {start_date}-{end_date}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stats/summary")
async def get_diary_stats(
    diary_service: StkDiaryService = Depends(get_stk_diary_service)
):
    """일지 통계 정보"""
    try:
        stats = await diary_service.get_stats()
        return {
            "total_diaries": stats["total"],
            "diaries_with_stock": stats["with_stock"],
            "general_diaries": stats["general"],
            "message": f"총 {stats['total']}개 일지 (종목별: {stats['with_stock']}, 전체: {stats['general']})"
        }
    except Exception as e:
        logger.error(f"Error getting diary stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))
