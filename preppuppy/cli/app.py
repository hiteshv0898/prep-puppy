import typer

from preppuppy.core.config import load_profile
from preppuppy.engine.planner import build_plan
from preppuppy.ui.console import show_banner, show_plan

app = typer.Typer()


@app.command()
def main(
    track: str = typer.Option("data-engineer", help="Track: data-engineer | ai-engineer | data-scientist"),
    mode: str = typer.Option("learn", help="Mode: learn | drill | mock"),
) -> None:
    config = load_profile(track=track, mode=mode)
    plan = build_plan(config)

    show_banner()
    show_plan(plan)


def main_cli() -> None:
    app()


if __name__ == "__main__":
    main_cli()
