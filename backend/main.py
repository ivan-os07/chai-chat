from fastapi import FastAPI

import uvicorn

from routers.user_router import router as user_router
from routers.ai_router import router as ai_router
from auth.auth import router as auth_router

app = FastAPI()

# подключаем rousers
app.include_router(user_router)
app.include_router(ai_router)
app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
