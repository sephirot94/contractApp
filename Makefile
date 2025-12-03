.PHONY: help up down restart logs build seed test clean install dev-setup frontend backend lint format type-check

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
NC := \033[0m # No Color

help: ## Show this help message
	@echo "$(BLUE)Contractor Finder - Available Commands$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)%-20s$(NC) %s\n", $$1, $$2}'

# ==============================================================================
# Docker Commands - Primary way to run the app (ensures consistency)
# ==============================================================================

up: ## Start all services (recommended - uses Docker)
	@echo "$(BLUE)Starting all services with Docker...$(NC)"
	docker-compose up -d
	@echo "$(GREEN)Services started!$(NC)"
	@echo "Frontend: http://localhost:3000"
	@echo "Backend API: http://localhost:8000"
	@echo "API Docs: http://localhost:8000/docs"
	@echo ""
	@echo "Run 'make seed' to populate the database with sample data"
	@echo "Run 'make logs' to view logs"

up-build: ## Start all services and rebuild containers
	@echo "$(BLUE)Building and starting all services...$(NC)"
	docker-compose up -d --build
	@echo "$(GREEN)Services started!$(NC)"

down: ## Stop all services
	@echo "$(BLUE)Stopping all services...$(NC)"
	docker-compose down
	@echo "$(GREEN)Services stopped!$(NC)"

restart: ## Restart all services
	@echo "$(BLUE)Restarting all services...$(NC)"
	docker-compose restart
	@echo "$(GREEN)Services restarted!$(NC)"

logs: ## View logs from all services
	docker-compose logs -f

logs-backend: ## View backend logs only
	docker-compose logs -f backend

logs-frontend: ## View frontend logs only
	docker-compose logs -f frontend

logs-db: ## View database logs only
	docker-compose logs -f db

build: ## Build Docker images
	@echo "$(BLUE)Building Docker images...$(NC)"
	docker-compose build

seed: ## Seed database with sample data
	@echo "$(BLUE)Seeding database...$(NC)"
	docker-compose exec backend python -m app.seed_data
	@echo "$(GREEN)Database seeded successfully!$(NC)"

# ==============================================================================
# Quick Start Commands
# ==============================================================================

start: up-build seed ## Quick start: build, start services, and seed database
	@echo ""
	@echo "$(GREEN)✓ App is ready!$(NC)"
	@echo "Open http://localhost:3000 in your browser"

first-run: install up-build seed ## First time setup: install everything and start
	@echo ""
	@echo "$(GREEN)✓ First run setup complete!$(NC)"
	@echo "Open http://localhost:3000 in your browser"

# ==============================================================================
# Testing Commands
# ==============================================================================

test: ## Run all tests (backend + frontend)
	@echo "$(BLUE)Running backend tests...$(NC)"
	docker-compose exec backend pipenv run pytest
	@echo ""
	@echo "$(BLUE)Running frontend tests...$(NC)"
	docker-compose exec frontend npm test
	@echo "$(GREEN)All tests passed!$(NC)"

test-backend: ## Run backend tests only
	@echo "$(BLUE)Running backend tests...$(NC)"
	docker-compose exec backend pipenv run pytest -v

test-frontend: ## Run frontend tests only
	@echo "$(BLUE)Running frontend tests...$(NC)"
	docker-compose exec frontend npm test

test-coverage: ## Run tests with coverage reports
	@echo "$(BLUE)Running backend tests with coverage...$(NC)"
	docker-compose exec backend pipenv run pytest --cov=app --cov-report=html
	@echo ""
	@echo "$(BLUE)Running frontend tests with coverage...$(NC)"
	docker-compose exec frontend npm run test:coverage
	@echo "$(GREEN)Coverage reports generated!$(NC)"
	@echo "Backend: backend/htmlcov/index.html"
	@echo "Frontend: frontend/coverage/lcov-report/index.html"

# ==============================================================================
# Code Quality Commands
# ==============================================================================

lint: ## Run linters on all code
	@echo "$(BLUE)Running Ruff linter on backend...$(NC)"
	docker-compose exec backend pipenv run ruff check .
	@echo ""
	@echo "$(BLUE)Running ESLint on frontend...$(NC)"
	docker-compose exec frontend npm run lint
	@echo "$(GREEN)Linting complete!$(NC)"

