numbers = [200, 350, 40, 1000, 270]

# Way 1 (the usual one): loop directly over the items.
for number in numbers:
    print(number, end=' ')
print()

# Way 2: loop over the indexes. Useful when we also need the position,
# or when we want to CHANGE the items.
for i in range(len(numbers)):
    print(f'index {i} -> {numbers[i]}')

# Changing every item needs the index version.
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)
