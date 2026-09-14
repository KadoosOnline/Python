names = ['Ali', 'Sara', 'Reza']


# The C way - it works, but it is not Python.
for i in range(len(names)):
    print(i, names[i])

print('---')

# enumerate() gives the index AND the item.
for index, name in enumerate(names):
    print(index, name)

print('---')

# 'start' changes the first index - perfect for a numbered menu.
for number, name in enumerate(names, start=1):
    print(f'{number}) {name}')

print('---')

# enumerate() works on anything we can loop over.
for index, letter in enumerate('Kadoos'):
    print(index, letter)

# It is also the clean way of finding a position.
for index, name in enumerate(names):
    if name == 'Sara':
        print('Sara is at index', index)
        break
