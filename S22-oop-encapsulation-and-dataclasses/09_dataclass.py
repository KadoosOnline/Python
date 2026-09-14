# Writing __init__ by hand for a class that only holds data is tiring.
# @dataclass writes __init__, __repr__ and __eq__ for us.
from dataclasses import dataclass


@dataclass
class User:
    name: str            # the type hint is REQUIRED here
    age: int


u1 = User('Adam', 25)
print(u1.name)
print(u1.age)
print(u1)                # __repr__ for free: User(name='Adam', age=25)

u2 = User('Adam', 25)

# __eq__ for free: two dataclasses are equal when their fields are equal.
if u1 == u2:
    print('They are the same person!')

# Without @dataclass the comparison would be False, because a normal class
# compares the identity of the objects, not their content.
class PlainUser:
    def __init__(self, name, age):
        self.name = name
        self.age = age

print(PlainUser('Adam', 25) == PlainUser('Adam', 25))     # False
