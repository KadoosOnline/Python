from functools import wraps


# Problem: a naive decorator replaces the function, so its name and its
# docstring disappear.
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def good_decorator(func):
    @wraps(func)              # copies __name__, __doc__, ... onto the wrapper
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@bad_decorator
def hello_bad():
    'Say hello.'


@good_decorator
def hello_good():
    'Say hello.'


print(hello_bad.__name__, '|', hello_bad.__doc__)     # wrapper | None
print(hello_good.__name__, '|', hello_good.__doc__)   # hello_good | Say hello.

# Always use @wraps in your decorators.
