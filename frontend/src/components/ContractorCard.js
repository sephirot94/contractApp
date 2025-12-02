import React from 'react';
import './ContractorCard.css';

function ContractorCard({ contractor }) {
  const getSpecialtyIcon = (specialty) => {
    const icons = {
      electrician: '⚡',
      plumber: '🔧',
      gas: '🔥',
      builder: '🏗️'
    };
    return icons[specialty] || '👷';
  };

  const getPriceColor = (priceRange) => {
    const colors = {
      '$': '#10b981',
      '$$': '#3b82f6',
      '$$$': '#f59e0b',
      '$$$$': '#8b5cf6'
    };
    return colors[priceRange] || '#6b7280';
  };

  return (
    <div className="contractor-card">
      <div className="card-header">
        <div className="specialty-icon">
          {getSpecialtyIcon(contractor.specialty)}
        </div>
        <div className="card-title">
          <h3>{contractor.name}</h3>
          <span className="specialty-badge">
            {contractor.specialty.charAt(0).toUpperCase() + contractor.specialty.slice(1)}
          </span>
        </div>
      </div>

      <div className="card-body">
        <div className="card-info">
          <span className="info-icon">📍</span>
          <span>{contractor.location}</span>
        </div>

        {contractor.distance && (
          <div className="card-info distance">
            <span className="info-icon">📏</span>
            <span>{contractor.distance} km away</span>
          </div>
        )}

        <div className="card-info">
          <span className="info-icon">💰</span>
          <span
            className="price-range"
            style={{ color: getPriceColor(contractor.price_range) }}
          >
            {contractor.price_range}
          </span>
        </div>

        {contractor.description && (
          <p className="description">{contractor.description}</p>
        )}
      </div>

      <div className="card-footer">
        {contractor.phone && (
          <a href={`tel:${contractor.phone}`} className="contact-button">
            📞 Call
          </a>
        )}
        {contractor.email && (
          <a href={`mailto:${contractor.email}`} className="contact-button">
            ✉️ Email
          </a>
        )}
      </div>
    </div>
  );
}

export default ContractorCard;
