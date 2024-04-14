from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.schemas import user as user_schema
from app.services.users import UserService

router = APIRouter(
    tags=["Users"],
)


@router.put("/users/{user_id}", response_model=user_schema.UserOutSchema)
async def update_user_by_id(user_id: int, user: user_schema.UserBaseSchema):
    user_to_update = await UserService.get_by_id(user_id)
    if user_to_update is None:
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! We don't have this user(("},
        )
    return await UserService.update_user(user_id, user)


@router.get("/user/{id}")
async def get_user_by_id(id: int):
    user = await UserService.get_by_id(id)
    if user is None:
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! We don't have this user(("},
        )
    return user


@router.get(
    "/users", response_model=list[user_schema.UserOutSchema]
)  # достать всех юзеров
async def get_all_users():
    users = await UserService.get_all_users()
    return users


@router.post("/users", response_model=user_schema.UserOutSchema)
async def create_user(user: user_schema.UserInSchema):
    user = await UserService.create_user(user)
    return user


@router.delete("/users/{id}")
async def delete_user(id: int):
    user_to_delete = await UserService.get_by_id(id)
    if not user_to_delete:
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! We don't have this user(("},
        )
    await UserService.delete_user(id)
    return "удалили user"
