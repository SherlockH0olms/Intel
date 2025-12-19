#!/usr/bin/env python3
"""Factory Simulator for Demo and Testing"""
import time
import random
import json
import argparse
from datetime import datetime
from typing import Dict, List
import paho.mqtt.client as mqtt

class FactorySimulator:
    def __init__(self, num_machines: int = 3):
        self.num_machines = num_machines
        self.machines = self._initialize_machines()
        self.mqtt_client = None
        
    def _initialize_machines(self) -> List[Dict]:
        """Initialize machine configurations"""
        machines = [
            {
                "id": "CNC_001",
                "name": "CNC Machine 1",
                "type": "CNC",
                "sensors": ["temperature", "vibration", "speed", "power"]
            },
            {
                "id": "INJ_001",
                "name": "Injection Molding 1",
                "type": "Injection",
                "sensors": ["temperature", "pressure", "cycle_time"]
            },
            {
                "id": "CONV_001",
                "name": "Conveyor Belt 1",
                "type": "Conveyor",
                "sensors": ["speed", "load", "vibration"]
            }
        ]
        return machines[:self.num_machines]
    
    def connect_mqtt(self, broker: str = "localhost", port: int = 1883):
        """Connect to MQTT broker"""
        self.mqtt_client = mqtt.Client()
        try:
            self.mqtt_client.connect(broker, port, 60)
            self.mqtt_client.loop_start()
            print(f"Connected to MQTT broker at {broker}:{port}")
        except Exception as e:
            print(f"Failed to connect to MQTT: {e}")
    
    def generate_sensor_data(self, machine: Dict) -> Dict:
        """Generate realistic sensor data"""
        data = {
            "machine_id": machine["id"],
            "timestamp": datetime.now().isoformat(),
            "sensors": {}
        }
        
        for sensor in machine["sensors"]:
            if sensor == "temperature":
                # Normal: 60-80°C, anomaly: >85°C
                base = 70
                value = random.gauss(base, 5)
                # Inject anomaly 5% of the time
                if random.random() < 0.05:
                    value = random.uniform(85, 95)
                data["sensors"][sensor] = {
                    "value": round(value, 2),
                    "unit": "°C"
                }
            
            elif sensor == "vibration":
                # Normal: 0.5-2.0 mm/s, anomaly: >2.5 mm/s
                base = 1.2
                value = random.gauss(base, 0.3)
                if random.random() < 0.05:
                    value = random.uniform(2.5, 4.0)
                data["sensors"][sensor] = {
                    "value": round(value, 2),
                    "unit": "mm/s"
                }
            
            elif sensor == "speed":
                # RPM for CNC, m/min for conveyor
                if machine["type"] == "CNC":
                    value = random.gauss(2500, 100)
                    unit = "RPM"
                else:
                    value = random.gauss(15, 2)
                    unit = "m/min"
                data["sensors"][sensor] = {
                    "value": round(value, 2),
                    "unit": unit
                }
            
            elif sensor == "pressure":
                value = random.gauss(150, 10)
                data["sensors"][sensor] = {
                    "value": round(value, 2),
                    "unit": "bar"
                }
            
            elif sensor == "power":
                value = random.gauss(45, 5)
                data["sensors"][sensor] = {
                    "value": round(value, 2),
                    "unit": "kW"
                }
            
            elif sensor == "cycle_time":
                value = random.gauss(30, 3)
                data["sensors"][sensor] = {
                    "value": round(value, 2),
                    "unit": "s"
                }
            
            elif sensor == "load":
                value = random.gauss(75, 10)
                data["sensors"][sensor] = {
                    "value": round(value, 2),
                    "unit": "kg"
                }
        
        return data
    
    def run(self, interval: int = 5, duration: int = None):
        """Run simulation"""
        print(f"Starting factory simulation with {self.num_machines} machines")
        print(f"Data generation interval: {interval} seconds")
        
        start_time = time.time()
        iteration = 0
        
        try:
            while True:
                iteration += 1
                
                for machine in self.machines:
                    data = self.generate_sensor_data(machine)
                    
                    # Publish to MQTT if connected
                    if self.mqtt_client:
                        topic = f"factory/{machine['id']}/sensors"
                        self.mqtt_client.publish(topic, json.dumps(data))
                    
                    # Print to console
                    print(f"[{iteration}] {machine['id']}: {json.dumps(data['sensors'], indent=2)}")
                
                # Check duration
                if duration and (time.time() - start_time) > duration:
                    print(f"Simulation completed after {duration} seconds")
                    break
                
                time.sleep(interval)
        
        except KeyboardInterrupt:
            print("\nSimulation stopped by user")
        finally:
            if self.mqtt_client:
                self.mqtt_client.loop_stop()
                self.mqtt_client.disconnect()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Factory Simulator")
    parser.add_argument("--machines", type=int, default=3, help="Number of machines")
    parser.add_argument("--interval", type=int, default=5, help="Data interval (seconds)")
    parser.add_argument("--duration", type=int, default=None, help="Simulation duration (seconds)")
    parser.add_argument("--mqtt-broker", default="localhost", help="MQTT broker address")
    parser.add_argument("--mqtt-port", type=int, default=1883, help="MQTT broker port")
    
    args = parser.parse_args()
    
    simulator = FactorySimulator(num_machines=args.machines)
    simulator.connect_mqtt(broker=args.mqtt_broker, port=args.mqtt_port)
    simulator.run(interval=args.interval, duration=args.duration)