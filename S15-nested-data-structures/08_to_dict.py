def main() -> None:
    # dict() accepts a sequence of (key, value) pairs.
    pairs = [('a', 1), ('b', 2)]
    print(dict(pairs))

    pairs_tuple = (('x', 10), ('y', 20))
    print(dict(pairs_tuple))

    # zip() glues two sequences together, item by item.
    keys = ['name', 'age']
    values = ['Ali', 20]
    print(dict(zip(keys, values)))

    # zip() stops at the shortest sequence.
    print(list(zip([1, 2, 3], 'ab')))

    # It is also very handy in a loop.
    subjects = ['math', 'physics', 'english']
    scores = [20, 18, 19]
    for subject, score in zip(subjects, scores):
        print(f'{subject}: {score}')

if __name__ == '__main__':
    main()
