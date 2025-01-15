from fastapi import APIRouter, HTTPException
import datetime

from src.common.models import Pomodoro
from src.modules.pomodoro_operations import PomodoroOperationsDep

router = APIRouter(prefix="/pomodoro")

@router.get("/")
def get_pomodoros(pomodoro_operations: PomodoroOperationsDep):
    return pomodoro_operations.storage


@router.get("/stats")
def get_pomodoro_stats(pomodoro_operations: PomodoroOperationsDep):
    completed_count = 0
    time = 0
    for pomodoro in pomodoro_operations.storage:
        if pomodoro.completed:
            completed_count += 1
            time += int((pomodoro.end_time - pomodoro.start_time).total_seconds() / 60)
    return {"completed":completed_count, "time":time}


@router.post("/")
def add_pomodoro(pomodoro_operations: PomodoroOperationsDep, pomodoro: Pomodoro):
    item = pomodoro_operations.add_pomodoro(pomodoro)
    if item is None:
        raise HTTPException(status_code=404, detail=f"Couldn't start pomodoro for task {pomodoro.task_id}")
    return item

@router.post("/{task_id}/stop")
def stop_pomodoro(pomodoro_operations: PomodoroOperationsDep, task_id: int):
    return pomodoro_operations.stop_pomodoro(task_id)