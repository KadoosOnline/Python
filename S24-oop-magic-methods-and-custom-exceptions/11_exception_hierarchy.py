'''A real application defines a FAMILY of exceptions.

    ShopError                <- the base: catch this to catch everything
      +-- ProductError
      |     +-- ProductNotFound
      |     +-- OutOfStock
      +-- PaymentError
            +-- NotEnoughMoney
'''


class ShopError(Exception):
    'Base class of every error of the shop.'


class ProductError(ShopError):
    'Something is wrong with a product.'


class ProductNotFound(ProductError):
    def __init__(self, name: str) -> None:
        super().__init__(f'The product {name!r} does not exist.')
        self.name = name


class OutOfStock(ProductError):
    def __init__(self, name: str, available: int) -> None:
        super().__init__(f'Only {available} left of {name!r}.')
        self.name = name
        self.available = available


class PaymentError(ShopError):
    'Something is wrong with the payment.'


class NotEnoughMoney(PaymentError):
    def __init__(self, missing: float) -> None:
        super().__init__(f'You need {missing:,.0f} more.')
        self.missing = missing


STOCK = {'Notebook': 3, 'Pencil': 0}
PRICES = {'Notebook': 15_000, 'Pencil': 5_000}


def buy(name: str, quantity: int, wallet: float) -> float:
    if name not in STOCK:
        raise ProductNotFound(name)

    if STOCK[name] < quantity:
        raise OutOfStock(name, STOCK[name])

    total = PRICES[name] * quantity
    if total > wallet:
        raise NotEnoughMoney(total - wallet)

    return wallet - total


def main() -> None:
    orders = [
        ('Notebook', 2, 100_000),
        ('Eraser', 1, 100_000),
        ('Pencil', 1, 100_000),
        ('Notebook', 3, 10_000),
    ]

    for name, quantity, wallet in orders:
        try:
            rest = buy(name, quantity, wallet)
        except ProductError as e:
            # One handler for every product problem.
            print(f'[product] {e}')
        except PaymentError as e:
            print(f'[payment] {e} (missing {e.missing:,.0f})')
        except ShopError as e:
            # The safety net for anything new added later.
            print(f'[shop] {e}')
        else:
            print(f'Bought {quantity} x {name}, {rest:,.0f} left.')


if __name__ == '__main__':
    main()
