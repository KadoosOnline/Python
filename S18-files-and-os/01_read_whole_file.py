# open() gives us a "file object". The default mode is 'r' (read).
# The path is relative to the folder the program is started from.
f = open('a.txt', encoding='utf-8')
# An absolute path works too:
# f = open('D:\\myprojects\\a.txt', encoding='utf-8')

content = f.read()      # read() returns the WHOLE file as one string
print(content)

f.close()               # the file must be closed - if we forget, data can be lost
