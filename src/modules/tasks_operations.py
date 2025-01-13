from dataclasses import dataclass
from typing import Annotated
from fastapi import Depends

from src.main import generate_id
from src.common.models import TaskStatus, Task

@dataclass
class TasksOperations:
    storage = []

    def get_tasks(self) -> list[Task]:
        return self.storage
    

    def get_task(self, id: int) -> Task:
        for task in self.storage:
            if task.id == id:
                return task
        return None
    

    def get_task_by_status(self, status: TaskStatus) -> list[Task]:
        return [task for task in self.storage if task.status == status]
    

    def add_task(self, task: Task) -> Task:
        task.id = generate_id(self.storage)
        self.storage.append(task)
        return task


    def update_task(self, id: int, updated_task: Task) -> Task:
        for task in self.storage:
            if task.id == id:
                task.id = task.id
                task.title = updated_task.title
                task.description = updated_task.description
                task.status = updated_task.status
                return task
        return None
    
    
    def delete_task(self, id: int):
        for task in self.storage:
            if task.id == id:
                self.storage.remove(task)

def get_tasks_operations() -> TasksOperations:
    return TasksOperations([])

TasksOperationsDep = Annotated[TasksOperations, Depends()]