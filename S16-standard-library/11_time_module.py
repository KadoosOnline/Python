import time

print('Start')
time.sleep(1)          # pause the program for one second
print('One second later')

# Measuring how long a piece of code takes.
start = time.time()

total = 0
for i in range(3_000_000):
    total += i

end = time.time()
print(f'The loop took {end - start:.3f} seconds.')

# perf_counter() is more precise for measuring short durations.
start = time.perf_counter()
sum(range(3_000_000))
print(f'sum() took {time.perf_counter() - start:.3f} seconds.')
