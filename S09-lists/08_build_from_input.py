# Starting from an empty list and filling it with append().
numbers = []

while True:
    user_input = input('Enter a number (or "exit"): ')

    if user_input == 'exit':
        break

    numbers.append(float(user_input))

print('You entered:', numbers)
print('How many:', len(numbers))

if len(numbers) > 0:
    total = 0
    for number in numbers:
        total += number
    print('Average:', total / len(numbers))
