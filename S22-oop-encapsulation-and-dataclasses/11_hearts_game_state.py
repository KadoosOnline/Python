'''The "lives" of a game, written as a proper class.

It puts together: validation with @property, a class constant,
a @classmethod constructor and saving/loading.
'''

import os


class Hearts:
    MAX = 9                                  # class constant
    SAVE_FILE = 'save.txt'

    def __init__(self, value: int = 5) -> None:
        self.value = value                   # goes through the setter

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, new_value: int) -> None:
        if not isinstance(new_value, int):
            raise TypeError('the number of hearts must be a whole number')
        # Keep the value inside 0 .. MAX instead of raising: a game should not
        # crash because the player lost one life too many.
        self._value = max(0, min(new_value, self.MAX))

    @property
    def is_alive(self) -> bool:
        return self._value > 0

    def add(self, amount: int = 1) -> None:
        self.value = self._value + amount

    def remove(self, amount: int = 1) -> None:
        self.value = self._value - amount

    def reset(self) -> None:
        self.value = 5

    def save(self) -> None:
        'Write the current number of hearts into a file.'
        with open(self.SAVE_FILE, 'w', encoding='utf-8') as f:
            f.write(str(self._value))

    @classmethod
    def load(cls) -> 'Hearts':
        'Build a Hearts object from the save file (or a new one).'
        if not os.path.exists(cls.SAVE_FILE):
            return cls()

        try:
            with open(cls.SAVE_FILE, encoding='utf-8') as f:
                return cls(int(f.read().strip()))
        except ValueError:
            print('[warning] the save file is damaged, starting a new game')
            return cls()

    def __str__(self) -> str:
        return 'Hearts: ' + '*' * self._value


def main() -> None:
    hearts = Hearts.load()
    print(hearts)

    hearts.remove(2)
    print(hearts, '| alive?', hearts.is_alive)

    hearts.add(5)
    print(hearts, '(never goes above', Hearts.MAX, ')')

    hearts.remove(100)
    print(hearts, '| alive?', hearts.is_alive)

    hearts.reset()
    hearts.save()
    print('Saved:', hearts)


if __name__ == '__main__':
    main()
