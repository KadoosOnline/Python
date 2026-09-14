# Combining 'and' and 'or'. The parentheses make the intention clear:
# (male AND older than 15) OR (female AND older than 9)
gender = input('Enter the gender (male / female): ')
age_input = input('Enter the age: ')
age = int(age_input)

if (gender == 'male' and age > 15) or (gender == 'female' and age > 9):
    print('She or he is ready to pray!')
else:
    print('Not ready yet.')
