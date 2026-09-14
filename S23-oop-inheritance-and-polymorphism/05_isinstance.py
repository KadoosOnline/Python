class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()

# isinstance() also answers True for the parents.
print(isinstance(dog, Dog))       # True
print(isinstance(dog, Animal))    # True
print(isinstance(dog, Cat))       # False

# type() is exact, isinstance() is not - prefer isinstance().
print(type(dog) is Dog)           # True
print(type(dog) is Animal)        # False

# issubclass() works on the classes themselves.
print(issubclass(Dog, Animal))    # True
print(issubclass(Animal, Dog))    # False

# Everything in Python inherits from object.
print(issubclass(Animal, object)) # True
