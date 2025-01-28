from dataclasses import dataclass
from typing import Annotated
from fastapi import Depends

from src.main import generate_id
from src.common.models import TaskStatus, Task
from src.common.db_storage import DBStorageHandler, DBStorageHandlerDep

@dataclass
class TasksOperations:
    db_storage: DBStorageHandler

    def get_tasks(self) -> list[Task]:
        return self.db_storage.get_all(Task)
    

    def get_task(self, id: int) -> Task:
        try:
            return self.db_storage.get_by_id(id, Task)
        except ValueError:
            raise ValueError(f"Task with id {id} not found")
    

    def get_task_by_status(self, status: TaskStatus) -> list[Task]:
        conditions = [Task.status == status]
        return self.db_storage.get_all_where(Task, conditions)
    

    def add_task(self, task: Task) -> Task:
        self.db_storage.create(task)
        return task


    def update_task(self, id: int, updated_task: Task) -> Task:
        try:
            task = self.get_task(id)
        except ValueError:
            raise Exception(f"Task with id {id} not found")
        
        task.id = task.id
        task.title = updated_task.title
        task.description = updated_task.description
        task.status = updated_task.status

        try:
            self.db_storage.update(id, task)
        except ValueError:
            raise Exception(f"Task with id {id} not found")
        return task
    
    
    def delete_task(self, id: int):
        try:
            self.db_storage.delete(id, Task)
        except ValueError:
            raise Exception(f"Task with id {id} not found")

def get_tasks_operations(db_storage: DBStorageHandlerDep) -> TasksOperations:
    return TasksOperations(db_storage)

TasksOperationsDep = Annotated[TasksOperations, Depends(get_tasks_operations)]