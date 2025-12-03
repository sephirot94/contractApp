from pydantic import BaseModel, EmailStr

from app.constants import Specialty
from app.models import PriceRange


class ContractorBase(BaseModel):
    name: str
    specialty: Specialty
    location: str
    latitude: float
    longitude: float
    price_range: PriceRange
    phone: str | None = None
    email: EmailStr | None = None
    description: str | None = None
    city_id: int


class ContractorCreate(ContractorBase):
    pass


class ContractorResponse(ContractorBase):
    id: int
    distance: float | None = None

    class Config:
        from_attributes = True
