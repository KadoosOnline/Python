# list() builds a list out of anything we can loop over.
def main() -> None:
    t = (1, 2, 3)
    print(list(t))                # [1, 2, 3]

    s = {4, 5, 6}
    print(list(s))                # order is not guaranteed

    d = {'a': 1, 'b': 2}
    print(list(d))                # ['a', 'b']  -> the KEYS
    print(list(d.values()))       # [1, 2]
    print(list(d.items()))        # [('a', 1), ('b', 2)]

    print(list('Kadoos'))         # ['K', 'a', 'd', 'o', 'o', 's']
    print(list(range(5)))         # [0, 1, 2, 3, 4]

if __name__ == '__main__':
    main()
