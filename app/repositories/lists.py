from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import TODOList


class ListRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def update_list_by_id(self, list_id: int, **todo_list: dict):
        query = (
            update(TODOList)
            .where(TODOList.id == list_id)
            .values(**todo_list)
            .returning(TODOList)
        )
        updated_list = await self.session.execute(query)
        return updated_list.scalar()

    async def get_all(self):
        query = select(TODOList)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_by_list_id(self, user_id: int):
        query = select(TODOList).where(TODOList.user_id == user_id)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create_list(self, todo_list: TODOList):
        self.session.add(todo_list)

    async def delete_list(self, id: int):
        query = select(TODOList).where(TODOList.id == id)
        result = await self.session.execute(query)
        todo_list = result.scalar()
        await self.session.delete(todo_list)
        return todo_list

    async def get_by_id(self, list_id: int):
        query = select(TODOList).where(TODOList.id == list_id)
        result = await self.session.execute(query)
        return result.scalars().first()
