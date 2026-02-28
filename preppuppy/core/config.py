from dataclasses import dataclass


@dataclass(frozen=True)
class PrepConfig:
    track: str
    mode: str
    domains: list[str]
    domain: str
    level: str


def load_profile(track: str, mode: str, domain: str | None = None, level: str = "basic") -> PrepConfig:
    normalized_track = track.strip().lower()
    normalized_mode = mode.strip().lower()
    normalized_level = level.strip().lower()

    if normalized_track not in {"data-engineer", "ai-engineer", "data-scientist"}:
        raise ValueError("track must be data-engineer | ai-engineer | data-scientist")
    if normalized_mode not in {"learn", "drill", "mock"}:
        raise ValueError("mode must be learn | drill | mock")

    domains = _domains_for_track(normalized_track)

    chosen = (domain or domains[0]).strip().lower()
    if chosen not in domains:
        raise ValueError(f"domain must be one of: {', '.join(domains)}")
    if normalized_level not in {"basic", "intermediate", "advanced"}:
        raise ValueError("level must be basic | intermediate | advanced")

    return PrepConfig(
        track=normalized_track,
        mode=normalized_mode,
        domains=domains,
        domain=chosen,
        level=normalized_level,
    )


def _domains_for_track(track: str) -> list[str]:
    if track == "ai-engineer":
        return [
            "python-basics",
            "math-for-ml",
            "probability",
            "stats",
            "ml-fundamentals",
            "mlops",
            "llm-engineering",
            "data-viz",
            "data-eng",
            "sql",
            "spark",
            "system-design",
            "distributed-systems",
            "behavioral",
        ]
    if track == "data-scientist":
        return [
            "python-basics",
            "math-for-ml",
            "probability",
            "stats",
            "experiments",
            "ml-fundamentals",
            "data-viz",
            "sql",
            "spark",
            "behavioral",
        ]
    return [
        "python-basics",
        "sql",
        "spark",
        "data-eng",
        "system-design",
        "distributed-systems",
        "mlops",
        "llm-engineering",
        "data-viz",
        "stats",
        "probability",
        "behavioral",
    ]
