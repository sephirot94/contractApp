from sqlalchemy import Column, Integer, String, Float, Enum
from app.database import Base
import enum

class ContractorType(str, enum.Enum):
    ELECTRICIAN = "electrician"
    PLUMBER = "plumber"
    GAS = "gas"
    BUILDER = "builder"

class PriceRange(str, enum.Enum):
    LOW = "$"
    MEDIUM = "$$"
    HIGH = "$$$"
    PREMIUM = "$$$$"

class Contractor(Base):
    __tablename__ = "contractors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    specialty = Column(Enum(ContractorType), nullable=False)
    location = Column(String(200), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    price_range = Column(Enum(PriceRange), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    description = Column(String(500))
