# A class is a blueprint. Writing it creates NOTHING by itself.
class MyClass:
    x = 5
    y = 'Hello'


def main():
    # Calling the class like a function creates an OBJECT (an instance).
    p1 = MyClass()
    print(p1.x)          # 5

    # Every object is independent: changing p2 does not touch p1.
    p2 = MyClass()
    p2.x = 12
    print(p2.x)          # 12
    print(p1.x)          # 5

    # A class is a type, exactly like int or str.
    a = 2
    print(type(a))       # <class 'int'>
    print(type(p1))      # <class '__main__.MyClass'>
    print(isinstance(p1, MyClass))   # True


if __name__ == '__main__':
    main()
