# Mode 'a' adds to the END of the file and never erases anything.
# Run this program several times and watch the file grow.
with open('g.txt', 'a', encoding='utf-8') as f:
    f.write('This is a text file!\n')

with open('g.txt', encoding='utf-8') as f:
    print(f.read())
