from fastapi import FastAPI

app = FastAPI(
    title="CodeMentor API",
    description="A learning platform for Python and C++ students.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/")
def welcome() -> dict[str, str]:
    return {
        "message": "Welcome to CodeMentor API",
        "docs": "/docs",
    }