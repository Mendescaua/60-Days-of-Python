from fastapi import FastAPI, Path, HTTPException, status, Response, Depends
from models import Curso
from time import sleep

app = FastAPI()


def fake_db():
    try:
        print('Abrindo conexão com o banco de dados...')
        sleep(1)
    finally:
        print('fechando conexão com banco de dados...')
        sleep(1)


cursos = {
    1: {
        'titulo': 'Flutter oob',
        'aulas': 112,
        'horas': 58
    },
    2: {
        'titulo': 'Formação python',
        'aulas': 265,
        'horas': 65
    }
}


@app.get("/cursos")
async def get_cursos(db: str = Depends(fake_db)):
    return cursos


@app.get("/cursos/{curso_id}")
async def get_cursos_id(curso_id: int = Path(gt=0, lt=3, description="Deve ser 1 ou 2"), db: str = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não encontrado"
        )


@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_cursos(curso: Curso, db: str = Depends(fake_db)):
    id = len(cursos) + 1
    cursos[id] = curso
    return 'Curso adicionado com sucesso!'


@app.put("/cursos/{curso_id}")
async def put_cursos(curso_id: int, curso: Curso, db: str = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return "Curso atualizado com sucesso!"
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Não existe um curso com id {curso_id}'
        )


@app.delete('/cursos/{curso_id}')
async def del_cursos(curso_id: int, db: str = Depends(fake_db)):
    try:
        curso = cursos.pop(curso_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Não existe um curso com id {curso_id}'
        )


# QueryParams
@app.get('/calculadora')
async def caculadora(a: float, b: float, c: float):
    soma = sum([a, b, c])
    return {'Resultado': soma}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
