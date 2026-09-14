# Looping directly over the file gives its lines one by one.
# This is the best way: it never loads the whole file into memory.
with open('numbers.txt', encoding='utf-8') as file:
    for line in file:
        print(line, end='')

print()

# readlines() puts every line into a list (only for small files).
with open('numbers.txt', encoding='utf-8') as file:
    lines = file.readlines()

print(lines)
print('number of lines:', len(lines))
