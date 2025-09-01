from fastapi import FastAPI
from routes import cursos_router, user_router

app = FastAPI(
    title="Curso de Fastapi",
    description="API para estudo de Fastapi",
    version="1.0.0"
)

app.include_router(cursos_router.router, tags=['cursos'])
app.include_router(user_router.router, tags=['users'])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
