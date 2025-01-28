from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.common.db_storage import create_db_and_tables
from src.server.routers import tasks
from src.server.routers import pomodoro


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(tasks.router)
app.include_router(pomodoro.router)

@app.get("/")
async def root():
    return {"message": "Hello World!"}