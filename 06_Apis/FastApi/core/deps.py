from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, Header, status
from jose import jwt, JWTError
from core.configs import settings
from core.auth import validate_api_key
from core.database import Session

# Validação API Key


async def get_current_client(x_api_key: str = Header(None)):
    if not x_api_key or not validate_api_key(x_api_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
    return x_api_key


# Validação JWT
async def get_current_user_from_jwt(authorization: str = Header(..., alias="Authorization")):
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token format")

    token = authorization.split(" ")[1]

    try:
        payload = jwt.decode(token, settings.JWT_SECRET,
                             algorithms=[settings.ALGORITHM])
        sub = payload.get("sub")
        if sub is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")
        return sub
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

# Sessão do banco de dados


async def get_session() -> AsyncGenerator:
    session: AsyncSession = Session()
    try:
        yield session
    finally:
        await session.close()
