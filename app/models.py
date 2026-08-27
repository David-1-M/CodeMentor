from enum import Enum

from sqlmodel import Field, SQLModel


class ProgrammingLanguage(str, Enum):
    PYTHON = "Python"
    CPP = "C++"


class DifficultyLevel(str, Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"


class QuestionBase(SQLModel):
    title: str = Field(min_length=3, max_length=120)
    language: ProgrammingLanguage
    difficulty: DifficultyLevel
    prompt: str = Field(min_length=10)
    hint: str | None = None
    solution_template: str | None = None


class Question(QuestionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    is_published: bool = Field(default=True)


class QuestionCreate(QuestionBase):
    pass


class QuestionRead(QuestionBase):
    id: int
    is_published: bool