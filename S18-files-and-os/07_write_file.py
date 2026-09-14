# Mode 'w' creates the file, and ERASES it completely when it already exists.
with open('h.txt', 'w', encoding='utf-8') as f:
    f.write('It deletes the existing file!\n')
    f.write('Second line.\n')          # write() does NOT add '\n' by itself

# writelines() writes a list of strings (still without adding '\n').
lines = ['Ali\n', 'Sara\n', 'Reza\n']
with open('names.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)

with open('h.txt', encoding='utf-8') as f:
    print(f.read())

with open('names.txt', encoding='utf-8') as f:
    print(f.read())
