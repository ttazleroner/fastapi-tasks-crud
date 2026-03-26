from pydantic import BaseModel

class TaskAdd(BaseModel):
    title: str
    description: str | None = None

class Task(TaskAdd):
    id: int