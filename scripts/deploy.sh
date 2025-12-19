#!/bin/bash
# Deployment script

set -e

ENV=${1:-production}

echo "Deploying Intellica to $ENV environment"

# Build images
echo "Building Docker images..."
docker-compose build --no-cache

# Tag images
echo "Tagging images..."
docker tag intellica_backend:latest intellica_backend:$ENV
docker tag intellica_frontend:latest intellica_frontend:$ENV

# Push to registry (if configured)
if [ ! -z "$DOCKER_REGISTRY" ]; then
    echo "Pushing to registry..."
    docker push $DOCKER_REGISTRY/intellica_backend:$ENV
    docker push $DOCKER_REGISTRY/intellica_frontend:$ENV
fi

# Deploy
if [ "$ENV" = "production" ]; then
    echo "Deploying to production..."
    docker-compose -f docker-compose.prod.yml up -d
else
    echo "Deploying to $ENV..."
    docker-compose up -d
fi

echo "Deployment complete!"