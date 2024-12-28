from fastapi import APIRouter
from .v1.weather import router as weather_router

router_v1 = APIRouter(prefix="/v1")
router_v1.include_router(weather_router)

router = APIRouter(prefix="/api")
router.include_router(router_v1, tags=["v1"])
