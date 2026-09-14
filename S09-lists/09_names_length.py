# Reading names into a list and computing the average length of the names.
names = []

while True:
    user_input = input('Enter a name (or "exit"): ')

    if user_input == 'exit':
        break

    names.append(user_input)

if len(names) == 0:
    print('No name was entered.')
else:
    total = 0
    for name in names:
        total += len(name)

    print('Average length of the names:', total / len(names))
