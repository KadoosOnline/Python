# A "sentinel" is a special value that means "stop".
# Here the sentinel is the word 'exit'.
total = 0

while True:                              # loop for ever ...
    user_input = input('Enter a number (or "exit"): ')

    if user_input == 'exit':
        break                            # ... until break jumps out of it

    number = float(user_input)
    total += number
    print('Sum is:', total)

print('Final sum:', total)
