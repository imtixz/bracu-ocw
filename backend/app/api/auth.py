from fastapi import APIRouter
from app.core.db import DatabaseConnection

router = APIRouter(prefix="/auth", tags=["auth"])

db = DatabaseConnection()


@router.post("/request-otp")
async def request_otp() -> dict[str, str]:
    # fetch the user's data from the db
    # generate a token and return that
    return {"token": "abcd"}


@router.post("/verify-otp")
async def verify_otp() -> dict[str, str]:
    # refreshes the token and returns a new access token
    return {"token": "abcd"}


@router.post("/refresh")
async def refresh() -> str:
    return "refresh route"


@router.post("/logout")
async def logout() -> str:
    return "logout route"
