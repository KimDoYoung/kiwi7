from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from backend.domains.stocks.my_stock_model import MyStockCreate, MyStockUpdate, MyStockResponse, MyStockFilter
from backend.domains.stocks.my_stock_service import get_my_stock_service, MyStockService
from backend.core.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()

@router.post("/", response_model=MyStockResponse)
async def create_stock(
    stock_data: MyStockCreate,
    my_stock_service: MyStockService = Depends(get_my_stock_service)
):
    """새로운 종목 추가"""
    try:
        # 중복 종목코드 확인
        existing = await my_stock_service.get_by_code(stock_data.stk_cd)
        if existing:
            raise HTTPException(status_code=400, detail=f"Stock code {stock_data.stk_cd} already exists")
        
        stock = await my_stock_service.create(stock_data)
        return MyStockResponse(**stock.__dict__)
    except Exception as e:
        logger.error(f"Error creating stock: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{stk_cd}", response_model=MyStockResponse)
async def get_stock(
    stk_cd: str,
    my_stock_service: MyStockService = Depends(get_my_stock_service)
):
    """종목코드로 종목 조회"""
    try:
        stock = await my_stock_service.get_by_code(stk_cd)
        if not stock:
            raise HTTPException(status_code=404, detail=f"Stock {stk_cd} not found")
        
        return MyStockResponse(**stock.__dict__)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting stock {stk_cd}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{stk_cd}", response_model=MyStockResponse)
async def update_stock(
    stk_cd: str,
    update_data: MyStockUpdate,
    my_stock_service: MyStockService = Depends(get_my_stock_service)
):
    """종목 정보 수정"""
    try:
        stock = await my_stock_service.update(stk_cd, update_data)
        if not stock:
            raise HTTPException(status_code=404, detail=f"Stock {stk_cd} not found")
        
        return MyStockResponse(**stock.__dict__)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating stock {stk_cd}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{stk_cd}")
async def delete_stock(
    stk_cd: str,
    my_stock_service: MyStockService = Depends(get_my_stock_service)
):
    """종목 삭제"""
    try:
        success = await my_stock_service.delete(stk_cd)
        if not success:
            raise HTTPException(status_code=404, detail=f"Stock {stk_cd} not found")
        
        return {"message": f"Stock {stk_cd} deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting stock {stk_cd}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[MyStockResponse])
async def list_stocks(
    is_hold: Optional[int] = Query(None, description="보유 여부 (1: 보유, 0: 미보유)"),
    is_watch: Optional[int] = Query(None, description="관심 여부 (1: 관심, 0: 비관심)"),
    sector: Optional[str] = Query(None, description="섹터 필터"),
    stk_nm_like: Optional[str] = Query(None, description="종목명 검색어"),
    my_stock_service: MyStockService = Depends(get_my_stock_service)
):
    """종목 목록 조회 (필터링 지원)"""
    try:
        filter_data = MyStockFilter(
            is_hold=is_hold,
            is_watch=is_watch,
            sector=sector,
            stk_nm_like=stk_nm_like
        )
        
        stocks = await my_stock_service.list_all(filter_data)
        return [MyStockResponse(**stock.__dict__) for stock in stocks]
    except Exception as e:
        logger.error(f"Error listing stocks: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/holding/list", response_model=List[MyStockResponse])
async def get_holding_stocks(
    my_stock_service: MyStockService = Depends(get_my_stock_service)
):
    """보유 종목 목록"""
    try:
        stocks = await my_stock_service.get_holding_stocks()
        return [MyStockResponse(**stock.__dict__) for stock in stocks]
    except Exception as e:
        logger.error(f"Error getting holding stocks: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/watching/list", response_model=List[MyStockResponse])
async def get_watching_stocks(
    my_stock_service: MyStockService = Depends(get_my_stock_service)
):
    """관심 종목 목록"""
    try:
        stocks = await my_stock_service.get_watching_stocks()
        return [MyStockResponse(**stock.__dict__) for stock in stocks]
    except Exception as e:
        logger.error(f"Error getting watching stocks: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/{stk_cd}/hold", response_model=MyStockResponse)
async def set_hold_status(
    stk_cd: str,
    is_hold: bool,
    my_stock_service: MyStockService = Depends(get_my_stock_service)
):
    """보유 상태 변경"""
    try:
        stock = await my_stock_service.set_hold_status(stk_cd, is_hold)
        if not stock:
            raise HTTPException(status_code=404, detail=f"Stock {stk_cd} not found")
        
        return MyStockResponse(**stock.__dict__)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error setting hold status for {stk_cd}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/{stk_cd}/watch", response_model=MyStockResponse)
async def set_watch_status(
    stk_cd: str,
    is_watch: bool,
    my_stock_service: MyStockService = Depends(get_my_stock_service)
):
    """관심 상태 변경"""
    try:
        stock = await my_stock_service.set_watch_status(stk_cd, is_watch)
        if not stock:
            raise HTTPException(status_code=404, detail=f"Stock {stk_cd} not found")
        
        return MyStockResponse(**stock.__dict__)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error setting watch status for {stk_cd}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search/name", response_model=List[MyStockResponse])
async def search_stocks_by_name(
    name: str = Query(..., description="검색할 종목명"),
    my_stock_service: MyStockService = Depends(get_my_stock_service)
):
    """종목명으로 검색"""
    try:
        stocks = await my_stock_service.search_by_name(name)
        return [MyStockResponse(**stock.__dict__) for stock in stocks]
    except Exception as e:
        logger.error(f"Error searching stocks by name '{name}': {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/sectors/list", response_model=List[str])
async def get_sectors(
    my_stock_service: MyStockService = Depends(get_my_stock_service)
):
    """등록된 섹터 목록"""
    try:
        sectors = await my_stock_service.get_sectors()
        return sectors
    except Exception as e:
        logger.error(f"Error getting sectors: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stats/summary")
async def get_stats(
    my_stock_service: MyStockService = Depends(get_my_stock_service)
):
    """통계 정보"""
    try:
        stats = await my_stock_service.get_stats()
        return {
            "total_stocks": stats["total"],
            "holding_stocks": stats["holding"],
            "watching_stocks": stats["watching"],
            "message": f"총 {stats['total']}종목 (보유: {stats['holding']}, 관심: {stats['watching']})"
        }
    except Exception as e:
        logger.error(f"Error getting stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))
