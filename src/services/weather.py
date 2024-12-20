import httpx

from core.config import ConfigApp


def get_weather_forecast(config_app: ConfigApp, lat: float, lon: float) -> dict:
    headers = {
        'X-Yandex-Weather-Key': config_app.api_key_yandex
    }
    url = f'{config_app.weather_host}?lat={lat}&lon={lon}'
    with httpx.Client(timeout=config_app.timeout) as client:
        response = client.get(url, headers=headers)
        response.raise_for_status()
    return response.json()
