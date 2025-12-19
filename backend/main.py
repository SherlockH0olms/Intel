from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI(
    title="Intellica API",
    description="AI-Powered Sənaye Optimallaşma Platforması",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()

@app.get("/")
async def root():
    return {
        "message": "Intellica API - AI-Powered Industrial Optimization",
        "version": "1.0.0",
        "status": "online",
        "features": [
            "Real-time sensor monitoring",
            "Anomaly detection",
            "Predictive maintenance",
            "Configuration optimization",
            "Defect detection"
        ]
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "backend"}

@app.get("/api/v1/machines")
async def get_machines():
    """Get all machines"""
    return {
        "machines": [
            {
                "id": "CNC_001",
                "name": "CNC Machine 1",
                "type": "CNC",
                "status": "running",
                "location": {"x": 100, "y": 150}
            },
            {
                "id": "INJ_001",
                "name": "Injection Molding 1",
                "type": "Injection",
                "status": "idle",
                "location": {"x": 300, "y": 150}
            },
            {
                "id": "CONV_001",
                "name": "Conveyor Belt 1",
                "type": "Conveyor",
                "status": "running",
                "location": {"x": 500, "y": 150}
            }
        ]
    }

@app.websocket("/ws/realtime")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast({"message": data})
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)