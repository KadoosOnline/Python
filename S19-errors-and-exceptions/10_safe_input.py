'''The most useful pattern of this session: reading a valid number.'''


def read_number(message: str) -> float:
    'Ask until the user really types a number.'
    while True:
        user_input = input(message)
        try:
            return float(user_input)
        except ValueError:
            print('That is not a number, try again.')


def read_int(message: str, minimum: int, maximum: int) -> int:
    'Ask until the user types a whole number inside the range.'
    while True:
        try:
            value = int(input(message))
        except ValueError:
            print('Please type digits only.')
            continue

        if value < minimum or value > maximum:
            print(f'The value must be between {minimum} and {maximum}.')
            continue

        return value


def main() -> None:
    a = read_number('Enter a number: ')
    b = read_number('Enter another number: ')
    print('Sum:', a + b)

    age = read_int('Enter your age (1-120): ', 1, 120)
    print('Your age is', age)


if __name__ == '__main__':
    main()
