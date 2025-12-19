"""MQTT Protocol Client"""
import paho.mqtt.client as mqtt
import json
import logging
from typing import Callable, Dict

logger = logging.getLogger(__name__)

class MQTTClient:
    def __init__(self, broker: str = "localhost", port: int = 1883):
        self.broker = broker
        self.port = port
        self.client = mqtt.Client()
        self.callbacks = {}
        
        # Setup callbacks
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_disconnect = self._on_disconnect
    
    def connect(self):
        """Connect to MQTT broker"""
        try:
            self.client.connect(self.broker, self.port, 60)
            self.client.loop_start()
            logger.info(f"Connected to MQTT broker at {self.broker}:{self.port}")
        except Exception as e:
            logger.error(f"Failed to connect to MQTT broker: {e}")
    
    def disconnect(self):
        """Disconnect from MQTT broker"""
        self.client.loop_stop()
        self.client.disconnect()
        logger.info("Disconnected from MQTT broker")
    
    def subscribe(self, topic: str, callback: Callable):
        """Subscribe to MQTT topic"""
        self.callbacks[topic] = callback
        self.client.subscribe(topic)
        logger.info(f"Subscribed to topic: {topic}")
    
    def publish(self, topic: str, payload: Dict):
        """Publish message to MQTT topic"""
        message = json.dumps(payload)
        self.client.publish(topic, message)
        logger.debug(f"Published to {topic}: {message}")
    
    def _on_connect(self, client, userdata, flags, rc):
        """Callback when connected"""
        if rc == 0:
            logger.info("MQTT connection successful")
        else:
            logger.error(f"MQTT connection failed with code {rc}")
    
    def _on_message(self, client, userdata, msg):
        """Callback when message received"""
        topic = msg.topic
        payload = json.loads(msg.payload.decode())
        
        if topic in self.callbacks:
            self.callbacks[topic](payload)
        else:
            logger.warning(f"No callback for topic: {topic}")
    
    def _on_disconnect(self, client, userdata, rc):
        """Callback when disconnected"""
        if rc != 0:
            logger.warning(f"Unexpected MQTT disconnect: {rc}")