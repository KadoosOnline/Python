def main() -> None:
    l = [1, 2, 2, 3]
    print(set(l))              # {1, 2, 3} -> the duplicates disappear

    t = (4, 5, 5, 6)
    print(set(t))

    d = {'a': 1, 'b': 2}
    print(set(d))              # the keys
    print(set(d.items()))      # the pairs, as tuples

    # Only immutable values can go into a set:
    # set([[1, 2]])   ->  TypeError: unhashable type: 'list'

if __name__ == '__main__':
    main()
