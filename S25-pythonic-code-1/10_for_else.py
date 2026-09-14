# The 'else' of a loop runs only when the loop was NOT stopped by a break.
# It is exactly what "I searched everything and found nothing" needs.
def main() -> None:
    for num in range(2, 30):
        for x in range(2, num):
            if num % x == 0:
                print(f'{num} = {x} * {num // x}')
                break
        else:
            print(f'{num} is prime!')

    # The same idea on a search.
    names = ['Ali', 'Sara', 'Reza']
    target = 'Omid'

    for name in names:
        if name == target:
            print('found!')
            break
    else:
        print(f'{target} is not in the list')


if __name__ == '__main__':
    main()
