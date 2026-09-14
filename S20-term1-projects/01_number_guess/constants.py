'''All the texts and the levels of the game.'''

LEVELS = [
    {
        'level_number': 1,
        'number': 2,
        'hint': 'A number between 1 and 3: ',
    },
    {
        'level_number': 2,
        'number': -7,
        'hint': "A negative number greater than -10: ",
    },
    {
        'level_number': 3,
        'number': 42,
        'hint': 'A number between 1 and 100: ',
    },
]

START_HEARTS = 5

MESSAGE_WIN = 'You won the level!'
MESSAGE_GREATER = 'The secret number is greater!'
MESSAGE_LOWER = 'The secret number is lower!'
MESSAGE_GAMEOVER = 'Game over!'
MESSAGE_FINISHED = 'There are no more levels right now!'
