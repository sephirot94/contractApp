import React, { useState } from 'react';
import './LocationInput.css';

function LocationInput({ location, onLocationChange, onUseCurrentLocation }) {
  const [latitude, setLatitude] = useState('');
  const [longitude, setLongitude] = useState('');

  const handleManualLocation = () => {
    if (latitude && longitude) {
      onLocationChange({
        latitude: parseFloat(latitude),
        longitude: parseFloat(longitude),
        name: 'Custom Location'
      });
    }
  };

  return (
    <div className="location-input">
      <div className="location-header">
        <h3>Location</h3>
        {location && (
          <span className="location-active">
            📍 {location.name} ({location.latitude.toFixed(4)}, {location.longitude.toFixed(4)})
          </span>
        )}
      </div>

      <div className="location-options">
        <button onClick={onUseCurrentLocation} className="location-button current">
          Use Current Location
        </button>

        <div className="manual-location">
          <input
            type="number"
            placeholder="Latitude (e.g., -33.8688)"
            value={latitude}
            onChange={(e) => setLatitude(e.target.value)}
            className="location-coord-input"
            step="0.0001"
          />
          <input
            type="number"
            placeholder="Longitude (e.g., 151.2093)"
            value={longitude}
            onChange={(e) => setLongitude(e.target.value)}
            className="location-coord-input"
            step="0.0001"
          />
          <button onClick={handleManualLocation} className="location-button manual">
            Set Location
          </button>
        </div>
      </div>

      <div className="location-hint">
        Tip: Sydney CBD is approximately -33.8688, 151.2093
      </div>
    </div>
  );
}

export default LocationInput;
