'''A second module in the same package.'''


def sub(num1: float, num2: float) -> float:
    'Return the difference of two numbers.'
    return num1 - num2


def div(num1: float, num2: float) -> float:
    'Return the quotient of two numbers.'
    if num2 == 0:
        raise ZeroDivisionError('num2 must not be zero')
    return num1 / num2
