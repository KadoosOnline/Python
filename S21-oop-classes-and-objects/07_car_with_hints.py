'''The same ideas, written with type hints and a main() function.'''


class Car:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand: str = brand
        self.model: str = model
        self.year: int = year

    def display_info(self) -> None:
        'Print a readable description of the car.'
        print(f'{self.year} {self.brand} {self.model}')

    def age(self, current_year: int = 2026) -> int:
        'Return how old the car is.'
        return current_year - self.year


def main() -> None:
    car1: Car = Car(brand='Mazda', model='6', year=2018)
    car1.display_info()
    print('Age:', car1.age())


if __name__ == '__main__':
    main()
