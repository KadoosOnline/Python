# A tuple is like a list, but it can NEVER be changed after it is created.
def main() -> None:
    my_tuple = (1, 'Hello', 2, 3, True, 3, 3, 4)

    print(my_tuple)
    print(my_tuple[1])         # indexing works
    print(my_tuple[2:5])       # slicing works
    print(len(my_tuple))
    print(my_tuple.count(3))   # 3 appears three times
    print(my_tuple.index(2))

    # my_tuple[0] = 100    ->  TypeError: 'tuple' object does not support
    #                          item assignment

    # A tuple with a single item needs a comma!
    one = (5,)
    not_a_tuple = (5)
    print(type(one), type(not_a_tuple))

    # The parentheses are optional.
    point = 3, 4
    print(point, type(point))

    # Why tuples? They are safe (nobody can modify them by mistake),
    # slightly faster, and they can be used as dictionary keys.
    distances = {(0, 0): 'origin', (3, 4): 'point A'}
    print(distances[(3, 4)])

if __name__ == '__main__':
    main()
