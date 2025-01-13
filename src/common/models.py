from enum import Enum
from pydantic import BaseModel, Field

class TaskStatus(str, Enum):
    todo = "TODO"
    in_progress = "INPROGRESS"
    done = "DONE"

class Task(BaseModel):
    id: int = Field(default=None)
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(default="", max_length=100)
    status: TaskStatus = Field(default=TaskStatus.todo)



# class Task(BaseModel):
#     id: int = generate_id(list_of_tasks)
#     title: Annotated[str, Query(min_length=3, max_length=100)]
#     description: Annotated[str, Query(max_length=300)] | None = None
#     status: TaskSatus = TaskSatus.TODO
