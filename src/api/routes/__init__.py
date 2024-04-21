from fastapi import FastAPI

from api.routes import upload, statisctics


def setup_routes(app: FastAPI) -> None:
    app.include_router(upload.router)
    app.include_router(statisctics.router)
