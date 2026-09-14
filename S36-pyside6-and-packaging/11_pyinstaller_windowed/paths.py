'''The two paths every frozen application needs. Read this file first.

When PyInstaller builds a `--onefile` executable, running it unpacks
everything into a TEMPORARY folder and deletes that folder when the program
ends. Python then sees:

    sys.frozen      -> True          (the attribute does not exist otherwise)
    sys._MEIPASS    -> the temporary folder
    __file__        -> a path INSIDE that temporary folder

That leads to the two classic bugs of a frozen program:

BUG 1 -- "my picture / my .ui file is not found"
    `Path(__file__).parent / 'logo.png'` works while you develop and fails in
    the .exe, because the file was never copied into the bundle. You have to
    ship it with `--add-data` and then look for it in `sys._MEIPASS`.
    -> use `resource_path()` below.

BUG 2 -- "my database is empty again every time"
    A database written next to `__file__` lands in the temporary folder and
    disappears with it. Anything the program WRITES must go somewhere
    permanent: next to the executable, or in the user's own folder.
    -> use `data_path()` below.

The rule in one line:
    resource_path() for what you READ and ship,
    data_path() for what you WRITE.
'''

import sys
from pathlib import Path


def is_frozen() -> bool:
    '''True when we are running inside a PyInstaller executable.'''
    return getattr(sys, 'frozen', False)


def resource_path(name: str) -> Path:
    '''Where to READ a file that was shipped with the program.'''
    if is_frozen():
        # PyInstaller unpacks --add-data files into sys._MEIPASS.
        base = Path(sys._MEIPASS)          # type: ignore[attr-defined]
    else:
        base = Path(__file__).parent
    return base / name


def data_path(name: str) -> Path:
    '''Where to WRITE a file so that it survives the next run.'''
    if is_frozen():
        # sys.executable is the .exe itself; its folder is permanent.
        base = Path(sys.executable).parent
    else:
        base = Path(__file__).parent
    return base / name
