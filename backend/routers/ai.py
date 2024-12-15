from fastapi import APIRouter


router = APIRouter(prefix="/api/v1", tags=["AI"])


@router.get("/get_ai/")
def get_message():
    return {"message": "together"}

