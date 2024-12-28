from dataclasses import dataclass
from pathlib import Path
import pyhocon


@dataclass
class ConfigApp:
    filename: str = str(Path(__file__).parent.parent / "config.conf")
    api_key_yandex: str = ''
    show_ui: bool = False
    weather_host: str = ''
    timeout: int = 60

    def __post_init__(self) -> None:
        config_path = Path(self.filename).resolve()

        if not config_path.is_file():
            raise FileNotFoundError(f"Config file not found at: {config_path}")

        config_data = pyhocon.ConfigFactory.parse_file(config_path)

        self.api_key_yandex = config_data.get('api_key_yandex', '')
        self.show_ui = config_data.get('show_ui', False)
        self.weather_host = config_data.get('weather_host', '')
        self.timeout = config_data.get('timeout', 60)


app_settings = ConfigApp()
