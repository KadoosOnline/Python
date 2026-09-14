# Duck typing: "If it walks like a duck and quacks like a duck, it is a duck."
# Python does not care about the class; it only cares that the method exists.
class Dog:
    def speak(self):
        print('Bark')


class Cat:
    def speak(self):
        print('Meow')


class Robot:
    'Not an animal at all - but it can speak, so it fits.'
    def speak(self):
        print('Beep boop')


def talk(thing):
    thing.speak()          # no inheritance, no interface, no check


if __name__ == '__main__':
    talk(Dog())
    talk(Cat())
    talk(Robot())

    for thing in (Dog(), Cat(), Robot()):
        talk(thing)

    # If the method is missing we get an AttributeError at that moment.
    # hasattr() lets us check first.
    class Stone:
        pass

    stone = Stone()
    if hasattr(stone, 'speak'):
        talk(stone)
    else:
        print('A stone cannot speak.')
