# Arguments can be given BY NAME. Then the order does not matter any more,
# and the call becomes much easier to read.
def student_info(name, age, city):
    print(name, age, city)

student_info('Ali', 20, 'Rasht')                       # positional
student_info(age=20, name='Ali', city='Rasht')         # keyword, any order

# A long call is often written over several lines.
student_info(
    name='Ali',
    age=20,
    city='Rasht',
)
