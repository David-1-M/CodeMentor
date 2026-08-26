from enum import Enum

from sqlmodel import Field, SQLModel


class ProgrammingLanguage(str, Enum):
    PYTHON = "Python"
    CPP = "C++"


class DifficultyLevel(str, Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"


class Question(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True, min_length=3, max_length=120)
    language: ProgrammingLanguage
    difficulty: DifficultyLevel
    prompt: str
    hint: str | None = None
    solution_template: str | None = None
    is_published: bool = Field(default=True)