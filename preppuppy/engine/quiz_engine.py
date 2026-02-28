from preppuppy.content.loader import load_quizzes


def run_quiz(domain: str) -> list[dict]:
    quizzes = load_quizzes()
    return quizzes.get(domain, [])
