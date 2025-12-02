#!/bin/bash

# Development Environment Setup Script for Contractor Finder App
# This script sets up pre-commit hooks and installs development dependencies

set -e

echo "=========================================="
echo "Setting up development environment..."
echo "=========================================="

# Check if we're in the right directory
if [ ! -f "docker-compose.yml" ]; then
    echo "Error: Please run this script from the project root directory"
    exit 1
fi

# Install pre-commit
echo ""
echo "Installing pre-commit..."
pip install pre-commit || {
    echo "Warning: Could not install pre-commit with pip. Please install it manually."
}

# Install pre-commit hooks
echo ""
echo "Installing pre-commit hooks..."
pre-commit install || {
    echo "Warning: Could not install pre-commit hooks. Please run 'pre-commit install' manually."
}

# Install pipenv and backend dependencies
echo ""
echo "Installing pipenv..."
pip install pipenv || {
    echo "Warning: Could not install pipenv. Please install it manually."
}

echo "Installing backend dependencies..."
cd backend
echo "Installing dependencies with pipenv..."
pipenv install --dev || {
    echo "Warning: Could not install backend dependencies. Please run 'pipenv install --dev' manually in the backend directory."
}
cd ..

# Install frontend dependencies
echo ""
echo "Installing frontend dependencies..."
cd frontend
if [ ! -d "node_modules" ]; then
    echo "Installing npm packages..."
    npm install
else
    echo "node_modules already exists. Skipping npm install."
fi
cd ..

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo ""
    echo "Creating .env file from .env.example..."
    cp .env.example .env
    echo ".env file created successfully!"
else
    echo ""
    echo ".env file already exists. Skipping."
fi

echo ""
echo "=========================================="
echo "Setup complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Start the application: docker-compose up --build"
echo "2. Seed the database: docker-compose exec backend python -m app.seed_data"
echo "3. Open http://localhost:3000 in your browser"
echo ""
echo "Pre-commit hooks are installed and will run automatically on every commit."
echo "To run hooks manually: pre-commit run --all-files"
echo ""
