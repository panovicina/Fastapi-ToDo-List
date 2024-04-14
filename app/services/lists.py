from app.database import async_session
from app.models import TODOList
from app.repositories.lists import ListRepository
from app.schemas import list as list_schema


class TODOListService:
    @staticmethod
    async def update_list_by_id(
        list_id: int, todo_list: list_schema.ListUpdateSchema
    ):
        async with async_session() as session:
            updated_list = await ListRepository(session).update_list_by_id(
                list_id, **todo_list.model_dump()
            )
            await session.commit()
        return updated_list

    @staticmethod
    async def get_all_lists():
        async with async_session() as session:
            lists = await ListRepository(session).get_all()
            users_data = [list1.__dict__ for list1 in lists]
            await session.commit()
        return users_data

    @staticmethod
    async def get_by_user_id(user_id: int):
        async with async_session() as session:
            lists = await ListRepository(session).get_by_list_id(user_id)
            await session.commit()
        return lists

    @staticmethod
    async def create_list(todo_list: list_schema.ListInSchema):
        async with async_session() as session:
            todo_list = TODOList(**todo_list.model_dump())
            await ListRepository(session).create_list(todo_list)
            # todo_list = TODOList(
            # name=todo_list.name,
            # description=todo_list.description,
            # user_id=todo_list.user_id)
            await session.commit()
        return todo_list

    @staticmethod
    async def delete_list(id: int):
        async with async_session() as session:
            result = await ListRepository(session).delete_list(id)
            await session.commit()
        return result

    @staticmethod
    async def get_by_id(id: int):
        async with async_session() as session:
            todo_list = await ListRepository(session).get_by_id(id)
            await session.commit()
        return todo_list
