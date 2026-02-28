from rich.console import Console
from rich.panel import Panel

console = Console()


def show_banner() -> None:
    console.print(Panel("prep-puppy: learn first, then crush interviews", title="PREP-PUPPY"))


def show_plan(plan) -> None:
    console.print(
        Panel(
            f"Track: {plan.track}\nMode: {plan.mode}\nDomains: {', '.join(plan.domains)}\n\n"
            f"Lessons: {', '.join(plan.lessons)}\n"
            f"Drills: {', '.join(plan.drills)}\n"
            f"Mocks: {', '.join(plan.mocks)}",
            title="STUDY PLAN",
        )
    )
