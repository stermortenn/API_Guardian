from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from API_Guardian.api.deps import get_db
from API_Guardian.models.models import Endpoint
from API_Guardian.schemas.endpoint_schema import EndpointCreate

router = APIRouter()


@router.post("/")
def create_endpoint(endpoint: EndpointCreate, db: Session = Depends(get_db)):
    new_endpoint = Endpoint(**endpoint.dict())
    db.add(new_endpoint)
    db.commit()
    db.refresh(new_endpoint)
    return new_endpoint


@router.get("/")
def get_endpoints(db: Session = Depends(get_db)):
    return db.query(Endpoint).all()