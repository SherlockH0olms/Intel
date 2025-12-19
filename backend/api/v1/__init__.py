"""API v1 package initialization"""
from fastapi import APIRouter

from .machines import router as machines_router
from .sensors import router as sensors_router
from .recommendations import router as recommendations_router
from .defects import router as defects_router
from .analytics import router as analytics_router

api_router = APIRouter()
api_router.include_router(machines_router, prefix="/machines", tags=["machines"])
api_router.include_router(sensors_router, prefix="/sensors", tags=["sensors"])
api_router.include_router(recommendations_router, prefix="/recommendations", tags=["recommendations"])
api_router.include_router(defects_router, prefix="/defects", tags=["defects"])
api_router.include_router(analytics_router, prefix="/analytics", tags=["analytics"])