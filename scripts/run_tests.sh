#!/bin/bash
# Run all tests

echo "Running Intellica Tests"
echo "====================="

# Backend tests
echo "Running backend tests..."
docker-compose exec backend pytest tests/ -v

# Frontend tests
echo "Running frontend tests..."
docker-compose exec frontend npm test

echo ""
echo "All tests completed!"