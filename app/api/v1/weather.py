from fastapi import Depends, APIRouter, HTTPException
import httpx

from clients.yandex_client import YandexClient
from clients.open_weater_client import OpenWeatherClient
from api.v1.depends import get_yandex_client, get_open_weather_client
from schemas.weather import WeatherRequest

router = APIRouter(prefix="/weather")


@router.post("/yandex")
def get_weather_from_yandex(request: WeatherRequest, yandex_client: YandexClient = Depends(get_yandex_client)):
    try:
        forecast: dict = yandex_client.get_weather_forecast(request.lat, request.lon)
        return {"status": "success", "data": forecast}
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Error fetching weather data")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/open-weather")
def get_weather_from_open_weather_map(request: WeatherRequest,
                                      open_weather_client: OpenWeatherClient = Depends(get_open_weather_client)):
    try:
        forecast: dict = open_weather_client.get_weather_forecast(request.lat, request.lon)
        return {"status": "success", "data": forecast}
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Error fetching weather data")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
