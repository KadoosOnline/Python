'''A complete little program: a note book stored in a text file.

It puts together everything of this session: menus, loops, functions,
lists and files.
'''

import os

NOTES_FILE = 'notes.txt'


def load_notes() -> list[str]:
    'Return the notes stored in the file (an empty list when there is none).'
    if not os.path.exists(NOTES_FILE):
        return []

    with open(NOTES_FILE, encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() != '']


def save_notes(notes: list[str]) -> None:
    'Write the whole list back to the file.'
    with open(NOTES_FILE, 'w', encoding='utf-8') as f:
        for note in notes:
            f.write(note + '\n')


def show_notes(notes: list[str]) -> None:
    'Print the notes with their number.'
    if len(notes) == 0:
        print('(no note yet)')
        return
    for index, note in enumerate(notes, start=1):
        print(f'{index}. {note}')


def main() -> None:
    notes = load_notes()

    while True:
        print('\n1) Show the notes')
        print('2) Add a note')
        print('3) Delete a note')
        print('0) Exit')

        choice = input('Your choice: ')

        if choice == '1':
            show_notes(notes)
        elif choice == '2':
            text = input('The note: ')
            if text.strip() != '':
                notes.append(text.strip())
                save_notes(notes)
                print('Saved.')
        elif choice == '3':
            show_notes(notes)
            number = input('Number of the note to delete: ')
            if number.isdigit() and 1 <= int(number) <= len(notes):
                removed = notes.pop(int(number) - 1)
                save_notes(notes)
                print('Deleted:', removed)
            else:
                print('Wrong number.')
        elif choice == '0':
            print('Goodbye!')
            break
        else:
            print('Unknown option.')


if __name__ == '__main__':
    main()
