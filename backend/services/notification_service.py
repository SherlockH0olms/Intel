"""Notification Service for Alerts"""
from typing import Dict, List
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class NotificationService:
    def __init__(self):
        self.subscribers = {}
        self.notification_history = []
    
    async def send_alert(self, alert: Dict) -> bool:
        """Send alert notification"""
        notification = {
            "id": f"NOTIF_{len(self.notification_history) + 1}",
            "alert_id": alert.get("id"),
            "type": alert.get("alert_type"),
            "severity": alert.get("severity"),
            "message": self._format_message(alert),
            "timestamp": datetime.now().isoformat(),
            "sent_to": [],
            "channels": []
        }
        
        # Send via multiple channels
        channels_sent = []
        
        # 1. WebSocket (real-time)
        if await self._send_websocket(notification):
            channels_sent.append("websocket")
        
        # 2. Email (if critical)
        if alert.get("severity") == "critical":
            if await self._send_email(notification):
                channels_sent.append("email")
        
        # 3. SMS (if critical)
        if alert.get("severity") == "critical":
            if await self._send_sms(notification):
                channels_sent.append("sms")
        
        notification["channels"] = channels_sent
        self.notification_history.append(notification)
        
        logger.info(f"Alert notification sent: {notification['id']}")
        return True
    
    async def send_recommendation(self, recommendation: Dict) -> bool:
        """Send AI recommendation notification"""
        notification = {
            "type": "recommendation",
            "title": recommendation.get("title"),
            "description": recommendation.get("description"),
            "confidence": recommendation.get("confidence"),
            "timestamp": datetime.now().isoformat()
        }
        
        await self._send_websocket(notification)
        return True
    
    def subscribe(self, machine_id: str, callback):
        """Subscribe to notifications for a machine"""
        if machine_id not in self.subscribers:
            self.subscribers[machine_id] = []
        self.subscribers[machine_id].append(callback)
    
    def _format_message(self, alert: Dict) -> str:
        """Format alert message"""
        return f"{alert.get('alert_type')}: {alert.get('description')}"
    
    async def _send_websocket(self, notification: Dict) -> bool:
        """Send notification via WebSocket"""
        # In production: broadcast to WebSocket connections
        logger.debug(f"WebSocket notification: {notification}")
        return True
    
    async def _send_email(self, notification: Dict) -> bool:
        """Send notification via Email"""
        # In production: use email service (SendGrid, AWS SES, etc.)
        logger.debug(f"Email notification: {notification}")
        return True
    
    async def _send_sms(self, notification: Dict) -> bool:
        """Send notification via SMS"""
        # In production: use SMS service (Twilio, AWS SNS, etc.)
        logger.debug(f"SMS notification: {notification}")
        return True