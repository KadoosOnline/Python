# 'with' closes the file automatically, even if an error happens inside.
# This is the only form you should use.
with open('a.txt', encoding='utf-8') as f:
    content = f.read()
    print(content)

# Here the file is already closed.
print('closed?', f.closed)
