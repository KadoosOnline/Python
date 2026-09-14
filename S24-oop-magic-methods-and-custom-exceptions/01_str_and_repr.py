# Without __str__, printing an object gives something useless like
# <__main__.Human object at 0x000001C3...>
class Human:
    def __init__(self, name: str = 'Adam', lastname: str = ''):
        self.name = name
        self.lastname = lastname

    def __str__(self) -> str:
        '''Used by print() and str(): a friendly text for the USER.'''
        return f'{self.name} {self.lastname}'.strip()

    def __repr__(self) -> str:
        '''Used in the interpreter, in a list, and while debugging:
        a precise text for the DEVELOPER. Ideally it looks like the code
        needed to rebuild the object.'''
        return f'Human(name={self.name!r}, lastname={self.lastname!r})'


if __name__ == '__main__':
    h = Human('Kasra', 'Bagheri')

    print(h)             # __str__
    print(str(h))        # __str__
    print(repr(h))       # __repr__
    print([h])           # a list uses __repr__ for its items!
    print(f'{h}')        # __str__
    print(f'{h!r}')      # __repr__

    # When only __repr__ is defined, print() falls back to it.
    # So if you write only one of the two, write __repr__.
