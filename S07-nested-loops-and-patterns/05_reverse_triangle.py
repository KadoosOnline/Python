# A triangle that shrinks: 5 stars, then 4, then 3 ...
SIZE = 5

for i in range(SIZE, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()

print('---')

# The same shape written with a condition instead of a counting-down range.
for i in range(SIZE):
    for j in range(SIZE):
        if i <= j:
            print('*', end=' ')
    print()
