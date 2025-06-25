
from fastapi import FastAPI
from api.projection_engine import router as projection_router
from api.download import router as download_router

app = FastAPI()
app.include_router(projection_router, prefix="/api")
app.include_router(download_router, prefix="/api")
