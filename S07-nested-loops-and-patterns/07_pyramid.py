# A centred pyramid: row i has (SIZE - 1 - i) leading spaces
# and (2 * i + 1) stars.
SIZE = 5

for i in range(SIZE):
    for space in range(SIZE - 1 - i):
        print(' ', end='')
    for star in range(2 * i + 1):
        print('*', end='')
    print()

print('---')

# The same pyramid in one line per row, using string repetition.
for i in range(SIZE):
    print(' ' * (SIZE - 1 - i) + '*' * (2 * i + 1))
