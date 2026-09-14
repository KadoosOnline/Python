# A decorator is a function that takes a function and returns a new one.
# It is used to add a behaviour WITHOUT touching the original code.
def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Call {func.__name__} with {args} {kwargs}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result}')
        return result                # never forget to return the result!
    return wrapper


@logger                              # exactly the same as: add = logger(add)
def add(num1: float, num2: float) -> float:
    return num1 + num2


@logger
def mul(num1: float, num2: float) -> float:
    return num1 * num2


def main() -> None:
    total = add(3, 4)
    product = mul(3, 4)
    print(total, product)

    # Without the '@' syntax it would be written like this:
    def sub(a, b):
        return a - b

    sub = logger(sub)
    sub(10, 3)


if __name__ == '__main__':
    main()
