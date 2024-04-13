from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def update_user(self, user_id: int, **user_data):
        query = (
            update(User)
            .where(User.id == user_id)
            .values(**user_data)
            .returning(User)
        )
        updated_user = await self.session.execute(query)
        return updated_user.scalar()

    async def get_by_id(self, user_id: int):
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        user = result.scalar()
        return user

    async def get_all_users(self):
        query = select(User)
        result = await self.session.execute(query)
        users = result.scalars().all()
        return users

    async def create_user(self, user: User):
        self.session.add(user)
        return user

    async def delete(self, user_id: int):
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        user = result.scalar()
        await self.session.delete(user)
        return user

    async def get_by_username(self, username: str):
        query = select(User).where(User.username == username)
        result = await self.session.execute(query)
        user = result.scalar()
        return user
