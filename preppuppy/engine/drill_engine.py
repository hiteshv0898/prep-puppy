from preppuppy.content.loader import load_drills


def run_drill(domain: str, limit: int = 3) -> list[str]:
    drills = load_drills()
    selected = drills.get(domain, ["No drills yet."])
    return selected[:limit]
