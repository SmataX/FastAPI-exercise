from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime, timedelta

class TaskStatus(str, Enum):
    todo = "TODO"
    in_progress = "INPROGRESS"
    done = "DONE"

class Task(BaseModel):
    id: int = Field(default=None)
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(default="", max_length=100)
    status: TaskStatus = Field(default=TaskStatus.todo)


class Pomodoro(BaseModel):
    task_id: int = Field()
    start_time: datetime = Field(default=datetime.now())
    end_time: datetime = Field(default=datetime.now() + timedelta(minutes=25))
    completed: bool = Field(default=False)