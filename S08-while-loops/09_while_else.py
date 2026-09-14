# A loop may have an 'else' block. It runs only when the loop finished
# normally, that is when it was NOT stopped by a 'break'.
number = int(input('Enter a number: '))

for i in range(2, number):
    if number % i == 0:
        print(f'{number} is divisible by {i}')
        break
else:
    # reached only when no divisor was found
    print(f'{number} is prime!')
