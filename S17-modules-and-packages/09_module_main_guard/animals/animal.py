'''This module can be RUN on its own and also be IMPORTED.'''


class Animal:
    def __init__(self, name: str, weight: int, is_pet: bool = False) -> None:
        self.name = name
        self.weight = weight
        self.is_pet = is_pet

    def __str__(self) -> str:
        return self.name


# Everything below runs only when this file is started directly
# (python animals/animal.py). Without this guard, the two animals would also
# be created and printed every time app.py imports the module.
if __name__ == '__main__':
    the_cat = Animal('Tom from the module', 7)
    print(the_cat)

    the_wolf = Animal('Fang from the module', 20)
    print(the_wolf)
