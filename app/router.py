from fastapi import APIRouter
from .geolocation import routes as geolocation

api_router = APIRouter()
api_router.include_router(geolocation.router, tags=["geolocation"], prefix="/geolocation")