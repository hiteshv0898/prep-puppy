from rich.console import Console
from rich.panel import Panel

console = Console()


def show_banner() -> None:
    console.print(Panel("prep-puppy: learn first, then crush interviews", title="PREP-PUPPY"))


def show_plan(plan) -> None:
    console.print(
        Panel(
            f"Track: {plan.track}\nMode: {plan.mode}\nDomain: {plan.domain}\nLevel: {plan.level}\n\n"
            f"Lessons: {', '.join(plan.lessons)}\n"
            f"Drills: {', '.join(plan.drills)}\n"
            f"Mocks: {', '.join(plan.mocks)}",
            title="STUDY PLAN",
        )
    )


def show_lesson(payload: dict) -> None:
    bullets = "\n".join(f"- {line}" for line in payload.get("bullets", []))
    console.print(Panel(f"{payload.get('title', 'Lesson')}\n\n{bullets}", title="LESSON"))


def show_drill(prompts: list[str]) -> None:
    bullets = "\n".join(f"- {line}" for line in prompts)
    console.print(Panel(bullets, title="DRILL"))


def show_quiz(items: list[dict]) -> None:
    if not items:
        console.print(Panel("No quiz items yet.", title="QUIZ"))
        return
    lines = []
    for idx, item in enumerate(items, start=1):
        question = item.get("question", "")
        answer = item.get("answer", "")
        lines.append(f"{idx}. {question}\n   Answer: {answer}")
    console.print(Panel("\n".join(lines), title="QUIZ"))


def show_mock(scenarios: list[str]) -> None:
    bullets = "\n".join(f"- {line}" for line in scenarios)
    console.print(Panel(bullets, title="MOCK"))
