# Deployment Guide

## Development Deployment

### Prerequisites
- Docker 24+
- Docker Compose 2.0+
- 4GB RAM minimum
- 10GB disk space

### Steps

1. **Clone repository**
```bash
git clone https://github.com/SherlockH0olms/Intel.git
cd Intel
```

2. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your values
```

3. **Start services**
```bash
docker-compose up -d
```

4. **Check status**
```bash
docker-compose ps
```

5. **View logs**
```bash
docker-compose logs -f backend
```

6. **Access services**
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs
- RabbitMQ: http://localhost:15672 (guest/guest)

## Production Deployment

### Option 1: Docker Compose

1. **Update docker-compose.yml**
- Set production environment variables
- Use Docker secrets for credentials
- Configure resource limits

2. **Deploy**
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Option 2: Kubernetes

1. **Build images**
```bash
docker build -t intellica-backend:latest ./backend
docker build -t intellica-frontend:latest ./frontend
```

2. **Push to registry**
```bash
docker tag intellica-backend:latest registry.example.com/intellica-backend:latest
docker push registry.example.com/intellica-backend:latest
```

3. **Deploy to Kubernetes**
```bash
kubectl apply -f kubernetes/
```

## Monitoring

### Health Checks
```bash
curl http://localhost:8000/health
```

### Logs
```bash
# Backend
docker-compose logs -f backend

# Frontend
docker-compose logs -f frontend

# Database
docker-compose logs -f timescaledb
```

## Backup

### Database Backup
```bash
docker-compose exec timescaledb pg_dump -U admin intellica > backup.sql
```

### Restore
```bash
cat backup.sql | docker-compose exec -T timescaledb psql -U admin intellica
```