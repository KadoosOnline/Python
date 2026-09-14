# Composition: an object HAS another object.
# It is usually a better idea than inheritance (session 23).
class Engine:
    def __init__(self, power: int) -> None:
        self.power = power
        self.running = False

    def start(self) -> None:
        self.running = True
        print(f'Engine of {self.power} hp started.')

    def stop(self) -> None:
        self.running = False
        print('Engine stopped.')


class Car:
    def __init__(self, brand: str, engine: Engine) -> None:
        self.brand = brand
        self.engine = engine        # the car HAS an engine

    def start(self) -> None:
        print(f'{self.brand}:')
        self.engine.start()         # the work is delegated to the engine

    def stop(self) -> None:
        self.engine.stop()


engine = Engine(150)
car = Car('Mazda', engine)

car.start()
print('running?', car.engine.running)
car.stop()
