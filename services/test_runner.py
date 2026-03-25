import httpx
import time
from sqlalchemy.orm import Session
from app.models.models import TestCase, Endpoint, API, TestRun
from app.services.validator import validate_response


def run_test(test_case_id, db: Session):
    test_case = db.query(TestCase).filter(TestCase.id == test_case_id).first()
    endpoint = db.query(Endpoint).filter(Endpoint.id == test_case.endpoint_id).first()
    api = db.query(API).filter(API.id == endpoint.api_id).first()

    url = api.base_url + endpoint.path

    start = time.time()

    response = httpx.request(
        method=endpoint.method,
        url=url,
        headers=endpoint.headers,
        json=endpoint.body
    )

    execution_time = time.time() - start

    is_valid = validate_response(
        test_case.expected_status,
        response.status_code,
        test_case.expected_body,
        response.json() if response.content else {}
    )

    result = TestRun(
        test_case_id=test_case.id,
        status="pass" if is_valid else "fail",
        response_status=response.status_code,
        response_body=response.json(),
        execution_time=execution_time
    )

    db.add(result)
    db.commit()
    db.refresh(result)

    return result