from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router

app = FastAPI(
    title="Curso de Fastapi",
    description="FastApi + SqlAlchemy",
    version="1.0.0"
)

app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
