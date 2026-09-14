# __call__ makes an OBJECT behave like a function.
class Multiplier:
    def __init__(self, factor: float) -> None:
        self.factor = factor

    def __call__(self, value: float) -> float:
        return value * self.factor


double = Multiplier(2)
triple = Multiplier(3)

print(double(10))        # 20  - the object is called like a function
print(triple(10))        # 30
print(callable(double))  # True


# __enter__ / __exit__ let us write our own 'with' block.
class Timer:
    'Measure how long the block inside "with" takes.'

    def __init__(self, label: str = 'block') -> None:
        self.label = label

    def __enter__(self):
        import time
        self.start = time.perf_counter()
        print(f'[{self.label}] started')
        return self          # what "as t" receives

    def __exit__(self, exc_type, exc_value, traceback):
        import time
        self.elapsed = time.perf_counter() - self.start
        print(f'[{self.label}] took {self.elapsed:.4f} s')
        # Returning False (or None) lets an exception propagate normally.
        return False


if __name__ == '__main__':
    with Timer('sum'):
        total = sum(range(2_000_000))

    with Timer('loop') as timer:
        total = 0
        for i in range(2_000_000):
            total += i
    print('elapsed was', round(timer.elapsed, 4))
