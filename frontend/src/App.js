import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import SearchBar from './components/SearchBar';
import ContractorCard from './components/ContractorCard';
import LocationInput from './components/LocationInput';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const [contractors, setContractors] = useState([]);
  const [loading, setLoading] = useState(false);
  const [specialty, setSpecialty] = useState('');
  const [location, setLocation] = useState(null);
  const [specialties, setSpecialties] = useState([]);
  const [cities, setCities] = useState([]);
  const [selectedCity, setSelectedCity] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    fetchSpecialties();
    fetchCities();
  }, []);

  const fetchSpecialties = async () => {
    try {
      const response = await axios.get(`${API_URL}/api/specialties`);
      setSpecialties(response.data.specialties);
    } catch (err) {
      console.error('Error fetching specialties:', err);
    }
  };

  const fetchCities = async () => {
    try {
      const response = await axios.get(`${API_URL}/api/cities`);
      setCities(response.data);
    } catch (err) {
      console.error('Error fetching cities:', err);
    }
  };

  const fetchContractors = async (filters = {}) => {
    setLoading(true);
    setError('');
    try {
      const params = {};
      if (filters.cityId) params.city_id = filters.cityId;
      if (filters.specialty) params.specialty = filters.specialty;
      if (filters.location) {
        params.latitude = filters.location.latitude;
        params.longitude = filters.location.longitude;
        params.max_distance = 50; // 50km radius
      }

      const response = await axios.get(`${API_URL}/api/contractors`, { params });
      setContractors(response.data);
    } catch (err) {
      console.error('Error fetching contractors:', err);
      setError('Failed to load contractors. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = () => {
    fetchContractors({ cityId: selectedCity, specialty, location });
  };

  const handleCityChange = (cityId) => {
    setSelectedCity(cityId);
  };

  const handleSpecialtyChange = (newSpecialty) => {
    setSpecialty(newSpecialty);
  };

  const handleLocationChange = (newLocation) => {
    setLocation(newLocation);
  };

  const handleUseCurrentLocation = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const newLocation = {
            latitude: position.coords.latitude,
            longitude: position.coords.longitude,
            name: 'Your Location',
          };
          setLocation(newLocation);
          fetchContractors({ specialty, location: newLocation });
        },
        (error) => {
          console.error('Error getting location:', error);
          setError('Failed to get your location. Please enter manually.');
        }
      );
    } else {
      setError('Geolocation is not supported by your browser.');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Find Your Contractor</h1>
        <p>Connect with local electricians, plumbers, gas fitters, and builders</p>
      </header>

      <main className="App-main">
        <div className="search-section">
          <div className="city-selector">
            <label htmlFor="city-select">Select City:</label>
            <select
              id="city-select"
              value={selectedCity}
              onChange={(e) => handleCityChange(e.target.value)}
              className="city-dropdown"
            >
              <option value="">All Cities</option>
              {cities.map((city) => (
                <option key={city.id} value={city.id}>
                  {city.name}, {city.country}
                </option>
              ))}
            </select>
          </div>

          <SearchBar
            specialty={specialty}
            specialties={specialties}
            onSpecialtyChange={handleSpecialtyChange}
            onSearch={handleSearch}
          />

          <LocationInput
            location={location}
            onLocationChange={handleLocationChange}
            onUseCurrentLocation={handleUseCurrentLocation}
          />
        </div>

        {error && <div className="error-message">{error}</div>}

        {loading ? (
          <div className="loading">Loading contractors...</div>
        ) : (
          <div className="contractors-grid">
            {contractors.length > 0 ? (
              contractors.map((contractor) => (
                <ContractorCard key={contractor.id} contractor={contractor} />
              ))
            ) : (
              <div className="no-results">
                <p>No contractors found. Try adjusting your search criteria.</p>
              </div>
            )}
          </div>
        )}
      </main>

      <footer className="App-footer">
        <p>&copy; 2025 Contractor Finder. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
