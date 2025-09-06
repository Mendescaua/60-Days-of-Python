from typing import Optional
from sqlmodel import Field, SQLModel
from pydantic import field_validator, EmailStr


class UserModel(SQLModel, table=True):
    __tablename__ = "cursos"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: EmailStr
    password: str

    @field_validator("password")
    def validar_senha(cls, value: str):
        if len(value) < 8 or "123" in value:
            raise ValueError("Senha muito fraca")
        return value
