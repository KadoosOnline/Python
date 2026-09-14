# The factorial of n is 1 * 2 * 3 * ... * n
# For a product the accumulator must start at 1, not at 0.
user_input = input('Enter a number: ')
number = int(user_input)

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print(f'{number}! = {factorial}')
