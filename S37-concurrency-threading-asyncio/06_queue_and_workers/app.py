'''`queue.Queue`: the right way to give work to threads and get answers back.

A `Queue` is a list that is ALREADY thread-safe: `put()` and `get()` take the
lock for you. That is why the pattern below needs no `Lock` at all -- and why
"share data through a queue instead of through variables" is the first advice
you will get from any experienced programmer.

The pattern:

    tasks = queue.Queue()          # main thread -> workers
    results = queue.Queue()        # workers -> main thread

    q.get()      takes one item, and BLOCKS while the queue is empty
    q.task_done()  says "this item is handled"
    q.join()     waits until every item has had its task_done()

`daemon=True` marks a thread as "not important": Python does not wait for a
daemon thread when the program ends. Perfect for workers that loop for ever;
dangerous for a thread that writes a file, because it can be cut in the
middle.
'''

import queue
import threading
import time


def worker(tasks: queue.Queue, results: queue.Queue) -> None:
    '''Take numbers from the queue until the sentinel arrives.'''
    name = threading.current_thread().name
    while True:
        number = tasks.get()
        try:
            if number is None:          # the sentinel: "no more work"
                return
            time.sleep(0.2)             # pretend the job takes time
            results.put((name, number, number * number))
        finally:
            # In a `finally`, so an exception cannot make queue.join() hang
            # for ever waiting for a task_done() that never comes.
            tasks.task_done()


def main() -> None:
    tasks: queue.Queue = queue.Queue()
    results: queue.Queue = queue.Queue()

    workers = [threading.Thread(target=worker, args=(tasks, results),
                                name=f'worker-{index}', daemon=True)
               for index in range(3)]
    for thread in workers:
        thread.start()

    for number in range(1, 11):
        tasks.put(number)

    # One sentinel per worker, so each of them sees exactly one.
    for _ in workers:
        tasks.put(None)

    tasks.join()                    # wait until everything is handled
    for thread in workers:
        thread.join()

    # Empty the result queue into a normal list.
    collected = []
    while not results.empty():
        collected.append(results.get())

    for name, number, square in sorted(collected, key=lambda row: row[1]):
        print(f'{name}: {number}^2 = {square}')
    print(f'{len(collected)} results, computed by {len(workers)} workers')


if __name__ == '__main__':
    main()
