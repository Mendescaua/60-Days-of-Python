from fastapi import APIRouter

router = APIRouter()


@router.get('/api/v1/user')
async def get_users():
    return {'Info': 'Todos os usuários'}


