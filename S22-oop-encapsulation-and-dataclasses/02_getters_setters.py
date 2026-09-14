# The classic solution (the one used in Java or C#): hide the attribute behind
# two methods.
class Student:
    def __init__(self, name, score=0):
        self._name = name        # a single underscore means "do not touch"
        self._score = 0
        self.set_score(score)    # reuse the validation of the setter

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('the score must be a number')
        if value < 0 or value > 20:
            raise ValueError('the score must be between 0 and 20')
        self._score = value


s = Student('Ali', 18)
print(s.get_score())

s.set_score(19.5)
print(s.get_score())

try:
    s.set_score(5000)
except ValueError as e:
    print('Refused:', e)

# It works, but every read becomes s.get_score() instead of s.score.
# Python has something better - see the next file.
