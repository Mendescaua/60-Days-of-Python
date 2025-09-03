from fastapi import APIRouter, Path, HTTPException, status, Response
from models import Curso, cursos
from typing import List

router = APIRouter()


@router.get("/api/v1/curso", description="Retorna todos os cursos ou uma lista vazia", summary="Retorna todos os cursos", response_model=List[Curso])
async def get_cursos():
    return cursos


@router.get("/api/v1/curso/{curso_id}", description="Retorna um curso pelo ID", summary="Retorna curso pelo ID")
async def get_cursos_id(curso_id: int = Path(gt=0, lt=3, description="Deve ser 1 ou 2")):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não encontrado"
        )


@router.post("/api/v1/curso", status_code=status.HTTP_201_CREATED, description='Criar um novo curso', summary='Criar curso', response_model=Curso)
async def post_cursos(curso: Curso):
    id = len(cursos) + 1
    curso.id = id
    cursos.append(curso)
    return curso


@router.put("/api/v1/curso/{curso_id}", description="Atualizar curso pelo ID", summary="Atualizar curso")
async def put_cursos(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Não existe um curso com id {curso_id}'
        )


@router.delete('/api/v1/curso/{curso_id}', description='Deleta o curso pelo ID', summary="Deletar curso")
async def del_cursos(curso_id: int):
    try:
        curso = cursos.pop(curso_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Não existe um curso com id {curso_id}'
        )
