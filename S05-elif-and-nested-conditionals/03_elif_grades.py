# The ORDER of the branches matters. We test from the highest score downwards,
# so when we reach 'elif score >= 17' we already know the score is below 20.
user_input = input('Enter the score (0-20): ')
score = float(user_input)

if score > 20 or score < 0:
    print('Invalid score')
elif score >= 17:
    print('A - Excellent')
elif score >= 14:
    print('B - Good')
elif score >= 10:
    print('C - Passed')
else:
    print('F - Failed')
