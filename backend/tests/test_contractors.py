import pytest
from app.models import ContractorType, PriceRange


def test_get_contractors_empty(client):
    """Test getting contractors when database is empty."""
    response = client.get("/api/contractors")
    assert response.status_code == 200
    assert response.json() == []


def test_get_contractors(client, sample_contractors):
    """Test getting all contractors."""
    response = client.get("/api/contractors")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3


def test_get_contractors_by_specialty(client, sample_contractors):
    """Test filtering contractors by specialty."""
    response = client.get("/api/contractors?specialty=electrician")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["specialty"] == "electrician"
    assert data[0]["name"] == "Sydney Electrician"


def test_get_contractors_with_location(client, sample_contractors):
    """Test getting contractors with location-based distance calculation."""
    # Search from Sydney CBD coordinates
    response = client.get("/api/contractors?latitude=-33.8688&longitude=151.2093")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3

    # Results should be sorted by distance
    # Sydney Electrician should be first (same location, distance ~0)
    assert data[0]["name"] == "Sydney Electrician"
    assert data[0]["distance"] is not None
    assert data[0]["distance"] < 1  # Very close

    # All should have distance field
    for contractor in data:
        assert "distance" in contractor
        assert contractor["distance"] is not None


def test_get_contractors_with_max_distance(client, sample_contractors):
    """Test filtering contractors by maximum distance."""
    # Search from Sydney CBD with 10km radius
    response = client.get(
        "/api/contractors?latitude=-33.8688&longitude=151.2093&max_distance=10"
    )
    assert response.status_code == 200
    data = response.json()

    # Should only get contractors within 10km
    for contractor in data:
        assert contractor["distance"] <= 10


def test_get_contractor_by_id(client, sample_contractor):
    """Test getting a specific contractor by ID."""
    contractor_id = sample_contractor.id
    response = client.get(f"/api/contractors/{contractor_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == contractor_id
    assert data["name"] == "Test Electrician"
    assert data["specialty"] == "electrician"


def test_get_contractor_not_found(client):
    """Test getting a non-existent contractor."""
    response = client.get("/api/contractors/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Contractor not found"


def test_create_contractor(client):
    """Test creating a new contractor."""
    new_contractor = {
        "name": "New Plumber",
        "specialty": "plumber",
        "location": "Melbourne",
        "latitude": -37.8136,
        "longitude": 144.9631,
        "price_range": "$$",
        "phone": "+61 3 1234 5678",
        "email": "newplumber@example.com",
        "description": "Expert plumber in Melbourne",
    }

    response = client.post("/api/contractors", json=new_contractor)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "New Plumber"
    assert data["specialty"] == "plumber"
    assert data["id"] is not None


def test_create_contractor_invalid_specialty(client):
    """Test creating a contractor with invalid specialty."""
    new_contractor = {
        "name": "Invalid Contractor",
        "specialty": "invalid_type",
        "location": "Sydney",
        "latitude": -33.8688,
        "longitude": 151.2093,
        "price_range": "$$",
    }

    response = client.post("/api/contractors", json=new_contractor)
    assert response.status_code == 422  # Validation error


def test_create_contractor_missing_fields(client):
    """Test creating a contractor with missing required fields."""
    incomplete_contractor = {
        "name": "Incomplete Contractor",
        "specialty": "electrician",
    }

    response = client.post("/api/contractors", json=incomplete_contractor)
    assert response.status_code == 422  # Validation error
