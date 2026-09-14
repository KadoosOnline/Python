# Mode 'x' creates the file, but raises FileExistsError when it already exists.
# It is the safe way of saying "I do not want to overwrite anything".
try:
    with open('i.txt', 'x', encoding='utf-8') as f:
        f.write('Created for the first time.\n')
    print('The file was created.')
except FileExistsError:
    print('The file already exists - nothing was touched.')
