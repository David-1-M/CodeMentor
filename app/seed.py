from sqlmodel import Session, select

from app.models import DifficultyLevel, ProgrammingLanguage, Question

STARTER_QUESTIONS = [
    {
        "title": "Check if a number is even",
        "language": ProgrammingLanguage.PYTHON,
        "difficulty": DifficultyLevel.BEGINNER,
        "prompt": (
            "Write a function named is_even that accepts an integer and "
            "returns True when the number is even and False otherwise."
        ),
        "hint": "Use the modulo operator (%) to check the remainder after division by 2.",
        "solution_template": (
            "def is_even(number: int) -> bool:\n"
            "    pass"
        ),
    },
    {
        "title": "Find the largest number in a list",
        "language": ProgrammingLanguage.PYTHON,
        "difficulty": DifficultyLevel.BEGINNER,
        "prompt": (
            "Write a function named find_largest that accepts a list of integers "
            "and returns the largest number."
        ),
        "hint": "Start with the first number, then compare every remaining number.",
        "solution_template": (
            "def find_largest(numbers: list[int]) -> int:\n"
            "    pass"
        ),
    },
    {
        "title": "Count word frequency",
        "language": ProgrammingLanguage.PYTHON,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "prompt": (
            "Write a function named count_words that accepts a sentence and "
            "returns a dictionary containing the number of times each word appears."
        ),
        "hint": "Split the sentence into words and use a dictionary to store counts.",
        "solution_template": (
            "def count_words(sentence: str) -> dict[str, int]:\n"
            "    pass"
        ),
    },
    {
        "title": "Add two numbers",
        "language": ProgrammingLanguage.CPP,
        "difficulty": DifficultyLevel.BEGINNER,
        "prompt": (
            "Write a C++ program that reads two integers from the user and "
            "prints their sum."
        ),
        "hint": "Use cin to read values and cout to display the result.",
        "solution_template": (
            "#include <iostream>\n\n"
            "int main() {\n"
            "    // Write your solution here\n"
            "    return 0;\n"
            "}"
        ),
    },
    {
        "title": "Classify a number",
        "language": ProgrammingLanguage.CPP,
        "difficulty": DifficultyLevel.BEGINNER,
        "prompt": (
            "Write a C++ program that reads an integer and prints whether it "
            "is positive, negative, or zero."
        ),
        "hint": "Use an if, else if, and else statement.",
        "solution_template": (
            "#include <iostream>\n\n"
            "int main() {\n"
            "    // Write your solution here\n"
            "    return 0;\n"
            "}"
        ),
    },
    {
        "title": "Find the largest array element",
        "language": ProgrammingLanguage.CPP,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "prompt": (
            "Write a C++ program that stores five integers in an array and "
            "prints the largest value."
        ),
        "hint": "Set the first array item as the largest value, then compare the others.",
        "solution_template": (
            "#include <iostream>\n\n"
            "int main() {\n"
            "    // Write your solution here\n"
            "    return 0;\n"
            "}"
        ),
    },
]


def seed_questions(session: Session) -> None:
    existing_question = session.exec(select(Question)).first()

    if existing_question is not None:
        return

    for question_data in STARTER_QUESTIONS:
        session.add(Question(**question_data))

    session.commit()