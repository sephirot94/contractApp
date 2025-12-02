# Contractor Finder

A full-stack web application for finding and connecting with local contractors including electricians, plumbers, gas fitters, and builders. The app features location-based search to find contractors nearest to you.

## Tech Stack

- **Frontend**: React.js
- **Backend**: Python FastAPI
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Containerization**: Docker & Docker Compose

## Features

- Search contractors by specialty (electrician, plumber, gas fitter, builder)
- Location-based search with distance calculation
- View contractor details including:
  - Name and specialty
  - Service area/location
  - Price range
  - Contact information (phone & email)
  - Description of services
- Responsive design for mobile and desktop
- Geolocation support to find contractors near you

## Project Structure

```
contractApp/
├── backend/                # FastAPI backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py        # FastAPI app entry point
│   │   ├── database.py    # Database configuration
│   │   ├── models.py      # SQLAlchemy models
│   │   ├── schemas.py     # Pydantic schemas
│   │   ├── routers/       # API routes
│   │   └── seed_data.py   # Database seeding script
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/              # React frontend
│   ├── public/
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── App.js
│   │   └── index.js
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml     # Multi-container orchestration
├── .env.example          # Environment variables template
└── README.md
```

## Quick Start

### Prerequisites

- Docker Desktop installed and running
- Git

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd contractApp
   ```

2. **Create environment file**
   ```bash
   cp .env.example .env
   ```

   The default settings in `.env.example` work out of the box for local development.

3. **Start the application**
   ```bash
   docker-compose up --build
   ```

   This will:
   - Start MySQL database on port 3306
   - Start FastAPI backend on port 8000
   - Start React frontend on port 3000
   - Automatically create database tables

4. **Seed the database with sample data**

   In a new terminal window, run:
   ```bash
   docker-compose exec backend python -m app.seed_data
   ```

5. **Access the application**
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend API: [http://localhost:8000](http://localhost:8000)
   - API Documentation: [http://localhost:8000/docs](http://localhost:8000/docs)

## Usage

### Searching for Contractors

1. Open the app at [http://localhost:3000](http://localhost:3000)
2. Use the search filters:
   - Select a contractor specialty (or leave as "All Specialties")
   - Click "Use Current Location" to find contractors near you
   - Or manually enter latitude/longitude coordinates
3. Click "Search" to see results
4. Contractors will be displayed as cards showing:
   - Name and specialty
   - Location and distance (if location search used)
   - Price range
   - Contact buttons (call/email)

### Sample Locations (Sydney, Australia)

The seeded data includes contractors around Sydney:
- Sydney CBD: -33.8688, 151.2093
- Parramatta: -33.8151, 150.9989
- Bondi: -33.8908, 151.2743

## API Endpoints

### GET /api/contractors
Get all contractors with optional filtering

**Query Parameters:**
- `specialty` (optional): Filter by contractor type (electrician, plumber, gas, builder)
- `latitude` (optional): User's latitude for distance calculation
- `longitude` (optional): User's longitude for distance calculation
- `max_distance` (optional): Maximum distance in km (default: 50)

**Example:**
```bash
curl "http://localhost:8000/api/contractors?specialty=electrician&latitude=-33.8688&longitude=151.2093&max_distance=20"
```

### GET /api/contractors/{contractor_id}
Get a specific contractor by ID

### POST /api/contractors
Create a new contractor

**Request Body:**
```json
{
  "name": "Example Plumbing",
  "specialty": "plumber",
  "location": "Sydney CBD",
  "latitude": -33.8688,
  "longitude": 151.2093,
  "price_range": "$$",
  "phone": "+61 2 1234 5678",
  "email": "contact@example.com",
  "description": "Professional plumbing services"
}
```

### GET /api/specialties
Get list of available contractor specialties

## Development

### Running without Docker

**Backend:**
```bash
cd backend
pip install pipenv
pipenv install --dev
pipenv run uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

### Dependency Management

**Backend (Python):**
This project uses **Pipfile** for Python dependency management instead of requirements.txt.

- Install dependencies: `pipenv install --dev`
- Add a package: `pipenv install package-name`
- Add a dev package: `pipenv install --dev package-name`
- Update dependencies: `pipenv update`
- Generate lock file: `pipenv lock`

**Frontend (JavaScript):**
Uses npm with package.json for dependency management.

### Code Quality & Testing

This project uses pre-commit hooks to ensure code quality. The hooks run automatically on every commit.

#### Setting up Pre-commit Hooks

1. **Install pre-commit** (one-time setup):
   ```bash
   pip install pre-commit
   ```

2. **Install the git hook scripts**:
   ```bash
   pre-commit install
   ```

3. **Run hooks manually** (optional):
   ```bash
   pre-commit run --all-files
   ```

#### Linting, Formatting & Type Checking

