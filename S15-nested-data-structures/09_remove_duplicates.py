# How do I remove the duplicates from a list?
def main() -> None:
    numbers = [1, 2, 3, 3, 4, 5, 5, 5]

    # set() drops the duplicates, list() turns it back into a list.
    print(list(set(numbers)))

    # A set has no order, so sort it when the order matters.
    print(sorted(set(numbers)))

    # A complete program: read numbers until 'stop', then show them
    # without duplicates and in order.
    values: list[float] = []
    while True:
        user_input = input('Enter a number (or "stop"): ')
        if user_input == 'stop':
            break
        values.append(float(user_input))

    print(sorted(set(values)))

if __name__ == '__main__':
    main()
