from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api import router
from core.config import app_settings

if app_settings.show_ui:
    app = FastAPI(
        default_response_class=ORJSONResponse
    )
else:
    app = FastAPI(
        docs_url=None,
        redoc_url=None,
        default_response_class=ORJSONResponse
    )

app.include_router(router)
