from fastapi import FastAPI

import uvicorn

app = FastAPI()


@app.get("/")
def hello():
    return {"hello": "chAI-chat"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
