# A variable created outside every function is "global": functions can READ it.
counter = 0

def show():
    print('counter is', counter)   # reading works without anything special

show()

# But ASSIGNING to it inside a function creates a NEW local variable,
# unless we declare it as global.
def increase_wrong():
    counter = 100                  # this is a local variable!
    print('local copy:', counter)

increase_wrong()
print('still:', counter)           # 0

def increase_right():
    global counter                 # now we really touch the global one
    counter += 1

increase_right()
increase_right()
print('after global:', counter)    # 2

# 'global' makes a program hard to follow. Prefer parameters and return values:
def increase(value):
    return value + 1

counter = increase(counter)
print('better style:', counter)
