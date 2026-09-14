'''A complete example: an abstract shape and three real shapes.'''

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def area(self) -> float:
        'Return the area of the shape.'

    @abstractmethod
    def perimeter(self) -> float:
        'Return the perimeter of the shape.'

    def describe(self) -> str:
        'Shared by every shape - written only once.'
        return (f'{self.name:<10} area={self.area():>8.2f} '
                f'perimeter={self.perimeter():>8.2f}')


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__('Rectangle')
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)
        self.name = 'Square'


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__('Circle')
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


def main() -> None:
    shapes: list[Shape] = [Rectangle(3, 4), Square(5), Circle(2)]

    for shape in shapes:
        print(shape.describe())

    # Sorting different classes by a common method.
    print('\nSorted by area:')
    for shape in sorted(shapes, key=lambda s: s.area()):
        print(' ', shape.name, round(shape.area(), 2))


if __name__ == '__main__':
    main()
