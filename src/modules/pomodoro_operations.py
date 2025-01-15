from dataclasses import dataclass
from typing import Annotated
from fastapi import Depends
from datetime import datetime

from src.common.models import Pomodoro
from src.modules.tasks_operations import TasksOperations

@dataclass
class PomodoroOperations:
    storage = []
    task_operations: TasksOperations

    def add_pomodoro(self, pomodoro: Pomodoro) -> Pomodoro:
        if self.task_operations.get_task(pomodoro.task_id) is None:
            return None
        if self.get_pomodoro_by_id(pomodoro.task_id) is not None and not self.get_pomodoro_by_id(pomodoro.task_id).completed:
            return None

        self.storage.append(pomodoro)
        return pomodoro
    
    def stop_pomodoro(self, id: int) -> Pomodoro:
        pomodoro = self.get_pomodoro(id)
        if pomodoro is not None and pomodoro.completed == False:
            pomodoro.end_time = datetime.now()
            pomodoro.completed = True
            return pomodoro

    def get_pomodoro_by_id(self, id: int) -> Pomodoro:
        self.update_pomodoro()
        for item in self.storage:
            if item.task_id == id:
                return item
        return None
    
    def get_pomodoro(self) -> list[Pomodoro]:
        self.update_pomodoro()
        return self.storage
    
    def update_pomodoro(self):
        for item in self.storage:
            if item.end_time < datetime.now():
                item.end_time = datetime.now()
                item.completed = True
    



def get_pomodoro_operations() -> PomodoroOperations:
    return PomodoroOperations([])

PomodoroOperationsDep = Annotated[PomodoroOperations, Depends(get_pomodoro_operations)]