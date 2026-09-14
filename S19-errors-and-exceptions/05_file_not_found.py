# Opening a file that does not exist raises FileNotFoundError.
try:
    with open('myfile.txt', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('File not found.')
except PermissionError:
    print('You are not allowed to read this file.')
