# The character depends on both counters: when (row + column) is even we print
# one character, otherwise the other one.
SIZE = 8

for row in range(SIZE):
    for column in range(SIZE):
        if (row + column) % 2 == 0:
            print('#', end=' ')
        else:
            print('.', end=' ')
    print()
