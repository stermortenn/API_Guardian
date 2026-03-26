from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.models import TestCase
from app.schemas.test_schema import TestCaseCreate
from app.services.test_runner import run_test

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