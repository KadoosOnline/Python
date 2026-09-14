'''The first thread.

Until now every program of this course did ONE thing at a time: line 2 waited
for line 1. A **thread** is a second line of execution inside the same
program, so two pieces of code can advance at the same time.

    thread = threading.Thread(target=function, args=(...))
    thread.start()     # start it -- returns immediately
    thread.join()      # wait here until the thread has finished

Three rules to remember from the very first day:

* `start()` runs the function in the new thread.
  Calling `thread.run()` by mistake runs it in the CURRENT thread -- no
  parallelism at all, and nothing tells you.
* `join()` does not stop or kill anything: it just WAITS.
* Threads inside one program share the same variables (see example 04) --
  that is their strength and their danger.
'''

import threading
import time


def worker() -> None:
    '''This function will run in a thread of its own.'''
    # current_thread().name is 'Thread-1', 'MainThread'...  very useful to see
    # who is doing what.
    name = threading.current_thread().name
    for step in range(3):
        print(f'[{name}] step {step}')
        time.sleep(1)
    print(f'[{name}] finished')


def main() -> None:
    print(f'[{threading.current_thread().name}] creating the thread')

    thread = threading.Thread(target=worker, name='worker')
    thread.start()                 # start() -- never run()

    # The main thread is free while the worker sleeps.
    print('[MainThread] the thread is running; I am not blocked')
    print(f'[MainThread] is it alive? {thread.is_alive()}')

    thread.join()                  # wait for it
    print(f'[MainThread] is it alive now? {thread.is_alive()}')
    print('[MainThread] done')


if __name__ == '__main__':
    main()
