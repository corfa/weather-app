from core.config import AppSettings, app_settings

from clients.yandex_client import YandexClient, yandex_client
from clients.open_weater_client import OpenWeatherClient, open_weather_client


def get_config() -> AppSettings:
    return app_settings


def get_yandex_client() -> YandexClient:
    return yandex_client


def get_open_weather_client() -> OpenWeatherClient:
    return open_weather_client
