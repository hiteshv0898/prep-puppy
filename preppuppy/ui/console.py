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


def show_mock(scenarios: list[str]) -> None:
    bullets = "\n".join(f"- {line}" for line in scenarios)
    console.print(Panel(bullets, title="MOCK"))
