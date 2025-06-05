from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.db import DatabaseConnection

from app.api.main import api_router
from app.core.config import settings

db = DatabaseConnection()


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def index() -> dict[str, str]:
    return {"status": "active"}


app.include_router(api_router, prefix=settings.API_V1_STR)


# @app.get("/me")
# async def profile() -> dict[str, str]:
#     pass


# @app.post("/me")
# async def update_profile() -> dict[str, str]:
#     pass


def main():
    print("initiated router")


if __name__ == "__main__":
    main()
