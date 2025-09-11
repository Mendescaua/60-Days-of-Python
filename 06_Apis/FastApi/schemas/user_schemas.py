from typing import Optional
# renomeei por conta que o sqlalchemy tbm tem BaseModel e para não confundir renomeei(ScBaseModel)
from pydantic import BaseModel as SCBaseModel

# Acessa dados do usuário sem a senha por regra de negócio


class UserSchema(SCBaseModel):
    id: Optional[int] = None
    name: str
    email: str

    class Config:
        orm_mode = True


# Acessa dados do usuário com a senha para cadastro e login
class UserLoginSchema(UserSchema):
    password: str


# Atualização de dados do usuário
class UserUpdateSchema(UserSchema):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
