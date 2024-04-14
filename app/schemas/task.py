from pydantic import BaseModel


class TaskInSchema(BaseModel):
    name: str
    is_done: bool = False
    list_id: int


class TaskUpdateSchema(BaseModel):
    name: str
    is_done: bool = False


class TaskOutSchema(TaskInSchema):
    id: int
