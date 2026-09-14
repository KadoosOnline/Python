# Linear search: walk through the list until the value is found.
numbers = [30, 20, 45, 18, -7, 22]

target = int(input('Which number are you looking for? '))

found_at = -1                     # -1 means "not found yet"

for i in range(len(numbers)):
    if numbers[i] == target:
        found_at = i
        break                     # stop at the first match

if found_at == -1:
    print('Not found.')
else:
    print(f'Found at index {found_at}.')

# Python offers the same thing directly:
if target in numbers:
    print('index() says:', numbers.index(target))
