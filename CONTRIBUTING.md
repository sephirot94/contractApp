# Contributing to Contractor Finder

Thank you for your interest in contributing to the Contractor Finder project! This document provides guidelines and instructions for contributing.

## Development Setup

### Quick Setup

Use the provided setup scripts to get started quickly:

**Unix/Linux/macOS:**
```bash
./setup-dev.sh
```

**Windows (PowerShell):**
```powershell
.\setup-dev.ps1
```

### Manual Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd contractApp
   ```

2. **Install pre-commit**:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

3. **Create .env file**:
   ```bash
   cp .env.example .env
   ```

4. **Start the application**:
   ```bash
   docker-compose up --build
   ```

## Code Quality Standards

### Pre-commit Hooks

This project uses pre-commit hooks to maintain code quality. Hooks run automatically before each commit:

- Trailing whitespace removal
- End-of-file fixes
- YAML/JSON validation
- Ruff (Python linting and formatting)
- Ty (Python type checking)
- ESLint (JavaScript linting)
- Prettier (JavaScript formatting)

To run hooks manually:
```bash
pre-commit run --all-files
```

### Python Code Standards

- **Dependency Management**: Pipfile (pipenv)
- **Linter/Formatter**: Ruff
- **Type Checker**: Ty (Astral's fast type checker)
- **Line length**: 100 characters
- **Style**: PEP 8 compliant
- **Imports**: Auto-sorted with isort rules

Run checks:
```bash
cd backend
pipenv run ruff check .              # Lint
pipenv run ruff check . --fix        # Auto-fix issues
pipenv run ruff format .             # Format code
pipenv run ty check                  # Type check
```

### JavaScript Code Standards

- **Linter**: ESLint (extends react-app)
- **Formatter**: Prettier
- **Style**: Standard React conventions
- **Line length**: 100 characters

Run checks:
```bash
cd frontend
npm run lint              # Lint
npm run lint:fix          # Auto-fix issues
npm run format            # Format code
npm run format:check      # Check formatting
```

## Testing Requirements

### Backend Tests (pytest)

All backend code must have tests. Run tests with:
```bash
cd backend
pipenv run pytest                    # Run all tests
pipenv run pytest --cov=app          # Run with coverage
```

**Test Coverage Requirements:**
- Minimum coverage: As configured in pyproject.toml
- All new features must include tests
- All bug fixes must include regression tests

### Frontend Tests (Jest)

All React components must have tests. Run tests with:
```bash
cd frontend
npm test                  # Run all tests
npm run test:coverage     # Run with coverage
```

**Test Coverage Requirements:**
- Minimum coverage: 50% (configurable in package.json)
- All new components must include tests
- Test user interactions and edge cases

## Pull Request Process

### Before Submitting

1. **Ensure all tests pass**:
   ```bash
   cd backend && pipenv run pytest
   cd ../frontend && npm test
   ```

2. **Check code formatting and type checking**:
   ```bash
   pre-commit run --all-files
   ```

3. **Update documentation** if needed

4. **Add tests** for new features

### PR Guidelines

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following code standards

3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```
   Pre-commit hooks will run automatically.

4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request** on GitHub

### PR Requirements

All PRs must:
- ✅ Pass all automated checks (GitHub Actions)
- ✅ Have passing tests (backend and frontend)
- ✅ Pass linting (Ruff, ESLint, Prettier)
- ✅ Pass type checking (Ty)
- ✅ Include tests for new features
- ✅ Have a clear description of changes
- ✅ Build successfully in Docker

### GitHub Actions CI

When you open a PR, GitHub Actions will automatically:

1. **Run all tests** (backend and frontend)
2. **Check code formatting** (Ruff, ESLint, Prettier)
3. **Run type checking** (Ty)
4. **Generate coverage reports**
5. **Verify Docker builds**
6. **Run pre-commit hooks**

PRs cannot be merged until all checks pass.

## Commit Message Guidelines

Write clear, descriptive commit messages:

**Format:**
```
<type>: <short description>

<optional longer description>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat: add distance filter to contractor search

fix: resolve geolocation permission error

test: add unit tests for distance calculation

docs: update API endpoint documentation
```

## Project Structure

```
contractApp/
├── backend/                 # Python FastAPI backend
│   ├── app/
│   │   ├── routers/        # API endpoints
│   │   ├── models.py       # Database models
│   │   ├── schemas.py      # Pydantic schemas
│   │   └── main.py         # App entry point
│   ├── tests/              # Backend tests
│   └── requirements.txt
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── App.js          # Main app component
│   │   └── App.test.js     # Tests
│   └── package.json
├── .github/workflows/      # CI/CD workflows
└── .pre-commit-config.yaml # Pre-commit configuration
```

## Need Help?

- Check existing issues on GitHub
- Review the [README.md](README.md) for setup instructions
- Ask questions in GitHub Discussions or issues

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

Thank you for contributing to Contractor Finder!
