# When the child defines a method that already exists in the parent,
# the child version wins. This is called OVERRIDING.
class Animal:
    def speak(self):
        print('Some generic sound')

    def describe(self):
        print('I am an animal and I say:')
        self.speak()          # calls the CHILD version when self is a child


class Dog(Animal):
    def speak(self):
        print('Bark')


class Cat(Animal):
    def speak(self):
        print('Meow')


if __name__ == '__main__':
    Animal().describe()
    Dog().describe()
    Cat().describe()
