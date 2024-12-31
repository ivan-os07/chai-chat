from fastapi import APIRouter


router = APIRouter(prefix="/api/v1", tags=["AI"])

# Здесь будет отправка боту уже обработанной информации от ai

@router.get("/get_ai/")
def get_message():
    return {"message": "together informational"}

