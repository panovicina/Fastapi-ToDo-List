from pydantic import BaseModel


class ListInSchema(BaseModel):
    name: str
    description: str | None = None
    user_id: int


class ListUpdateSchema(BaseModel):
    name: str
    description: str | None = None


class ListOutSchema(ListInSchema):
    id: int
