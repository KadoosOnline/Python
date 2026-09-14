# A classic use of // and % together:
# convert a number of seconds into hours, minutes and seconds.
user_input = input('Enter a number of seconds: ')
total_seconds = int(user_input)

hours = total_seconds // 3600            # how many whole hours
remaining = total_seconds % 3600         # what is left after removing the hours
minutes = remaining // 60                # how many whole minutes
seconds = remaining % 60                 # what is left after removing the minutes

print(hours, 'h', minutes, 'm', seconds, 's')
