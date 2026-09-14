# Instead of a star we can print the value of the inner counter.
SIZE = 6

for i in range(1, SIZE + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

print('---')

# And here the row number is repeated instead.
for i in range(1, SIZE + 1):
    for j in range(1, i + 1):
        print(i, end=' ')
    print()
