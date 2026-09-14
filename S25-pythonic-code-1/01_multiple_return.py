# A function returns one value - but that value can be a tuple,
# which looks exactly like "returning several values".
def min_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)      # the parentheses are optional


def statistics(numbers: list[int] | list[float]) -> tuple[float, float, float]:
    return sum(numbers), sum(numbers) / len(numbers), max(numbers)


def main() -> None:
    my_list = [3, 77, -6, 14, 31]

    low, high = min_max(my_list)
    print(f'Min: {low}, Max: {high}')

    total, average, biggest = statistics(my_list)
    print(total, average, biggest)

    # '_' is the usual name for a value we do not care about.
    _, average, _ = statistics(my_list)
    print(average)


if __name__ == '__main__':
    main()
