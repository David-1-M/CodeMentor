from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models import Question, QuestionCreate, QuestionRead

router = APIRouter(
    prefix="/questions",
    tags=["Questions"],
)

SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/", response_model=QuestionRead, status_code=status.HTTP_201_CREATED)
def create_question(
    question: QuestionCreate,
    session: SessionDep,
) -> Question:
    db_question = Question.model_validate(question)
    session.add(db_question)
    session.commit()
    session.refresh(db_question)

    return db_question


@router.get("/", response_model=list[QuestionRead])
def list_questions(session: SessionDep) -> list[Question]:
    statement = select(Question).where(Question.is_published.is_(True))
    return list(session.exec(statement).all())


@router.get("/{question_id}", response_model=QuestionRead)
def get_question(question_id: int, session: SessionDep) -> Question:
    question = session.get(Question, question_id)

    if question is None or not question.is_published:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found",
        )

    return question