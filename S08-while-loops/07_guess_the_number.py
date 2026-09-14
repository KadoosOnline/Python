# A tiny game: the program knows a number, the player has to find it.
SECRET = 16

tries = 0

while True:
    user_input = input('Enter a number: ')
    guess = int(user_input)
    tries += 1

    if guess < SECRET:
        print('The number is greater!')
    elif guess > SECRET:
        print('The number is smaller!')
    else:
        print(f'You win! You needed {tries} tries.')
        break
