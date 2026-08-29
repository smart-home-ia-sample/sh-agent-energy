import os

from fastapi import FastAPI

from app.routes import mount
from smart_home_common import configure_logging

configure_logging(service="energy", level=os.environ.get("LOG_LEVEL", "INFO"))

app = FastAPI(title="Smart Home AI - Energy Agent")
mount(app)
