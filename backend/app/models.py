from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.constants import Specialty
from app.database import Base


class City(Base):
    """City model representing a city in the system."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    country = Column(String(100), nullable=False)

    # Relationship with contractors
    contractors = relationship("Contractor", back_populates="city")


class Contractor(Base):
    __tablename__ = "contractors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    specialty = Column(Enum(Specialty), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    phone = Column(String(25))
    email = Column(String(75))
    description = Column(String(500))
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False, index=True)

    # Relationship with city
    city = relationship("City", back_populates="contractors")
