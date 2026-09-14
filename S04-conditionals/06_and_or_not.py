# and -> True only when BOTH sides are True
# or  -> True when AT LEAST ONE side is True
# not -> reverses the value

age = 20
has_ticket = True

print(age >= 18 and has_ticket)     # True
print(age >= 18 or has_ticket)      # True
print(not has_ticket)               # False

# A very common pattern: is a value inside a range?
score = 15
if score >= 10 and score <= 20:
    print('Valid score')

# Python also allows the mathematical way of writing it:
if 10 <= score <= 20:
    print('Valid score (chained comparison)')
