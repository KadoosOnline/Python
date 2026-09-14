# Taking a number apart digit by digit is a classic 'while' exercise.
user_input = input('Enter a positive number: ')
number = int(user_input)

digit_count = 0
digit_sum = 0

while number > 0:
    digit = number % 10       # the last digit
    digit_sum += digit
    digit_count += 1
    number = number // 10     # remove the last digit

print('Number of digits:', digit_count)
print('Sum of the digits:', digit_sum)
