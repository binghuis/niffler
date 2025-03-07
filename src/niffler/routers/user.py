from fastapi import APIRouter

from niffler.schemas.user import UserResponse
from niffler.services.user import get_all_users

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserResponse])
async def list_users(skip: int = 0, limit: int = 10):
    return await get_all_users(skip, limit)
