# A child class receives everything the parent has, and may add more.
class Animal:
    def run(self):
        print('Running...')


class Dog(Animal):          # Dog inherits from Animal
    def speak(self):
        print('Bark')


if __name__ == '__main__':
    dog = Dog()
    dog.speak()             # its own method
    dog.run()               # inherited from Animal

    # The parent knows nothing about the child:
    animal = Animal()
    animal.run()
    # animal.speak()   ->  AttributeError
