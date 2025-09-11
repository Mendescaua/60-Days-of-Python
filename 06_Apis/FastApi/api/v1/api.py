from fastapi import APIRouter
from api.v1.endpoints import user, login


api_router = APIRouter()

api_router.include_router(user.router, prefix='/users', tags=['users'])
api_router.include_router(login.router, prefix='/login', tags=['login'])
