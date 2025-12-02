import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app
from app.models import Contractor, ContractorType, PriceRange

# Use in-memory SQLite for tests
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """Create a fresh database session for each test."""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """Create a test client with overridden database dependency."""

    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def sample_contractor(db_session):
    """Create a sample contractor for testing."""
    contractor = Contractor(
        name="Test Electrician",
        specialty=ContractorType.ELECTRICIAN,
        location="Sydney CBD",
        latitude=-33.8688,
        longitude=151.2093,
        price_range=PriceRange.MEDIUM,
        phone="+61 2 1234 5678",
        email="test@example.com",
        description="Test contractor",
    )
    db_session.add(contractor)
    db_session.commit()
    db_session.refresh(contractor)
    return contractor


@pytest.fixture
def sample_contractors(db_session):
    """Create multiple sample contractors for testing."""
    contractors = [
        Contractor(
            name="Sydney Electrician",
            specialty=ContractorType.ELECTRICIAN,
            location="Sydney CBD",
            latitude=-33.8688,
            longitude=151.2093,
            price_range=PriceRange.MEDIUM,
        ),
        Contractor(
            name="Parramatta Plumber",
            specialty=ContractorType.PLUMBER,
            location="Parramatta",
            latitude=-33.8151,
            longitude=150.9989,
            price_range=PriceRange.LOW,
        ),
        Contractor(
            name="Bondi Builder",
            specialty=ContractorType.BUILDER,
            location="Bondi",
            latitude=-33.8908,
            longitude=151.2743,
            price_range=PriceRange.HIGH,
        ),
    ]
    db_session.add_all(contractors)
    db_session.commit()
    return contractors
