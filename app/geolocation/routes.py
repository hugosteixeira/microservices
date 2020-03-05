from fastapi import APIRouter
from .controller import Controller
from starlette.requests import Request

router = APIRouter()
controller = Controller()

@router.get("/")
def get(request: Request):
    return controller.get_geolocation(request)