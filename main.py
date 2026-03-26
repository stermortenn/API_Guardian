from fastapi import FastAPI
from API_Guardian.api.routes import api_router, endpont_routes
from API_Guardian.services import test_router

app = FastAPI()

app.include_router(api_router.router, prefix="/apis")
app.include_router(endpont_routes.router, prefix="/endpoints")
app.include_router(test_router.router, prefix="/tests")