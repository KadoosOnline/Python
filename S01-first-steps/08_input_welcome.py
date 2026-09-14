# Reading a value and using it inside a message.
user_input = input('Please enter your name: ')

# print() separates its arguments with a space by default.
print('Welcome', user_input, '!')

# With sep='' there is no space, so the exclamation mark sticks to the name.
print('Welcome ', user_input, '!', sep='')
