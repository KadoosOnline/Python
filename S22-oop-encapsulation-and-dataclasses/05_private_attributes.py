# Python has no real "private". It has two conventions instead.
class Demo:
    def __init__(self):
        self.public = 1        # anybody may use it
        self._protected = 2    # convention: "internal, do not touch"
        self.__private = 3     # name mangling: becomes _Demo__private

    def show(self):
        print(self.public, self._protected, self.__private)


d = Demo()
d.show()

print(d.public)
print(d._protected)      # works: it is only a convention

# print(d.__private)     ->  AttributeError
print(d._Demo__private)  # it is still reachable if you really insist

# The double underscore is not a security feature: its real purpose is to
# avoid a name clash when a subclass uses the same attribute name.
print(d.__dict__)
