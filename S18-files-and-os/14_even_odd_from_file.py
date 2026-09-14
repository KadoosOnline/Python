'''Read a single number from number.txt and say whether it is even.'''


def main() -> None:
    with open('number.txt', encoding='utf-8') as file:
        content: str = file.read().strip()
        number: int = int(content)

        if number % 2 == 0:
            print(f'{number} is even.')
        else:
            print(f'{number} is odd.')


if __name__ == '__main__':
    main()
