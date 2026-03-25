from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from API_Guardian.api.deps import get_db
from API_Guardian.models.models import TestCase
from API_Guardian.schemas.test_schema import TestCaseCreate
from API_Guardian.services.test_runner import run_test

router = APIRouter()


@router.post("/")
def create_test(test: TestCaseCreate, db: Session = Depends(get_db)):
    new_test = TestCase(**test.dict())
    db.add(new_test)
    db.commit()
    db.refresh(new_test)
    return new_test


@router.post("/{test_id}/run")
def run_test_case(test_id: str, db: Session = Depends(get_db)):
    return run_test(test_id, db)