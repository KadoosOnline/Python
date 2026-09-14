# A function that contains 'yield' is a GENERATOR: it does not run when it is
# called; it runs a little more every time you ask for the next value.
def simple_gen():
    print('Start')
    yield 1
    print('Yield after 1')
    yield 2
    print('Yield after 2')
    yield 3
    print('Finish!')


def main() -> None:
    g = simple_gen()
    print(g)                 # <generator object ...> - nothing has run yet

    print(next(g))           # runs until the first yield
    print(next(g))
    print(next(g))

    # A fourth next() would raise StopIteration - that is exactly what a
    # 'for' loop catches for us.
    try:
        next(g)
    except StopIteration:
        print('the generator is exhausted')

    print('--- with a for loop ---')
    for value in simple_gen():
        print('got', value)

    # A generator can only be read once.
    g2 = simple_gen()
    print(list(g2))
    print(list(g2))          # [] - already exhausted


if __name__ == '__main__':
    main()
