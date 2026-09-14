'''All the settings of the program in one place.

Constants are written in CAPITALS. Keeping them in their own module means that
changing a message or a limit never requires touching the logic of the program.
'''

APP_NAME: str = 'Kadoos Shop'
CURRENCY: str = 'Toman'

VAT_RATE: float = 0.09
MAX_ITEMS: int = 10

WELCOME_MESSAGE: str = 'Welcome to {app}!'
GOODBYE_MESSAGE: str = 'Thank you, see you soon.'

PRODUCTS: dict[str, int] = {
    'Notebook': 15_000,
    'Pencil': 5_000,
    'Eraser': 3_000,
}
