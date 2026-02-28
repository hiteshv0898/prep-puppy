from pathlib import Path
import yaml


def load_tracks() -> dict:
    path = Path(__file__).with_name("tracks.yaml")
    payload = yaml.safe_load(path.read_text())
    return payload if isinstance(payload, dict) else {}
