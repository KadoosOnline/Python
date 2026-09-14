def min_max(numbers: list[int]) -> tuple[int, int]:
    'Return the smallest and the biggest number - two values in one tuple.'
    return min(numbers), max(numbers)

def main() -> None:
    my_list = [3, 77, -6, 14, 31]

    # Unpacking: the two returned values land in two variables.
    low, high = min_max(my_list)
    print(f'Min: {low}, Max: {high}')

    # Unpacking works on any sequence.
    a, b, c = (1, 2, 3)
    print(a, b, c)

    x, y, z = [10, 20, 30]
    print(x, y, z)

    # The classic swap - no temporary variable needed.
    x, y = y, x
    print(x, y)

    # '*' collects "the rest".
    first, *others = [1, 2, 3, 4, 5]
    print(first, others)

if __name__ == '__main__':
    main()
