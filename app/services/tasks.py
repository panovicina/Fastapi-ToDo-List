from app.database import async_session
from app.repositories.tasks import TaskRepository


class TaskService:
    @staticmethod
    async def get_by_id(id: int):
        async with async_session() as session:
            task = await TaskRepository(session).get_by_id(id)
            await session.commit()
        return task

    @staticmethod
    async def create_task(task_data):
        async with async_session() as session:
            task = await TaskRepository(session).create_task(task_data)
            await session.commit()
        return task

    @staticmethod
    async def delete_task(task_id):
        async with async_session() as session:
            rows_deleted = await TaskRepository(session).delete_task(task_id)
            await session.commit()
        return rows_deleted

    @staticmethod
    async def get_all_tasks():
        async with async_session() as session:
            tasks = await TaskRepository(session).get_all_tasks()
            await session.commit()

        return [task.__dict__ for task in tasks]

    @staticmethod
    async def get_tasks_by_list_id(list_id):
        async with async_session() as session:
            tasks = await TaskRepository(session).get_tasks_by_list_id(list_id)
            await session.commit()
        return tasks

    @staticmethod
    async def update_task(task_id, task_data):
        async with async_session() as session:
            updated_task = await TaskRepository(session).update_task(
                task_id, task_data
            )
            await session.commit()
        return updated_task
