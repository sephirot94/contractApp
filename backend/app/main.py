from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import contractors
import os

app = FastAPI(title="Contractor Finder API")

# CORS configuration
origins = os.getenv("BACKEND_CORS_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(contractors.router, prefix="/api", tags=["contractors"])

@app.get("/")
def read_root():
    return {"message": "Contractor Finder API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
