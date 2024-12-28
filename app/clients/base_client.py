
from abc import ABC, abstractmethod


class WeatherClient(ABC):
    def __init__(self, host: str, api_key: str, timeout: int) -> None:
        self.host = host
        self.api_key = api_key
        self.timeout = timeout

    @abstractmethod
    def get_weather_forecast(self, lat: float, lon: float) -> dict:
        pass
