scores = [18, 12, 9, 20]

# any() -> True when AT LEAST ONE item is true
# all() -> True when EVERY item is true
print(any(score < 10 for score in scores))     # True: somebody failed
print(all(score >= 10 for score in scores))    # False

# The long version needed a loop and a flag:
has_failure = False
for score in scores:
    if score < 10:
        has_failure = True
        break
print(has_failure)

# sum() with a condition counts.
print(sum(1 for score in scores if score >= 10))   # how many passed
print(sum(score for score in scores if score >= 10))

# min/max with a key.
students = [{'name': 'Ali', 'score': 18}, {'name': 'Sara', 'score': 20}]
print(max(students, key=lambda s: s['score'])['name'])

# any()/all() stop as soon as the answer is known - they do not read the rest.
print(any(x > 2 for x in range(1_000_000)))
