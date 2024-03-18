import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_everything():
    return "Hello everyone!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
