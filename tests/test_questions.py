from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

QUESTION_PAYLOAD = {
    "title": "Print a greeting",
    "language": "Python",
    "difficulty": "Beginner",
    "prompt": "Write a program that prints a greeting message.",
    "hint": "Use the print function.",
    "solution_template": 'print("Hello, World!")',
}


def test_create_question() -> None:
    response = client.post("/questions/", json=QUESTION_PAYLOAD)

    assert response.status_code == 201

    data = response.json()
    assert data["id"] is not None
    assert data["title"] == QUESTION_PAYLOAD["title"]
    assert data["language"] == "Python"
    assert data["is_published"] is True


def test_list_questions() -> None:
    response = client.get("/questions/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1


def test_get_question() -> None:
    created_question = client.post("/questions/", json=QUESTION_PAYLOAD).json()

    response = client.get(f"/questions/{created_question['id']}")

    assert response.status_code == 200
    assert response.json()["id"] == created_question["id"]


def test_get_missing_question() -> None:
    response = client.get("/questions/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Question not found"