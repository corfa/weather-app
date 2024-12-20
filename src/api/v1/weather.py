from fastapi import Depends, APIRouter, HTTPException
import httpx

from core.config import ConfigApp
from services.weather import get_weather_forecast
from api.v1.depends import get_config
from schemas.weather import WeatherRequest

router = APIRouter()


@router.post("/weather")
def weather(request: WeatherRequest, config: ConfigApp = Depends(get_config)):
    try:
        forecast: dict = get_weather_forecast(config, request.lat, request.lon)
        return {"status": "success", "data": forecast}
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Error fetching weather data")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
