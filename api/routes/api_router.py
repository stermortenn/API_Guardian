from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from API_Guardian.api.deps import get_db
from API_Guardian.models.models import API
from API_Guardian.schemas.api_schema import APICreate

router = APIRouter()


@router.post("/")
def create_api(api: APICreate, db: Session = Depends(get_db)):
    new_api = API(name=api.name, base_url=api.base_url)
    db.add(new_api)
    db.commit()
    db.refresh(new_api)
    return new_api


@router.get("/")
def get_apis(db: Session = Depends(get_db)):
    return db.query(API).all()