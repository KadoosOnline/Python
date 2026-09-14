'''A program with a data file, built from a .spec recipe.

`words.txt` is READ by the program and must travel inside the executable, so
it goes through `resource_path()` exactly like the icon of example 11.
'''

import random
import sys
from pathlib import Path


def resource_path(name: str) -> Path:
    '''Where to read a file that was shipped with the program.'''
    if getattr(sys, 'frozen', False):
        base = Path(sys._MEIPASS)          # type: ignore[attr-defined]
    else:
        base = Path(__file__).parent
    return base / name


def load_words() -> list[str]:
    path = resource_path('words.txt')
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except OSError as error:
        # This is the message you get when --add-data was forgotten.
        print(f'Cannot read {path}: {error}')
        return []


def main() -> None:
    words = load_words()
    if not words:
        input('Press Enter to exit...')
        return

    print(f'{len(words)} words were shipped with this program.')
    print('Today\'s word is:', random.choice(words))
    input('Press Enter to exit...')


if __name__ == '__main__':
    main()
