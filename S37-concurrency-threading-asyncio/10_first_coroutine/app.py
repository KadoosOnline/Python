'''asyncio: concurrency with ONE thread.

A thread is expensive: the operating system creates it, switches to it, and
each one costs memory. A thousand threads is a problem; a thousand
**coroutines** is nothing.

Three new words:

    async def       defines a COROUTINE -- a function that can pause
    await           "pause here until this is ready, and let something else
                    run in the meantime"
    asyncio.run()   starts the event loop and runs one coroutine to the end

The two rules people trip over:

1. Calling a coroutine does NOT run it.
       worker()          -> creates a coroutine object, runs nothing
       await worker()    -> runs it
   Python warns you: "coroutine 'worker' was never awaited".

2. `await` is only allowed inside an `async def`.

And the rule that decides whether asyncio helps at all:

    *** never call a BLOCKING function inside a coroutine ***

`time.sleep(1)` stops the WHOLE event loop for one second -- every other
coroutine included. The async version is `await asyncio.sleep(1)`, and the
same goes for `requests` (blocking) versus `httpx.AsyncClient` (async).
For a blocking call you cannot avoid: `await asyncio.to_thread(function, arg)`.
'''

import asyncio
import time


async def worker(name: str, seconds: float) -> str:
    '''A coroutine: it can pause at every `await`.'''
    print(f'{name}: starting')
    await asyncio.sleep(seconds)        # NOT time.sleep()
    print(f'{name}: finished after {seconds} s')
    return f'{name} is done'


async def main_async() -> None:
    # `await` one after the other = sequential. Two seconds in total.
    start = time.perf_counter()
    first = await worker('A', 1)
    second = await worker('B', 1)
    print(f'{first} / {second}')
    print(f'awaited one after the other: {time.perf_counter() - start:.2f} s')

    # What happens if you forget the await:
    coroutine = worker('C', 1)          # nothing runs here
    print(f'\nwithout await, worker() gives: {type(coroutine).__name__}')
    print(await coroutine)              # NOW it runs


def main() -> None:
    # asyncio.run creates the event loop, runs the coroutine, closes the loop.
    # Call it ONCE, at the very top of your program.
    asyncio.run(main_async())


if __name__ == '__main__':
    main()
