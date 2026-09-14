'''STRATEGY - behavioural pattern.

Problem:  several interchangeable algorithms (ways of computing a discount, of
          sorting, of paying), and a long if/elif that grows at every new one.
Solution: one class per algorithm, all with the same interface; the client
          receives the one it must use.
'''

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    'The common interface of every discount.'

    @abstractmethod
    def apply(self, price: float) -> float:
        ...


class NoDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price


class TenPercentDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price * 0.9


class FixedDiscount(DiscountStrategy):
    'Adding a new strategy changes NO existing class.'

    def __init__(self, amount: float) -> None:
        self.amount = amount

    def apply(self, price: float) -> float:
        return max(0.0, price - self.amount)


class ShoppingCart:
    'The client. It does not know which discount it is using.'

    def __init__(self, discount_strategy: DiscountStrategy) -> None:
        self.discount_strategy = discount_strategy

    def checkout(self, price: float) -> float:
        return self.discount_strategy.apply(price)


def main() -> None:
    print(ShoppingCart(NoDiscount()).checkout(1000))          # 1000
    print(ShoppingCart(TenPercentDiscount()).checkout(1000))  # 900.0
    print(ShoppingCart(FixedDiscount(250)).checkout(1000))    # 750.0

    # The strategy can even be changed while the program runs.
    cart = ShoppingCart(NoDiscount())
    print(cart.checkout(1000))
    cart.discount_strategy = TenPercentDiscount()
    print(cart.checkout(1000))


if __name__ == '__main__':
    main()
