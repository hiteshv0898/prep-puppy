from preppuppy.content.loader import load_mocks


def run_mock(track: str) -> list[str]:
    mocks = load_mocks()
    return mocks.get(track, ["No mock scenario yet."])
