from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Sequence

from app.core.models import User
from app.core.schemas.user import UserCreate


async def get_all_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_user(session: AsyncSession, user_create: UserCreate) -> User:
    user = User(username=user_create.username, email=user_create.email)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
