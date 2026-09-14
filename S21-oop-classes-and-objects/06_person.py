# A class puts the data (name, age) and the behaviour (greet) together.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello, my name is {self.name}!')

    def have_birthday(self):
        'A method may change the state of the object.'
        self.age += 1
        print(f'{self.name} is now {self.age}.')

    def is_adult(self):
        'A method may also just answer a question.'
        return self.age >= 18


if __name__ == '__main__':
    p1 = Person('Ali', 32)
    p1.greet()
    p1.have_birthday()
    print(p1.is_adult())

    p2 = Person('Reza', 12)
    p2.greet()
    print(p2.is_adult())
