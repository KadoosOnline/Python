from functools import wraps


# A decorator that takes parameters needs THREE levels:
#   the factory -> the decorator -> the wrapper
def repeat(times: int):
    'Run the decorated function "times" times.'
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def greet(name: str) -> None:
    print(f'Hello {name}!')


def require_positive(func):
    'A decorator that validates the arguments.'
    @wraps(func)
    def wrapper(*args, **kwargs):
        for value in args:
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f'{func.__name__} refuses negative values')
        return func(*args, **kwargs)
    return wrapper


@require_positive
def area(width: float, height: float) -> float:
    return width * height


if __name__ == '__main__':
    greet('Kadoos')

    print(area(3, 4))
    try:
        area(-3, 4)
    except ValueError as e:
        print('Refused:', e)
