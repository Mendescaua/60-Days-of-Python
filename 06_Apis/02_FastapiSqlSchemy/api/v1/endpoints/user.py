from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.user_model import UserModel
from schemas.user_schemas import UserSchema
from core.deps import get_session

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserSchema)
async def post_user(user: UserSchema, db: AsyncSession = Depends(get_session)):
    new_user = UserModel(name=user.name, email=user.email,
                         password=user.password)

    db.add(new_user)
    await db.commit()

    return new_user


@router.get('/', response_model=List[UserSchema])
async def get_user(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UserModel)
        result = await session.execute(query)
        users = List[UserModel] = result.scalars().all()

        return users
