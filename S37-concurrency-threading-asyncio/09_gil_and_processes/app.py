'''The GIL, and what to do about it: processes.

THE GIL (Global Interpreter Lock) is a lock inside CPython itself: **only one
thread executes Python bytecode at a time**. So:

    waiting work (network, disk, database)  -> threads help a lot:
        the GIL is released while a thread waits
    calculating work (loops, maths)         -> threads help NOTHING:
        the threads take turns instead of running together

Run this program: the threaded version of a pure calculation is as slow as the
sequential one -- sometimes slower, because of the cost of switching.

The answer for calculation is `ProcessPoolExecutor`: several real operating
system PROCESSES, each with its own interpreter and its own GIL, on several
cores.

The price of a process:
* arguments and results are `pickle`d and copied, so passing big objects is
  expensive -- and a lambda or a local function cannot be pickled at all;
* there are no shared variables any more (that is also the good news: no race
  conditions);
* on Windows every process re-imports your module, which is why
  `if __name__ == '__main__':` is not optional here. Without it the program
  starts itself again and again for ever.

(Free-threaded builds of Python 3.13+ can run without the GIL. Until that is
the normal case everywhere, the rule above is what you plan with.)
'''

import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def count_primes(limit: int) -> int:
    '''Pure calculation, no waiting at all: the GIL's worst case.'''
    total = 0
    for number in range(2, limit):
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                break
        else:
            total += 1
    return total


JOBS = [300_000, 300_000, 300_000, 300_000]


def measure(label: str, function) -> float:
    start = time.perf_counter()
    results = function()
    duration = time.perf_counter() - start
    print(f'{label:<22} {duration:5.2f} s   {results}')
    return duration


def main() -> None:
    print('counting the primes below 300000, four times\n')

    sequential = measure('one after the other',
                         lambda: [count_primes(job) for job in JOBS])

    def with_threads():
        with ThreadPoolExecutor(max_workers=4) as pool:
            return list(pool.map(count_primes, JOBS))

    threaded = measure('4 threads', with_threads)

    def with_processes():
        with ProcessPoolExecutor(max_workers=4) as pool:
            return list(pool.map(count_primes, JOBS))

    processed = measure('4 processes', with_processes)

    print(f'\nthreads:   {sequential / threaded:.2f} times faster '
          f'(about 1.0 -- the GIL)')
    print(f'processes: {sequential / processed:.2f} times faster '
          f'(depends on the number of cores)')


# Mandatory for ProcessPoolExecutor: without it Windows starts the program
# again in every child process.
if __name__ == '__main__':
    main()
