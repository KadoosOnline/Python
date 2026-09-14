'''Tic-tac-toe: the player (X) against a simple computer (O).

Review of: lists, functions, validation, loops and the os module.
'''

import os
import random

PLAYER_SIGN = 'X'
AI_SIGN = 'O'

WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),      # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),      # columns
    (0, 4, 8), (2, 4, 6),                 # diagonals
]


def new_board() -> list[str]:
    'Return a fresh board where every cell shows its own number.'
    return ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def clear_screen() -> None:
    'Clear the terminal on Windows as well as on Linux/macOS.'
    os.system('cls' if os.name == 'nt' else 'clear')


def show_board(board: list[str]) -> None:
    'Draw the board.'
    print()
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print()


def convert_persian_digits(text: str) -> str:
    'Turn Persian digits into English ones so both keyboards work.'
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    table = str.maketrans(persian_digits, english_digits)
    return text.translate(table)


def is_legal(board: list[str], move: str) -> bool:
    'A move is legal when it is 1-9 and the cell is still free.'
    if not move.isdigit():
        return False

    number = int(move)
    if number < 1 or number > 9:
        return False

    return board[number - 1] not in (PLAYER_SIGN, AI_SIGN)


def set_move(board: list[str], move: str, sign: str) -> None:
    'Write a sign into the chosen cell.'
    board[int(move) - 1] = sign


def has_won(board: list[str], sign: str) -> bool:
    'Return True when the given sign owns a full line.'
    for a, b, c in WINNING_LINES:
        if board[a] == board[b] == board[c] == sign:
            return True
    return False


def is_full(board: list[str]) -> bool:
    'Return True when no cell is free any more.'
    for cell in board:
        if cell not in (PLAYER_SIGN, AI_SIGN):
            return False
    return True


def free_cells(board: list[str]) -> list[str]:
    'Return the numbers of the cells that are still free.'
    return [cell for cell in board if cell not in (PLAYER_SIGN, AI_SIGN)]


def read_player_move(board: list[str]) -> str:
    'Ask the player for a legal move, or "exit".'
    while True:
        raw = input("Choose a position (1-9) or type 'exit': ")
        move = convert_persian_digits(raw).strip()

        if move.lower() == 'exit':
            return 'exit'

        if is_legal(board, move):
            return move

        print('Invalid move! Try again.')


def play_one_game() -> str:
    '''Play a full game.

    Return 'player', 'ai', 'draw' or 'exit'.
    '''
    board = new_board()

    while True:
        show_board(board)

        move = read_player_move(board)
        if move == 'exit':
            return 'exit'

        set_move(board, move, PLAYER_SIGN)

        if has_won(board, PLAYER_SIGN):
            show_board(board)
            return 'player'

        if is_full(board):
            show_board(board)
            return 'draw'

        # The computer simply picks one of the free cells at random.
        ai_move = random.choice(free_cells(board))
        set_move(board, ai_move, AI_SIGN)
        print(f'The computer played {ai_move}.')

        if has_won(board, AI_SIGN):
            show_board(board)
            return 'ai'

        if is_full(board):
            show_board(board)
            return 'draw'


def main() -> None:
    player_score = 0
    ai_score = 0

    while True:
        clear_screen()
        print(f'Player: {player_score}  |  Computer: {ai_score}')

        result = play_one_game()

        if result == 'exit':
            print('Game exited. Final score:')
            print(f'Player: {player_score}  |  Computer: {ai_score}')
            break

        if result == 'player':
            player_score += 1
            print('You win!')
        elif result == 'ai':
            ai_score += 1
            print('The computer wins!')
        else:
            print("It's a draw!")

        input('Press Enter for the next game...')


if __name__ == '__main__':
    main()
