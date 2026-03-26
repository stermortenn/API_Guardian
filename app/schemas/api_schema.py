from pydantic import BaseModel

class APICreate(BaseModel):
    name: str
    base_url: str

class APIResponse(BaseModel):
    id: str
    name: str
    base_url: str

    class Config:
        from_attributes = True