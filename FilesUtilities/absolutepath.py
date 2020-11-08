from pathlib import Path


def absolutepath(filepath):
    abspath = Path(filepath)
    return abspath.absolute()