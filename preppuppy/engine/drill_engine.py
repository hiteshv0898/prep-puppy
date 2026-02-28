from preppuppy.content.loader import load_drills


def run_drill(domain: str) -> list[str]:
    drills = load_drills()
    return drills.get(domain, ["No drills yet."])
