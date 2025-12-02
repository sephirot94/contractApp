# Development Environment Setup Script for Contractor Finder App (Windows)
# This script sets up pre-commit hooks and installs development dependencies

$ErrorActionPreference = "Stop"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Setting up development environment..." -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# Check if we're in the right directory
if (-not (Test-Path "docker-compose.yml")) {
    Write-Host "Error: Please run this script from the project root directory" -ForegroundColor Red
    exit 1
}

# Install pre-commit
Write-Host ""
Write-Host "Installing pre-commit..." -ForegroundColor Yellow
try {
    pip install pre-commit
} catch {
    Write-Host "Warning: Could not install pre-commit with pip. Please install it manually." -ForegroundColor Yellow
}

# Install pre-commit hooks
Write-Host ""
Write-Host "Installing pre-commit hooks..." -ForegroundColor Yellow
try {
    pre-commit install
} catch {
    Write-Host "Warning: Could not install pre-commit hooks. Please run 'pre-commit install' manually." -ForegroundColor Yellow
}

# Install backend dependencies
Write-Host ""
Write-Host "Installing backend dependencies..." -ForegroundColor Yellow
Set-Location backend

if (-not (Test-Path "venv")) {
    Write-Host "Creating Python virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

Write-Host "Activating virtual environment and installing dependencies..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
deactivate
Set-Location ..

# Install frontend dependencies
Write-Host ""
Write-Host "Installing frontend dependencies..." -ForegroundColor Yellow
Set-Location frontend

if (-not (Test-Path "node_modules")) {
    Write-Host "Installing npm packages..." -ForegroundColor Yellow
    npm install
} else {
    Write-Host "node_modules already exists. Skipping npm install." -ForegroundColor Yellow
}
Set-Location ..

# Create .env file if it doesn't exist
if (-not (Test-Path ".env")) {
    Write-Host ""
    Write-Host "Creating .env file from .env.example..." -ForegroundColor Yellow
    Copy-Item .env.example .env
    Write-Host ".env file created successfully!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host ".env file already exists. Skipping." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host "Setup complete!" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:"
Write-Host "1. Start the application: docker-compose up --build"
Write-Host "2. Seed the database: docker-compose exec backend python -m app.seed_data"
Write-Host "3. Open http://localhost:3000 in your browser"
Write-Host ""
Write-Host "Pre-commit hooks are installed and will run automatically on every commit."
Write-Host "To run hooks manually: pre-commit run --all-files"
Write-Host ""
