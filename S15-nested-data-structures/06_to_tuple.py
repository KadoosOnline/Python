def main() -> None:
    l = [1, 2, 3]
    print(tuple(l))

    s = {4, 5, 6}
    print(tuple(s))

    d = {'a': 1, 'b': 2}
    print(tuple(d))            # the keys
    print(tuple(d.items()))    # (('a', 1), ('b', 2))

if __name__ == '__main__':
    main()
