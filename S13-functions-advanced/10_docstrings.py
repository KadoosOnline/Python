'''Module docstring: a short description of what this file does.'''


def area_of_rectangle(length: float, width: float) -> float:
    '''Return the area of a rectangle.

    Args:
        length: the length of the rectangle.
        width: the width of the rectangle.

    Returns:
        The area, i.e. length * width.
    '''
    return length * width


def main() -> None:
    print(area_of_rectangle(3, 4))

    # A docstring is stored in the function and can be read at run time.
    print(area_of_rectangle.__doc__)

    # help() displays it nicely.
    help(area_of_rectangle)


if __name__ == '__main__':
    main()
