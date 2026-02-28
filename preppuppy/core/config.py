from dataclasses import dataclass


@dataclass(frozen=True)
class PrepConfig:
    track: str
    mode: str
    domains: list[str]


def load_profile(track: str, mode: str) -> PrepConfig:
    normalized_track = track.strip().lower()
    normalized_mode = mode.strip().lower()

    if normalized_track not in {"data-engineer", "ai-engineer", "data-scientist"}:
        raise ValueError("track must be data-engineer | ai-engineer | data-scientist")
    if normalized_mode not in {"learn", "drill", "mock"}:
        raise ValueError("mode must be learn | drill | mock")

    domains = _domains_for_track(normalized_track)
    return PrepConfig(track=normalized_track, mode=normalized_mode, domains=domains)


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
            "behavioral",
        ]
    return [
        "python-basics",
        "sql",
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
