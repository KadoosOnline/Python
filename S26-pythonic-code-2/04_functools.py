from functools import reduce, partial, lru_cache
import time

# reduce() folds a sequence into a single value.
numbers = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, numbers))          # 15 - but sum() is better
print(reduce(lambda a, b: a * b, numbers))          # 120 - here it is useful

# partial() freezes some arguments of a function.
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(square(5), cube(5))

# lru_cache remembers the results: a huge win for recursive functions.
def slow_fibonacci(n):
    if n < 2:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


@lru_cache(maxsize=None)
def fast_fibonacci(n):
    if n < 2:
        return n
    return fast_fibonacci(n - 1) + fast_fibonacci(n - 2)


start = time.perf_counter()
slow_fibonacci(30)
print(f'without cache: {time.perf_counter() - start:.3f} s')

start = time.perf_counter()
fast_fibonacci(30)
print(f'with cache:    {time.perf_counter() - start:.6f} s')

print(fast_fibonacci.cache_info())
