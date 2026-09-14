# A set holds only UNIQUE values, and it has no order.
def main() -> None:
    my_set = {1, 1, 5, 3, 3, 3, 3, 7, 7}
    print(my_set)                  # {1, 3, 5, 7} - the duplicates are gone

    for item in my_set:
        print(item, end=' ')
    print()

    my_set.add(10)                 # add one item
    my_set.discard(1)              # remove, and stay silent when it is missing
    # my_set.remove(99)            # remove, but raise KeyError when missing
    print(my_set)

    print(5 in my_set)             # membership test - very fast on a set

    # The most common use: removing the duplicates of a list.
    numbers = [1, 2, 3, 3, 4, 5, 5, 5]
    unique = list(set(numbers))
    print(unique)

    # Careful: a set has no order, so sort it if the order matters.
    print(sorted(set(numbers)))

    # An empty set must be created with set(); {} is an empty DICTIONARY.
    empty_set = set()
    empty_dict = {}
    print(type(empty_set), type(empty_dict))

if __name__ == '__main__':
    main()
