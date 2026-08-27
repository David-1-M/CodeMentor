from fastapi import FastAPI
from app import models

from sqlmodel import Session

from app.database import create_database_and_tables, engine
from app.seed import seed_questions

from app.api.questions import router as questions_router

from app.database import create_database_and_tables

app = FastAPI(
    title="CodeMentor API",
    description="A learning platform for Python and C++ students.",
    version="0.1.0",
)

app.include_router(questions_router)


@app.on_event("startup")
def on_startup() -> None:
    create_database_and_tables()
    
    with Session(engine) as session:
        seed_questions(session)


@app.get("/")
def welcome() -> dict[str, str]:
    return {
        "message": "Welcome to CodeMentor API",
        "docs": "/docs",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}