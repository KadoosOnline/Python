# Polymorphism: the same call gives a different result depending on the object.
class Shape:
    def area(self) -> float:
        raise NotImplementedError('every shape must implement area()')

    def name(self) -> str:
        return type(self).__name__


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2


class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)


if __name__ == '__main__':
    shapes: list[Shape] = [Rectangle(3, 4), Circle(5), Square(2)]

    # One single loop handles every kind of shape.
    for shape in shapes:
        print(f'{shape.name():<10} area = {shape.area():.2f}')

    print('Total area:', sum(shape.area() for shape in shapes))
