# __init__ runs automatically right after the object is created.
# It is where the instance attributes are born.
class Person:

    def __init__(self, name, age):
        self.name = name       # instance attribute, one per object
        self.age = age


if __name__ == '__main__':
    p1 = Person('Ali', 36)
    p2 = Person(name='Reza', age=22)     # keyword arguments work here too

    print(p1.name, p1.age)
    print(p2.name, p2.age)

    # Each object keeps its own values.
    p1.age = 37
    print(p1.age, p2.age)

    # __dict__ shows the instance attributes of an object.
    print(p1.__dict__)
