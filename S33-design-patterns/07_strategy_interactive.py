'''STRATEGY, chosen at run time.

This is where the pattern really pays off: the DECISION (which strategy) and
the BEHAVIOUR (what the strategy does) are separated.
'''

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        ...


class NoDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price


class TenPercentDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price * 0.9


class TwentyPercentDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price * 0.8


class ShoppingCart:
    def __init__(self, discount_strategy: DiscountStrategy) -> None:
        self.discount_strategy = discount_strategy

    def checkout(self, price: float) -> float:
        return self.discount_strategy.apply(price)


def choose_strategy(price: float) -> DiscountStrategy:
    'The business rule lives here, and ONLY here.'
    if price >= 10_000_000:
        return TwentyPercentDiscount()
    if price >= 5_000_000:
        return TenPercentDiscount()
    return NoDiscount()


def read_price() -> float:
    'Ask until the answer is a number.'
    while True:
        try:
            return float(input('Enter the price: '))
        except ValueError:
            print('That is not a number.')


def main() -> None:
    price = read_price()

    cart = ShoppingCart(choose_strategy(price))

    print(f'Strategy: {type(cart.discount_strategy).__name__}')
    print(f'To pay:   {cart.checkout(price):,.0f}')


if __name__ == '__main__':
    main()
