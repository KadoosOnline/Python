'''Rock - paper - scissors, first player to three points wins.

Review of: dictionaries, random, while loops and functions.
'''

import random

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

MOVES = [ROCK, PAPER, SCISSORS]

# BEATS[a] is the move that 'a' defeats. One dictionary replaces six elif lines.
BEATS = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}

POINTS_TO_WIN = 3


def read_move(player: str) -> str:
    'Ask a player for a valid move (or "exit").'
    while True:
        move = input(f'{player}, enter your move (rock/paper/scissors): ').lower().strip()

        if move == 'exit' or move in MOVES:
            return move

        print('Unknown move, try again.')


def winner_of(move1: str, move2: str) -> int:
    '''Return 0 for a draw, 1 when move1 wins, 2 when move2 wins.'''
    if move1 == move2:
        return 0
    if BEATS[move1] == move2:
        return 1
    return 2


def main() -> None:
    player_score = 0
    computer_score = 0

    while True:
        player_move = read_move('Player')

        if player_move == 'exit':
            print('Goodbye!')
            break

        computer_move = random.choice(MOVES)
        print('The computer played:', computer_move)

        result = winner_of(player_move, computer_move)

        if result == 0:
            print('Nobody won this round.')
        elif result == 1:
            player_score += 1
            print('You won this round!')
        else:
            computer_score += 1
            print('The computer won this round!')

        print(f'Score - you: {player_score}, computer: {computer_score}\n')

        if player_score == POINTS_TO_WIN:
            print('You won the match!')
            break

        if computer_score == POINTS_TO_WIN:
            print('The computer won the match!')
            break


if __name__ == '__main__':
    main()
