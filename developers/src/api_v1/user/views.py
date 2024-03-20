from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api_v1.user import crud
from src.api_v1.user.schemas import UserCreate, User
from src.database import database
from fastapi_pagination import Page

router = APIRouter(tags=["User"])


@router.get("/", response_model=Page[User])
async def get_users(
    session: AsyncSession = Depends(database.scoped_session_dependency),
):
    return await crud.get_users(session=session)


@router.post("/", response_model=User, status_code=201)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(database.scoped_session_dependency),
):
    return await crud.create_user(
        session=session,
        user_in=user_in,
    )


