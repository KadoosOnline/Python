# Nothing stops the outside world from writing nonsense into an attribute.
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


s = Student('Ali', 18)
print(s.score)

s.score = 5000          # a score of 5000 out of 20?
s.score = -3            # a negative score?
s.score = 'excellent'   # not even a number!
print(s.score)

# The object no longer guarantees anything about its own data.
# Encapsulation means: the class - and only the class - decides what a valid
# value is.
