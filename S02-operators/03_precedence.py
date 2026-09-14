# Python follows the usual mathematical order of operations:
#   1) **        2) * / // %        3) + -
# Operators on the same level are evaluated from left to right.

print(2 + 3 * 4)        # 14, not 20: multiplication happens first
print((2 + 3) * 4)      # 20: parentheses change the order
print(2 ** 3 ** 2)      # 512: ** is evaluated from RIGHT to left -> 2 ** 9
print(-3 ** 2)          # -9: the power is applied before the minus sign
print((-3) ** 2)        # 9

# When in doubt, add parentheses: they cost nothing and make the code readable.
