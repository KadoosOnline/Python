# readline() reads ONE line, including the '\n' at its end.
with open('a.txt', encoding='utf-8') as f:
    print(f.readline())
    print(f.readline())

# That is why the output looks double spaced: the line already ends with '\n'
# and print() adds another one. end='' fixes it.
print('--- without the extra blank line ---')
with open('a.txt', encoding='utf-8') as f:
    print(f.readline(), end='')
    print(f.readline(), end='')
