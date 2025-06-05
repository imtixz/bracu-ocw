from fastapi import APIRouter
from app.api.auth import router as auth_router

api_router = APIRouter()

# add some routes about profile and leaderboard here
api_router.include_router(auth_router)
