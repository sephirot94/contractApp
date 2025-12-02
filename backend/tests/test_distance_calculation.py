from app.routers.contractors import calculate_distance


def test_calculate_distance_same_location():
    """Test distance calculation between same coordinates."""
    distance = calculate_distance(-33.8688, 151.2093, -33.8688, 151.2093)
    assert distance == 0.0


def test_calculate_distance_sydney_to_parramatta():
    """Test distance calculation between Sydney CBD and Parramatta."""
    # Sydney CBD to Parramatta is approximately 23km
    distance = calculate_distance(-33.8688, 151.2093, -33.8151, 150.9989)
    assert 20 < distance < 25  # Should be around 23km


def test_calculate_distance_sydney_to_bondi():
    """Test distance calculation between Sydney CBD and Bondi."""
    # Sydney CBD to Bondi is approximately 7km
    distance = calculate_distance(-33.8688, 151.2093, -33.8908, 151.2743)
    assert 5 < distance < 10  # Should be around 7km


def test_calculate_distance_symmetry():
    """Test that distance calculation is symmetric."""
    distance1 = calculate_distance(-33.8688, 151.2093, -33.8151, 150.9989)
    distance2 = calculate_distance(-33.8151, 150.9989, -33.8688, 151.2093)
    assert distance1 == distance2


def test_calculate_distance_positive():
    """Test that distance is always positive."""
    distance = calculate_distance(-33.8688, 151.2093, -37.8136, 144.9631)
    assert distance > 0
