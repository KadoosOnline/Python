# To push the stars to the right we print SPACES first.
# Row i gets (SIZE - 1 - i) spaces and (i + 1) stars.
SIZE = 5

for i in range(SIZE):
    for j in range(SIZE):
        if j < SIZE - 1 - i:
            print(' ', end=' ')   # a space keeps the column width
        else:
            print('*', end=' ')
    print()
