from pydantic_settings import BaseSettings
from sqlalchemy.orm import declarative_base
from typing import ClassVar


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:%40Mc140723@localhost:5432/USERS'
    DBBaseModel: ClassVar = declarative_base()
    JWT_SECRET: str = 'eh0Xqwbf9wSwAlYizZomb8yxYl0rW03nnOt6aelQ0U4'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60  # 1 hour
    REFRESH_TOKEN_EXPIRE_DAYS: int = 60 * 24 * 7   # 7 days

    class Config:
        env_file = ".env"  # permite carregar variáveis do arquivo .env
        case_sensitive = True


settings = Settings()
