'''`Lock`: only one thread at a time inside the dangerous part.

    lock = threading.Lock()

    with lock:              # acquire() ... release(), even if it raises
        counter += 1        # <- the "critical section"

While one thread holds the lock, every other thread that reaches `with lock:`
WAITS. The three steps of `counter += 1` can no longer be cut in half.

Keep the critical section as SHORT as possible: everything inside it is
sequential again, so a lock around a slow operation throws the parallelism
away.

Other tools of `threading`:
    RLock   the same thread may take it several times (nested calls)
    Event   one thread waits for a signal from another (`wait()` / `set()`)
    Semaphore  at most N threads at a time (a connection pool, for example)

DEADLOCK -- the trap: two locks taken in a different order by two threads.
A waits for lock 2 while holding lock 1, B waits for lock 1 while holding
lock 2, and the program stops for ever. The cure is a rule: always take the
locks in the same order.
'''

import threading
import time


class BankAccount:
    '''A shared account. Every change to `balance` goes through the lock.'''

    def __init__(self, balance: int = 0) -> None:
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount: int) -> None:
        with self.lock:
            # Slow motion again, to prove the lock really protects us.
            new_balance = self.balance + amount
            time.sleep(0.000_01)
            self.balance = new_balance

    def withdraw(self, amount: int) -> bool:
        with self.lock:
            # "Check, then act" MUST be inside the same lock, otherwise the
            # balance can change between the `if` and the subtraction.
            if amount > self.balance:
                return False
            self.balance -= amount
            return True


def spend(account: BankAccount, rounds: int) -> None:
    for _ in range(rounds):
        account.deposit(2)
        account.withdraw(1)


def main() -> None:
    account = BankAccount()

    threads = [threading.Thread(target=spend, args=(account, 500))
               for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(f'expected balance: {10 * 500 * (2 - 1)}')
    print(f'real balance:     {account.balance}')

    # An Event: the main thread tells a worker when to stop.
    print('\nEvent demonstration:')
    stop = threading.Event()

    def blinker() -> None:
        while not stop.is_set():
            print('  ...working')
            # wait() returns as soon as the event is set: much better than
            # sleep(), which would always run to the end.
            stop.wait(timeout=0.3)
        print('  worker stopped cleanly')

    worker = threading.Thread(target=blinker)
    worker.start()
    time.sleep(1)
    stop.set()                  # ask it to stop
    worker.join()


if __name__ == '__main__':
    main()
