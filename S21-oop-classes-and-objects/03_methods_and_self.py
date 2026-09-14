# A method is a function written inside a class.
# Its first parameter is always 'self': the object the method was called on.
class MyClass:
    x = 5

    def hello(self):
        print(f'Hello {self.x}')

    def bye(self):
        print(f'Goodbye {self.x}')


if __name__ == '__main__':
    p1 = MyClass()
    p2 = MyClass()
    p3 = MyClass()

    print(p1.x, p2.x, p3.x)

    p1.x = 15
    p2.x = -7
    p3.x = 24

    # p1.hello() is really MyClass.hello(p1): that is where 'self' comes from.
    p1.hello()
    p2.hello()
    p3.hello()

    p1.bye()
    p2.bye()
    p3.bye()
