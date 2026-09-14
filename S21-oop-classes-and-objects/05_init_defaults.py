# The parameters of __init__ can have default values, like any function.
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age


if __name__ == '__main__':
    user_input = input('Enter your name: ')

    p1 = Person(user_input)        # age takes its default
    p2 = Person('Reza', 22)

    print(p1.name, p1.age)
    print(p2.name, p2.age)

    # Remember the trap of session 13: never use a list as a default value.
    class Basket:
        def __init__(self, items=None):
            # a NEW list for every basket
            self.items = items if items is not None else []

    b1 = Basket()
    b2 = Basket()
    b1.items.append('apple')
    print(b1.items, b2.items)      # ['apple'] []
