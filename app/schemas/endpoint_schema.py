from pydantic import BaseModel
from typing import Optional, Dict 

class EndpointCreate(BaseModel):
    api_id: str
    path: str
    method: str
    headers: Optional[Dict] = None
    body: Optional[Dict] = None

    