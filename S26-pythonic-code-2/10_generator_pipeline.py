'''Why generators matter: laziness and memory.'''


def primes():
    'An INFINITE generator of prime numbers.'
    number = 2
    while True:
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                break
        else:
            yield number
        number += 1


def read_large_file(path: str):
    'Yield the lines of a file one by one, whatever its size.'
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')


def main() -> None:
    # An infinite generator is fine as long as we stop asking.
    generator = primes()
    for _ in range(20):
        print(next(generator), end=' ')
    print()

    # A list comprehension builds everything in memory,
    # a generator expression computes on demand.
    import sys
    as_list = [x ** 2 for x in range(100_000)]
    as_generator = (x ** 2 for x in range(100_000))
    print('list      :', sys.getsizeof(as_list), 'bytes')
    print('generator :', sys.getsizeof(as_generator), 'bytes')

    # A pipeline: each step is lazy, nothing is stored.
    with open('demo.txt', 'w', encoding='utf-8') as f:
        f.write('10\n-5\n8\n\n42\n')

    lines = read_large_file('demo.txt')
    non_empty = (line for line in lines if line.strip())
    numbers = (int(line) for line in non_empty)
    positives = (n for n in numbers if n > 0)

    print('sum of the positive numbers:', sum(positives))


if __name__ == '__main__':
    main()
