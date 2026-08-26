# CodeMentor

CodeMentor is a programming-learning platform designed to help students practise Python and C++ through questions, hints, progress tracking, and guided feedback.

## Planned features

- User registration and authentication
- Python and C++ programming questions
- Hints and explanations
- Student progress tracking
- Automated tests and continuous integration
- AI-powered learning support in a future release

## Technology

- Python
- FastAPI
- SQLite
- pytest
- GitHub Actions
- SQLModel

## Local setup

```bash
python -m venv .venv
```

Activate the virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive API documentation.

Run tests:

```bash
python -m pytest
```