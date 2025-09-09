from typing import List
from fastapi import APIRouter, HTTPException, status, Depends, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from sqlmodel.sql.expression import Select, SelectOfScalar

from models.user_model import UserModel
from core.deps import get_session

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserModel)
async def post_user(user: UserModel, db: AsyncSession = Depends(get_session)):
    novo_user = UserModel(name=user.name, email=user.email,
                          password=user.password)
    db.add(novo_user)
    await db.commit()

    return novo_user

# Get users


@router.get('/', response_model=List[UserModel])
async def get_users(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel)
        result = await session.execute(query)
        users: List[UserModel] = result.scalars().all()

        return users


# Get user by id
@router.get('/{user_id}', response_model=UserModel)
async def get_user(user_id: int, db: AsyncSession = Depends(get_session)):
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
@router.put('/{user_id}', response_model=UserModel, status_code=status.HTTP_202_ACCEPTED)
async def put_user(user_id: int, user: UserModel, db: AsyncSession = Depends(get_session)):
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
