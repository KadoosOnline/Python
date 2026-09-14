# A list holds several values in one variable, in a fixed order,
# written between square brackets and separated by commas.
animals = ['Cat', 'Lion', 'Dog', 'Wolf']
numbers = [5, 7, 15, 32, 104, 1]
empty = []                         # a list with nothing in it

print(animals)
print(numbers)
print(empty)

print(animals[0])                  # the first item
print(type(animals))               # <class 'list'>
print(len(animals))                # how many items -> 4

# A list may even mix different types (rarely a good idea, but it is allowed).
mixed = ['Ali', 20, 19.5, True]
print(mixed)
