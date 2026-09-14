'''Guess the hidden word, one letter at a time.

Review of: strings, lists, sets, functions, modules and input validation.
'''

import random

from utility import WORDS, MAX_WRONG_GUESSES


def mask_word(word: str, found_letters: set[str]) -> str:
    'Show the letters already found and hide the others behind "_".'
    masked = ''
    for letter in word:
        if letter in found_letters:
            masked += letter
        else:
            masked += '_'
        masked += ' '
    return masked.strip()


def read_letter(already_tried: set[str]) -> str:
    'Ask for one single letter that was not tried before.'
    while True:
        letter = input('Enter a letter: ').lower().strip()

        if len(letter) != 1:
            print('You can only enter one letter!')
            continue

        if not letter.isalpha():
            print('Letters only, please.')
            continue

        if letter in already_tried:
            print('You already tried that one.')
            continue

        return letter


def play(word: str) -> bool:
    'Play one word. Return True when the player found it.'
    found_letters: set[str] = set()
    tried_letters: set[str] = set()
    wrong_guesses = 0

    print(f'\nThe word has {len(word)} letters!')
    print(mask_word(word, found_letters))

    while wrong_guesses < MAX_WRONG_GUESSES:
        letter = read_letter(tried_letters)
        tried_letters.add(letter)

        if letter in word:
            found_letters.add(letter)
            print('Yes!')
        else:
            wrong_guesses += 1
            print(f'No. Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}')

        print(mask_word(word, found_letters))

        # The word is complete when every one of its letters has been found.
        if set(word) == set(word) & found_letters:
            print(f'You win! The word was {word.capitalize()}.')
            return True

    print(f'You lost. The word was {word.capitalize()}.')
    return False


def main() -> None:
    words = WORDS.copy()
    random.shuffle(words)

    score = 0

    for word in words:
        if play(word.lower()):
            score += 1

        if input('\nPlay another word? (y/n) ').lower() != 'y':
            break

    print(f'\nYou found {score} word(s). Thanks for playing!')


if __name__ == '__main__':
    main()
