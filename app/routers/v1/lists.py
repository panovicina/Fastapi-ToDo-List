import sqlalchemy
from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from app.schemas import list as list_schema
from app.services.auth import get_current_user
from app.services.lists import TODOListService

router = APIRouter(
    tags=["Lists"],
)


@router.put("/lists/{list_id}", response_model=list_schema.ListOutSchema)
async def update_list_by_id(
    list_id: int, todo_list: list_schema.ListUpdateSchema
):
    list_to_update = await TODOListService.get_by_id(list_id)
    if not list_to_update:
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! We don't have list yet(("},
        )
    updated_list = await TODOListService.update_list_by_id(list_id, todo_list)
    return updated_list


@router.get(
    "/lists", response_model=list[list_schema.ListOutSchema]
)  # достать все to do lists
async def get_all_lists(user=Depends(get_current_user)):
    print(user)
    lists = await TODOListService.get_by_user_id(user_id=user.id)
    if not lists:
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! We don't have lists yet(("},
        )
    return lists


@router.get("/lists/user/{user_id}")  # достать листы юзера по user_id
async def get_lists_by_user_id(user_id: int):
    lists = await TODOListService.get_by_user_id(user_id)
    if not lists:
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! We don't have this user(("},
        )
    return lists


@router.post("/lists", response_model=list_schema.ListOutSchema)
async def create_todolist(
    todo_list: list_schema.ListInSchema, user=Depends(get_current_user)
):
    todo_list.user_id = user.id
    try:
        list1 = await TODOListService.create_list(todo_list)
    except sqlalchemy.exc.IntegrityError:
        return JSONResponse(
            status_code=400,
            content={"message": "Bad request"},
        )
    return list1


@router.delete("/lists/{id}")
async def delete_list(id: int):
    todo_list = await TODOListService.get_by_id(id)
    print(todo_list)
    if not todo_list:
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! We don't have this to-do list(("},
        )
    await TODOListService.delete_list(id)
    return JSONResponse(
        status_code=203,
        content={"message": "deleted"},
    )


@router.get("/lists/{list_id}")
async def get_list_by_id(list_id: int):
    todo_list = await TODOListService.get_by_id(list_id)
    if not todo_list:
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! We don't have this list(("},
        )
    return todo_list
