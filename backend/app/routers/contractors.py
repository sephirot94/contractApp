from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models import Contractor, ContractorType
from app.schemas import ContractorResponse, ContractorCreate
import math

router = APIRouter()

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate distance between two coordinates using Haversine formula.
    Returns distance in kilometers.
    """
    R = 6371  # Earth's radius in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return round(distance, 2)

@router.get("/contractors", response_model=List[ContractorResponse])
def get_contractors(
    specialty: Optional[ContractorType] = None,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
    max_distance: Optional[float] = Query(None, description="Maximum distance in km"),
    db: Session = Depends(get_db)
):
    """
    Get contractors filtered by specialty and/or location.
    Results are sorted by distance if lat/lon provided.
    """
    query = db.query(Contractor)

    if specialty:
        query = query.filter(Contractor.specialty == specialty)

    contractors = query.all()

    # Calculate distances if location provided
    if latitude is not None and longitude is not None:
        contractor_list = []
        for contractor in contractors:
            distance = calculate_distance(
                latitude, longitude,
                contractor.latitude, contractor.longitude
            )

            # Filter by max distance if specified
            if max_distance is None or distance <= max_distance:
                contractor_dict = {
                    "id": contractor.id,
                    "name": contractor.name,
                    "specialty": contractor.specialty,
                    "location": contractor.location,
                    "latitude": contractor.latitude,
                    "longitude": contractor.longitude,
                    "price_range": contractor.price_range,
                    "phone": contractor.phone,
                    "email": contractor.email,
                    "description": contractor.description,
                    "distance": distance
                }
                contractor_list.append(ContractorResponse(**contractor_dict))

        # Sort by distance
        contractor_list.sort(key=lambda x: x.distance)
        return contractor_list

    return [ContractorResponse.model_validate(c) for c in contractors]

@router.get("/contractors/{contractor_id}", response_model=ContractorResponse)
def get_contractor(contractor_id: int, db: Session = Depends(get_db)):
    """Get a specific contractor by ID."""
    contractor = db.query(Contractor).filter(Contractor.id == contractor_id).first()
    if not contractor:
        raise HTTPException(status_code=404, detail="Contractor not found")
    return contractor

@router.post("/contractors", response_model=ContractorResponse)
def create_contractor(contractor: ContractorCreate, db: Session = Depends(get_db)):
    """Create a new contractor."""
    db_contractor = Contractor(**contractor.model_dump())
    db.add(db_contractor)
    db.commit()
    db.refresh(db_contractor)
    return db_contractor

@router.get("/specialties")
def get_specialties():
    """Get list of available contractor specialties."""
    return {"specialties": [e.value for e in ContractorType]}
