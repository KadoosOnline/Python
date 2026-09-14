# Text files store bytes; the ENCODING says how those bytes become characters.
# Without encoding='utf-8', Persian text can be unreadable on Windows.
persian = 'سلام، به موسسه کادوس خوش آمدید'

with open('persian.txt', 'w', encoding='utf-8') as f:
    f.write(persian + '\n')

with open('persian.txt', encoding='utf-8') as f:
    print(f.read())

# Always pass encoding='utf-8' when you open a text file, for reading
# and for writing.
