# The prime test of session 08, turned into a reusable function.
def is_prime(number):
    # 0, 1 and the negative numbers are not prime.
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False     # a divisor was found -> stop immediately

    return True              # no divisor was found

user_input = input('Enter a number: ')
n = int(user_input)

if is_prime(n):
    print('Prime!')
else:
    print('Not prime.')

# The same function on a whole list of numbers.
numbers = [13, 11, 6, 8, 2, 7, 21, 1, 0, -3]
for num in numbers:
    print(num, is_prime(num))
