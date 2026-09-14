'''Inheritance says "IS A", composition says "HAS A".

Choosing the wrong one is the most common OOP mistake.
'''


# --- Wrong: a car is NOT an engine -------------------------------------------
class Engine:
    def start(self):
        print('Engine started')


class BadCar(Engine):
    'A car that inherits from Engine also inherits everything an engine can do,'
    'which makes no sense and breaks as soon as Engine changes.'


# --- Right: a car HAS an engine ----------------------------------------------
class GoodCar:
    def __init__(self, brand: str, engine: Engine) -> None:
        self.brand = brand
        self.engine = engine

    def start(self) -> None:
        print(f'{self.brand}:', end=' ')
        self.engine.start()


# --- Right use of inheritance: an electric car IS A car ----------------------
class ElectricCar(GoodCar):
    def __init__(self, brand: str, battery_kwh: float) -> None:
        super().__init__(brand, Engine())
        self.battery_kwh = battery_kwh

    def start(self) -> None:
        print(f'{self.brand} starts silently ({self.battery_kwh} kWh).')


if __name__ == '__main__':
    GoodCar('Mazda', Engine()).start()
    ElectricCar('Tesla', 75).start()

    print()
    print('Ask yourself: "is a X really a Y?"')
    print('  Student IS A Person      -> inheritance')
    print('  Car HAS AN Engine        -> composition')
