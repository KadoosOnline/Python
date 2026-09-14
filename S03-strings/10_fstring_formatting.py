# f-strings can also control HOW a value is displayed.
price = 1234.5678
name = 'Ali'

print(f'{price:.2f}')      # 1234.57   -> two digits after the point
print(f'{price:10.2f}')    # right aligned in a field of 10 characters
print(f'{price:,.2f}')     # 1,234.57  -> thousands separator

print(f'{name:>10}|')      # right aligned
print(f'{name:<10}|')      # left aligned
print(f'{name:^10}|')      # centred

# '=' prints the expression and its value - very useful while debugging.
total = 42
print(f'{total = }')
