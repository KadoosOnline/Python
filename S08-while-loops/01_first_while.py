# A 'while' repeats as long as its condition is True.
# Something inside the loop MUST eventually make the condition False,
# otherwise the program never stops (an "infinite loop").
x = 0

while x < 10:
    x += 1          # without this line the loop would never end
    print(x)
