from typing import Optional

from app.app import LabyrinthApplication

_app: Optional[LabyrinthApplication] = None


def setup_app(configuration_path: str) -> None:
    global _app
    if not _app:
        _app = LabyrinthApplication(configuration_path=configuration_path)
    else:
        raise Exception("You can't call setup_app several times!")


def get_app() -> LabyrinthApplication:
    if not _app:
        raise Exception("You need to setup the app before trying to get it.")
    else:
        return _app