**Backend (Python):**
- **Ruff**: Fast Python linter and formatter
  ```bash
  cd backend
  pipenv run ruff check .              # Lint
  pipenv run ruff check . --fix        # Lint with auto-fix
  pipenv run ruff format .             # Format code
  ```

- **Ty**: Astral's blazing-fast type checker
  ```bash
  cd backend
  pipenv run ty check                  # Run type checker
  pipenv run ty check --watch          # Watch mode
  ```

**Frontend (JavaScript):**
- **ESLint**: JavaScript linter
  ```bash
  cd frontend
  npm run lint              # Check for issues
  npm run lint:fix          # Fix issues automatically
  ```

- **Prettier**: Code formatter
  ```bash
  cd frontend
  npm run format            # Format code
  npm run format:check      # Check formatting
  ```

#### Running Tests

**Backend Tests (pytest):**
```bash
cd backend
pipenv run pytest                      # Run all tests
pipenv run pytest --cov=app            # Run with coverage
pipenv run pytest -v                   # Verbose output
pipenv run pytest tests/test_main.py   # Run specific test file
```

**Frontend Tests (Jest):**
```bash
cd frontend
npm test                    # Run all tests
npm run test:watch          # Run in watch mode
npm run test:coverage       # Run with coverage report
```

#### Test Coverage

Both backend and frontend tests include coverage reporting:
- Backend: Coverage reports are in `backend/htmlcov/`
- Frontend: Coverage reports are in `frontend/coverage/`

### Pre-commit Hooks

The following checks run automatically on every commit:

1. **General Checks:**
   - Trailing whitespace removal
   - End-of-file fixer
   - YAML/JSON validation
   - Large file check
   - Merge conflict detection

2. **Python (Backend):**
   - Ruff linter with auto-fix
   - Ruff formatter
   - Ty type checker

3. **JavaScript (Frontend):**
   - ESLint with auto-fix
   - Prettier formatter

If any check fails, the commit will be blocked. Fix the issues and try again.

### CI/CD - GitHub Actions

This project includes GitHub Actions workflows that run on every pull request:

#### PR Checks Workflow
Automatically runs on PRs to `main` or `develop`:

1. **Backend Tests & Linting**:
   - Ruff linting and formatting checks
   - Ty type checking
   - pytest with coverage reporting
   - MySQL service for integration tests

2. **Frontend Tests & Linting**:
   - ESLint checks
   - Prettier checks
   - Jest tests with coverage reporting

3. **Build Check**:
   - Docker build verification for both services
   - Ensures containers build successfully

4. **Coverage Reports**:
   - Uploads to Codecov for both frontend and backend

#### Pre-commit Workflow
Validates that all pre-commit hooks pass in CI environment.

### GitHub Actions Setup

The workflows are located in [.github/workflows/](.github/workflows/):
- `pr-checks.yml`: Main PR validation workflow
- `pre-commit.yml`: Pre-commit hook validation

**No additional setup required!** The workflows run automatically when you:
- Create a pull request
- Push commits to a PR
- Push to main or develop branches

**Optional Codecov Setup:**
If you want coverage reports, add your repository to [Codecov](https://codecov.io/) and add the `CODECOV_TOKEN` to your repository secrets.

### Stopping the Application

```bash
docker-compose down
```

To also remove the database volume:
```bash
docker-compose down -v
```

## Database

The application uses MySQL 8.0 by default. The database schema includes:

**Contractors Table:**
- id (Primary Key)
- name
- specialty (electrician, plumber, gas, builder)
- location
- latitude
- longitude
- price_range ($, $$, $$$, $$$$)
- phone
- email
- description

## Deployment Considerations

For production deployment, consider:

1. **Database**: Use AWS RDS (MySQL or PostgreSQL)
   - RDS provides automated backups, scaling, and high availability
   - PostgreSQL offers more advanced features but both work well for this app
   - Update `DATABASE_URL` in your environment variables

2. **Backend**: Deploy to:
   - AWS ECS/Fargate (containerized)
   - AWS Elastic Beanstalk
   - Heroku
   - Railway

3. **Frontend**: Deploy to:
   - Vercel
   - Netlify
   - AWS S3 + CloudFront
   - AWS Amplify

4. **Environment Variables**:
   - Set secure passwords for production
   - Update CORS origins to match your frontend domain
   - Use secrets management (AWS Secrets Manager, etc.)

5. **Security**:
   - Enable HTTPS
   - Implement rate limiting
   - Add authentication/authorization if needed
   - Validate and sanitize all inputs

## Future Enhancements

- User authentication and contractor profiles
- Review and rating system
- Booking/scheduling functionality
- Image upload for contractor portfolios
- Advanced search filters (price range, availability, ratings)
- Map view of contractors
- Email notifications
- Payment integration

## License

MIT
