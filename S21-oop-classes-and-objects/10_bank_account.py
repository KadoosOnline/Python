'''A class whose whole point is to protect a value that changes.'''


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance
        self.history: list[str] = []      # a NEW list for every account

    def deposit(self, amount: float) -> None:
        'Add money to the account.'
        if amount <= 0:
            print('The amount must be positive.')
            return
        self.balance += amount
        self.history.append(f'+{amount}')

    def withdraw(self, amount: float) -> bool:
        'Take money out. Return False when there is not enough.'
        if amount <= 0:
            print('The amount must be positive.')
            return False
        if amount > self.balance:
            print('Not enough money.')
            return False
        self.balance -= amount
        self.history.append(f'-{amount}')
        return True

    def show(self) -> None:
        print(f'{self.owner}: {self.balance:,.0f}')
        print('  history:', ', '.join(self.history) or '(empty)')


if __name__ == '__main__':
    account = BankAccount('Ali', 100_000)
    account.deposit(50_000)
    account.withdraw(30_000)
    account.withdraw(1_000_000)      # refused
    account.show()

    # A second account is completely independent.
    other = BankAccount('Sara')
    other.deposit(20_000)
    other.show()
