# 🚀 Quick Start Guide

## First Time Setup (3 steps)

```bash
# 1. Clone and navigate
git clone <your-repo-url>
cd contractApp

# 2. Copy environment file
cp .env.example .env

# 3. Start everything!
make start
```

✅ **Done!** Open http://localhost:3000

---

## Daily Development Commands

```bash
# Start the app
make up                 # Start all services
make start              # Start + rebuild if needed

# Stop the app
make down               # Stop all services

# View what's happening
make logs               # See all logs
make status             # Check service status

# Run tests
make test               # Run all tests
make quality            # Run tests + linting + type-check

# Reset everything
make down               # Stop services
make start              # Fresh start with rebuild
```

---

## Common Tasks

### Add Sample Data
```bash
make seed
```

### View Backend Logs
```bash
make logs-backend
```

### Run Tests Before Committing
```bash
make quality           # Runs lint, type-check, and tests
```

### Database Shell Access
```bash
make db-shell
```

### Clean Up Everything
```bash
make clean             # Remove containers and temp files
```

---

## Service URLs

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

---

## Test the App

1. Open http://localhost:3000
2. Click "Use Current Location" or enter coordinates:
   - Sydney CBD: `-33.8688, 151.2093`
3. Select a specialty (electrician, plumber, etc.)
4. Click "Search"
5. View contractor cards with distance!

---

## Troubleshooting

### Ports Already in Use?
```bash
make down              # Stop all services
lsof -ti:3000 | xargs kill -9  # Kill process on port 3000
lsof -ti:8000 | xargs kill -9  # Kill process on port 8000
make up                # Start again
```

### Database Issues?
```bash
make db-reset          # Reset database (deletes all data)
```

### Docker Issues?
```bash
make clean-all         # Nuclear option: delete everything
make start             # Fresh start
```

### Still Having Issues?
```bash
make help              # See all available commands
```

---

## Need More Info?

- **Full Documentation**: See [README.md](README.md)
- **Contributing Guide**: See [CONTRIBUTING.md](CONTRIBUTING.md)
- **All Make Commands**: Run `make help`

---

## Production Readiness ✅

This setup uses Docker to ensure:
- ✅ Consistent environment (dev = prod)
- ✅ Isolated dependencies
- ✅ Easy deployment
- ✅ No "works on my machine" issues
- ✅ All tests run in same environment as production
