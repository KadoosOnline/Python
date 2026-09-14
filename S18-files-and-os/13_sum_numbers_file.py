'''Add up all the numbers stored in numbers.txt, one per line.'''


def main() -> None:
    total: float = 0

    with open('numbers.txt', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line == '':
                continue
            total += float(line)

    print(f'Sum: {total}')


if __name__ == '__main__':
    main()
