'''`ThreadPoolExecutor`: the modern, short way to do everything above.

`concurrent.futures` gives you a pool of ready threads and takes care of
starting, joining and collecting the results:

    with ThreadPoolExecutor(max_workers=5) as pool:
        results = pool.map(function, items)          # in order, like map()

    with ThreadPoolExecutor() as pool:
        future = pool.submit(function, arg)          # one job
        value = future.result()                      # its answer (or its error)

The `with` block waits for every job before it ends -- no `join()` loop.

`map` vs `submit`:
    map      one function over a list, results IN ORDER, exceptions raised
             when you read the result
    submit   returns a `Future` for each job; with `as_completed` you get the
             answers as soon as they arrive, in whatever order

Very important: an exception inside a worker does NOT crash the program and
does NOT print anything. It is stored in the `Future` and re-raised when you
call `.result()`. A `submit()` whose result is never read is an error you will
never see.
'''

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


SITES = {'kadoos.ir': 0.5, 'python.org': 1.2, 'sqlite.org': 0.3,
         'qt.io': 0.8, 'flask.dev': 0.6}


def fetch(site: str) -> int:
    '''Pretend to download a page and return its size.'''
    if site == 'flask.dev':
        raise ConnectionError('the site does not answer')
    time.sleep(SITES[site])
    return len(site) * 1000


def main() -> None:
    start = time.perf_counter()

    # -- map: simple, ordered, and it stops at the first exception ---------
    print('with map():')
    with ThreadPoolExecutor(max_workers=4) as pool:
        good_sites = [site for site in SITES if site != 'flask.dev']
        for site, size in zip(good_sites, pool.map(fetch, good_sites)):
            print(f'  {site}: {size} bytes')

    # -- submit + as_completed: answers as soon as they are ready ----------
    print('\nwith submit() and as_completed():')
    with ThreadPoolExecutor(max_workers=4) as pool:
        # A dict Future -> site, to know which job an answer belongs to.
        futures = {pool.submit(fetch, site): site for site in SITES}

        for future in as_completed(futures):
            site = futures[future]
            try:
                size = future.result()      # re-raises the worker's exception
            except ConnectionError as error:
                print(f'  {site}: FAILED ({error})')
            else:
                print(f'  {site}: {size} bytes')

    # Both blocks visit every site once; flask.dev raises at once and costs
    # no time, so the sequential cost of the two blocks is twice this sum.
    sequential = 2 * sum(seconds for site, seconds in SITES.items()
                         if site != 'flask.dev')
    print(f'\ntotal: {time.perf_counter() - start:.2f} seconds '
          f'(one after the other it would be {sequential:.1f})')


if __name__ == '__main__':
    main()
