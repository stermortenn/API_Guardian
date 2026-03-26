from fastapi import FastAPI
from app.api.routes import api_router, endpoint_routes, test_router

app = FastAPI()

app.include_router(api_router.router, prefix="/apis")
app.include_router(endpoint_routes.router, prefix="/endpoints")
app.include_router(test_router.router, prefix="/tests")