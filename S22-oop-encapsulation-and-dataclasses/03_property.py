# @property turns a METHOD into something that is READ like an attribute.
class Student:
    def __init__(self, name, score=0):
        self._name = name
        self._score = score

    @property
    def score(self):
        'Reading s.score really calls this method.'
        return self._score

    @score.setter
    def score(self, value):
        'Writing s.score = ... really calls this method.'
        if value < 0 or value > 20:
            raise ValueError('the score must be between 0 and 20')
        self._score = value

    @property
    def passed(self):
        'A computed property: there is no attribute behind it.'
        return self._score >= 10


s = Student('Ali', 18)

print(s.score)        # looks like an attribute, but calls the getter
s.score = 19.5        # calls the setter
print(s.score)
print(s.passed)       # computed on the fly

try:
    s.score = 100
except ValueError as e:
    print('Refused:', e)

# 'passed' has no setter, so it is read-only:
# s.passed = True   ->  AttributeError
