from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

import os

from app.config import settings

def init_db(app: FastAPI) -> None:
    Tortoise.init_models(["app.models.models"], "models")
    register_tortoise(
        app
        #db_url=os.environ.get("POSTGRES_CONNECTION_STRING"),
        ,db_url=settings.db_url
        ,modules={"models":["app.models.models"]}
        ,generate_schemas=True
        ,add_exception_handlers=True
    )
    Tortoise.generate_schemas()

TORTOISE_ORM = {
    "connections": {"default": settings.db_url}
    #{"default": os.environ.get("POSTGRES_CONNECTION_STRING")}
    ,"apps": {
        "models": {
            "models": ["app.models.models",]
            ,"default_connection": "default"
        },
    },
}
