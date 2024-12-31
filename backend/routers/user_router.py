from fastapi import APIRouter


router = APIRouter(prefix="/api/v1", tags=["User"])

# получение списка всех пользователей
@router.get("/userlist/")
def get_userlist():
    return {"список": "пользователей"}

# получение конкретного пользователя
@router.post("/user/{user_id}")
def get_user(user_id: int):
    return {"user": user_id}
