from datetime import datetime, timedelta
from pytz import timezone
from jose import jwt
from core.configs import settings

# API Keys válidas (pode vir do banco ou .env)
VALID_API_KEYS = ["10", "11"]


def validate_api_key(api_key: str) -> bool:
    return api_key in VALID_API_KEYS


def create_access_token(sub: str) -> str:
    sp = timezone("America/Sao_Paulo")
    expire = datetime.now(
        tz=sp) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "type": "access_token",
        "exp": expire,
        "iat": datetime.now(tz=sp),
        "sub": str(sub),
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)


def create_refresh_token(sub: str) -> str:
    sp = timezone("America/Sao_Paulo")
    expire = datetime.now(tz=sp) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

    payload = {
        "type": "refresh_token",
        "exp": expire,
        "iat": datetime.now(tz=sp),
        "sub": str(sub),
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)
