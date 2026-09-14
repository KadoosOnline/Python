'''Real network calls: `requests` (blocking) versus `httpx` (async).

Install what this example needs:

    pip install httpx requests

THE POINT OF THIS FILE

`requests.get()` BLOCKS. Inside a coroutine it stops the whole event loop, so
ten "concurrent" downloads written with `requests` take exactly as long as ten
sequential ones. The library you use has to be an async one:

    requests  ->  httpx.AsyncClient  (or aiohttp)
    sqlite3   ->  aiosqlite
    open()    ->  aiofiles

For a blocking call you cannot replace, hand it to a thread:

    await asyncio.to_thread(requests.get, url)

Three ways to fetch the same pages are measured below. Do not be surprised
that "async" and "threads" are about equally fast for five URLs -- the
difference appears with hundreds of them, where threads become expensive and
coroutines stay cheap.

If the classroom has no internet, run it anyway: every failure is caught and
the timings are still meaningful.
'''

import asyncio
import time

try:
    import httpx
    import requests
except ImportError:
    print('This example needs two packages:\n\n    pip install httpx requests\n')
    raise SystemExit(1)


URLS = [
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
]
TIMEOUT = 10


def fetch_blocking(url: str) -> str:
    '''The ordinary, blocking way.'''
    try:
        response = requests.get(url, timeout=TIMEOUT)
        return f'{response.status_code} ({len(response.content)} bytes)'
    except requests.RequestException as error:
        return f'failed: {type(error).__name__}'


def sequential() -> None:
    start = time.perf_counter()
    for url in URLS:
        print('   ', fetch_blocking(url))
    print(f'  -> {time.perf_counter() - start:.2f} s')


def with_threads() -> None:
    from concurrent.futures import ThreadPoolExecutor
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=len(URLS)) as pool:
        for line in pool.map(fetch_blocking, URLS):
            print('   ', line)
    print(f'  -> {time.perf_counter() - start:.2f} s')


async def fetch_async(client: httpx.AsyncClient, url: str) -> str:
    try:
        response = await client.get(url)
        return f'{response.status_code} ({len(response.content)} bytes)'
    except httpx.HTTPError as error:
        return f'failed: {type(error).__name__}'


async def with_asyncio() -> None:
    start = time.perf_counter()
    # ONE client for every request: it reuses the connections, which is the
    # main reason an async client is fast. Opening a client per request is a
    # classic and expensive mistake.
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        lines = await asyncio.gather(*(fetch_async(client, url)
                                       for url in URLS))
    for line in lines:
        print('   ', line)
    print(f'  -> {time.perf_counter() - start:.2f} s')


async def the_wrong_way() -> None:
    '''`requests` inside a coroutine: concurrent on paper, sequential in fact.'''
    start = time.perf_counter()
    for url in URLS:                    # gather would not help either:
        fetch_blocking(url)             # the loop is blocked all the same
    print(f'  -> {time.perf_counter() - start:.2f} s  (no better at all)')


async def to_thread_demo() -> None:
    '''The escape hatch: run the blocking function in a thread.'''
    start = time.perf_counter()
    lines = await asyncio.gather(*(asyncio.to_thread(fetch_blocking, url)
                                   for url in URLS))
    for line in lines:
        print('   ', line)
    print(f'  -> {time.perf_counter() - start:.2f} s')


def main() -> None:
    print(f'{len(URLS)} requests, each one taking about 1 second\n')

    print('1. requests, one after the other:')
    sequential()

    print('\n2. requests in a ThreadPoolExecutor:')
    with_threads()

    print('\n3. httpx.AsyncClient + gather:')
    asyncio.run(with_asyncio())

    print('\n4. requests INSIDE a coroutine (the mistake):')
    asyncio.run(the_wrong_way())

    print('\n5. asyncio.to_thread(requests.get, ...):')
    asyncio.run(to_thread_demo())


if __name__ == '__main__':
    main()
