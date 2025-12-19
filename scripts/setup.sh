#!/bin/bash
# Initial setup script

echo "Intellica Setup Script"
echo "====================="

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is not installed"
    exit 1
fi

# Check Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo "Error: Docker Compose is not installed"
    exit 1
fi

# Create .env if not exists
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "Please edit .env with your configuration"
fi

# Create necessary directories
echo "Creating directories..."
mkdir -p ml_models
mkdir -p logs
mkdir -p uploads

# Pull Docker images
echo "Pulling Docker images..."
docker-compose pull

# Build services
echo "Building services..."
docker-compose build

echo ""
echo "Setup complete!"
echo "Run 'docker-compose up -d' to start services"