from datetime import datetime, date

# The current date and time.
now = datetime.now()
print(now)
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)

# Only the date.
today = date.today()
print(today)

# Building a specific date.
birthday = date(2005, 3, 21)
print(birthday)

# strftime() turns a date into text the way we want it.
print(now.strftime('%Y/%m/%d'))
print(now.strftime('%d %B %Y'))
print(now.strftime('%H:%M:%S'))

# strptime() does the opposite: it reads a date out of a text.
parsed = datetime.strptime('2026-09-08', '%Y-%m-%d')
print(parsed)
