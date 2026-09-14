'''`asyncio.gather`: running coroutines at the same time.

`await one(); await two()` is sequential -- the second starts when the first
is finished. To run them TOGETHER:

    results = await asyncio.gather(one(), two(), three())

`gather` returns the results as a list, **in the order you passed them in**,
not in the order they finished.

Errors: by default the first exception is raised at once (the others keep
running in the background). With `return_exceptions=True` you get the
exception objects inside the result list instead, which is what you want when
one failing download must not lose the four that worked.

Modern alternative (Python 3.11+): `asyncio.TaskGroup`, which cancels the
other tasks when one of them fails -- usually what you want in a server.
'''

import asyncio
import time


async def fetch(site: str, seconds: float) -> int:
    print(f'  start  {site}')
    await asyncio.sleep(seconds)
    if site == 'broken.ir':
        raise ConnectionError(f'{site} does not answer')
    print(f'  finish {site}')
    return len(site) * 1000


async def main_async() -> None:
    sites = [('kadoos.ir', 1.0), ('python.org', 0.4),
             ('sqlite.org', 0.7), ('qt.io', 0.2)]

    print('sequential:')
    start = time.perf_counter()
    for site, seconds in sites:
        await fetch(site, seconds)
    print(f'-> {time.perf_counter() - start:.2f} s\n')

    print('with gather:')
    start = time.perf_counter()
    sizes = await asyncio.gather(*(fetch(site, seconds)
                                   for site, seconds in sites))
    print(f'-> {time.perf_counter() - start:.2f} s')
    print(f'   results in the ORDER OF THE ARGUMENTS: {sizes}\n')

    print('with a failure and return_exceptions=True:')
    results = await asyncio.gather(
        fetch('kadoos.ir', 0.3),
        fetch('broken.ir', 0.1),
        fetch('qt.io', 0.2),
        return_exceptions=True,
    )
    for result in results:
        if isinstance(result, Exception):
            print(f'   FAILED: {result}')
        else:
            print(f'   ok: {result} bytes')


def main() -> None:
    asyncio.run(main_async())


if __name__ == '__main__':
    main()
