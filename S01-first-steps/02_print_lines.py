# Every print() call writes one line, so these five calls draw a triangle.
print('*')
print('**')
print('***')
print('****')
print('*****')

# print() with no argument writes an empty line.
print()

# A single print() can take several values; they are separated by a space.
print('Kadoos', 'Institute', 'Rasht')

# 'sep' changes the separator and 'end' changes what is printed at the end.
print('2026', '09', '08', sep='-')
print('No new line here ->', end=' ')
print('...the next print continues on the same line.')
