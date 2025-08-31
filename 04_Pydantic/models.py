from pydantic import BaseModel, EmailStr


class Usuario(BaseModel):
    nome: str
    email: EmailStr
    investimento: float


usuario = Usuario(nome="Caua", email="caua@email", investimento=1000)
print(usuario)
