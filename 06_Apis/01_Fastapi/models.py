from typing import Optional
from pydantic import BaseModel, field_validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @field_validator('titulo')
    def validar_titulo(value: str):
        palavra = value.split(' ')
        if len(palavra) < 3:
            raise ValueError('O Titulo deve conter 3 palavras.')

        if value.islower():
            raise ValueError('A primeira letra do titulo deve ser maiuscula.')

        return value


cursos = [
    Curso(id=1, titulo='Programação em Python', aulas=12, horas=8),
    Curso(id=2, titulo='Programação em JavaScript', aulas=8, horas=6),
    Curso(id=3, titulo='Programação em Java', aulas=16, horas=12),
]
