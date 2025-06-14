from fastapi import FastAPI, Depends, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.db import DatabaseConnection
from app.api.main import api_router
from app.core.config import settings
from redis import Redis

from app.core.storage import FileStorageLocal, FileStorageS3, FileStorage


db = DatabaseConnection()
storage = FileStorageLocal() if settings.ENVIRONEMNT == "DEV" else FileStorageS3()


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.init_db()

    try:
        yield
    finally:
        db.close_db()


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index() -> dict[str, str]:
    return {"status": "active"}


@app.get("/counter")
async def get_counter(redis: Redis = Depends(lambda: db.redis)):
    value = str(redis.get("counter"))
    return {"counter": int(value) if value.isnumeric() else 0}


@app.post("/counter/increment")
async def increment_counter(redis: Redis = Depends(lambda: db.redis)):
    value = redis.incr("counter")
    return {"counter": value}


@app.post("/upload-file")
async def create_upload_file(
    file: UploadFile, storage: FileStorage = Depends(lambda: storage)
):
    await storage.store_file(file=file)
    return {"filename": file.filename}


@app.get("/uploads/{filename}")
async def get_uploaded_file(filename: str):
    return await storage.get_file(filename)


app.include_router(api_router, prefix=settings.API_V1_STR)


print(settings.ENVIRONEMNT, "THIS IS THE ENVIRONMENT")


def main():
    print("initiated router")


if __name__ == "__main__":
    main()
