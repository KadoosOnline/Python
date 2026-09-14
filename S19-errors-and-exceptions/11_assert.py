# 'assert condition, message' stops the program with an AssertionError when the
# condition is False. It is a tool for the DEVELOPER, not for the user:
# it documents an assumption and catches a bug early.
def average(numbers: list[float]) -> float:
    assert len(numbers) > 0, 'average() needs at least one number'
    return sum(numbers) / len(numbers)


print(average([10, 20, 30]))

try:
    average([])
except AssertionError as e:
    print('AssertionError:', e)

# Careful: assertions disappear when Python is run with the -O option,
# so never use assert to validate what a USER typed - use if/raise for that.
