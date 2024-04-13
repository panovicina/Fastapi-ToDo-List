from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    username: str


class UserInSchema(UserBaseSchema):
    password: str


class UserOutSchema(UserBaseSchema):
    id: int
