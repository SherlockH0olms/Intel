from fastapi import APIRouter, Query
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta
import random

router = APIRouter()

class SensorData(BaseModel):
    time: datetime
    machine_id: str
    sensor_name: str
    value: float
    unit: str

@router.get("/{machine_id}", response_model=List[SensorData])
async def get_sensor_data(
    machine_id: str,
    sensor_name: Optional[str] = None,
    limit: int = Query(100, le=1000)
):
    """Get sensor data for a machine"""
    # TODO: Implement database query
    sensors = ["temperature", "vibration", "speed", "pressure"]
    data = []
    
    for i in range(limit):
        for sensor in sensors:
            if sensor_name and sensor != sensor_name:
                continue
            data.append({
                "time": datetime.now() - timedelta(minutes=i),
                "machine_id": machine_id,
                "sensor_name": sensor,
                "value": random.uniform(50, 100),
                "unit": "°C" if sensor == "temperature" else "mm/s" if sensor == "vibration" else "RPM" if sensor == "speed" else "bar"
            })
    
    return data[:limit]

@router.post("/")
async def post_sensor_data(data: List[SensorData]):
    """Post sensor data (for protocols to use)"""
    # TODO: Implement database insert
    return {"message": f"Inserted {len(data)} sensor readings"}