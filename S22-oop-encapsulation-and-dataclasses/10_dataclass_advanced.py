from dataclasses import dataclass, field, asdict


@dataclass
class Product:
    name: str
    price: float = 0.0                       # a default value
    tags: list[str] = field(default_factory=list)   # NEVER write tags: list = []

    def with_vat(self, rate: float = 0.09) -> float:
        'A dataclass can have normal methods too.'
        return self.price * (1 + rate)

    def __post_init__(self) -> None:
        '__post_init__ runs right after the generated __init__: validate here.'
        if self.price < 0:
            raise ValueError('the price cannot be negative')


p1 = Product('Notebook', 15_000)
p2 = Product('Pencil')
p1.tags.append('paper')

print(p1)
print(p2)
print(p2.tags)                # [] - each product has its OWN list
print(round(p1.with_vat()))
print(asdict(p1))             # turn it into a dictionary

# order=True generates <, <=, > and >= so the objects can be sorted.
@dataclass(order=True)
class Score:
    value: int
    student: str

scores = [Score(18, 'Ali'), Score(20, 'Sara'), Score(15, 'Reza')]
print(sorted(scores))

# frozen=True makes the object immutable (and hashable).
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p)
# p.x = 5    ->  FrozenInstanceError
print({Point(1, 2): 'origin-ish'})     # usable as a dictionary key

try:
    Product('Bad', -10)
except ValueError as e:
    print('Refused:', e)
