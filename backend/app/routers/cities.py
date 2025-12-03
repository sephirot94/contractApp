"""Cities router for the Contractor Finder API."""


from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import City

router = APIRouter(prefix="/cities", tags=["cities"])


class CityResponse(BaseModel):
    """Response model for a city."""

    id: int
    name: str
    country: str

    class Config:
        """Pydantic config."""

        from_attributes = True


@router.get("/", response_model=list[CityResponse])
def get_cities(db: Session = Depends(get_db)) -> list[City]:
    """
    Get all cities.

    Args:
        db: Database session

    Returns:
        List of all cities in the system
    """
    return db.query(City).order_by(City.name).all()
