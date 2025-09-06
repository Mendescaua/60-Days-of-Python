from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:%40Mc140723@localhost:5432/USERS'

    class Config:
        env_file = ".env"  # permite carregar variáveis do arquivo .env
        case_sensitive = True


settings: Settings = Settings()
