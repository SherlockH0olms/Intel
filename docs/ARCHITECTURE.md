# Intellica System Architecture

## Overview

Intellica is a microservices-based industrial optimization platform with AI-powered features.

## System Components

### 1. Frontend (React + TypeScript)
- **Dashboard**: Real-time factory overview
- **Machine Details**: Individual machine monitoring
- **AI Recommendations**: Human-in-the-loop approvals
- **Analytics**: OEE, downtime, defect tracking
- **WebSocket**: Real-time data streaming

### 2. Backend (FastAPI + Python)
- **REST API**: CRUD operations for machines, sensors, etc.
- **WebSocket Server**: Real-time data broadcasting
- **ML Inference**: On-demand predictions
- **Protocol Clients**: MQTT, OPC-UA, Modbus integration

### 3. ML Models
- **Anomaly Detection**: Isolation Forest (96% accuracy)
- **Predictive Maintenance**: Random Forest (F1: 0.84)
- **Configuration Optimization**: Bayesian Optimization
- **Defect Detection**: MobileNetV2 CNN (94% accuracy)

### 4. Data Layer
- **TimescaleDB**: Time-series sensor data
- **PostgreSQL**: Relational data (machines, alerts, configs)
- **Redis**: Caching and session management
- **RabbitMQ**: Message queue for async tasks

## Data Flow

```
[Machines] 
    ↓ (MQTT/OPC-UA/Modbus)
[Protocol Clients]
    ↓
[Backend API]
    ↓
[TimescaleDB] ←→ [ML Models]
    ↓
[WebSocket Server]
    ↓
[Frontend Dashboard]
```

## Deployment Architecture

### Development
- Docker Compose with 5 services
- Local volumes for data persistence
- Hot-reload for backend and frontend

### Production
- Kubernetes deployment
- Horizontal pod autoscaling
- Load balancer for API
- Persistent volumes for databases

## Security

- JWT authentication
- Role-based access control (RBAC)
- TLS/SSL encryption
- API rate limiting
- Input validation

## Scalability

- Stateless API design
- Database connection pooling
- Redis caching layer
- Async task processing
- Horizontal scaling ready