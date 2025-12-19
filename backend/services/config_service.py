"""Configuration Management Service"""
from typing import Dict, List
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class ConfigService:
    def __init__(self):
        self.config_history = []
    
    async def apply_configuration(self, 
                                   machine_id: str,
                                   parameters: Dict,
                                   operator_id: str,
                                   ai_confidence: float = None) -> Dict:
        """Apply configuration changes to machine"""
        # Get current configuration
        current_config = await self._get_current_config(machine_id)
        
        # Validate new configuration
        is_valid, errors = self._validate_config(parameters)
        if not is_valid:
            return {
                "success": False,
                "errors": errors
            }
        
        # Record configuration change
        change_record = {
            "id": f"CONFIG_{len(self.config_history) + 1}",
            "machine_id": machine_id,
            "old_config": current_config,
            "new_config": parameters,
            "changed_by": operator_id,
            "ai_confidence": ai_confidence,
            "timestamp": datetime.now().isoformat(),
            "status": "applied"
        }
        
        # Apply configuration (in production: send to machine via protocol)
        success = await self._send_to_machine(machine_id, parameters)
        
        if success:
            self.config_history.append(change_record)
            logger.info(f"Configuration applied to {machine_id}")
            return {
                "success": True,
                "change_id": change_record["id"],
                "applied_at": change_record["timestamp"]
            }
        else:
            return {
                "success": False,
                "errors": ["Failed to communicate with machine"]
            }
    
    async def rollback_configuration(self, 
                                      machine_id: str,
                                      change_id: str) -> Dict:
        """Rollback to previous configuration"""
        # Find change record
        change_record = next(
            (c for c in self.config_history if c["id"] == change_id),
            None
        )
        
        if not change_record:
            return {
                "success": False,
                "errors": ["Change record not found"]
            }
        
        # Rollback to old configuration
        old_config = change_record["old_config"]
        success = await self._send_to_machine(machine_id, old_config)
        
        if success:
            logger.info(f"Configuration rolled back for {machine_id}")
            return {
                "success": True,
                "rolled_back_to": old_config
            }
        else:
            return {
                "success": False,
                "errors": ["Failed to rollback configuration"]
            }
    
    async def get_configuration_history(self, 
                                         machine_id: str,
                                         limit: int = 100) -> List[Dict]:
        """Get configuration change history"""
        history = [
            c for c in self.config_history 
            if c["machine_id"] == machine_id
        ]
        return history[-limit:]
    
    async def _get_current_config(self, machine_id: str) -> Dict:
        """Get current machine configuration"""
        # In production: query from database or machine
        return {
            "spindle_speed": 2500,
            "feed_rate": 200,
            "cutting_depth": 2.0,
            "temperature": 60
        }
    
    def _validate_config(self, parameters: Dict) -> tuple:
        """Validate configuration parameters"""
        errors = []
        
        # Add validation rules
        if "spindle_speed" in parameters:
            if parameters["spindle_speed"] < 1000 or parameters["spindle_speed"] > 3000:
                errors.append("Spindle speed out of range [1000, 3000]")
        
        return len(errors) == 0, errors
    
    async def _send_to_machine(self, machine_id: str, config: Dict) -> bool:
        """Send configuration to machine via protocol"""
        # In production: use protocol clients (MQTT, OPC-UA, Modbus)
        logger.debug(f"Sending config to {machine_id}: {config}")
        return True