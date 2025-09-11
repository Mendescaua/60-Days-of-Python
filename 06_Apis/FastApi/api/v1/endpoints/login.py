from fastapi import APIRouter, Depends, HTTPException, Header
from pydantic import BaseModel
from jose import jwt, JWTError
from core.deps import get_current_client, get_current_user_from_jwt
from core.auth import create_access_token, create_refresh_token
from core.configs import settings

router = APIRouter()

# Uso para criação de tokens com API Key
# Rota de login com API Key
@router.post("/login_apikey")
async def login_with_apikey(client: str = Depends(get_current_client)):
    """
    Gera Access Token e Refresh Token usando a API Key.
    """
    access_token = create_access_token(sub=client)
    refresh_token = create_refresh_token(sub=client)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


# Modelo para receber refresh token no body
class RefreshTokenRequest(BaseModel):
    refresh_token: str


# Rota de refresh token
@router.post("/refresh_apikey")
async def refresh_tokens(authorization: str = Header(..., alias="Authorization")):
    """
    Recebe um refresh token via header 'Authorization: Bearer <token>'
    e retorna novos access e refresh tokens.
    """
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")

    refresh_token = authorization.split(" ")[1]

    try:
        payload = jwt.decode(
            refresh_token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM]
        )

        if payload.get("type") != "refresh_token":
            raise HTTPException(status_code=401, detail="Invalid token type")

        sub = payload.get("sub")
        if sub is None:
            raise HTTPException(
                status_code=401, detail="Invalid token payload")

        new_access_token = create_access_token(sub=sub)
        new_refresh_token = create_refresh_token(sub=sub)

        return {
            "access_token": new_access_token,
            "refresh_token": new_refresh_token,
            "token_type": "bearer"
        }

    except JWTError:
        raise HTTPException(
            status_code=401, detail="Invalid or expired refresh token")


# Rota protegida de exemplo
@router.get("/me")
async def get_me(client: str = Depends(get_current_user_from_jwt)):
    """
    Rota protegida que retorna quem está autenticado pelo JWT.
    """
    return {"message": f"Você está autenticado como {client}"}
