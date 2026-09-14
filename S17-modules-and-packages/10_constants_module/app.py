'''A small shop that reads every setting from constants.py.'''

import constants


def show_products() -> None:
    'Print the price list.'
    for name, price in constants.PRODUCTS.items():
        print(f'{name:<10}{price:>10,} {constants.CURRENCY}')


def price_with_vat(price: float) -> float:
    'Return the price including VAT.'
    return price * (1 + constants.VAT_RATE)


def main() -> None:
    print(constants.WELCOME_MESSAGE.format(app=constants.APP_NAME))
    show_products()

    product = input('Which product do you want? ')

    if product in constants.PRODUCTS:
        total = price_with_vat(constants.PRODUCTS[product])
        print(f'With VAT: {total:,.0f} {constants.CURRENCY}')
    else:
        print('We do not sell that.')

    print(constants.GOODBYE_MESSAGE)


if __name__ == '__main__':
    main()
