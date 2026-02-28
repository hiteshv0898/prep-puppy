from preppuppy.content.loader import load_lessons


def run_lesson(domain: str) -> dict:
    lessons = load_lessons()
    entry = lessons.get(domain, {})
    return {
        "title": entry.get("title", f"{domain} basics"),
        "bullets": entry.get("bullets", ["No content yet."]),
    }
