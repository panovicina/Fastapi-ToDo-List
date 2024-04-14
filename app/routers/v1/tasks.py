import sqlalchemy
from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.schemas import task as task_schema
from app.services.tasks import TaskService

router = APIRouter(
    tags=["Tasks"],
)


@router.post("/tasks", response_model=task_schema.TaskOutSchema)
async def create_task(task: task_schema.TaskInSchema):
    try:
        created_task = await TaskService.create_task(task.model_dump())
    except sqlalchemy.exc.IntegrityError:
        return JSONResponse(
            status_code=400,
            content={"message": "Bad request"},
        )
    return created_task


@router.delete("/tasks/{id}")
async def delete_task(id: int):
    task = await TaskService.get_by_id(id)
    if not task:
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! We don't have this task(("},
        )
    await TaskService.delete_task(id)
    return "удалили задачу"


@router.get("/tasks", response_model=list[task_schema.TaskOutSchema])
async def get_all_tasks():
    tasks = await TaskService.get_all_tasks()
    if not tasks:
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! We don't have tasks yet(("},
        )
    return tasks


@router.get("/tasks/list/{list_id}")
async def get_tasks_by_list_id(list_id: int):
    tasks = await TaskService.get_tasks_by_list_id(list_id)
    if not tasks:
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! We don't have this list(("},
        )
    return tasks


@router.put("/tasks/{task_id}", response_model=task_schema.TaskOutSchema)
async def update_task_by_id(task_id: int, task: task_schema.TaskUpdateSchema):
    task_to_update = await TaskService.get_by_id(task_id)
    if not task_to_update:
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! We don't have this task(("},
        )
    updated_task = await TaskService.update_task(task_id, task.model_dump())
    return updated_task


@router.get("/tasks/{task_id}")
async def get_tasks_by_id(task_id: int):
    task = await TaskService.get_by_id(task_id)
    if not task:
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! We don't have this task(("},
        )
    return task
