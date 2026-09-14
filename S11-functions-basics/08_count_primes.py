# Once the function exists, answering a bigger question is easy.
def is_prime(number):
    if number < 2:
        return False
    # Testing up to the square root is enough: a divisor bigger than the root
    # always has a partner smaller than the root.
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

count = 0

for number in range(50000, 100000):
    if is_prime(number):
        count += 1

print('Number of primes between 50000 and 100000:', count)
