from fastapi import FastAPI

app = FastAPI()

from src.server.routers import tasks
app.include_router(tasks.router)

from src.server.routers import pomodoro
app.include_router(pomodoro.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}