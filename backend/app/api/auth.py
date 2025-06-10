from fastapi import APIRouter, Depends
from sqlmodel import Session
from pydantic import BaseModel
from app.core.db import DatabaseConnection

router = APIRouter(prefix="/auth", tags=["auth"])

db = DatabaseConnection()


class RequestOtpBody(BaseModel):
    email: str


@router.post("/request-otp")
async def request_otp(
    body: RequestOtpBody, session: Session = Depends(db.get_session)
) -> None:
    # accepts an email address in body
    # generates and saves otp (with expiry)
    # sends an email
    # output is just 200

    # generate an otp? how
    # how do i save the otp?
    # how do i send the email?

    return


class VerifyOtpBody(BaseModel):
    email: str
    otp: str


@router.post("/verify-otp")
async def verify_otp(body: VerifyOtpBody) -> dict[str, str]:
    # accepts an email address and otp code in body
    # check if the otp is valid
    # if this is user's first time, create new user
    # issue access token + refresh token
    # set http-only refresh token
    return {"token": "abcd"}


@router.post("/refresh")
async def refresh() -> str:
    # input is refresh token in cookie
    # returns an access token if refresh token is valid
    # also before returning, refresh the refresh token (store in redis maybe?)
    return "refresh route"


@router.post("/logout")
async def logout() -> str:
    # remove the refresh token from the http-only cookie
    return "logout route"
