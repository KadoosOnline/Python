'''A fully annotated and documented version of the prime test.'''


def is_prime(number: int) -> bool:
    '''Return True when 'number' is a prime number.'''
    if number < 2:
        return False

    # Testing the divisors up to the square root is enough.
    divisor: int = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def main() -> None:
    user_input: str = input('Enter a number: ')
    number: int = int(user_input)

    if is_prime(number):
        print(number, 'is prime.')
    else:
        print(number, 'is NOT prime.')


if __name__ == '__main__':
    main()
