# Building a small table with a loop. The \t escape keeps the columns aligned.
print('n\tn^2\tn^3')

for n in range(1, 11):
    print(f'{n}\t{n ** 2}\t{n ** 3}')
