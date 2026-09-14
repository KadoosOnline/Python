'''When do threads actually make a program faster?

Answer: when the program WAITS. Downloading a file, reading a disk, querying
a database, calling a web API -- during all of that the processor does
nothing, and another thread can use the time.

Here `fake_download` is `time.sleep`, which is exactly the same kind of
waiting. Four downloads of one second each:

    one after the other -> about 4 seconds
    four threads        -> about 1 second

For pure CALCULATION (adding numbers in a loop) threads bring nothing at all
in Python -- that is the GIL, and it is example 09.

`time.perf_counter()` is the right clock for measuring a duration: it only
goes forward and it has a high resolution.
'''

import threading
import time


SITES = ['kadoos.ir', 'python.org', 'sqlite.org', 'qt.io']


def fake_download(site: str, seconds: float = 1.0) -> None:
    '''Pretend to download a page. `sleep` = waiting for the network.'''
    time.sleep(seconds)
    print(f'  downloaded {site}')


def sequential() -> float:
    start = time.perf_counter()
    for site in SITES:
        fake_download(site)
    return time.perf_counter() - start


def threaded() -> float:
    start = time.perf_counter()
    threads = [threading.Thread(target=fake_download, args=(site,))
               for site in SITES]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return time.perf_counter() - start


def main() -> None:
    print(f'one after the other ({len(SITES)} sites):')
    slow = sequential()
    print(f'  -> {slow:.2f} seconds\n')

    print(f'with {len(SITES)} threads:')
    fast = threaded()
    print(f'  -> {fast:.2f} seconds\n')

    print(f'{slow / fast:.1f} times faster')


if __name__ == '__main__':
    main()
