def test_read_root(client):
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Contractor Finder API is running"}


def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_specialties(client):
    """Test getting list of specialties."""
    response = client.get("/api/specialties")
    assert response.status_code == 200
    data = response.json()
    assert "specialties" in data
    assert len(data["specialties"]) == 4
    assert "electrician" in data["specialties"]
    assert "plumber" in data["specialties"]
    assert "gas" in data["specialties"]
    assert "builder" in data["specialties"]
