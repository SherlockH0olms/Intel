#!/bin/bash
# Start development environment

echo "Starting Intellica development environment..."

# Start Docker services
docker-compose up -d

# Wait for services to be ready
echo "Waiting for services to start..."
sleep 10

# Check service health
echo "Checking service health..."
curl -f http://localhost:8000/health || echo "Backend not ready"

# Show logs
echo ""
echo "Services started! Showing logs..."
echo "Press Ctrl+C to stop following logs (services will continue running)"
docker-compose logs -f