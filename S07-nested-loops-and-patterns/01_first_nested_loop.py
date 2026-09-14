# The inner loop runs from start to end for EVERY single turn of the outer loop.
# 3 outer turns x 4 inner turns = 12 lines.
for i in range(3):
    for j in range(4):
        print(f'i={i}, j={j}')
    print('--- end of one outer turn ---')
