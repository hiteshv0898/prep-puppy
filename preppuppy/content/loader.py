from pathlib import Path
import yaml


def load_yaml(name: str) -> dict:
    path = Path(__file__).with_name(f"{name}.yaml")
    payload = yaml.safe_load(path.read_text())
    return payload if isinstance(payload, dict) else {}


def load_lessons() -> dict:
    return load_yaml("lessons")


def load_drills() -> dict:
    return load_yaml("drills")


def load_mocks() -> dict:
    return load_yaml("mocks")
