def main() -> None:
    # Basic unpacking.
    a, b, c = [1, 2, 3]
    print(a, b, c)

    # Swapping without a temporary variable.
    a, b = b, a
    print(a, b)

    # '*' collects the rest into a list.
    first, *rest = [1, 2, 3, 4, 5]
    print(first, rest)

    *start, last = [1, 2, 3, 4, 5]
    print(start, last)

    first, *middle, last = [1, 2, 3, 4, 5]
    print(first, middle, last)

    # Nested unpacking.
    name, (city, code) = ('Ali', ('Rasht', 41))
    print(name, city, code)

    # Very common on a list of pairs.
    pairs = [('math', 20), ('physics', 18)]
    for subject, score in pairs:
        print(subject, score)

    # Merging containers with * and **.
    list1 = [1, 2]
    list2 = [3, 4]
    print([*list1, *list2])

    dict1 = {'a': 1}
    dict2 = {'b': 2}
    print({**dict1, **dict2})


if __name__ == '__main__':
    main()
