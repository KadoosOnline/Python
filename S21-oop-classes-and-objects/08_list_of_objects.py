# Objects are values like any other: they can live in a list, in a dictionary,
# be passed to a function and be returned from one.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says vagh! And its age is {self.age}.")


def oldest(dogs):
    'Return the oldest dog of a list.'
    best = dogs[0]
    for dog in dogs:
        if dog.age > best.age:
            best = dog
    return best


if __name__ == '__main__':
    dogs = [
        Dog('Jessy', 3),
        Dog('Blacky', 5),
        Dog('Rex', 1),
    ]

    dogs[1].bark()

    for dog in dogs:
        dog.bark()

    print('The oldest is', oldest(dogs).name)

    # Sorting a list of objects needs a key that says WHAT to compare.
    for dog in sorted(dogs, key=lambda d: d.age):
        print(dog.name, dog.age)
