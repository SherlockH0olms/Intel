from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class MachineBase(BaseModel):
    name: str
    type: str
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    location_x: int
    location_y: int
    protocol: str
    status: str = "idle"

class Machine(MachineBase):
    id: str
    created_at: datetime
    updated_at: datetime

@router.get("/", response_model=List[Machine])
async def get_machines():
    """Get all machines"""
    return [
        {
            "id": "CNC_001",
            "name": "CNC Machine 1",
            "type": "CNC",
            "manufacturer": "Haas",
            "model": "VF-2",
            "location_x": 100,
            "location_y": 150,
            "protocol": "MQTT",
            "status": "running",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "id": "INJ_001",
            "name": "Injection Molding 1",
            "type": "Injection",
            "manufacturer": "Engel",
            "model": "e-victory",
            "location_x": 300,
            "location_y": 150,
            "protocol": "OPC-UA",
            "status": "idle",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "id": "CONV_001",
            "name": "Conveyor Belt 1",
            "type": "Conveyor",
            "manufacturer": "Siemens",
            "model": "SIMATIC",
            "location_x": 500,
            "location_y": 150,
            "protocol": "Modbus",
            "status": "running",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
    ]

@router.get("/{machine_id}", response_model=Machine)
async def get_machine(machine_id: str):
    """Get specific machine by ID"""
    # TODO: Implement database query
    return {
        "id": machine_id,
        "name": f"Machine {machine_id}",
        "type": "CNC",
        "manufacturer": "Haas",
        "model": "VF-2",
        "location_x": 100,
        "location_y": 150,
        "protocol": "MQTT",
        "status": "running",
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }

@router.post("/", response_model=Machine)
async def create_machine(machine: MachineBase):
    """Create new machine"""
    # TODO: Implement database insert
    return {
        "id": "NEW_001",
        **machine.dict(),
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }

@router.put("/{machine_id}", response_model=Machine)
async def update_machine(machine_id: str, machine: MachineBase):
    """Update machine"""
    # TODO: Implement database update
    return {
        "id": machine_id,
        **machine.dict(),
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }

@router.delete("/{machine_id}")
async def delete_machine(machine_id: str):
    """Delete machine"""
    # TODO: Implement database delete
    return {"message": f"Machine {machine_id} deleted"}