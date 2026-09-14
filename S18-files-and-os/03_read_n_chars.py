# read(n) reads at most n characters instead of the whole file.
with open('a.txt', encoding='utf-8') as f:
    print(f.read(5))     # 'Hello'
    print(f.read(3))     # the reading continues where it stopped
