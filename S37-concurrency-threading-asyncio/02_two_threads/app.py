'''Two threads at once -- and why the output order changes every run.

`args=` passes the arguments of the target function, and it must be a TUPLE:
`args=('A',)` with the comma. `args=('A')` is just the string 'A' and Python
would try to call `worker('A'[0], 'A'[1], ...)`.
Use `kwargs={'name': 'A'}` for keyword arguments.

Run this program three times. The lines will not come out in the same order,
because it is the OPERATING SYSTEM that decides which thread advances and
when. Never write code that depends on that order.
'''

import threading
import time


def worker(name: str, steps: int) -> None:
    for step in range(steps):
        print(f'{name}{step}', end=' ', flush=True)
        # A tiny sleep gives the other thread a chance to run.
        time.sleep(0.01)


def main() -> None:
    threads = [
        threading.Thread(target=worker, args=('A', 5)),   # note the comma
        threading.Thread(target=worker, args=('B', 5)),
        threading.Thread(target=worker, kwargs={'name': 'C', 'steps': 5}),
    ]

    for thread in threads:
        thread.start()

    # Start them ALL first, then wait for them all. Starting and joining one
    # by one in the same loop would run them one after the other -- a very
    # common mistake that quietly removes all the parallelism.
    for thread in threads:
        thread.join()

    print('\nfinished')


if __name__ == '__main__':
    main()
