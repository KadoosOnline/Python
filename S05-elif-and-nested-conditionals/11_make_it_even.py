# If the number is odd, make it even by adding 1, then print its square.
user_input = input('Please enter a number: ')
number = int(user_input)

if number % 2 != 0:
    number += 1

result = number ** 2
print('Result:', result)
