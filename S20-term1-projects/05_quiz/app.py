'''A quiz whose questions are stored in a text file.

File format, one question per line:
    question|correct answer|wrong 1|wrong 2|wrong 3

Review of: files, lists, dictionaries, random, exceptions and functions.
'''

import os
import random

QUESTIONS_FILE = 'questions.txt'


def load_questions(path: str) -> list[dict]:
    '''Read the file and return a list of questions.

    Every question is a dictionary: {'text': ..., 'correct': ..., 'options': [...]}
    '''
    if not os.path.exists(path):
        raise FileNotFoundError(f'{path} was not found')

    questions: list[dict] = []

    with open(path, encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if line == '':
                continue

            parts = line.split('|')
            if len(parts) < 3:
                print(f'[warning] line {line_number} is ignored (wrong format)')
                continue

            text = parts[0]
            correct = parts[1]
            options = parts[1:]
            random.shuffle(options)

            questions.append({
                'text': text,
                'correct': correct,
                'options': options,
            })

    return questions


def ask(question: dict, number: int) -> bool:
    'Ask one question and return True when the answer is correct.'
    print(f"\nQuestion {number}: {question['text']}")

    for index, option in enumerate(question['options'], start=1):
        print(f'  {index}) {option}')

    while True:
        answer = input('Your answer (number): ').strip()

        if not answer.isdigit() or not 1 <= int(answer) <= len(question['options']):
            print('Please type the number of one of the options.')
            continue

        chosen = question['options'][int(answer) - 1]
        break

    if chosen == question['correct']:
        print('Correct!')
        return True

    print(f"Wrong. The right answer was: {question['correct']}")
    return False


def main() -> None:
    try:
        questions = load_questions(QUESTIONS_FILE)
    except FileNotFoundError as e:
        print('Error:', e)
        return

    if len(questions) == 0:
        print('There is no question in the file.')
        return

    random.shuffle(questions)

    score = 0
    for number, question in enumerate(questions, start=1):
        if ask(question, number):
            score += 1

    print(f'\nYour score: {score} / {len(questions)}')

    percentage = score / len(questions) * 100
    print(f'That is {percentage:.0f}%.')

    if percentage >= 80:
        print('Excellent!')
    elif percentage >= 50:
        print('Not bad.')
    else:
        print('Time to review the first term :)')


if __name__ == '__main__':
    main()
