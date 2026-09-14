'''Guess the number - with levels and lives.

Review of: while loops, functions, lists of dictionaries, exceptions,
and a constants module.
'''

from constants import (
    LEVELS,
    START_HEARTS,
    MESSAGE_WIN,
    MESSAGE_GREATER,
    MESSAGE_LOWER,
    MESSAGE_GAMEOVER,
    MESSAGE_FINISHED,
)


def show_hearts(count: int) -> None:
    'Draw the remaining lives.'
    print('Hearts: ' + '*' * count)


def read_number(message: str) -> int:
    'Ask until the user really types a whole number.'
    while True:
        try:
            return int(input(message))
        except ValueError:
            print('Please type a whole number.')


def play_level(level: dict, hearts: int) -> int:
    '''Play one level.

    Returns the number of hearts left; 0 means the player lost.
    '''
    secret = level['number']

    while hearts > 0:
        guess = read_number(level['hint'])

        if guess == secret:
            print(MESSAGE_WIN)
            hearts += 1                 # a bonus life for winning the level
            show_hearts(hearts)
            return hearts

        if guess > secret:
            print(MESSAGE_LOWER)
        else:
            print(MESSAGE_GREATER)

        hearts -= 1
        show_hearts(hearts)

    return 0


def main() -> None:
    hearts = START_HEARTS
    show_hearts(hearts)

    for level in LEVELS:
        print(f"\n--- Level {level['level_number']} ---")
        hearts = play_level(level, hearts)

        if hearts == 0:
            print(MESSAGE_GAMEOVER)
            return          # leave the game at once

    print(MESSAGE_FINISHED)


if __name__ == '__main__':
    main()
