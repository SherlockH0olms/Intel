"""Sensor Data Processing Service"""
from typing import List, Dict
from datetime import datetime, timedelta
import numpy as np

class SensorService:
    def __init__(self):
        self.cache = {}
    
    async def process_sensor_data(self, data: List[Dict]) -> Dict:
        """Process incoming sensor data"""
        processed = {
            "total_records": len(data),
            "machines": set(),
            "sensors": set(),
            "timestamp": datetime.now().isoformat()
        }
        
        for record in data:
            processed["machines"].add(record.get("machine_id"))
            processed["sensors"].add(record.get("sensor_name"))
        
        processed["machines"] = list(processed["machines"])
        processed["sensors"] = list(processed["sensors"])
        
        return processed
    
    async def get_aggregated_data(self, 
                                   machine_id: str, 
                                   sensor_name: str,
                                   window: str = "1h") -> Dict:
        """Get aggregated sensor data"""
        # In production: query TimescaleDB with time_bucket
        # For demo:
        return {
            "machine_id": machine_id,
            "sensor_name": sensor_name,
            "window": window,
            "avg": 75.5,
            "min": 65.2,
            "max": 88.3,
            "stddev": 5.2,
            "count": 3600
        }
    
    async def detect_sensor_anomalies(self, 
                                       machine_id: str,
                                       sensor_name: str) -> List[Dict]:
        """Detect anomalies in sensor data"""
        # This will call MLService
        return []
    
    def calculate_statistics(self, values: List[float]) -> Dict:
        """Calculate statistical metrics"""
        arr = np.array(values)
        return {
            "mean": float(np.mean(arr)),
            "median": float(np.median(arr)),
            "std": float(np.std(arr)),
            "min": float(np.min(arr)),
            "max": float(np.max(arr)),
            "p95": float(np.percentile(arr, 95)),
            "p99": float(np.percentile(arr, 99))
        }