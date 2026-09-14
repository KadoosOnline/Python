'''Where the files of the application live.

Every path in the program goes through this module, so there is exactly one
place to change when the layout moves -- and exactly one place that knows
about PyInstaller (session 36).

    resource_path()  what we READ and ship with the program (the .ui files)
    data_dir()       what we WRITE, and that must survive a restart
'''

import sys
from pathlib import Path


def is_frozen() -> bool:
    '''True inside a PyInstaller executable.'''
    return getattr(sys, 'frozen', False)


def project_root() -> Path:
    '''The folder that holds `main.py` (or the .exe once frozen).'''
    if is_frozen():
        return Path(sys.executable).resolve().parent
    # paths.py -> core -> library
    return Path(__file__).resolve().parent.parent


def resource_path(relative: str) -> Path:
    '''A file that was SHIPPED with the program (read-only).'''
    if is_frozen() and hasattr(sys, '_MEIPASS'):
        # --add-data puts the files here (session 36).
        return Path(sys._MEIPASS) / relative      # type: ignore[attr-defined]
    return project_root() / relative


def ui_path(name: str) -> Path:
    '''One of the Qt Designer files.'''
    return resource_path(f'ui/{name}')


def data_dir() -> Path:
    '''Where the program WRITES. Created if it does not exist yet.'''
    folder = project_root() / 'data'
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def database_path() -> Path:
    return data_dir() / 'library.db'
