# A complete little program: read numbers until 'exit',
# then report several statistics about them.
numbers = []

while True:
    user_input = input('Enter a number (or "exit"): ')

    if user_input == 'exit':
        break

    numbers.append(float(user_input))

if len(numbers) == 0:
    print('Nothing to report.')
else:
    even_total = 0
    for number in numbers:
        if number % 2 == 0:
            even_total += number

    print('Count:  ', len(numbers))
    print('Sum:    ', sum(numbers))
    print('Average:', sum(numbers) / len(numbers))
    print('Max:    ', max(numbers))
    print('Min:    ', min(numbers))
    print('Sum of the even ones:', even_total)
    print('Sorted: ', sorted(numbers))
