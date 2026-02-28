import typer

from preppuppy.core.config import load_profile
from preppuppy.engine.drill_engine import run_drill
from preppuppy.engine.lesson_engine import run_lesson
from preppuppy.engine.mock_engine import run_mock
from preppuppy.engine.planner import build_plan
from preppuppy.engine.quiz_engine import run_quiz
from preppuppy.ui.console import show_banner, show_drill, show_lesson, show_mock, show_plan, show_quiz

app = typer.Typer()


@app.command()
def main(
    track: str = typer.Option("data-engineer", help="Track: data-engineer | ai-engineer | data-scientist"),
    mode: str = typer.Option("learn", help="Mode: learn | drill | mock"),
    domain: str | None = typer.Option(None, help="Domain within the track"),
    level: str = typer.Option("basic", help="Level: basic | intermediate | advanced"),
) -> None:
    config = load_profile(track=track, mode=mode, domain=domain, level=level)
    plan = build_plan(config)

    show_banner()
    show_plan(plan)

    if plan.mode == "learn":
        show_lesson(run_lesson(plan.domain))
        show_quiz(run_quiz(plan.domain))
        show_drill(run_drill(plan.domain, limit=3))
        return
    if plan.mode == "drill":
        show_drill(run_drill(plan.domain))
        return
    show_mock(run_mock(plan.track))


def main_cli() -> None:
    app()


if __name__ == "__main__":
    main_cli()
