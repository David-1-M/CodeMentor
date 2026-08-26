from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "sqlite:///./codementor.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


def create_database_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session