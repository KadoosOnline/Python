'''The race condition: the bug that only appears sometimes.

Ten threads each add 1 to the same counter a thousand times, so the answer
must be 10 000. Run it: you will get 10 000 almost never.

Why? `counter += 1` is not one single step. The processor does:

    1. READ  the value of counter
    2. ADD   one to the value it read
    3. WRITE the result back

If thread A is interrupted between step 1 and step 3, thread B reads the SAME
old value, and both write back the same number: one increment is lost.

`counter = temp + 1` with a tiny sleep in the middle just makes the window
wide enough to see it every time. The bug is there without the sleep too --
it simply appears once every few thousand runs, on the customer's machine, on
a Friday evening. That is what makes it dangerous.

The rule: **the moment two threads write to the same variable, you need a
lock** (example 05).
'''

import threading
import time


counter = 0                 # shared between every thread


def worker(rounds: int) -> None:
    global counter
    for _ in range(rounds):
        # This is `counter += 1` written out in slow motion.
        temp = counter          # 1. read
        time.sleep(0.000_01)    # <- the interruption, made visible
        temp += 1               # 2. add
        counter = temp          # 3. write


def main() -> None:
    threads = [threading.Thread(target=worker, args=(1000,))
               for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(f'expected: 10000')
    print(f'obtained: {counter}')
    print(f'lost:     {10000 - counter} increments')


if __name__ == '__main__':
    main()
