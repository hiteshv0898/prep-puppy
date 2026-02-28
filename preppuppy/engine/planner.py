from dataclasses import dataclass

from preppuppy.core.config import PrepConfig
from preppuppy.content.tracks import load_tracks


@dataclass(frozen=True)
class StudyPlan:
    track: str
    mode: str
    domains: list[str]
    domain: str
    level: str
    lessons: list[str]
    drills: list[str]
    mocks: list[str]


def build_plan(config: PrepConfig) -> StudyPlan:
    tracks = load_tracks()
    track = tracks.get(config.track, {})

    lessons = track.get("lessons", [])
    drills = track.get("drills", [])
    mocks = track.get("mocks", [])

    return StudyPlan(
        track=config.track,
        mode=config.mode,
        domains=config.domains,
        domain=config.domain,
        level=config.level,
        lessons=lessons,
        drills=drills,
        mocks=mocks,
    )
