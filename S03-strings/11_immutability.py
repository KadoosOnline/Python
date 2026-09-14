# Strings are IMMUTABLE: once created, a string can never be changed.
name = 'kadoos'

# This line would raise a TypeError:
# name[0] = 'K'

# Instead we build a NEW string and store it back in the variable.
name = 'K' + name[1:]
print(name)          # Kadoos

# The same idea with a method: capitalize() returns a new string,
# it does not modify the original one.
city = 'rasht'
print(city.capitalize())   # Rasht
print(city)                # rasht  -> unchanged!
