FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock* ./

# Install dependencies
# --system: Install packages into the system python, not a virtualenv
# --deploy: Ensure Pipfile.lock is up-to-date
# --ignore-pipfile: Install from Pipfile.lock only
RUN pipenv install --system --deploy --ignore-pipfile --dev

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application with auto-reload for development
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
