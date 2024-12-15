from fastapi import FastAPI

import uvicorn

from routers.user import router as user_router
from routers.ai import router as ai_router

app = FastAPI()

# подключаем rousers
app.include_router(user_router)
app.include_router(ai_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
