# Intellica API Documentation

## Base URL
```
http://localhost:8000/api/v1
```

## Authentication
Currently in development mode. Production will use JWT tokens.

## Endpoints

### Machines

#### GET /machines
Get all machines

**Response:**
```json
[
  {
    "id": "CNC_001",
    "name": "CNC Machine 1",
    "type": "CNC",
    "status": "running",
    "location": {"x": 100, "y": 150}
  }
]
```

#### GET /machines/{machine_id}
Get specific machine

#### POST /machines
Create new machine

**Request Body:**
```json
{
  "name": "New Machine",
  "type": "CNC",
  "location_x": 200,
  "location_y": 200,
  "protocol": "MQTT"
}
```

### Sensors

#### GET /sensors/{machine_id}
Get sensor data for machine

**Query Parameters:**
- `sensor_name` (optional): Filter by sensor
- `limit` (default: 100): Number of records

**Response:**
```json
[
  {
    "time": "2025-12-20T01:00:00Z",
    "machine_id": "CNC_001",
    "sensor_name": "temperature",
    "value": 75.5,
    "unit": "°C"
  }
]
```

### Recommendations

#### GET /recommendations/{machine_id}
Get AI recommendations

**Response:**
```json
[
  {
    "id": "REC_001",
    "machine_id": "CNC_001",
    "type": "configuration",
    "title": "Reduce Spindle Speed",
    "confidence": 0.92,
    "parameters": {
      "spindle_speed": {
        "current": 2500,
        "recommended": 2200
      }
    }
  }
]
```

#### POST /recommendations/{recommendation_id}/approve
Approve or reject recommendation

**Request Body:**
```json
{
  "approved": true,
  "operator_id": "OP123",
  "notes": "Applied successfully"
}
```

### Analytics

#### GET /analytics/metrics
Get performance metrics

**Response:**
```json
{
  "oee": 0.85,
  "availability": 0.92,
  "performance": 0.88,
  "quality": 0.95,
  "downtime_hours": 2.5,
  "defect_rate": 0.03
}
```

### Defects

#### POST /defects/detect
Detect defects in image

**Request:**
- Content-Type: multipart/form-data
- file: Image file
- machine_id: Machine ID

**Response:**
```json
{
  "defect_type": "crack",
  "confidence": 0.94,
  "bounding_box": {
    "x": 120,
    "y": 80,
    "width": 50,
    "height": 30
  }
}
```

## WebSocket

### Endpoint
```
ws://localhost:8000/ws/realtime
```

### Message Format
```json
{
  "type": "sensor_update",
  "machine_id": "CNC_001",
  "data": {...}
}
```