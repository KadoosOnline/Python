# A prime number is only divisible by 1 and by itself.
# As soon as we find one divisor we can stop looking -> 'break'.
user_input = input('Enter your number: ')
number = int(user_input)

# 0, 1 and the negative numbers are NOT prime, so we handle them separately.
if number < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break            # no need to test the remaining divisors

if is_prime:
    print("It's prime!")
else:
    print("It's not prime.")
