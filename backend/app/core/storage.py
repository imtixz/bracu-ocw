from fastapi import UploadFile
from app.core.config import settings

from pathlib import Path

import boto3
from fastapi import HTTPException
from botocore.exceptions import BotoCoreError, ClientError

from mypy_boto3_s3.client import S3Client

from fastapi.responses import FileResponse, StreamingResponse

from abc import ABC, abstractmethod


class FileStorage(ABC):
    def __init__(self):
        pass

    @abstractmethod
    async def store_file(self, file: UploadFile):
        pass

    @abstractmethod
    async def get_file(self, filename: str) -> FileResponse | StreamingResponse:
        pass


class FileStorageLocal(FileStorage):
    async def store_file(self, file: UploadFile):
        upload_dir = Path() / "uploads"
        data = await file.read()
        filename = str(file.filename)
        save_to = upload_dir / filename

        with open(save_to, "wb") as f:
            f.write(data)

    async def get_file(self, filename: str):
        upload_dir = Path() / "uploads"
        file_path = upload_dir / filename
        if not file_path.exists() or not file_path.is_file():
            raise HTTPException(status_code=404, detail="File not found")
        return FileResponse(file_path, filename=filename)


class FileStorageS3(FileStorage):
    async def get_s3_client(self) -> S3Client:
        R2_ENDPOINT_URL = settings.R2_ENDPOINT_URL
        R2_ACCESS_KEY_ID = settings.R2_ACCESS_KEY_ID
        R2_SECRET_ACCESS_KEY = settings.R2_SECRET_ACCESS_KEY

        client: S3Client = boto3.client(  # type: ignore
            service_name="s3",
            endpoint_url=R2_ENDPOINT_URL,
            aws_access_key_id=R2_ACCESS_KEY_ID,
            aws_secret_access_key=R2_SECRET_ACCESS_KEY,
            region_name="apac",
        )
        return client

    async def store_file(self, file: UploadFile):
        bucket_name = "bracu-ocw"
        data = await file.read()
        filename = str(file.filename)

        s3 = await self.get_s3_client()

        try:
            s3.put_object(Bucket=bucket_name, Key=filename, Body=data)
        except (BotoCoreError, ClientError) as e:
            raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

    async def get_file(self, filename: str):
        R2_BUCKET_NAME = "bracu-ocw"
        s3 = await self.get_s3_client()
        try:
            obj = s3.get_object(Bucket=R2_BUCKET_NAME, Key=filename)
            content = obj["Body"].read()
            content_type = obj.get("ContentType", "application/octet-stream")
        except (BotoCoreError, ClientError):
            raise HTTPException(status_code=404, detail="File not found in R2")

        return StreamingResponse(
            iter([content]),
            media_type=content_type,
            headers={"Content-Disposition": f'attachment; filename="{filename}"'},
        )
