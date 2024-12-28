import httpx

from base_client import WeatherClient
from core.config import app_settings


class OpenWeatherClient(WeatherClient):
    def __init__(self, host: str, api_key, timeout: int = 60) -> None:
        self.host = host
        self.api_key = api_key
        self.timeout = timeout

    def get_weather_forecast(self, lat: float, lon: float) -> dict:
        with httpx.Client(timeout=self.timeout) as client:
            response = client.get(f'https://{self.host}/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}')
            response.raise_for_status()
        return response.json()


open_weather_client = OpenWeatherClient(app_settings.open_weather.host,
                                        app_settings.open_weather.host,
                                        app_settings.open_weather.timeout)
