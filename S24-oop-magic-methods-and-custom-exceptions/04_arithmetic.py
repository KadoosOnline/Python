# Operator overloading: giving a meaning to +, - and * for our own class.
class Money:
    def __init__(self, amount: float, currency: str = 'Toman') -> None:
        self.amount = amount
        self.currency = currency

    def __str__(self) -> str:
        return f'{self.amount:,.0f} {self.currency}'

    def __repr__(self) -> str:
        return f'Money({self.amount}, {self.currency!r})'

    def __add__(self, other: 'Money') -> 'Money':
        '''Called by  a + b.
        IMPORTANT: it must RETURN a value, not print one.'''
        if not isinstance(other, Money) or other.currency != self.currency:
            return NotImplemented
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other: 'Money') -> 'Money':
        if not isinstance(other, Money) or other.currency != self.currency:
            return NotImplemented
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, factor: float) -> 'Money':
        'Called by  money * 3'
        return Money(self.amount * factor, self.currency)

    def __rmul__(self, factor: float) -> 'Money':
        'Called by  3 * money  (the "reflected" version)'
        return self * factor

    def __neg__(self) -> 'Money':
        'Called by  -money'
        return Money(-self.amount, self.currency)


if __name__ == '__main__':
    price = Money(15_000)
    tax = Money(1_350)

    print(price + tax)
    print(price - tax)
    print(price * 3)
    print(3 * price)         # works thanks to __rmul__
    print(-price)

    # A different currency is refused by Python itself:
    try:
        print(price + Money(10, 'Euro'))
    except TypeError as e:
        print('Refused:', e)
