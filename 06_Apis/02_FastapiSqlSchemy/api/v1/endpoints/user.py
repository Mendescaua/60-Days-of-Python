from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user_model import UserModel
from schemas.user_schemas import UserSchema
from core.deps import get_session

router = APIRouter()


# Post user
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserSchema)
async def post_user(user: UserSchema, db: AsyncSession = Depends(get_session)):
    new_user = UserModel(name=user.name, email=user.email,
                         password=user.password)

    db.add(new_user)
    await db.commit()

    return new_user


# Get all users
@router.get('/', response_model=List[UserSchema])
async def get_user(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).order_by((UserModel.id))
        result = await session.execute(query)
        users: List[UserModel] = result.scalars().all()

        if users:
            return users
        else:
            raise HTTPException(detail='Não existe nenhum usuário',
                                status_code=status.HTTP_404_NOT_FOUND)


# Get user by ID
@router.get('/{user_id}', response_model=UserSchema, status_code=status.HTTP_200_OK)
async def get_user_id(user_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.id == user_id)
        result = await session.execute(query)
        users = result.scalar_one_or_none()

        if users:
            return users
        else:
            raise HTTPException(detail='Usuário não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# Put user
@router.put('/{user_id}', response_model=UserSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_user(user_id: int, user: UserSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.id == user_id)
        result = await session.execute(query)
        users = result.scalar_one_or_none()

        if users:
            users.name = user.name
            users.email = user.email
            users.password = user.password

            await session.commit()

            return users
        else:
            raise HTTPException(detail='Usuário não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# Delete user
@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel).filter(UserModel.id == user_id)
        result = await session.execute(query)
        users = result.scalar_one_or_none()

        if users:
            await session.delete(users)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Usuário não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)
