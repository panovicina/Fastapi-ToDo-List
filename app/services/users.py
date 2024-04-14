from app.database import async_session
from app.models import User
from app.repositories.users import UserRepository
from app.schemas import user as user_schema
from app.utils import hash_pass


class UserService:
    @staticmethod
    async def update_user(user_id: int, user: user_schema.UserBaseSchema):
        async with async_session() as session:
            updated_user = await UserRepository(session).update_user(
                user_id, **user.model_dump()
            )
            await session.commit()
        return updated_user

    @staticmethod
    async def get_by_id(user_id: int):
        async with async_session() as session:
            user = await UserRepository(session).get_by_id(user_id)
            await session.commit()
        return user

    @staticmethod
    async def get_all_users():
        async with async_session() as session:
            users = await UserRepository(session).get_all_users()
            users_data = [user.__dict__ for user in users]
            await session.commit()
        return users_data

    @staticmethod
    async def create_user(user: user_schema.UserInSchema):
        async with async_session() as session:
            hashed_pass = hash_pass(user.password)
            user.password = hashed_pass
            user = User(**user.model_dump())
            # user = User(username=user.username,
            # password=user.password)
            await UserRepository(session).create_user(user)
            await session.commit()
        return user

    @staticmethod
    async def delete_user(id: int):
        async with async_session() as session:
            user = await UserRepository(session).delete(user_id=id)
            await session.commit()
        return user

    @staticmethod
    async def get_by_username(username: str):
        async with async_session() as session:
            user = await UserRepository(session).get_by_username(username)
            await session.commit()
        return user
