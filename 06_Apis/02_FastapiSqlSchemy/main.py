from fastapi import FastAPI

app = FastAPI(
    title="Curso de Fastapi",
    description="FastApi + SqlAlchemy",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
