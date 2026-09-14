'''A temperature that can be read in Celsius and in Fahrenheit.'''


class Temperature:
    def __init__(self, celsius: float = 0.0) -> None:
        self.celsius = celsius        # goes through the setter, so it is checked

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError('below the absolute zero!')
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        'Computed from the Celsius value - nothing is stored.'
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        'Writing Fahrenheit updates the Celsius value.'
        self.celsius = (value - 32) * 5 / 9


t = Temperature(25)
print(t.celsius, t.fahrenheit)

t.fahrenheit = 212
print(t.celsius)          # 100.0

try:
    t.celsius = -300
except ValueError as e:
    print('Refused:', e)
