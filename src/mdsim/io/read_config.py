import tomllib
from pathlib import Path

def load_config(path: str) -> dict:
    import tomllib
    with open(path, "rb") as f:
        return tomllib.load(f)
