import httpx

from base_client import WeatherClient
from core.config import app_settings


class YandexClient(WeatherClient):
    def __init__(self, host: str, api_key, timeout: int = 60) -> None:
        self.host = host
        self.api_key = api_key
        self.timeout = timeout

    def get_weather_forecast(self, lat: float, lon: float) -> dict:
        headers = {
            'X-Yandex-Weather-Key': self.api_key
        }
        with httpx.Client(timeout=self.timeout) as client:
            response = client.get(f'{self.hosthost}?lat={lat}&lon={lon}', headers=headers)
            response.raise_for_status()
        return response.json()


yandex_client = YandexClient(app_settings.yandex.host,
                             app_settings.yandex.api_key,
                             app_settings.yandex.timeout)
