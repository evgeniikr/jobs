from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from fastapi_pagination import paginate

from src.api_v1.user.schemas import UserCreate
from src.models import User


async def get_users(session: AsyncSession):
    stmt = select(User).order_by(User.created_at)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return paginate(users)


async def create_user(
    session: AsyncSession,
    user_in: UserCreate,
) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user
