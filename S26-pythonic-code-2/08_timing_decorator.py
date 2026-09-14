'''The most useful decorator of everyday life: measuring a function.'''

import time
from functools import wraps


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'{func.__name__} took {elapsed:.4f} seconds')
        return result
    return wrapper


@timing
def slow_function():
    time.sleep(1)
    print('Function finished')


@timing
def sum_with_loop(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total


@timing
def sum_with_builtin(n: int) -> int:
    return sum(range(n))


if __name__ == '__main__':
    slow_function()
    sum_with_loop(5_000_000)
    sum_with_builtin(5_000_000)
