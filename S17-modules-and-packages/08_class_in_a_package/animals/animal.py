'''The Animal class (classes are studied in detail in session 21).'''


class Animal:
    def __init__(self, name: str, weight: int, is_pet: bool = False) -> None:
        self.name = name
        self.weight = weight
        self.is_pet = is_pet

    def __str__(self) -> str:
        return self.name
