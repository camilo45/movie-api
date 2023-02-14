from fastapi import APIRouter
from utils.jwt_manger import create_token
from schemas.user import User
from fastapi.responses import HTMLResponse, JSONResponse
user_router = APIRouter()

@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)

