from sqlmodel import Session, SQLModel, StaticPool, create_engine, select

from app.models import Question
from app.seed import seed_questions


def test_seed_questions_adds_starter_questions() -> None:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        seed_questions(session)

        questions = session.exec(select(Question)).all()

    assert len(questions) == 6


def test_seed_questions_does_not_duplicate_questions() -> None:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        seed_questions(session)
        seed_questions(session)

        questions = session.exec(select(Question)).all()

    assert len(questions) == 6