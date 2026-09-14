'''A small dice game: the player and the computer roll two dice.'''

import random


def roll_two_dice() -> int:
    'Roll two dice and return their total.'
    return random.randint(1, 6) + random.randint(1, 6)


def main() -> None:
    player_score = 0
    computer_score = 0

    for round_number in range(1, 4):
        input(f'Round {round_number} - press Enter to roll...')

        player = roll_two_dice()
        computer = roll_two_dice()

        print(f'You: {player}   Computer: {computer}')

        if player > computer:
            player_score += 1
            print('You win this round!')
        elif computer > player:
            computer_score += 1
            print('The computer wins this round!')
        else:
            print('Draw.')

    print(f'\nFinal score - you: {player_score}, computer: {computer_score}')


if __name__ == '__main__':
    main()
