from pydantic import BaseModel
from typing import Optional, Dict

class TestCaseCreate(BaseModel):
    endpoint_id: str
    name: str
    expected_status: int 
    expected_body: Optional[Dict] = None