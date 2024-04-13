from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Tasks


class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_task(self, task_data):
        task = Tasks(**task_data)
        self.session.add(task)
        return task

    async def delete_task(self, task_id):
        query = select(Tasks).where(Tasks.id == task_id)
        result = await self.session.execute(query)
        task = result.scalar()
        await self.session.delete(task)
        return task

    async def get_all_tasks(self):
        query = select(Tasks)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_tasks_by_list_id(self, list_id):
        query = select(Tasks).where(Tasks.list_id == list_id)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def update_task(self, task_id, task_data):
        query = (
            update(Tasks)
            .where(Tasks.id == task_id)
            .values(**task_data)
            .returning(Tasks)
        )
        result = await self.session.execute(query)
        return result.scalar()

    async def get_by_id(self, task_id: int):
        query = select(Tasks).where(Tasks.id == task_id)
        result = await self.session.execute(query)
        return result.scalars().first()
