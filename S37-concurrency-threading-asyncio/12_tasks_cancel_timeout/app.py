'''Tasks: starting a coroutine in the background, cancelling it, timing it out.

    task = asyncio.create_task(coroutine())   # starts NOW, in the background
    ...                                       # your code keeps running
    result = await task                       # collect the answer

`create_task` is what you use when you do not want to wait immediately.
Two warnings:

* Keep a reference to the task. The event loop only keeps a WEAK reference, so
  a task nobody holds can be garbage-collected in the middle of its work.
* An exception inside a task you never `await` is not printed until the task
  is destroyed, and then only as a warning. Always await your tasks.

Cancelling: `task.cancel()` makes the `await` inside the coroutine raise
`asyncio.CancelledError`. Catch it to clean up -- then **re-raise it**.
Swallowing `CancelledError` means the task refuses to be cancelled, and that
is how a program stops answering Ctrl-C.

Timeout: `asyncio.timeout()` (3.11+) or `asyncio.wait_for()` cancel the
coroutine for you and raise `TimeoutError`.
'''

import asyncio


async def long_job(name: str, seconds: float) -> str:
    '''A job that cleans up properly when it is cancelled.'''
    try:
        for second in range(int(seconds)):
            print(f'  {name}: working ({second + 1}/{int(seconds)})')
            await asyncio.sleep(1)
        return f'{name} finished'
    except asyncio.CancelledError:
        print(f'  {name}: cancelled -- closing the file, the socket...')
        raise            # ALWAYS re-raise: the caller must know


async def main_async() -> None:
    # -- create_task: the work starts, we do something else meanwhile -------
    print('create_task:')
    task = asyncio.create_task(long_job('background', 3))
    print('  the main coroutine is free')
    await asyncio.sleep(1)
    print(f'  is it done? {task.done()}')
    print(f'  result: {await task}\n')

    # -- cancelling --------------------------------------------------------
    print('cancel:')
    task = asyncio.create_task(long_job('endless', 10))
    await asyncio.sleep(2.5)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print('  the caller sees CancelledError\n')

    # -- timeout (Python 3.11+) --------------------------------------------
    print('timeout:')
    try:
        async with asyncio.timeout(2):
            await long_job('slow', 10)
    except TimeoutError:
        print('  too slow: the job was cancelled for us\n')

    # -- the older form, which still works everywhere ----------------------
    print('wait_for (the older form):')
    try:
        await asyncio.wait_for(long_job('slow again', 10), timeout=2)
    except asyncio.TimeoutError:      # the same class as TimeoutError in 3.11+
        print('  too slow, again')


def main() -> None:
    asyncio.run(main_async())


if __name__ == '__main__':
    main()
