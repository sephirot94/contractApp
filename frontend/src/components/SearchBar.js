import React from 'react';
import './SearchBar.css';

function SearchBar({ specialty, specialties, onSpecialtyChange, onSearch }) {
  return (
    <div className="search-bar">
      <div className="search-group">
        <label htmlFor="specialty">Contractor Type:</label>
        <select
          id="specialty"
          value={specialty}
          onChange={(e) => onSpecialtyChange(e.target.value)}
          className="search-input"
        >
          <option value="">All Specialties</option>
          {specialties.map((spec) => (
            <option key={spec} value={spec}>
              {spec.charAt(0).toUpperCase() + spec.slice(1)}
            </option>
          ))}
        </select>
      </div>

      <button onClick={onSearch} className="search-button">
        Search
      </button>
    </div>
  );
}

export default SearchBar;
