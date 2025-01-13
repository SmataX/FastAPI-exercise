from fastapi import FastAPI, Query, HTTPException
# from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from enum import Enum
from typing import Annotated, List, Optional
from datetime import datetime, timedelta

app = FastAPI()

def generate_id(l: list) -> int:
    if len(l) > 0:
        return max([task.id for task in l]) + 1
    return 0



# class PomodoroSessions(BaseModel):
#     task_id: int
#     start_time: datetime = datetime.now()
#     end_time: datetime = datetime.now() + timedelta(minutes=25)
#     completed: bool = False