format: ## Format all code
	@echo "$(BLUE)Formatting backend code with Ruff...$(NC)"
	docker-compose exec backend pipenv run ruff format .
	@echo ""
	@echo "$(BLUE)Formatting frontend code with Prettier...$(NC)"
	docker-compose exec frontend npm run format
	@echo "$(GREEN)Code formatted!$(NC)"

type-check: ## Run type checker on backend
	@echo "$(BLUE)Running Ty type checker...$(NC)"
	docker-compose exec backend pipenv run ty check
	@echo "$(GREEN)Type checking complete!$(NC)"

quality: lint type-check test ## Run all quality checks (lint, type-check, test)
	@echo "$(GREEN)✓ All quality checks passed!$(NC)"

# ==============================================================================
# Development Setup (Local - without Docker)
# ==============================================================================

install: ## Install all dependencies (for local development)
	@echo "$(BLUE)Installing dependencies...$(NC)"
	@echo "Installing pre-commit..."
	pip install pre-commit pipenv
	pre-commit install
	@echo ""
	@echo "Installing backend dependencies..."
	cd backend && pipenv install --dev
	@echo ""
	@echo "Installing frontend dependencies..."
	cd frontend && npm install
	@echo "$(GREEN)Dependencies installed!$(NC)"

dev-backend: ## Run backend locally (without Docker)
	@echo "$(BLUE)Starting backend on http://localhost:8000$(NC)"
	@echo "$(YELLOW)Warning: Using local development. Docker is recommended for consistency.$(NC)"
	cd backend && pipenv run uvicorn app.main:app --reload

dev-frontend: ## Run frontend locally (without Docker)
	@echo "$(BLUE)Starting frontend on http://localhost:3000$(NC)"
	@echo "$(YELLOW)Warning: Using local development. Docker is recommended for consistency.$(NC)"
	cd frontend && npm start

# ==============================================================================
# Database Commands
# ==============================================================================

db-shell: ## Open MySQL shell
	docker-compose exec db mysql -u contractor_user -pcontractor_pass contractor_db

db-reset: ## Reset database (WARNING: deletes all data)
	@echo "$(YELLOW)WARNING: This will delete all database data!$(NC)"
	@read -p "Are you sure? [y/N] " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		docker-compose down -v; \
		docker-compose up -d db; \
		sleep 5; \
		docker-compose up -d backend frontend; \
		make seed; \
	fi

# ==============================================================================
# Cleanup Commands
# ==============================================================================

clean: ## Clean up containers, volumes, and generated files
	@echo "$(BLUE)Cleaning up...$(NC)"
	docker-compose down -v
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	rm -rf frontend/coverage 2>/dev/null || true
	rm -rf frontend/build 2>/dev/null || true
	rm -rf backend/.venv 2>/dev/null || true
	@echo "$(GREEN)Cleanup complete!$(NC)"

clean-all: clean ## Clean everything including Docker images
	@echo "$(BLUE)Removing Docker images...$(NC)"
	docker-compose down --rmi all -v
	@echo "$(GREEN)All cleaned!$(NC)"

# ==============================================================================
# Development Tools
# ==============================================================================

shell-backend: ## Open shell in backend container
	docker-compose exec backend /bin/bash

shell-frontend: ## Open shell in frontend container
	docker-compose exec frontend /bin/sh

pre-commit: ## Run pre-commit hooks on all files
	pre-commit run --all-files

# ==============================================================================
# Status & Info
# ==============================================================================

status: ## Show status of all services
	@echo "$(BLUE)Service Status:$(NC)"
	docker-compose ps

info: ## Show service information and URLs
	@echo "$(BLUE)Contractor Finder - Service Information$(NC)"
	@echo ""
	@echo "$(GREEN)Frontend:$(NC)     http://localhost:3000"
	@echo "$(GREEN)Backend API:$(NC)  http://localhost:8000"
	@echo "$(GREEN)API Docs:$(NC)     http://localhost:8000/docs"
	@echo "$(GREEN)Database:$(NC)     localhost:3306"
	@echo ""
	@echo "$(BLUE)Sample Location (Sydney CBD):$(NC) -33.8688, 151.2093"
