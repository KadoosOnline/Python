# 'continue' skips the REST of the current turn and goes back to the top.
# Here the odd numbers are simply ignored.
total = 0

while True:
    user_input = input('Enter a number (or "exit"): ')

    if user_input == 'exit':
        break

    number = int(user_input)

    if number % 2 != 0:
        print('Odd number ignored.')
        continue                 # go back to the input() line

    total += number
    print('Sum is:', total)
