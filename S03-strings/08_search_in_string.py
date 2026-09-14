text = 'Kadoos Institute, Rasht'

# 'in' answers: does this piece exist inside the text?
print('Rasht' in text)          # True
print('Tehran' in text)         # False

# find() gives the index of the first occurrence, or -1 when it is not found.
print(text.find('Institute'))   # 7
print(text.find('Tehran'))      # -1

# count() says how many times a piece appears.
print(text.count('a'))

# startswith() / endswith() are used a lot when checking file names.
print(text.startswith('Kadoos'))   # True
print('app.py'.endswith('.py'))    # True
