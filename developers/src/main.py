from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.api_v1 import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=users_router)
add_pagination(app)


@app.get("/")
async def get_everything():
    return "Hello everyone!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
