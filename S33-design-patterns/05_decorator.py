'''DECORATOR - structural pattern.

Problem:  add a behaviour (logging, timing, caching, permission checks) to a
          function without changing its code and without copying it everywhere.
Solution: wrap it in another function.

We already used this in session 26; here it is as a PATTERN.
'''

import time
from functools import wraps


def timing_decorator(func):
    'Measure how long the decorated function takes.'

    @wraps(func)          # keeps the name and the docstring of func
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)      # the original behaviour
        end = time.time()
        print(f'{func.__name__} took {end - start:.4f} seconds')
        return result

    return wrapper


def audit(username: str):
    'A decorator with a parameter: who is allowed to run this?'
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'[audit] {username} called {func.__name__}')
            return func(*args, **kwargs)
        return wrapper
    return decorator


@timing_decorator
def slow_function():
    'A function that takes some time.'
    time.sleep(1)
    print('Function finished')


@audit('admin')
@timing_decorator          # decorators stack: the closest one wraps first
def compute(n: int) -> int:
    return sum(range(n))


if __name__ == '__main__':
    slow_function()
    print(compute(3_000_000))

    # Note the difference with the DECORATOR of the classic catalogue:
    # in Python the pattern is usually applied to FUNCTIONS with '@',
    # while the original pattern wraps OBJECTS. The idea is the same:
    # add behaviour by wrapping, not by inheriting.
