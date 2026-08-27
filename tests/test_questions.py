import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, StaticPool, create_engine

from app.database import get_session
from app.main import app

TEST_DATABASE_URL = "sqlite://"

test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


@pytest.fixture(name="client")
def client_fixture():
    SQLModel.metadata.create_all(test_engine)

    def get_test_session():
        with Session(test_engine) as session:
            yield session

    app.dependency_overrides[get_session] = get_test_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    SQLModel.metadata.drop_all(test_engine)


QUESTION_PAYLOAD = {
    "title": "Print a greeting",
    "language": "Python",
    "difficulty": "Beginner",
    "prompt": "Write a program that prints a greeting message.",
    "hint": "Use the print function.",
    "solution_template": 'print("Hello, World!")',
}


def test_create_question(client: TestClient) -> None:
    response = client.post("/questions/", json=QUESTION_PAYLOAD)

    assert response.status_code == 201

    data = response.json()
    assert data["id"] is not None
    assert data["title"] == QUESTION_PAYLOAD["title"]
    assert data["language"] == "Python"
    assert data["is_published"] is True


def test_list_questions(client: TestClient) -> None:
    client.post("/questions/", json=QUESTION_PAYLOAD)

    response = client.get("/questions/")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_question(client: TestClient) -> None:
    created_question = client.post(
        "/questions/",
        json=QUESTION_PAYLOAD,
    ).json()

    response = client.get(f"/questions/{created_question['id']}")

    assert response.status_code == 200
    assert response.json()["id"] == created_question["id"]


def test_get_missing_question(client: TestClient) -> None:
    response = client.get("/questions/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Question not found"