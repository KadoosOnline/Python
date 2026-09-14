# Small program: read a full name and print the initials, e.g. "Ali Rezaei" -> "A.R."
full_name = input('Enter your full name: ')

parts = full_name.strip().split(' ')

initials = ''
for part in parts:
    if part != '':                       # skip the extra spaces
        initials = initials + part[0].upper() + '.'

print('Initials:', initials)
