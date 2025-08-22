from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from backend.domains.stocks.stk_cache_model import StkCacheCreate, StkCacheUpdate, StkCacheResponse, StkCacheFilter
from backend.domains.stocks.stk_cache_service import get_stk_cache_service, StkCacheService
from backend.core.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()

@router.post("/", response_model=StkCacheResponse)
async def create_cache(
    cache_data: StkCacheCreate,
    cache_service: StkCacheService = Depends(get_stk_cache_service)
):
    """새로운 캐시 데이터 생성"""
    try:
        cache = await cache_service.create(cache_data)
        return StkCacheResponse(**cache.__dict__)
    except Exception as e:
        logger.error(f"Error creating cache: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{cache_id}", response_model=StkCacheResponse)
async def get_cache(
    cache_id: int,
    cache_service: StkCacheService = Depends(get_stk_cache_service)
):
    """ID로 캐시 데이터 조회"""
    try:
        cache = await cache_service.get_by_id(cache_id)
        if not cache:
            raise HTTPException(status_code=404, detail=f"Cache {cache_id} not found")
        
        return StkCacheResponse(**cache.__dict__)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting cache {cache_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stock/{stk_cd}/name/{name}", response_model=StkCacheResponse)
async def get_cache_by_stock_and_name(
    stk_cd: str,
    name: str,
    cache_service: StkCacheService = Depends(get_stk_cache_service)
):
    """종목코드와 캐시명으로 조회 (최신 데이터)"""
    try:
        cache = await cache_service.get_by_stock_and_name(stk_cd, name)
        if not cache:
            raise HTTPException(status_code=404, detail=f"Cache for {stk_cd}/{name} not found")
        
        return StkCacheResponse(**cache.__dict__)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting cache by stock {stk_cd} and name {name}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{cache_id}", response_model=StkCacheResponse)
async def update_cache(
    cache_id: int,
    update_data: StkCacheUpdate,
    cache_service: StkCacheService = Depends(get_stk_cache_service)
):
    """캐시 데이터 수정"""
    try:
        cache = await cache_service.update(cache_id, update_data)
        if not cache:
            raise HTTPException(status_code=404, detail=f"Cache {cache_id} not found")
        
        return StkCacheResponse(**cache.__dict__)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating cache {cache_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/upsert/{stk_cd}/{name}", response_model=StkCacheResponse)
async def upsert_cache(
    stk_cd: str,
    name: str,
    value: str = Query(..., description="캐시 값"),
    cache_service: StkCacheService = Depends(get_stk_cache_service)
):
    """캐시 데이터 생성 또는 업데이트"""
    try:
        cache = await cache_service.upsert(stk_cd, name, value)
        return StkCacheResponse(**cache.__dict__)
    except Exception as e:
        logger.error(f"Error upserting cache {stk_cd}/{name}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{cache_id}")
async def delete_cache(
    cache_id: int,
    cache_service: StkCacheService = Depends(get_stk_cache_service)
):
    """캐시 데이터 삭제"""
    try:
        success = await cache_service.delete(cache_id)
        if not success:
            raise HTTPException(status_code=404, detail=f"Cache {cache_id} not found")
        
        return {"message": f"Cache {cache_id} deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting cache {cache_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[StkCacheResponse])
async def list_caches(
    stk_cd: Optional[str] = Query(None, description="종목코드 필터"),
    name: Optional[str] = Query(None, description="캐시명 필터"),
    name_like: Optional[str] = Query(None, description="캐시명 검색어"),
    value_like: Optional[str] = Query(None, description="캐시 값 검색어"),
    cache_service: StkCacheService = Depends(get_stk_cache_service)
):
    """캐시 데이터 목록 조회 (필터링 지원)"""
    try:
        filter_data = StkCacheFilter(
            stk_cd=stk_cd,
            name=name,
            name_like=name_like,
            value_like=value_like
        )
        
        caches = await cache_service.list_all(filter_data)
        return [StkCacheResponse(**cache.__dict__) for cache in caches]
    except Exception as e:
        logger.error(f"Error listing caches: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stock/{stk_cd}", response_model=List[StkCacheResponse])
async def get_caches_by_stock(
    stk_cd: str,
    cache_service: StkCacheService = Depends(get_stk_cache_service)
):
    """특정 종목의 모든 캐시 데이터"""
    try:
        caches = await cache_service.get_by_stock(stk_cd)
        return [StkCacheResponse(**cache.__dict__) for cache in caches]
    except Exception as e:
        logger.error(f"Error getting caches by stock {stk_cd}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/name/{name}", response_model=List[StkCacheResponse])
async def get_caches_by_name(
    name: str,
    cache_service: StkCacheService = Depends(get_stk_cache_service)
):
    """특정 캐시명의 모든 데이터"""
    try:
        caches = await cache_service.get_by_name(name)
        return [StkCacheResponse(**cache.__dict__) for cache in caches]
    except Exception as e:
        logger.error(f"Error getting caches by name {name}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/stock/{stk_cd}")
async def delete_caches_by_stock(
    stk_cd: str,
    cache_service: StkCacheService = Depends(get_stk_cache_service)
):
    """특정 종목의 모든 캐시 데이터 삭제"""
    try:
        deleted_count = await cache_service.delete_by_stock(stk_cd)
        return {"message": f"Deleted {deleted_count} cache entries for stock {stk_cd}"}
    except Exception as e:
        logger.error(f"Error deleting caches by stock {stk_cd}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/name/{name}")
async def delete_caches_by_name(
    name: str,
    cache_service: StkCacheService = Depends(get_stk_cache_service)
):
    """특정 캐시명의 모든 데이터 삭제"""
    try:
        deleted_count = await cache_service.delete_by_name(name)
        return {"message": f"Deleted {deleted_count} cache entries for name '{name}'"}
    except Exception as e:
        logger.error(f"Error deleting caches by name {name}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/meta/cache-names", response_model=List[str])
async def get_cache_names(
    cache_service: StkCacheService = Depends(get_stk_cache_service)
):
    """등록된 모든 캐시명 목록"""
    try:
        names = await cache_service.get_cache_names()
        return names
    except Exception as e:
        logger.error(f"Error getting cache names: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/meta/stock-codes", response_model=List[str])
async def get_stock_codes(
    cache_service: StkCacheService = Depends(get_stk_cache_service)
):
    """캐시된 모든 종목코드 목록"""
    try:
        codes = await cache_service.get_stock_codes()
        return codes
    except Exception as e:
        logger.error(f"Error getting stock codes: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stats/summary")
async def get_cache_stats(
    cache_service: StkCacheService = Depends(get_stk_cache_service)
):
    """캐시 데이터 통계 정보"""
    try:
        stats = await cache_service.get_stats()
        return {
            "total_cache_entries": stats["total_cache_entries"],
            "unique_stocks": stats["unique_stocks"],
            "unique_cache_names": stats["unique_cache_names"],
            "message": f"총 {stats['total_cache_entries']}개 캐시 ({stats['unique_stocks']}개 종목, {stats['unique_cache_names']}개 캐시명)"
        }
    except Exception as e:
        logger.error(f"Error getting cache stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))
