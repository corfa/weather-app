from dataclasses import dataclass
import os
from pyhocon import ConfigFactory


@dataclass
class YandexSettings:
    api_key: str = ''
    host: str = ''
    timeout: int = 60


@dataclass
class OpenWeatherSettings:
    api_key: str = ''
    host: str = ''
    timeout: int = 60


@dataclass
class AppSettings:
    debug_mode: bool = False
    yandex: YandexSettings = None
    open_weather: OpenWeatherSettings = None


def load_config(file_path: str) -> AppSettings:
    config_data = ConfigFactory.parse_file(file_path)
    app_config = config_data.get('app', {})

    yandex_config = app_config.get('yandex', {})
    open_weather_config = app_config.get('open_weather', {})

    app_settings = AppSettings(
        debug_mode=bool(app_config.get('debug_mode', False)),
        yandex=YandexSettings(**yandex_config),
        open_weather=OpenWeatherSettings(**open_weather_config)
    )
    return app_settings


app_settings = load_config(os.getenv('CONFIG_PATH', 'config.conf'))
