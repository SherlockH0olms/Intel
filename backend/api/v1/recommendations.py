from fastapi import APIRouter
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class Recommendation(BaseModel):
    id: str
    machine_id: str
    type: str
    title: str
    description: str
    confidence: float
    parameters: dict
    status: str = "pending"
    created_at: datetime

class RecommendationApproval(BaseModel):
    approved: bool
    operator_id: str
    notes: Optional[str] = None

@router.get("/{machine_id}", response_model=List[Recommendation])
async def get_recommendations(machine_id: str):
    """Get AI recommendations for a machine"""
    return [
        {
            "id": "REC_001",
            "machine_id": machine_id,
            "type": "configuration",
            "title": "Reduce Spindle Speed",
            "description": "AI detects high vibration. Recommend reducing spindle speed from 2500 RPM to 2200 RPM.",
            "confidence": 0.92,
            "parameters": {
                "spindle_speed": {
                    "current": 2500,
                    "recommended": 2200,
                    "unit": "RPM"
                }
            },
            "status": "pending",
            "created_at": datetime.now()
        }
    ]

@router.post("/{recommendation_id}/approve")
async def approve_recommendation(
    recommendation_id: str,
    approval: RecommendationApproval
):
    """Approve or reject AI recommendation"""
    # TODO: Implement approval logic
    return {
        "message": f"Recommendation {recommendation_id} {'approved' if approval.approved else 'rejected'}",
        "applied": approval.approved
    }