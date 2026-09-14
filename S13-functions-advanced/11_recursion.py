# A recursive function is a function that calls itself.
# It always needs a BASE CASE, otherwise it never stops.

def factorial(n: int) -> int:
    'n! computed recursively.'
    if n <= 1:            # base case
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    'The n-th Fibonacci number (0, 1, 1, 2, 3, 5, ...).'
    if n < 2:             # two base cases: fib(0) = 0 and fib(1) = 1
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def countdown(n: int) -> None:
    'Print n, n-1, ... 1 and then "Go!".'
    if n == 0:
        print('Go!')
        return
    print(n)
    countdown(n - 1)


def main() -> None:
    print(factorial(5))                       # 120
    print([fibonacci(i) for i in range(10)])
    countdown(5)

    # Recursion is elegant but not free: every call uses memory, and Python
    # stops at about 1000 nested calls (RecursionError). A loop is often better.


if __name__ == '__main__':
    main()
