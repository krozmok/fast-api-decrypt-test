from fastapi import FastAPI

from app.database.database import init_db
from app.routers import freqlang
import os

decrypt_app = FastAPI()

decrypt_app.include_router(freqlang.router)

@decrypt_app.on_event("startup")
async def startup_event():
    init_db(decrypt_app)
    
#Comentado por si acaso
#postgresql_string = 'postgres://postgres:n3clFrUr1sLsw5W6eFO&@localhost:5432/freqlangdb'

# register_tortoise(
#     decrypt_app,
#     db_url=str(os.environ.get("POSTGRES_CONNECTION_STRING")),
#     modules={'models': ['app.models.models', 'aerich.models']},
#     generate_schemas=True,
#     add_exception_handlers=True,
# )

# register_tortoise(
#     app,
#     db_url='sqlite://db.sqlite3',/
#     modules={'models': ['models.models']},
#     generate_schemas=True,
#     add_exception_handlers=True,
# )