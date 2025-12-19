"""Inject anomalies for testing ML models"""
import random
from typing import Dict

class AnomalyInjector:
    def __init__(self, anomaly_rate: float = 0.1):
        self.anomaly_rate = anomaly_rate
        self.anomaly_types = [
            "high_temperature",
            "high_vibration",
            "speed_drop",
            "pressure_spike"
        ]
    
    def inject(self, data: Dict, machine_type: str) -> Dict:
        """Inject anomaly into sensor data"""
        if random.random() > self.anomaly_rate:
            return data  # No anomaly
        
        anomaly_type = random.choice(self.anomaly_types)
        
        if anomaly_type == "high_temperature":
            if "temperature" in data["sensors"]:
                data["sensors"]["temperature"]["value"] = random.uniform(85, 95)
                data["anomaly"] = "high_temperature"
        
        elif anomaly_type == "high_vibration":
            if "vibration" in data["sensors"]:
                data["sensors"]["vibration"]["value"] = random.uniform(2.5, 4.0)
                data["anomaly"] = "high_vibration"
        
        elif anomaly_type == "speed_drop":
            if "speed" in data["sensors"]:
                current = data["sensors"]["speed"]["value"]
                data["sensors"]["speed"]["value"] = current * 0.6  # 40% drop
                data["anomaly"] = "speed_drop"
        
        elif anomaly_type == "pressure_spike":
            if "pressure" in data["sensors"]:
                data["sensors"]["pressure"]["value"] = random.uniform(180, 200)
                data["anomaly"] = "pressure_spike"
        
        return data