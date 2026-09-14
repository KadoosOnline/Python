'''`asyncio.Queue`: the producer / consumer pattern, without a single lock.

The same idea as example 06, but with coroutines instead of threads -- and
because everything runs in one thread, there is no race condition to protect
against at all.

    queue.put(item)      -> `await queue.put(...)`  (waits if the queue is full)
    queue.get()          -> `await queue.get()`     (waits if it is empty)
    queue.task_done()    -> the same as in `queue.Queue`
    await queue.join()   -> waits until every item has been handled

`maxsize` gives you BACK-PRESSURE: when the consumers fall behind, the queue
fills up and `put` starts waiting, so the producer slows down instead of
eating all the memory. That is the whole trick behind a healthy pipeline.

Ending the consumers: they loop for ever, so after `queue.join()` we cancel
them. That is the normal, correct way -- not a bug.
'''

import asyncio
import random


async def producer(queue: asyncio.Queue, count: int) -> None:
    '''Puts `count` jobs into the queue.'''
    for number in range(1, count + 1):
        await asyncio.sleep(random.uniform(0.05, 0.15))
        await queue.put(number)
        print(f'produced  {number:>2}   (queue: {queue.qsize()})')
    print('the producer has finished')


async def consumer(name: str, queue: asyncio.Queue) -> None:
    '''Takes jobs for ever, until it is cancelled.'''
    while True:
        number = await queue.get()
        try:
            await asyncio.sleep(random.uniform(0.1, 0.3))
            print(f'  {name} handled {number:>2} -> {number ** 2}')
        finally:
            # In a `finally`, so a failure cannot make join() wait for ever.
            queue.task_done()


async def main_async() -> None:
    # maxsize=3: the producer has to wait when the consumers fall behind.
    queue: asyncio.Queue = asyncio.Queue(maxsize=3)

    consumers = [asyncio.create_task(consumer(f'consumer-{index}', queue))
                 for index in range(2)]

    await producer(queue, 10)
    await queue.join()              # every job has had its task_done()

    # The consumers wait for ever on `queue.get()`: cancel them.
    for task in consumers:
        task.cancel()
    # gather with return_exceptions=True collects the CancelledErrors quietly.
    await asyncio.gather(*consumers, return_exceptions=True)
    print('everything is finished')


def main() -> None:
    asyncio.run(main_async())


if __name__ == '__main__':
    main()
