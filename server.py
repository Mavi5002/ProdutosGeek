from fastapi import FastAPI
from produtos_controllers import router
from database import sync_database, get_engine

app = FastAPI()

sync_database(get_engine())

app.include_router(router,prefix="/api/rides")
