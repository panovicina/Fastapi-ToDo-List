from pydantic import BaseModel


class ListInSchema(BaseModel):
    name: str
    description: str | None = None
    user_id: int | None = None


class ListUpdateSchema(BaseModel):
    name: str
    description: str | None = None


class ListOutSchema(ListInSchema):
    id: int
