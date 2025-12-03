"""City model for the Contractor Finder application."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class City(Base):
    """City model representing a city in the system."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    country = Column(String(100), nullable=False)

    # Relationship with contractors
    contractors = relationship("Contractor", back_populates="city")

    def __repr__(self) -> str:
        """Return string representation of City."""
        return f"<City(id={self.id}, name={self.name}, country={self.country})>"
