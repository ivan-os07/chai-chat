import os
from fastapi import APIRouter, Depends, HTTPException
from authx import AuthX, AuthXConfig
from pydantic import BaseModel

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


router = APIRouter(prefix="/api/v1", tags=["Auth"])

config = AuthXConfig()
config.JWT_ALGORITHM = "HS256"
config.JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

security = AuthX(config=config)

class UserLoginSchema(BaseModel):
    username: str
    password: str

    
@router.post("/login/")
def login(creds: UserLoginSchema):
    if creds.username == "test" and creds.password == "test":
        token = security.create_access_token(uid=creds.username)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail={"message": "Bad credentials"})


@router.get("/protected/", dependencies=[Depends(security.access_token_required)])
def get_protected():
    return {"message": "Hello World"}
