# Two accumulators: the total and how many numbers were entered.
total = 0
counter = 0

while True:
    user_input = input('Enter a number (or "exit"): ')

    if user_input == 'exit':
        break

    number = float(user_input)

    total += number
    counter += 1

    print('Average is:', total / counter)

# After the loop, counter may still be 0 - never divide by it blindly.
if counter == 0:
    print('No number was entered.')
else:
    print('Final average:', total / counter)
