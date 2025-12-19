from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime, timedelta
import random

router = APIRouter()

class AnalyticsMetrics(BaseModel):
    oee: float
    availability: float
    performance: float
    quality: float
    downtime_hours: float
    defect_rate: float
    maintenance_cost_savings: float

@router.get("/metrics")
async def get_metrics(machine_id: str = None):
    """Get analytics metrics"""
    return {
        "oee": 0.85,
        "availability": 0.92,
        "performance": 0.88,
        "quality": 0.95,
        "downtime_hours": 2.5,
        "defect_rate": 0.03,
        "maintenance_cost_savings": 12500.0
    }

@router.get("/timeline")
async def get_timeline(days: int = 7):
    """Get timeline data for charts"""
    timeline = []
    for i in range(days):
        timeline.append({
            "date": (datetime.now() - timedelta(days=i)).isoformat(),
            "oee": random.uniform(0.75, 0.95),
            "downtime": random.uniform(0, 5),
            "defects": random.randint(0, 10)
        })
    return timeline