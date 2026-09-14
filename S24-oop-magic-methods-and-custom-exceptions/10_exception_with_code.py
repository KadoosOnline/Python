# An exception is an object, so it can carry extra data - a code, a field name,
# the value that was refused...
class AppError(Exception):
    def __init__(self, message: str, code: int) -> None:
        super().__init__(message)     # let Exception store the message
        self.code = code              # our own extra data


def withdraw(balance: float, amount: float) -> float:
    if amount <= 0:
        raise AppError('The amount must be more than zero.', code=1001)
    if amount > balance:
        raise AppError('Not enough money.', code=1002)
    return balance - amount


if __name__ == '__main__':
    try:
        new_balance = withdraw(200, -1000)
        print(new_balance)
    except AppError as e:
        print(f'Error [{e.code}]: {e}')

    # The code lets the caller react differently to each situation,
    # and lets the message be translated without touching the logic.
    MESSAGES = {
        1001: 'The amount you entered is not valid.',
        1002: 'Your balance is too low.',
    }

    try:
        withdraw(100, 500)
    except AppError as e:
        print(MESSAGES.get(e.code, 'Unknown error.'))
