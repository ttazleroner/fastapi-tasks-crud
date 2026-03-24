from pydantic import BaseModel

class TaskAdd(BaseModel):
    name: str
    desc: str | None = None

class Task(TaskAdd):
    id: int