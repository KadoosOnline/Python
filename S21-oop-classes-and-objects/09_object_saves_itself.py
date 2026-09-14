'''An object can carry the code that saves and loads it.'''

import os


class Dog:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def bark(self) -> None:
        print(f"{self.name} says vagh! And its age is {self.age}.")

    def save(self) -> None:
        'Write this dog into its own text file.'
        with open(f'{self.name}.txt', 'w', encoding='utf-8') as file:
            file.write(f'{self.name}\n{self.age}\n')

    @staticmethod
    def load(name: str) -> 'Dog | None':
        'Read a dog back from its file (None when the file is missing).'
        filename = f'{name}.txt'
        if not os.path.exists(filename):
            return None

        with open(filename, encoding='utf-8') as file:
            saved_name = file.readline().strip()
            saved_age = int(file.readline().strip())

        return Dog(saved_name, saved_age)


if __name__ == '__main__':
    dogs = [Dog('Jessy', 3), Dog('Blacky', 5)]

    for dog in dogs:
        dog.bark()
        dog.save()

    loaded = Dog.load('Jessy')
    if loaded is not None:
        print('Loaded from the file:', loaded.name, loaded.age)
