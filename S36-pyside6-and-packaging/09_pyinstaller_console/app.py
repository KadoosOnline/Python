'''The program we are going to turn into a real .exe file.

It is deliberately tiny: the point of examples 09-12 is the BUILD, not the
code. Note the last line -- without it a console program opened by a
double-click flashes on the screen and disappears before you can read
anything.
'''


def main() -> None:
    print('Hello from Kadoos Institute!')
    name = input('What is your name? ')
    print(f'Nice to meet you, {name}.')

    # A console .exe closes its window as soon as the program ends.
    input('Press Enter to exit...')


if __name__ == '__main__':
    main()
