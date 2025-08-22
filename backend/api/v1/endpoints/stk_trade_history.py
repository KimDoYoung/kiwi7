from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from backend.domains.stocks.stk_trade_history_model import StkTradeHistoryCreate, StkTradeHistoryUpdate, StkTradeHistoryResponse, StkTradeHistoryFilter
from backend.domains.stocks.stk_trade_history_service import get_stk_trade_history_service, StkTradeHistoryService
from backend.core.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()

@router.post("/", response_model=StkTradeHistoryResponse)
async def create_trade_history(
    trade_data: StkTradeHistoryCreate,
    trade_service: StkTradeHistoryService = Depends(get_stk_trade_history_service)
):
    """새로운 매매 이력 생성"""
    try:
        trade = await trade_service.create(trade_data)
        return StkTradeHistoryResponse(**trade.__dict__)
    except Exception as e:
        logger.error(f"Error creating trade history: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{trade_id}", response_model=StkTradeHistoryResponse)
async def get_trade_history(
    trade_id: int,
    trade_service: StkTradeHistoryService = Depends(get_stk_trade_history_service)
):
    """ID로 매매 이력 조회"""
    try:
        trade = await trade_service.get_by_id(trade_id)
        if not trade:
            raise HTTPException(status_code=404, detail=f"Trade history {trade_id} not found")
        
        return StkTradeHistoryResponse(**trade.__dict__)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting trade history {trade_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{trade_id}", response_model=StkTradeHistoryResponse)
async def update_trade_history(
    trade_id: int,
    update_data: StkTradeHistoryUpdate,
    trade_service: StkTradeHistoryService = Depends(get_stk_trade_history_service)
):
    """매매 이력 수정"""
    try:
        trade = await trade_service.update(trade_id, update_data)
        if not trade:
            raise HTTPException(status_code=404, detail=f"Trade history {trade_id} not found")
        
        return StkTradeHistoryResponse(**trade.__dict__)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating trade history {trade_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{trade_id}")
async def delete_trade_history(
    trade_id: int,
    trade_service: StkTradeHistoryService = Depends(get_stk_trade_history_service)
):
    """매매 이력 삭제"""
    try:
        success = await trade_service.delete(trade_id)
        if not success:
            raise HTTPException(status_code=404, detail=f"Trade history {trade_id} not found")
        
        return {"message": f"Trade history {trade_id} deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting trade history {trade_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[StkTradeHistoryResponse])
async def list_trade_histories(
    stk_cd: Optional[str] = Query(None, description="종목코드 필터"),
    ymd_from: Optional[str] = Query(None, description="시작 날짜 (YYYYMMDD)"),
    ymd_to: Optional[str] = Query(None, description="종료 날짜 (YYYYMMDD)"),
    stk_nm_like: Optional[str] = Query(None, description="종목명 검색어"),
    note_like: Optional[str] = Query(None, description="매매 기록 검색어"),
    trade_service: StkTradeHistoryService = Depends(get_stk_trade_history_service)
):
    """매매 이력 목록 조회 (필터링 지원)"""
    try:
        filter_data = StkTradeHistoryFilter(
            stk_cd=stk_cd,
            ymd_from=ymd_from,
            ymd_to=ymd_to,
            stk_nm_like=stk_nm_like,
            note_like=note_like
        )
        
        trades = await trade_service.list_all(filter_data)
        return [StkTradeHistoryResponse(**trade.__dict__) for trade in trades]
    except Exception as e:
        logger.error(f"Error listing trade histories: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stock/{stk_cd}", response_model=List[StkTradeHistoryResponse])
async def get_trade_histories_by_stock(
    stk_cd: str,
    trade_service: StkTradeHistoryService = Depends(get_stk_trade_history_service)
):
    """특정 종목의 매매 이력"""
    try:
        trades = await trade_service.get_by_stock(stk_cd)
        return [StkTradeHistoryResponse(**trade.__dict__) for trade in trades]
    except Exception as e:
        logger.error(f"Error getting trade histories by stock {stk_cd}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/date/{ymd}", response_model=List[StkTradeHistoryResponse])
async def get_trade_histories_by_date(
    ymd: str,
    trade_service: StkTradeHistoryService = Depends(get_stk_trade_history_service)
):
    """특정 날짜의 매매 이력"""
    try:
        trades = await trade_service.get_by_date(ymd)
        return [StkTradeHistoryResponse(**trade.__dict__) for trade in trades]
    except Exception as e:
        logger.error(f"Error getting trade histories by date {ymd}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/date-range/{start_date}/{end_date}", response_model=List[StkTradeHistoryResponse])
async def get_trade_histories_by_date_range(
    start_date: str,
    end_date: str,
    trade_service: StkTradeHistoryService = Depends(get_stk_trade_history_service)
):
    """날짜 범위로 매매 이력 조회"""
    try:
        trades = await trade_service.get_date_range(start_date, end_date)
        return [StkTradeHistoryResponse(**trade.__dict__) for trade in trades]
    except Exception as e:
        logger.error(f"Error getting trade histories by date range {start_date}-{end_date}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search/stock-name", response_model=List[StkTradeHistoryResponse])
async def search_trade_histories_by_stock_name(
    stock_name: str = Query(..., description="검색할 종목명"),
    trade_service: StkTradeHistoryService = Depends(get_stk_trade_history_service)
):
    """종목명으로 매매 이력 검색"""
    try:
        trades = await trade_service.search_by_stock_name(stock_name)
        return [StkTradeHistoryResponse(**trade.__dict__) for trade in trades]
    except Exception as e:
        logger.error(f"Error searching trade histories by stock name '{stock_name}': {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search/note", response_model=List[StkTradeHistoryResponse])
async def search_trade_histories_by_note(
    keyword: str = Query(..., description="검색할 키워드"),
    trade_service: StkTradeHistoryService = Depends(get_stk_trade_history_service)
):
    """매매 기록 내용으로 검색"""
    try:
        trades = await trade_service.search_by_note(keyword)
        return [StkTradeHistoryResponse(**trade.__dict__) for trade in trades]
    except Exception as e:
        logger.error(f"Error searching trade histories by note '{keyword}': {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stats/summary")
async def get_trade_stats(
    trade_service: StkTradeHistoryService = Depends(get_stk_trade_history_service)
):
    """매매 이력 통계 정보"""
    try:
        stats = await trade_service.get_stats()
        return {
            "total_trades": stats["total_trades"],
            "unique_stocks": stats["unique_stocks"],
            "latest_trade_date": stats["latest_trade_date"],
            "earliest_trade_date": stats["earliest_trade_date"],
            "message": f"총 {stats['total_trades']}건 매매 ({stats['unique_stocks']}개 종목)"
        }
    except Exception as e:
        logger.error(f"Error getting trade stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stats/stock/{stk_cd}")
async def get_stock_trade_summary(
    stk_cd: str,
    trade_service: StkTradeHistoryService = Depends(get_stk_trade_history_service)
):
    """특정 종목의 매매 요약 정보"""
    try:
        summary = await trade_service.get_stock_trade_summary(stk_cd)
        return {
            "stock_code": summary["stk_cd"],
            "stock_name": summary["stk_nm"],
            "trade_count": summary["trade_count"],
            "latest_trade_date": summary["latest_trade_date"],
            "earliest_trade_date": summary["earliest_trade_date"],
            "message": f"{summary['stk_nm']}({summary['stk_cd']}) 총 {summary['trade_count']}건 매매"
        }
    except Exception as e:
        logger.error(f"Error getting stock trade summary for {stk_cd}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
