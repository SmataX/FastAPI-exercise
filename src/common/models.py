from enum import Enum
from datetime import datetime, timedelta
from sqlmodel import SQLModel, Field


class TaskStatus(str, Enum):
    todo = "TODO"
    in_progress = "INPROGRESS"
    done = "DONE"

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(default="", max_length=300)
    status: TaskStatus = Field(default=TaskStatus.todo)


class Pomodoro(SQLModel, table=True):
    task_id: int = Field(foreign_key="task.id", primary_key=True)
    start_time: datetime = Field(default_factory=datetime.now)
    end_time: datetime = Field(default_factory=lambda: datetime.now() + timedelta(minutes=25))
    completed: bool = Field(default=False)

