'''A 2-D vector class that uses many dunder methods at once.'''

import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # --- text representations ---
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'

    # --- arithmetic ---
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, factor: float) -> 'Vector':
        return Vector(self.x * factor, self.y * factor)

    def __rmul__(self, factor: float) -> 'Vector':
        return self * factor

    def __neg__(self) -> 'Vector':
        return Vector(-self.x, -self.y)

    # --- comparison ---
    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    # --- built-in functions ---
    def __abs__(self) -> float:
        'abs(v) returns the length of the vector.'
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __bool__(self) -> bool:
        return abs(self) != 0

    def __getitem__(self, index: int) -> float:
        'v[0] is x, v[1] is y.'
        return (self.x, self.y)[index]

    def __iter__(self):
        'Allows  x, y = v'
        yield self.x
        yield self.y


if __name__ == '__main__':
    a = Vector(3, 4)
    b = Vector(1, 2)

    print(a, repr(a))
    print(a + b)
    print(a - b)
    print(a * 2, 2 * a)
    print(-a)
    print(abs(a))            # 5.0
    print(a == Vector(3, 4)) # True
    print(a[0], a[1])
    x, y = a                 # unpacking, thanks to __iter__
    print(x, y)
    print(bool(Vector(0, 0)))
