from pydantic import BaseModel, EmailStr
from typing import Optional
from app.models import ContractorType, PriceRange

class ContractorBase(BaseModel):
    name: str
    specialty: ContractorType
    location: str
    latitude: float
    longitude: float
    price_range: PriceRange
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    description: Optional[str] = None

class ContractorCreate(ContractorBase):
    pass

class ContractorResponse(ContractorBase):
    id: int
    distance: Optional[float] = None

    class Config:
        from_attributes = True
