# The multiplication table of the numbers 1..n
user_input = input('Enter a number: ')
n = int(user_input)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end='\t')   # \t keeps the columns aligned
    print()
