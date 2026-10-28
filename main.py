"""A simple multiple-choice quiz that runs in the terminal."""

QUESTIONS = [
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. make"],
        "answer": "B",
    },
    {
        "question": "Which data type stores an ordered collection?",
        "options": ["A. list", "B. bool", "C. int", "D. None"],
        "answer": "A",
    },
    {
        "question": "What does AI stand for?",
        "options": [
            "A. Automated Internet",
            "B. Artificial Intelligence",
            "C. Applied Interface",
            "D. Advanced Input",
        ],
        "answer": "B",
    },
]


def run_quiz() -> None:
    score = 0
    print("=== Python & Technology Quiz ===")
    print("Enter A, B, C, or D.\n")

    for number, item in enumerate(QUESTIONS, start=1):
        print(f"{number}. {item['question']}")
        for option in item["options"]:
            print(f"   {option}")

        answer = input("Your answer: ").strip().upper()
        if answer == item["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Not quite. Correct answer: {item['answer']}.\n")

    total = len(QUESTIONS)
    print(f"Your score: {score}/{total}")
    print(f"Percentage: {score / total * 100:.0f}%")


if __name__ == "__main__":
    run_quiz()
