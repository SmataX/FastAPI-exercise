from dataclasses import dataclass
from typing import Annotated
from fastapi import Depends
from datetime import datetime

from src.common.models import Pomodoro
from src.modules.tasks_operations import TasksOperations, TasksOperationsDep
from src.common.db_storage import DBStorageHandler, DBStorageHandlerDep

@dataclass
class PomodoroOperations:
    task_operations: TasksOperations
    db_storage: DBStorageHandler


    def add_pomodoro(self, pomodoro: Pomodoro) -> Pomodoro:
        if self.task_operations.get_task(pomodoro.task_id) is None:
            return None
        
        checked_pomodoro = self.get_pomodoro_by_id(pomodoro.task_id)
        if checked_pomodoro is not None and not checked_pomodoro.completed:
            return None

        self.db_storage.create(pomodoro)
        return pomodoro
    
    def stop_pomodoro(self, id: int) -> Pomodoro:
        pomodoro = self.get_pomodoro_by_id(id)
        if pomodoro is not None and pomodoro.completed == False:
            pomodoro.end_time = datetime.now()
            pomodoro.completed = True
            self.db_storage.update(id, pomodoro)
            return pomodoro

    def get_pomodoro_by_id(self, id: int) -> Pomodoro:
        try:
            return self.db_storage.get_by_id(id, Pomodoro)
        except ValueError:
            raise ValueError(f"Pomodoro with id {id} not found")
    
    def get_pomodoro(self) -> list[Pomodoro]:
        self.update_pomodoro()
        return self.db_storage.get_all()
    
    def update_pomodoro(self):
        try:
            pomodoro = self.get_pomodoro_by_id(id)
        except ValueError:
            raise Exception(f"Pomodoro with id {id} not found")
        
        if pomodoro.end_time < datetime.now():
            pomodoro.end_time = datetime.now()
            pomodoro.completed = True

        try:
            self.db_storage.update(id, pomodoro)
        except ValueError:
            raise Exception(f"Pomodoro with id {id} not found")
        return pomodoro
    



def get_pomodoro_operations(tasks_operations: TasksOperationsDep, db_storage: DBStorageHandlerDep) -> PomodoroOperations:
    return PomodoroOperations(tasks_operations, db_storage)

PomodoroOperationsDep = Annotated[PomodoroOperations, Depends(get_pomodoro_operations)]